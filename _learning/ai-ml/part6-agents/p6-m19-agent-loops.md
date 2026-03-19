---
layout: default
title: "P6-M19 - Agent Loops & LangGraph"
permalink: /learning/ai-ml/part6-agents/p6-m19-agent-loops/
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
/* agent loop diagram */
.agent-loop{display:flex;flex-direction:column;align-items:center;gap:.3rem;margin:.8rem 0}
.al-box{padding:.5rem 1.2rem;border-radius:8px;font-size:.84rem;font-weight:600;font-family:monospace;border:1.5px solid;min-width:180px;text-align:center}
.al-arrow{color:#7c3aed;font-size:1.1rem;font-weight:700}
.al-llm{background:#f5f0ff;border-color:#c4b5fd;color:#4c1d95}
.al-tool{background:#e2f0e8;border-color:#6ee7b7;color:#065f46}
.al-cond{background:#fdf4dc;border-color:#fcd34d;color:#92400e}
.al-end{background:#faeaea;border-color:#fca5a5;color:#991b1b}
/* state diagram */
.state-box{display:inline-block;background:#1e0a3a;border:1.5px solid #7c3aed;border-radius:8px;padding:.6rem 1rem;font-family:monospace;font-size:.82rem;color:#ede9fe;margin:.3rem}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 6 — Agents, Workflows &amp; Evaluation &nbsp;·&nbsp; Module 19 of 22</div>
  <div class="mod-title">Agent Loops &amp; LangGraph</div>
  <div class="mod-subtitle">Build LLM systems that reason, act, and iterate — from scratch and with LangGraph</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟠 Intermediate–Advanced</span>
    <span class="mod-pill">🔧 LangGraph · Anthropic SDK</span>
    <span class="mod-pill">📋 Prerequisite: P4-M12 (Tool Calling)</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🧠 Agent Mental Model</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔄 ReAct Loop</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🗂 State & Memory</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🔀 LangGraph</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🧑‍💻 Human-in-the-Loop</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-violet">Core of Part 6</span></div>
  <div class="cp-body">
    <p>An agent is an LLM that decides what to do next by choosing from a set of tools, executes those tools, observes results, and repeats until it completes a goal — or knows it cannot. This module teaches you to build agents from scratch and with LangGraph.</p>
    <ul>
      <li><strong>Agent mental model</strong> — what separates an agent from a chain; the think-act-observe loop</li>
      <li><strong>ReAct loop from scratch</strong> — Reasoning + Acting pattern, fully implemented without a framework</li>
      <li><strong>State management</strong> — how agents track what they know and what they have done</li>
      <li><strong>LangGraph</strong> — state schemas, nodes, edges, conditional routing, checkpointing</li>
      <li><strong>Human-in-the-loop</strong> — pausing for approval before consequential tool calls</li>
      <li><strong>Multi-turn agent conversations</strong> — maintaining context across user interactions</li>
    </ul>
  </div>
</div>
</div>


<!-- ══════════ TAB 1 — MENTAL MODEL ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🧠</span><h3>What Is an Agent?</h3><span class="tag tag-violet">Concept First</span></div>
  <div class="cp-body">
    <p>The word "agent" is overloaded. Here is the precise definition: an agent is an LLM that is given tools and a goal, and then <strong>decides for itself</strong> which tools to call, in what order, with what arguments — until it determines the goal is achieved.</p>
    <div class="cb"><pre><span class="ck"># NOT an agent — you decide what to call:</span>
weather = get_weather(<span class="cs">"Mumbai"</span>)       <span class="ck"># you chose to call this</span>
summary = summarise(weather)          <span class="ck"># you chose to call this next</span>

<span class="ck"># IS an agent — the LLM decides what to call:</span>
<span class="ck"># User: "Should I carry an umbrella in Mumbai today?"</span>
<span class="ck">#</span>
<span class="ck"># LLM thinks: I need weather data → calls get_weather("Mumbai")</span>
<span class="ck"># LLM observes: {"temp": 28, "condition": "partly cloudy", "rain_chance": 20%}</span>
<span class="ck"># LLM thinks: 20% chance of rain — not high. I have enough to answer.</span>
<span class="ck"># LLM responds: "Probably not necessary, but a light one wouldn't hurt."</span>
<span class="ck">#</span>
<span class="ck"># The LLM made ALL the decisions. You only provided tools and a question.</span></pre></div>

    <div class="agent-loop">
      <div class="al-box al-llm">🧠 LLM: Think about what to do next</div>
      <div class="al-arrow">↓</div>
      <div class="al-box al-cond">Decision: need tool? or have final answer?</div>
      <div class="al-arrow">↓ need tool</div>
      <div class="al-box al-tool">⚙️ Execute tool call — your code runs</div>
      <div class="al-arrow">↓ tool result</div>
      <div class="al-box al-llm">🧠 LLM: Observe result, think again</div>
      <div class="al-arrow">↓ final answer</div>
      <div class="al-box al-end">✅ Return answer to user</div>
    </div>
    <div class="warn"><p>⚠️ <strong>Agents are not always the right tool.</strong> A deterministic chain (M18 RAG pipeline) is more predictable, cheaper, and easier to debug. Use an agent when the task requires dynamic decision-making — the sequence of steps cannot be known in advance.</p></div>
  </div>
</div>
</div><!-- end t1 -->


<!-- ══════════ TAB 2 — REACT LOOP ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>ReAct Loop from Scratch</h3><span class="tag tag-violet">Build to Understand</span></div>
  <div class="cp-body">
    <p>ReAct (Reasoning + Acting) is the foundational agent pattern. Before using any framework, build it from scratch.</p>
    <div class="cb"><pre>import anthropic, json
from typing import Any

client = anthropic.Anthropic()

<span class="ck"># ── Tool definitions ──────────────────────────────────</span>
def search_web(query: str) -> str:
    return <span class="cs">f"Search results for '{query}': [simulated results about {query}]"</span>

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {<span class="cs">"__builtins__"</span>: {}})
        return <span class="cs">f"{expression} = {result}"</span>
    except Exception as e:
        return <span class="cs">f"Error: {e}"</span>

def get_current_time() -> str:
    from datetime import datetime
    return datetime.now().strftime(<span class="cs">"%Y-%m-%d %H:%M:%S"</span>)

TOOLS = [
    {<span class="cs">"name"</span>: <span class="cs">"search_web"</span>,
     <span class="cs">"description"</span>: <span class="cs">"Search the web for current information. Use when you need facts not in your training data."</span>,
     <span class="cs">"input_schema"</span>: {<span class="cs">"type"</span>: <span class="cs">"object"</span>, <span class="cs">"properties"</span>: {
         <span class="cs">"query"</span>: {<span class="cs">"type"</span>: <span class="cs">"string"</span>, <span class="cs">"description"</span>: <span class="cs">"The search query"</span>}},
         <span class="cs">"required"</span>: [<span class="cs">"query"</span>]}},
    {<span class="cs">"name"</span>: <span class="cs">"calculate"</span>,
     <span class="cs">"description"</span>: <span class="cs">"Evaluate a mathematical expression. Use for any arithmetic."</span>,
     <span class="cs">"input_schema"</span>: {<span class="cs">"type"</span>: <span class="cs">"object"</span>, <span class="cs">"properties"</span>: {
         <span class="cs">"expression"</span>: {<span class="cs">"type"</span>: <span class="cs">"string"</span>}}, <span class="cs">"required"</span>: [<span class="cs">"expression"</span>]}},
    {<span class="cs">"name"</span>: <span class="cs">"get_current_time"</span>,
     <span class="cs">"description"</span>: <span class="cs">"Get the current date and time."</span>,
     <span class="cs">"input_schema"</span>: {<span class="cs">"type"</span>: <span class="cs">"object"</span>, <span class="cs">"properties"</span>: {}}},
]

TOOL_REGISTRY = {<span class="cs">"search_web"</span>: search_web,
                 <span class="cs">"calculate"</span>: calculate,
                 <span class="cs">"get_current_time"</span>: get_current_time}

<span class="ck"># ── ReAct agent loop ──────────────────────────────────</span>
def run_agent(user_message: str, system: str = <span class="cs">""</span>,
              max_turns: int = <span class="cv">10</span>) -> str:
    messages = [{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
            max_tokens=<span class="cv">4096</span>,
            system=system,
            tools=TOOLS,
            messages=messages
        )

        <span class="ck"># Agent finished — return final text</span>
        if response.stop_reason == <span class="cs">"end_turn"</span>:
            for block in response.content:
                if hasattr(block, <span class="cs">"text"</span>):
                    return block.text
            return <span class="cs">""</span>

        <span class="ck"># Agent wants to use tools</span>
        if response.stop_reason == <span class="cs">"tool_use"</span>:
            messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: response.content})

            tool_results = []
            for block in response.content:
                if block.type != <span class="cs">"tool_use"</span>:
                    continue
                func = TOOL_REGISTRY.get(block.name)
                if func is None:
                    result = {<span class="cs">"error"</span>: <span class="cs">f"Unknown tool: {block.name}"</span>}
                else:
                    try:
                        result = func(**block.input)
                    except Exception as e:
                        result = {<span class="cs">"error"</span>: str(e)}

                tool_results.append({
                    <span class="cs">"type"</span>: <span class="cs">"tool_result"</span>,
                    <span class="cs">"tool_use_id"</span>: block.id,
                    <span class="cs">"content"</span>: str(result)
                })

            messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: tool_results})

    return <span class="cs">f"Agent reached max_turns ({max_turns}) without completing."</span>

<span class="ck"># Run the agent</span>
answer = run_agent(
    <span class="cs">"What is the square root of 1764, and what day of the week is it today?"</span>
)
print(answer)</pre></div>
  </div>
</div>
</div><!-- end t2 -->


<!-- ══════════ TAB 3 — STATE & MEMORY ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🗂</span><h3>Agent State — What the Agent Knows</h3><span class="tag tag-violet">Architecture</span></div>
  <div class="cp-body">
    <p>State is everything the agent needs to track across turns: the conversation history, tool results, intermediate data, and decisions made. Designing state well determines how complex your agent can become.</p>
    <div class="cb"><pre>from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime

@dataclass
class AgentState:
    <span class="ck"># Core</span>
    messages:      list[dict]       = field(default_factory=list)
    turn_count:    int              = <span class="cv">0</span>
    started_at:    str              = field(default_factory=lambda: datetime.utcnow().isoformat())

    <span class="ck"># Tool tracking</span>
    tools_called:  list[str]        = field(default_factory=list)
    tool_results:  dict[str, Any]   = field(default_factory=dict)

    <span class="ck"># Working memory — agent can store intermediate findings</span>
    scratch_pad:   dict[str, Any]   = field(default_factory=dict)

    <span class="ck"># Task tracking</span>
    goal:          str              = <span class="cs">""</span>
    subtasks:      list[str]        = field(default_factory=list)
    completed:     list[str]        = field(default_factory=list)
    status:        str              = <span class="cs">"running"</span>   <span class="ck"># running | waiting | done | failed</span>

    <span class="ck"># Human interaction</span>
    awaiting_approval: bool         = <span class="cv">False</span>
    pending_action:    Optional[dict] = None

def agent_with_state(user_message: str, state: AgentState = None) -> AgentState:
    if state is None:
        state = AgentState(goal=user_message)

    state.messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user_message})

    while state.status == <span class="cs">"running"</span> and state.turn_count < <span class="cv">10</span>:
        state.turn_count += <span class="cv">1</span>
        response = client.messages.create(
            model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
            max_tokens=<span class="cv">4096</span>,
            tools=TOOLS,
            messages=state.messages
        )

        if response.stop_reason == <span class="cs">"end_turn"</span>:
            state.status = <span class="cs">"done"</span>
            for block in response.content:
                if hasattr(block, <span class="cs">"text"</span>):
                    state.messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: block.text})
            break

        state.messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: response.content})

        tool_results = []
        for block in response.content:
            if block.type != <span class="cs">"tool_use"</span>:
                continue
            state.tools_called.append(block.name)
            result = TOOL_REGISTRY.get(block.name, lambda **k: <span class="cs">"unknown tool"</span>)(**block.input)
            state.tool_results[block.id] = result
            tool_results.append({<span class="cs">"type"</span>: <span class="cs">"tool_result"</span>,
                                  <span class="cs">"tool_use_id"</span>: block.id, <span class="cs">"content"</span>: str(result)})

        state.messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: tool_results})

    return state</pre></div>
  </div>
</div>
</div><!-- end t3 -->


<!-- ══════════ TAB 4 — LANGGRAPH ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>LangGraph — Stateful Agent Graphs</h3><span class="tag tag-violet">Framework</span></div>
  <div class="cp-body">
    <p>LangGraph models agents as graphs: nodes (functions that transform state), edges (connections between nodes), and conditional edges (routes based on current state). It adds persistence, checkpointing, and human-in-the-loop out of the box.</p>
    <div class="cb"><pre>pip install langgraph langchain-anthropic

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from typing import TypedDict, Annotated
import operator

<span class="ck"># ── 1. Define state schema ────────────────────────────</span>
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]   <span class="ck"># reducer: add new messages</span>

<span class="ck"># ── 2. Define nodes ───────────────────────────────────</span>
llm = ChatAnthropic(model=<span class="cs">"claude-3-5-sonnet-20241022"</span>)
llm_with_tools = llm.bind_tools(langchain_tools)   <span class="ck"># tools bound to LLM</span>

def call_llm(state: AgentState) -> dict:
    <span class="cs">"""LLM node — decides what to do next."""</span>
    response = llm_with_tools.invoke(state[<span class="cs">"messages"</span>])
    return {<span class="cs">"messages"</span>: [response]}

def execute_tools(state: AgentState) -> dict:
    <span class="cs">"""Tool node — executes all pending tool calls."""</span>
    last_message = state[<span class="cs">"messages"</span>][-<span class="cv">1</span>]
    tool_results = []
    for tool_call in last_message.tool_calls:
        func  = TOOL_REGISTRY[tool_call[<span class="cs">"name"</span>]]
        result = func(**tool_call[<span class="cs">"args"</span>])
        tool_results.append(ToolMessage(
            content=str(result),
            tool_call_id=tool_call[<span class="cs">"id"</span>]
        ))
    return {<span class="cs">"messages"</span>: tool_results}

<span class="ck"># ── 3. Conditional edge — route based on state ────────</span>
def should_continue(state: AgentState) -> str:
    <span class="cs">"""Return 'tools' if LLM wants to call tools, 'end' if done."""</span>
    last = state[<span class="cs">"messages"</span>][-<span class="cv">1</span>]
    if hasattr(last, <span class="cs">"tool_calls"</span>) and last.tool_calls:
        return <span class="cs">"tools"</span>
    return <span class="cs">"end"</span>

<span class="ck"># ── 4. Build the graph ────────────────────────────────</span>
graph = StateGraph(AgentState)

graph.add_node(<span class="cs">"llm"</span>,   call_llm)
graph.add_node(<span class="cs">"tools"</span>, execute_tools)

graph.set_entry_point(<span class="cs">"llm"</span>)
graph.add_conditional_edges(<span class="cs">"llm"</span>, should_continue, {
    <span class="cs">"tools"</span>: <span class="cs">"tools"</span>,
    <span class="cs">"end"</span>:   END
})
graph.add_edge(<span class="cs">"tools"</span>, <span class="cs">"llm"</span>)   <span class="ck"># after tools, always go back to LLM</span>

<span class="ck"># ── 5. Compile with checkpointer (persistence) ────────</span>
memory  = MemorySaver()
agent   = graph.compile(checkpointer=memory)

<span class="ck"># ── 6. Run the agent ──────────────────────────────────</span>
config  = {<span class="cs">"configurable"</span>: {<span class="cs">"thread_id"</span>: <span class="cs">"session-123"</span>}}
result  = agent.invoke(
    {<span class="cs">"messages"</span>: [HumanMessage(content=<span class="cs">"What is 15% of 8500 and what is today's date?"</span>)]},
    config=config
)
print(result[<span class="cs">"messages"</span>][-<span class="cv">1</span>].content)</pre></div>
    <div class="ins"><p>💡 <strong>The thread_id in config enables multi-session persistence.</strong> Every invocation with the same thread_id continues from where it left off — the graph state is checkpointed automatically. Different users get different thread_ids and completely isolated state.</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>LangGraph State Reducers — Advanced Patterns</h3><span class="tag tag-blue">Power Feature</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Reducers control how state is updated when nodes return new values</span>

from typing import TypedDict, Annotated
import operator

class ResearchState(TypedDict):
    <span class="ck"># operator.add — appends new items to existing list</span>
    messages:    Annotated[list, operator.add]
    sources:     Annotated[list, operator.add]

    <span class="ck"># No reducer — node's returned value REPLACES current value</span>
    current_task: str
    is_complete:  bool

    <span class="ck"># Custom reducer — keep only last 10 messages</span>
    short_memory: Annotated[list, lambda old, new: (old + new)[-<span class="cv">10</span>:]]

<span class="ck"># Parallel nodes — execute concurrently in the graph</span>
graph.add_node(<span class="cs">"search"</span>,    search_node)
graph.add_node(<span class="cs">"calculate"</span>, calc_node)
<span class="ck"># Both run in parallel when the graph reaches this fork</span>
graph.add_edge(<span class="cs">"start"</span>, <span class="cs">"search"</span>)
graph.add_edge(<span class="cs">"start"</span>, <span class="cs">"calculate"</span>)
<span class="ck"># Both must complete before proceeding</span>
graph.add_edge([<span class="cs">"search"</span>, <span class="cs">"calculate"</span>], <span class="cs">"synthesize"</span>)</pre></div>
  </div>
</div>
</div><!-- end t4 -->


<!-- ══════════ TAB 5 — HUMAN-IN-THE-LOOP ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🧑‍💻</span><h3>Human-in-the-Loop — Pause Before Consequential Actions</h3><span class="tag tag-violet">Safety Critical</span></div>
  <div class="cp-body">
    <p>Never let an agent autonomously send emails, delete data, make purchases, or call external APIs without human approval. LangGraph's interrupt mechanism pauses the graph at any node, waits for human input, then resumes.</p>
    <div class="cb"><pre>from langgraph.graph import StateGraph, END, interrupt

<span class="ck"># ── Interrupt before executing a tool ─────────────────</span>
SENSITIVE_TOOLS = {<span class="cs">"send_email"</span>, <span class="cs">"delete_record"</span>, <span class="cs">"make_payment"</span>}

def execute_tools_with_approval(state: AgentState) -> dict:
    last_message = state[<span class="cs">"messages"</span>][-<span class="cv">1</span>]
    tool_results = []

    for tool_call in last_message.tool_calls:
        tool_name = tool_call[<span class="cs">"name"</span>]

        if tool_name in SENSITIVE_TOOLS:
            <span class="ck"># Pause and ask human for approval</span>
            approval = interrupt({
                <span class="cs">"question"</span>: <span class="cs">f"Agent wants to call {tool_name} with args: {tool_call['args']}. Approve?"</span>,
                <span class="cs">"tool_name"</span>: tool_name,
                <span class="cs">"tool_args"</span>: tool_call[<span class="cs">"args"</span>]
            })
            if not approval.get(<span class="cs">"approved"</span>):
                tool_results.append(ToolMessage(
                    content=<span class="cs">"User declined this action."</span>,
                    tool_call_id=tool_call[<span class="cs">"id"</span>]
                ))
                continue

        <span class="ck"># Approved or non-sensitive — execute</span>
        result = TOOL_REGISTRY[tool_name](**tool_call[<span class="cs">"args"</span>])
        tool_results.append(ToolMessage(content=str(result),
                                        tool_call_id=tool_call[<span class="cs">"id"</span>]))

    return {<span class="cs">"messages"</span>: tool_results}

<span class="ck"># ── Resuming after human approval ─────────────────────</span>
<span class="ck"># When the graph is interrupted, it returns a snapshot</span>
<span class="ck"># The human inspects and provides a response</span>
<span class="ck"># Then you resume with Command(resume=response)</span>

from langgraph.types import Command

<span class="ck"># Graph pauses here, returns to caller</span>
result = agent.invoke(task, config)

<span class="ck"># Human reviews the interrupt value</span>
pending = result[<span class="cs">"__interrupt__"</span>]
print(<span class="cs">f"Waiting for approval: {pending[0]['value']}"</span>)

<span class="ck"># Human approves (or rejects)</span>
human_response = {<span class="cs">"approved"</span>: <span class="cv">True</span>}   <span class="ck"># or False</span>

<span class="ck"># Resume the graph from where it paused</span>
result = agent.invoke(Command(resume=human_response), config)</pre></div>
    <div class="warn"><p>⚠️ <strong>Human-in-the-loop is not optional for consequential actions.</strong> An agent that autonomously sends emails, deletes records, or makes API calls is an accident waiting to happen. Always implement interrupt-based approval for irreversible or high-stakes tool calls (OWASP LLM08: Excessive Agency).</p></div>
  </div>
</div>
</div><!-- end t5 -->


<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://langchain-ai.github.io/langgraph/concepts/low_level/" target="_blank" rel="noopener">LangGraph Low-Level Concepts — langchain-ai.github.io/langgraph</a></td><td>State schemas, reducers, nodes, edges, checkpointing — the definitive reference.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://academy.langchain.com/courses/intro-to-langgraph" target="_blank" rel="noopener">LangChain Academy: Intro to LangGraph — academy.langchain.com</a></td><td>Free official LangGraph course. Hands-on with real agent examples. Best starting point.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://www.anthropic.com/research/building-effective-agents" target="_blank" rel="noopener">Anthropic: Building Effective Agents — anthropic.com/research</a></td><td>Anthropic's definitive guide on when to use agents vs workflows, and how to build reliable agents.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://langchain-ai.github.io/langgraph/concepts/multi_agent/" target="_blank" rel="noopener">LangGraph: Multi-Agent Concepts — langchain-ai.github.io/langgraph</a></td><td>Supervisor patterns, handoff between agents, shared state in multi-agent systems.</td></tr>
  </tbody>
</table>
</div>


<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Research Agent — Scratch + LangGraph</span>
    <span class="proj-dur">[Intermediate–Advanced] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build a research agent that can search, calculate, and synthesise multi-step answers — first from scratch, then rebuilt with LangGraph to compare the approaches.</p>
    <h4>Part A — From Scratch</h4>
    <ul>
      <li>Implement the full ReAct loop with 4 tools: search_web, calculate, get_current_time, read_file</li>
      <li>Track state: tools_called, turn_count, intermediate_results</li>
      <li>Add max_turns safeguard and meaningful error messages</li>
      <li>Test with 5 multi-step queries that require 2+ tool calls each</li>
    </ul>
    <h4>Part B — LangGraph</h4>
    <ul>
      <li>Rebuild with LangGraph: StateGraph, MemorySaver, conditional edges</li>
      <li>Add human-in-the-loop: interrupt before any web search (simulating a gated tool)</li>
      <li>Test session persistence: run 3 turns, restart Python process, resume with same thread_id</li>
      <li>Compare: what did LangGraph give you for free vs scratch?</li>
    </ul>
    <p><strong>Skills:</strong> ReAct loop, AgentState, LangGraph StateGraph, MemorySaver, interrupt/resume, conditional routing</p>
  </div>
</div>
</div>


<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Build and Break a ReAct Agent</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build deep intuition for agent behaviour by deliberately breaking it and observing failures.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the scratch ReAct loop from Tab 2 with 3 tools (search, calculate, get_time).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Test with a 5-step query: "What is today's date? What was the population of India in that year? What is 2.3% of that number?" — observe the full tool-calling sequence.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Deliberately trigger each failure mode: (a) set max_turns=2 on a 4-step task, (b) make a tool return an error string, (c) give contradictory tool results — how does the agent handle each?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Remove one tool the agent needs mid-task. What happens? Does it give up gracefully or loop?</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Add logging: print every turn number, stop_reason, and tools called. Run 5 different queries and compare turn counts. Which queries take the most turns and why?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>LangGraph — Visualise and Trace the Graph</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a LangGraph agent and use its tracing to deeply understand the execution path.</p>
    <div class="lab-step"><div class="sn">1</div><div>Build the simple 2-node LangGraph (llm → tools → llm) from Tab 4. Draw the graph: <code>print(agent.get_graph().draw_mermaid())</code> — paste into mermaid.live to visualise.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add a third node: <code>validate_output</code> — after the LLM produces a final answer, this node checks it meets quality criteria. Add a conditional edge: if quality check fails, route back to LLM; if passes, route to END.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run with verbose streaming: <code>for event in agent.stream(inputs, config): print(event)</code>. Observe every state transition.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Test checkpoint persistence: run 3 turns with a thread_id, then: <code>snapshot = agent.get_state(config)</code>. Print the snapshot. Kill the Python process, restart, restore from snapshot, continue.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Human-in-the-Loop — Approval Flow</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement and test the full interrupt/resume cycle for a gated tool.</p>
    <div class="lab-step"><div class="sn">1</div><div>Add a <code>send_email(to, subject, body)</code> tool to your LangGraph agent. Mark it as SENSITIVE.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Ask the agent: "Draft and send an email to boss@example.com explaining that the DPDK migration is complete." It should reach the send_email tool call and pause.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Inspect the interrupt value — does it contain the full email content? Approve it: <code>Command(resume={"approved": True})</code>. Verify the agent completes.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Repeat but reject with feedback: <code>Command(resume={"approved": False, "reason": "Subject line too informal"})</code>. Does the agent revise and ask again?</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Document:</strong> What information should always be in the interrupt payload to give a human enough context to approve or reject? Design the ideal approval UI payload.</div></div>
  </div>
</div>
</div><!-- end t8 -->


<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P6-M19 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain the difference between a chain (you decide what runs) and an agent (LLM decides) in one sentence</li>
  <li>Know when NOT to use an agent — predictable tasks with fixed steps should be chains</li>
  <li>Can implement the full ReAct loop from scratch: LLM call → tool execution → result feeding → repeat</li>
  <li>Correctly handle the max_turns safeguard to prevent infinite loops</li>
  <li>Can design an AgentState dataclass that tracks messages, tools_called, tool_results, and status</li>
  <li>Can define a LangGraph StateGraph with two nodes (llm, tools) and a conditional edge</li>
  <li>Understand state reducers: operator.add appends to lists, no reducer replaces the value</li>
  <li>Can compile a LangGraph agent with MemorySaver for session persistence across invocations</li>
  <li>Understand thread_id: same thread_id = continued conversation; different = new session</li>
  <li>Can add a third node (e.g. validator) and route back with a conditional edge</li>
  <li>Can implement human-in-the-loop using LangGraph's interrupt() in a tool node</li>
  <li>Can resume a paused graph using Command(resume=response)</li>
  <li>Know that SENSITIVE_TOOLS (send email, delete, pay) must always require human approval (OWASP LLM08)</li>
  <li>Completed Lab 1: ReAct agent built and deliberately broken to understand failure modes</li>
  <li>Completed Lab 2: LangGraph with visualisation and checkpoint tracing</li>
  <li>Completed Lab 3: full interrupt/resume approval flow</li>
  <li>Milestone project pushed to GitHub: research agent in both scratch and LangGraph</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P6-M20 — Tool Design, Workflow Patterns &amp; When NOT to Use Agents</strong>. You now know how agents work mechanically. M20 teaches you to design agents that are reliable in production — which is harder than it looks.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part5-rag/p5-m18-rag-pipelines/' | relative_url }}">← P5-M18: RAG Pipelines</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part6-agents/p6-m20-tool-design/' | relative_url }}">Next: P6-M20 — Tool Design →</a>
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
    const key = 'p6m19-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
