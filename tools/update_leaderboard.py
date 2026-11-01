#!/usr/bin/env python3
"""Refresh the ShadowBench table on leaderboard/index.html.

Reads the public leaderboard data (the same JSON that
https://ldilab.github.io/shadowbench-leaderboard/ renders) and rewrites the
table rows and the "as of" date between the LB:* markers in the page.

Usage:
  python3 tools/update_leaderboard.py                # fetch the live JSON
  python3 tools/update_leaderboard.py results.json   # use a local copy
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

SOURCE_URL = "https://ldilab.github.io/shadowbench-leaderboard/data/paper_results.json"
PAGE = Path(__file__).resolve().parent.parent / "leaderboard" / "index.html"


def load(arg: str | None) -> dict:
    if arg:
        return json.loads(Path(arg).read_text(encoding="utf-8"))
    with urllib.request.urlopen(SOURCE_URL, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def kind(row: dict) -> str:
    if row.get("approach") == "agentic":
        return "Agentic"
    if row.get("approach") == "lean":
        return "Lean prover"
    return "Model · open" if row.get("weights") == "open" else "Model · closed"


def fmt(value) -> str:
    return "—" if value is None else f"{float(value):.1f}"


def build_rows(data: dict) -> str:
    rows = [r for r in data["rows"] if r.get("average")]
    rows.sort(key=lambda r: (-r["average"]["saPass"], -r["average"]["saPassSoft"],
                             -r["average"]["compile"], r["method"]))
    out = []
    for rank, row in enumerate(rows, 1):
        avg = row["average"]
        post = row.get("postPaper")
        if post:
            source = f'<span class="badge open" title="{html.escape(post.get("note", ""))}">After paper · {html.escape(post.get("date", ""))}</span>'
        else:
            source = '<span class="badge closed">Paper</span>'
        cls = ' class="top"' if rank <= 3 else ""
        out.append(
            f'          <tr{cls}><td class="num">{rank}</td><td>{html.escape(row["method"])}</td>'
            f'<td>{kind(row)}</td><td class="num">{fmt(avg["compile"])}</td>'
            f'<td class="num">{fmt(avg["saPassSoft"])}</td><td class="num"><strong>{fmt(avg["saPass"])}</strong></td>'
            f'<td class="num">{fmt(row.get("L3", {}).get("saPass"))}</td><td>{source}</td></tr>'
        )
    return "\n".join(out)


def replace_between(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- LB:{name}:START -->)(.*?)(<!-- LB:{name}:END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker LB:{name} not found in {PAGE}")
    return pattern.sub(lambda m: m.group(1) + body + m.group(3), text, count=1)


def main() -> None:
    data = load(sys.argv[1] if len(sys.argv) > 1 else None)
    page = PAGE.read_text(encoding="utf-8")
    page = replace_between(page, "ROWS", "\n" + build_rows(data) + "\n          ")
    page = replace_between(page, "ASOF", dt.date.today().isoformat())
    page = replace_between(page, "COUNT", str(len([r for r in data["rows"] if r.get("average")])))
    PAGE.write_text(page, encoding="utf-8")
    print(f"updated {PAGE} with {len(data['rows'])} rows")


if __name__ == "__main__":
    main()
