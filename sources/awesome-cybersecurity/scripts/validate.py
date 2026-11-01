#!/usr/bin/env python3
"""Consistency checks for README.md (English) and OKUBENI.md (Turkish).

Checks, per file:
  * every Markdown table has the same number of columns on every row
  * every in-page anchor (#id) points to an existing <a id="...">
  * the `resources-N` badge equals the real number of resource rows
  * no resource appears twice in the same section
Then across files:
  * both files list the same resources (matched by URL) in the same sections
Exit code 1 if anything is wrong.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = ["README.md", "OKUBENI.md"]
ROW = re.compile(r"^\| .+? \| (?:⚔️🛡️|⚔️|🛡️|🏛️|🧩) ")
URL = re.compile(r"\]\((https?://[^)\s]+)\)")
errors = []


def err(msg):
    errors.append(msg)


def parse(name):
    text = (ROOT / name).read_text(encoding="utf-8")
    lines = text.split("\n")
    ids = set(re.findall(r'<a id="([^"]+)"', text)) | {"top"}

    # anchors
    for a in re.findall(r'href="#([^"]+)"', text) + re.findall(r"\]\(#([^)]+)\)", text):
        if a not in ids:
            err(f"{name}: broken anchor #{a}")

    # table column consistency
    cols = None
    for i, ln in enumerate(lines, 1):
        if ln.startswith("|"):
            n = len(ln.strip().strip("|").split("|"))
            if cols is None:
                cols = n
            elif n != cols:
                err(f"{name}:{i}: expected {cols} columns, found {n}")
        else:
            cols = None

    # resources per section
    sections, current, started = {}, None, False
    for ln in lines:
        m = re.match(r'<a id="([^"]+)"></a>', ln)
        if m:
            current = m.group(1)
            started = started or current == "fundamentals"
            if current == "ethics":
                break
            if started:
                sections.setdefault(current, [])
            continue
        if started and current and ROW.match(ln):
            first = ln.strip().strip("|").split("|")[0].strip()
            urls = URL.findall(first)
            # rows without a link are matched by count (their names are translated)
            sections[current].append(tuple(urls) if urls else ("(no link)",))

    total = sum(len(v) for v in sections.values())
    badge = re.search(r"badge/resources-(\d+)-", text)
    if not badge or int(badge.group(1)) != total:
        err(f"{name}: resources badge says {badge.group(1) if badge else '?'} but {total} rows found")

    for sec, rows in sections.items():
        seen = set()
        for r in rows:
            if r != ("(no link)",) and r in seen:
                err(f"{name}: duplicate resource in '{sec}': {r}")
            seen.add(r)
    return sections, total


results = {n: parse(n) for n in FILES}
a, b = (results[n][0] for n in FILES)
for sec in sorted(set(a) | set(b)):
    if len(a.get(sec, [])) != len(b.get(sec, [])):
        err(f"'{sec}': {FILES[0]} has {len(a.get(sec, []))} rows, {FILES[1]} has {len(b.get(sec, []))}")
    sa, sb = set(a.get(sec, [])), set(b.get(sec, []))
    for r in sorted(sa - sb):
        err(f"'{sec}': in {FILES[0]} but missing from {FILES[1]}: {r}")
    for r in sorted(sb - sa):
        err(f"'{sec}': in {FILES[1]} but missing from {FILES[0]}: {r}")

if errors:
    print("Validation failed:\n")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)
print(f"OK: {results[FILES[0]][1]} resources, both files consistent.")
