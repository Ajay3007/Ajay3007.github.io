---
layout: default
title: "P6-M20 - Tool Design, Workflow Patterns & When NOT to Use Agents"
permalink: /learning/ai-ml/part6-agents/p6-m20-tool-design/
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
.note{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
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
/* pattern cards */
.pattern-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.8rem;margin:.8rem 0}
.pc{border-radius:10px;padding:1rem 1.1rem;border:1.5px solid}
.pc h4{font-size:.9rem;font-weight:700;margin:0 0 .4rem;border:none}
.pc p{font-size:.82rem;line-height:1.6;margin:0 0 .35rem;color:var(--text-color,#444)}
.pc .use{font-size:.75rem;font-family:monospace;font-weight:600}
.pc-prompt{background:#f5f0ff;border-color:#c4b5fd}.pc-prompt h4{color:#4c1d95}.pc-prompt .use{color:#7c3aed}
.pc-routing{background:#e0f2fe;border-color:#7dd3fc}.pc-routing h4{color:#0c4a6e}.pc-routing .use{color:#0284c7}
.pc-parallel{background:#e2f0e8;border-color:#6ee7b7}.pc-parallel h4{color:#065f46}.pc-parallel .use{color:#059669}
.pc-orchestrator{background:#faeee4;border-color:#fdba74}.pc-orchestrator h4{color:#9a3412}.pc-orchestrator .use{color:#ea580c}
.pc-evaluator{background:#ede8f5;border-color:#c4b5fd}.pc-evaluator h4{color:#5b21b6}.pc-evaluator .use{color:#7c3aed}
/* decision matrix */
.dm-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.83rem}
.dm-table th{background:#1e0a3a;color:#ede9fe;padding:.55rem .8rem;text-align:left;font-weight:700;font-size:.75rem}
.dm-table td{padding:.55rem .8rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.55}
.dm-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.dm-use{color:#059669;font-weight:600}.dm-avoid{color:#dc2626;font-weight:600}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 6 — Agents, Workflows &amp; Evaluation &nbsp;·&nbsp; Module 20 of 22</div>
  <div class="mod-title">Tool Design, Workflow Patterns &amp; When NOT to Use Agents</div>
  <div class="mod-subtitle">Design reliable tools, pick the right workflow pattern, and know when simpler is better</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟠 Intermediate–Advanced</span>
    <span class="mod-pill">🔧 LangGraph · FastAPI · Anthropic</span>
    <span class="mod-pill">📋 Prerequisite: P6-M19</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🔧 Tool Design</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🗺 Workflow Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🚫 When NOT Agents</button>
  <button class="tab-btn" onclick="vt(event,'t4')">⚡ Parallel Workflows</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🎯 Orchestrator-Subagent</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-violet">Design Thinking</span></div>
  <div class="cp-body">
    <p>Building agents that work in a notebook is easy. Building agents that work reliably in production is hard. This module covers the engineering judgment that separates toy agents from production ones: how to design tools that are reliable, how to choose the right workflow architecture, and critically — when a simple chain beats a complex agent every time.</p>
    <ul>
      <li><strong>Tool design principles</strong> — idempotency, error contracts, atomicity, what makes a good vs bad tool</li>
      <li><strong>The five workflow patterns</strong> — prompt chaining, routing, parallelisation, orchestrator-subagent, evaluator-optimizer</li>
      <li><strong>When NOT to use agents</strong> — the decision matrix that saves you from over-engineering</li>
      <li><strong>Parallel workflows</strong> — fan-out/fan-in patterns, when to parallelise, how to handle partial failures</li>
      <li><strong>Orchestrator-subagent</strong> — breaking complex goals into specialised sub-agents with handoff</li>
    </ul>
  </div>
</div>
</div>


<!-- ══════════ TAB 1 — TOOL DESIGN ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>What Makes a Good Tool</h3><span class="tag tag-violet">Design Principles</span></div>
  <div class="cp-body">
    <p>A tool is the interface between your agent and the real world. Bad tool design is the #1 source of agent failures — not the LLM, not the prompting.</p>
    <div class="cb"><pre><span class="ck"># ── PRINCIPLE 1: Idempotent tools ────────────────────</span>
<span class="ck"># If the agent calls a tool twice with the same args, the result should be the same</span>
<span class="ck"># and no duplicate side effects should occur</span>

<span class="ck"># BAD: calling twice creates two records</span>
def create_ticket(title: str, description: str) -> dict:
    return db.insert(<span class="cs">"tickets"</span>, {<span class="cs">"title"</span>: title, <span class="cs">"description"</span>: description})

<span class="ck"># GOOD: upsert on a natural key — safe to call multiple times</span>
def create_or_get_ticket(title: str, description: str) -> dict:
    existing = db.find_one(<span class="cs">"tickets"</span>, {<span class="cs">"title"</span>: title})
    if existing:
        return existing
    return db.insert(<span class="cs">"tickets"</span>, {<span class="cs">"title"</span>: title, <span class="cs">"description"</span>: description})

<span class="ck"># ── PRINCIPLE 2: Explicit error contracts ────────────</span>
<span class="ck"># Never raise exceptions — return structured errors the agent can understand</span>

<span class="ck"># BAD: agent receives an unhandled exception, gets confused</span>
def get_user(user_id: str) -> dict:
    return db.get(<span class="cs">"users"</span>, user_id)   <span class="ck"># raises KeyError if not found</span>

<span class="ck"># GOOD: structured error the agent can reason about</span>
def get_user(user_id: str) -> dict:
    user = db.find_one(<span class="cs">"users"</span>, {<span class="cs">"id"</span>: user_id})
    if not user:
        return {<span class="cs">"error"</span>: <span class="cs">"USER_NOT_FOUND"</span>,
                <span class="cs">"message"</span>: <span class="cs">f"No user with id '{user_id}'"</span>,
                <span class="cs">"suggestion"</span>: <span class="cs">"Try searching by email with search_users()"</span>}
    return {<span class="cs">"success"</span>: <span class="cv">True</span>, <span class="cs">"user"</span>: user}

<span class="ck"># ── PRINCIPLE 3: Atomic operations ───────────────────</span>
<span class="ck"># One tool should do ONE thing — not a chain of things</span>

<span class="ck"># BAD: one tool does too much — partial failures are unrecoverable</span>
def process_order(order_id: str) -> dict:
    validate_stock()
    charge_payment()
    send_confirmation_email()
    update_inventory()

<span class="ck"># GOOD: separate tools, agent orchestrates the sequence</span>
def validate_stock(items: list) -> dict: ...
def charge_payment(amount: float, card_id: str) -> dict: ...
def send_confirmation_email(order_id: str, email: str) -> dict: ...
def update_inventory(items: list, delta: int) -> dict: ...</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Tool Description Engineering</h3><span class="tag tag-blue">Selection Precision</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># The description determines WHEN the agent calls the tool.</span>
<span class="ck"># Bad descriptions → wrong tool selection → wrong results.</span>

<span class="ck"># ── Pattern: Use When / Don't Use When ───────────────</span>
SEARCH_TOOL = {
    <span class="cs">"name"</span>: <span class="cs">"search_knowledge_base"</span>,
    <span class="cs">"description"</span>: <span class="cs">"""Search the internal knowledge base for product documentation,
API references, and troubleshooting guides.

USE when:
- User asks about product features, configuration, or known issues
- User needs step-by-step instructions from documentation
- User references a specific version or release note

DO NOT USE when:
- Question is about general programming (use your training knowledge)
- Question requires real-time data (use get_live_status instead)
- Question is a math calculation (use calculate instead)"""</span>,
    <span class="cs">"input_schema"</span>: {
        <span class="cs">"type"</span>: <span class="cs">"object"</span>,
        <span class="cs">"properties"</span>: {
            <span class="cs">"query"</span>: {
                <span class="cs">"type"</span>: <span class="cs">"string"</span>,
                <span class="cs">"description"</span>: <span class="cs">"Natural language search query. Be specific. Example: 'how to configure DPDK hugepages on Linux'"</span>
            },
            <span class="cs">"version"</span>: {
                <span class="cs">"type"</span>: <span class="cs">"string"</span>,
                <span class="cs">"description"</span>: <span class="cs">"Optionally filter by product version, e.g. '23.11'. Omit for all versions."</span>
            }
        },
        <span class="cs">"required"</span>: [<span class="cs">"query"</span>]
    }
}

<span class="ck"># ── Consistent return schema ──────────────────────────</span>
<span class="ck"># All tools should return a dict with consistent keys</span>
<span class="ck"># so the agent can reliably check for success/failure</span>

def tool_success(data: dict, message: str = <span class="cs">""</span>) -> dict:
    return {<span class="cs">"ok"</span>: <span class="cv">True</span>, <span class="cs">"data"</span>: data, <span class="cs">"message"</span>: message}

def tool_error(code: str, message: str, suggestion: str = <span class="cs">""</span>) -> dict:
    return {<span class="cs">"ok"</span>: <span class="cv">False</span>, <span class="cs">"error_code"</span>: code,
            <span class="cs">"message"</span>: message, <span class="cs">"suggestion"</span>: suggestion}</pre></div>
    <div class="ins"><p>💡 <strong>Tool names are critical.</strong> <code>search</code> is ambiguous — the agent doesn't know what it searches. <code>search_knowledge_base</code>, <code>search_web</code>, <code>search_customer_records</code> are unambiguous. When you have multiple search tools, the names must make the distinction obvious without reading the description.</p></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>Tool Safety — Scope Limiting and Validation</h3><span class="tag tag-teal">Production</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Scope limiting — tools should only do what they say</span>
def query_database(sql: str, allowed_tables: list[str] = None) -> dict:
    <span class="ck"># Validate it's a SELECT (never allow INSERT/DELETE/UPDATE from agent)</span>
    if not sql.strip().upper().startswith(<span class="cs">"SELECT"</span>):
        return tool_error(<span class="cs">"FORBIDDEN_OPERATION"</span>,
                          <span class="cs">"Only SELECT queries are allowed"</span>,
                          <span class="cs">"Use write_record() for data modification"</span>)

    <span class="ck"># Validate only allowed tables are accessed</span>
    if allowed_tables:
        import re
        tables_in_query = re.findall(r<span class="cs">'FROM\s+(\w+)'</span>, sql, re.IGNORECASE)
        for t in tables_in_query:
            if t not in allowed_tables:
                return tool_error(<span class="cs">"TABLE_NOT_ALLOWED"</span>,
                                  <span class="cs">f"Table {t!r} not in allowed list: {allowed_tables}"</span>)
    try:
        results = db.execute(sql)
        return tool_success({<span class="cs">"rows"</span>: results, <span class="cs">"count"</span>: len(results)})
    except Exception as e:
        return tool_error(<span class="cs">"QUERY_ERROR"</span>, str(e))

<span class="ck"># Rate limiting per tool to prevent runaway agents</span>
from collections import defaultdict
import time

_tool_calls = defaultdict(list)
RATE_LIMITS = {<span class="cs">"search_web"</span>: (<span class="cv">10</span>, <span class="cv">60</span>)}   <span class="ck"># 10 calls per 60 seconds</span>

def rate_limit_check(tool_name: str) -> bool:
    if tool_name not in RATE_LIMITS:
        return <span class="cv">True</span>
    max_calls, window = RATE_LIMITS[tool_name]
    now = time.time()
    calls = [t for t in _tool_calls[tool_name] if now - t < window]
    _tool_calls[tool_name] = calls
    if len(calls) >= max_calls:
        return <span class="cv">False</span>
    _tool_calls[tool_name].append(now)
    return <span class="cv">True</span></pre></div>
  </div>
</div>
</div><!-- end t1 -->


<!-- ══════════ TAB 2 — WORKFLOW PATTERNS ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🗺</span><h3>The Five Workflow Patterns</h3><span class="tag tag-violet">Architecture Toolkit</span></div>
  <div class="cp-body">
    <p>These five patterns cover 90% of real AI system architectures. Knowing them prevents you from reaching for a full agent when a simpler pattern will do.</p>
    <div class="pattern-grid">
      <div class="pc pc-prompt">
        <h4>Prompt Chaining</h4>
        <p>LLM output of step N feeds as input to step N+1. Each step does one thing well.</p>
        <div class="use">Use: linear multi-step tasks, document pipelines</div>
      </div>
      <div class="pc pc-routing">
        <h4>Routing</h4>
        <p>A classifier LLM routes input to one of several specialised handlers. Each handler is optimised for its class.</p>
        <div class="use">Use: multi-category support, mixed content types</div>
      </div>
      <div class="pc pc-parallel">
        <h4>Parallelisation</h4>
        <p>Multiple LLM calls run concurrently on the same input. Results are aggregated (voting or merge).</p>
        <div class="use">Use: independent subtasks, multi-perspective analysis</div>
      </div>
      <div class="pc pc-orchestrator">
        <h4>Orchestrator-Subagent</h4>
        <p>A planning LLM breaks the task into subtasks and dispatches to specialised subagents. Results are synthesised.</p>
        <div class="use">Use: complex multi-domain tasks, large research jobs</div>
      </div>
      <div class="pc pc-evaluator">
        <h4>Evaluator-Optimizer</h4>
        <p>One LLM generates output, another evaluates quality and provides feedback for improvement. Loops until quality threshold met.</p>
        <div class="use">Use: code generation, content quality requirements</div>
      </div>
    </div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Prompt Chaining — Implementation</h3><span class="tag tag-blue">Most Common</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Prompt chaining: clean, testable, each step independently improvable</span>
<span class="ck"># Each gate() call validates before passing to the next step</span>

def chain_extract_summarise_translate(document: str, target_lang: str) -> dict:
    <span class="ck"># Step 1: Extract key facts</span>
    facts = call_llm(
        system=<span class="cs">"Extract the 5 most important factual claims from this document. Output as a numbered list."</span>,
        user=document
    )
    if not facts:
        return {<span class="cs">"error"</span>: <span class="cs">"Extraction failed"</span>}

    <span class="ck"># Step 2: Summarise the facts</span>
    summary = call_llm(
        system=<span class="cs">"Write a 2-3 sentence executive summary based on these key facts."</span>,
        user=facts
    )

    <span class="ck"># Step 3: Translate (only if not English)</span>
    if target_lang.lower() not in (<span class="cs">"en"</span>, <span class="cs">"english"</span>):
        translated = call_llm(
            system=<span class="cs">f"Translate to {target_lang}. Maintain tone and technical terms."</span>,
            user=summary
        )
    else:
        translated = summary

    return {<span class="cs">"facts"</span>: facts, <span class="cs">"summary"</span>: summary, <span class="cs">"translated"</span>: translated}

<span class="ck"># Evaluator-Optimizer pattern</span>
def generate_with_quality_loop(prompt: str, max_iterations: int = <span class="cv">3</span>) -> str:
    output = call_llm(system=<span class="cs">"Generate a response."</span>, user=prompt)

    for i in range(max_iterations):
        evaluation = call_llm(
            system=<span class="cs">"""Evaluate this output for: accuracy, completeness, clarity.
Return JSON: {"score": 1-10, "issues": [...], "passed": bool}"""</span>,
            user=<span class="cs">f"Original prompt: {prompt}\n\nOutput: {output}"</span>
        )
        import json
        result = json.loads(evaluation)
        if result.get(<span class="cs">"passed"</span>) or result.get(<span class="cs">"score"</span>, <span class="cv">0</span>) >= <span class="cv">8</span>:
            break

        <span class="ck"># Regenerate with feedback</span>
        output = call_llm(
            system=<span class="cs">"Improve the output based on this feedback."</span>,
            user=<span class="cs">f"Previous output: {output}\n\nIssues: {result['issues']}"</span>
        )
    return output</pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>Routing Pattern — LLM as Classifier</h3><span class="tag tag-teal">Scalable</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from typing import Literal
from pydantic import BaseModel
import instructor, anthropic

instr_client = instructor.from_anthropic(anthropic.Anthropic())

class RouteDecision(BaseModel):
    category: Literal[<span class="cs">"billing"</span>, <span class="cs">"technical"</span>, <span class="cs">"general"</span>, <span class="cs">"complaint"</span>]
    confidence: float
    reasoning: str

def route_support_ticket(ticket: str) -> RouteDecision:
    return instr_client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,   <span class="ck"># cheap model for routing</span>
        max_tokens=<span class="cv">100</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: <span class="cs">f"Classify this support ticket:\n\n{ticket}"</span>}],
        response_model=RouteDecision
    )

<span class="ck"># Specialised handlers — each optimised for its category</span>
HANDLERS = {
    <span class="cs">"billing"</span>:   handle_billing_ticket,
    <span class="cs">"technical"</span>: handle_technical_ticket,
    <span class="cs">"general"</span>:   handle_general_ticket,
    <span class="cs">"complaint"</span>: handle_complaint_ticket,
}

def process_ticket(ticket: str) -> dict:
    route = route_support_ticket(ticket)
    handler = HANDLERS[route.category]
    return handler(ticket)</pre></div>
  </div>
</div>
</div><!-- end t2 -->


<!-- ══════════ TAB 3 — WHEN NOT AGENTS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🚫</span><h3>When NOT to Use Agents — The Decision Matrix</h3><span class="tag tag-red">Most Important Lesson</span></div>
  <div class="cp-body">
    <p>The most common mistake in AI engineering is reaching for agents when a simpler architecture would be more reliable, cheaper, and faster to debug. Agents introduce non-determinism — every additional LLM decision is a point of potential failure.</p>
    <table class="dm-table">
      <thead><tr><th>Situation</th><th>Use Agent?</th><th>Better Alternative</th></tr></thead>
      <tbody>
        <tr><td>Steps are always the same</td><td class="dm-avoid">✗ No</td><td>Prompt chain — deterministic, testable</td></tr>
        <tr><td>Steps depend on content classification</td><td class="dm-avoid">✗ No</td><td>Routing — LLM classifier + fixed handlers</td></tr>
        <tr><td>Independent subtasks on same input</td><td class="dm-avoid">✗ No</td><td>Parallelisation — asyncio.gather()</td></tr>
        <tr><td>Single API call answers the question</td><td class="dm-avoid">✗ No</td><td>Simple function call or RAG query</td></tr>
        <tr><td>Steps are known, but order varies by input</td><td class="dm-avoid">✗ No</td><td>Routing with multiple fixed chains</td></tr>
        <tr><td>Task requires dynamic tool selection</td><td class="dm-use">✓ Yes</td><td>—</td></tr>
        <tr><td>Number of steps not known in advance</td><td class="dm-use">✓ Yes</td><td>—</td></tr>
        <tr><td>Task requires reasoning about partial results</td><td class="dm-use">✓ Yes</td><td>—</td></tr>
        <tr><td>Task spans multiple API/DB systems dynamically</td><td class="dm-use">✓ Yes</td><td>—</td></tr>
      </tbody>
    </table>
    <div class="cb"><pre><span class="ck"># The "do I need an agent?" test — ask these questions in order:</span>
<span class="ck">#</span>
<span class="ck"># 1. Can I write the steps as a fixed Python function?</span>
<span class="ck">#    YES → use a chain or function call. NOT an agent.</span>
<span class="ck">#</span>
<span class="ck"># 2. Do the steps vary, but can I enumerate all the variations?</span>
<span class="ck">#    YES → use routing. NOT an agent.</span>
<span class="ck">#</span>
<span class="ck"># 3. Are the subtasks independent and can run in parallel?</span>
<span class="ck">#    YES → use asyncio.gather(). NOT an agent.</span>
<span class="ck">#</span>
<span class="ck"># 4. Is the sequence truly unpredictable until you see the data?</span>
<span class="ck">#    YES → now consider an agent.</span>
<span class="ck">#</span>
<span class="ck"># If you reach question 4 — also ask:</span>
<span class="ck"># - Can I tolerate non-determinism in production?</span>
<span class="ck"># - Do I have evaluation/monitoring to catch failures?</span>
<span class="ck"># - Is the latency and cost of multi-turn LLM reasoning acceptable?</span></pre></div>
    <div class="warn"><p>⚠️ <strong>Agents are harder to test, harder to debug, more expensive, and slower than deterministic pipelines.</strong> Every additional LLM call is a potential point of failure, cost, and latency. Anthropic's own guidelines say: augment agents with workflows wherever possible, and only add true autonomy where it is genuinely necessary.</p></div>
  </div>
</div>
</div><!-- end t3 -->


<!-- ══════════ TAB 4 — PARALLEL WORKFLOWS ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Parallel Workflows — Fan-Out / Fan-In</h3><span class="tag tag-violet">Performance Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import asyncio, anthropic

async_client = anthropic.AsyncAnthropic()

async def call_llm_async(system: str, user: str) -> str:
    response = await async_client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">1024</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user}],
        system=system
    )
    return response.content[<span class="cv">0</span>].text

<span class="ck"># ── Pattern 1: Same input, multiple perspectives ──────</span>
async def multi_perspective_review(code: str) -> dict:
    security, performance, readability = await asyncio.gather(
        call_llm_async(<span class="cs">"Review this code for security vulnerabilities only."</span>, code),
        call_llm_async(<span class="cs">"Review this code for performance issues only."</span>, code),
        call_llm_async(<span class="cs">"Review this code for readability and maintainability only."</span>, code),
    )
    <span class="ck"># Synthesise all three perspectives</span>
    synthesis = await call_llm_async(
        <span class="cs">"Combine these three code reviews into a single prioritised action list."</span>,
        <span class="cs">f"Security:\n{security}\n\nPerformance:\n{performance}\n\nReadability:\n{readability}"</span>
    )
    return {<span class="cs">"security"</span>: security, <span class="cs">"performance"</span>: performance,
            <span class="cs">"readability"</span>: readability, <span class="cs">"synthesis"</span>: synthesis}

<span class="ck"># ── Pattern 2: Different inputs, same processing ──────</span>
async def process_documents_parallel(documents: list[str]) -> list[str]:
    summaries = await asyncio.gather(
        *[call_llm_async(<span class="cs">"Summarise in 2 sentences."</span>, doc) for doc in documents]
    )
    return list(summaries)

<span class="ck"># ── Pattern 3: Voting — run N times, take majority ────</span>
async def classify_with_voting(text: str, n: int = <span class="cv">3</span>) -> str:
    from collections import Counter
    labels = await asyncio.gather(
        *[call_llm_async(
            <span class="cs">"Classify as POSITIVE, NEGATIVE, or NEUTRAL. Reply with one word only."</span>, text
          ) for _ in range(n)]
    )
    labels = [l.strip().upper() for l in labels]
    return Counter(labels).most_common(<span class="cv">1</span>)[<span class="cv">0</span>][<span class="cv">0</span>]

<span class="ck"># ── Handling partial failures ──────────────────────────</span>
async def gather_with_fallback(coroutines: list) -> list:
    results = await asyncio.gather(*coroutines, return_exceptions=<span class="cv">True</span>)
    processed = []
    for r in results:
        if isinstance(r, Exception):
            processed.append({<span class="cs">"error"</span>: str(r)})
        else:
            processed.append(r)
    return processed</pre></div>
  </div>
</div>
</div><!-- end t4 -->


<!-- ══════════ TAB 5 — ORCHESTRATOR ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Orchestrator-Subagent Pattern</h3><span class="tag tag-violet">Complex Tasks</span></div>
  <div class="cp-body">
    <p>For complex tasks that span multiple domains (research + analysis + writing), an orchestrator LLM plans and dispatches to specialised subagents. Each subagent has its own tools and system prompt optimised for its domain.</p>
    <div class="cb"><pre>from pydantic import BaseModel
from typing import List, Literal
import instructor, anthropic, asyncio

instr_client = instructor.from_anthropic(anthropic.Anthropic())

class SubTask(BaseModel):
    agent:       Literal[<span class="cs">"researcher"</span>, <span class="cs">"analyst"</span>, <span class="cs">"writer"</span>]
    task:        str
    depends_on:  List[int] = []   <span class="ck"># indices of tasks that must complete first</span>

class OrchestratorPlan(BaseModel):
    goal_summary: str
    subtasks:    List[SubTask]

def orchestrate(user_goal: str) -> str:
    <span class="ck"># 1. Orchestrator plans the work</span>
    plan = instr_client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">1024</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>:
            <span class="cs">f"""Break this goal into subtasks for specialised agents:
Goal: {user_goal}

Available agents:
- researcher: searches web, finds facts, gathers data
- analyst: processes data, identifies patterns, creates structured analysis
- writer: synthesises research and analysis into coherent written output"""</span>}],
        response_model=OrchestratorPlan
    )

    results = {}

    <span class="ck"># 2. Execute subtasks in dependency order</span>
    for i, subtask in enumerate(plan.subtasks):
        <span class="ck"># Wait for dependencies</span>
        context = <span class="cs">"\n\n"</span>.join(
            <span class="cs">f"Result from task {j}: {results[j]}"</span>
            for j in subtask.depends_on if j in results
        )

        <span class="ck"># Dispatch to specialised subagent</span>
        AGENT_SYSTEMS = {
            <span class="cs">"researcher"</span>: <span class="cs">"You are a researcher. Find accurate information. Cite sources."</span>,
            <span class="cs">"analyst"</span>:   <span class="cs">"You are an analyst. Process data systematically. Be precise."</span>,
            <span class="cs">"writer"</span>:    <span class="cs">"You are a technical writer. Write clearly for the target audience."</span>,
        }
        task_with_context = subtask.task
        if context:
            task_with_context = <span class="cs">f"Prior results:\n{context}\n\nYour task: {subtask.task}"</span>

        results[i] = run_agent(
            user_message=task_with_context,
            system=AGENT_SYSTEMS[subtask.agent]
        )

    <span class="ck"># 3. Final synthesis</span>
    all_results = <span class="cs">"\n\n"</span>.join(<span class="cs">f"Task {i}: {r}"</span> for i, r in results.items())
    return run_agent(
        user_message=<span class="cs">f"Goal: {user_goal}\n\nAll subtask results:\n{all_results}\n\nSynthesize into a complete answer."</span>,
        system=<span class="cs">"You are a senior analyst. Synthesise all results into a coherent, complete response."</span>
    )</pre></div>
  </div>
</div>
</div><!-- end t5 -->


<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Article</td><td><a href="https://www.anthropic.com/research/building-effective-agents" target="_blank" rel="noopener">Anthropic: Building Effective Agents — anthropic.com/research</a></td><td>The definitive guide on workflow patterns, when to use agents, and how to design reliable systems. Required reading.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://langchain-ai.github.io/langgraph/concepts/multi_agent/" target="_blank" rel="noopener">LangGraph: Multi-Agent Systems — langchain-ai.github.io/langgraph</a></td><td>Supervisor patterns, handoff protocols, and shared memory between agents.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://platform.openai.com/docs/guides/orchestration" target="_blank" rel="noopener">OpenAI: A Practical Guide to Building Agents — cdn.openai.com</a></td><td>OpenAI's agent patterns including orchestrator-subagent and guardrail design.</td></tr>
  </tbody>
</table>
</div>


<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Multi-Pattern Pipeline — Same Task, Three Architectures</span>
    <span class="proj-dur">[Advanced] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build the same complex task using three different architectures and compare reliability, cost, and latency. This is the exercise that builds real engineering judgment.</p>
    <h4>Task: Competitive Intelligence Report</h4>
    <p>Given a company name, produce a structured report: executive summary, products/services, market position, recent news, SWOT analysis.</p>
    <h4>Architecture 1 — Prompt Chain</h4>
    <ul>
      <li>5 fixed sequential LLM calls, each producing one section</li>
      <li>Each step's output feeds the next as context</li>
    </ul>
    <h4>Architecture 2 — Parallel + Synthesis</h4>
    <ul>
      <li>4 parallel calls (exec summary, products, market, news)</li>
      <li>1 final synthesis call combining all results</li>
    </ul>
    <h4>Architecture 3 — Orchestrator-Subagent</h4>
    <ul>
      <li>Orchestrator plans and dispatches to researcher + analyst + writer subagents</li>
      <li>Each subagent has its own tools and system prompt</li>
    </ul>
    <h4>Evaluation</h4>
    <ul>
      <li>Run all three on the same 3 companies. Measure: total latency, total tokens, total cost, output quality (manual 1-5 rating)</li>
      <li>Document: which architecture would you ship and why?</li>
    </ul>
    <p><strong>Skills:</strong> Prompt chaining, asyncio.gather, orchestrator-subagent, cost/latency measurement, architecture trade-off analysis</p>
  </div>
</div>
</div>


<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Tool Design Audit — Fix Three Bad Tools</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Apply the tool design principles to real tool definitions and measure the improvement.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write three intentionally bad tools: (a) a <code>do_stuff(input)</code> with vague name and description, (b) a tool that raises an exception on error instead of returning a dict, (c) a tool that does 3 things (fetch + process + save) in one call.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Connect these to an agent. Run 5 queries that should trigger these tools. Record how often the agent: selects the wrong tool, crashes on the exception, or produces inconsistent results from the multi-purpose tool.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Fix each tool: rename with specific verb+noun, return structured error dicts, split into atomic operations. Rerun the same 5 queries. Compare failure rates.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add the USE/DON'T USE pattern to each tool description. Test with ambiguous queries that could trigger multiple tools — does selection improve?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Pattern Selection — Choose the Right Architecture</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Practice the decision matrix by correctly categorising 10 real tasks.</p>
    <div class="lab-step"><div class="sn">1</div><div>For each of the following tasks, apply the decision matrix and determine the right pattern (chain, routing, parallel, agent, orchestrator): (a) translate a document to 5 languages, (b) answer a customer support email (billing/technical/general), (c) generate a test suite for a function, (d) research and write a 10-page market analysis, (e) summarise a meeting transcript into action items.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement two of the non-agent solutions (chain or parallel). Measure latency and cost vs a naive "just use an agent" implementation for the same tasks.</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>Document:</strong> For which tasks was the simpler architecture actually better? What would have gone wrong with the agent approach?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Parallel Fan-Out — Measure Real Speedup</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Quantify the latency benefit of parallelisation on a real multi-perspective task.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take a 500-word technical document. Build a sequential pipeline: 4 sequential LLM calls for security, performance, readability, and documentation reviews. Time the total.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Build the parallel version using asyncio.gather for the same 4 reviews. Time the total.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Add a 5th synthesis step (sequential in both versions). Compare: total time, total tokens, quality of synthesis output.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Test partial failure handling: make one of the 4 review calls intentionally fail. Does gather(return_exceptions=True) allow the other 3 to succeed? Does the synthesis handle the missing review gracefully?</div></div>
  </div>
</div>
</div><!-- end t8 -->


<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P6-M20 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can name the 3 tool design principles: idempotency, explicit error contracts, atomicity</li>
  <li>All tools return a dict — never raise exceptions that the agent cannot handle</li>
  <li>Tool names are verb+noun specific: search_knowledge_base not search</li>
  <li>Tool descriptions include "USE when" and "DON'T USE when" sections</li>
  <li>Can implement scope limiting: SQL tools allow only SELECT; rate limiting per tool</li>
  <li>Can name all 5 workflow patterns: prompt chaining, routing, parallelisation, orchestrator-subagent, evaluator-optimizer</li>
  <li>Can apply the "do I need an agent?" decision matrix to a new task</li>
  <li>Know that chains are preferred over agents when steps are predictable</li>
  <li>Can implement the evaluator-optimizer loop: generate → evaluate → improve → repeat</li>
  <li>Can implement routing with a Pydantic classifier and specialised handlers</li>
  <li>Can implement parallel fan-out with asyncio.gather for independent LLM calls</li>
  <li>Know to use return_exceptions=True for fault-tolerant parallel calls</div></li>
  <li>Can implement voting (N parallel calls, majority answer) for classification tasks</li>
  <li>Can implement orchestrator-subagent: planning → dispatch → synthesis</li>
  <li>Completed Lab 1: tool design audit with before/after failure rate comparison</li>
  <li>Completed Lab 2: pattern selection exercise with implementation and measurement</li>
  <li>Completed Lab 3: parallel fan-out speedup measurement with partial failure test</li>
  <li>Milestone project pushed to GitHub: 3-architecture comparison with findings</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P6-M21 — Failure Handling in Agents</strong>. You now know how to design good agents. M21 covers what to do when they go wrong — which they will, at scale.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part6-agents/p6-m19-agent-loops/' | relative_url }}">← P6-M19: Agent Loops</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part6-agents/p6-m21-failure-handling/' | relative_url }}">Next: P6-M21 — Failure Handling →</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.cl li').forEach((li, i) => {
    const key = 'p6m20-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
