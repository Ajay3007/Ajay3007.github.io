---
title: "P5-M17 - Retrieval Quality"
description: "Part 5 — RAG Systems · Module 17 of 18 Retrieval Quality Filtering, reranking, query expansion and diagnosing why your RAG retrieval is failing ⏱ 1 Week 🟡 Intermediate 🔧…"
domain: ai-ml
track: ai-ml-engineering
module: part5-rag
order: 517
ownHeader: true
url: /learning/ai-ml/part5-rag/p5-m17-retrieval-quality/
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
.ck{color:#6ee7b7}.cv{color:#f0c080}.cs{color:#34d399}
.ins{background:#ecfdf5;border:1.5px solid #059669;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#064e3b;border-color:#059669}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#065f46}[data-theme=dark] .ins strong{color:#34d399}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
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
/* failure cards */
.failure-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:.8rem;margin:.8rem 0}
.fc{border-radius:10px;padding:1rem 1.1rem;border:1.5px solid}
.fc h4{font-size:.88rem;font-weight:700;margin:0 0 .4rem;border:none}
.fc p{font-size:.82rem;line-height:1.6;margin:0 0 .4rem;color:var(--text-color,#444)}
.fc .fix{font-size:.78rem;font-family:monospace;font-weight:600}
.fc-vocab{background:#faeaea;border-color:#fca5a5}.fc-vocab h4{color:#991b1b}.fc-vocab .fix{color:#15803d}
.fc-semantic{background:#faeee4;border-color:#fdba74}.fc-semantic h4{color:#9a3412}.fc-semantic .fix{color:#15803d}
.fc-chunk{background:#fdf4dc;border-color:#fcd34d}.fc-chunk h4{color:#92400e}.fc-chunk .fix{color:#15803d}
.fc-topk{background:#ede8f5;border-color:#c4b5fd}.fc-topk h4{color:#5b21b6}.fc-topk .fix{color:#15803d}
.fc-meta{background:#e0f2fe;border-color:#7dd3fc}.fc-meta h4{color:#0c4a6e}.fc-meta .fix{color:#15803d}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 5 — RAG Systems &nbsp;·&nbsp; Module 17 of 18</div>
  <div class="mod-title">Retrieval Quality</div>
  <div class="mod-subtitle">Filtering, reranking, query expansion and diagnosing why your RAG retrieval is failing</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 Cohere Reranker · HyDE · MMR</span>
    <span class="mod-pill">📋 Prerequisite: P5-M16</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🚨 Failure Modes</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔍 Pre-Retrieval</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📊 Reranking</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🌀 HyDE</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🎯 MMR & Diversity</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📏 Evaluation</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-emerald">RAG Quality Engineering</span></div>
  <div class="cp-body">
    <p>You have a working RAG pipeline. Now you need to make it <em>good</em>. This module covers the techniques that separate a demo from a production system: diagnosing why retrieval fails, fixing it with pre-retrieval query improvements, adding a reranker for precision, and using HyDE for semantically difficult queries.</p>
    <ul>
      <li><strong>Failure modes</strong> — the 5 most common reasons RAG retrieval returns wrong or irrelevant chunks</li>
      <li><strong>Pre-retrieval improvements</strong> — query rewriting, multi-query expansion, step-back prompting</li>
      <li><strong>Reranking with Cohere</strong> — a cross-encoder that re-scores your top-K results for precision</li>
      <li><strong>HyDE</strong> — Hypothetical Document Embeddings for queries that don't match document language</li>
      <li><strong>MMR</strong> — Maximum Marginal Relevance to reduce redundancy in retrieved chunks</li>
      <li><strong>Evaluation metrics</strong> — MRR, NDCG, Hit Rate — measuring retrieval quality systematically</li>
    </ul>
  </div>
</div>
</div><!-- end t0 -->


<!-- ══════════ TAB 1 — FAILURE MODES ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>The 5 Most Common RAG Retrieval Failures</h3><span class="tag tag-red">Diagnose First</span></div>
  <div class="cp-body">
    <p>Before applying fixes, diagnose which failure mode you have. Each requires a different solution.</p>
    <div class="failure-grid">
      <div class="fc fc-vocab">
        <h4>Vocabulary Mismatch</h4>
        <p>User asks "how do I make packets go faster?" — docs say "throughput optimisation". Embedding similarity is low despite identical meaning.</p>
        <div class="fix">Fix: HyDE, query rewriting, synonym expansion</div>
      </div>
      <div class="fc fc-semantic">
        <h4>Semantic Drift</h4>
        <p>Correct chunk is retrieved at rank 8 but you only return top-3. The answer exists but doesn't rank high enough.</p>
        <div class="fix">Fix: larger top-K then rerank, better chunk size</div>
      </div>
      <div class="fc fc-chunk">
        <h4>Answer Spans Chunks</h4>
        <p>The answer requires combining information from two chunks that were split at a paragraph boundary.</p>
        <div class="fix">Fix: increase overlap, larger chunks, parent-child chunking</div>
      </div>
      <div class="fc fc-topk">
        <h4>Redundant Retrieval</h4>
        <p>Top-5 chunks all say the same thing from slightly different angles. The LLM gets no diverse context.</p>
        <div class="fix">Fix: MMR (Maximum Marginal Relevance) diversity</div>
      </div>
      <div class="fc fc-meta">
        <h4>Wrong Scope Retrieved</h4>
        <p>Query is about v2.0 of an API but retrieves chunks from v1.0 that has the same section names.</p>
        <div class="fix">Fix: metadata filtering on version, date, source</div>
      </div>
    </div>
    <div class="cb"><pre><span class="ck"># Diagnostic checklist — run this before adding complexity</span>
def diagnose_retrieval(query: str, collection, expected_source: str = None):
    <span class="ck"># 1. Retrieve top-20 instead of top-5</span>
    results = collection.query(query_texts=[query], n_results=<span class="cv">20</span>,
                               include=[<span class="cs">"documents"</span>, <span class="cs">"distances"</span>, <span class="cs">"metadatas"</span>])
    docs  = results[<span class="cs">"documents"</span>][<span class="cv">0</span>]
    dists = results[<span class="cs">"distances"</span>][<span class="cv">0</span>]
 
    print(<span class="cs">f"Top-20 similarity scores: {[round(1-d,3) for d in dists]}"</span>)
    <span class="ck"># If correct chunk is rank 8+: semantic drift → reranker</span>
    <span class="ck"># If all scores < 0.5: vocabulary mismatch → HyDE or query rewrite</span>
    <span class="ck"># If scores are clustered (0.82, 0.81, 0.80...): redundancy → MMR</span>
 
    <span class="ck"># 2. Check if expected chunk exists at all</span>
    if expected_source:
        found = any(expected_source in m.get(<span class="cs">"source"</span>, <span class="cs">""</span>)
                    for m in results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>])
        print(<span class="cs">f"Expected source in top-20: {found}"</span>)
        <span class="ck"># If False and you know the doc exists: chunk too large/small → rechunk</span>
        <span class="ck"># If False because doc not indexed: ingestion bug</span></pre></div>
  </div>
</div>
</div><!-- end t1 -->


<!-- ══════════ TAB 2 — PRE-RETRIEVAL ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Query Rewriting — Fix Vocabulary Mismatch</h3><span class="tag tag-emerald">Pre-Retrieval</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Query rewriting: LLM transforms user query to better match document language</span>
REWRITE_PROMPT = <span class="cs">"""Rewrite the following user question to be more likely to
match technical documentation. Make it precise and use domain terminology.
Output only the rewritten question, nothing else.
 
User question: {query}
 
Rewritten:"""</span>
 
def rewrite_query(query: str) -> str:
    response = client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">100</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: REWRITE_PROMPT.format(query=query)}]
    )
    return response.content[<span class="cv">0</span>].text.strip()
 
<span class="ck"># "how do I make packets go faster?" →</span>
<span class="ck"># "methods to improve packet processing throughput and reduce latency in DPDK"</span></pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Multi-Query Expansion — Cast a Wider Net</h3><span class="tag tag-blue">Recall Boost</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Generate multiple query variants → retrieve for each → merge and deduplicate</span>
MULTI_QUERY_PROMPT = <span class="cs">"""Generate {n} different search queries that all ask about
the same topic from different angles. The queries will be used to search
technical documentation.
 
Original query: {query}
 
Output only the queries, one per line, numbered 1-{n}:"""</span>
 
def multi_query_retrieve(query: str, collection, n_variants: int = <span class="cv">3</span>,
                          n_results: int = <span class="cv">5</span>) -> list[dict]:
    <span class="ck"># Generate query variants</span>
    response = client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">200</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: MULTI_QUERY_PROMPT.format(query=query, n=n_variants)}]
    )
    lines = response.content[<span class="cv">0</span>].text.strip().split(<span class="cs">"\n"</span>)
    queries = [query]  <span class="ck"># include original</span>
    for line in lines:
        q = line.lstrip(<span class="cs">"0123456789. "</span>).strip()
        if q:
            queries.append(q)
 
    <span class="ck"># Retrieve for each query, merge results by ID</span>
    seen_ids = set()
    all_results = []
    for q in queries:
        results = collection.query(query_texts=[q], n_results=n_results,
                                   include=[<span class="cs">"documents"</span>, <span class="cs">"distances"</span>, <span class="cs">"metadatas"</span>, <span class="cs">"ids"</span>])
        for doc, dist, meta, id_ in zip(
            results[<span class="cs">"documents"</span>][<span class="cv">0</span>], results[<span class="cs">"distances"</span>][<span class="cv">0</span>],
            results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>], results[<span class="cs">"ids"</span>][<span class="cv">0</span>]
        ):
            if id_ not in seen_ids:
                seen_ids.add(id_)
                all_results.append({<span class="cs">"text"</span>: doc, <span class="cs">"score"</span>: <span class="cv">1</span>-dist, <span class="cs">"meta"</span>: meta})
 
    <span class="ck"># Sort by score and return top-K unique</span>
    return sorted(all_results, key=lambda x: x[<span class="cs">"score"</span>], reverse=<span class="cv">True</span>)</pre></div>
    <div class="ins"><p>💡 <strong>Multi-query expansion is one of the cheapest quality improvements.</strong> 3-4 Haiku calls cost ~$0.001 and dramatically improve recall — especially when users phrase queries very differently from how your documents are written. LangChain ships a <code>MultiQueryRetriever</code> that implements this pattern.</p></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⬆️</span><h3>Step-Back Prompting — Abstract Before Searching</h3><span class="tag tag-teal">Concept Shift</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Step-back: ask a more general question first, retrieve those chunks,</span>
<span class="ck"># then use them as context for the specific question</span>
<span class="ck">#</span>
<span class="ck"># Original: "What is the max burst size for rte_ring_enqueue_burst?"</span>
<span class="ck"># Step-back: "How do DPDK ring buffer enqueue operations work?"</span>
<span class="ck"># → retrieves conceptual overview → LLM can reason to the specific answer</span>
 
STEPBACK_PROMPT = <span class="cs">"""Given this specific question, write a more general version
that asks about the underlying concept or principle.
 
Specific: {query}
 
General:"""</span>
 
async def step_back_retrieve(query: str, collection) -> list[dict]:
    <span class="ck"># Generate step-back query</span>
    response = await async_client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">80</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: STEPBACK_PROMPT.format(query=query)}]
    )
    abstract_query = response.content[<span class="cv">0</span>].text.strip()
 
    <span class="ck"># Retrieve for both queries concurrently</span>
    specific_task  = asyncio.create_task(async_retrieve(query,          collection))
    abstract_task  = asyncio.create_task(async_retrieve(abstract_query, collection))
    specific, abstract = await asyncio.gather(specific_task, abstract_task)
 
    <span class="ck"># Combine: abstract provides background, specific provides targeted answer</span>
    return abstract[:<span class="cv">2</span>] + specific[:<span class="cv">3</span>]   <span class="ck"># 2 background + 3 specific</span></pre></div>
  </div>
</div>
</div><!-- end t2 -->


<!-- ══════════ TAB 3 — RERANKING ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Reranking — Two-Stage Retrieval for Precision</h3><span class="tag tag-emerald">Biggest Quality Jump</span></div>
  <div class="cp-body">
    <p>The single biggest retrieval quality improvement in most RAG systems. Embeddings are fast but approximate — they measure general semantic similarity. A reranker is a cross-encoder that reads the query AND the chunk together for a more precise relevance score.</p>
    <div class="cb"><pre><span class="ck"># Two-stage retrieval:</span>
<span class="ck"># Stage 1 — Retrieve: fast embedding search, get top-50</span>
<span class="ck"># Stage 2 — Rerank:   cross-encoder scores each of the 50 precisely</span>
<span class="ck"># Return top-5 of the reranked 50</span>
<span class="ck">#</span>
<span class="ck"># Why not use the cross-encoder for all 50,000 chunks?</span>
<span class="ck"># Cross-encoders are ~100x slower — fine for 50, too slow for 50,000</span>
 
pip install cohere
 
import cohere
co = cohere.Client()   <span class="ck"># COHERE_API_KEY from environment</span>
 
def retrieve_and_rerank(
    query: str,
    collection,
    retrieve_k: int = <span class="cv">50</span>,   <span class="ck"># retrieve many</span>
    return_k: int = <span class="cv">5</span>       <span class="ck"># return few, best ones</span>
) -> list[dict]:
    <span class="ck"># Stage 1: fast vector search</span>
    results = collection.query(
        query_texts=[query], n_results=retrieve_k,
        include=[<span class="cs">"documents"</span>, <span class="cs">"metadatas"</span>]
    )
    docs  = results[<span class="cs">"documents"</span>][<span class="cv">0</span>]
    metas = results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>]
 
    if not docs:
        return []
 
    <span class="ck"># Stage 2: Cohere reranker</span>
    rerank_response = co.rerank(
        model=<span class="cs">"rerank-english-v3.0"</span>,
        query=query,
        documents=docs,
        top_n=return_k,
        return_documents=<span class="cv">True</span>
    )
 
    return [
        {
            <span class="cs">"text"</span>:      hit.document.text,
            <span class="cs">"score"</span>:     hit.relevance_score,    <span class="ck"># 0-1, higher = more relevant</span>
            <span class="cs">"rank"</span>:      hit.index,              <span class="ck"># original rank before reranking</span>
            <span class="cs">"meta"</span>:      metas[hit.index],
        }
        for hit in rerank_response.results
    ]
 
<span class="ck"># Usage</span>
results = retrieve_and_rerank(<span class="cs">"How does DPDK mempool work?"</span>, collection)
for r in results:
    print(<span class="cs">f"Score: {r['score']:.3f} (was rank {r['rank']+1}) | {r['text'][:60]}"</span>)</pre></div>
    <div class="ins"><p>💡 <strong>Reranking typically improves precision@5 by 15-30%.</strong> The key insight is that the embedding model ranks by general semantic similarity, but the reranker asks "given THIS query, how relevant is THIS specific chunk?" — a much harder and more accurate question. Cohere rerank-english-v3.0 is the best available cross-encoder as of 2024.</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🆓</span><h3>Free Reranking — Cross-Encoders with sentence-transformers</h3><span class="tag tag-blue">No API Cost</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install sentence-transformers
 
from sentence_transformers import CrossEncoder
 
<span class="ck"># Free cross-encoder models (smaller than Cohere, still effective)</span>
<span class="ck"># ms-marco-MiniLM-L-6-v2 — fastest, reasonable quality</span>
<span class="ck"># ms-marco-MiniLM-L-12-v2 — better quality, slower</span>
<span class="ck"># cross-encoder/ms-marco-electra-base — best free quality</span>
 
reranker = CrossEncoder(<span class="cs">"cross-encoder/ms-marco-MiniLM-L-6-v2"</span>)
 
def rerank_local(query: str, docs: list[str], top_k: int = <span class="cv">5</span>) -> list[tuple]:
    """Returns (score, doc) pairs sorted by relevance."""
    pairs  = [(query, doc) for doc in docs]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(scores, docs), reverse=<span class="cv">True</span>)
    return ranked[:top_k]
 
<span class="ck"># Use in two-stage pipeline</span>
stage1_docs  = [r[<span class="cs">"text"</span>] for r in stage1_results]
reranked     = rerank_local(query, stage1_docs, top_k=<span class="cv">5</span>)
final_chunks = [doc for score, doc in reranked]</pre></div>
  </div>
</div>
</div><!-- end t3 -->


<!-- ══════════ TAB 4 — HYDE ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🌀</span><h3>HyDE — Hypothetical Document Embeddings</h3><span class="tag tag-emerald">Vocabulary Bridge</span></div>
  <div class="cp-body">
    <p>HyDE solves vocabulary mismatch by generating a hypothetical document that would answer the query, then searching for real documents similar to that hypothetical. This works because the hypothetical uses the same vocabulary and style as your real documents.</p>
    <div class="cb"><pre><span class="ck"># Standard search: embed query → find similar chunks</span>
<span class="ck"># Problem: "make packets go faster" != "throughput optimisation"</span>
<span class="ck">#</span>
<span class="ck"># HyDE search: generate a hypothetical document → embed that → find similar chunks</span>
<span class="ck"># "make packets go faster" → generates paragraph using "throughput", "mbps", "pps"</span>
<span class="ck"># → now embedding matches real doc language</span>
 
HYDE_PROMPT = <span class="cs">"""Write a short technical document passage (2-3 sentences) that would
directly answer the following question. Write as if you are an expert
writing documentation. Use precise technical terminology.
 
Question: {query}
 
Technical passage:"""</span>
 
def hyde_retrieve(query: str, collection, n_results: int = <span class="cv">5</span>) -> list[dict]:
    <span class="ck"># Step 1: generate hypothetical document</span>
    response = client.messages.create(
        model=<span class="cs">"claude-3-haiku-20240307"</span>,
        max_tokens=<span class="cv">200</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>,
                   <span class="cs">"content"</span>: HYDE_PROMPT.format(query=query)}]
    )
    hypothetical_doc = response.content[<span class="cv">0</span>].text.strip()
 
    <span class="ck"># Step 2: embed the hypothetical doc and search</span>
    results = collection.query(
        query_texts=[hypothetical_doc],   <span class="ck"># ← key: search with generated doc, not original query</span>
        n_results=n_results,
        include=[<span class="cs">"documents"</span>, <span class="cs">"distances"</span>, <span class="cs">"metadatas"</span>]
    )
    return [
        {<span class="cs">"text"</span>: doc, <span class="cs">"score"</span>: <span class="cv">1</span>-dist, <span class="cs">"meta"</span>: meta,
         <span class="cs">"hypothetical"</span>: hypothetical_doc}
        for doc, dist, meta in zip(
            results[<span class="cs">"documents"</span>][<span class="cv">0</span>],
            results[<span class="cs">"distances"</span>][<span class="cv">0</span>],
            results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>]
        )
    ]
 
<span class="ck"># Hybrid: retrieve with both original query and HyDE, merge</span>
def hybrid_hyde(query: str, collection, n_results: int = <span class="cv">5</span>) -> list[dict]:
    standard = collection.query(query_texts=[query], n_results=n_results,
                                include=[<span class="cs">"documents"</span>, <span class="cs">"distances"</span>, <span class="cs">"metadatas"</span>, <span class="cs">"ids"</span>])
    hyde_res  = hyde_retrieve(query, collection, n_results=n_results)
 
    <span class="ck"># Merge unique results, original query results get slight preference</span>
    seen = set()
    merged = []
    for r in hyde_res:
        if r[<span class="cs">"text"</span>] not in seen:
            seen.add(r[<span class="cs">"text"</span>])
            merged.append(r)
    for doc, dist, meta in zip(standard[<span class="cs">"documents"</span>][<span class="cv">0</span>],
                                standard[<span class="cs">"distances"</span>][<span class="cv">0</span>],
                                standard[<span class="cs">"metadatas"</span>][<span class="cv">0</span>]):
        if doc not in seen:
            seen.add(doc)
            merged.append({<span class="cs">"text"</span>: doc, <span class="cs">"score"</span>: <span class="cv">1</span>-dist, <span class="cs">"meta"</span>: meta})
    return sorted(merged, key=lambda x: x[<span class="cs">"score"</span>], reverse=<span class="cv">True</span>)[:n_results]</pre></div>
    <div class="warn"><p>⚠️ <strong>HyDE adds hallucination risk.</strong> If the hypothetical document is factually wrong, you retrieve chunks similar to wrong information. Always use HyDE as an additional retrieval path (hybrid), never as the sole retrieval method. Rerank afterwards to surface the truly relevant chunks.</p></div>
  </div>
</div>
</div><!-- end t4 -->


<!-- ══════════ TAB 5 — MMR & DIVERSITY ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>MMR — Maximum Marginal Relevance</h3><span class="tag tag-emerald">Diversity</span></div>
  <div class="cp-body">
    <p>MMR balances relevance and diversity. Without it, your top-5 chunks might all be near-identical paragraphs from the same section. MMR ensures each selected chunk adds new information.</p>
    <div class="cb"><pre>import numpy as np
 
def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + <span class="cv">1e-8</span>))
 
def mmr(
    query_vec: list[float],
    candidate_vecs: list[list[float]],
    candidate_docs: list[str],
    top_k: int = <span class="cv">5</span>,
    lambda_param: float = <span class="cv">0.5</span>   <span class="ck"># 0=max diversity, 1=max relevance</span>
) -> list[str]:
    """
    Maximum Marginal Relevance selection.
    Iteratively picks the candidate that maximises:
        lambda * similarity(query, doc) - (1-lambda) * max_similarity(doc, selected)
    """
    selected_idx   = []
    selected_vecs  = []
    remaining_idx  = list(range(len(candidate_docs)))
 
    for _ in range(min(top_k, len(candidate_docs))):
        best_score, best_idx = -<span class="cv">1</span>, -<span class="cv">1</span>
 
        for idx in remaining_idx:
            relevance = cosine_sim(query_vec, candidate_vecs[idx])
 
            if not selected_vecs:
                redundancy = <span class="cv">0</span>
            else:
                redundancy = max(cosine_sim(candidate_vecs[idx], sv)
                                 for sv in selected_vecs)
 
            score = lambda_param * relevance - (<span class="cv">1</span> - lambda_param) * redundancy
            if score > best_score:
                best_score, best_idx = score, idx
 
        selected_idx.append(best_idx)
        selected_vecs.append(candidate_vecs[best_idx])
        remaining_idx.remove(best_idx)
 
    return [candidate_docs[i] for i in selected_idx]
 
<span class="ck"># Practical example</span>
<span class="ck"># 1. Retrieve top-20 with embeddings</span>
<span class="ck"># 2. Apply MMR to select 5 diverse chunks</span>
<span class="ck"># 3. Pass to LLM — it now has diverse context, not 5 copies of the same info</span></pre></div>
    <div class="ins"><p>💡 <strong>lambda_param tuning:</strong> For factual Q&A where precision matters, use lambda=0.7 (favour relevance). For open-ended research questions where you want broad coverage, use lambda=0.3 (favour diversity). ChromaDB's <code>query()</code> does not natively support MMR — implement it as a post-retrieval step on the returned vectors.</p></div>
  </div>
</div>
</div><!-- end t5 -->


<!-- ══════════ TAB 6 — EVALUATION ══════════ -->
<div id="t6" class="tab-pane">
<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">📏</span><h3>Measuring Retrieval Quality — MRR, Hit Rate, NDCG</h3><span class="tag tag-emerald">Systematic Evaluation</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Build a test set: queries + expected source chunks</span>
test_set = [
    {<span class="cs">"query"</span>: <span class="cs">"How does DPDK mempool initialisation work?"</span>,
     <span class="cs">"expected_source"</span>: <span class="cs">"dpdk_guide.pdf"</span>,
     <span class="cs">"expected_section"</span>: <span class="cs">"Memory Management"</span>},
    {<span class="cs">"query"</span>: <span class="cs">"What is the rte_ring burst size limit?"</span>,
     <span class="cs">"expected_source"</span>: <span class="cs">"dpdk_guide.pdf"</span>,
     <span class="cs">"expected_section"</span>: <span class="cs">"Ring Library"</span>},
    <span class="ck"># ... 20+ test cases</span>
]
 
def hit_rate(results: list[dict], expected_source: str, k: int = <span class="cv">5</span>) -> float:
    """1 if expected source appears in top-k, else 0."""
    top_k = results[:k]
    return <span class="cv">1.0</span> if any(expected_source in r[<span class="cs">"meta"</span>].get(<span class="cs">"source"</span>, <span class="cs">""</span>)
                         for r in top_k) else <span class="cv">0.0</span>
 
def mrr(results: list[dict], expected_source: str) -> float:
    """Mean Reciprocal Rank — higher rank = higher score."""
    for i, r in enumerate(results):
        if expected_source in r[<span class="cs">"meta"</span>].get(<span class="cs">"source"</span>, <span class="cs">""</span>):
            return <span class="cv">1.0</span> / (i + <span class="cv">1</span>)
    return <span class="cv">0.0</span>
 
def evaluate_pipeline(retrieval_fn, test_set: list[dict], k: int = <span class="cv">5</span>) -> dict:
    hit_rates, mrrs = [], []
    for test in test_set:
        results = retrieval_fn(test[<span class="cs">"query"</span>])
        hit_rates.append(hit_rate(results, test[<span class="cs">"expected_source"</span>], k))
        mrrs.append(mrr(results, test[<span class="cs">"expected_source"</span>]))
 
    return {
        <span class="cs">f"hit_rate@{k}"</span>: round(sum(hit_rates) / len(hit_rates), <span class="cv">3</span>),
        <span class="cs">"mrr"</span>:         round(sum(mrrs) / len(mrrs), <span class="cv">3</span>),
        <span class="cs">"n_queries"</span>:   len(test_set),
    }
 
<span class="ck"># Compare pipelines</span>
baseline = evaluate_pipeline(lambda q: basic_retrieve(q), test_set)
reranked = evaluate_pipeline(lambda q: retrieve_and_rerank(q, collection), test_set)
hyde_res = evaluate_pipeline(lambda q: hyde_retrieve(q, collection), test_set)
 
print(<span class="cs">f"Baseline:  {baseline}"</span>)  <span class="ck"># {"hit_rate@5": 0.65, "mrr": 0.48}</span>
print(<span class="cs">f"Reranked:  {reranked}"</span>)  <span class="ck"># {"hit_rate@5": 0.82, "mrr": 0.67}</span>
print(<span class="cs">f"HyDE:      {hyde_res}"</span>)  <span class="ck"># {"hit_rate@5": 0.74, "mrr": 0.55}</span></pre></div>
  </div>
</div>
</div><!-- end t6 -->


<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.cohere.com/docs/reranking-with-cohere" target="_blank" rel="noopener">Cohere Reranking Guide — docs.cohere.com/docs/reranking-with-cohere</a></td><td>Official Cohere reranker documentation with API reference and best practices.</td></tr>
    <tr><td class="res-type">Guide</td><td><a href="https://www.pinecone.io/learn/retrieval-augmented-generation" target="_blank" rel="noopener">Pinecone: Improving Retrieval Quality — pinecone.io/learn</a></td><td>Practical guide covering common RAG failure modes and fixes including reranking and HyDE.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://python.langchain.com/docs/how_to/#query-analysis" target="_blank" rel="noopener">LangChain: Query Transformations — python.langchain.com</a></td><td>Query rewriting, step-back prompting, and HyDE implementation in LangChain.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://www.anthropic.com/news/contextual-retrieval" target="_blank" rel="noopener">Anthropic: Contextual Retrieval — anthropic.com</a></td><td>Covers BM25 hybrid search + reranking combination for best retrieval quality.</td></tr>
  </tbody>
</table>
</div><!-- end t7 -->


<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Retrieval Quality Benchmark — 4 Pipelines Compared</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build and benchmark 4 retrieval pipelines on the same document collection and test set. This is the experiment you would run before choosing a retrieval strategy for production.</p>
    <h4>Requirements</h4>
    <ul>
      <li>Use the document collection from M16. Write a 20-question test set with ground truth sources.</li>
      <li><strong>Pipeline 1</strong> — Baseline: simple vector search, top-5</li>
      <li><strong>Pipeline 2</strong> — Multi-query: 3 query variants, deduplicated results</li>
      <li><strong>Pipeline 3</strong> — Reranked: top-50 vector search → Cohere rerank → top-5</li>
      <li><strong>Pipeline 4</strong> — HyDE + Rerank: hypothetical doc search → Cohere rerank → top-5</li>
      <li>Evaluate all 4 on hit_rate@5, mrr, and avg query latency</li>
      <li>Present findings: which pipeline wins? What is the cost per query for each?</li>
    </ul>
    <p><strong>Skills:</strong> Cohere reranker, multi-query expansion, HyDE, MRR/hit-rate evaluation, cost analysis</p>
  </div>
</div>
</div><!-- end t8 -->


<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Diagnose a Failing RAG System</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Apply the diagnostic framework to identify which failure mode you have — before guessing at fixes.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take your M16 collection. Find 3 queries where the baseline retrieval clearly fails (answer not in top-5). Log the failure for each.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>For each failure, run the diagnostic: retrieve top-20, print similarity scores. Classify: vocabulary mismatch (&lt;0.5 scores), semantic drift (correct at rank 8+), redundancy (scores clustered), span issue, or wrong scope.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Apply the matching fix for each failure mode. Verify the fix improved retrieval for that specific query.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Check for regressions: did the fix break any previously working queries? Document the trade-off.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Reranker — Measure the Precision Jump</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Quantify exactly how much reranking improves precision on your specific document collection.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write 15 test queries with ground truth sources. Run baseline (top-5 vector search). Score hit_rate@5 and MRR.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run two-stage: top-50 vector search → Cohere rerank → top-5. Score the same metrics.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>For queries where reranking changed the rank ordering significantly, inspect the before/after. Why did the reranker move those chunks up or down?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Calculate cost per query: embedding cost (stage 1) + reranking cost (stage 2). At what query volume does the cost become significant?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>HyDE vs Standard — When Does It Help?</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Identify which types of queries benefit most from HyDE.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create 3 categories of test queries: (a) 5 queries using exact document vocabulary ("rte_mempool initialisation"), (b) 5 queries using layman language ("make memory faster"), (c) 5 conceptual queries ("why does DPDK avoid kernel").</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run standard retrieval and HyDE on all 15. Record hit_rate@5 per category for each method.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>For each category, compare: standard vs HyDE. Which query type benefits most from HyDE?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Document your conclusion: when to activate HyDE, when to skip it (and why it adds unnecessary latency and cost for queries that already match well).</div></div>
  </div>
</div>
</div><!-- end t9 -->


<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P5-M17 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can name the 5 RAG retrieval failure modes and identify which one is occurring from diagnostic signals</li>
  <li>Know that similarity scores below 0.5 indicate vocabulary mismatch, not bad chunking</li>
  <li>Can implement query rewriting using a cheap LLM to match document vocabulary</li>
  <li>Can implement multi-query expansion: generate N variants, retrieve for each, deduplicate by ID</li>
  <li>Can implement step-back prompting: abstract the query first, retrieve background context</li>
  <li>Understand two-stage retrieval: retrieve large K with embeddings, rerank to small K with cross-encoder</li>
  <li>Can implement Cohere reranking with retrieve_k=50 and return_k=5</li>
  <li>Can implement free local reranking with sentence-transformers CrossEncoder</li>
  <li>Know that rerankers read query+chunk together (cross-encoder) vs embeddings which are independent (bi-encoder)</li>
  <li>Can explain HyDE: generate hypothetical document → embed it → search for real similar documents</li>
  <li>Know that HyDE adds hallucination risk and should always be used as a hybrid, not sole retrieval path</li>
  <li>Can implement MMR to reduce redundancy in retrieved chunks</li>
  <li>Know lambda_param for MMR: 0.7 for factual Q&amp;A (relevance), 0.3 for research (diversity)</li>
  <li>Can build a test set with ground truth and compute hit_rate@K and MRR</li>
  <li>Can run an evaluation comparing multiple retrieval pipelines and make a cost/quality trade-off decision</li>
  <li>Completed Lab 1: diagnosed failing RAG system with failure mode classification</li>
  <li>Completed Lab 2: reranker precision measurement</li>
  <li>Completed Lab 3: HyDE vs standard query type analysis</li>
  <li>Milestone project: 4-pipeline benchmark pushed to GitHub with findings</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P5-M18 — RAG Pipelines, Grounding &amp; Hallucination Reduction</strong>. You now have excellent retrieval. M18 covers combining retrieval with LLM generation into a complete, production-grade RAG system.</p>
</div>
</div><!-- end t10 -->

<div class="mod-nav">
  <a href="/learning/ai-ml/part5-rag/p5-m16-chunking/">← P5-M16: Chunking</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part5-rag/p5-m18-rag-pipelines/">Next: P5-M18 — RAG Pipelines →</a>
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
    const key = 'p5m17-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
