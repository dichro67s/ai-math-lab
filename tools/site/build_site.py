#!/usr/bin/env python3
"""Regenerate the website's HTML pages (English at the root, Korean under ko/).

Usage (from anywhere):
  python3 tools/site/build_site.py              # all pages, both languages
  python3 tools/site/build_site.py news people  # only these pages

Edit the content in pages_en.py / pages_ko.py (and people.json, ag_block*.html),
then run this script. Afterwards run tools/update_leaderboard.py, because a
regenerated leaderboard page starts with an empty table.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pages_en  # noqa: E402
import pages_ko  # noqa: E402
from common import SITE  # noqa: E402

KEYS = ["home", "people", "publications", "projects", "benchmarks", "leaderboard", "news"]


def target(lang: str, key: str) -> Path:
    base = SITE / "ko" if lang == "ko" else SITE
    return base / ("index.html" if key == "home" else f"{key}/index.html")


def main(selected):
    for key in selected:
        for lang, module in (("en", pages_en), ("ko", pages_ko)):
            out = target(lang, key)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(getattr(module, key)(), encoding="utf-8")
            print("wrote", out.relative_to(SITE))


if __name__ == "__main__":
    wanted = sys.argv[1:] or KEYS
    unknown = [k for k in wanted if k not in KEYS]
    if unknown:
        sys.exit(f"unknown page(s): {unknown}; choose from {KEYS}")
    main(wanted)
