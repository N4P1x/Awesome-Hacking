#!/usr/bin/env python3
"""Search index for MAX-HACK-TOOLS — keyword → source map (READMEs only)."""

import os, re
from collections import defaultdict

TERMS = [
    "osint",
    "pentest",
    "red team",
    "bug bounty",
    "reversing",
    "malware",
    "web",
    "cloud",
    "iot",
    "android",
    "firmware",
    "ctf",
    "forensics",
    "devsecops",
    "threat intel",
    "social engineering",
    "yara",
    "fuzzing",
    "honeypot",
    "vehicle",
    "drone",
    "ics",
    "mainframe",
    "password",
    "wireless",
    "sdr",
    "ai security",
    "llm",
    "prompt injection",
    "mcp",
    "autonomous",
]


def get_source(path):
    """Return the source directory name for a given path."""
    parts = path.split(os.sep)
    for i, p in enumerate(parts):
        if p == "sources" and i + 1 < len(parts):
            return parts[i + 1]
    return "root"


def is_readme(path):
    """Only index README files."""
    base = os.path.basename(path).lower()
    return base in ("readme.md", "readme", "readme.txt")


def main():
    terms = defaultdict(lambda: defaultdict(int))
    total_files = 0
    total_readmes = 0

    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for f in files:
            path = os.path.join(root, f)
            if not is_readme(path):
                continue
            total_readmes += 1
            try:
                text = open(path, errors="ignore", encoding="utf-8").read().lower()
                src = get_source(path)
                for term in TERMS:
                    count = text.count(term)
                    if count > 0:
                        terms[term][src] += count
            except Exception:
                pass
            total_files += 1

    print(f"=== MAX-HACK-TOOLS Search Index ===")
    print(f"README files indexed: {total_readmes}\n")

    for term in sorted(terms):
        hits = sorted(terms[term].items(), key=lambda x: -x[1])
        total = sum(c for _, c in hits)
        top = ", ".join(f"{n}({c})" for n, c in hits[:5])
        print(f"{term}: {total} hits across {len(hits)} sources → {top}")


if __name__ == "__main__":
    main()
