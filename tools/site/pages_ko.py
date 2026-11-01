"""Korean pages of the lab website (served under /ko/).

Technical terms (Lean 4, autoformalization, SA-Pass, shadow, Mathlib, model and
system names) and paper titles stay in English on purpose.
"""
from pathlib import Path

from common import (ARXIV, CODABENCH, F4_CODE, GITHUB, HF, KATEX, LB_PUBLIC, LEAN4ALL, LEAN4ALL_CODE,
                    PEOPLE_JSON, initials, json_load, news_items, page_hero, wrap)

L = "ko"

NEWS = [
    ("2026-11", "연구실 웹사이트를 새로 열었습니다. 벤치마크, 리더보드, 논문을 소개합니다."),
    ("2026-11", f'<strong><a href="{LEAN4ALL}">Lean4All</a></strong>을 공개했습니다. AI agent로 수학을 Lean&nbsp;4로 형식화하는 오픈 플랫폼으로, GitHub를 통해 운영되고 blueprint를 제공하며, arXiv 논문이나 업로드한 파일로 mission을 만들 수 있습니다. 모든 증명은 Lean이 검사합니다.'),
    ("2026-10-26", f'<strong>새 원고:</strong> Dongwook Cheon, <a href="{{P}}publications/">Formalizing Faugère\'s F<sub>4</sub> Algorithm in Lean&nbsp;4</a>. 형식화된 F<sub>4</sub> 절차가 종료하며 입력 ideal의 Gröbner basis를 반환함을 Lean으로 증명했습니다. <a href="{F4_CODE}">Code</a>.'),
    ("2026-10-20", "<strong>리더보드 업데이트.</strong> ShadowBench에 새 agentic 결과가 추가되었습니다. Numina-Lean-Agent를 쓴 Codex (GPT-6.1 Sol)가 SA-Pass 18.5%로 현재 최고입니다. Numina-Lean-Agent를 쓴 Claude Code (Opus 5.5)는 출력의 93.8%가 컴파일되지만 SA-Pass는 16.9%에 그칩니다."),
    ("2026-10-14", "<strong>리더보드 업데이트.</strong> 직접 프롬프팅한 frontier 모델(Claude Opus 5.5, Sonnet 5.5, Fable 5.1; GPT-6 Sol, Luna, Astra)은 출력의 최대 38.2%가 컴파일되지만 SA-Pass는 최대 1.1%입니다."),
    ("2026-09", "<strong>ShadowBench</strong>가 <strong>EMNLP 2026</strong>에 발표됩니다."),
    ("2026-08-29", f'ShadowBench 프리프린트를 arXiv(<a href="{ARXIV}">2608.29270</a>)에 공개했습니다. <a href="{GITHUB}">코드</a>, <a href="{HF}">공개 데이터셋</a>, <a href="{LB_PUBLIC}">공개 리더보드</a>도 함께 제공합니다.'),
    ("2026-04 – 06", f'ShadowBench의 초기 126문제 버전이 <a href="{CODABENCH}">ICML 2026 AI for Math Workshop &amp; Challenge의 Track 4</a> 벤치마크로 쓰였습니다(Lean&nbsp;4에서의 end-to-end autoformalization과 증명). 약 117개 팀이 등록했고 27개 팀이 참가했습니다.'),
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
            우리는 수학을 읽고, 형식화하고, 검증하는 AI 시스템을 만듭니다. 핵심 주제는
            autoformalization, 즉 사람이 쓴 수학을 컴퓨터가 모든 단계를 검증할 수 있는 언어인
            Lean&nbsp;4로 옮기는 일입니다. 그리고 그 번역이 수학자가 의도한 내용을 정확히 담고 있는지를
            엄밀하게 측정합니다.
          </p>
          <p style="margin-top: 14px;">
            이를 위한 벤치마크, checker, 리더보드를 만들고, 수학 문제를 풀고 생성하고 검증하는
            시스템을 연구합니다.
          </p>
          <div class="korean-name">서울대학교 수리과학부</div>
          <div class="hero-actions">
            <a class="btn primary" href="benchmarks/">ShadowBench</a>
            <a class="btn secondary" href="leaderboard/">리더보드</a>
            <a class="btn secondary" href="people/">구성원 소개</a>
          </div>
        </div>

        <div class="hero-side">
          <div class="mini-panel metric">
            <span>New · EMNLP 2026</span>
            <strong>ShadowBench</strong>
            <span>형식 명제가 컴파일되는지만이 아니라 정리의 내용을 제대로 담고 있는지를 검사하는 Lean&nbsp;4 벤치마크입니다. <a class="text-link" href="{ARXIV}">논문 보기</a></span>
          </div>
          <div class="mini-panel">
            <h3 style="margin-bottom: 8px;">컴파일은 이해가 아니다</h3>
            <p style="margin: 0;">최신 시스템은 우리 문제의 90% 이상에서 컴파일되는 Lean 코드를 만들지만, 의도한 정리를 정확히 진술하는 비율은 최대 18.5%입니다.</p>
          </div>
          <div class="mini-panel">
            <h3 style="margin-bottom: 8px;">연구 책임자</h3>
            <p style="margin: 0;">현동훈 (David Donghoon Hyeon), 서울대학교 수리과학부 교수.</p>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="stat-grid">
          <div class="stat"><strong>178</strong><span>ShadowBench의 대학원~연구 수준 문제</span></div>
          <div class="stat"><strong>706</strong><span>Lean으로 검증되는 hidden shadow 정리</span></div>
          <div class="stat"><strong>98.8%</strong><span>SA-Pass와 전문가 판정의 일치율</span></div>
          <div class="stat"><strong>41</strong><span>공개 리더보드에 오른 시스템</span></div>
        </div>
      </div>
    </section>

    <section id="highlights">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">주요 성과</div>
            <h2>현재 연구</h2>
          </div>
          <p>지금 공개되어 있는 벤치마크, checker, 결과입니다.</p>
        </div>
        <div class="feature-grid">
          <article class="panel feature">
            <span class="tag">Benchmark · EMNLP 2026</span>
            <h3>ShadowBench와 SA-Pass</h3>
            <p>각 문제에는 shadow라 부르는 숨겨진 보조 정리들이 있습니다. 생성된 명제가 모든 shadow를 함의하고, shadow들을 모두 합하면 다시 그 명제가 나온다는 것을 Lean이 증명할 때에만 점수를 받습니다.</p>
            <a class="more" href="benchmarks/#shadowbench">작동 방식 →</a>
          </article>
          <article class="panel feature">
            <span class="tag">Leaderboard</span>
            <h3>41개 시스템 평가</h3>
            <p>Lean 도구를 쓰거나 쓰지 않는 agentic 코딩 어시스턴트, frontier 모델과 open 모델, Lean 특화 prover를 모두 같은 178문제로 평가했습니다.</p>
            <a class="more" href="leaderboard/">결과 보기 →</a>
          </article>
          <article class="panel feature">
            <span class="tag">Challenge · ICML 2026</span>
            <h3>AI for Math, Track 4</h3>
            <p>ShadowBench의 초기 버전이 ICML 2026 AI for Math Challenge Track 4의 벤치마크로 쓰였습니다. 약 117개 팀이 등록했습니다.</p>
            <a class="more" href="news/">소식 →</a>
          </article>
        </div>
      </div>
    </section>

    <section id="about">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">소개</div>
            <h2>AI와 수학이 만나는 연구</h2>
          </div>
          <p>SNU AI Mathematics Lab은 기계가 수학 지식을 형식화하고, 풀고, 생성하고, 검증하는 방법을 연구합니다.</p>
        </div>

        <div class="about-grid">
          <div class="panel">
            <h3>연구실 소개</h3>
            <p>
              대규모 언어 모델은 이제 컴파일되는 Lean 코드를 쓸 수 있지만, 컴파일되는 명제도 틀린 내용을 말할 수
              있습니다. 가정이 빠지거나, 결론이 약해지거나, 계산해야 할 값을 가정으로 두는 식입니다. 우리는 이
              간극을 측정 가능하게 만듭니다. 대학원 교재와 최신 연구 논문에서 벤치마크 문제를 만들고, Lean이 직접
              검증하는 hidden checker를 구축하며, 공개 평가를 운영하고, 참조 형식화가 없을 때에도 형식화가
              충실한지 판정하는 방법을 개발합니다.
            </p>
          </div>
          <div class="panel">
            <h3>바로 가기</h3>
            <ul class="clean-list">
              <li><a class="text-link" href="publications/">논문</a></li>
              <li><a class="text-link" href="benchmarks/">ShadowBench, ABM, LIFT@Seoul</a></li>
              <li><a class="text-link" href="leaderboard/">리더보드</a></li>
              <li><a class="text-link" href="{HF}">Hugging Face 데이터셋</a></li>
              <li><a class="text-link" href="{LEAN4ALL}">Lean4All: AI agent 기반 오픈 형식화 플랫폼</a></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="research">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">연구</div>
            <h2>주요 연구 분야</h2>
          </div>
          <p>여섯 분야를 하나의 질문이 잇습니다: AI 시스템이 수학을 제대로 했는지 어떻게 알 수 있는가?</p>
        </div>

        <div class="research-grid">
          <article class="panel research-card"><span class="tag">01</span><h3>Autoformalization</h3><p>교재와 연구 수준의 수학을 Lean&nbsp;4 명제와 증명으로 옮깁니다. 대학원 대수, 해석, 위상, 대수기하부터 최신 arXiv 논문까지 다룹니다.</p></article>
          <article class="panel research-card"><span class="tag">02</span><h3>벤치마크와 리더보드</h3><p>ShadowBench, 더 큰 내부 컬렉션인 ABM, 샌드박스 평가 서버 LIFT@Seoul, 그리고 공개 리더보드.</p></article>
          <article class="panel research-card"><span class="tag">03</span><h3>Semantic Alignment와 검증</h3><p>형식 명제가 비형식 명제와 같은 뜻인지 판정합니다. 양방향 hidden shadow 검사와, 참조 형식화가 없을 때의 alignment 판정을 연구합니다.</p></article>
          <article class="panel research-card"><span class="tag">04</span><h3>자동 문제 풀이</h3><p>Lean 코드를 쓰고, 컴파일하고, 고치는 과정을 반복하는 agentic 시스템과, 그런 시스템이 여전히 의도한 정리를 진술하지 못하는 지점을 연구합니다.</p></article>
          <article class="panel research-card"><span class="tag">05</span><h3>자동 문제 생성</h3><p>논문과 교재를 참조 Lean 파일과 checker를 갖춘 벤치마크 문제로 바꿉니다. 모델이 초안을 쓰고 수학자가 검토합니다.</p></article>
          <article class="panel research-card"><span class="tag">06</span><h3>정리 생성</h3><p>의미 있는 추측, 보조정리, 정리를 proof assistant가 검사할 수 있는 형태로 제안하는 모델을 탐구합니다.</p></article>
        </div>
      </div>
    </section>

    <section id="news">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">소식</div>
            <h2>최신 소식</h2>
          </div>
          <p><a class="text-link" href="news/">전체 소식 →</a></p>
        </div>
        <div class="panel">
          <ul class="news-list">
{news_items(NEWS[1:4])}
          </ul>
        </div>
      </div>
    </section>
  </main>"""
    return wrap(title="", desc="SNU AI Mathematics Lab: autoformalization, Lean 4 벤치마크, AI가 생성한 수학의 의미 검증.", active=None, main=main, home=True, lang=L)


# ---------------------------------------------------------------- benchmarks
AG_BLOCK = Path(__file__).with_name("ag_block_ko.html").read_text()


def benchmarks():
    main = f"""<main>
{page_hero("Benchmarks", "벤치마크", "AI 시스템이 수학을 충실하게 형식화하는지를 검사하는 벤치마크를 만듭니다. Lean 코드가 컴파일되는지만 보지 않습니다.")}

  <section id="shadowbench">
    <div class="container stack">
      <div class="section-head">
        <div>
          <div class="eyebrow">EMNLP 2026</div>
          <h2>ShadowBench</h2>
        </div>
        <p>여덟 개 수학 분야의 대학원~연구 수준 문제 178개로 이루어진 Lean&nbsp;4 full autoformalization 벤치마크이며, SA-Pass로 채점합니다.</p>
      </div>

      <div class="two-col">
        <div class="panel">
          <h3>컴파일률의 문제</h3>
          <p>
            모델이 만든 Lean 명제는 컴파일되면서도 틀릴 수 있습니다. 결론을 약하게 하거나, 가정을 빠뜨리거나,
            증명해야 할 것을 가정할 수 있습니다. 컴파일률은 이 모두를 정답으로 셉니다. 반대로 하나의 참조
            형식화와 비교하는 방식은 다르지만 동치인 방식으로 쓴 올바른 명제를 틀렸다고 판정합니다.
          </p>
          <p>
            SA-Pass(Semantic Alignment Pass)는 코드 생성에서의 unit test 아이디어를 가져옵니다. 문제마다 전문가가
            의도한 정리를 함께 특징짓는 작은 보조 Lean 명제들, 즉 <strong>shadow</strong>를 정합니다. Shadow는
            평가 서버에 숨겨져 있고, Lean이 모든 제출을 shadow에 대해 자동으로 채점합니다.
          </p>
        </div>
        <div class="panel">
          <h3>자료</h3>
          <ul class="clean-list">
            <li><a href="{ARXIV}">논문 (arXiv 2608.29270)</a></li>
            <li><a href="{GITHUB}">코드 (GitHub)</a></li>
            <li><a href="{HF}">데이터셋 (Hugging Face, CC BY 4.0)</a></li>
            <li><a href="{LB_PUBLIC}">공개 리더보드와 제출</a></li>
            <li><a href="{CODABENCH}">ICML 2026 AI for Math Challenge, Track 4</a></li>
          </ul>
        </div>
      </div>

      <div class="stat-grid">
        <div class="stat"><strong>178</strong><span>문제: level&nbsp;1 113개, level&nbsp;2 52개, level&nbsp;3(연구 수준) 13개</span></div>
        <div class="stat"><strong>8</strong><span>수학 분야</span></div>
        <div class="stat"><strong>706</strong><span>shadow: forward 검사 513개, backward 검사 193개</span></div>
        <div class="stat"><strong>98.8%</strong><span>전문가 판정과의 일치율 (precision 1.000, recall 0.930)</span></div>
      </div>

      <div class="two-col">
        <div class="panel">
          <h3>SA-Pass 채점 방식</h3>
          <ol class="steps">
            <li><span><strong>컴파일.</strong> 생성된 Lean 파일이 <code class="inline">sorry</code> 없이 Mathlib과 함께 단독으로 컴파일되어야 합니다.</span></li>
            <li><span><strong>Forward 검사.</strong> 명제가 모든 shadow를 함의함을 Lean이 증명해야 합니다. 약해지거나 일부만 담은 명제를 잡아냅니다.</span></li>
            <li><span><strong>Backward 검사.</strong> Shadow들을 모두 합하면 명제가 나온다는 것을 Lean이 증명해야 합니다. 덧붙인 결론과 빠진 가정을 잡아냅니다.</span></li>
            <li><span><strong>점수.</strong> 모든 검사를 통과해야 SA-Pass가 1입니다. SA-Pass<sub>soft</sub>는 부분 점수로, forward 검사 통과 비율에 절반, backward 검사에 절반을 줍니다.</span></li>
          </ol>
        </div>
        <div class="panel">
          <h3>분야별 문제 수</h3>
          <div class="table-wrap">
            <table>
              <thead><tr><th>분야</th><th class="num">문제</th></tr></thead>
              <tbody>
                <tr><td>해석학</td><td class="num">28</td></tr>
                <tr><td>대수학</td><td class="num">26</td></tr>
                <tr><td>위상수학</td><td class="num">25</td></tr>
                <tr><td>기하학</td><td class="num">24</td></tr>
                <tr><td>대수기하학</td><td class="num">22</td></tr>
                <tr><td>확률론</td><td class="num">20</td></tr>
                <tr><td>정수론</td><td class="num">19</td></tr>
                <tr><td>조합론</td><td class="num">14</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

{AG_BLOCK}      <div class="panel">
        <h3>주요 결과</h3>
        <ul class="clean-list">
          <li><strong>컴파일률은 alignment를 과대평가합니다.</strong> 논문에서 가장 좋은 시스템(Opus 4.8과 Numina-Lean-Agent를 쓴 Claude Code)은 문제의 61.8%를 컴파일하지만 SA-Pass는 11.2%입니다. 더 새로운 시스템은 90% 이상을 컴파일하지만 SA-Pass는 최대 18.5%입니다.</li>
          <li><strong>Lean 도구는 의미보다 컴파일을 더 끌어올립니다.</strong> Numina-Lean-Agent를 붙이자 Opus&nbsp;4.8의 컴파일률은 41.6%p 올랐지만 SA-Pass는 8.4%p 오르는 데 그쳤습니다.</li>
          <li><strong>직접 프롬프팅은 크게 뒤처집니다.</strong> 논문의 closed, open, Lean 특화 모델은 직접 프롬프팅했을 때 모두 SA-Pass 0.0이었습니다.</li>
          <li><strong>SA-Pass는 전문가 판정과 일치합니다.</strong> 여섯 가지 agentic 설정에서 컴파일에 성공한 출력에 대해 SA-Pass는 전문가와 98.8% 일치합니다(BEq+: 80.6%, 컴파일 검사: 17.8%).</li>
        </ul>
      </div>

      <div class="panel">
        <h3>구축 과정</h3>
        <p>문제는 대학원 교재(Lee, <em>Introduction to Smooth Manifolds</em>; Stein–Shakarchi, <em>Real Analysis</em>; Cox–Little–O'Shea, <em>Ideals, Varieties, and Algorithms</em>; Boyd–Vandenberghe, <em>Convex Optimization</em>; Wunsch, <em>Complex Variables with Applications</em>; EGA; <em>Proofs from THE BOOK</em>), Stacks Project, Wiedijk 1000+ 목록에서 아직 형식화되지 않은 정리, "PRIMES is in P" 논문, Mathlib&nbsp;4에서 가져왔습니다. 언어 모델이 각 문제의 shadow 초안을 쓰며, 85%의 문제에서는 첫 초안이 이미 완전합니다. 수학자가 모든 shadow 집합을 검토하고, Lean이 shadow들이 참조 명제를 함께 특징짓는지 검사합니다. Checker 구축에는 문제당 평균 약 10분이 걸립니다.</p>
      </div>
    </div>
  </section>

  <section id="abm">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="eyebrow">개발 중</div>
          <h2>ABM: Autoformalization Benchmark</h2>
        </div>
        <p>ShadowBench의 바탕이 된 더 큰 내부 컬렉션입니다.</p>
      </div>
      <div class="simple-grid">
        <div class="panel">
          <h3>구성</h3>
          <p>1,200개가 넘는 Lean&nbsp;4 문제로 이루어져 있습니다. 약 370개는 연구실이 대학원 교재, 대한수학회 대학생 수학경시대회, 최신 arXiv 논문 38편으로부터 열 개 분야에 걸쳐 직접 만들었습니다. 나머지는 miniF2F와 ProofNet 문제를 최신 Lean과 Mathlib에서 다시 검사한 것입니다. 연구실이 만든 문제에는 참조 Lean 파일이 있고, 상당수에는 hidden forward·backward checker도 있습니다.</p>
        </div>
        <div class="panel">
          <h3>난이도</h3>
          <ul class="clean-list">
            <li><strong>L1:</strong> 정의와 명제, 증명 없음.</li>
            <li><strong>L2:</strong> 짧고 직접적인 증명이 있는 명제.</li>
            <li><strong>L3:</strong> 정의와 보조정리들이 모여 주정리로 이어지는 묶음.</li>
            <li><strong>L4:</strong> 연구 수준의 결과.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="lift">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="eyebrow">평가 서버</div>
          <h2>LIFT@Seoul</h2>
        </div>
        <p>Lean4 Inference and Formalization Test @ Seoul National University.</p>
      </div>
      <div class="panel">
        <p>LIFT@Seoul은 연구실의 평가 서버입니다. 각 문제를 모델이나 agent에 보내고, 돌려받은 Lean 파일을 네트워크가 차단된 샌드박스에서 고정된 Lean과 Mathlib으로 컴파일하며, <code class="inline">sorry</code>를 쓰거나 axiom을 추가하거나 목표 명제를 바꾼 파일은 거부합니다. 이어서 hidden forward·backward checker를 실행하고 분야별, 난이도별 결과를 보고합니다. 현재는 연구실 구성원과 공동 연구자에게 열려 있습니다.</p>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="벤치마크", desc="ShadowBench, ABM autoformalization benchmark, LIFT@Seoul 평가 서버.", active="benchmarks", main=main, extra_head=KATEX, lang=L)


# ---------------------------------------------------------------- leaderboard
def leaderboard():
    main = f"""<main>
{page_hero("Leaderboard", "ShadowBench 리더보드", f'ShadowBench test split 178문제에 대한 결과로, SA-Pass 순으로 정렬했습니다. <a href="{LB_PUBLIC}">공개 리더보드</a>의 데이터를 가져왔으며, 기준일은 <!-- LB:ASOF:START -->2026-11-02<!-- LB:ASOF:END -->입니다.')}

  <section>
    <div class="container stack">
      <div class="feature-grid">
        <div class="panel"><h3>Compile</h3><p>생성된 Lean 코드가 <code class="inline">sorry</code> 없이 단독으로 컴파일되는 문제의 비율.</p></div>
        <div class="panel"><h3>SA-Pass<sub>soft</sub></h3><p>부분 점수: forward 검사 통과 비율에 절반, backward 검사에 절반. 컴파일되지 않은 출력은 0점입니다.</p></div>
        <div class="panel"><h3>SA-Pass</h3><p>컴파일되고 모든 forward·backward 검사를 통과한 문제의 비율. 즉 명제가 정리의 뜻을 정확히 담은 경우입니다.</p></div>
      </div>

      <div class="panel table-wrap">
        <table>
          <thead><tr><th class="num">#</th><th>시스템</th><th>유형</th><th class="num">Compile</th><th class="num">SA-Pass<sub>soft</sub></th><th class="num">SA-Pass</th><th class="num">L3 SA-Pass</th><th>출처</th></tr></thead>
          <tbody><!-- LB:ROWS:START --><!-- LB:ROWS:END --></tbody>
        </table>
      </div>

      <div class="panel">
        <p class="note">모든 값은 같은 178문제에 대한 백분율입니다(시스템 <!-- LB:COUNT:START -->0<!-- LB:COUNT:END -->개). "논문" 행은 <a href="{ARXIV}">ShadowBench 논문</a>의 Table&nbsp;3입니다. "논문 이후" 행은 같은 문제로 나중에 실행한 결과로, agentic 시스템은 2026-10-20, 직접 프롬프팅은 출력 토큰 최대 128k로 2026-10-14에 실행했습니다(논문은 2k–8k). 이 실행들에서는 한 문제의 기록이 없어 실패로 셉니다. "+ Numina"는 agent가 Numina-Lean-Agent의 Lean 도구를 쓸 수 있었다는 뜻입니다. L3는 연구 수준 문제 13개입니다.</p>
        <p class="note">시스템을 제출하려면 <a href="{LB_PUBLIC}">공개 리더보드</a>를 이용하세요.</p>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="리더보드", desc="ShadowBench 리더보드: 178문제에 대한 41개 시스템의 compile rate와 SA-Pass.", active="leaderboard", main=main, lang=L)


# ---------------------------------------------------------------- publications
F4_BLURB = (r"Faugère의 F<sub>4</sub> 알고리즘을 Mathlib의 다변수 다항식 위에서 Lean&nbsp;4로 형식화했습니다. "
            r"유한개 변수의 체 위 다항식들로 이루어진, 0이 아닌 다항식의 유한집합 \(F\)에 대해 이 절차는 종료하며 "
            r"\(\langle G\rangle = \langle F\rangle\)이고 \(\langle \mathrm{LM}(g) : g \in G\rangle = \mathrm{in}_\prec(\langle F\rangle)\)인 "
            r"유한집합 \(G\)를 반환합니다. 즉 \(G\)는 Gröbner basis입니다(정리 <code class=\"inline\">F4_groebner</code>). "
            r"Symbolic preprocessing과 Gaussian elimination을 다항식의 유한집합 위에서 직접 수행하고, 종료성은 사전식 well-founded relation으로 보입니다. "
            r"검사한 결과들은 Lean의 표준 axiom 세 개만 사용하며 <code class=\"inline\">sorry</code>가 없습니다.").replace('\\"', '"')


def publications():
    authors = ("<strong>Hojae Han</strong>*, <strong>Jongyoon Kim</strong>*, <strong>Sanghyeok Park</strong>*, "
               "<strong>Dongwook Cheon</strong>, <strong>Yeachan Park</strong>, <strong>Myeong Jae Jeon</strong>, "
               "<strong>Sunjong Choe</strong>, Soonho Kong, Wonseok Hur, Seung-won Hwang†, <strong>Donghoon Hyeon</strong>†")
    r = "../../"
    main = f"""<main>
{page_hero("Publications", "논문", "연구실의 논문입니다. 연구실 구성원은 굵게 표시했습니다.")}
  <section>
    <div class="container stack">
      <div class="panel">
        <h3>2026</h3>
        <div class="pub">
          <div class="pub-title">ShadowBench: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization</div>
          <div class="pub-authors">{authors}</div>
          <div class="pub-venue"><em>EMNLP 2026</em> · arXiv:2608.29270 · * 공동 제1저자, † 교신저자</div>
          <p style="margin:6px 0 0;">숨겨진 보조 정리(shadow)와의 양방향 함의를 Lean으로 검사해 형식 명제를 채점하는 SA-Pass와, 대학원~연구 수준 Lean&nbsp;4 문제 178개로 이루어진 ShadowBench를 제안합니다. SA-Pass는 전문가 판정과 98.8% 일치하며, 논문에서 가장 좋은 시스템은 61.8%를 컴파일하지만 SA-Pass는 11.2%입니다.</p>
          <div class="pub-links">
            <a class="badge closed" href="{ARXIV}">arXiv</a>
            <a class="badge closed" href="{GITHUB}">Code</a>
            <a class="badge closed" href="{HF}">Dataset</a>
            <a class="badge closed" href="{LB_PUBLIC}">Leaderboard</a>
          </div>
        </div>
        <div class="pub">
          <div class="pub-title">Formalizing Faugère's F<sub>4</sub> Algorithm in Lean&nbsp;4</div>
          <div class="pub-authors"><strong>Dongwook Cheon</strong></div>
          <div class="pub-venue"><em>원고</em> · 2026년 10월</div>
          <p style="margin:6px 0 0;">{F4_BLURB}</p>
          <div class="pub-links">
            <a class="badge closed" href="{r}papers/cheon-2026-f4-lean4.pdf">PDF</a>
            <a class="badge closed" href="{F4_CODE}">Code</a>
          </div>
        </div>
        <p class="note" style="margin-top:14px;">BibTeX는 <a href="{r}publications/">영문 페이지</a>에 있습니다.</p>
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="논문", desc="SNU AI Mathematics Lab의 논문.", active="publications", main=main, extra_head=KATEX, lang=L)


# ---------------------------------------------------------------- projects
def projects():
    cards = [
        ("발표", "open", "ShadowBench와 SA-Pass",
         "Lean이 양방향으로 검증하는 숨겨진 shadow 정리를 이용해, 형식 명제가 정리의 뜻을 정확히 담고 있는지 검사하는 벤치마크이자 평가 지표입니다.",
         f'<a href="../benchmarks/#shadowbench">벤치마크</a><a href="{ARXIV}">논문</a><a href="{GITHUB}">Code</a>'),
        ("운영 중", "open", "Lean4All",
         "AI agent로 수학을 Lean&nbsp;4로 형식화하는 오픈 플랫폼입니다. 참여자는 자신의 AI agent로 mission의 정리들을 증명하고, 작업은 GitHub를 통해 이루어지며, 모든 증명은 Lean이 검사합니다. Blueprint는 형식화된 정의와 보조정리들이 서로 어떻게 의존하는지 보여 줍니다. Mission은 arXiv 논문에서 몇 단계 만에, 또는 업로드한 파일로 만들 수 있습니다. Lean4All은 Prove2Me에서 영감을 받은 독립 플랫폼이며 한국어 인터페이스를 제공합니다.",
         f'<a href="{LEAN4ALL}">사이트 열기</a><a href="{LEAN4ALL_CODE}">Code</a>'),
        ("진행 중", "closed", "ABM: Autoformalization Benchmark",
         "1,200개가 넘는 Lean&nbsp;4 문제로 이루어진 내부 컬렉션입니다. 그중 약 370개는 연구실이 교재, 경시대회, 최신 arXiv 논문으로부터 직접 만들었습니다.",
         '<a href="../benchmarks/#abm">자세히</a>'),
        ("진행 중", "closed", "LIFT@Seoul 평가 서버",
         "모델과 agent를 샌드박스에서 두 단계로 평가합니다. 먼저 Lean으로 컴파일하고, 이어서 hidden forward·backward 검사를 실행해 분야별, 난이도별로 보고합니다.",
         '<a href="../benchmarks/#lift">자세히</a>'),
        ("진행 중", "closed", "참조 없는 alignment 판정",
         "실제 형식화에는 비교할 참조가 없는 경우가 대부분입니다. 비형식 명제와 형식 명제만으로 판정하는 judge를 만듭니다. 각 명제가 다루는 대상과 주장을 추출해 서로 대응시키고, 둘이 다르면 그 차이를 드러내는 구체적인 예를 찾습니다.",
         ""),
        ("진행 중", "closed", "증명과 코드를 위한 shadow",
         "Shadow 검사를 명제 너머로 확장합니다. 증명에 대해서는 형식 증명이 비형식 증명이 주장하는 단계들을 실제로 확립하는지, 프로그램에 대해서는 두 프로그램이 같게 동작하는지를 검사합니다.",
         ""),
        ("진행 중", "closed", "성장하는 라이브러리의 형식화",
         "각 명제가 앞선 명제들 위에 쌓이는 Stacks Project에서 형식화 대상을 가져와, 라이브러리가 커져 갈 때의 autoformalization을 시험합니다.",
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
{page_hero("Projects", "프로젝트", "지금 만들고 있는 것들입니다. 발표된 연구는 논문, 코드, 데이터로 연결됩니다.")}
  <section>
    <div class="container"><div class="feature-grid">
{chr(10).join(html_cards)}
    </div></div>
  </section>
</main>"""
    return wrap(title="프로젝트", desc="SNU AI Mathematics Lab의 연구 프로젝트.", active="projects", main=main, lang=L)


# ---------------------------------------------------------------- news
def news():
    main = f"""<main>
{page_hero("News", "소식", "공지, 공개, 결과.")}
  <section>
    <div class="container"><div class="panel">
      <ul class="news-list">
{news_items(NEWS, "../")}
      </ul>
    </div></div>
  </section>
</main>"""
    return wrap(title="소식", desc="SNU AI Mathematics Lab 소식.", active="news", main=main, lang=L)


# ---------------------------------------------------------------- people
def people():
    data = json_load(PEOPLE_JSON)
    cards = []
    for m in data:
        name = m.get("name_ko") or m["name"]
        sub = f' <span class="note">{m["name"]}</span>' if m.get("name_ko") else ""
        if m.get("photo"):
            avatar = f'<img class="avatar" src="../../assets/img/people/{m["photo"]}" alt="{m["name"]}" loading="lazy" />'
        else:
            avatar = f'<div class="avatar" aria-hidden="true">{initials(m["name"])}</div>'
        links = "".join(f'<a href="{u}">{label}</a>' for label, u in m.get("links_ko", m.get("links", [])))
        links_html = f'<div class="member-links">{links}</div>' if links else ""
        lead = " lead" if m.get("lead") else ""
        cards.append(f"""        <div class="panel member{lead}">
          {avatar}
          <div class="member-name">{name}{sub}</div>
          <div class="member-role">{m.get("role_ko", m["role"])}</div>
          {links_html}
        </div>""")
    main = f"""<main>
{page_hero("People", "구성원", "SNU AI Mathematics Lab의 구성원과 공동 연구자입니다.")}
  <section>
    <div class="container">
      <div class="members-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
</main>"""
    return wrap(title="구성원", desc="SNU AI Mathematics Lab 구성원.", active="people", main=main, lang=L)
