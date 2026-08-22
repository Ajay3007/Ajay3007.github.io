---
title: "P5-M16 - Chunking & Document Ingestion"
description: "Part 5 — RAG Systems · Module 16 of 18 Chunking Document Ingestion How you split documents determines everything about retrieval quality — get this right ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part5-rag
order: 516
url: /learning/ai-ml/part5-rag/p5-m16-chunking/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#0a2040 40%,#065f46 70%,#059669 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#6ee7b7;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#d1fae5;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d1fae5}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1e14;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#6ee7b7;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#34d399;border-bottom-color:#34d399}
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
.p-green .cp-hdr{background:#d1fae5}[data-theme=dark] .p-green .cp-hdr{background:#064e3b}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.p-emerald .cp-hdr{background:#ecfdf5}[data-theme=dark] .p-emerald .cp-hdr{background:#064e3b}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#a7f3d0;color:#065f46}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}.tag-emerald{background:#6ee7b7;color:#065f46}
.cb{background:#0a1e14;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #059669}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#d1fae5;white-space:pre}
.cm{color:#4ade80}.ck{color:#6ee7b7}.cv{color:#f0c080}.cs{color:#34d399}
.ins{background:#ecfdf5;border:1.5px solid #059669;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#064e3b;border-color:#059669}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#065f46}[data-theme=dark] .ins strong{color:#34d399}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.wk-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
.wk-table th{background:#0a2040;color:#d1fae5;padding:.7rem 1rem;text-align:left;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}
.wk-table td{padding:.65rem 1rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.6}
.wk-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.wk-num{font-family:monospace;font-weight:700;color:#059669;white-space:nowrap}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#059669;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#0a2040;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#059669;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#d1fae5;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#059669;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#059669}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#059669;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #059669;transition:all .15s}
.mod-nav a:hover{background:#059669;color:#fff}
.mod-nav .nb{background:#059669;color:#fff}
.mod-nav .nb:hover{background:#047857;border-color:#047857}
.proj-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#15803d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#15803d}
/* chunk visualiser */
.chunk-demo{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:8px;padding:1rem;margin:.8rem 0;font-size:.84rem;line-height:1.7}
.chunk-demo .text{color:var(--text-color,#333)}
.chunk-hl{border-radius:3px;padding:1px 2px}
.c1{background:#d1fae5;border-bottom:2px solid #059669}
.c2{background:#dbeafe;border-bottom:2px solid #3b82f6}
.c3{background:#fef9c3;border-bottom:2px solid #ca8a04}
.overlap{background:#fde8d8;border-bottom:2px solid #ea580c}
.chunk-legend{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:.5rem;font-size:.75rem}
.cl-item{display:flex;align-items:center;gap:.3rem}
.cl-dot{width:12px;height:12px;border-radius:2px}
/* strategy cards */
.strategy-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.8rem;margin:.8rem 0}
.sc{border-radius:10px;padding:1rem 1.1rem;border:1.5px solid}
.sc h4{font-size:.9rem;font-weight:700;margin:.0 0 .4rem;border:none}
.sc p{font-size:.82rem;line-height:1.6;margin:0;color:var(--text-color,#444)}
.sc .when{font-size:.75rem;font-family:monospace;margin-top:.5rem;font-weight:600}
.sc-fixed{background:#ecfdf5;border-color:#6ee7b7}.sc-fixed h4{color:#065f46}.sc-fixed .when{color:#059669}
.sc-recursive{background:#eef2ff;border-color:#818cf8}.sc-recursive h4{color:#3730a3}.sc-recursive .when{color:#4f46e5}
.sc-semantic{background:#fdf4dc;border-color:#fcd34d}.sc-semantic h4{color:#92400e}.sc-semantic .when{color:#b45309}
.sc-document{background:#faeee4;border-color:#fdba74}.sc-document h4{color:#9a3412}.sc-document .when{color:#ea580c}
.sc-agentic{background:#ede8f5;border-color:#c4b5fd}.sc-agentic h4{color:#5b21b6}.sc-agentic .when{color:#7c3aed}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 5 — RAG Systems &nbsp;·&nbsp; Module 16 of 18</div>
  <div class="mod-title">Chunking &amp; Document Ingestion</div>
  <div class="mod-subtitle">How you split documents determines everything about retrieval quality — get this right</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 LangChain · Unstructured · PyMuPDF</span>
    <span class="mod-pill">📋 Prerequisite: P5-M15</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">✂️ Chunking Strategies</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔧 LangChain Splitters</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📄 Document Loaders</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🏷 Metadata & Enrichment</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔄 Ingestion Pipeline</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-emerald">RAG Layer 2</span></div>
  <div class="cp-body">
    <p>Chunking is the most underestimated part of RAG. A beautiful embedding model and fast vector DB will still produce terrible retrieval if your chunks are poorly designed. Chunks that are too large dilute the embedding signal. Chunks that are too small lose context. Chunks that break sentences mid-way confuse the LLM. This module teaches you to get it right.</p>
    <ul>
      <li><strong>Chunking strategies</strong> — fixed-size, recursive, semantic, document-aware, agentic — when each is appropriate</li>
      <li><strong>Overlap</strong> — why you need it and how much to use</li>
      <li><strong>LangChain text splitters</strong> — the standard toolkit for chunking</li>
      <li><strong>Document loaders</strong> — extracting clean text from PDF, DOCX, HTML, Markdown, code</li>
      <li><strong>Metadata enrichment</strong> — adding source, page, section, headings to every chunk for better filtering</li>
      <li><strong>Full ingestion pipeline</strong> — load → clean → chunk → embed → store, as a reusable class</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧠</span><h3>Why Chunking Quality Determines RAG Quality</h3><span class="tag tag-blue">Motivation</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># The chunking problem:</span>
<span class="ck">#</span>
<span class="ck"># DOCUMENT: 10,000 token technical manual about DPDK</span>
<span class="ck">#</span>
<span class="ck"># BAD: chunk = entire document</span>
<span class="ck"># → embedding averages over everything → signal diluted</span>
<span class="ck"># → 10,000 tokens fills context → too expensive</span>
<span class="ck">#</span>
<span class="ck"># BAD: chunk = 20 tokens (half a sentence)</span>
<span class="ck"># → embedding has no context → meaningless</span>
<span class="ck"># → "The ring buffer" has no meaning without surrounding text</span>
<span class="ck">#</span>
<span class="ck"># GOOD: chunk = 300-500 tokens (2-4 paragraphs on one topic)</span>
<span class="ck"># → embedding captures a complete idea</span>
<span class="ck"># → LLM gets enough context to answer</span>
<span class="ck"># → small enough for high precision retrieval</span>

<span class="ck"># The overlap problem:</span>
<span class="ck"># Without overlap — answers that span chunk boundaries are lost</span>
<span class="ck"># "The mempool must be... [CHUNK BOUNDARY] ...initialised before the port"</span>
<span class="ck"># → Neither chunk contains the complete fact</span>
<span class="ck">#</span>
<span class="ck"># With 10-20% overlap — boundary-spanning content appears in both chunks</span>
<span class="ck"># → At least one chunk retrieved will contain the complete answer</span></pre></div>
  </div>
</div>

</div><!-- end t0 -->


<!-- ══════════ TAB 1 — CHUNKING STRATEGIES ══════════ -->
<div id="t1" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>The Five Chunking Strategies</h3><span class="tag tag-emerald">Decision Framework</span></div>
  <div class="cp-body">
    <div class="strategy-grid">
      <div class="sc sc-fixed">
        <h4>Fixed-Size</h4>
        <p>Split by token or character count, regardless of content structure. Simple and predictable.</p>
        <div class="when">✓ Use when: quick prototype, uniform content, no structure</div>
      </div>
      <div class="sc sc-recursive">
        <h4>Recursive</h4>
        <p>Try to split on paragraph breaks, then sentences, then words — preserves natural boundaries when possible.</p>
        <div class="when">✓ Use when: general text — best default strategy</div>
      </div>
      <div class="sc sc-semantic">
        <h4>Semantic</h4>
        <p>Measure embedding similarity between consecutive sentences — split where similarity drops (topic change).</p>
        <div class="when">✓ Use when: high quality required, varied content</div>
      </div>
      <div class="sc sc-document">
        <h4>Document-Aware</h4>
        <p>Split on structural markers: headings in Markdown, sections in code, HTML tags, PDF pages.</p>
        <div class="when">✓ Use when: structured documents (docs, code, PDFs)</div>
      </div>
      <div class="sc sc-agentic">
        <h4>Agentic</h4>
        <p>LLM decides how to chunk — generates chunk boundaries and summaries. Highest quality, highest cost.</p>
        <div class="when">✓ Use when: critical domain, small corpus, max quality</div>
      </div>
    </div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Chunk Size Guidelines</h3><span class="tag tag-blue">Calibration</span></div>
  <div class="cp-body">
    <table style="width:100%;border-collapse:collapse;font-size:.84rem;margin:.8rem 0">
      <thead><tr style="background:#0a2040;color:#d1fae5"><th style="padding:.55rem .8rem;text-align:left">Chunk Size</th><th style="padding:.55rem .8rem">Tokens (approx)</th><th style="padding:.55rem .8rem">Best For</th><th style="padding:.55rem .8rem">Risk</th></tr></thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem">Tiny</td><td style="padding:.55rem .8rem">50–100</td><td style="padding:.55rem .8rem">Keyword-heavy fact retrieval</td><td style="padding:.55rem .8rem">No context — LLM gets fragments</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>Small ✓</strong></td><td style="padding:.55rem .8rem">200–400</td><td style="padding:.55rem .8rem">Q&amp;A, facts, customer support</td><td style="padding:.55rem .8rem">May miss multi-paragraph answers</td></tr>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>Medium ✓</strong></td><td style="padding:.55rem .8rem">400–800</td><td style="padding:.55rem .8rem">Technical docs, general RAG</td><td style="padding:.55rem .8rem">Good default — balanced precision/recall</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem">Large</td><td style="padding:.55rem .8rem">800–1500</td><td style="padding:.55rem .8rem">Long-form summaries, analysis</td><td style="padding:.55rem .8rem">Embedding signal diluted, slow search</td></tr>
        <tr><td style="padding:.55rem .8rem">Whole doc</td><td style="padding:.55rem .8rem">&gt;1500</td><td style="padding:.55rem .8rem">Do not use for RAG</td><td style="padding:.55rem .8rem">Precision collapse — everything matches</td></tr>
      </tbody>
    </table>
    <div class="ins"><p>💡 <strong>The golden rule: the chunk should be the smallest unit that can fully answer a likely query.</strong> If users ask "What is the DPDK mempool?" — the chunk should contain the complete mempool explanation, not just one sentence about it. Test empirically: try chunk sizes 256, 512, 1024 and measure retrieval precision on real queries.</p></div>
    <h4>Overlap — How Much?</h4>
    <div class="cb"><pre><span class="ck"># Overlap = how many tokens repeat between adjacent chunks</span>
<span class="ck"># Rule of thumb: 10–20% of chunk size</span>

chunk_size = <span class="cv">500</span>   <span class="ck"># tokens</span>
overlap    = <span class="cv">50</span>    <span class="ck"># tokens — 10% overlap</span>

<span class="ck"># Chunk 1: tokens 0-500</span>
<span class="ck"># Chunk 2: tokens 450-950  (50 token overlap)</span>
<span class="ck"># Chunk 3: tokens 900-1400 (50 token overlap)</span>

<span class="ck"># Too little overlap (0): boundary-spanning answers lost</span>
<span class="ck"># Too much overlap (50%): doubles storage, slows indexing, redundant retrieval</span>
<span class="ck"># Sweet spot: 50-100 tokens for chunk_size=500</span></pre></div>

    <div class="chunk-demo">
      <div style="font-size:.75rem;font-family:monospace;font-weight:700;color:#065f46;margin-bottom:.5rem">OVERLAP VISUALISATION (chunk_size=10 words, overlap=3 words)</div>
      <div class="text">
        <span class="chunk-hl c1">The ring buffer in DPDK stores packets</span> <span class="chunk-hl overlap c1 c2">waiting to be processed</span> <span class="chunk-hl c2">by the worker lcores. Each lcore</span> <span class="chunk-hl overlap c2 c3">reads from its dedicated</span> <span class="chunk-hl c3">queue without locking overhead.</span>
      </div>
      <div class="chunk-legend">
        <div class="cl-item"><div class="cl-dot" style="background:#d1fae5;border:2px solid #059669"></div> Chunk 1</div>
        <div class="cl-item"><div class="cl-dot" style="background:#dbeafe;border:2px solid #3b82f6"></div> Chunk 2</div>
        <div class="cl-item"><div class="cl-dot" style="background:#fef9c3;border:2px solid #ca8a04"></div> Chunk 3</div>
        <div class="cl-item"><div class="cl-dot" style="background:#fde8d8;border:2px solid #ea580c"></div> Overlap (repeated)</div>
      </div>
    </div>
  </div>
</div>

</div><!-- end t1 -->


<!-- ══════════ TAB 2 — LANGCHAIN SPLITTERS ══════════ -->
<div id="t2" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>LangChain Text Splitters — The Standard Toolkit</h3><span class="tag tag-emerald">Production Tools</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install langchain langchain-text-splitters tiktoken

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    MarkdownHeaderTextSplitter,
    PythonCodeTextSplitter,
    TokenTextSplitter,
)

<span class="ck"># ── 1. RecursiveCharacterTextSplitter — your default ──</span>
<span class="ck"># Tries to split on: \n\n, \n, " ", "" in that order</span>
<span class="ck"># Produces naturally bounded chunks (paragraphs, then sentences)</span>
splitter = RecursiveCharacterTextSplitter(
    chunk_size=<span class="cv">500</span>,       <span class="ck"># max characters per chunk</span>
    chunk_overlap=<span class="cv">50</span>,    <span class="ck"># characters of overlap</span>
    length_function=len,  <span class="ck"># use len(str) — swap for token counter</span>
    separators=[<span class="cs">"\n\n"</span>, <span class="cs">"\n"</span>, <span class="cs">" "</span>, <span class="cs">""</span>]   <span class="ck"># priority order</span>
)
chunks = splitter.split_text(long_text)
print(<span class="cs">f"{len(chunks)} chunks, avg length: {sum(len(c) for c in chunks)//len(chunks)}"</span>)

<span class="ck"># ── 2. Token-based splitting (recommended for LLM context) ──</span>
<span class="ck"># Characters are misleading — tokens are what the LLM actually counts</span>
splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name=<span class="cs">"gpt-4"</span>,    <span class="ck"># tokeniser to use</span>
    chunk_size=<span class="cv">400</span>,        <span class="ck"># max TOKENS per chunk</span>
    chunk_overlap=<span class="cv">40</span>       <span class="ck"># TOKENS of overlap</span>
)
chunks = splitter.split_text(long_text)

<span class="ck"># ── 3. Document splitting — preserves metadata ───────</span>
from langchain_core.documents import Document

docs = [Document(page_content=text, metadata={<span class="cs">"source"</span>: <span class="cs">"dpdk_guide.pdf"</span>, <span class="cs">"page"</span>: <span class="cv">1</span>})]
split_docs = splitter.split_documents(docs)
<span class="ck"># Each chunk keeps metadata from parent document</span>
print(split_docs[<span class="cv">0</span>].metadata)   <span class="ck"># {"source": "dpdk_guide.pdf", "page": 1}</span></pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📑</span><h3>Structure-Aware Splitters</h3><span class="tag tag-blue">Document-Aware</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># ── Markdown — split on headers ───────────────────────</span>
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    (<span class="cs">"#"</span>,  <span class="cs">"h1"</span>),
    (<span class="cs">"##"</span>, <span class="cs">"h2"</span>),
    (<span class="cs">"###"</span>,<span class="cs">"h3"</span>),
]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_docs = md_splitter.split_text(markdown_text)
<span class="ck"># Each doc has metadata: {"h1": "DPDK Guide", "h2": "Memory Management"}</span>
<span class="ck"># This lets you filter by section during retrieval</span>

<span class="ck"># Then apply size-based splitting to large sections</span>
secondary_splitter = RecursiveCharacterTextSplitter(chunk_size=<span class="cv">500</span>, chunk_overlap=<span class="cv">50</span>)
final_chunks = secondary_splitter.split_documents(md_docs)

<span class="ck"># ── Python code — split on function/class boundaries ──</span>
python_splitter = PythonCodeTextSplitter(chunk_size=<span class="cv">1000</span>, chunk_overlap=<span class="cv">0</span>)
code_chunks = python_splitter.split_text(python_source_code)
<span class="ck"># Splits at: class def, def, comments, then fallback to character</span>

<span class="ck"># ── Custom separators for any format ──────────────────</span>
<span class="ck"># C/C++ code</span>
cpp_splitter = RecursiveCharacterTextSplitter(
    separators=[<span class="cs">"\n\n"</span>, <span class="cs">"\nvoid "</span>, <span class="cs">"\nstatic "</span>, <span class="cs">"\nint "</span>, <span class="cs">"\n"</span>, <span class="cs">" "</span>],
    chunk_size=<span class="cv">800</span>, chunk_overlap=<span class="cv">80</span>
)

<span class="ck"># RST documentation</span>
rst_splitter = RecursiveCharacterTextSplitter(
    separators=[<span class="cs">"\n\n\n"</span>, <span class="cs">"\n\n"</span>, <span class="cs">".. "</span>, <span class="cs">"\n"</span>],
    chunk_size=<span class="cv">500</span>, chunk_overlap=<span class="cv">50</span>
)</pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧠</span><h3>Semantic Chunking — Split on Topic Changes</h3><span class="tag tag-teal">Highest Quality</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install langchain-experimental

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

<span class="ck"># SemanticChunker splits where embedding similarity drops</span>
<span class="ck"># → natural topic boundaries, not arbitrary character counts</span>
embeddings = OpenAIEmbeddings(model=<span class="cs">"text-embedding-3-small"</span>)

semantic_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type=<span class="cs">"percentile"</span>,  <span class="ck"># "percentile" | "standard_deviation" | "interquartile"</span>
    breakpoint_threshold_amount=<span class="cv">95</span>           <span class="ck"># split where similarity drop is in top 5%</span>
)
chunks = semantic_splitter.split_text(long_text)

<span class="ck"># Trade-offs vs recursive:</span>
<span class="ck"># ✓ Better topical coherence — each chunk covers one idea</span>
<span class="ck"># ✓ Variable chunk sizes adapt to content</span>
<span class="ck"># ✗ 1 API embedding call per sentence — expensive for large docs</span>
<span class="ck"># ✗ Slower — not suitable for real-time ingestion</span>
<span class="ck"># ✓ Best for: high-value static corpora, legal/medical docs</span></pre></div>
    <div class="warn"><p>⚠️ <strong>Semantic chunking makes an embedding API call for every sentence.</strong> For a 100-page PDF (~5000 sentences), that is 5000 embedding calls before you even start indexing. Use it for small, high-value corpora where retrieval quality matters more than ingestion speed or cost.</p></div>
  </div>
</div>

</div><!-- end t2 -->


<!-- ══════════ TAB 3 — DOCUMENT LOADERS ══════════ -->
<div id="t3" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">📄</span><h3>Loading Documents — PDF, DOCX, HTML, Markdown</h3><span class="tag tag-emerald">Source Agnostic</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install pymupdf python-docx beautifulsoup4 unstructured

<span class="ck"># ── PDF — PyMuPDF (fastest, best quality) ────────────</span>
import fitz   <span class="ck"># PyMuPDF</span>

def load_pdf(path: str) -> list[dict]:
    """Load PDF, return list of {text, page, source} dicts."""
    doc = fitz.open(path)
    pages = []
    for page_num, page in enumerate(doc):
        text = page.get_text(<span class="cs">"text"</span>)   <span class="ck"># plain text extraction</span>
        if text.strip():              <span class="ck"># skip blank pages</span>
            pages.append({
                <span class="cs">"text"</span>:   text,
                <span class="cs">"page"</span>:   page_num + <span class="cv">1</span>,
                <span class="cs">"source"</span>: path
            })
    doc.close()
    return pages

<span class="ck"># ── DOCX ─────────────────────────────────────────────</span>
from docx import Document as DocxDocument

def load_docx(path: str) -> str:
    doc = DocxDocument(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return <span class="cs">"\n\n"</span>.join(paragraphs)

<span class="ck"># ── HTML ─────────────────────────────────────────────</span>
from bs4 import BeautifulSoup
import requests

def load_html(url: str) -> str:
    response = requests.get(url, timeout=<span class="cv">10</span>)
    soup = BeautifulSoup(response.text, <span class="cs">"html.parser"</span>)
    <span class="ck"># Remove noise elements</span>
    for tag in soup.find_all([<span class="cs">"script"</span>, <span class="cs">"style"</span>, <span class="cs">"nav"</span>, <span class="cs">"footer"</span>, <span class="cs">"header"</span>]):
        tag.decompose()
    return soup.get_text(separator=<span class="cs">"\n"</span>, strip=<span class="cv">True</span>)

<span class="ck"># ── Markdown ──────────────────────────────────────────</span>
from pathlib import Path

def load_markdown(path: str) -> str:
    return Path(path).read_text(encoding=<span class="cs">"utf-8"</span>)

<span class="ck"># ── Directory loader — batch ingest ───────────────────</span>
import os
from pathlib import Path

def load_directory(dir_path: str, extensions: list[str] = [<span class="cs">".txt"</span>, <span class="cs">".md"</span>, <span class="cs">".pdf"</span>]) -> list[dict]:
    docs = []
    for path in Path(dir_path).rglob(<span class="cs">"*"</span>):
        if path.suffix in extensions and path.is_file():
            try:
                if path.suffix == <span class="cs">".pdf"</span>:
                    for page in load_pdf(str(path)):
                        docs.append(page)
                else:
                    text = path.read_text(encoding=<span class="cs">"utf-8"</span>, errors=<span class="cs">"ignore"</span>)
                    docs.append({<span class="cs">"text"</span>: text, <span class="cs">"source"</span>: str(path)})
            except Exception as e:
                print(<span class="cs">f"Failed to load {path}: {e}"</span>)
    return docs</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧹</span><h3>Text Cleaning — Remove Noise Before Chunking</h3><span class="tag tag-blue">Quality Gate</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import re

def clean_text(text: str) -> str:
    """Clean extracted text before chunking."""
    <span class="ck"># Remove excessive whitespace</span>
    text = re.sub(r<span class="cs">'\s+'</span>, <span class="cs">' '</span>, text)           <span class="ck"># collapse spaces/tabs</span>
    text = re.sub(r<span class="cs">'\n{3,}'</span>, <span class="cs">'\n\n'</span>, text)     <span class="ck"># max 2 consecutive newlines</span>

    <span class="ck"># Remove PDF artefacts (page numbers, headers, footers)</span>
    text = re.sub(r<span class="cs">'\nPage \d+ of \d+\n'</span>, <span class="cs">'\n'</span>, text)
    text = re.sub(r<span class="cs">'\n\d+\n'</span>, <span class="cs">'\n'</span>, text)        <span class="ck"># standalone page numbers</span>

    <span class="ck"># Remove non-printable characters</span>
    text = re.sub(r<span class="cs">'[^\x20-\x7E\n]'</span>, <span class="cs">' '</span>, text)

    <span class="ck"># Remove URLs if not relevant</span>
    <span class="ck"># text = re.sub(r'https?://\S+', '', text)</span>

    return text.strip()

def is_noise_chunk(chunk: str, min_words: int = <span class="cv">10</span>) -> bool:
    """Return True if the chunk is too short or mostly noise to be useful."""
    words = chunk.split()
    if len(words) < min_words:
        return <span class="cv">True</span>
    <span class="ck"># High ratio of non-alphabetic chars = likely table/figure noise</span>
    alpha_ratio = sum(<span class="cv">1</span> for c in chunk if c.isalpha()) / max(len(chunk), <span class="cv">1</span>)
    if alpha_ratio < <span class="cv">0.4</span>:
        return <span class="cv">True</span>
    return <span class="cv">False</span>

<span class="ck"># Filter after chunking</span>
chunks = [c for c in raw_chunks if not is_noise_chunk(c)]</pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Unstructured — Universal Document Parser</h3><span class="tag tag-teal">Production Grade</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install unstructured[all-docs]

from unstructured.partition.auto import partition
from unstructured.chunking.title import chunk_by_title

<span class="ck"># Auto-detect format and extract elements</span>
<span class="ck"># Works for: PDF, DOCX, HTML, PPTX, XLSX, EML, images (with OCR)</span>
elements = partition(filename=<span class="cs">"document.pdf"</span>)

<span class="ck"># Each element has a type and metadata</span>
for elem in elements[:5]:
    print(f<span class="cs">"{elem.category:15} | {str(elem)[:60]}"</span>)
<span class="ck"># Title           | DPDK Programmer's Guide</span>
<span class="ck"># NarrativeText   | This guide explains the Data Plane Development Kit</span>
<span class="ck"># Table           | | Feature | Status | Notes |</span>
<span class="ck"># Image           | [Image: figure1.png]</span>

<span class="ck"># Chunk by section title — respects document structure</span>
chunks = chunk_by_title(
    elements,
    max_characters=<span class="cv">1500</span>,
    new_after_n_chars=<span class="cv">800</span>,
    combine_text_under_n_chars=<span class="cv">200</span>
)

<span class="ck"># Convert to dicts for ingestion</span>
for chunk in chunks:
    text = str(chunk)
    meta = chunk.metadata.to_dict()
    <span class="ck"># meta contains: filename, page_number, url, coordinates, etc.</span></pre></div>
    <div class="ins"><p>💡 <strong>Use Unstructured when document quality matters more than speed.</strong> It extracts tables as structured data, ignores headers/footers intelligently, handles multi-column PDFs, and preserves heading hierarchy. The free version handles most formats; the hosted API handles scanned PDFs with OCR.</p></div>
  </div>
</div>

</div><!-- end t3 -->


<!-- ══════════ TAB 4 — METADATA & ENRICHMENT ══════════ -->
<div id="t4" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🏷</span><h3>Metadata — The Secret Weapon of Good RAG</h3><span class="tag tag-emerald">Often Neglected</span></div>
  <div class="cp-body">
    <p>Every chunk should carry rich metadata. Metadata enables filtering (only search recent docs), post-retrieval validation (show source), and attribution (cite the page). The chunks stored in your vector DB are only as useful as their metadata.</p>
    <div class="cb"><pre><span class="ck"># Minimum metadata per chunk</span>
chunk_metadata = {
    <span class="cs">"source"</span>:      <span class="cs">"dpdk-programmers-guide-v23.pdf"</span>,
    <span class="cs">"source_type"</span>: <span class="cs">"pdf"</span>,             <span class="ck"># pdf | html | docx | md | code</span>
    <span class="cs">"chunk_idx"</span>:   <span class="cv">42</span>,                <span class="ck"># position in document</span>
    <span class="cs">"char_count"</span>:  <span class="cv">487</span>,
}

<span class="ck"># Good metadata per chunk (for serious RAG)</span>
chunk_metadata = {
    <span class="cs">"source"</span>:      <span class="cs">"dpdk-programmers-guide-v23.pdf"</span>,
    <span class="cs">"source_type"</span>: <span class="cs">"pdf"</span>,
    <span class="cs">"page"</span>:        <span class="cv">47</span>,
    <span class="cs">"section"</span>:     <span class="cs">"Memory Management"</span>,
    <span class="cs">"subsection"</span>:  <span class="cs">"Mempool Library"</span>,
    <span class="cs">"chunk_idx"</span>:   <span class="cv">42</span>,
    <span class="cs">"total_chunks"</span>: <span class="cv">380</span>,
    <span class="cs">"ingested_at"</span>: <span class="cs">"2024-03-15T10:30:00Z"</span>,
    <span class="cs">"doc_version"</span>: <span class="cs">"23.11"</span>,
    <span class="cs">"language"</span>:    <span class="cs">"en"</span>,
    <span class="cs">"token_count"</span>: <span class="cv">412</span>,
}

<span class="ck"># For web content</span>
web_chunk_metadata = {
    <span class="cs">"url"</span>:         <span class="cs">"https://doc.dpdk.org/guides/prog_guide/mempool_lib.html"</span>,
    <span class="cs">"title"</span>:       <span class="cs">"Mempool Library — DPDK documentation"</span>,
    <span class="cs">"scraped_at"</span>:  <span class="cs">"2024-03-15"</span>,
    <span class="cs">"domain"</span>:      <span class="cs">"doc.dpdk.org"</span>,
    <span class="cs">"section"</span>:     <span class="cs">"Programmer's Guide"</span>,
}</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">✨</span><h3>Contextual Retrieval — LLM-Generated Chunk Summaries</h3><span class="tag tag-blue">Anthropic Technique</span></div>
  <div class="cp-body">
    <p>Anthropic published a technique (2024) that dramatically improves retrieval: before embedding each chunk, prepend a short LLM-generated summary that situates the chunk within the full document. This gives the embedding model more context to work with.</p>
    <div class="cb"><pre><span class="ck"># Contextual Retrieval — add document context to each chunk before embedding</span>
<span class="ck"># Cost: 1 cheap LLM call per chunk (use Haiku). Quality gain: significant.</span>

CONTEXT_PROMPT = <span class="cs">"""&lt;document&gt;
{full_document}
&lt;/document&gt;

The chunk below is part of this document. Write a short 1-2 sentence
context that situates this chunk within the document. Focus on what
section this is from and what concept it explains.

&lt;chunk&gt;
{chunk}
&lt;/chunk&gt;

Context:"""</span>

async def add_context(chunk: str, full_doc: str) -> str:
    """Prepend LLM-generated context to chunk before embedding."""
    response = await haiku_client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,   <span class="ck"># cheap fast model</span>
        max_tokens=<span class="cv">100</span>,
        messages=[{
            <span class="cs">"role"</span>: <span class="cs">"user"</span>,
            <span class="cs">"content"</span>: CONTEXT_PROMPT.format(full_document=full_doc[:3000], chunk=chunk)
        }]
    )
    context = response.content[<span class="cv">0</span>].text.strip()
    return <span class="cs">f"{context}\n\n{chunk}"</span>   <span class="ck"># context-enriched chunk ready to embed</span>

<span class="ck"># Apply to all chunks before embedding</span>
async def enrich_chunks(chunks: list[str], full_doc: str) -> list[str]:
    return await asyncio.gather(*[add_context(c, full_doc) for c in chunks])</pre></div>
    <div class="ins"><p>💡 <strong>This technique is worth the cost.</strong> Anthropic reported 49% reduction in retrieval failures on their benchmarks. A chunk saying "This section covers DPDK mempool initialisation. The ring buffer..." retrieves far better than a bare chunk starting mid-explanation without context.</p></div>
  </div>
</div>

</div><!-- end t4 -->


<!-- ══════════ TAB 5 — INGESTION PIPELINE ══════════ -->
<div id="t5" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Complete Ingestion Pipeline — Production Class</h3><span class="tag tag-emerald">Reusable</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import asyncio, hashlib, json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class IngestionConfig:
    chunk_size:    int   = <span class="cv">500</span>
    chunk_overlap: int   = <span class="cv">50</span>
    min_chunk_len: int   = <span class="cv">100</span>     <span class="ck"># discard shorter chunks</span>
    embedding_model: str = <span class="cs">"text-embedding-3-small"</span>
    collection_name: str = <span class="cs">"documents"</span>
    chroma_path:    str  = <span class="cs">"./chroma_db"</span>
    add_context:    bool = <span class="cv">False</span>   <span class="ck"># enable LLM context enrichment</span>

class DocumentIngestionPipeline:
    def __init__(self, config: IngestionConfig = IngestionConfig()):
        self.config   = config
        self.splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name=<span class="cs">"gpt-4"</span>,
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
        )
        self.chroma   = chromadb.PersistentClient(path=config.chroma_path)
        self.ef       = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.environ[<span class="cs">"OPENAI_API_KEY"</span>],
            model_name=config.embedding_model
        )
        self.collection = self.chroma.get_or_create_collection(
            name=config.collection_name,
            embedding_function=self.ef,
            metadata={<span class="cs">"hnsw:space"</span>: <span class="cs">"cosine"</span>}
        )

    def _doc_id(self, text: str, meta: dict) -> str:
        """Stable ID based on content hash — prevents duplicate ingestion."""
        key = json.dumps({<span class="cs">"text"</span>: text, <span class="cs">"source"</span>: meta.get(<span class="cs">"source"</span>, <span class="cs">""</span>)})
        return hashlib.md5(key.encode()).hexdigest()

    def ingest_text(self, text: str, metadata: dict = {}) -> int:
        """Ingest a single text string. Returns number of chunks added."""
        <span class="ck"># Clean</span>
        text = clean_text(text)
        if not text.strip():
            return <span class="cv">0</span>

        <span class="ck"># Chunk</span>
        chunks = self.splitter.split_text(text)
        chunks = [c for c in chunks if len(c) >= self.config.min_chunk_len]

        if not chunks:
            return <span class="cv">0</span>

        <span class="ck"># Build IDs, documents, metadatas</span>
        ids, docs, metas = [], [], []
        for i, chunk in enumerate(chunks):
            chunk_meta = {
                **metadata,
                <span class="cs">"chunk_idx"</span>:    i,
                <span class="cs">"total_chunks"</span>: len(chunks),
                <span class="cs">"char_count"</span>:   len(chunk),
                <span class="cs">"ingested_at"</span>:  datetime.utcnow().isoformat(),
            }
            ids.append(self._doc_id(chunk, chunk_meta))
            docs.append(chunk)
            metas.append(chunk_meta)

        <span class="ck"># Add to ChromaDB (skips existing IDs automatically)</span>
        self.collection.upsert(ids=ids, documents=docs, metadatas=metas)
        return len(chunks)

    def ingest_file(self, path: str) -> int:
        """Auto-detect file type and ingest."""
        path = Path(path)
        meta = {<span class="cs">"source"</span>: str(path), <span class="cs">"filename"</span>: path.name}

        if path.suffix == <span class="cs">".pdf"</span>:
            total = <span class="cv">0</span>
            for page in load_pdf(str(path)):
                total += self.ingest_text(page[<span class="cs">"text"</span>], {**meta, <span class="cs">"page"</span>: page[<span class="cs">"page"</span>]})
            return total
        elif path.suffix == <span class="cs">".docx"</span>:
            text = load_docx(str(path))
        elif path.suffix in (<span class="cs">".md"</span>, <span class="cs">".txt"</span>):
            text = path.read_text(encoding=<span class="cs">"utf-8"</span>)
        else:
            raise ValueError(<span class="cs">f"Unsupported file type: {path.suffix}"</span>)

        return self.ingest_text(text, meta)

    def ingest_directory(self, dir_path: str) -> dict:
        """Ingest all supported files in a directory."""
        results = {<span class="cs">"files"</span>: <span class="cv">0</span>, <span class="cs">"chunks"</span>: <span class="cv">0</span>, <span class="cs">"errors"</span>: []}
        for path in Path(dir_path).rglob(<span class="cs">"*"</span>):
            if path.suffix in (<span class="cs">".pdf"</span>, <span class="cs">".docx"</span>, <span class="cs">".md"</span>, <span class="cs">".txt"</span>) and path.is_file():
                try:
                    n = self.ingest_file(str(path))
                    results[<span class="cs">"chunks"</span>] += n
                    results[<span class="cs">"files"</span>]  += <span class="cv">1</span>
                except Exception as e:
                    results[<span class="cs">"errors"</span>].append({<span class="cs">"file"</span>: str(path), <span class="cs">"error"</span>: str(e)})
        return results

    def query(self, text: str, n_results: int = <span class="cv">5</span>, where: dict = None) -> list[dict]:
        """Semantic search — returns list of {text, score, metadata}."""
        kwargs = {<span class="cs">"query_texts"</span>: [text], <span class="cs">"n_results"</span>: n_results,
                  <span class="cs">"include"</span>: [<span class="cs">"documents"</span>, <span class="cs">"distances"</span>, <span class="cs">"metadatas"</span>]}
        if where:
            kwargs[<span class="cs">"where"</span>] = where
        results = self.collection.query(**kwargs)
        return [
            {<span class="cs">"text"</span>: doc, <span class="cs">"score"</span>: <span class="cv">1</span> - dist, <span class="cs">"meta"</span>: meta}
            for doc, dist, meta in zip(
                results[<span class="cs">"documents"</span>][<span class="cv">0</span>],
                results[<span class="cs">"distances"</span>][<span class="cv">0</span>],
                results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>]
            )
        ]</pre></div>
  </div>
</div>

</div><!-- end t5 -->


<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://python.langchain.com/docs/concepts/text_splitters/" target="_blank" rel="noopener">LangChain Text Splitters — python.langchain.com/docs/concepts/text_splitters</a></td><td>Complete reference for all LangChain splitter types with code examples.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://www.anthropic.com/news/contextual-retrieval" target="_blank" rel="noopener">Anthropic: Contextual Retrieval — anthropic.com/news/contextual-retrieval</a></td><td>Anthropic's technique for LLM-enriched chunks. Shows 49% fewer retrieval failures.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://unstructured.io/blog/chunking-for-rag-best-practices" target="_blank" rel="noopener">Unstructured: Chunking for RAG Best Practices — unstructured.io/blog</a></td><td>Production-tested chunking strategies including chunk size, overlap, and structure awareness.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://weaviate.io/blog/chunking-strategies-for-rag" target="_blank" rel="noopener">Weaviate: Chunking Strategies for RAG — weaviate.io/blog</a></td><td>Covers fixed, recursive, and semantic chunking with visual diagrams.</td></tr>
    <tr><td class="res-type">Library</td><td><a href="https://docs.unstructured.io/" target="_blank" rel="noopener">Unstructured.io Docs — docs.unstructured.io</a></td><td>Universal document parser. Handles PDF, DOCX, HTML, PPTX with intelligent element extraction.</td></tr>
  </tbody>
</table>
</div><!-- end t6 -->


<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>

<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Document Ingestion Pipeline with Chunking Comparison</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build the reusable <code>DocumentIngestionPipeline</code> class and empirically compare three chunking strategies to understand when each is best.</p>
    <h4>Part A — Build the Pipeline</h4>
    <ul>
      <li>Implement the full <code>DocumentIngestionPipeline</code> class from Tab 5</li>
      <li>Support: PDF, DOCX, Markdown, plain text ingestion</li>
      <li>Embed with OpenAI text-embedding-3-small, store in ChromaDB</li>
      <li>Track: files ingested, chunks created, errors, total tokens used</li>
      <li>Ingest at least 20 real documents from any domain you care about</li>
    </ul>
    <h4>Part B — Compare Chunking Strategies</h4>
    <ul>
      <li>Take 3 long documents and chunk them three ways: fixed-size (500), recursive (500/50), semantic</li>
      <li>For each strategy, create a separate ChromaDB collection</li>
      <li>Write 10 test queries. For each query, check: (a) does the top-1 chunk contain the answer? (b) does the top-3 contain it? (c) is the returned chunk complete or does it cut off mid-sentence?</li>
      <li>Document which strategy works best and why for your document type</li>
    </ul>
    <p><strong>Skills:</strong> LangChain splitters, PyMuPDF, ChromaDB, batch embedding, metadata design, empirical evaluation</p>
  </div>
</div>
</div><!-- end t7 -->


<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Chunking Parameter Sensitivity — Find the Sweet Spot</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Discover how chunk size and overlap affect retrieval quality on your documents.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take a 20-page technical document (PDF or Markdown). Write 10 specific questions whose answers you can locate manually in the document. Record the page/section for each answer.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Chunk with 4 configurations and index each in a separate ChromaDB collection: (a) size=200, overlap=0, (b) size=500, overlap=0, (c) size=500, overlap=100, (d) size=1000, overlap=100.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>For each configuration, run all 10 questions and check if the answer appears in the top-3 retrieved chunks. Score: 1 point for top-1, 0.5 for top-2/3, 0 for not found.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Build a table: config | score/10 | avg chunk size | num chunks | query time. Which configuration wins? Is the winner different for short factual questions vs long explanatory questions?</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Key finding to document:</strong> what chunk size and overlap would you use for this document type in production?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Metadata Filtering — See the Quality Jump</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Demonstrate that metadata filtering dramatically improves precision when your collection has multiple sources.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a ChromaDB collection with chunks from 3 different domains: (a) DPDK/networking, (b) Python programming, (c) cooking recipes. At least 10 chunks per domain with "domain" metadata field.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run 5 queries relevant to each domain WITHOUT filtering. Record: how many of the top-5 results are from the correct domain?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Re-run the same 15 queries WITH domain filter (where={"domain": "dpdk"}). Record the same metric.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Compare precision@5: with vs without filtering. Document the improvement. This is the argument for rich metadata in production RAG.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Contextual Retrieval — Measure the Improvement</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement Anthropic's contextual retrieval technique and measure how much it improves retrieval.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take a 10-page document and chunk it into ~30 chunks with RecursiveCharacterTextSplitter.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Create <strong>Collection A</strong>: index the raw chunks as-is.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>For each chunk, call Claude Haiku to generate a 1-2 sentence context using the full document. Prepend the context to the chunk. Create <strong>Collection B</strong>: index the context-enriched chunks.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Write 10 test questions. For each, query both collections and check if the answer is in top-3. Score both.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Compare: Collection A score vs Collection B score. Also compare: total Haiku API cost for enrichment. Is the quality gain worth the cost for your use case?</div></div>
  </div>
</div>

</div><!-- end t8 -->


<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P5-M16 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain why chunk size critically affects retrieval quality — too large dilutes signal, too small loses context</li>
  <li>Know the 5 chunking strategies and when to use each: fixed, recursive, semantic, document-aware, agentic</li>
  <li>Can explain why overlap is needed and choose an appropriate overlap amount (10-20% of chunk size)</li>
  <li>Always use RecursiveCharacterTextSplitter as the default — never plain CharacterTextSplitter for prose</li>
  <li>Can use from_tiktoken_encoder() to split by tokens rather than characters</li>
  <li>Can use MarkdownHeaderTextSplitter to preserve section hierarchy as metadata</li>
  <li>Can implement semantic chunking and know when the cost is justified</li>
  <li>Can load clean text from PDF (PyMuPDF), DOCX, HTML, and Markdown</li>
  <li>Can clean extracted text: remove page numbers, excessive whitespace, non-printable characters</li>
  <li>Can filter noise chunks that are too short or low in alphabetic content</li>
  <li>Know what Unstructured.io does and when to use it over simple loaders</li>
  <li>Include rich metadata with every chunk: source, page, section, chunk_idx, ingested_at, token_count</li>
  <li>Can implement the Anthropic contextual retrieval technique and explain the quality tradeoff</li>
  <li>Can build a complete DocumentIngestionPipeline that handles load → clean → chunk → embed → store</li>
  <li>Use content-hash IDs (MD5) to prevent duplicate chunk ingestion</li>
  <li>Completed Lab 1: chunk size sensitivity experiment with scoring</li>
  <li>Completed Lab 2: metadata filtering precision comparison</li>
  <li>Completed Lab 3: contextual retrieval quality measurement</li>
  <li>Milestone project pushed to GitHub with README and chunking comparison findings</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P5-M17 — Retrieval Quality</strong>. You now have a solid ingestion pipeline. M17 covers how to improve what comes back from that pipeline: filtering, reranking with Cohere, HyDE, and diagnosing retrieval failures.</p>
</div>
</div><!-- end t9 -->


<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part5-rag/p5-m15-embeddings-vectordb/">← P5-M15: Embeddings &amp; Vector DBs</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part5-rag/p5-m17-retrieval-quality/">Next: P5-M17 — Retrieval Quality →</a>
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
    const key = 'p5m16-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
