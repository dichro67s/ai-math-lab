"""Shared pieces of the site generator: links, page frame (nav + footer), helpers."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent          # repository root
PEOPLE_JSON = HERE / "people.json"
UPDATED = "2026-11-02"

ARXIV = "https://arxiv.org/abs/2608.29270"
GITHUB = "https://github.com/ldilab/shadowbench"
HF = "https://huggingface.co/datasets/DicoTiar/ShadowBench"
LB_PUBLIC = "https://ldilab.github.io/shadowbench-leaderboard/"
CODABENCH = "https://www.codabench.org/competitions/16295/"
LEAN4ALL = "https://dichro67s.github.io/lean4all/"
LEAN4ALL_CODE = "https://github.com/dichro67s/lean4all"
F4_CODE = "https://github.com/dongwook0826/FaugereF4"

# (label, href relative to the language root, page key)
NAV = {
    "en": [
        ("About", "index.html#about", None),
        ("Research", "index.html#research", None),
        ("People", "people/", "people"),
        ("Publications", "publications/", "publications"),
        ("Projects", "projects/", "projects"),
        ("Benchmarks", "benchmarks/", "benchmarks"),
        ("Leaderboard", "leaderboard/", "leaderboard"),
        ("News", "news/", "news"),
    ],
    "ko": [
        ("소개", "index.html#about", None),
        ("연구", "index.html#research", None),
        ("구성원", "people/", "people"),
        ("논문", "publications/", "publications"),
        ("프로젝트", "projects/", "projects"),
        ("벤치마크", "benchmarks/", "benchmarks"),
        ("리더보드", "leaderboard/", "leaderboard"),
        ("소식", "news/", "news"),
    ],
}

FOOTER = {
    "en": {"dept": "Department of Mathematical Sciences, Seoul National University", "updated": "Updated",
           "paper": "ShadowBench paper", "code": "Code", "lb": "Leaderboard", "switch": "한국어"},
    "ko": {"dept": "서울대학교 수리과학부", "updated": "업데이트",
           "paper": "ShadowBench 논문", "code": "Code", "lb": "리더보드", "switch": "English"},
}

KATEX = """
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}]});"></script>"""


def root(lang, key):
    """Relative path from a page back to the repository root."""
    depth = (0 if not key else 1) + (1 if lang == "ko" else 0)
    return "../" * depth


def wrap(*, title, desc, active, main, home=False, extra_head="", lang="en"):
    key = None if home else active
    p = root(lang, key)                       # to the repo root (assets)
    base = p + ("ko/" if lang == "ko" else "")  # to this language's root
    other = p + ("" if lang == "ko" else "ko/") + (f"{key}/" if key else "index.html")
    full_title = "SNU AI Mathematics Lab" if home else f"{title} — SNU AI Mathematics Lab"
    links = []
    for label, href, k in NAV[lang]:
        cur = ' aria-current="page"' if k and k == active else ""
        links.append(f'          <a href="{base}{href}"{cur}>{label}</a>')
    f = FOOTER[lang]
    links.append(f'          <a class="lang-switch" href="{other}" hreflang="{"en" if lang == "ko" else "ko"}">{f["switch"]}</a>')
    logo_cls = ' class="logo"' if home else ""
    small = "서울대학교" if lang == "ko" else "Seoul National University"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{full_title}</title>
  <meta name="description" content="{desc}" />
  <link rel="alternate" hreflang="{"en" if lang == "ko" else "ko"}" href="{other}" />
  <link rel="icon" type="image/png" href="{p}assets/img/favicon.png" />
  <link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png" />
  <link rel="stylesheet" href="{p}assets/css/style.css" />{extra_head}
</head>
<body>

  <div class="nav-wrap">
    <div class="container">
      <nav>
        <a class="brand" href="{base}index.html" aria-label="SNU AI Mathematics Lab home">
          <img src="{p}assets/img/logo.png"{logo_cls} alt="SNU AI Mathematics Lab logo" />
          <div class="brand-text">
            <span>SNU AI Mathematics Lab</span>
            <small>{small}</small>
          </div>
        </a>
        <div class="nav-links">
{chr(10).join(links)}
        </div>
      </nav>
    </div>
  </div>

{main}

  <footer class="footer">
    <div class="container">
      <div class="footer-box">
        <div>
          <strong>SNU AI Mathematics Lab</strong>
          <div class="footer-note">{f["dept"]} · {f["updated"]} {UPDATED}</div>
        </div>
        <div class="member-links">
          <a href="{ARXIV}">{f["paper"]}</a>
          <a href="{GITHUB}">{f["code"]}</a>
          <a href="{base}leaderboard/">{f["lb"]}</a>
          <a href="{LEAN4ALL}">Lean4All</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="{p}assets/js/main.js"></script>
</body>
</html>
"""


def page_hero(eyebrow, h1, text):
    return f"""  <section class="page-hero">
    <div class="container">
      <div class="page-hero-box">
        <div class="eyebrow">{eyebrow}</div>
        <h1 style="max-width:none; font-size:clamp(2rem,3vw,3.4rem);">{h1}</h1>
        <p>{text}</p>
      </div>
    </div>
  </section>"""


def news_items(items, p=""):
    return "\n".join(f"            <li><time>{d}</time><span>{t.replace('{P}', p)}</span></li>" for d, t in items)


def initials(name):
    parts = [w for w in name.replace("Dr.", "").replace("Prof.", "").split() if w[0].isupper()]
    return (parts[0][0] + parts[-1][0]) if len(parts) > 1 else parts[0][0]


def json_load(path):
    import json
    return json.loads(Path(path).read_text(encoding="utf-8"))
