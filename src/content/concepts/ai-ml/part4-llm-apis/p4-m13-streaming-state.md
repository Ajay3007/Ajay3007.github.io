---
title: "P4-M13 - Streaming & Conversation State"
description: "Part 4 — LLM API Mastery · Module 13 of 14 Streaming Conversation State Stream tokens in real-time and manage multi-turn conversations without losing context ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part4-llm-apis
order: 413
ownHeader: true
url: /learning/ai-ml/part4-llm-apis/p4-m13-streaming-state/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1a0a3a 40%,#312e81 70%,#4f46e5 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a5b4fc;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#e0e7ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#e0e7ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0f0a1e;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#a5b4fc;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#818cf8;border-bottom-color:#818cf8}
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
.p-indigo .cp-hdr{background:#eef2ff}[data-theme=dark] .p-indigo .cp-hdr{background:#1e1a3a}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}.tag-indigo{background:#e0e7ff;color:#3730a3}
.cb{background:#0f0a1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #4f46e5}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#e0e7ff;white-space:pre}
.cm{color:#6d6875}.ck{color:#a5b4fc}.cv{color:#f0c080}.cs{color:#818cf8}
.ins{background:#eef2ff;border:1.5px solid #4f46e5;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e1a3a;border-color:#4f46e5}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3730a3}[data-theme=dark] .ins strong{color:#818cf8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.wk-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
.wk-table th{background:#1e1a3a;color:#e0e7ff;padding:.7rem 1rem;text-align:left;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}
.wk-table td{padding:.65rem 1rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.6}
.wk-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.wk-num{font-family:monospace;font-weight:700;color:#4f46e5;white-space:nowrap}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#4f46e5;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#1e1a3a;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#4f46e5;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#e0e7ff;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#4f46e5;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#4f46e5}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#4f46e5;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #4f46e5;transition:all .15s}
.mod-nav a:hover{background:#4f46e5;color:#fff}
.mod-nav .nb{background:#4f46e5;color:#fff}
.mod-nav .nb:hover{background:#3730a3;border-color:#3730a3}
.proj-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#15803d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#15803d}
/* token meter */
.token-bar{background:var(--bg-color,#f0f0f0);border-radius:8px;height:18px;overflow:hidden;margin:.5rem 0;position:relative}
.token-fill{height:100%;border-radius:8px;display:flex;align-items:center;padding-left:.5rem;font-size:.72rem;font-weight:700;color:#fff;font-family:monospace}
.tf-sys{background:#4f46e5;width:15%}
.tf-hist{background:#818cf8;width:55%}
.tf-resp{background:#a5b4fc;width:20%;color:#1e1a3a}
.tf-avail{background:#e0e7ff;width:10%;color:#3730a3}
.token-legend{display:flex;flex-wrap:wrap;gap:.5rem;margin:.4rem 0;font-size:.75rem}
.tl-dot{width:10px;height:10px;border-radius:2px;display:inline-block;margin-right:.3rem}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 4 — LLM API Mastery &nbsp;·&nbsp; Module 13 of 14</div>
  <div class="mod-title">Streaming &amp; Conversation State</div>
  <div class="mod-subtitle">Stream tokens in real-time and manage multi-turn conversations without losing context</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 SSE · FastAPI · tiktoken · Redis</span>
    <span class="mod-pill">📋 Prerequisite: P4-M12</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">⚡ Streaming Basics</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🌐 Streaming in FastAPI</button>
  <button class="tab-btn" onclick="vt(event,'t3')">💬 Conversation State</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📏 Context Management</button>
  <button class="tab-btn" onclick="vt(event,'t5')">💾 Persistent History</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-indigo">UX + Architecture</span></div>
  <div class="cp-body">
    <p>Two skills that separate prototype AI apps from production ones: streaming responses and conversation state management. Without streaming, users stare at a blank screen for 10 seconds. Without proper state management, your chatbot forgets everything after one message.</p>
    <ul>
      <li><strong>Streaming basics</strong> — how Server-Sent Events work, streaming from Anthropic and OpenAI SDKs</li>
      <li><strong>Streaming in FastAPI</strong> — exposing a streaming endpoint that the browser or client can consume</li>
      <li><strong>Conversation state</strong> — the messages array pattern, multi-turn management, turn limits</li>
      <li><strong>Context window management</strong> — counting tokens with tiktoken, sliding window, summarisation strategies</li>
      <li><strong>Persistent history</strong> — storing and retrieving conversation history from SQLite and Redis</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Why These Skills Matter</h3><span class="tag tag-blue">Context</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>Streaming</strong> — users perceive a streaming response as 3-5× faster than waiting for the same content to appear all at once. Every production LLM app streams.</li>
      <li><strong>Conversation state</strong> — LLMs are stateless. Each API call is independent. Your code is responsible for maintaining the illusion of memory by sending the full message history with every request.</li>
      <li><strong>Context management</strong> — context windows are expensive. A 200k token context window costs ~20× more per token than a 10k window. You need strategies to keep context lean without losing important information.</li>
      <li><strong>Persistent history</strong> — users expect their conversation to survive a page refresh. You need a storage layer.</li>
    </ul>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — STREAMING BASICS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>How Streaming Works — Server-Sent Events</h3><span class="tag tag-indigo">Concept First</span></div>
  <div class="cp-body">
    <p>LLM streaming uses Server-Sent Events (SSE) — an HTTP connection stays open and the server pushes data chunks as they are generated. Each chunk contains a few tokens. The client appends them to build the final response.</p>
    <div class="cb"><pre><span class="ck"># Without streaming — user waits 8 seconds, then sees everything at once</span>
response = client.messages.create(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"Explain RAG in detail"</span>}]
)
print(response.content[<span class="cv">0</span>].text)   <span class="ck"># appears all at once after 8s</span>
<span class="ck"># With streaming — first token appears in ~300ms, rest stream in</span>
with client.messages.stream(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"Explain RAG in detail"</span>}]
) as stream:
    for text in stream.text_stream:
        print(text, end=<span class="cs">""</span>, flush=<span class="cv">True</span>)   <span class="ck"># each chunk printed as it arrives</span>
<span class="ck"># Get final message after streaming completes</span>
final_message = stream.get_final_message()
print(<span class="cs">f"\nTokens used: {final_message.usage.input_tokens} in, {final_message.usage.output_tokens} out"</span>)</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Streaming Events — What Actually Arrives</h3><span class="tag tag-blue">Under the Hood</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Low-level event iteration — see every event type</span>
with client.messages.stream(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">512</span>,
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"Say hello"</span>}]
) as stream:
    for event in stream:
        match event.type:
            case <span class="cs">"message_start"</span>:
                <span class="ck"># First event — contains model, message id</span>
                print(<span class="cs">f"Started: {event.message.id}"</span>)
            case <span class="cs">"content_block_start"</span>:
                <span class="ck"># A new content block begins (text or tool_use)</span>
                print(<span class="cs">f"Block type: {event.content_block.type}"</span>)
            case <span class="cs">"content_block_delta"</span>:
                <span class="ck"># A chunk of text (text_delta) or tool input (input_json_delta)</span>
                if event.delta.type == <span class="cs">"text_delta"</span>:
                    print(event.delta.text, end=<span class="cs">""</span>, flush=<span class="cv">True</span>)
            case <span class="cs">"content_block_stop"</span>:
                <span class="ck"># Content block finished</span>
                pass
            case <span class="cs">"message_delta"</span>:
                <span class="ck"># Stop reason and final token counts</span>
                print(<span class="cs">f"\nStop: {event.delta.stop_reason}"</span>)
            case <span class="cs">"message_stop"</span>:
                <span class="ck"># Streaming complete</span>
                print(<span class="cs">"Stream finished"</span>)
 
<span class="ck"># OpenAI streaming — similar pattern</span>
with client.chat.completions.stream(
    model=<span class="cs">"gpt-4o"</span>,
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"Say hello"</span>}]
) as stream:
    for chunk in stream:
        delta = chunk.choices[<span class="cv">0</span>].delta
        if delta.content:
            print(delta.content, end=<span class="cs">""</span>, flush=<span class="cv">True</span>)</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Streaming with Tool Calls</h3><span class="tag tag-teal">Advanced</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Streaming tool use — tool input arrives in chunks too</span>
with client.messages.stream(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    tools=tools,
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"What's the weather in Mumbai?"</span>}]
) as stream:
    current_tool_input = <span class="cs">""</span>
    for event in stream:
        if event.type == <span class="cs">"content_block_start"</span>:
            if event.content_block.type == <span class="cs">"tool_use"</span>:
                tool_name = event.content_block.name
                tool_id   = event.content_block.id
        elif event.type == <span class="cs">"content_block_delta"</span>:
            if event.delta.type == <span class="cs">"text_delta"</span>:
                print(event.delta.text, end=<span class="cs">""</span>, flush=<span class="cv">True</span>)
            elif event.delta.type == <span class="cs">"input_json_delta"</span>:
                current_tool_input += event.delta.partial_json  <span class="ck"># accumulate</span>
        elif event.type == <span class="cs">"content_block_stop"</span>:
            if current_tool_input:
                import json
                tool_args = json.loads(current_tool_input)
                <span class="ck"># Now execute the tool...</span>
                current_tool_input = <span class="cs">""</span>
 
    final = stream.get_final_message()
    <span class="ck"># Use final.content to build the next turn of the conversation</span></pre></div>
    <div class="ins"><p>💡 <strong>Always call <code>get_final_message()</code> after streaming.</strong> This gives you the complete, assembled message including all content blocks — safe to append directly to your conversation history. Never try to assemble the message yourself from streaming chunks.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — STREAMING IN FASTAPI ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>FastAPI Streaming Endpoint — SSE Pattern</h3><span class="tag tag-indigo">Production Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import anthropic, asyncio, json
 
app = FastAPI()
client = anthropic.AsyncAnthropic()   <span class="ck"># async client for FastAPI</span>
 
class ChatRequest(BaseModel):
    message:  str
    session_id: str = <span class="cs">"default"</span>
<span class="ck"># ── Streaming endpoint ────────────────────────────────</span>
@app.post(<span class="cs">"/chat/stream"</span>)
async def chat_stream(request: ChatRequest):
 
    async def generate():
        async with client.messages.stream(
            model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
            max_tokens=<span class="cv">2048</span>,
            messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: request.message}]
        ) as stream:
            async for text in stream.text_stream:
                <span class="ck"># SSE format: "data: {payload}
 
"</span>
                yield <span class="cs">f"data: {json.dumps({'text': text})}
 
"</span>
            <span class="ck"># Send final event with usage stats</span>
            final = await stream.get_final_message()
            yield <span class="cs">f"data: {json.dumps({'done': True, 'usage': {'input': final.usage.input_tokens, 'output': final.usage.output_tokens}})}
 
"</span>
 
    return StreamingResponse(
        generate(),
        media_type=<span class="cs">"text/event-stream"</span>,
        headers={
            <span class="cs">"Cache-Control"</span>: <span class="cs">"no-cache"</span>,
            <span class="cs">"X-Accel-Buffering"</span>: <span class="cs">"no"</span>,   <span class="ck"># disable nginx buffering</span>
        }
    )</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🖥</span><h3>Consuming the Stream — Browser JavaScript</h3><span class="tag tag-blue">Frontend Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck">// Browser JavaScript — EventSource API for SSE</span>
async function streamChat(message) {
  const response = await fetch('/chat/stream', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message})
  });
 
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
 
  while (true) {
    const {done, value} = await reader.read();
    if (done) break;
 
    buffer += decoder.decode(value, {stream: true});
    const lines = buffer.split('\n');
    buffer = lines.pop();   // keep incomplete line in buffer
 
    for (const line of lines) {
      if (!line.startsWith('data: ')) continue;
      const data = JSON.parse(line.slice(6));
 
      if (data.text) {
        document.getElementById('response').textContent += data.text;
      }
      if (data.done) {
        console.log('Tokens:', data.usage);
      }
    }
  }
}
 
<span class="ck">// Python client consuming the stream</span>
import httpx, json
 
async def consume_stream(message: str):
    async with httpx.AsyncClient(timeout=<span class="cv">60</span>) as http:
        async with http.stream(<span class="cs">"POST"</span>, <span class="cs">"http://localhost:8000/chat/stream"</span>,
                               json={<span class="cs">"message"</span>: message}) as response:
            async for line in response.aiter_lines():
                if not line.startswith(<span class="cs">"data: "</span>):
                    continue
                data = json.loads(line[<span class="cv">6</span>:])
                if data.get(<span class="cs">"text"</span>):
                    print(data[<span class="cs">"text"</span>], end=<span class="cs">""</span>, flush=<span class="cv">True</span>)</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Streaming Gotchas</h3><span class="tag tag-teal">Common Issues</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>Nginx buffering</strong> — nginx buffers responses by default. Add <code>X-Accel-Buffering: no</code> header to disable or configure <code>proxy_buffering off</code> in nginx config.</li>
      <li><strong>Error handling mid-stream</strong> — errors can occur after streaming has started (e.g. rate limit hit at token 500). Wrap your generator in try/except and send an error SSE event before closing.</li>
      <li><strong>Connection drops</strong> — if the client disconnects mid-stream, FastAPI's <code>StreamingResponse</code> will raise a <code>anyio.EndOfStream</code>. Handle this gracefully.</li>
      <li><strong>Buffered proxies</strong> — some cloud platforms (AWS ALB, certain CDNs) buffer SSE. Use WebSockets instead if SSE is unreliable in your deployment.</li>
    </ul>
    <div class="cb"><pre><span class="ck"># Error-safe streaming generator</span>
async def generate_safe():
    try:
        async with client.messages.stream(...) as stream:
            async for text in stream.text_stream:
                yield <span class="cs">f"data: {json.dumps({'text': text})}
 
"</span>
    except anthropic.RateLimitError:
        yield <span class="cs">f"data: {json.dumps({'error': 'rate_limit', 'message': 'Too many requests. Please wait a moment.'})}
 
"</span>
    except anthropic.APIStatusError as e:
        yield <span class="cs">f"data: {json.dumps({'error': 'api_error', 'status': e.status_code})}
 
"</span>
    except Exception as e:
        yield <span class="cs">f"data: {json.dumps({'error': 'unknown', 'message': str(e)})}
 
"</span>
    finally:
        yield <span class="cs">"data: {"done": true}
 
"</span>   <span class="ck"># always send done event</span></pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — CONVERSATION STATE ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">💬</span><h3>The Messages Array — LLMs Are Stateless</h3><span class="tag tag-indigo">Critical Concept</span></div>
  <div class="cp-body">
    <p>LLMs have no memory between API calls. Every call is completely independent. The only "memory" is the messages array you send. Your code is entirely responsible for maintaining conversation state.</p>
    <div class="cb"><pre><span class="ck"># ── WRONG — no conversation state ─────────────────────</span>
response1 = client.messages.create(
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"My name is Ajay"</span>}], ...
)
response2 = client.messages.create(
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"What is my name?"</span>}], ...
)
<span class="ck"># Model: "I don't know your name" — it never saw the first message</span>
<span class="ck"># ── CORRECT — full history sent every call ─────────────</span>
messages = []
 
<span class="ck"># Turn 1</span>
messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"My name is Ajay"</span>})
response = client.messages.create(model=<span class="cs">"..."</span>, max_tokens=<span class="cv">512</span>, messages=messages)
messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: response.content[<span class="cv">0</span>].text})
 
<span class="ck"># Turn 2</span>
messages.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: <span class="cs">"What is my name?"</span>})
response = client.messages.create(model=<span class="cs">"..."</span>, max_tokens=<span class="cv">512</span>, messages=messages)
messages.append({<span class="cs">"role"</span>: <span class="cs">"assistant"</span>, <span class="cs">"content"</span>: response.content[<span class="cv">0</span>].text})
<span class="ck"># Model: "Your name is Ajay" — it sees the full history</span></pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗</span><h3>ConversationManager — Clean State Pattern</h3><span class="tag tag-blue">Production Class</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import anthropic
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
 
@dataclass
class Turn:
    role:      str
    content:   str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    tokens:    Optional[int] = None
 
class ConversationManager:
    def __init__(
        self,
        system_prompt: str = <span class="cs">""</span>,
        model: str = <span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens: int = <span class="cv">2048</span>,
    ):
        self.client        = anthropic.Anthropic()
        self.system_prompt = system_prompt
        self.model         = model
        self.max_tokens    = max_tokens
        self.history: list[Turn] = []
 
    def _build_messages(self) -> list[dict]:
        return [
            {<span class="cs">"role"</span>: t.role, <span class="cs">"content"</span>: t.content}
            for t in self.history
        ]
 
    def chat(self, user_message: str) -> str:
        self.history.append(Turn(role=<span class="cs">"user"</span>, content=user_message))
 
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self._build_messages()
        )
 
        reply = response.content[<span class="cv">0</span>].text
        self.history.append(Turn(
            role=<span class="cs">"assistant"</span>,
            content=reply,
            tokens=response.usage.output_tokens
        ))
        return reply
 
    def chat_stream(self, user_message: str):
        self.history.append(Turn(role=<span class="cs">"user"</span>, content=user_message))
        full_reply = <span class="cs">""</span>
 
        with self.client.messages.stream(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self._build_messages()
        ) as stream:
            for text in stream.text_stream:
                full_reply += text
                yield text
            final = stream.get_final_message()
 
        self.history.append(Turn(
            role=<span class="cs">"assistant"</span>,
            content=full_reply,
            tokens=final.usage.output_tokens
        ))
 
    def clear(self):
        self.history = []
 
    @property
    def turn_count(self) -> int:
        return len([t for t in self.history if t.role == <span class="cs">"user"</span>])
 
<span class="ck"># Usage</span>
conv = ConversationManager(system_prompt=<span class="cs">"You are a helpful coding assistant."</span>)
print(conv.chat(<span class="cs">"My name is Ajay and I work with DPDK"</span>))
print(conv.chat(<span class="cs">"What is my name and what technology do I work with?"</span>))
print(conv.turn_count)   <span class="ck"># 2</span></pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>System Prompt Design for Multi-Turn</h3><span class="tag tag-teal">Best Practice</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># System prompt rules for multi-turn conversations</span>
<span class="ck"># 1. State what information the model should REMEMBER across turns</span>
system = <span class="cs">"""You are a helpful coding assistant.
 
Remember and use throughout the conversation:
- The user's name and role (if they tell you)
- Programming languages they work with
- Specific codebase or project context they share
- Decisions made in earlier turns of this conversation
 
When the user references "the function" or "the code" without specifying,
use context from earlier in the conversation."""</span>
<span class="ck"># 2. Define how to handle ambiguous references</span>
system += <span class="cs">"""
 
If a reference is ambiguous and cannot be resolved from context,
ask for clarification before answering."""</span>
<span class="ck"># 3. Set turn-specific behaviour</span>
system += <span class="cs">"""
 
For code reviews: always reference specific line numbers.
For debugging: always ask to see the error message if not provided."""</span></pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — CONTEXT MANAGEMENT ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">📏</span><h3>Context Windows and Token Counting</h3><span class="tag tag-indigo">Cost Control</span></div>
  <div class="cp-body">
    <p>Every token in your context costs money and increases latency. As conversations grow, managing context becomes essential.</p>
    <div class="token-bar"><div class="token-fill tf-sys">System 15%</div><div class="token-fill tf-hist">History 55%</div><div class="token-fill tf-resp" style="color:#1e1a3a">Reserve 20%</div><div class="token-fill tf-avail" style="color:#3730a3">Avail 10%</div></div>
    <div class="token-legend">
      <span><span class="tl-dot" style="background:#4f46e5"></span>System prompt</span>
      <span><span class="tl-dot" style="background:#818cf8"></span>Conversation history</span>
      <span><span class="tl-dot" style="background:#a5b4fc"></span>Reserved for response</span>
      <span><span class="tl-dot" style="background:#e0e7ff"></span>Available for next turn</span>
    </div>
    <div class="cb"><pre>pip install tiktoken   <span class="ck"># OpenAI's fast token counter — works for Claude too (approx)</span>
 
import tiktoken
 
def count_tokens(text: str, model: str = <span class="cs">"cl100k_base"</span>) -> int:
    """Approximate token count. cl100k_base works for GPT-4 and Claude."""
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))
 
def count_messages_tokens(messages: list[dict]) -> int:
    total = <span class="cv">0</span>
    for msg in messages:
        total += count_tokens(msg[<span class="cs">"content"</span>])
        total += <span class="cv">4</span>   <span class="ck"># overhead per message (role + formatting)</span>
    return total + <span class="cv">2</span>   <span class="ck"># reply priming tokens</span>
<span class="ck"># Check context usage before sending</span>
MAX_CONTEXT = <span class="cv">180_000</span>   <span class="ck"># Claude 3.5 Sonnet context window</span>
RESERVE_TOKENS = <span class="cv">4_096</span>  <span class="ck"># always reserve for response</span>
 
def will_fit(messages: list, system: str) -> bool:
    used = count_messages_tokens(messages) + count_tokens(system)
    return used + RESERVE_TOKENS < MAX_CONTEXT
 
<span class="ck"># Anthropic's own token counter (exact, not approximate)</span>
response = client.messages.count_tokens(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    system=system_prompt,
    messages=messages
)
print(response.input_tokens)   <span class="ck"># exact count before sending</span></pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🪟</span><h3>Sliding Window — Keep Last N Turns</h3><span class="tag tag-blue">Simple Strategy</span></div>
  <div class="cp-body">
    <div class="cb"><pre>def sliding_window(
    messages: list[dict],
    max_tokens: int = <span class="cv">100_000</span>,
    min_turns: int = <span class="cv">2</span>
) -> list[dict]:
    """
    Keep as many recent messages as fit within max_tokens.
    Always keep at least min_turns (user+assistant pairs).
    """
    <span class="ck"># Always keep messages in pairs (user + assistant)</span>
    <span class="ck"># Start from most recent, work backwards</span>
    result = []
    token_count = <span class="cv">0</span>
    pairs = []
 
    <span class="ck"># Group into user+assistant pairs</span>
    i = <span class="cv">0</span>
    while i < len(messages) - <span class="cv">1</span>:
        if messages[i][<span class="cs">"role"</span>] == <span class="cs">"user"</span> and messages[i+<span class="cv">1</span>][<span class="cs">"role"</span>] == <span class="cs">"assistant"</span>:
            pairs.append((messages[i], messages[i+<span class="cv">1</span>]))
            i += <span class="cv">2</span>
        else:
            i += <span class="cv">1</span>
    <span class="ck"># Always include last user message</span>
    if messages and messages[-<span class="cv">1</span>][<span class="cs">"role"</span>] == <span class="cs">"user"</span>:
        result = [messages[-<span class="cv">1</span>]]
        token_count = count_tokens(messages[-<span class="cv">1</span>][<span class="cs">"content"</span>])
        pairs_to_check = pairs
    else:
        pairs_to_check = pairs
 
    <span class="ck"># Add pairs from most recent backwards until we hit the limit</span>
    included = []
    for user_msg, asst_msg in reversed(pairs_to_check):
        pair_tokens = count_tokens(user_msg[<span class="cs">"content"</span>]) + count_tokens(asst_msg[<span class="cs">"content"</span>])
        if token_count + pair_tokens > max_tokens and len(included) >= min_turns:
            break
        included.insert(<span class="cv">0</span>, (user_msg, asst_msg))
        token_count += pair_tokens
 
    for u, a in included:
        result = [u, a] + result
 
    return result</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Summarisation Strategy — Compress Old History</h3><span class="tag tag-teal">Better Than Sliding Window</span></div>
  <div class="cp-body">
    <div class="cb"><pre>async def summarise_old_turns(
    messages: list[dict],
    keep_recent: int = <span class="cv">6</span>
) -> list[dict]:
    """
    When context gets long: summarise all but the last N turns,
    then continue with [summary_message, ...recent_turns].
    """
    if len(messages) <= keep_recent * <span class="cv">2</span>:
        return messages   <span class="ck"># not long enough to summarise</span>
 
    old_turns = messages[:-(keep_recent * <span class="cv">2</span>)]
    recent_turns = messages[-(keep_recent * <span class="cv">2</span>):]
 
    old_text = <span class="cs">"\n"</span>.join(
        <span class="cs">f"{m['role'].upper()}: {m['content']}"</span>
        for m in old_turns
    )
 
    summary_response = await async_client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,   <span class="ck"># use cheaper model for summarisation</span>
        max_tokens=<span class="cv">512</span>,
        messages=[{
            <span class="cs">"role"</span>: <span class="cs">"user"</span>,
            <span class="cs">"content"</span>: <span class="cs">f"""Summarise this conversation history concisely.
Preserve: key facts stated by the user, decisions made, context needed for future turns.
Do not include: greetings, filler, repeated information.
 
{old_text}
 
Provide a dense 3-5 sentence summary:"""</span>
        }]
    )
    summary = summary_response.content[<span class="cv">0</span>].text
 
    <span class="ck"># Replace old history with summary message</span>
    summary_msg = {
        <span class="cs">"role"</span>: <span class="cs">"user"</span>,
        <span class="cs">"content"</span>: <span class="cs">f"[Previous conversation summary]: {summary}"</span>
    }
    ack_msg = {
        <span class="cs">"role"</span>: <span class="cs">"assistant"</span>,
        <span class="cs">"content"</span>: <span class="cs">"Understood. I've noted the conversation history."</span>
    }
    return [summary_msg, ack_msg] + recent_turns</pre></div>
    <div class="ins"><p>💡 <strong>Use a cheap fast model (Haiku, GPT-4o-mini) for summarisation.</strong> Summarising a 20-turn conversation with Claude Haiku costs ~$0.001. Using Sonnet would cost ~$0.05. The quality difference for summarisation is negligible, but the cost difference is 50×.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — PERSISTENT HISTORY ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">💾</span><h3>Storing Conversation History — SQLite</h3><span class="tag tag-indigo">Persistence</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import sqlite3, json
from contextlib import contextmanager
from datetime import datetime
 
@contextmanager
def get_db():
    conn = sqlite3.connect(<span class="cs">"conversations.db"</span>)
    conn.row_factory = sqlite3.Row
    conn.execute(<span class="cs">"""
        CREATE TABLE IF NOT EXISTS conversations (
            id          TEXT PRIMARY KEY,
            created_at  TEXT NOT NULL,
            updated_at  TEXT NOT NULL,
            system_prompt TEXT DEFAULT ''
        )
    """</span>)
    conn.execute(<span class="cs">"""
        CREATE TABLE IF NOT EXISTS messages (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id TEXT NOT NULL REFERENCES conversations(id),
            role            TEXT NOT NULL,
            content         TEXT NOT NULL,
            created_at      TEXT NOT NULL,
            token_count     INTEGER
        )
    """</span>)
    conn.commit()
    try:
        yield conn
    finally:
        conn.close()
 
def save_turn(conv_id: str, user_msg: str, assistant_msg: str, tokens: int = <span class="cv">0</span>):
    now = datetime.utcnow().isoformat()
    with get_db() as conn:
        <span class="ck"># Upsert conversation record</span>
        conn.execute(<span class="cs">"""
            INSERT INTO conversations (id, created_at, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET updated_at = ?
        """</span>, (conv_id, now, now, now))
        <span class="ck"># Insert both messages</span>
        conn.executemany(<span class="cs">"""
            INSERT INTO messages (conversation_id, role, content, created_at, token_count)
            VALUES (?, ?, ?, ?, ?)
        """</span>, [
            (conv_id, <span class="cs">"user"</span>,      user_msg,      now, <span class="cv">0</span>),
            (conv_id, <span class="cs">"assistant"</span>, assistant_msg, now, tokens),
        ])
        conn.commit()
 
def load_history(conv_id: str, last_n: int = <span class="cv">0</span>) -> list[dict]:
    with get_db() as conn:
        query = <span class="cs">"SELECT role, content FROM messages WHERE conversation_id = ? ORDER BY id"</span>
        rows = conn.execute(query, (conv_id,)).fetchall()
    messages = [{<span class="cs">"role"</span>: r[<span class="cs">"role"</span>], <span class="cs">"content"</span>: r[<span class="cs">"content"</span>]} for r in rows]
    return messages[-last_n * <span class="cv">2</span>:] if last_n else messages</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Redis for High-Traffic Conversations</h3><span class="tag tag-blue">Scalable</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import redis, json
 
r = redis.Redis(host=<span class="cs">"localhost"</span>, port=<span class="cv">6379</span>, decode_responses=<span class="cv">True</span>)
 
def save_message_redis(session_id: str, role: str, content: str, ttl: int = <span class="cv">3600</span>):
    """Store message in Redis list. TTL in seconds (default: 1 hour)."""
    key = <span class="cs">f"conv:{session_id}"</span>
    message = json.dumps({<span class="cs">"role"</span>: role, <span class="cs">"content"</span>: content})
    r.rpush(key, message)        <span class="ck"># append to list</span>
    r.expire(key, ttl)           <span class="ck"># reset TTL on each message</span>
 
def load_history_redis(session_id: str, last_n: int = <span class="cv">0</span>) -> list[dict]:
    """Load conversation history from Redis."""
    key = <span class="cs">f"conv:{session_id}"</span>
    start = -last_n * <span class="cv">2</span> if last_n else <span class="cv">0</span>
    raw = r.lrange(key, start, -<span class="cv">1</span>)
    return [json.loads(m) for m in raw]
 
def clear_history_redis(session_id: str):
    r.delete(<span class="cs">f"conv:{session_id}"</span>)
 
<span class="ck"># When to use SQLite vs Redis:</span>
<span class="ck"># SQLite  — single server, persistent storage, needs query/search, < 1k concurrent users</span>
<span class="ck"># Redis   — multi-server, ephemeral (TTL), fast read/write, > 1k concurrent sessions</span>
<span class="ck"># Both    — use Redis as cache + SQLite/PostgreSQL for durable archive</span></pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Full Stateful Chat API — Putting It Together</h3><span class="tag tag-teal">Complete Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from fastapi import FastAPI
from pydantic import BaseModel
import anthropic, uuid
 
app = FastAPI()
client = anthropic.AsyncAnthropic()
 
class ChatRequest(BaseModel):
    message:    str
    session_id: str = <span class="cs">""</span>   <span class="ck"># empty = new session</span>
 
class ChatResponse(BaseModel):
    session_id: str
    reply:      str
    turn_count: int
 
@app.post(<span class="cs">"/chat"</span>, response_model=ChatResponse)
async def chat(request: ChatRequest):
    session_id = request.session_id or str(uuid.uuid4())
 
    <span class="ck"># Load existing history</span>
    history = load_history_redis(session_id, last_n=<span class="cv">10</span>)
 
    <span class="ck"># Add new user message</span>
    history.append({<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: request.message})
 
    <span class="ck"># Call LLM with full history</span>
    response = await client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">2048</span>,
        system=<span class="cs">"You are a helpful AI assistant."</span>,
        messages=history
    )
    reply = response.content[<span class="cv">0</span>].text
 
    <span class="ck"># Persist both turns</span>
    save_message_redis(session_id, <span class="cs">"user"</span>,      request.message)
    save_message_redis(session_id, <span class="cs">"assistant"</span>, reply)
 
    turn_count = len(history) // <span class="cv">2</span> + <span class="cv">1</span>
    return ChatResponse(session_id=session_id, reply=reply, turn_count=turn_count)</pre></div>
  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.anthropic.com/en/api/messages-streaming" target="_blank" rel="noopener">Anthropic Streaming Reference — docs.anthropic.com/en/api/messages-streaming</a></td><td>Complete SSE event reference for Claude streaming including all event types and formats.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://platform.openai.com/docs/api-reference/streaming" target="_blank" rel="noopener">OpenAI Streaming Docs — platform.openai.com</a></td><td>OpenAI's streaming API reference with chunk formats.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse" target="_blank" rel="noopener">FastAPI StreamingResponse — fastapi.tiangolo.com</a></td><td>Official FastAPI documentation on streaming responses.</td></tr>
    <tr><td class="res-type">Library</td><td><a href="https://github.com/openai/tiktoken" target="_blank" rel="noopener">tiktoken — github.com/openai/tiktoken</a></td><td>Fast token counter by OpenAI. Works for approximate Claude token counting too.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://redis.io/docs/clients/python/" target="_blank" rel="noopener">Redis Python Client — redis.io/docs</a></td><td>Official redis-py documentation for conversation state storage at scale.</td></tr>
  </tbody>
</table>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Streaming Chatbot API with Persistent Sessions</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build a complete stateful chatbot API with streaming responses, session management, and context window control.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>POST /chat/stream/{session_id}</strong> — streaming SSE endpoint. New session if session_id = "new". Streams tokens as they arrive.</li>
      <li><strong>GET /sessions/{session_id}/history</strong> — return full conversation history as JSON</li>
      <li><strong>DELETE /sessions/{session_id}</strong> — clear a session</li>
      <li><strong>GET /sessions/{session_id}/stats</strong> — return: turn count, total tokens used, session age</li>
      <li>Persist conversation to SQLite — history survives server restarts</li>
      <li>Context window management: if history exceeds 50k tokens, apply sliding window (keep last 10 turns)</li>
      <li>Custom system prompt per session — passed in POST body on first message</li>
      <li>Error-safe streaming — proper SSE error events on API failures</li>
    </ul>
    <h4>Test it</h4>
    <ul>
      <li>Start a session, have a 10-turn conversation, restart the server, continue — history should persist</li>
      <li>Test a 20-turn conversation — verify context management kicks in and older turns are dropped</li>
      <li>Test error handling — disconnect mid-stream and observe how the server handles it</li>
    </ul>
    <p><strong>Skills:</strong> FastAPI StreamingResponse, SQLite persistence, context window management, SSE protocol, session lifecycle</p>
  </div>
</div>
</div><!-- end t7 -->
<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Streaming — Measure Time to First Token</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Quantify the user experience improvement from streaming with real measurements.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write a function that measures time-to-first-token (TTFT) for streaming: record timestamp when you call messages.stream(), record timestamp when you receive the first text chunk. TTFT = second - first.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write a function that measures total time for non-streaming: time from API call to response.content available.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run both on 5 different prompts ranging from 50 to 500 token outputs. For each: record TTFT (stream), total time (stream), total time (non-stream), and subjective UX rating (1-5).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Plot a simple text table: prompt length | stream TTFT | stream total | non-stream total | TTFT speedup.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Key insight to document:</strong> At what output length does streaming provide the most meaningful UX improvement? At what length is it negligible?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Context Window — Observe Forgetting Without History</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Make the stateless nature of LLMs viscerally obvious — then fix it.</p>
    <div class="lab-step"><div class="sn">1</div><div>Have a 5-turn conversation WITHOUT passing history: tell the model your name, your favourite language, a project you're working on. Then ask "What is my name?" in a new API call. Observe the failure.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Repeat with the ConversationManager from Tab 3. Observe that the model correctly answers all questions.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Now test context limits: build a very long conversation (50+ turns of substantial messages). Use client.messages.count_tokens() to track token usage after each turn. At what turn does the token count become concerning?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Apply the sliding_window() function from Tab 4. Verify: (a) recent turns are preserved, (b) the model can still answer questions from recent context, (c) the model correctly says it cannot recall very old turns.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Apply the summarisation strategy. Compare quality: does the model retain important facts from summarised turns? What information gets lost? Is it acceptable for your use case?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Build a Persistent Session Store</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement and test the complete persistence pattern end-to-end.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the SQLite persistence functions from Tab 5: save_turn(), load_history(), and add a list_sessions() function that returns all session IDs and their last updated time.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Build a simple CLI chat loop: ask for user input, call Claude, save both turns to SQLite, print the reply. Accept --session flag to resume an existing session by ID.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test the persistence: start a conversation, note the session ID, kill the process (Ctrl+C), restart with --session [id], verify the model has context from the previous run.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add a --summarise flag that applies the summarisation strategy when history exceeds 20 turns. Verify the summarised history loads correctly on the next session.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Extension:</strong> Replace SQLite with Redis. Set TTL to 10 minutes. Verify that after 10 minutes of inactivity, the session is automatically cleaned up.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P4-M13 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain why streaming feels faster to users even though total time is the same</li>
  <li>Know the SSE event types: message_start, content_block_start, content_block_delta, message_stop</li>
  <li>Can implement streaming with both Anthropic and OpenAI SDKs</li>
  <li>Can build a FastAPI StreamingResponse endpoint that correctly formats SSE data</li>
  <li>Know to add X-Accel-Buffering: no header to prevent nginx from buffering SSE</li>
  <li>Can handle errors mid-stream — sending error SSE events and always sending a done event</li>
  <li>Can explain why LLMs are stateless and what that means for conversation management</li>
  <li>Can implement a ConversationManager that correctly sends full history with every API call</li>
  <li>Can count tokens with tiktoken and with Anthropic's native count_tokens() method</li>
  <li>Can implement a sliding window strategy that keeps the last N turns within a token budget</li>
  <li>Can implement a summarisation strategy using a cheap model for old conversation turns</li>
  <li>Can persist conversation history to SQLite with proper schema and load it back</li>
  <li>Know when to use Redis vs SQLite for conversation storage — and can implement both</li>
  <li>Always call get_final_message() after streaming to get the complete assembled message</li>
  <li>Completed Lab 1: time-to-first-token measurement</li>
  <li>Completed Lab 2: context window observation and management</li>
  <li>Completed Lab 3: persistent session store end-to-end</li>
  <li>Milestone project pushed to GitHub with README</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P4-M14 — Reliability, Cost &amp; Security</strong>. This is the final Part 4 module — covering retries, rate limit handling, cost monitoring, and prompt injection defence before you move to RAG in Part 5.</p>
</div>
</div><!-- end t9 -->
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part4-llm-apis/p4-m12-structured-outputs/">← P4-M12: Structured Outputs</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part4-llm-apis/p4-m14-reliability-security/">Next: P4-M14 — Reliability &amp; Security →</a>
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
    const key = 'p4m13-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
