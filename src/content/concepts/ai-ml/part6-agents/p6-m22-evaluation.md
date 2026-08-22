---
title: "P6-M22 - Evaluation Harnesses & Task Success Metrics"
description: "Part 6 — Agents, Workflows Evaluation · Module 22 of 22 Evaluation Harnesses Task Success Metrics Measure what matters — RAG faithfulness, agent task success, and LLM-as-judge…"
domain: ai-ml
track: ai-ml-engineering
module: part6-agents
order: 622
url: /learning/ai-ml/part6-agents/p6-m22-evaluation/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1e0a3a 40%,#4a1080 70%,#7c3aed 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c4b5fd;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ede9fe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ede9fe}
.tab-bar{display:flex;flex-wrap:wrap;background:#0f0a1e;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#c4b5fd;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#a78bfa;border-bottom-color:#a78bfa}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.p-violet .cp-hdr{background:#f5f0ff}[data-theme=dark] .p-violet .cp-hdr{background:#1e0a3a}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}.tag-violet{background:#ede9fe;color:#4c1d95}
.cb{background:#0f0a1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #7c3aed}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ede9fe;white-space:pre}
.ck{color:#c4b5fd}.cv{color:#f0c080}.cs{color:#a78bfa}
.ins{background:#f5f0ff;border:1.5px solid #7c3aed;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e0a3a;border-color:#7c3aed}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#5b21b6}[data-theme=dark] .ins strong{color:#a78bfa}
.warn{background:#faeaea;border:1.5px solid #fca5a5;border-left:4px solid #dc2626;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#7c3aed;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#1e0a3a;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#7c3aed;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#ede9fe;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#7c3aed;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#7c3aed}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#7c3aed;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #7c3aed;transition:all .15s}
.mod-nav a:hover{background:#7c3aed;color:#fff}
.mod-nav .nb{background:#7c3aed;color:#fff}
.mod-nav .nb:hover{background:#5b21b6;border-color:#5b21b6}
.proj-box{background:#f5f0ff;border:1.5px solid #c4b5fd;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#5b21b6;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#5b21b6}
/* part6 complete banner */
.part-complete{background:linear-gradient(135deg,#1e0a3a,#4a1080);border-radius:12px;padding:1.5rem 1.8rem;color:#fff;margin:2rem 0;text-align:center}
.part-complete h3{font-size:1.3rem;font-weight:800;margin-bottom:.5rem;border:none;color:#fff}
.part-complete p{font-size:.9rem;color:#c4b5fd;margin:0 0 1rem}
.part-skills{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.6rem;margin-top:1rem}
.ps-item{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:.6rem .9rem;font-size:.82rem;color:#ede9fe}
.ps-item::before{content:"✓  ";color:#a78bfa;font-weight:700}
/* metric cards */
.metric-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.7rem;margin:.8rem 0}
.mc{border-radius:8px;padding:.8rem 1rem;border:1.5px solid;text-align:center}
.mc .name{font-size:.78rem;font-family:monospace;font-weight:700;margin-bottom:.2rem}
.mc .val{font-size:1.4rem;font-weight:800;margin-bottom:.2rem}
.mc .desc{font-size:.75rem;line-height:1.5;color:var(--text-color,#555)}
.m-rag{background:#f5f0ff;border-color:#c4b5fd}.m-rag .name{color:#5b21b6}.m-rag .val{color:#7c3aed}
.m-agent{background:#ecfdf5;border-color:#6ee7b7}.m-agent .name{color:#065f46}.m-agent .val{color:#059669}
.m-general{background:#fdf4dc;border-color:#fcd34d}.m-general .name{color:#92400e}.m-general .val{color:#b45309}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 6 — Agents, Workflows &amp; Evaluation &nbsp;·&nbsp; Module 22 of 22</div>
  <div class="mod-title">Evaluation Harnesses &amp; Task Success Metrics</div>
  <div class="mod-subtitle">Measure what matters — RAG faithfulness, agent task success, and LLM-as-judge patterns</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟠 Intermediate–Advanced</span>
    <span class="mod-pill">🔧 DeepEval · Ragas · LangSmith · Promptfoo</span>
    <span class="mod-pill">📋 Prerequisite: P6-M21</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📐 Key Metrics</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🤖 LLM-as-Judge</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📊 RAG Evaluation</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🕵 Agent Evaluation</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔧 DeepEval & Ragas</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🔭 LangSmith</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-thumb" onclick="vt(event,'t10')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-violet">Final Part 6 Module</span></div>
  <div class="cp-body">
    <p>You cannot improve what you cannot measure. Evaluation is what separates teams that ship reliable AI systems from teams that rely on vibes and hope. This module covers the full evaluation stack — from simple metrics you implement yourself to production-grade harnesses.</p>
    <ul>
      <li><strong>Key metrics</strong> — faithfulness, answer relevancy, context recall, task success rate, tool precision</li>
      <li><strong>LLM-as-judge</strong> — using an LLM to evaluate LLM outputs, calibration, and known biases</li>
      <li><strong>RAG evaluation</strong> — RAGAS framework: faithfulness, answer relevancy, context precision, context recall</li>
      <li><strong>Agent evaluation</strong> — task success rate, tool call efficiency, trajectory accuracy</li>
      <li><strong>DeepEval &amp; Ragas</strong> — production eval frameworks with built-in metrics</li>
      <li><strong>LangSmith</strong> — tracing, datasets, evaluation runs, regression testing</li>
    </ul>
  </div>
</div>
</div>


<!-- ══════════ TAB 1 — KEY METRICS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">📐</span><h3>The Metrics That Matter</h3><span class="tag tag-violet">Know These by Name</span></div>
  <div class="cp-body">
    <p class="sep">RAG METRICS</p>
    <div class="metric-grid">
      <div class="mc m-rag">
        <div class="name">Faithfulness</div>
        <div class="val">0–1</div>
        <div class="desc">Are all claims in the answer supported by the retrieved context? 1.0 = fully grounded</div>
      </div>
      <div class="mc m-rag">
        <div class="name">Answer Relevancy</div>
        <div class="val">0–1</div>
        <div class="desc">Does the answer actually address the question asked? High score = on-topic</div>
      </div>
      <div class="mc m-rag">
        <div class="name">Context Precision</div>
        <div class="val">0–1</div>
        <div class="desc">Of the retrieved chunks, what fraction were actually useful? 1.0 = all relevant</div>
      </div>
      <div class="mc m-rag">
        <div class="name">Context Recall</div>
        <div class="val">0–1</div>
        <div class="desc">Did retrieval find all the chunks needed to answer? 1.0 = nothing missed</div>
      </div>
    </div>
    <p class="sep">AGENT METRICS</p>
    <div class="metric-grid">
      <div class="mc m-agent">
        <div class="name">Task Success Rate</div>
        <div class="val">0–100%</div>
        <div class="desc">% of tasks where the agent achieved the stated goal. The headline metric.</div>
      </div>
      <div class="mc m-agent">
        <div class="name">Tool Call Precision</div>
        <div class="val">0–1</div>
        <div class="desc">Were all tool calls necessary? Unused/redundant calls lower this.</div>
      </div>
      <div class="mc m-agent">
        <div class="name">Trajectory Accuracy</div>
        <div class="val">0–1</div>
        <div class="desc">Did the agent follow an efficient path? Compared to optimal sequence.</div>
      </div>
      <div class="mc m-agent">
        <div class="name">Cost per Task</div>
        <div class="val">$</div>
        <div class="desc">Average USD spent per successful task completion.</div>
      </div>
    </div>
    <p class="sep">GENERAL LLM METRICS</p>
    <div class="metric-grid">
      <div class="mc m-general">
        <div class="name">Correctness</div>
        <div class="val">0–1</div>
        <div class="desc">Is the answer factually correct? Requires ground truth.</div>
      </div>
      <div class="mc m-general">
        <div class="name">Coherence</div>
        <div class="val">0–1</div>
        <div class="desc">Is the output well-structured and logically consistent?</div>
      </div>
      <div class="mc m-general">
        <div class="name">Toxicity</div>
        <div class="val">0–1</div>
        <div class="desc">Does output contain harmful content? 0.0 = safe.</div>
      </div>
    </div>
  </div>
</div>
</div><!-- end t1 -->


<!-- ══════════ TAB 2 — LLM-AS-JUDGE ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🤖</span><h3>LLM-as-Judge — Using AI to Evaluate AI</h3><span class="tag tag-violet">Core Technique</span></div>
  <div class="cp-body">
    <p>When you can't write deterministic evaluation rules (most LLM outputs), use a capable LLM as the judge. The key is calibration — your judge must agree with human raters on a validation set.</p>
    <div class="cb"><pre>import anthropic
from pydantic import BaseModel
import instructor

judge_client = instructor.from_anthropic(anthropic.Anthropic())

class JudgeVerdict(BaseModel):
    score:      float   <span class="ck"># 0.0 to 1.0</span>
    reasoning:  str
    passed:     bool    <span class="ck"># True if score >= threshold</span>

<span class="ck"># ── Faithfulness judge ────────────────────────────────</span>
FAITHFULNESS_JUDGE = <span class="cs">"""You are an expert evaluator. Determine whether every factual
claim in the ANSWER is directly supported by the CONTEXT.

Score 1.0: All claims are explicitly stated in the context.
Score 0.5: Most claims supported, some extrapolation.
Score 0.0: Major claims not in context — hallucination present.

CONTEXT:
{context}

ANSWER:
{answer}"""</span>

def judge_faithfulness(context: str, answer: str,
                        threshold: float = <span class="cv">0.7</span>) -> JudgeVerdict:
    result = judge_client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,   <span class="ck"># strong model for judging</span>
        max_tokens=<span class="cv">300</span>,
        temperature=<span class="cv">0.0</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: FAITHFULNESS_JUDGE.format(context=context, answer=answer)}],
        response_model=JudgeVerdict
    )
    result.passed = result.score >= threshold
    return result

<span class="ck"># ── Task success judge ────────────────────────────────</span>
TASK_SUCCESS_JUDGE = <span class="cs">"""Did the AI agent successfully complete the following task?

ORIGINAL TASK: {task}
AGENT'S OUTPUT: {output}

Score 1.0: Task fully completed — all requirements met.
Score 0.5: Task partially completed — some requirements missing.
Score 0.0: Task failed — output does not address the task."""</span>

def judge_task_success(task: str, output: str) -> JudgeVerdict:
    return judge_client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">200</span>, temperature=<span class="cv">0.0</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: TASK_SUCCESS_JUDGE.format(task=task, output=output)}],
        response_model=JudgeVerdict
    )</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>LLM Judge Biases — Know These</h3><span class="tag tag-blue">Calibration</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>Position bias</strong> — judges prefer the first option shown in A/B comparisons. Always randomise ordering and average results.</li>
      <li><strong>Verbosity bias</strong> — longer answers score higher even if less accurate. Penalise unnecessary length explicitly in your judge prompt.</li>
      <li><strong>Self-preference bias</strong> — Claude tends to prefer Claude outputs, GPT prefers GPT outputs. Use a different model family as judge when evaluating your primary model.</li>
      <li><strong>Sycophancy</strong> — judges rate answers higher if they seem confident. Include "do not be influenced by the confidence of the answer" in your judge prompt.</li>
    </ul>
    <div class="cb"><pre><span class="ck"># Calibrate your judge against human ratings</span>
<span class="ck"># Step 1: get 50 human-rated examples (your gold set)</span>
<span class="ck"># Step 2: run your judge on the same 50</span>
<span class="ck"># Step 3: compute correlation (Pearson r or Spearman ρ)</span>
<span class="ck"># Step 4: if r < 0.7, iterate on the judge prompt</span>

from scipy.stats import pearsonr, spearmanr

def calibrate_judge(human_scores: list[float], judge_scores: list[float]) -> dict:
    pearson_r, _ = pearsonr(human_scores, judge_scores)
    spearman_r, _ = spearmanr(human_scores, judge_scores)
    agreement    = sum(<span class="cv">1</span> for h, j in zip(human_scores, judge_scores)
                       if abs(h - j) < <span class="cv">0.2</span>) / len(human_scores)
    return {
        <span class="cs">"pearson_r"</span>:   round(pearson_r, <span class="cv">3</span>),
        <span class="cs">"spearman_r"</span>:  round(spearman_r, <span class="cv">3</span>),
        <span class="cs">"agreement"</span>:   round(agreement, <span class="cv">3</span>),
        <span class="cs">"calibrated"</span>: pearson_r >= <span class="cv">0.7</span>   <span class="ck"># r ≥ 0.7 considered acceptable</span>
    }</pre></div>
  </div>
</div>
</div><!-- end t2 -->


<!-- ══════════ TAB 3 — RAG EVALUATION ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Evaluating Your RAG Pipeline End-to-End</h3><span class="tag tag-violet">Systematic</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Build a ground truth dataset for RAG evaluation</span>
<span class="ck"># Each test case: question + expected answer + expected source</span>
RAG_TEST_SET = [
    {
        <span class="cs">"question"</span>: <span class="cs">"How does DPDK mempool initialisation work?"</span>,
        <span class="cs">"ground_truth"</span>: <span class="cs">"DPDK mempool uses rte_mempool_create() with a fixed pool of memory objects pre-allocated at startup."</span>,
        <span class="cs">"expected_source"</span>: <span class="cs">"dpdk-guide-mempool.pdf"</span>,
    },
    <span class="ck"># ... 20+ test cases</span>
]

<span class="ck"># Run full eval loop</span>
async def evaluate_rag_pipeline(pipeline, test_set: list) -> dict:
    scores = {<span class="cs">"faithfulness"</span>: [], <span class="cs">"relevancy"</span>: [], <span class="cs">"hit_rate"</span>: [],
              <span class="cs">"cost_usd"</span>: [], <span class="cs">"latency_ms"</span>: []}

    for case in test_set:
        import time
        t_start = time.perf_counter()
        result  = await pipeline.query(case[<span class="cs">"question"</span>])
        latency = (time.perf_counter() - t_start) * <span class="cv">1000</span>

        <span class="ck"># Metric 1: Faithfulness</span>
        faith = judge_faithfulness(
            context=<span class="cs">" ".join(s[<span class="cs">"text"</span>] for s in result[<span class="cs">"sources"</span>]),
            answer=result[<span class="cs">"answer"</span>]
        )
        scores[<span class="cs">"faithfulness"</span>].append(faith.score)

        <span class="ck"># Metric 2: Answer relevancy (does answer address the question?)</span>
        relevancy = judge_answer_relevancy(case[<span class="cs">"question"</span>], result[<span class="cs">"answer"</span>])
        scores[<span class="cs">"relevancy"</span>].append(relevancy.score)

        <span class="ck"># Metric 3: Source hit rate</span>
        expected = case[<span class="cs">"expected_source"</span>]
        hit = any(expected in s.get(<span class="cs">"source"</span>, <span class="cs">""</span>) for s in result[<span class="cs">"sources"</span>])
        scores[<span class="cs">"hit_rate"</span>].append(float(hit))

        scores[<span class="cs">"latency_ms"</span>].append(latency)

    def avg(lst): return round(sum(lst) / len(lst), <span class="cv">3</span>) if lst else <span class="cv">0</span>
    return {k: avg(v) for k, v in scores.items()}</pre></div>
  </div>
</div>
</div><!-- end t3 -->


<!-- ══════════ TAB 4 — AGENT EVALUATION ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🕵</span><h3>Evaluating Agents — Task Success and Trajectory</h3><span class="tag tag-violet">Agent Specific</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Agent evaluation is harder than RAG eval because:</span>
<span class="ck"># 1. The "right answer" may not be unique</span>
<span class="ck"># 2. The path matters, not just the destination</span>
<span class="ck"># 3. Tool calls have side effects that are hard to undo</span>

@dataclass
class AgentTestCase:
    task:              str
    expected_outcome:  str                <span class="ck"># what a successful completion looks like</span>
    required_tools:    list[str] = None   <span class="ck"># tools that MUST be called</span>
    forbidden_tools:   list[str] = None   <span class="ck"># tools that must NOT be called</span>
    max_turns:         int = <span class="cv">10</span>
    max_cost_usd:      float = <span class="cv">0.50</span>

AGENT_TEST_SET = [
    AgentTestCase(
        task=<span class="cs">"Find the square root of 1764 and the current time"</span>,
        expected_outcome=<span class="cs">"Answer mentions 42 and current time"</span>,
        required_tools=[<span class="cs">"calculate"</span>, <span class="cs">"get_current_time"</span>],
        max_turns=<span class="cv">5</span>
    ),
    AgentTestCase(
        task=<span class="cs">"Search for DPDK documentation on hugepages"</span>,
        expected_outcome=<span class="cs">"Returns information about hugepage configuration"</span>,
        required_tools=[<span class="cs">"search_web"</span>],
        forbidden_tools=[<span class="cs">"send_email"</span>],   <span class="ck"># should not email anyone</span>
    ),
]

class AgentEvaluator:
    def evaluate(self, agent_fn, test_case: AgentTestCase) -> dict:
        result = agent_fn(test_case.task)
        tools_called = result.get(<span class="cs">"tools_called"</span>, [])
        output       = result.get(<span class="cs">"answer"</span>, <span class="cs">""</span>)
        turns        = result.get(<span class="cs">"turns_used"</span>, <span class="cv">0</span>)
        cost         = result.get(<span class="cs">"cost_usd"</span>, <span class="cv">0</span>)

        <span class="ck"># Task success — LLM judge</span>
        success = judge_task_success(test_case.task, output)

        <span class="ck"># Required tools coverage</span>
        tool_coverage = <span class="cv">1.0</span>
        if test_case.required_tools:
            called_set  = set(tools_called)
            required    = set(test_case.required_tools)
            tool_coverage = len(called_set & required) / len(required)

        <span class="ck"># Forbidden tools check</span>
        forbidden_used = []
        if test_case.forbidden_tools:
            forbidden_used = [t for t in tools_called if t in test_case.forbidden_tools]

        <span class="ck"># Efficiency: did it use more turns than needed?</span>
        efficiency = min(<span class="cv">1.0</span>, (test_case.max_turns - turns) / test_case.max_turns + <span class="cv">0.5</span>)

        return {
            <span class="cs">"task_success"</span>:   success.score,
            <span class="cs">"task_passed"</span>:    success.passed,
            <span class="cs">"tool_coverage"</span>:  tool_coverage,
            <span class="cs">"forbidden_used"</span>: forbidden_used,
            <span class="cs">"turns_used"</span>:     turns,
            <span class="cs">"cost_usd"</span>:       cost,
            <span class="cs">"efficiency"</span>:     efficiency,
            <span class="cs">"judge_reasoning"</span>: success.reasoning,
        }

    def evaluate_batch(self, agent_fn, test_set) -> dict:
        results   = [self.evaluate(agent_fn, tc) for tc in test_set]
        successes = [r[<span class="cs">"task_success"</span>] for r in results]
        return {
            <span class="cs">"task_success_rate"</span>: sum(r[<span class="cs">"task_passed"</span>] for r in results) / len(results),
            <span class="cs">"avg_success_score"</span>: sum(successes) / len(successes),
            <span class="cs">"avg_turns"</span>:         sum(r[<span class="cs">"turns_used"</span>] for r in results) / len(results),
            <span class="cs">"avg_cost_usd"</span>:      sum(r[<span class="cs">"cost_usd"</span>] for r in results) / len(results),
            <span class="cs">"forbidden_violations"</span>: sum(<span class="cv">1</span> for r in results if r[<span class="cs">"forbidden_used"</span>]),
            <span class="cs">"n"</span>:                 len(results),
        }</pre></div>
  </div>
</div>
</div><!-- end t4 -->


<!-- ══════════ TAB 5 — DEEPEVAL & RAGAS ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>DeepEval — Production Eval Framework</h3><span class="tag tag-violet">Framework</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install deepeval

from deepeval import evaluate
from deepeval.metrics import (
    AnswerRelevancyMetric, FaithfulnessMetric,
    ContextualPrecisionMetric, ContextualRecallMetric,
    HallucinationMetric, ToxicityMetric,
)
from deepeval.test_case import LLMTestCase

<span class="ck"># Define metrics</span>
metrics = [
    AnswerRelevancyMetric(threshold=<span class="cv">0.7</span>, model=<span class="cs">"gpt-4o"</span>),
    FaithfulnessMetric(threshold=<span class="cv">0.7</span>, model=<span class="cs">"gpt-4o"</span>),
    ContextualPrecisionMetric(threshold=<span class="cv">0.7</span>, model=<span class="cs">"gpt-4o"</span>),
    ContextualRecallMetric(threshold=<span class="cv">0.7</span>, model=<span class="cs">"gpt-4o"</span>),
]

<span class="ck"># Create a test case</span>
test_case = LLMTestCase(
    input=<span class="cs">"How does DPDK mempool work?"</span>,
    actual_output=<span class="cs">"DPDK mempool pre-allocates a fixed pool of memory objects..."</span>,
    expected_output=<span class="cs">"rte_mempool_create() creates a fixed-size pool..."</span>,   <span class="ck"># optional</span>
    retrieval_context=[<span class="cs">"The DPDK mempool library provides an API to allocate..."</span>]
)

<span class="ck"># Run evaluation</span>
results = evaluate([test_case], metrics)

<span class="ck"># Use in pytest for CI/CD regression testing</span>
from deepeval import assert_test
import pytest

@pytest.mark.parametrize(<span class="cs">"test_case"</span>, my_test_cases)
def test_rag_quality(test_case):
    assert_test(test_case, metrics)</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Ragas — RAG Assessment Framework</h3><span class="tag tag-blue">RAG Specific</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install ragas

from ragas import evaluate
from ragas.metrics import (
    faithfulness, answer_relevancy,
    context_precision, context_recall
)
from datasets import Dataset

<span class="ck"># Prepare your evaluation dataset</span>
data = {
    <span class="cs">"question"</span>: [<span class="cs">"How does DPDK mempool work?"</span>, <span class="cs">"What is VPP?"</span>],
    <span class="cs">"answer"</span>:   [<span class="cs">"DPDK mempool uses rte_mempool_create..."</span>, <span class="cs">"VPP is Vector Packet Processor..."</span>],
    <span class="cs">"contexts"</span>: [
        [<span class="cs">"The mempool library provides..."</span>, <span class="cs">"rte_mempool_create allocates..."</span>],
        [<span class="cs">"VPP is FD.io's data plane..."</span>],
    ],
    <span class="cs">"ground_truth"</span>: [<span class="cs">"rte_mempool_create creates a fixed pool"</span>, <span class="cs">"VPP processes vectors of packets"</span>]
}
dataset = Dataset.from_dict(data)

<span class="ck"># Run Ragas evaluation</span>
result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
print(result)
<span class="ck"># {'faithfulness': 0.92, 'answer_relevancy': 0.88,</span>
<span class="ck">#  'context_precision': 0.84, 'context_recall': 0.79}</span>

<span class="ck"># Convert to pandas for analysis</span>
df = result.to_pandas()
df.to_csv(<span class="cs">"rag_eval_results.csv"</span>, index=<span class="cv">False</span>)
<span class="ck"># Identify lowest-scoring questions → improve retrieval or chunking for those</span></pre></div>
  </div>
</div>
</div><!-- end t5 -->


<!-- ══════════ TAB 6 — LANGSMITH ══════════ -->
<div id="t6" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔭</span><h3>LangSmith — Tracing and Evaluation Platform</h3><span class="tag tag-violet">Observability</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install langsmith

import os
os.environ[<span class="cs">"LANGCHAIN_TRACING_V2"</span>] = <span class="cs">"true"</span>
os.environ[<span class="cs">"LANGCHAIN_API_KEY"</span>]      = os.environ[<span class="cs">"LANGSMITH_API_KEY"</span>]
os.environ[<span class="cs">"LANGCHAIN_PROJECT"</span>]       = <span class="cs">"my-rag-project"</span>

<span class="ck"># All LangChain calls now auto-trace to LangSmith</span>
<span class="ck"># Go to smith.langchain.com → see every run</span>

<span class="ck"># ── Manual tracing (without LangChain) ───────────────</span>
from langsmith import Client, traceable

ls_client = Client()

@traceable(name=<span class="cs">"rag_query"</span>, run_type=<span class="cs">"chain"</span>)
def traced_rag_query(question: str) -> dict:
    <span class="ck"># Your RAG pipeline here — every call is auto-logged</span>
    result = rag_query(question)
    return result

<span class="ck"># ── Dataset-based evaluation ──────────────────────────</span>
<span class="ck"># Create a dataset in LangSmith</span>
dataset = ls_client.create_dataset(<span class="cs">"rag-eval-set"</span>)
ls_client.create_examples(
    inputs=[{<span class="cs">"question"</span>: t[<span class="cs">"question"</span>]} for t in RAG_TEST_SET],
    outputs=[{<span class="cs">"answer"</span>: t[<span class="cs">"ground_truth"</span>]} for t in RAG_TEST_SET],
    dataset_id=dataset.id
)

<span class="ck"># Define evaluator function</span>
def faithfulness_evaluator(run, example) -> dict:
    verdict = judge_faithfulness(
        context=run.outputs.get(<span class="cs">"context"</span>, <span class="cs">""</span>),
        answer=run.outputs.get(<span class="cs">"answer"</span>, <span class="cs">""</span>)
    )
    return {<span class="cs">"key"</span>: <span class="cs">"faithfulness"</span>, <span class="cs">"score"</span>: verdict.score,
            <span class="cs">"comment"</span>: verdict.reasoning}

<span class="ck"># Run evaluation against the dataset</span>
from langsmith.evaluation import evaluate as ls_evaluate

results = ls_evaluate(
    traced_rag_query,
    data=<span class="cs">"rag-eval-set"</span>,
    evaluators=[faithfulness_evaluator],
    experiment_prefix=<span class="cs">"v2-reranked"</span>
)
<span class="ck"># Results visible in LangSmith UI with charts, per-example scores, diffs</span></pre></div>
    <div class="ins"><p>💡 <strong>LangSmith's experiment comparison is its killer feature.</strong> Run your baseline (v1) and improved (v2) pipelines against the same dataset, and LangSmith shows a side-by-side diff of every metric. This is how you prove that a new reranker or chunking strategy improved quality without regressions.</p></div>
  </div>
</div>
</div><!-- end t6 -->


<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.confident-ai.com/" target="_blank" rel="noopener">DeepEval Documentation — docs.confident-ai.com</a></td><td>Complete reference for DeepEval metrics. Covers RAG, agent, and LLM evaluation with pytest integration.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.ragas.io/" target="_blank" rel="noopener">Ragas Documentation — docs.ragas.io</a></td><td>RAG-specific metrics framework. Best for faithfulness, context precision/recall evaluation.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.smith.langchain.com/" target="_blank" rel="noopener">LangSmith Documentation — docs.smith.langchain.com</a></td><td>Tracing, datasets, and experiment comparison. Essential for production AI observability.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://learn.deeplearning.ai/courses/building-and-evaluating-advanced-rag" target="_blank" rel="noopener">DeepLearning.AI: Building and Evaluating Advanced RAG (Free)</a></td><td>Covers RAG evaluation end-to-end with Ragas. Hands-on notebooks included.</td></tr>
    <tr><td class="res-type">Library</td><td><a href="https://github.com/promptfoo/promptfoo" target="_blank" rel="noopener">Promptfoo — github.com/promptfoo/promptfoo</a></td><td>Open-source prompt testing framework. Red-teaming, regression testing, and CI/CD integration.</td></tr>
  </tbody>
</table>
</div>


<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Full Eval Harness — RAG + Agent on Real Dataset</span>
    <span class="proj-dur">[Advanced] 4–5 days</span>
  </div>
  <div class="proj-body">
    <p>Build a complete evaluation harness that runs on every commit — the CI/CD layer for your AI system.</p>
    <h4>Part A — RAG Evaluation</h4>
    <ul>
      <li>Build a 30-question test set from your M18 "Chat With Your Docs" app with ground truth answers</li>
      <li>Run Ragas evaluation: faithfulness, answer_relevancy, context_precision, context_recall</li>
      <li>Run baseline (no reranking) vs enhanced (Cohere reranker from M17) — compare all 4 metrics</li>
      <li>Export results to CSV, identify the 5 worst-performing questions and diagnose why</li>
    </ul>
    <h4>Part B — Agent Evaluation</h4>
    <ul>
      <li>Build a 20-task test set for your M21 hardened agent with expected outcomes and required tools</li>
      <li>Run AgentEvaluator: task_success_rate, avg_turns, avg_cost, forbidden_violations</li>
      <li>Use LLM-as-judge for task success with calibrated faithfulness judge</li>
    </ul>
    <h4>Part C — CI Integration</h4>
    <ul>
      <li>Write a pytest test file using DeepEval assertions</li>
      <li>The test fails if: faithfulness &lt; 0.7 OR task_success_rate &lt; 0.8 OR any forbidden tool used</li>
      <li>Run locally: <code>pytest eval_tests.py -v</code></li>
    </ul>
    <p><strong>Skills:</strong> Ragas, DeepEval, LLM-as-judge, AgentEvaluator, pytest integration, regression baselines</p>
  </div>
</div>
</div>


<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Build and Calibrate an LLM Judge</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a faithfulness judge, calibrate it against human ratings, and measure its reliability.</p>
    <div class="lab-step"><div class="sn">1</div><div>Generate 30 RAG outputs (question + context + answer) from your M18 pipeline — 10 clearly faithful, 10 clearly unfaithful (manually inject hallucinations), 10 borderline cases.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Rate all 30 yourself (0.0, 0.5, or 1.0). These are your human ratings — your gold set.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run your LLM judge (Claude Haiku) on all 30. Compute pearson_r between human and judge scores using calibrate_judge().</div></div>
    <div class="lab-step"><div class="sn">4</div><div>If pearson_r &lt; 0.7, iterate on the judge prompt — add clearer scoring criteria, add examples. Re-run until calibrated.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Test the 4 known biases: (a) verbosity — does a longer answer get higher score? (b) position — does ordering change scores in A/B? (c) self-preference — does Haiku prefer Haiku outputs? (d) confidence — does a confident wrong answer score higher?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Ragas End-to-End on Your RAG System</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Run a full Ragas evaluation and use the results to drive a concrete improvement.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a 20-question dataset for your M18 RAG system. Include: question, ground_truth, contexts (retrieved chunks), answer (your pipeline's output).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run Ragas with all 4 metrics. Print the aggregate scores and the per-question DataFrame.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Identify the 3 questions with the lowest faithfulness score. Manually inspect: what did the answer say that wasn't in the context? Is this a retrieval failure or generation failure?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Fix the lowest-performing failure (e.g. rechunk, add reranker, strengthen grounding prompt). Re-run Ragas. Document: which metric improved? Did any regress?</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Document the regression test rule:</strong> "Our faithfulness must be ≥ X and context_recall must be ≥ Y on this test set." Write a pytest assertion that enforces this.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Agent Evaluation — Measure Before You Improve</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Establish a baseline for your M21 agent, identify the most common failure pattern, and measure improvement.</div></p>
    <div class="lab-step"><div class="sn">1</div><div>Write a 15-task test set for your M21 hardened agent covering: 5 simple (1-2 tools), 5 medium (3-4 tools), 5 complex (5+ tools or multi-step reasoning).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run AgentEvaluator.evaluate_batch(). Record: task_success_rate, avg_turns, avg_cost, forbidden_violations.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>For every failed task (task_success < 0.6), read the judge_reasoning and classify the failure: wrong tool selected, correct tool but wrong args, took too many turns, gave partial answer.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Fix the most common failure category (likely wrong tool selection or bad tool description). Re-run the evaluation. Show the before/after task_success_rate.</div></div>
  </div>
</div>
</div><!-- end t9 -->


<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P6-M22 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can name and define the 4 RAG metrics: faithfulness, answer relevancy, context precision, context recall</li>
  <li>Can name and define the 4 agent metrics: task success rate, tool call precision, trajectory accuracy, cost per task</li>
  <li>Can implement an LLM-as-judge with Pydantic structured output (score, reasoning, passed)</li>
  <li>Know the 4 LLM judge biases: position bias, verbosity bias, self-preference, sycophancy</li>
  <li>Can calibrate a judge against human ratings using pearson_r — r ≥ 0.7 is acceptable</li>
  <li>Can build a RAG test set with question, ground_truth, expected_source fields</li>
  <li>Can run a Ragas evaluation and interpret the per-metric scores</li>
  <li>Can use Ragas results to identify and fix specific failure cases</div></li>
  <li>Can implement AgentTestCase with required_tools and forbidden_tools constraints</li>
  <li>Can run AgentEvaluator.evaluate_batch() and report task_success_rate and avg_cost</li>
  <li>Can set up LangSmith tracing with @traceable decorator</li>
  <li>Can create a LangSmith dataset and run an experiment with custom evaluators</li>
  <li>Can use DeepEval metrics in a pytest test that fails on quality regression</li>
  <li>Understand the eval-improve loop: measure baseline → find worst cases → fix → re-measure → repeat</li>
  <li>Completed Lab 1: LLM judge built and calibrated against human ratings</li>
  <li>Completed Lab 2: Ragas evaluation with improvement iteration</li>
  <li>Completed Lab 3: Agent evaluation baseline + fix + re-measure cycle</li>
  <li>Milestone project: full eval harness with pytest CI integration pushed to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>Part 6 Complete!</strong> Move to <strong>Part 7 — Production &amp; Deployment</strong> to learn how to ship everything you've built into a real production environment.</p>
</div>
</div>

<!-- ── PART 6 COMPLETION BANNER ── -->
<div class="part-complete">
  <h3>🎉 Part 6 — Agents, Workflows &amp; Evaluation Complete!</h3>
  <p>You can now build, harden, and measure production-grade AI agent systems.</p>
  <div class="part-skills">
    <div class="ps-item">Build agents from scratch with ReAct loops</div>
    <div class="ps-item">Design stateful agents with LangGraph</div>
    <div class="ps-item">Implement human-in-the-loop with interrupt/resume</div>
    <div class="ps-item">Design reliable tools with proper error contracts</div>
    <div class="ps-item">Choose the right workflow pattern (chain/route/parallel/agent)</div>
    <div class="ps-item">Detect and contain all 5 agent failure modes</div>
    <div class="ps-item">Implement cost circuit breakers and structured logging</div>
    <div class="ps-item">Evaluate RAG with Ragas and agents with LLM-as-judge</div>
  </div>
</div>

<div class="mod-nav">
  <a href="/learning/ai-ml/part6-agents/p6-m21-failure-handling/">← P6-M21: Failure Handling</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part7-production/p7-m23-fastapi-prod/">Next: P7-M23 — FastAPI Production →</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn,.tab-thumb').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.cl li').forEach((li, i) => {
    const key = 'p6m22-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
