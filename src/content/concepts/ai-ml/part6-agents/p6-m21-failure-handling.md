---
title: "P6-M21 - Failure Handling in Agents"
description: "Part 6 — Agents, Workflows Evaluation · Module 21 of 22 Failure Handling in Agents Loops, stuck states, hallucinated tool calls, runaway costs — and how to handle all of them ⏱…"
domain: ai-ml
track: ai-ml-engineering
module: part6-agents
order: 621
ownHeader: true
url: /learning/ai-ml/part6-agents/p6-m21-failure-handling/
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
/* failure mode cards */
.fm-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.8rem;margin:.8rem 0}
.fm{border-radius:10px;padding:1rem 1.1rem;border:1.5px solid}
.fm h4{font-size:.88rem;font-weight:700;margin:0 0 .3rem;border:none}
.fm p{font-size:.82rem;line-height:1.6;margin:0 0 .3rem;color:var(--text-color,#444)}
.fm .fix{font-size:.75rem;font-family:monospace;font-weight:600;color:#059669}
.fm-loop{background:#faeaea;border-color:#fca5a5}.fm-loop h4{color:#991b1b}
.fm-stuck{background:#faeee4;border-color:#fdba74}.fm-stuck h4{color:#9a3412}
.fm-halluc{background:#fdf4dc;border-color:#fcd34d}.fm-halluc h4{color:#92400e}
.fm-cost{background:#ede8f5;border-color:#c4b5fd}.fm-cost h4{color:#5b21b6}
.fm-partial{background:#e0f2fe;border-color:#7dd3fc}.fm-partial h4{color:#0c4a6e}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 6 — Agents, Workflows &amp; Evaluation &nbsp;·&nbsp; Module 21 of 22</div>
  <div class="mod-title">Failure Handling in Agents</div>
  <div class="mod-subtitle">Loops, stuck states, hallucinated tool calls, runaway costs — and how to handle all of them</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟠 Intermediate–Advanced</span>
    <span class="mod-pill">🔧 LangGraph · Tenacity · Structlog</span>
    <span class="mod-pill">📋 Prerequisite: P6-M20</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🚨 Failure Modes</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔄 Loop Detection</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🛡 Guardrails</button>
  <button class="tab-btn" onclick="vt(event,'t4')">💰 Cost Circuits</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📋 Structured Logging</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🔁 Recovery Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-violet">Production Hardening</span></div>
  <div class="cp-body">
    <p>Agents fail in ways chains never do. They can loop forever, call tools that don't exist, spend your entire monthly API budget in 10 minutes, or get stuck unable to make progress. This module gives you the tools to detect, contain, and recover from every major agent failure mode.</p>
    <ul>
      <li><strong>Failure taxonomy</strong> — the 5 agent failure modes and how to recognise each</li>
      <li><strong>Loop detection</strong> — detecting infinite loops, repeated tool calls, lack of progress</li>
      <li><strong>Guardrails</strong> — output validation, tool call validation, scope enforcement</li>
      <li><strong>Cost circuit breakers</strong> — hard spending limits that stop runaway agents</li>
      <li><strong>Structured agent logging</strong> — capturing every decision for debugging and audit</li>
      <li><strong>Recovery patterns</strong> — graceful degradation, fallback to human, partial result return</li>
    </ul>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — FAILURE MODES ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>The 5 Agent Failure Modes</h3><span class="tag tag-red">Know These</span></div>
  <div class="cp-body">
    <div class="fm-grid">
      <div class="fm fm-loop">
        <h4>Infinite Loop</h4>
        <p>Agent calls the same tool repeatedly with same args, never making progress. max_turns doesn't help if the loop is subtle.</p>
        <div class="fix">Fix: tool call history deduplication, progress detection</div>
      </div>
      <div class="fm fm-stuck">
        <h4>Stuck State</h4>
        <p>Agent keeps trying a failing approach, can't recover. Tool returns error, agent retries with same args, same error.</p>
        <div class="fix">Fix: error escalation counter, alternative strategy prompt</div>
      </div>
      <div class="fm fm-halluc">
        <h4>Hallucinated Tool Calls</h4>
        <p>Agent invents tool names that don't exist, or calls real tools with nonsensical arguments.</p>
        <div class="fix">Fix: strict tool registry validation, argument schema enforcement</div>
      </div>
      <div class="fm fm-cost">
        <h4>Runaway Cost</h4>
        <p>Agent spawns subagents, each calling expensive tools in loops. $0.01 task becomes $100 task.</p>
        <div class="fix">Fix: cost circuit breaker, per-session spending cap</div>
      </div>
      <div class="fm fm-partial">
        <h4>Silent Partial Failure</h4>
        <p>Agent completes but with incorrect results. It said it succeeded but actually failed midway. No error raised.</p>
        <div class="fix">Fix: result validation, structured completion checks, audit log</div>
      </div>
    </div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — LOOP DETECTION ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Loop Detection and Progress Tracking</h3><span class="tag tag-violet">Critical</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import hashlib, json
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from typing import Any
 
@dataclass
class AgentGuardian:
    """Monitors agent execution for failure patterns."""
    max_turns:         int   = <span class="cv">20</span>
    max_repeated_calls: int  = <span class="cv">3</span>     <span class="ck"># same tool+args N times = loop</span>
    max_errors:        int   = <span class="cv">5</span>     <span class="ck"># 5 consecutive errors = stuck</span>
    max_cost_usd:      float = <span class="cv">1.0</span>   <span class="ck"># hard spending limit</span>
 
    turn_count:        int   = <span class="cv">0</span>
    error_count:       int   = <span class="cv">0</span>
    total_cost_usd:    float = <span class="cv">0.0</span>
    tool_call_log:     list  = field(default_factory=list)
    call_counts:       dict  = field(default_factory=lambda: Counter())
 
    def _call_fingerprint(self, tool_name: str, args: dict) -> str:
        """Hash of tool name + sorted args — detects repeated identical calls."""
        key = json.dumps({<span class="cs">"tool"</span>: tool_name, <span class="cs">"args"</span>: args}, sort_keys=<span class="cv">True</span>)
        return hashlib.md5(key.encode()).hexdigest()[:8]
 
    def record_tool_call(self, tool_name: str, args: dict,
                         result: Any, tokens_used: int = <span class="cv">0</span>) -> None:
        fp = self._call_fingerprint(tool_name, args)
        self.call_counts[fp] += <span class="cv">1</span>
        self.tool_call_log.append({
            <span class="cs">"turn"</span>:    self.turn_count,
            <span class="cs">"tool"</span>:    tool_name,
            <span class="cs">"args"</span>:    args,
            <span class="cs">"fp"</span>:      fp,
            <span class="cs">"success"</span>: <span class="cs">"error"</span> not in str(result).lower(),
        })
        if isinstance(result, dict) and not result.get(<span class="cs">"ok"</span>, <span class="cv">True</span>):
            self.error_count += <span class="cv">1</span>
        else:
            self.error_count = <span class="cv">0</span>   <span class="ck"># reset on success</span>
        cost = tokens_used * (<span class="cv">3.00</span> / <span class="cv">1_000_000</span>)
        self.total_cost_usd += cost
 
    def check(self) -> tuple[bool, str]:
        """Returns (should_stop, reason). Call before each turn."""
        self.turn_count += <span class="cv">1</span>
 
        if self.turn_count > self.max_turns:
            return <span class="cv">True</span>, <span class="cs">f"Max turns exceeded ({self.max_turns})"</span>
 
        if self.total_cost_usd > self.max_cost_usd:
            return <span class="cv">True</span>, <span class="cs">f"Cost limit exceeded: ${self.total_cost_usd:.4f} > ${self.max_cost_usd}"</span>
 
        if self.error_count >= self.max_errors:
            return <span class="cv">True</span>, <span class="cs">f"Stuck: {self.error_count} consecutive errors"</span>
 
        for fp, count in self.call_counts.items():
            if count >= self.max_repeated_calls:
                recent = [c for c in self.tool_call_log if c[<span class="cs">"fp"</span>] == fp][-<span class="cv">1</span>]
                return <span class="cv">True</span>, <span class="cs">f"Loop detected: {recent['tool']} called {count}x with same args"</span>
 
        return <span class="cv">False</span>, <span class="cs">""</span>
<span class="ck"># Usage inside agent loop</span>
def guarded_agent(user_message: str) -> dict:
    guardian = AgentGuardian(max_turns=<span class="cv">15</span>, max_cost_usd=<span class="cv">0.50</span>)
    messages  = [{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user_message}]
 
    while <span class="cv">True</span>:
        should_stop, reason = guardian.check()
        if should_stop:
            return {<span class="cs">"status"</span>: <span class="cs">"stopped"</span>, <span class="cs">"reason"</span>: reason,
                    <span class="cs">"partial_result"</span>: extract_partial_result(messages),
                    <span class="cs">"turns_used"</span>: guardian.turn_count,
                    <span class="cs">"cost_usd"</span>: guardian.total_cost_usd}
 
        response = client.messages.create(model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
                                           max_tokens=<span class="cv">4096</span>, tools=TOOLS, messages=messages)
 
        if response.stop_reason == <span class="cs">"end_turn"</span>:
            return {<span class="cs">"status"</span>: <span class="cs">"completed"</span>,
                    <span class="cs">"answer"</span>: response.content[<span class="cv">0</span>].text,
                    <span class="cs">"turns_used"</span>: guardian.turn_count,
                    <span class="cs">"cost_usd"</span>: guardian.total_cost_usd}
 
        messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: response.content})
        tool_results = []
        for block in response.content:
            if block.type == <span class="cs">"tool_use"</span>:
                result = execute_tool(block.name, block.input)
                guardian.record_tool_call(block.name, block.input, result,
                                          tokens_used=response.usage.output_tokens)
                tool_results.append({<span class="cs">"type"</span>: <span class="cs">"tool_result"</span>,
                                      <span class="cs">"tool_use_id"</span>: block.id, <span class="cs">"content"</span>: str(result)})
        messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: tool_results})</pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — GUARDRAILS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🛡</span><h3>Input and Output Guardrails</h3><span class="tag tag-violet">Validation Layer</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># ── Tool call validation ──────────────────────────────</span>
def validate_tool_call(tool_name: str, args: dict) -> tuple[bool, str]:
    """Validate before executing. Returns (is_valid, error_message)."""
    if tool_name not in TOOL_REGISTRY:
        return <span class="cv">False</span>, <span class="cs">f"Tool {tool_name!r} does not exist. Available: {list(TOOL_REGISTRY)}"</span>
 
    tool_schema = next(t for t in TOOLS if t[<span class="cs">"name"</span>] == tool_name)
    required = tool_schema[<span class="cs">"input_schema"</span>].get(<span class="cs">"required"</span>, [])
    properties = tool_schema[<span class="cs">"input_schema"</span>].get(<span class="cs">"properties"</span>, {})
 
    for req_field in required:
        if req_field not in args:
            return <span class="cv">False</span>, <span class="cs">f"Missing required field: {req_field!r}"</span>
 
    for field_name, field_val in args.items():
        if field_name not in properties:
            return <span class="cv">False</span>, <span class="cs">f"Unknown field: {field_name!r}"</span>
        expected_type = properties[field_name].get(<span class="cs">"type"</span>)
        if expected_type == <span class="cs">"string"</span> and not isinstance(field_val, str):
            return <span class="cv">False</span>, <span class="cs">f"{field_name} must be a string, got {type(field_val).__name__}"</span>
        if expected_type == <span class="cs">"integer"</span> and not isinstance(field_val, int):
            return <span class="cv">False</span>, <span class="cs">f"{field_name} must be an integer"</span>
 
    return <span class="cv">True</span>, <span class="cs">""</span>
 
def execute_tool_safe(tool_name: str, args: dict) -> dict:
    is_valid, error = validate_tool_call(tool_name, args)
    if not is_valid:
        return {<span class="cs">"ok"</span>: <span class="cv">False</span>, <span class="cs">"error"</span>: <span class="cs">"INVALID_TOOL_CALL"</span>, <span class="cs">"message"</span>: error,
                <span class="cs">"suggestion"</span>: <span class="cs">"Check the tool name and argument types before calling again."</span>}
    try:
        result = TOOL_REGISTRY[tool_name](**args)
        return result if isinstance(result, dict) else {<span class="cs">"ok"</span>: <span class="cv">True</span>, <span class="cs">"result"</span>: result}
    except Exception as e:
        return {<span class="cs">"ok"</span>: <span class="cv">False</span>, <span class="cs">"error"</span>: <span class="cs">"TOOL_EXECUTION_ERROR"</span>, <span class="cs">"message"</span>: str(e)}
 
<span class="ck"># ── Output guardrail ──────────────────────────────────</span>
<span class="ck"># Validate the agent's final answer before returning to user</span>
from pydantic import BaseModel
from typing import Optional
 
class AgentOutputGuardrail(BaseModel):
    is_complete: bool
    has_answer:  bool
    is_on_topic: bool
    issues:      list[str] = []
 
def validate_agent_output(original_goal: str, output: str) -> AgentOutputGuardrail:
    return instructor_client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">200</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>:
            <span class="cs">f"""Validate this agent output against the original goal.
 
Goal: {original_goal}
Output: {output}
 
Check: Is the goal addressed? Is there a clear answer? Is it on topic?"""</span>}],
        response_model=AgentOutputGuardrail
    )</pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — COST CIRCUITS ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">💰</span><h3>Cost Circuit Breakers</h3><span class="tag tag-violet">Financial Safety</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import sqlite3
from datetime import datetime
 
MODEL_COSTS = {
    <span class="cs">"claude-3-5-sonnet-20241022"</span>: {<span class="cs">"input"</span>: <span class="cv">3.0</span>/<span class="cv">1e6</span>, <span class="cs">"output"</span>: <span class="cv">15.0</span>/<span class="cv">1e6</span>},
    <span class="cs">"claude-3-haiku-20240307"</span>:    {<span class="cs">"input"</span>: <span class="cv">0.25</span>/<span class="cv">1e6</span>, <span class="cs">"output"</span>: <span class="cv">1.25</span>/<span class="cv">1e6</span>},
}
 
class AgentCostCircuitBreaker:
    """Hard spending limits for agent sessions."""
    def __init__(self, session_limit_usd: float = <span class="cv">1.0</span>,
                 daily_limit_usd: float = <span class="cv">10.0</span>,
                 per_tool_call_limit_usd: float = <span class="cv">0.10</span>):
        self.session_limit      = session_limit_usd
        self.daily_limit        = daily_limit_usd
        self.per_tool_call_limit = per_tool_call_limit_usd
        self.session_spend      = <span class="cv">0.0</span>
        self.session_id         = datetime.utcnow().isoformat()
 
    def _compute_cost(self, model: str, input_tok: int, output_tok: int) -> float:
        prices = MODEL_COSTS.get(model, MODEL_COSTS[<span class="cs">"claude-3-5-sonnet-20241022"</span>])
        return input_tok * prices[<span class="cs">"input"</span>] + output_tok * prices[<span class="cs">"output"</span>]
 
    def _get_daily_spend(self) -> float:
        today = datetime.utcnow().strftime(<span class="cs">"%Y-%m-%d"</span>)
        with sqlite3.connect(<span class="cs">"agent_costs.db"</span>) as conn:
            conn.execute(<span class="cs">"CREATE TABLE IF NOT EXISTS costs (ts TEXT, session TEXT, cost REAL)"</span>)
            row = conn.execute(
                <span class="cs">"SELECT SUM(cost) FROM costs WHERE ts LIKE ?"</span>, (f<span class="cs">"{today}%"</span>,)).fetchone()
        return row[<span class="cv">0</span>] or <span class="cv">0.0</span>
 
    def record_and_check(self, model: str, input_tok: int,
                         output_tok: int) -> tuple[float, bool, str]:
        cost  = self._compute_cost(model, input_tok, output_tok)
        self.session_spend += cost
 
        with sqlite3.connect(<span class="cs">"agent_costs.db"</span>) as conn:
            conn.execute(<span class="cs">"INSERT INTO costs VALUES (?,?,?)"</span>,
                         (datetime.utcnow().isoformat(), self.session_id, cost))
 
        daily = self._get_daily_spend()
 
        if cost > self.per_tool_call_limit:
            return cost, <span class="cv">True</span>, <span class="cs">f"Single call cost ${cost:.4f} exceeds per-call limit"</span>
        if self.session_spend > self.session_limit:
            return cost, <span class="cv">True</span>, <span class="cs">f"Session spend ${self.session_spend:.4f} exceeds session limit"</span>
        if daily > self.daily_limit:
            return cost, <span class="cv">True</span>, <span class="cs">f"Daily spend ${daily:.4f} exceeds daily limit"</span>
 
        return cost, <span class="cv">False</span>, <span class="cs">""</span></pre></div>
    <div class="warn"><p>⚠️ <strong>Always set a session cost limit for any agent that can spawn subagents or loop.</strong> A misconfigured agent that recursively calls expensive tools can exhaust a $100 budget in minutes. The circuit breaker pattern is not optional — it is the difference between a manageable incident and a billing nightmare.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — STRUCTURED LOGGING ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Structured Agent Logging</h3><span class="tag tag-violet">Audit & Debug</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install structlog
 
import structlog, time
from datetime import datetime
 
<span class="ck"># Configure structlog for JSON output</span>
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt=<span class="cs">"iso"</span>),
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger()
 
class AgentLogger:
    """Structured logging for agent execution."""
    def __init__(self, session_id: str, goal: str):
        self.session_id = session_id
        self.goal       = goal
        self.turn       = <span class="cv">0</span>
        self.start_time = time.time()
        logger.info(<span class="cs">"agent_started"</span>, session_id=session_id, goal=goal)
 
    def log_turn(self, stop_reason: str, tools_called: list):
        self.turn += <span class="cv">1</span>
        logger.info(<span class="cs">"agent_turn"</span>, session_id=self.session_id,
                    turn=self.turn, stop_reason=stop_reason,
                    tools_called=tools_called)
 
    def log_tool_call(self, tool_name: str, args: dict, result: dict,
                      latency_ms: float, cost_usd: float):
        success = result.get(<span class="cs">"ok"</span>, <span class="cv">True</span>)
        logger.info(<span class="cs">"tool_call"</span>, session_id=self.session_id, turn=self.turn,
                    tool=tool_name, success=success,
                    latency_ms=round(latency_ms, <span class="cv">1</span>), cost_usd=round(cost_usd, <span class="cv">6</span>),
                    error=result.get(<span class="cs">"error"</span>) if not success else None)
 
    def log_completion(self, status: str, total_cost_usd: float, answer: str = <span class="cs">""</span>):
        elapsed = round(time.time() - self.start_time, <span class="cv">2</span>)
        logger.info(<span class="cs">"agent_completed"</span>, session_id=self.session_id,
                    status=status, total_turns=self.turn,
                    elapsed_sec=elapsed, total_cost_usd=round(total_cost_usd, <span class="cv">6</span>),
                    answer_length=len(answer))
 
    def log_failure(self, reason: str, last_tool: str = <span class="cs">""</span>):
        logger.error(<span class="cs">"agent_failed"</span>, session_id=self.session_id,
                     turn=self.turn, reason=reason, last_tool=last_tool)
 
<span class="ck"># Example output (one JSON line per event):</span>
<span class="ck"># {"event":"agent_started","session_id":"abc123","goal":"Analyse Q3 sales","level":"info","timestamp":"2024-..."}</span>
<span class="ck"># {"event":"tool_call","tool":"search_sales_db","success":true,"latency_ms":124.3,"cost_usd":0.000045,...}</span>
<span class="ck"># {"event":"agent_failed","reason":"Loop detected: search_sales_db called 3x with same args",...}</span></pre></div>
    <div class="ins"><p>💡 <strong>Structured logs are queryable.</strong> When you have 10,000 agent runs in production and one fails, you need to find: which session, which turn, which tool, what the exact args were. JSON logs let you grep, jq-filter, and aggregate across millions of events. Unstructured print() statements do not.</p></div>
  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — RECOVERY PATTERNS ══════════ -->
<div id="t6" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔁</span><h3>Recovery and Graceful Degradation</h3><span class="tag tag-violet">Resilience</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># ── Pattern 1: Alternative strategy prompt ────────────</span>
<span class="ck"># When tool fails N times, inject a prompt asking the agent to try differently</span>
 
STUCK_RECOVERY_MSG = <span class="cs">"""You have encountered repeated errors with {tool_name}.
The error was: {error_message}
 
Please try a different approach:
- Use a different tool if available
- Simplify your query or arguments
- If you cannot complete this subtask, explain what you found so far and skip it
 
Do NOT call {tool_name} again with the same arguments."""</span>
 
def inject_recovery_hint(messages: list, tool_name: str, error: str) -> list:
    recovery = STUCK_RECOVERY_MSG.format(tool_name=tool_name, error_message=error)
    messages.append({
        <span class="cs">"role"</span>: <span class="cs">"user"</span>,
        <span class="cs">"content"</span>: [{<span class="cs">"type"</span>: <span class="cs">"text"</span>, <span class="cs">"text"</span>: recovery}]
    })
    return messages
 
<span class="ck"># ── Pattern 2: Partial result extraction ─────────────</span>
<span class="ck"># When agent hits limit, extract what it learned before stopping</span>
 
def extract_partial_result(messages: list) -> str:
    if len(messages) < <span class="cv">2</span>:
        return <span class="cs">"No results gathered before timeout."</span>
 
    response = client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">512</span>,
        messages=[
            *messages,
            {<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>:
             <span class="cs">"Summarise what you have found so far, even if incomplete. Be honest about what's missing."</span>}
        ]
    )
    return response.content[<span class="cv">0</span>].text
 
<span class="ck"># ── Pattern 3: Fallback to human ─────────────────────</span>
<span class="ck"># When agent cannot proceed, escalate with full context</span>
 
def escalate_to_human(session_id: str, goal: str, messages: list,
                      failure_reason: str) -> dict:
    partial = extract_partial_result(messages)
    ticket  = {
        <span class="cs">"session_id"</span>:      session_id,
        <span class="cs">"original_goal"</span>:   goal,
        <span class="cs">"failure_reason"</span>:  failure_reason,
        <span class="cs">"partial_result"</span>:  partial,
        <span class="cs">"turns_completed"</span>: len([m for m in messages if m[<span class="cs">"role"</span>] == <span class="cs">"assistant"</span>]),
        <span class="cs">"escalated_at"</span>:    datetime.utcnow().isoformat(),
        <span class="cs">"priority"</span>:        <span class="cs">"high"</span> if <span class="cs">"cost"</span> in failure_reason.lower() else <span class="cs">"normal"</span>
    }
    create_human_task(ticket)   <span class="ck"># your ticketing system</span>
    return {<span class="cs">"status"</span>: <span class="cs">"escalated"</span>, <span class="cs">"ticket_id"</span>: ticket[<span class="cs">"session_id"</span>],
            <span class="cs">"message"</span>: <span class="cs">"A human agent will continue this task."</span>}
 
<span class="ck"># ── Pattern 4: Checkpoint and resume ─────────────────</span>
<span class="ck"># Save progress periodically — resume if agent crashes</span>
 
import pickle, pathlib
 
def save_checkpoint(session_id: str, messages: list, state: dict):
    path = pathlib.Path(<span class="cs">f".checkpoints/{session_id}.pkl"</span>)
    path.parent.mkdir(exist_ok=<span class="cv">True</span>)
    with open(path, <span class="cs">"wb"</span>) as f:
        pickle.dump({<span class="cs">"messages"</span>: messages, <span class="cs">"state"</span>: state}, f)
 
def load_checkpoint(session_id: str) -> dict | None:
    path = pathlib.Path(<span class="cs">f".checkpoints/{session_id}.pkl"</span>)
    if not path.exists():
        return None
    with open(path, <span class="cs">"rb"</span>) as f:
        return pickle.load(f)</pre></div>
  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Article</td><td><a href="https://www.anthropic.com/research/building-effective-agents" target="_blank" rel="noopener">Anthropic: Building Effective Agents — anthropic.com/research</a></td><td>Covers agent failure modes and the importance of minimal footprint and human oversight.</td></tr>
    <tr><td class="res-type">Library</td><td><a href="https://www.structlog.org/" target="_blank" rel="noopener">structlog — structlog.org — structured logging for Python</a></td><td>The standard library for structured JSON logging in Python. Read the Getting Started guide.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://langchain-ai.github.io/langgraph/concepts/low_level/" target="_blank" rel="noopener">LangGraph: Checkpointing — langchain-ai.github.io/langgraph</a></td><td>LangGraph's built-in checkpoint system for agent state persistence and recovery.</td></tr>
  </tbody>
</table>
</div>
<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Hardened Agent with Full Failure Handling</span>
    <span class="proj-dur">[Advanced] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Take your M19 research agent and add the full production hardening layer from this module.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>AgentGuardian</strong> — loop detection via tool call fingerprinting, max_turns, consecutive error counter</li>
      <li><strong>AgentCostCircuitBreaker</strong> — session limit ($1), daily limit ($10), per-call limit ($0.10)</li>
      <li><strong>Tool validation</strong> — validate all tool names and arg types before execution</li>
      <li><strong>Structured logging</strong> — every turn, tool call, failure, and completion logged as JSON</li>
      <li><strong>Recovery hints</strong> — inject alternative strategy prompt after 3 consecutive tool errors</li>
      <li><strong>Partial result extraction</strong> — on any stop (limit/loop/cost), extract and return what was learned</li>
      <li><strong>Checkpoint/resume</strong> — save state after each turn, auto-resume if session_id provided</li>
    </ul>
    <h4>Testing</h4>
    <ul>
      <li>Trigger every failure mode deliberately and verify each guard works</li>
      <li>Run 10 real tasks and review the structured logs — identify any unexpected failure patterns</li>
    </ul>
    <p><strong>Skills:</strong> AgentGuardian, cost circuit breaker, tool validation, structlog, recovery patterns, checkpoint/resume</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Trigger and Detect Every Failure Mode</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Deliberately trigger all 5 failure modes and verify the AgentGuardian catches each one.</p>
    <div class="lab-step"><div class="sn">1</div><div>Build an agent with AgentGuardian (max_turns=10, max_repeated_calls=3, max_errors=4, max_cost=$0.50).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Trigger <strong>Infinite Loop</strong>: make a tool that always returns "retry" and never changes state. Verify guardian catches it at 3 repeated calls.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Trigger <strong>Stuck State</strong>: make a tool always return an error dict. Verify guardian catches it at 4 consecutive errors.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Trigger <strong>Hallucinated Tool</strong>: remove a tool from the registry but leave it in the description. Verify execute_tool_safe catches and returns structured error.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Trigger <strong>Runaway Cost</strong>: set max_cost=$0.001 and run any real query. Verify circuit breaker fires after first turn.</div></div>
    <div class="lab-step"><div class="sn">6</div><div>For each triggered failure: verify the agent returns a useful partial_result, not a Python exception. Document the structured log output for each.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Structured Log Analysis</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Practice querying structured logs to diagnose agent failures post-hoc.</p>
    <div class="lab-step"><div class="sn">1</div><div>Run your hardened agent on 20 different tasks. All logs go to a file agent.jsonl (one JSON object per line).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write Python to parse agent.jsonl and compute: (a) total sessions, (b) success rate, (c) most called tools, (d) most common failure reason, (e) avg turns per successful session.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Find all sessions where a specific tool failed. Print: session_id, turn number, args passed, error message. This is the debugging workflow you'd use in production.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Identify the most expensive session. Reconstruct its full tool call sequence from the logs. What did it do that cost the most?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Checkpoint and Resume</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Verify that checkpointing allows agent recovery from crashes without losing work.</p>
    <div class="lab-step"><div class="sn">1</div><div>Add checkpoint saving after every tool call in your agent. Use session_id as filename.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Start a long-running 10-turn task. After turn 5, forcefully kill the process (Ctrl+C or sys.exit()).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Restart the agent with the same session_id. Verify it loads from the checkpoint and continues from turn 6 — it should not redo turns 1-5.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify the final answer matches what you would have gotten without the interruption. Compare cost: checkpoint run should cost ~50% of a full restart.</div></div>
  </div>
</div>
</div><!-- end t9 -->
<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P6-M21 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can name all 5 agent failure modes: infinite loop, stuck state, hallucinated tool calls, runaway cost, silent partial failure</li>
  <li>Can implement tool call fingerprinting using content hash to detect repeated identical calls</li>
  <li>Can implement AgentGuardian that checks max_turns, max_repeated_calls, consecutive errors, and cost before every turn</li>
  <li>All agents return structured results on failure — never Python exceptions propagating to the user</li>
  <li>Can validate tool name and argument types before execution using the tool's JSON schema</li>
  <li>Can validate agent output against the original goal using a cheap LLM checker</li>
  <li>Can implement cost circuit breaker with session, daily, and per-call limits using SQLite</li>
  <li>Can set up structlog for JSON-structured logging with turn, tool, cost, and latency fields</li>
  <li>Can implement the recovery hint pattern: inject alternative strategy prompt after repeated errors</li>
  <li>Can extract a partial result from conversation history when an agent hits a limit</li>
  <li>Can escalate to human with a structured ticket containing partial results and failure context</li>
  <li>Can implement checkpoint/resume with pickle or LangGraph's built-in checkpointer</li>
  <li>Can query JSONL structured logs to compute success rate, failure distribution, and most-called tools</li>
  <li>Completed Lab 1: all 5 failure modes triggered and verified</li>
  <li>Completed Lab 2: structured log analysis with success rate and failure debugging</li>
  <li>Completed Lab 3: checkpoint/resume verified end-to-end</li>
  <li>Milestone project: hardened agent with all guards pushed to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P6-M22 — Evaluation Harnesses</strong>. You now have agents that fail safely. M22 covers how to measure and improve agent quality systematically with DeepEval, Ragas, and LLM-as-judge.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part6-agents/p6-m20-tool-design/">← P6-M20: Tool Design</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part6-agents/p6-m22-evaluation/">Next: P6-M22 — Evaluation Harnesses →</a>
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
    const key = 'p6m21-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
