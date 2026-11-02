#!/usr/bin/env python3
"""Check README URLs for broken links — concurrent edition.

Usage:
    python3 check-broken-links.py           # check all READMEs
    python3 check-broken-links.py --sample  # quick sample (fast smoke test)

Outputs a report to broken-links-report.txt and prints a summary.
"""

import os
import re
import sys
import concurrent.futures
from collections import Counter

try:
    import requests
except ImportError:
    print("Error: 'requests' not installed. Run: pip install requests")
    sys.exit(1)

URL_PATTERN = re.compile(r'https?://[^\s"<>\)\]]+')
TIMEOUT = 8
WORKERS = 32
UA = {"User-Agent": "Mozilla/5.0 (MAX-HACK-TOOLS link-checker)"}


def iter_readmes():
    """Yield paths of README files (root + sources, no .git)."""
    for dirpath, dirnames, filenames in os.walk("."):
        if ".git" in dirpath.split(os.sep):
            continue
        for f in filenames:
            if f.lower().startswith("readme"):
                yield os.path.join(dirpath, f)


def extract_urls(path):
    """Extract unique URLs from a file."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return set(URL_PATTERN.findall(fh.read()))
    except OSError:
        return set()


def check_url(url):
    """Return (url, status_code_or_error)."""
    try:
        r = requests.head(url, timeout=TIMEOUT, allow_redirects=True, headers=UA)
        # Some servers reject HEAD; retry with GET (streamed)
        if r.status_code in (403, 405, 406, 501):
            r = requests.get(
                url, timeout=TIMEOUT, allow_redirects=True, headers=UA, stream=True
            )
        return url, r.status_code
    except requests.exceptions.Timeout:
        return url, "TIMEOUT"
    except requests.exceptions.SSLError:
        return url, "SSL_ERROR"
    except requests.exceptions.TooManyRedirects:
        return url, "TOO_MANY_REDIRECTS"
    except requests.exceptions.ConnectionError:
        return url, "CONNECTION_ERROR"
    except Exception as exc:  # noqa: BLE001
        return url, f"ERROR: {type(exc).__name__}"


def main():
    sample = "--sample" in sys.argv

    # Collect URL -> set of source files
    url_sources = {}
    n_readmes = 0
    for path in iter_readmes():
        n_readmes += 1
        for url in extract_urls(path):
            url_sources.setdefault(url, set()).add(path)

    urls = sorted(url_sources)
    if sample:
        urls = urls[:100]

    print(f"READMEs scanned: {n_readmes}")
    print(
        f"Unique URLs: {len(url_sources)}"
        + (f" (checking first {len(urls)})" if sample else "")
    )
    print(f"Checking with {WORKERS} workers, timeout {TIMEOUT}s...")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(check_url, u): u for u in urls}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            url, status = fut.result()
            results.append((url, status))
            done += 1
            if done % 50 == 0:
                print(f"  checked {done}/{len(urls)}...")

    # Classify
    broken = [
        (u, s)
        for u, s in results
        if isinstance(s, str) or (isinstance(s, int) and s >= 400)
    ]
    # 403/405 often = bot-blocking, not truly dead; flag separately
    blocked = [
        (u, s) for u, s in broken if isinstance(s, int) and s in (403, 405, 406, 429)
    ]
    dead = [(u, s) for u, s in broken if (u, s) not in blocked]

    status_counts = Counter()
    for _, s in results:
        status_counts[s] += 1

    with open("broken-links-report.txt", "w", encoding="utf-8") as out:
        out.write("# Broken Link Report — MAX-HACK-TOOLS\n")
        out.write(f"READMEs scanned: {n_readmes}\n")
        out.write(f"URLs checked: {len(results)}\n")
        out.write(f"Dead/broken: {len(dead)}\n")
        out.write(
            f"Blocked (403/405/406/429 — may be bot protection): {len(blocked)}\n\n"
        )

        out.write("## Status distribution\n")
        for st, cnt in status_counts.most_common():
            out.write(f"  {st}: {cnt}\n")

        out.write("\n## Dead/broken links\n")
        for u, s in sorted(dead, key=lambda x: str(x[1])):
            out.write(f"- [{s}] {u}\n")
            for src in sorted(url_sources.get(u, []))[:3]:
                out.write(f"    found in: {src}\n")

        out.write("\n## Blocked (verify manually)\n")
        for u, s in sorted(blocked, key=lambda x: str(x[1])):
            out.write(f"- [{s}] {u}\n")

    print()
    print(f"Status distribution: {dict(status_counts.most_common(8))}")
    print(f"Dead/broken: {len(dead)}")
    print(f"Blocked (403 etc): {len(blocked)}")
    print("Report written: broken-links-report.txt")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
