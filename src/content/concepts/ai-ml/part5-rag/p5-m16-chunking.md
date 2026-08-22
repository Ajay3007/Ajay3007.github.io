---
title: "P5-M16 - Chunking & Document Ingestion"
description: "Part 5 — RAG Systems · Module 16 of 18 Chunking Document Ingestion How you split documents determines everything about retrieval quality — get this right ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part5-rag
order: 516
ownHeader: true
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
    

```python
# The chunking problem:
#
# DOCUMENT: 10,000 token technical manual about DPDK
#
# BAD: chunk = entire document
# → embedding averages over everything → signal diluted
# → 10,000 tokens fills context → too expensive
#
# BAD: chunk = 20 tokens (half a sentence)
# → embedding has no context → meaningless
# → "The ring buffer" has no meaning without surrounding text
#
# GOOD: chunk = 300-500 tokens (2-4 paragraphs on one topic)
# → embedding captures a complete idea
# → LLM gets enough context to answer
# → small enough for high precision retrieval

# The overlap problem:
# Without overlap — answers that span chunk boundaries are lost
# "The mempool must be... [CHUNK BOUNDARY] ...initialised before the port"
# → Neither chunk contains the complete fact
#
# With 10-20% overlap — boundary-spanning content appears in both chunks
# → At least one chunk retrieved will contain the complete answer
```


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
    

```bash
# Overlap = how many tokens repeat between adjacent chunks
# Rule of thumb: 10–20% of chunk size

chunk_size = 500   # tokens
overlap    = 50    # tokens — 10% overlap

# Chunk 1: tokens 0-500
# Chunk 2: tokens 450-950  (50 token overlap)
# Chunk 3: tokens 900-1400 (50 token overlap)

# Too little overlap (0): boundary-spanning answers lost
# Too much overlap (50%): doubles storage, slows indexing, redundant retrieval
# Sweet spot: 50-100 tokens for chunk_size=500
```



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
    

```python
pip install langchain langchain-text-splitters tiktoken

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    MarkdownHeaderTextSplitter,
    PythonCodeTextSplitter,
    TokenTextSplitter,
)

# ── 1. RecursiveCharacterTextSplitter — your default ──
# Tries to split on: \n\n, \n, " ", "" in that order
# Produces naturally bounded chunks (paragraphs, then sentences)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # max characters per chunk
    chunk_overlap=50,    # characters of overlap
    length_function=len,  # use len(str) — swap for token counter
    separators=["\n\n", "\n", " ", ""]   # priority order
)
chunks = splitter.split_text(long_text)
print(f"{len(chunks)} chunks, avg length: {sum(len(c) for c in chunks)//len(chunks)}")

# ── 2. Token-based splitting (recommended for LLM context) ──
# Characters are misleading — tokens are what the LLM actually counts
splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",    # tokeniser to use
    chunk_size=400,        # max TOKENS per chunk
    chunk_overlap=40       # TOKENS of overlap
)
chunks = splitter.split_text(long_text)

# ── 3. Document splitting — preserves metadata ───────
from langchain_core.documents import Document

docs = [Document(page_content=text, metadata={"source": "dpdk_guide.pdf", "page": 1})]
split_docs = splitter.split_documents(docs)
# Each chunk keeps metadata from parent document
print(split_docs[0].metadata)   # {"source": "dpdk_guide.pdf", "page": 1}
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📑</span><h3>Structure-Aware Splitters</h3><span class="tag tag-blue">Document-Aware</span></div>
  <div class="cp-body">
    

```python
# ── Markdown — split on headers ───────────────────────
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#",  "h1"),
    ("##", "h2"),
    ("###","h3"),
]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_docs = md_splitter.split_text(markdown_text)
# Each doc has metadata: {"h1": "DPDK Guide", "h2": "Memory Management"}
# This lets you filter by section during retrieval

# Then apply size-based splitting to large sections
secondary_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
final_chunks = secondary_splitter.split_documents(md_docs)

# ── Python code — split on function/class boundaries ──
python_splitter = PythonCodeTextSplitter(chunk_size=1000, chunk_overlap=0)
code_chunks = python_splitter.split_text(python_source_code)
# Splits at: class def, def, comments, then fallback to character

# ── Custom separators for any format ──────────────────
# C/C++ code
cpp_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\nvoid ", "\nstatic ", "\nint ", "\n", " "],
    chunk_size=800, chunk_overlap=80
)

# RST documentation
rst_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n\n", "\n\n", ".. ", "\n"],
    chunk_size=500, chunk_overlap=50
)
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧠</span><h3>Semantic Chunking — Split on Topic Changes</h3><span class="tag tag-teal">Highest Quality</span></div>
  <div class="cp-body">
    

```python
pip install langchain-experimental

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# SemanticChunker splits where embedding similarity drops
# → natural topic boundaries, not arbitrary character counts
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

semantic_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",  # "percentile" | "standard_deviation" | "interquartile"
    breakpoint_threshold_amount=95           # split where similarity drop is in top 5%
)
chunks = semantic_splitter.split_text(long_text)

# Trade-offs vs recursive:
# ✓ Better topical coherence — each chunk covers one idea
# ✓ Variable chunk sizes adapt to content
# ✗ 1 API embedding call per sentence — expensive for large docs
# ✗ Slower — not suitable for real-time ingestion
# ✓ Best for: high-value static corpora, legal/medical docs
```


<div class="warn"><p>⚠️ <strong>Semantic chunking makes an embedding API call for every sentence.</strong> For a 100-page PDF (~5000 sentences), that is 5000 embedding calls before you even start indexing. Use it for small, high-value corpora where retrieval quality matters more than ingestion speed or cost.</p></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — DOCUMENT LOADERS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">📄</span><h3>Loading Documents — PDF, DOCX, HTML, Markdown</h3><span class="tag tag-emerald">Source Agnostic</span></div>
  <div class="cp-body">
    

```python
pip install pymupdf python-docx beautifulsoup4 unstructured

# ── PDF — PyMuPDF (fastest, best quality) ────────────
import fitz   # PyMuPDF

def load_pdf(path: str) -> list[dict]:
    """Load PDF, return list of {text, page, source} dicts."""
    doc = fitz.open(path)
    pages = []
    for page_num, page in enumerate(doc):
        text = page.get_text("text")   # plain text extraction
        if text.strip():              # skip blank pages
            pages.append({
                "text":   text,
                "page":   page_num + 1,
                "source": path
            })
    doc.close()
    return pages

# ── DOCX ─────────────────────────────────────────────
from docx import Document as DocxDocument

def load_docx(path: str) -> str:
    doc = DocxDocument(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)

# ── HTML ─────────────────────────────────────────────
from bs4 import BeautifulSoup
import requests

def load_html(url: str) -> str:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    # Remove noise elements
    for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)

# ── Markdown ──────────────────────────────────────────
from pathlib import Path

def load_markdown(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

# ── Directory loader — batch ingest ───────────────────
import os
from pathlib import Path

def load_directory(dir_path: str, extensions: list[str] = [".txt", ".md", ".pdf"]) -> list[dict]:
    docs = []
    for path in Path(dir_path).rglob("*"):
        if path.suffix in extensions and path.is_file():
            try:
                if path.suffix == ".pdf":
                    for page in load_pdf(str(path)):
                        docs.append(page)
                else:
                    text = path.read_text(encoding="utf-8", errors="ignore")
                    docs.append({"text": text, "source": str(path)})
            except Exception as e:
                print(f"Failed to load {path}: {e}")
    return docs
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧹</span><h3>Text Cleaning — Remove Noise Before Chunking</h3><span class="tag tag-blue">Quality Gate</span></div>
  <div class="cp-body">
    

```python
import re

def clean_text(text: str) -> str:
    """Clean extracted text before chunking."""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)           # collapse spaces/tabs
    text = re.sub(r'\n{3,}', '\n\n', text)     # max 2 consecutive newlines

    # Remove PDF artefacts (page numbers, headers, footers)
    text = re.sub(r'\nPage \d+ of \d+\n', '\n', text)
    text = re.sub(r'\n\d+\n', '\n', text)        # standalone page numbers

    # Remove non-printable characters
    text = re.sub(r'[^\x20-\x7E\n]', ' ', text)

    # Remove URLs if not relevant
    # text = re.sub(r'https?://\S+', '', text)

    return text.strip()

def is_noise_chunk(chunk: str, min_words: int = 10) -> bool:
    """Return True if the chunk is too short or mostly noise to be useful."""
    words = chunk.split()
    if len(words) True
    # High ratio of non-alphabetic chars = likely table/figure noise
    alpha_ratio = sum(1 for c in chunk if c.isalpha()) / max(len(chunk), 1)
    if alpha_ratio 0.4:
        return True
    return False

# Filter after chunking
chunks = [c for c in raw_chunks if not is_noise_chunk(c)]
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Unstructured — Universal Document Parser</h3><span class="tag tag-teal">Production Grade</span></div>
  <div class="cp-body">
    

```python
pip install unstructured[all-docs]

from unstructured.partition.auto import partition
from unstructured.chunking.title import chunk_by_title

# Auto-detect format and extract elements
# Works for: PDF, DOCX, HTML, PPTX, XLSX, EML, images (with OCR)
elements = partition(filename="document.pdf")

# Each element has a type and metadata
for elem in elements[:5]:
    print(f"{elem.category:15} | {str(elem)[:60]}")
# Title           | DPDK Programmer's Guide
# NarrativeText   | This guide explains the Data Plane Development Kit
# Table           | | Feature | Status | Notes |
# Image           | [Image: figure1.png]

# Chunk by section title — respects document structure
chunks = chunk_by_title(
    elements,
    max_characters=1500,
    new_after_n_chars=800,
    combine_text_under_n_chars=200
)

# Convert to dicts for ingestion
for chunk in chunks:
    text = str(chunk)
    meta = chunk.metadata.to_dict()
    # meta contains: filename, page_number, url, coordinates, etc.
```


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
    

```python
# Minimum metadata per chunk
chunk_metadata = {
    "source":      "dpdk-programmers-guide-v23.pdf",
    "source_type": "pdf",             # pdf | html | docx | md | code
    "chunk_idx":   42,                # position in document
    "char_count":  487,
}

# Good metadata per chunk (for serious RAG)
chunk_metadata = {
    "source":      "dpdk-programmers-guide-v23.pdf",
    "source_type": "pdf",
    "page":        47,
    "section":     "Memory Management",
    "subsection":  "Mempool Library",
    "chunk_idx":   42,
    "total_chunks": 380,
    "ingested_at": "2024-03-15T10:30:00Z",
    "doc_version": "23.11",
    "language":    "en",
    "token_count": 412,
}

# For web content
web_chunk_metadata = {
    "url":         "https://doc.dpdk.org/guides/prog_guide/mempool_lib.html",
    "title":       "Mempool Library — DPDK documentation",
    "scraped_at":  "2024-03-15",
    "domain":      "doc.dpdk.org",
    "section":     "Programmer's Guide",
}
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">✨</span><h3>Contextual Retrieval — LLM-Generated Chunk Summaries</h3><span class="tag tag-blue">Anthropic Technique</span></div>
  <div class="cp-body">
<p>Anthropic published a technique (2024) that dramatically improves retrieval: before embedding each chunk, prepend a short LLM-generated summary that situates the chunk within the full document. This gives the embedding model more context to work with.</p>
    

```python
# Contextual Retrieval — add document context to each chunk before embedding
# Cost: 1 cheap LLM call per chunk (use Haiku). Quality gain: significant.

CONTEXT_PROMPT = """<document>
{full_document}
</document>

The chunk below is part of this document. Write a short 1-2 sentence
context that situates this chunk within the document. Focus on what
section this is from and what concept it explains.

<chunk>
{chunk}
</chunk>

Context:"""

async def add_context(chunk: str, full_doc: str) -> str:
    """Prepend LLM-generated context to chunk before embedding."""
    response = await haiku_client.messages.create(
        model="claude-3-haiku-20240307",   # cheap fast model
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": CONTEXT_PROMPT.format(full_document=full_doc[:3000], chunk=chunk)
        }]
    )
    context = response.content[0].text.strip()
    return f"{context}\n\n{chunk}"   # context-enriched chunk ready to embed

# Apply to all chunks before embedding
async def enrich_chunks(chunks: list[str], full_doc: str) -> list[str]:
    return await asyncio.gather(*[add_context(c, full_doc) for c in chunks])
```


<div class="ins"><p>💡 <strong>This technique is worth the cost.</strong> Anthropic reported 49% reduction in retrieval failures on their benchmarks. A chunk saying "This section covers DPDK mempool initialisation. The ring buffer..." retrieves far better than a bare chunk starting mid-explanation without context.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — INGESTION PIPELINE ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Complete Ingestion Pipeline — Production Class</h3><span class="tag tag-emerald">Reusable</span></div>
  <div class="cp-body">
    

```python
import asyncio, hashlib, json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class IngestionConfig:
    chunk_size:    int   = 500
    chunk_overlap: int   = 50
    min_chunk_len: int   = 100     # discard shorter chunks
    embedding_model: str = "text-embedding-3-small"
    collection_name: str = "documents"
    chroma_path:    str  = "./chroma_db"
    add_context:    bool = False   # enable LLM context enrichment

class DocumentIngestionPipeline:
    def __init__(self, config: IngestionConfig = IngestionConfig()):
        self.config   = config
        self.splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="gpt-4",
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
        )
        self.chroma   = chromadb.PersistentClient(path=config.chroma_path)
        self.ef       = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"],
            model_name=config.embedding_model
        )
        self.collection = self.chroma.get_or_create_collection(
            name=config.collection_name,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"}
        )

    def _doc_id(self, text: str, meta: dict) -> str:
        """Stable ID based on content hash — prevents duplicate ingestion."""
        key = json.dumps({"text": text, "source": meta.get("source", "")})
        return hashlib.md5(key.encode()).hexdigest()

    def ingest_text(self, text: str, metadata: dict = {}) -> int:
        """Ingest a single text string. Returns number of chunks added."""
        # Clean
        text = clean_text(text)
        if not text.strip():
            return 0

        # Chunk
        chunks = self.splitter.split_text(text)
        chunks = [c for c in chunks if len(c) >= self.config.min_chunk_len]

        if not chunks:
            return 0

        # Build IDs, documents, metadatas
        ids, docs, metas = [], [], []
        for i, chunk in enumerate(chunks):
            chunk_meta = {
                **metadata,
                "chunk_idx":    i,
                "total_chunks": len(chunks),
                "char_count":   len(chunk),
                "ingested_at":  datetime.utcnow().isoformat(),
            }
            ids.append(self._doc_id(chunk, chunk_meta))
            docs.append(chunk)
            metas.append(chunk_meta)

        # Add to ChromaDB (skips existing IDs automatically)
        self.collection.upsert(ids=ids, documents=docs, metadatas=metas)
        return len(chunks)

    def ingest_file(self, path: str) -> int:
        """Auto-detect file type and ingest."""
        path = Path(path)
        meta = {"source": str(path), "filename": path.name}

        if path.suffix == ".pdf":
            total = 0
            for page in load_pdf(str(path)):
                total += self.ingest_text(page["text"], {**meta, "page": page["page"]})
            return total
        elif path.suffix == ".docx":
            text = load_docx(str(path))
        elif path.suffix in (".md", ".txt"):
            text = path.read_text(encoding="utf-8")
        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")

        return self.ingest_text(text, meta)

    def ingest_directory(self, dir_path: str) -> dict:
        """Ingest all supported files in a directory."""
        results = {"files": 0, "chunks": 0, "errors": []}
        for path in Path(dir_path).rglob("*"):
            if path.suffix in (".pdf", ".docx", ".md", ".txt") and path.is_file():
                try:
                    n = self.ingest_file(str(path))
                    results["chunks"] += n
                    results["files"]  += 1
                except Exception as e:
                    results["errors"].append({"file": str(path), "error": str(e)})
        return results

    def query(self, text: str, n_results: int = 5, where: dict = None) -> list[dict]:
        """Semantic search — returns list of {text, score, metadata}."""
        kwargs = {"query_texts": [text], "n_results": n_results,
                  "include": ["documents", "distances", "metadatas"]}
        if where:
            kwargs["where"] = where
        results = self.collection.query(**kwargs)
        return [
            {"text": doc, "score": 1 - dist, "meta": meta}
            for doc, dist, meta in zip(
                results["documents"][0],
                results["distances"][0],
                results["metadatas"][0]
            )
        ]
```


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
