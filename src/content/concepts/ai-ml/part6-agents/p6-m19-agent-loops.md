---
title: "P6-M19 - Agent Loops & LangGraph"
description: "Part 6 — Agents, Workflows Evaluation · Module 19 of 22 Agent Loops LangGraph Build LLM systems that reason, act, and iterate — from scratch and with LangGraph ⏱ 1 Week 🟠…"
domain: ai-ml
track: ai-ml-engineering
module: part6-agents
order: 619
ownHeader: true
url: /learning/ai-ml/part6-agents/p6-m19-agent-loops/
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
    

```python
# NOT an agent — you decide what to call:
weather = get_weather("Mumbai")       # you chose to call this
summary = summarise(weather)          # you chose to call this next

# IS an agent — the LLM decides what to call:
# User: "Should I carry an umbrella in Mumbai today?"
#
# LLM thinks: I need weather data → calls get_weather("Mumbai")
# LLM observes: {"temp": 28, "condition": "partly cloudy", "rain_chance": 20%}
# LLM thinks: 20% chance of rain — not high. I have enough to answer.
# LLM responds: "Probably not necessary, but a light one wouldn't hurt."
#
# The LLM made ALL the decisions. You only provided tools and a question.
```



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
    

```python
import anthropic, json
from typing import Any

client = anthropic.Anthropic()

# ── Tool definitions ──────────────────────────────────
def search_web(query: str) -> str:
    return f"Search results for '{query}': [simulated results about {query}]"

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error: {e}"

def get_current_time() -> str:
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS = [
    {"name": "search_web",
     "description": "Search the web for current information. Use when you need facts not in your training data.",
     "input_schema": {"type": "object", "properties": {
         "query": {"type": "string", "description": "The search query"}},
         "required": ["query"]}},
    {"name": "calculate",
     "description": "Evaluate a mathematical expression. Use for any arithmetic.",
     "input_schema": {"type": "object", "properties": {
         "expression": {"type": "string"}}, "required": ["expression"]}},
    {"name": "get_current_time",
     "description": "Get the current date and time.",
     "input_schema": {"type": "object", "properties": {}}},
]

TOOL_REGISTRY = {"search_web": search_web,
                 "calculate": calculate,
                 "get_current_time": get_current_time}

# ── ReAct agent loop ──────────────────────────────────
def run_agent(user_message: str, system: str = "",
              max_turns: int = 10) -> str:
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            system=system,
            tools=TOOLS,
            messages=messages
        )

        # Agent finished — return final text
        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return ""

        # Agent wants to use tools
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})

            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                func = TOOL_REGISTRY.get(block.name)
                if func is None:
                    result = {"error": f"Unknown tool: {block.name}"}
                else:
                    try:
                        result = func(**block.input)
                    except Exception as e:
                        result = {"error": str(e)}

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

            messages.append({"role": "user", "content": tool_results})

    return f"Agent reached max_turns ({max_turns}) without completing."

# Run the agent
answer = run_agent(
    "What is the square root of 1764, and what day of the week is it today?"
)
print(answer)
```


  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — STATE & MEMORY ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🗂</span><h3>Agent State — What the Agent Knows</h3><span class="tag tag-violet">Architecture</span></div>
  <div class="cp-body">
<p>State is everything the agent needs to track across turns: the conversation history, tool results, intermediate data, and decisions made. Designing state well determines how complex your agent can become.</p>
    

```python
from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime

@dataclass
class AgentState:
    # Core
    messages:      list[dict]       = field(default_factory=list)
    turn_count:    int              = 0
    started_at:    str              = field(default_factory=lambda: datetime.utcnow().isoformat())

    # Tool tracking
    tools_called:  list[str]        = field(default_factory=list)
    tool_results:  dict[str, Any]   = field(default_factory=dict)

    # Working memory — agent can store intermediate findings
    scratch_pad:   dict[str, Any]   = field(default_factory=dict)

    # Task tracking
    goal:          str              = ""
    subtasks:      list[str]        = field(default_factory=list)
    completed:     list[str]        = field(default_factory=list)
    status:        str              = "running"   # running | waiting | done | failed

    # Human interaction
    awaiting_approval: bool         = False
    pending_action:    Optional[dict] = None

def agent_with_state(user_message: str, state: AgentState = None) -> AgentState:
    if state is None:
        state = AgentState(goal=user_message)

    state.messages.append({"role": "user", "content": user_message})

    while state.status == "running" and state.turn_count 10:
        state.turn_count += 1
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            tools=TOOLS,
            messages=state.messages
        )

        if response.stop_reason == "end_turn":
            state.status = "done"
            for block in response.content:
                if hasattr(block, "text"):
                    state.messages.append({"role": "assistant", "content": block.text})
            break

        state.messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            state.tools_called.append(block.name)
            result = TOOL_REGISTRY.get(block.name, lambda **k: "unknown tool")(**block.input)
            state.tool_results[block.id] = result
            tool_results.append({"type": "tool_result",
                                  "tool_use_id": block.id, "content": str(result)})

        state.messages.append({"role": "user", "content": tool_results})

    return state
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — LANGGRAPH ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>LangGraph — Stateful Agent Graphs</h3><span class="tag tag-violet">Framework</span></div>
  <div class="cp-body">
<p>LangGraph models agents as graphs: nodes (functions that transform state), edges (connections between nodes), and conditional edges (routes based on current state). It adds persistence, checkpointing, and human-in-the-loop out of the box.</p>
    

```python
pip install langgraph langchain-anthropic

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from typing import TypedDict, Annotated
import operator

# ── 1. Define state schema ────────────────────────────
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]   # reducer: add new messages

# ── 2. Define nodes ───────────────────────────────────
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm_with_tools = llm.bind_tools(langchain_tools)   # tools bound to LLM

def call_llm(state: AgentState) -> dict:
    """LLM node — decides what to do next."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

def execute_tools(state: AgentState) -> dict:
    """Tool node — executes all pending tool calls."""
    last_message = state["messages"][-1]
    tool_results = []
    for tool_call in last_message.tool_calls:
        func  = TOOL_REGISTRY[tool_call["name"]]
        result = func(**tool_call["args"])
        tool_results.append(ToolMessage(
            content=str(result),
            tool_call_id=tool_call["id"]
        ))
    return {"messages": tool_results}

# ── 3. Conditional edge — route based on state ────────
def should_continue(state: AgentState) -> str:
    """Return 'tools' if LLM wants to call tools, 'end' if done."""
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return "end"

# ── 4. Build the graph ────────────────────────────────
graph = StateGraph(AgentState)

graph.add_node("llm",   call_llm)
graph.add_node("tools", execute_tools)

graph.set_entry_point("llm")
graph.add_conditional_edges("llm", should_continue, {
    "tools": "tools",
    "end":   END
})
graph.add_edge("tools", "llm")   # after tools, always go back to LLM

# ── 5. Compile with checkpointer (persistence) ────────
memory  = MemorySaver()
agent   = graph.compile(checkpointer=memory)

# ── 6. Run the agent ──────────────────────────────────
config  = {"configurable": {"thread_id": "session-123"}}
result  = agent.invoke(
    {"messages": [HumanMessage(content="What is 15% of 8500 and what is today's date?")]},
    config=config
)
print(result["messages"][-1].content)
```


<div class="ins"><p>💡 <strong>The thread_id in config enables multi-session persistence.</strong> Every invocation with the same thread_id continues from where it left off — the graph state is checkpointed automatically. Different users get different thread_ids and completely isolated state.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>LangGraph State Reducers — Advanced Patterns</h3><span class="tag tag-blue">Power Feature</span></div>
  <div class="cp-body">
    

```python
# Reducers control how state is updated when nodes return new values

from typing import TypedDict, Annotated
import operator

class ResearchState(TypedDict):
    # operator.add — appends new items to existing list
    messages:    Annotated[list, operator.add]
    sources:     Annotated[list, operator.add]

    # No reducer — node's returned value REPLACES current value
    current_task: str
    is_complete:  bool

    # Custom reducer — keep only last 10 messages
    short_memory: Annotated[list, lambda old, new: (old + new)[-10:]]

# Parallel nodes — execute concurrently in the graph
graph.add_node("search",    search_node)
graph.add_node("calculate", calc_node)
# Both run in parallel when the graph reaches this fork
graph.add_edge("start", "search")
graph.add_edge("start", "calculate")
# Both must complete before proceeding
graph.add_edge(["search", "calculate"], "synthesize")
```


  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — HUMAN-IN-THE-LOOP ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🧑‍💻</span><h3>Human-in-the-Loop — Pause Before Consequential Actions</h3><span class="tag tag-violet">Safety Critical</span></div>
  <div class="cp-body">
<p>Never let an agent autonomously send emails, delete data, make purchases, or call external APIs without human approval. LangGraph's interrupt mechanism pauses the graph at any node, waits for human input, then resumes.</p>
    

```python
from langgraph.graph import StateGraph, END, interrupt

# ── Interrupt before executing a tool ─────────────────
SENSITIVE_TOOLS = {"send_email", "delete_record", "make_payment"}

def execute_tools_with_approval(state: AgentState) -> dict:
    last_message = state["messages"][-1]
    tool_results = []

    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]

        if tool_name in SENSITIVE_TOOLS:
            # Pause and ask human for approval
            approval = interrupt({
                "question": f"Agent wants to call {tool_name} with args: {tool_call['args']}. Approve?",
                "tool_name": tool_name,
                "tool_args": tool_call["args"]
            })
            if not approval.get("approved"):
                tool_results.append(ToolMessage(
                    content="User declined this action.",
                    tool_call_id=tool_call["id"]
                ))
                continue

        # Approved or non-sensitive — execute
        result = TOOL_REGISTRY[tool_name](**tool_call["args"])
        tool_results.append(ToolMessage(content=str(result),
                                        tool_call_id=tool_call["id"]))

    return {"messages": tool_results}

# ── Resuming after human approval ─────────────────────
# When the graph is interrupted, it returns a snapshot
# The human inspects and provides a response
# Then you resume with Command(resume=response)

from langgraph.types import Command

# Graph pauses here, returns to caller
result = agent.invoke(task, config)

# Human reviews the interrupt value
pending = result["__interrupt__"]
print(f"Waiting for approval: {pending[0]['value']}")

# Human approves (or rejects)
human_response = {"approved": True}   # or False

# Resume the graph from where it paused
result = agent.invoke(Command(resume=human_response), config)
```


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
  <a href="/learning/ai-ml/part5-rag/p5-m18-rag-pipelines/">← P5-M18: RAG Pipelines</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part6-agents/p6-m20-tool-design/">Next: P6-M20 — Tool Design →</a>
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
