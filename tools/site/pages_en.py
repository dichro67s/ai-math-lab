"""English pages of the lab website."""
from pathlib import Path

from common import (ARXIV, CODABENCH, F4_CODE, GITHUB, HF, KATEX, LB_PUBLIC, LEAN4ALL, LEAN4ALL_CODE, UPDATED,
                    PEOPLE_JSON, initials, json_load, news_items, page_hero, wrap)

# ---------------------------------------------------------------- news (shared)
NEWS = [
    ("2026-11", "Lab website relaunched with our benchmark, leaderboard and publications."),
    ("2026-11", f'<strong><a href="{LEAN4ALL}">Lean4All</a></strong> is online: an open platform for formalizing mathematics in Lean&nbsp;4 with AI agents. It works through GitHub, offers blueprints, and sets up missions from an arXiv paper or an uploaded file; Lean checks every proof.'),
    ("2026-10-26", "<strong>New manuscript:</strong> Dongwook Cheon, <a href=\"{P}publications/\">Formalizing Faugère's F<sub>4</sub> Algorithm in Lean&nbsp;4</a>. The formalized F<sub>4</sub> procedure provably terminates and returns a Gröbner basis of the input ideal. <a href=\"https://github.com/dongwook0826/FaugereF4\">Code</a>."),
    ("2026-10-20", "<strong>Leaderboard update.</strong> New agentic results on ShadowBench: Codex (GPT-6.1 Sol) with Numina-Lean-Agent reaches 18.5% SA-Pass, the best so far. Claude Code (Opus 5.5) with Numina-Lean-Agent compiles 93.8% of its outputs, yet only 16.9% pass SA-Pass."),
    ("2026-10-14", "<strong>Leaderboard update.</strong> Frontier models prompted directly (Claude Opus 5.5, Sonnet 5.5, Fable 5.1; GPT-6 Sol, Luna, Astra) compile up to 38.2% of their outputs but reach at most 1.1% SA-Pass."),
    ("2026-09", "<strong>ShadowBench</strong> will appear at <strong>EMNLP 2026</strong>."),
    ("2026-08-29", f'ShadowBench preprint posted on arXiv (<a href="{ARXIV}">2608.29270</a>), with <a href="{GITHUB}">code</a>, the <a href="{HF}">public dataset</a> and a <a href="{LB_PUBLIC}">public leaderboard</a>.'),
    ("2026-04 – 06", f'An early 126-problem version of ShadowBench was <a href="{CODABENCH}">Track 4 of the ICML 2026 AI for Math Workshop &amp; Challenge</a>: end-to-end autoformalization and proving in Lean 4. About 117 teams registered and 27 took part.'),
]



# ---------------------------------------------------------------- home
def home():
    main = f"""  <main id="top">
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-card">
          <div class="eyebrow">AI × Mathematics</div>
          <h1>SNU AI Mathematics Lab</h1>
          <p>
            We build AI systems that read, formalize and check mathematics. Our main focus is
            autoformalization: translating mathematics written by people into Lean&nbsp;4, a language
            in which a computer can verify every step, and measuring rigorously whether the
            translation says what the mathematician meant.
          </p>
          <p style="margin-top: 14px;">
            We build the benchmarks, checkers and leaderboards this needs, and study the systems
            that solve, generate and verify mathematics.
          </p>
          <div class="korean-name">Department of Mathematical Sciences, Seoul National University</div>
          <div class="hero-actions">
            <a class="btn primary" href="benchmarks/">ShadowBench</a>
            <a class="btn secondary" href="leaderboard/">Leaderboard</a>
            <a class="btn secondary" href="people/">Meet the team</a>
          </div>
        </div>

        <div class="hero-side">
          <div class="mini-panel metric">
            <span>New · EMNLP 2026</span>
            <strong>ShadowBench</strong>
            <span>A Lean&nbsp;4 benchmark that checks whether a formal statement means what the theorem says, not just whether it compiles. <a class="text-link" href="{ARXIV}">Read the paper</a></span>
          </div>
          <div class="mini-panel">
            <h3 style="margin-bottom: 8px;">Compiling is not understanding</h3>
            <p style="margin: 0;">The best systems now produce Lean that compiles for over 90% of our problems, yet at most 18.5% state the intended theorem.</p>
          </div>
          <div class="mini-panel">
            <h3 style="margin-bottom: 8px;">Lab lead</h3>
            <p style="margin: 0;">David Donghoon Hyeon, Professor of Mathematical Sciences, Seoul National University.</p>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="stat-grid">
          <div class="stat"><strong>178</strong><span>postgraduate- to research-level problems in ShadowBench</span></div>
          <div class="stat"><strong>706</strong><span>hidden shadow theorems, each checked by Lean</span></div>
          <div class="stat"><strong>98.8%</strong><span>agreement of SA-Pass with expert judgments</span></div>
          <div class="stat"><strong>41</strong><span>systems on the public leaderboard</span></div>
        </div>
      </div>
    </section>

    <section id="highlights">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">Highlights</div>
            <h2>Current work</h2>
          </div>
          <p>Benchmarks, checkers and results that are public now.</p>
        </div>
        <div class="feature-grid">
          <article class="panel feature">
            <span class="tag">Benchmark · EMNLP 2026</span>
            <h3>ShadowBench and SA-Pass</h3>
            <p>Each problem carries hidden auxiliary theorems, called shadows. A generated statement earns credit only if Lean proves it implies every shadow and that the shadows together imply it.</p>
            <a class="more" href="benchmarks/#shadowbench">How it works →</a>
          </article>
          <article class="panel feature">
            <span class="tag">Leaderboard</span>
            <h3>41 systems evaluated</h3>
            <p>Agentic coding assistants with and without Lean tools, frontier and open models, and Lean-specialized provers, all scored on the same 178 problems.</p>
            <a class="more" href="leaderboard/">See the results →</a>
          </article>
          <article class="panel feature">
            <span class="tag">Challenge · ICML 2026</span>
            <h3>AI for Math, Track 4</h3>
            <p>An early version of ShadowBench was the benchmark for Track 4 of the ICML 2026 AI for Math Challenge. About 117 teams registered.</p>
            <a class="more" href="news/">News →</a>
          </article>
        </div>
      </div>
    </section>

    <section id="about">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">About</div>
            <h2>Research at the intersection of AI and mathematics</h2>
          </div>
          <p>
            SNU AI Mathematics Lab studies how machines can formalize, solve, generate and verify
            mathematical knowledge.
          </p>
        </div>

        <div class="about-grid">
          <div class="panel">
            <h3>Lab overview</h3>
            <p>
              Large language models can now write Lean code that compiles, but a statement that compiles
              can still say the wrong thing: a hypothesis dropped, a conclusion weakened, a quantity
              assumed instead of computed. Our work makes that gap measurable. We write benchmark
              problems from graduate textbooks and recent research papers, build hidden checkers that
              Lean itself verifies, run public evaluations, and develop methods to judge whether a
              formalization is faithful when no reference exists.
            </p>
          </div>
          <div class="panel">
            <h3>Quick links</h3>
            <ul class="clean-list">
              <li><a class="text-link" href="publications/">Publications</a></li>
              <li><a class="text-link" href="benchmarks/">ShadowBench, ABM and LIFT@Seoul</a></li>
              <li><a class="text-link" href="leaderboard/">Leaderboard</a></li>
              <li><a class="text-link" href="{HF}">Dataset on Hugging Face</a></li>
              <li><a class="text-link" href="{LEAN4ALL}">Lean4All: open, agent-powered formalization</a></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="research">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">Research</div>
            <h2>Main research directions</h2>
          </div>
          <p>
            Six directions, connected by one question: how do we know an AI system got the mathematics right?
          </p>
        </div>

        <div class="research-grid">
          <article class="panel research-card"><span class="tag">01</span><h3>Autoformalization</h3><p>Translating textbook and research mathematics into Lean&nbsp;4 statements and proofs, from graduate algebra, analysis, topology and algebraic geometry to recent arXiv papers.</p></article>
          <article class="panel research-card"><span class="tag">02</span><h3>Benchmarks &amp; Leaderboards</h3><p>ShadowBench, the larger in-house ABM collection, and LIFT@Seoul, our sandboxed evaluation server, with a public leaderboard.</p></article>
          <article class="panel research-card"><span class="tag">03</span><h3>Semantic Alignment &amp; Verification</h3><p>Deciding whether a formal statement means what the informal one says: hidden shadow checks in both directions, and judging alignment when no reference formalization exists.</p></article>
          <article class="panel research-card"><span class="tag">04</span><h3>Automated Problem Solving</h3><p>Studying agentic systems that write, compile and repair Lean in a loop, and where they still fail to state the intended theorem.</p></article>
          <article class="panel research-card"><span class="tag">05</span><h3>Automated Problem Generation</h3><p>Turning papers and textbooks into benchmark problems with reference Lean files and checkers, drafted by models and reviewed by mathematicians.</p></article>
          <article class="panel research-card"><span class="tag">06</span><h3>Theorem Generation</h3><p>Exploring models that propose meaningful conjectures, lemmas and theorems in forms a proof assistant can check.</p></article>
        </div>
      </div>
    </section>

    <section id="news">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">News</div>
            <h2>Latest</h2>
          </div>
          <p><a class="text-link" href="news/">All news →</a></p>
        </div>
        <div class="panel">
          <ul class="news-list">
{news_items(NEWS[1:4])}
          </ul>
        </div>
      </div>
    </section>
  </main>"""
    return wrap(title="", desc="SNU AI Mathematics Lab: autoformalization, Lean 4 benchmarks and semantic verification of AI-generated mathematics.", active=None, main=main, home=True)


# ---------------------------------------------------------------- benchmarks
AG_BLOCK = Path(__file__).with_name("ag_block.html").read_text()


def benchmarks():
    main = f"""<main>
{page_hero("Benchmarks", "Benchmarks", "We build benchmarks that test whether AI systems formalize mathematics faithfully, not only whether their Lean code compiles.")}

  <section id="shadowbench">
    <div class="container stack">
      <div class="section-head">
        <div>
          <div class="eyebrow">EMNLP 2026</div>
          <h2>ShadowBench</h2>
        </div>
        <p>A Lean&nbsp;4 full-autoformalization benchmark of 178 postgraduate- to research-level problems across eight areas of mathematics, scored with SA-Pass.</p>
      </div>

      <div class="two-col">
        <div class="panel">
          <h3>The problem with compile rate</h3>
          <p>
            A model's Lean statement can compile and still be wrong: it may weaken the conclusion, drop a
            hypothesis, or assume what it should prove. Compile rate counts all of these as correct.
            Comparing against one reference formalization has the opposite flaw: it rejects correct
            statements written in a different but equivalent way.
          </p>
          <p>
            SA-Pass (Semantic Alignment Pass) takes the idea of unit tests from code generation. For each
            problem, experts fix a small set of auxiliary Lean statements, called <strong>shadows</strong>,
            that together characterize the intended theorem. The shadows stay hidden on the evaluation
            server, and Lean grades any submission against them automatically.
          </p>
        </div>
        <div class="panel">
          <h3>Resources</h3>
          <ul class="clean-list">
            <li><a href="{ARXIV}">Paper (arXiv 2608.29270)</a></li>
            <li><a href="{GITHUB}">Code (GitHub)</a></li>
            <li><a href="{HF}">Dataset (Hugging Face, CC BY 4.0)</a></li>
            <li><a href="{LB_PUBLIC}">Public leaderboard and submissions</a></li>
            <li><a href="{CODABENCH}">ICML 2026 AI for Math Challenge, Track 4</a></li>
          </ul>
        </div>
      </div>

      <div class="stat-grid">
        <div class="stat"><strong>178</strong><span>problems: 113 at level&nbsp;1, 52 at level&nbsp;2, 13 at level&nbsp;3 (research level)</span></div>
        <div class="stat"><strong>8</strong><span>areas of mathematics</span></div>
        <div class="stat"><strong>706</strong><span>shadows: 513 forward and 193 backward checks</span></div>
        <div class="stat"><strong>98.8%</strong><span>agreement with expert judgments (precision 1.000, recall 0.930)</span></div>
      </div>

      <div class="two-col">
        <div class="panel">
          <h3>How SA-Pass scores a statement</h3>
          <ol class="steps">
            <li><span><strong>Compile.</strong> The generated Lean file must compile on its own against Mathlib, with no <code class="inline">sorry</code>.</span></li>
            <li><span><strong>Forward checks.</strong> Lean must prove that the statement implies every shadow. This catches weakened or partial statements.</span></li>
            <li><span><strong>Backward check.</strong> Lean must prove that the shadows together imply the statement. This catches extra conclusions and dropped hypotheses.</span></li>
            <li><span><strong>Score.</strong> SA-Pass is 1 only if all checks pass. SA-Pass<sub>soft</sub> gives partial credit: half for the share of forward checks passed, half for the backward check.</span></li>
          </ol>
        </div>
        <div class="panel">
          <h3>Problems by area</h3>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Area</th><th class="num">Problems</th></tr></thead>
              <tbody>
                <tr><td>Analysis</td><td class="num">28</td></tr>
                <tr><td>Algebra</td><td class="num">26</td></tr>
                <tr><td>Topology</td><td class="num">25</td></tr>
                <tr><td>Geometry</td><td class="num">24</td></tr>
                <tr><td>Algebraic geometry</td><td class="num">22</td></tr>
                <tr><td>Probability</td><td class="num">20</td></tr>
                <tr><td>Number theory</td><td class="num">19</td></tr>
                <tr><td>Combinatorics</td><td class="num">14</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

{AG_BLOCK}      <div class="panel">
        <h3>What we found</h3>
        <ul class="clean-list">
          <li><strong>Compilation overestimates alignment.</strong> In the paper, the best system (Claude Code with Opus 4.8 and Numina-Lean-Agent) compiles 61.8% of problems but reaches 11.2% SA-Pass. Newer systems compile over 90% and reach at most 18.5%.</li>
          <li><strong>Lean tooling helps compile more than meaning.</strong> Adding Numina-Lean-Agent raised Opus&nbsp;4.8's compile rate by 41.6 points but its SA-Pass by only 8.4.</li>
          <li><strong>Direct prompting is far behind.</strong> Every closed, open and Lean-specialized model in the paper scored 0.0 SA-Pass when prompted directly.</li>
          <li><strong>SA-Pass matches expert judgment.</strong> On compile-passed outputs from six agentic configurations, SA-Pass agrees with experts on 98.8% of cases (BEq+: 80.6%; compile check: 17.8%).</li>
        </ul>
      </div>

      <div class="panel">
        <h3>How it was built</h3>
        <p>Problems come from graduate textbooks (Lee, <em>Introduction to Smooth Manifolds</em>; Stein–Shakarchi, <em>Real Analysis</em>; Cox–Little–O'Shea, <em>Ideals, Varieties, and Algorithms</em>; Boyd–Vandenberghe, <em>Convex Optimization</em>; Wunsch, <em>Complex Variables with Applications</em>; EGA; <em>Proofs from THE BOOK</em>), the Stacks Project, theorems missing from Wiedijk's 1000+ list, the "PRIMES is in P" paper and Mathlib&nbsp;4. A language model drafts each problem's shadows, and for 85% of problems the first draft is already complete. Mathematicians review every set, and Lean checks that the shadows together characterize the reference statement. Building the checkers takes about ten minutes per problem on average.</p>
      </div>
    </div>
  </section>

  <section id="abm">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="eyebrow">In development</div>
          <h2>ABM: Autoformalization Benchmark</h2>
        </div>
        <p>Our larger in-house collection, from which ShadowBench was drawn.</p>
      </div>
      <div class="simple-grid">
        <div class="panel">
          <h3>What it contains</h3>
          <p>More than 1,200 Lean&nbsp;4 problems. About 370 were written by the lab across ten areas, from graduate textbooks, the KMS College Mathematics Competition and 38 recent arXiv papers. The rest are miniF2F and ProofNet problems, re-checked under a current Lean and Mathlib. Lab-written problems come with reference Lean files and, for many, hidden forward and backward checkers.</p>
        </div>
        <div class="panel">
          <h3>Levels</h3>
          <ul class="clean-list">
            <li><strong>L1:</strong> definitions and statements, no proofs.</li>
            <li><strong>L2:</strong> statements with short, direct proofs.</li>
            <li><strong>L3:</strong> clusters of definitions and lemmas leading to a main theorem.</li>
            <li><strong>L4:</strong> research-level results.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="lift">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="eyebrow">Evaluation server</div>
          <h2>LIFT@Seoul</h2>
        </div>
        <p>Lean4 Inference and Formalization Test @ Seoul National University.</p>
      </div>
      <div class="panel">
        <p>LIFT@Seoul is the lab's evaluation server. It sends each problem to a model or agent, compiles the returned Lean file in a network-isolated sandbox against a pinned Lean and Mathlib, and rejects files that use <code class="inline">sorry</code>, add axioms or change the target statement. It then runs the hidden forward and backward checkers and reports results by area and level. It is currently open to lab members and collaborators.</p>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="Benchmarks", desc="ShadowBench, the ABM autoformalization benchmark and the LIFT@Seoul evaluation server.", active="benchmarks", main=main, extra_head=KATEX)


# ---------------------------------------------------------------- leaderboard
def leaderboard():
    main = f"""<main>
{page_hero("Leaderboard", "ShadowBench leaderboard", f'Results on the 178-problem ShadowBench test split, sorted by SA-Pass. Mirrored from the <a href="{LB_PUBLIC}">public leaderboard</a>, as of <!-- LB:ASOF:START -->{UPDATED}<!-- LB:ASOF:END -->.')}

  <section>
    <div class="container stack">
      <div class="feature-grid">
        <div class="panel"><h3>Compile</h3><p>Share of problems whose generated Lean code compiles on its own, with no <code class="inline">sorry</code>.</p></div>
        <div class="panel"><h3>SA-Pass<sub>soft</sub></h3><p>Partial credit: half for the share of forward checks passed, half for the backward check. Non-compiling outputs score zero.</p></div>
        <div class="panel"><h3>SA-Pass</h3><p>Share of problems that compile and pass every forward and backward check: the statement means what the theorem says.</p></div>
      </div>

      <div class="panel table-wrap">
        <table>
          <thead><tr><th class="num">#</th><th>System</th><th>Type</th><th class="num">Compile</th><th class="num">SA-Pass<sub>soft</sub></th><th class="num">SA-Pass</th><th class="num">L3 SA-Pass</th><th>Source</th></tr></thead>
          <tbody><!-- LB:ROWS:START --><!-- LB:ROWS:END --></tbody>
        </table>
      </div>

      <div class="panel">
        <p class="note">All values are percentages over the same 178 problems (<!-- LB:COUNT:START -->0<!-- LB:COUNT:END --> systems). "Paper" rows are Table&nbsp;3 of the <a href="{ARXIV}">ShadowBench paper</a>. "After paper" rows were run later on the same problems: agentic systems on 2026-10-20, and direct prompting with up to 128k output tokens on 2026-10-14 (the paper used 2k–8k). In those runs one problem has no record and counts as a failure. "+ Numina" means the agent could use Numina-Lean-Agent's Lean tools. L3 is the 13 research-level problems.</p>
        <p class="note">To submit a system, use the <a href="{LB_PUBLIC}">public leaderboard</a>.</p>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="Leaderboard", desc="ShadowBench leaderboard: compile rate and SA-Pass for 41 systems on 178 problems.", active="leaderboard", main=main)


# ---------------------------------------------------------------- publications
def publications():
    authors = ("<strong>Hojae Han</strong>*, <strong>Jongyoon Kim</strong>*, <strong>Sanghyeok Park</strong>*, "
               "<strong>Dongwook Cheon</strong>, <strong>Yeachan Park</strong>, <strong>Myeong Jae Jeon</strong>, "
               "<strong>Sunjong Choe</strong>, Soonho Kong, Wonseok Hur, Seung-won Hwang†, <strong>Donghoon Hyeon</strong>†")
    bib = """@inproceedings{han2026shadowbench,
  title     = {ShadowBench: Toward Reliable Automatic Evaluation of
               Semantic Alignment in Autoformalization},
  author    = {Han, Hojae and Kim, Jongyoon and Park, Sanghyeok and
               Cheon, Dongwook and Park, Yeachan and Jeon, Myeong Jae and
               Choe, Sunjong and Kong, Soonho and Hur, Wonseok and
               Hwang, Seung-won and Hyeon, Donghoon},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods
               in Natural Language Processing (EMNLP)},
  year      = {2026},
  note      = {arXiv:2608.29270}
}"""
    F4_PDF = "../papers/cheon-2026-f4-lean4.pdf"
    F4_CODE = "https://github.com/dongwook0826/FaugereF4"
    f4_bib = """@unpublished{cheon2026f4,
  title  = {Formalizing Faug{\\`e}re's {F}$_4$ Algorithm in {Lean} 4},
  author = {Cheon, Dongwook},
  note   = {Manuscript},
  year   = {2026},
  url    = {https://github.com/dongwook0826/FaugereF4}
}"""
    main = f"""<main>
{page_hero("Publications", "Publications", "Papers from the lab. Lab members are in bold.")}
  <section>
    <div class="container stack">
      <div class="panel">
        <h3>2026</h3>
        <div class="pub">
          <div class="pub-title">ShadowBench: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization</div>
          <div class="pub-authors">{authors}</div>
          <div class="pub-venue"><em>EMNLP 2026</em> · arXiv:2608.29270 · * equal contribution, † corresponding authors</div>
          <p style="margin:6px 0 0;">Introduces SA-Pass, which scores a formal statement by Lean-checked implications to and from hidden auxiliary theorems (shadows), and ShadowBench, 178 postgraduate- to research-level Lean&nbsp;4 problems. SA-Pass agrees with expert judgments on 98.8% of cases; the best system in the paper compiles 61.8% but reaches 11.2% SA-Pass.</p>
          <div class="pub-links">
            <a class="badge closed" href="{ARXIV}">arXiv</a>
            <a class="badge closed" href="{GITHUB}">Code</a>
            <a class="badge closed" href="{HF}">Dataset</a>
            <a class="badge closed" href="{LB_PUBLIC}">Leaderboard</a>
          </div>
          <details style="margin-top:8px;"><summary class="note" style="cursor:pointer;">BibTeX</summary><pre class="code" style="margin-top:8px;">{bib}</pre></details>
        </div>
        <div class="pub">
          <div class="pub-title">Formalizing Faugère's F<sub>4</sub> Algorithm in Lean&nbsp;4</div>
          <div class="pub-authors"><strong>Dongwook Cheon</strong></div>
          <div class="pub-venue"><em>Manuscript</em> · October 2026</div>
          <p style="margin:6px 0 0;">A Lean&nbsp;4 formalization of Faugère's F<sub>4</sub> algorithm over Mathlib's multivariate polynomials. For every finite set \\(F\\) of nonzero polynomials over a field in finitely many variables, the procedure terminates and returns a finite set \\(G\\) with \\(\\langle G\\rangle = \\langle F\\rangle\\) and \\(\\langle \\mathrm{{LM}}(g) : g \\in G\\rangle = \\mathrm{{in}}_\\prec(\\langle F\\rangle)\\), so \\(G\\) is a Gröbner basis (theorem <code class="inline">F4_groebner</code>). Symbolic preprocessing and Gaussian elimination work directly on finite sets of polynomials; termination uses a lexicographic well-founded relation. The checked results use only Lean's three standard axioms, with no <code class="inline">sorry</code>.</p>
          <div class="pub-links">
            <a class="badge closed" href="{F4_PDF}">PDF</a>
            <a class="badge closed" href="{F4_CODE}">Code</a>
          </div>
          <details style="margin-top:8px;"><summary class="note" style="cursor:pointer;">BibTeX</summary><pre class="code" style="margin-top:8px;">{f4_bib}</pre></details>
        </div>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="Publications", desc="Publications of the SNU AI Mathematics Lab.", active="publications", main=main, extra_head=KATEX)


# ---------------------------------------------------------------- projects
def projects():
    cards = [
        ("Published", "open", "ShadowBench and SA-Pass",
         "A benchmark and metric that check whether a formal statement means what the theorem says, using hidden shadow theorems verified by Lean in both directions.",
         '<a href="../benchmarks/#shadowbench">Benchmark</a><a href="' + ARXIV + '">Paper</a><a href="' + GITHUB + '">Code</a>'),
        ("Live", "open", "Lean4All",
         "An open, agent-powered platform for formalizing mathematics in Lean&nbsp;4. Contributors prove a mission's theorems with their own AI agents, the work goes through GitHub, and Lean checks every proof. Blueprints show how the definitions and lemmas of a formalization depend on one another. A mission can be set up from an arXiv paper in a few steps, or from an uploaded file. Lean4All is a standalone platform, inspired by Prove2Me, with a Korean interface.",
         '<a href="' + LEAN4ALL + '">Open the site</a><a href="' + LEAN4ALL_CODE + '">Code</a>'),
        ("Ongoing", "closed", "ABM: Autoformalization Benchmark",
         "Our in-house collection of more than 1,200 Lean&nbsp;4 problems, with about 370 written by the lab from textbooks, competitions and recent arXiv papers.",
         '<a href="../benchmarks/#abm">Details</a>'),
        ("Ongoing", "closed", "LIFT@Seoul evaluation server",
         "Sandboxed, two-phase evaluation of models and agents: Lean compilation first, then hidden forward and backward checks, reported by area and level.",
         '<a href="../benchmarks/#lift">Details</a>'),
        ("Ongoing", "closed", "Alignment without a reference",
         "Most real formalizations have no reference to compare against. We build judges that work from the informal and formal statements alone: extract the objects and claims each one makes, match them, and look for a concrete instance that separates the two when they differ.",
         ""),
        ("Ongoing", "closed", "Shadows for proofs and code",
         "Extending shadow checks beyond statements: to proofs (does the formal proof establish the steps the informal proof claims?) and to programs (do two programs behave the same?).",
         ""),
        ("Ongoing", "closed", "Formalizing a growing library",
         "Formalization targets drawn from the Stacks Project, where each statement builds on earlier ones, to test autoformalization as a library grows.",
         ""),
    ]
    html_cards = []
    for status, cls, title, text, links in cards:
        link_html = f'<div class="member-links">{links}</div>' if links else ""
        html_cards.append(f"""      <article class="panel feature">
        <span class="badge {cls}">{status}</span>
        <h3>{title}</h3>
        <p>{text}</p>
        {link_html}
      </article>""")
    main = f"""<main>
{page_hero("Projects", "Projects", "What we are building now. Published work links to papers, code and data.")}
  <section>
    <div class="container"><div class="feature-grid">
{chr(10).join(html_cards)}
    </div></div>
  </section>
</main>"""
    return wrap(title="Projects", desc="Research projects of the SNU AI Mathematics Lab.", active="projects", main=main)


# ---------------------------------------------------------------- news
def news():
    main = f"""<main>
{page_hero("News", "News", "Announcements, releases and results.")}
  <section>
    <div class="container"><div class="panel">
      <ul class="news-list">
{news_items(NEWS, "../")}
      </ul>
    </div></div>
  </section>
</main>"""
    return wrap(title="News", desc="News from the SNU AI Mathematics Lab.", active="news", main=main)


# ---------------------------------------------------------------- people

def people():
    data = json_load(PEOPLE_JSON)
    cards = []
    for m in data:
        if m.get("photo"):
            avatar = f'<img class="avatar" src="../assets/img/people/{m["photo"]}" alt="{m["name"]}" loading="lazy" />'
        else:
            avatar = f'<div class="avatar" aria-hidden="true">{initials(m["name"])}</div>'
        links = "".join(f'<a href="{u}">{label}</a>' for label, u in m.get("links", []))
        links_html = f'<div class="member-links">{links}</div>' if links else ""
        lead = " lead" if m.get("lead") else ""
        cards.append(f"""        <div class="panel member{lead}">
          {avatar}
          <div class="member-name">{m["name"]}</div>
          <div class="member-role">{m["role"]}</div>
          {links_html}
        </div>""")
    main = f"""<main>
{page_hero("People", "Members", "Current members and collaborators of SNU AI Mathematics Lab.")}
  <section>
    <div class="container">
      <div class="members-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="People", desc="Members of the SNU AI Mathematics Lab.", active="people", main=main)


