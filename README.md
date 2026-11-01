# SNU AI Mathematics Lab website

Static website of the SNU AI Mathematics Lab (Department of Mathematical Sciences,
Seoul National University), served by GitHub Pages from the `main` branch (root).

Live: https://dichro67s.github.io/ai-math-lab/

## Structure
- `index.html`: home (overview, highlights, research directions, latest news)
- `people/`: members, with photos in `assets/img/people/` (square JPEG, 320×320)
- `publications/`: papers, newest year first
- `papers/`: PDFs of the lab's papers and manuscripts, named `<author>-<year>-<topic>.pdf`
- `projects/`: current projects
- `benchmarks/`: ShadowBench, the ABM benchmark and the LIFT@Seoul evaluation server
- `leaderboard/`: ShadowBench results
- `news/`: announcements, newest first (the three latest also appear on the home page)
- `assets/`: stylesheet, images, favicon

English pages live at the root and Korean pages under `ko/` (same layout). Every
page has an English / 한국어 switch in the navigation bar.

## Editing content
The HTML pages are generated. Do not edit them by hand; edit the sources in
`tools/site/` and rebuild:

- `pages_en.py`, `pages_ko.py`: page text (news items are the `NEWS` list at the top)
- `people.json`: members (`name_ko`, `role_ko`, `links_ko` for the Korean page)
- `ag_block.html`, `ag_block_ko.html`: the worked example on the Benchmarks page
- `common.py`: navigation, footer, shared links, the "Updated" date

```bash
python3 tools/site/build_site.py          # rebuild every page in both languages
python3 tools/update_leaderboard.py       # then refill the leaderboard tables
```

## Updating the leaderboard
The leaderboard table mirrors the public ShadowBench leaderboard
(https://ldilab.github.io/shadowbench-leaderboard/). To refresh it:

```bash
python3 tools/update_leaderboard.py
```

This fetches the leaderboard data and rewrites only the table rows, the system count
and the "as of" date in `leaderboard/index.html` and `ko/leaderboard/index.html`. If a headline number changes, also
update the home page and the news page by hand.

## Publishing
Push to `main`; GitHub Pages redeploys in about a minute.
