---
title: "P7-M26 - Prompt Versioning, Cost Monitoring & Caching"
description: "Part 7 — Production Deployment · Module 26 of 27 Prompt Versioning, Cost Monitoring Caching Manage prompt changes safely, track spend, and eliminate redundant LLM calls ⏱ 1…"
domain: ai-ml
track: ai-ml-engineering
module: part7-production
order: 726
ownHeader: true
url: /learning/ai-ml/part7-production/p7-m26-prompt-versioning/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#0c1a40 40%,#1e3a5f 70%,#1d4ed8 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#93c5fd;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#dbeafe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#dbeafe}
.tab-bar{display:flex;flex-wrap:wrap;background:#0c1a40;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#93c5fd;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#60a5fa;border-bottom-color:#60a5fa}
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
.p-blue .cp-hdr{background:#eff6ff}[data-theme=dark] .p-blue .cp-hdr{background:#0c1a40}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.p-navy .cp-hdr{background:#eff6ff}[data-theme=dark] .p-navy .cp-hdr{background:#0c1a40}
.tag-blue{background:#dbeafe;color:#1e40af}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-red{background:#f4d0d0;color:#6c1a1a}.tag-amber{background:#fae8a0;color:#5a3800}
.tag-navy{background:#dbeafe;color:#1e3a5f}
.cb{background:#0c1a40;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1d4ed8}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dbeafe;white-space:pre}
.ck{color:#93c5fd}.cv{color:#f0c080}.cs{color:#60a5fa}
.ins{background:#eff6ff;border:1.5px solid #1d4ed8;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0c1a40;border-color:#1d4ed8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1e3a5f}[data-theme=dark] .ins strong{color:#60a5fa}
.warn{background:#faeaea;border:1.5px solid #fca5a5;border-left:4px solid #dc2626;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#1d4ed8;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#0c1a40;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#1d4ed8;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#dbeafe;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#1d4ed8;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#1d4ed8}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#1d4ed8;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #1d4ed8;transition:all .15s}
.mod-nav a:hover{background:#1d4ed8;color:#fff}
.mod-nav .nb{background:#1d4ed8;color:#fff}
.mod-nav .nb:hover{background:#1e3a8a;border-color:#1e3a8a}
.proj-box{background:#eff6ff;border:1.5px solid #93c5fd;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#1e40af;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#1e40af}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">Part 7 — Production &amp; Deployment &nbsp;·&nbsp; Module 26 of 27</div>
  <div class="mod-title">Prompt Versioning, Cost Monitoring &amp; Caching</div>
  <div class="mod-subtitle">Manage prompt changes safely, track spend, and eliminate redundant LLM calls</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 Git · Redis · Promptfoo · SQLite</span>
    <span class="mod-pill">📋 Prerequisite: P7-M25</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📝 Prompt Versioning</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🧪 Prompt Testing</button>
  <button class="tab-btn" onclick="vt(event,'t3')">💰 Cost Monitoring</button>
  <button class="tab-btn" onclick="vt(event,'t4')">⚡ Response Caching</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔄 Prompt Caching</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-navy">AI-Specific Ops</span></div>
  <div class="cp-body">
    <p>The operational challenges unique to AI systems: prompts silently change behaviour when edited, LLM costs accumulate invisibly, and identical queries hit the API repeatedly. This module gives you systems for each problem.</p>
    <ul>
      <li><strong>Prompt versioning</strong> — storing prompts in DB/Git, tracking changes, rollback on regression</li>
      <li><strong>Prompt testing</strong> — regression testing before deploying a changed prompt</li>
      <li><strong>Cost monitoring</strong> — per-user, per-endpoint, per-model spend dashboards</li>
      <li><strong>Response caching</strong> — semantic deduplication, Redis TTL cache for identical queries</li>
      <li><strong>Anthropic prompt caching</strong> — 90% cost reduction on large repeated system prompts</li>
    </ul>
  </div>
</div>
</div>
<!-- TAB 1 — PROMPT VERSIONING -->
<div id="t1" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Prompt Versioning — Never Lose a Working Prompt</h3><span class="tag tag-navy">Version Control</span></div>
  <div class="cp-body">
    <p>A prompt is code. Like code, it should be versioned, reviewed, and tested before deployment. A casual edit to a production system prompt can break behaviour for every user — silently.</p>
    <div class="cb"><pre>import sqlite3, hashlib, json
from datetime import datetime
from typing import Optional
 
<span class="ck"># ── DB-backed prompt registry ─────────────────────────</span>
def init_prompt_db():
    with sqlite3.connect(<span class="cs">"prompts.db"</span>) as conn:
        conn.execute(<span class="cs">"""CREATE TABLE IF NOT EXISTS prompts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            version     INTEGER NOT NULL,
            content     TEXT NOT NULL,
            hash        TEXT NOT NULL,
            author      TEXT,
            notes       TEXT,
            is_active   INTEGER DEFAULT 0,
            created_at  TEXT NOT NULL,
            UNIQUE(name, version))"""</span>)
        conn.execute(<span class="cs">"CREATE INDEX IF NOT EXISTS idx_name ON prompts(name, is_active)"</span>)
 
def register_prompt(name: str, content: str, author: str = <span class="cs">""</span>, notes: str = <span class="cs">""</span>) -> int:
    """Register a new version of a prompt. Returns version number."""
    h   = hashlib.sha256(content.encode()).hexdigest()[:12]
    now = datetime.utcnow().isoformat()
    with sqlite3.connect(<span class="cs">"prompts.db"</span>) as conn:
        row = conn.execute(
            <span class="cs">"SELECT MAX(version) FROM prompts WHERE name=?"</span>, (name,)).fetchone()
        version = (row[<span class="cv">0</span>] or <span class="cv">0</span>) + <span class="cv">1</span>
        conn.execute(<span class="cs">"""INSERT INTO prompts (name,version,content,hash,author,notes,created_at)
            VALUES (?,?,?,?,?,?,?)"""</span>, (name, version, content, h, author, notes, now))
    return version
 
def activate_prompt(name: str, version: int):
    """Activate a specific version — all others for this name become inactive."""
    with sqlite3.connect(<span class="cs">"prompts.db"</span>) as conn:
        conn.execute(<span class="cs">"UPDATE prompts SET is_active=0 WHERE name=?"</span>, (name,))
        conn.execute(
            <span class="cs">"UPDATE prompts SET is_active=1 WHERE name=? AND version=?"</span>,
            (name, version))
 
def get_active_prompt(name: str) -> Optional[dict]:
    with sqlite3.connect(<span class="cs">"prompts.db"</span>) as conn:
        row = conn.execute(
            <span class="cs">"SELECT content, version, hash FROM prompts WHERE name=? AND is_active=1"</span>,
            (name,)).fetchone()
    if not row:
        return None
    return {<span class="cs">"content"</span>: row[<span class="cv">0</span>], <span class="cs">"version"</span>: row[<span class="cv">1</span>], <span class="cs">"hash"</span>: row[<span class="cv">2</span>]}
 
def rollback_prompt(name: str, to_version: int):
    """Rollback to a previous version."""
    activate_prompt(name, to_version)
    print(<span class="cs">f"Rolled back {name!r} to version {to_version}"</span>)
 
def list_prompt_history(name: str) -> list[dict]:
    with sqlite3.connect(<span class="cs">"prompts.db"</span>) as conn:
        rows = conn.execute(<span class="cs">"""SELECT version, hash, author, is_active, created_at, notes
            FROM prompts WHERE name=? ORDER BY version DESC"""</span>, (name,)).fetchall()
    return [{<span class="cs">"version"</span>: r[<span class="cv">0</span>], <span class="cs">"hash"</span>: r[<span class="cv">1</span>], <span class="cs">"author"</span>: r[<span class="cv">2</span>],
             <span class="cs">"active"</span>: bool(r[<span class="cv">3</span>]), <span class="cs">"created"</span>: r[<span class="cv">4</span>], <span class="cs">"notes"</span>: r[<span class="cv">5</span>]} for r in rows]
 
<span class="ck"># Usage workflow:</span>
<span class="ck"># v1 = register_prompt("rag_system", "You are a helpful assistant...")     → version 1</span>
<span class="ck"># activate_prompt("rag_system", 1)                                          → live</span>
<span class="ck"># v2 = register_prompt("rag_system", "You are a precise assistant...")     → version 2</span>
<span class="ck"># run_regression_tests("rag_system", v2)  ← test BEFORE activating</span>
<span class="ck"># activate_prompt("rag_system", 2)                                          → live</span>
<span class="ck"># if metrics worsen: rollback_prompt("rag_system", 1)                      → instant</span></pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📁</span><h3>Git-Based Prompt Management</h3><span class="tag tag-blue">File-First</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># prompts/ directory — treat prompts like source files</span>
<span class="ck">#</span>
<span class="ck"># prompts/</span>
<span class="ck"># ├── rag_system.txt           ← current version</span>
<span class="ck"># ├── rag_system.v1.txt        ← archived version</span>
<span class="ck"># ├── chat_system.txt</span>
<span class="ck"># └── agent_system.txt</span>
 
from pathlib import Path
import hashlib
 
PROMPT_DIR = Path(<span class="cs">"prompts"</span>)
 
def load_prompt(name: str) -> str:
    """Load prompt from file. Falls back to DB if file not found."""
    path = PROMPT_DIR / <span class="cs">f"{name}.txt"</span>
    if path.exists():
        return path.read_text(encoding=<span class="cs">"utf-8"</span>)
    <span class="ck"># Fall back to DB</span>
    p = get_active_prompt(name)
    return p[<span class="cs">"content"</span>] if p else <span class="cs">""</span>
 
def prompt_changed(name: str) -> bool:
    """Detect if the file version differs from the DB active version."""
    file_content = load_prompt(name)
    db_version   = get_active_prompt(name)
    if not db_version:
        return <span class="cv">True</span>
    file_hash = hashlib.sha256(file_content.encode()).hexdigest()[:12]
    return file_hash != db_version[<span class="cs">"hash"</span>]
 
<span class="ck"># CI/CD hook: on prompt file change, require test pass before merge</span>
<span class="ck"># .github/workflows/test-prompts.yml</span>
<span class="ck"># jobs:</span>
<span class="ck">#   test-prompts:</span>
<span class="ck">#     steps:</span>
<span class="ck">#       - run: python -m pytest tests/test_prompts.py -v</span>
<span class="ck">#       - run: python scripts/sync_prompts_to_db.py  # only if tests pass</span></pre></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- TAB 2 — PROMPT TESTING -->
<div id="t2" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🧪</span><h3>Prompt Regression Testing</h3><span class="tag tag-navy">Test Before Deploy</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pytest, anthropic
 
client = anthropic.Anthropic()
 
def call_with_prompt(prompt_content: str, user_message: str) -> str:
    response = client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">512</span>,
        system=prompt_content,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user_message}]
    )
    return response.content[<span class="cv">0</span>].text
 
<span class="ck"># ── Deterministic assertions (temperature=0) ──────────</span>
<span class="ck"># These must pass for every prompt version before activation</span>
 
RAG_PROMPT_V2 = load_prompt_version(<span class="cs">"rag_system"</span>, version=<span class="cv">2</span>)
 
def test_rag_stays_grounded():
    """Prompt must refuse to answer from outside context."""
    reply = call_with_prompt(RAG_PROMPT_V2,
                             <span class="cs">"What is the capital of France? (Context: [empty])"</span>)
    forbidden = [<span class="cs">"Paris"</span>, <span class="cs">"France"</span>]
    for word in forbidden:
        assert word not in reply, <span class="cs">f"Hallucinated '{word}' outside context"</span>
 
def test_rag_uses_context():
    """Prompt must use provided context."""
    ctx = <span class="cs">"The DPDK mempool is initialised with rte_mempool_create()."</span>
    reply = call_with_prompt(RAG_PROMPT_V2,
                             <span class="cs">f"Context: {ctx}\n\nHow is DPDK mempool initialised?"</span>)
    assert <span class="cs">"rte_mempool_create"</span> in reply
 
def test_rag_declines_gracefully():
    """Prompt must produce the exact 'I don't know' phrase when context empty."""
    reply = call_with_prompt(RAG_PROMPT_V2,
                             <span class="cs">"Context: [no documents retrieved]\n\nWhat is VPP?"</span>)
    assert <span class="cs">"don't have"</span> in reply.lower() or <span class="cs">"not contain"</span> in reply.lower()
 
<span class="ck"># ── LLM-as-judge tests (non-deterministic behaviour) ──</span>
from eval_helpers import judge_faithfulness
 
def test_rag_faithfulness_score():
    """Faithfulness must be >= 0.85 on held-out test set."""
    scores = []
    for case in HELD_OUT_TEST_CASES:
        reply = call_with_prompt(RAG_PROMPT_V2, case[<span class="cs">"prompt"</span>])
        v = judge_faithfulness(case[<span class="cs">"context"</span>], reply)
        scores.append(v.score)
    avg = sum(scores) / len(scores)
    assert avg >= <span class="cv">0.85</span>, <span class="cs">f"Faithfulness {avg:.3f} < 0.85 threshold"</span>
<span class="ck"># Run: pytest tests/test_prompts.py -v</span>
<span class="ck"># If tests pass: activate_prompt("rag_system", 2)</span>
<span class="ck"># If tests fail: do NOT activate — investigate and fix prompt</span></pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- TAB 3 — COST MONITORING -->
<div id="t3" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">💰</span><h3>Cost Monitoring — Know Where Every Dollar Goes</h3><span class="tag tag-navy">Financial Control</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import sqlite3
from datetime import datetime, timedelta
 
MODEL_PRICES = {
    <span class="cs">"claude-3-5-sonnet-20241022"</span>: (<span class="cv">3.0</span>/<span class="cv">1e6</span>, <span class="cv">15.0</span>/<span class="cv">1e6</span>),
    <span class="cs">"claude-3-haiku-20240307"</span>:    (<span class="cv">0.25</span>/<span class="cv">1e6</span>, <span class="cv">1.25</span>/<span class="cv">1e6</span>),
    <span class="cs">"gpt-4o"</span>:                     (<span class="cv">2.5</span>/<span class="cv">1e6</span>, <span class="cv">10.0</span>/<span class="cv">1e6</span>),
}
 
def init_cost_db():
    with sqlite3.connect(<span class="cs">"costs.db"</span>) as conn:
        conn.execute(<span class="cs">"""CREATE TABLE IF NOT EXISTS llm_calls (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            ts          TEXT NOT NULL,
            model       TEXT NOT NULL,
            endpoint    TEXT NOT NULL,
            user_id     TEXT NOT NULL,
            input_tok   INTEGER, output_tok INTEGER,
            cost_usd    REAL,
            latency_ms  REAL,
            cached      INTEGER DEFAULT 0)"""</span>)
        conn.executescript(<span class="cs">"""
            CREATE INDEX IF NOT EXISTS idx_ts      ON llm_calls(ts);
            CREATE INDEX IF NOT EXISTS idx_user    ON llm_calls(user_id);
            CREATE INDEX IF NOT EXISTS idx_model   ON llm_calls(model);
        """</span>)
 
def log_llm_call(model: str, endpoint: str, user_id: str,
                 input_tok: int, output_tok: int, latency_ms: float,
                 cached: bool = <span class="cv">False</span>):
    p_in, p_out = MODEL_PRICES.get(model, (<span class="cv">3e-6</span>, <span class="cv">15e-6</span>))
    cost = input_tok * p_in + output_tok * p_out
    with sqlite3.connect(<span class="cs">"costs.db"</span>) as conn:
        conn.execute(<span class="cs">"""INSERT INTO llm_calls
            (ts,model,endpoint,user_id,input_tok,output_tok,cost_usd,latency_ms,cached)
            VALUES (?,?,?,?,?,?,?,?,?)"""</span>,
            (datetime.utcnow().isoformat(), model, endpoint, user_id,
             input_tok, output_tok, cost, latency_ms, int(cached)))
 
<span class="ck"># ── Reporting queries ─────────────────────────────────</span>
def cost_report(days: int = <span class="cv">30</span>) -> dict:
    cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()
    with sqlite3.connect(<span class="cs">"costs.db"</span>) as conn:
        total = conn.execute(
            <span class="cs">"SELECT SUM(cost_usd), SUM(input_tok+output_tok), COUNT(*) FROM llm_calls WHERE ts>?"</span>,
            (cutoff,)).fetchone()
        by_model = conn.execute(
            <span class="cs">"SELECT model, SUM(cost_usd), COUNT(*) FROM llm_calls WHERE ts>? GROUP BY model ORDER BY SUM(cost_usd) DESC"</span>,
            (cutoff,)).fetchall()
        by_user = conn.execute(
            <span class="cs">"SELECT user_id, SUM(cost_usd) FROM llm_calls WHERE ts>? GROUP BY user_id ORDER BY SUM(cost_usd) DESC LIMIT 10"</span>,
            (cutoff,)).fetchall()
        cache_savings = conn.execute(
            <span class="cs">"SELECT SUM(cost_usd) FROM llm_calls WHERE ts>? AND cached=1"</span>,
            (cutoff,)).fetchone()[<span class="cv">0</span>] or <span class="cv">0</span>
    return {
        <span class="cs">"period_days"</span>:    days,
        <span class="cs">"total_usd"</span>:      round(total[<span class="cv">0</span>] or <span class="cv">0</span>, <span class="cv">4</span>),
        <span class="cs">"total_tokens"</span>:   total[<span class="cv">1</span>] or <span class="cv">0</span>,
        <span class="cs">"total_calls"</span>:    total[<span class="cv">2</span>] or <span class="cv">0</span>,
        <span class="cs">"cache_savings"</span>:  round(cache_savings, <span class="cv">4</span>),
        <span class="cs">"by_model"</span>:       [{<span class="cs">"model"</span>: r[<span class="cv">0</span>], <span class="cs">"cost"</span>: round(r[<span class="cv">1</span>], <span class="cv">4</span>), <span class="cs">"calls"</span>: r[<span class="cv">2</span>]} for r in by_model],
        <span class="cs">"top_users"</span>:      [{<span class="cs">"user_id"</span>: r[<span class="cv">0</span>], <span class="cs">"cost"</span>: round(r[<span class="cv">1</span>], <span class="cv">4</span>)} for r in by_user],
    }</pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- TAB 4 — RESPONSE CACHING -->
<div id="t4" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Response Caching — Eliminate Redundant API Calls</h3><span class="tag tag-navy">Cost + Speed</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import redis, hashlib, json
from typing import Optional
 
r = redis.Redis(host=<span class="cs">"localhost"</span>, port=<span class="cv">6379</span>, decode_responses=<span class="cv">True</span>)
 
<span class="ck"># ── Exact match cache ─────────────────────────────────</span>
<span class="ck"># Same prompt + same system → same deterministic response</span>
<span class="ck"># Only valid for temperature=0 calls</span>
 
def cache_key(system: str, messages: list, model: str) -> str:
    payload = json.dumps({<span class="cs">"system"</span>: system, <span class="cs">"messages"</span>: messages,
                          <span class="cs">"model"</span>: model}, sort_keys=<span class="cv">True</span>)
    return <span class="cs">f"llm:resp:{hashlib.md5(payload.encode()).hexdigest()}"</span>
 
def get_cached(system: str, messages: list, model: str,
               ttl_seconds: int = <span class="cv">3600</span>) -> Optional[str]:
    """Check cache. Returns cached response or None."""
    key = cache_key(system, messages, model)
    return r.get(key)
 
def set_cached(system: str, messages: list, model: str,
               response: str, ttl_seconds: int = <span class="cv">3600</span>):
    key = cache_key(system, messages, model)
    r.setex(key, ttl_seconds, response)
 
async def cached_llm_call(system: str, messages: list,
                           model: str = <span class="cs">"claude-3-5-sonnet-20241022"</span>,
                           temperature: float = <span class="cv">0.0</span>) -> tuple[str, bool]:
    """Returns (response_text, was_cached)."""
    if temperature == <span class="cv">0.0</span>:   <span class="ck"># only cache deterministic calls</span>
        cached = get_cached(system, messages, model)
        if cached:
            return cached, <span class="cv">True</span>
 
    response = await llm_client.messages.create(
        model=model, max_tokens=<span class="cv">1024</span>, temperature=temperature,
        system=system, messages=messages
    )
    text = response.content[<span class="cv">0</span>].text
 
    if temperature == <span class="cv">0.0</span>:
        set_cached(system, messages, model, text)
 
    return text, <span class="cv">False</span>
<span class="ck"># ── Semantic cache — cache similar (not just identical) queries ──</span>
<span class="ck"># 1. Embed the query</span>
<span class="ck"># 2. Search cached embeddings for cosine similarity > threshold</span>
<span class="ck"># 3. Return cached response if similar enough</span>
 
import numpy as np
 
class SemanticCache:
    def __init__(self, similarity_threshold: float = <span class="cv">0.95</span>, ttl: int = <span class="cv">3600</span>):
        self.threshold = similarity_threshold
        self.ttl = ttl
        self._entries: list[dict] = []   <span class="ck"># in-prod: use vector DB</span>
 
    def _cosine_sim(self, a, b) -> float:
        a, b = np.array(a), np.array(b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + <span class="cv">1e-8</span>))
 
    def get(self, query_embedding: list[float]) -> Optional[str]:
        for entry in self._entries:
            sim = self._cosine_sim(query_embedding, entry[<span class="cs">"embedding"</span>])
            if sim >= self.threshold:
                return entry[<span class="cs">"response"</span>]
        return None
 
    def set(self, query_embedding: list[float], response: str):
        self._entries.append({<span class="cs">"embedding"</span>: query_embedding, <span class="cs">"response"</span>: response})</pre></div>
    <div class="ins"><p>💡 <strong>Cache hit rate is a key business metric.</strong> Even a 20% cache hit rate on RAG queries means 20% fewer LLM API calls — directly reducing cost and latency. Track cache_savings in your cost report (see Tab 3) to show the value of caching to stakeholders.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- TAB 5 — PROMPT CACHING -->
<div id="t5" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Anthropic Prompt Caching — 90% Cost Reduction</h3><span class="tag tag-navy">Provider Feature</span></div>
  <div class="cp-body">
    <p>Anthropic's prompt caching caches the KV computation for large system prompts and documents. When the same cached prefix is sent again within 5 minutes, you pay 90% less for those tokens.</p>
    <div class="cb"><pre>import anthropic
client = anthropic.Anthropic()
 
<span class="ck"># ── Cache a large system prompt ───────────────────────</span>
<span class="ck"># Use when: same large system prompt sent with every request</span>
response = client.messages.create(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    system=[{
        <span class="cs">"type"</span>: <span class="cs">"text"</span>,
        <span class="cs">"text"</span>: very_long_system_prompt,   <span class="ck"># must be > 1024 tokens for caching to apply</span>
        <span class="cs">"cache_control"</span>: {<span class="cs">"type"</span>: <span class="cs">"ephemeral"</span>}
    }],
    messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: user_question}]
)
 
<span class="ck"># First call: cache_creation_input_tokens = N (full price)</span>
<span class="ck"># Subsequent calls within 5 min: cache_read_input_tokens = N (10% price)</span>
print(<span class="cs">f"Cache write: {response.usage.cache_creation_input_tokens}"</span>)
print(<span class="cs">f"Cache read:  {response.usage.cache_read_input_tokens}"</span>)
 
<span class="ck"># ── Cache a large document for RAG ────────────────────</span>
<span class="ck"># Use when: same large document referenced in many queries</span>
response = client.messages.create(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    system=<span class="cs">"You are a document Q&A assistant."</span>,
    messages=[{
        <span class="cs">"role"</span>: <span class="cs">"user"</span>,
        <span class="cs">"content"</span>: [
            {<span class="cs">"type"</span>: <span class="cs">"text"</span>, <span class="cs">"text"</span>: <span class="cs">"Here is the DPDK programmer's guide:"</span>},
            {<span class="cs">"type"</span>: <span class="cs">"text"</span>, <span class="cs">"text"</span>: large_dpdk_document,
             <span class="cs">"cache_control"</span>: {<span class="cs">"type"</span>: <span class="cs">"ephemeral"</span>}},
            {<span class="cs">"type"</span>: <span class="cs">"text"</span>, <span class="cs">"text"</span>: user_question}
        ]
    }]
)
 
<span class="ck"># ── When prompt caching is worth it ───────────────────</span>
<span class="ck"># Break-even: cache_write_cost = 1.25× normal. Cache reads = 0.1× normal.</span>
<span class="ck"># Break-even after 2 cache reads. If a prompt is used 10+ times per 5 min → always worth it.</span>
<span class="ck">#</span>
<span class="ck"># Best use cases:</span>
<span class="ck"># - Long system prompts (>2k tokens) sent with every request</span>
<span class="ck"># - Large documents referenced in many RAG queries</span>
<span class="ck"># - Few-shot examples in prompts</span>
<span class="ck"># - Tool definitions for agents with many tools</span></pre></div>
  </div>
</div>
</div><!-- end t5 -->
<!-- TAB 6 — RESOURCES -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching" target="_blank" rel="noopener">Anthropic: Prompt Caching — docs.anthropic.com</a></td><td>Official guide on prompt caching. Covers supported models, cache lifetime, and pricing.</td></tr>
    <tr><td class="res-type">Tool</td><td><a href="https://github.com/promptfoo/promptfoo" target="_blank" rel="noopener">Promptfoo — github.com/promptfoo/promptfoo</a></td><td>Open-source prompt testing framework. CI/CD integration, regression tests, red-teaming.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://hamel.dev/blog/posts/prompt_versioning/" target="_blank" rel="noopener">Prompt Versioning in Production — hamel.dev</a></td><td>Battle-tested strategies for managing prompts in production ML systems.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://redis.io/docs/manual/keyspace-notifications/" target="_blank" rel="noopener">Redis TTL and Expiry — redis.io/docs</a></td><td>Redis TTL mechanics for response cache expiry and keyspace events.</td></tr>
  </tbody>
</table>
</div>
<!-- TAB 7 — PROJECTS -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span>
    <span class="proj-title">Prompt Management System + Cost Dashboard</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build a complete prompt management and cost monitoring system for your AI API.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>Prompt registry</strong> — SQLite-backed register, activate, rollback, history endpoints in FastAPI</li>
      <li><strong>Prompt regression tests</strong> — pytest suite: grounding test, context-use test, graceful-decline test</li>
      <li><strong>Cost logger</strong> — log every LLM call to costs.db with model, endpoint, user, tokens, cost</li>
      <li><strong>Cost report API</strong> — GET /admin/costs returns 30-day report: total, by model, top users, cache savings</li>
      <li><strong>Response cache</strong> — Redis-backed exact match for temperature=0 calls, 1-hour TTL</li>
      <li><strong>Prompt caching</strong> — apply cache_control to your RAG system prompt; log cache_read vs cache_write tokens</li>
    </ul>
    <p><strong>Skills:</strong> SQLite versioning, pytest fixtures, Redis caching, cost analytics, Anthropic prompt caching</p>
  </div>
</div>
</div>
<!-- TAB 8 — LABS -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Prompt Versioning Lifecycle</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Practise the full register → test → activate → monitor → rollback cycle.</p>
    <div class="lab-step"><div class="sn">1</div><div>Register your current RAG system prompt as v1. Activate it. Make a deliberate quality-degrading change (remove the "only answer from context" rule). Register as v2.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run your regression test suite on v2. Verify the grounding test fails (as expected — the change broke it).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Fix the prompt. Register v3. Verify all tests pass on v3. Activate v3.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify prompt_changed() returns False (DB matches file). Call list_prompt_history() and verify v1, v2, v3 are all recorded with their authors and timestamps.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Cost Report — Find Your Biggest Spend</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Instrument 100 real API calls and use the cost report to identify optimisation opportunities.</p>
    <div class="lab-step"><div class="sn">1</div><div>Add log_llm_call() to every LLM call in your M23 API. Run 100 test requests across all endpoints. Generate cost_report(days=1).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Answer from the report: Which model costs the most? Which endpoint uses the most tokens? Which user has the highest spend?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Identify 2 endpoints where you can switch to Haiku instead of Sonnet. Make the switch. Run another 100 requests. Compare the cost reports before and after. What is the % cost reduction?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add the response cache. Run the same 100 requests again. How many were served from cache? What is cache_savings in the report? What is the effective cost reduction including caching?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Prompt Caching — Measure the Savings</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Add Anthropic prompt caching and measure the real cost reduction.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take your RAG system prompt (make it long — add extensive instructions until it exceeds 1024 tokens). Log the cache_creation_input_tokens on the first call and cache_read_input_tokens on subsequent calls.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run 20 queries in rapid succession (within 5 min). For each, print: cache_write, cache_read, total cost. Verify calls 2-20 show cache_read_input_tokens instead of cache_creation_input_tokens.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Calculate: cost without caching (20 × full system prompt cost) vs cost with caching (1 write + 19 reads). What is the % savings?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Wait 6 minutes (beyond the 5-min cache window). Send another request. Verify cache_creation_input_tokens is non-zero again (cache expired). Confirm caching is re-triggered.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- TAB 9 — CHECKLIST -->
<div id="t9" class="tab-pane">
<p class="sep">P7-M26 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Treat prompts as code: every production prompt is versioned, reviewed, and tested before activation</li>
  <li>Can implement a SQLite-backed prompt registry with register, activate, rollback, and history functions</li>
  <li>Can detect prompt drift: compare file hash to active DB version with prompt_changed()</li>
  <li>Can write at least 3 prompt regression tests: grounding, context-use, graceful-decline</li>
  <li>Know the deployment workflow: register → test → activate → monitor → rollback if needed</li>
  <li>Can log every LLM call to SQLite: model, endpoint, user_id, tokens, cost, cached flag</li>
  <li>Can generate a cost report broken down by model, endpoint, and top users</li>
  <li>Can implement Redis-backed exact match response cache for temperature=0 calls</li>
  <li>Know that semantic cache requires embedding similarity above a threshold (0.95 is a good starting point)</li>
  <li>Know that prompt caching requires >1024 tokens in the cached block to be eligible</li>
  <li>Can apply cache_control: ephemeral to system prompt and documents in Anthropic API calls</li>
  <li>Know to log cache_creation_input_tokens vs cache_read_input_tokens separately for cost tracking</li>
  <li>Know prompt caching TTL is 5 minutes — repeated calls must arrive within 5 min to hit the cache</li>
  <li>Completed Lab 1: prompt versioning lifecycle with regression test failure and fix</li>
  <li>Completed Lab 2: cost report analysis with model switching and caching impact</li>
  <li>Completed Lab 3: Anthropic prompt caching measured with savings calculation</li>
  <li>Milestone project: prompt management system + cost dashboard pushed to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P7-M27 — MLOps Foundations</strong>. The final Part 7 module covers CI/CD for AI, model versioning, and the operational patterns needed for long-running AI products.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part7-production/p7-m25-auth-logging/">← P7-M25: Auth &amp; Logging</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part7-production/p7-m27-mlops/">Next: P7-M27 — MLOps Foundations →</a>
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
    const key = 'p7m26-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
