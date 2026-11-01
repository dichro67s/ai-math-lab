#!/usr/bin/env python3
"""Refresh the ShadowBench table on leaderboard/index.html and ko/leaderboard/index.html.

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
SITE = Path(__file__).resolve().parent.parent
PAGES = {"en": SITE / "leaderboard" / "index.html", "ko": SITE / "ko" / "leaderboard" / "index.html"}
LABELS = {
    "en": {"Agentic": "Agentic", "Lean prover": "Lean prover", "Model · open": "Model · open",
           "Model · closed": "Model · closed", "paper": "Paper", "after": "After paper"},
    "ko": {"Agentic": "에이전트", "Lean prover": "Lean prover", "Model · open": "모델 · 공개 가중치",
           "Model · closed": "모델 · 비공개", "paper": "논문", "after": "논문 이후"},
}


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


def build_rows(data: dict, lang: str = "en") -> str:
    labels = LABELS[lang]
    rows = [r for r in data["rows"] if r.get("average")]
    rows.sort(key=lambda r: (-r["average"]["saPass"], -r["average"]["saPassSoft"],
                             -r["average"]["compile"], r["method"]))
    out = []
    for rank, row in enumerate(rows, 1):
        avg = row["average"]
        post = row.get("postPaper")
        if post:
            source = f'<span class="badge open" title="{html.escape(post.get("note", ""))}">{labels["after"]} · {html.escape(post.get("date", ""))}</span>'
        else:
            source = f'<span class="badge closed">{labels["paper"]}</span>'
        cls = ' class="top"' if rank <= 3 else ""
        out.append(
            f'          <tr{cls}><td class="num">{rank}</td><td>{html.escape(row["method"])}</td>'
            f'<td>{labels[kind(row)]}</td><td class="num">{fmt(avg["compile"])}</td>'
            f'<td class="num">{fmt(avg["saPassSoft"])}</td><td class="num"><strong>{fmt(avg["saPass"])}</strong></td>'
            f'<td class="num">{fmt(row.get("L3", {}).get("saPass"))}</td><td>{source}</td></tr>'
        )
    return "\n".join(out)


def replace_between(text: str, name: str, body: str, page: Path) -> str:
    pattern = re.compile(rf"(<!-- LB:{name}:START -->)(.*?)(<!-- LB:{name}:END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker LB:{name} not found in {page}")
    return pattern.sub(lambda m: m.group(1) + body + m.group(3), text, count=1)


def main() -> None:
    data = load(sys.argv[1] if len(sys.argv) > 1 else None)
    count = str(len([r for r in data["rows"] if r.get("average")]))
    for lang, path in PAGES.items():
        if not path.exists():
            print(f"skipped {path} (missing)")
            continue
        page = path.read_text(encoding="utf-8")
        page = replace_between(page, "ROWS", "\n" + build_rows(data, lang) + "\n          ", path)
        page = replace_between(page, "ASOF", dt.date.today().isoformat(), path)
        page = replace_between(page, "COUNT", count, path)
        path.write_text(page, encoding="utf-8")
        print(f"updated {path.relative_to(SITE)} with {count} rows")


if __name__ == "__main__":
    main()
