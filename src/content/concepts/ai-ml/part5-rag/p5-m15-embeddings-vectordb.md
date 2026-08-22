---
title: "P5-M15 - Embeddings & Vector Databases"
description: "Part 5 — RAG Systems · Module 15 of 18 Embeddings Vector Databases Turn text into searchable numbers — the foundation of every RAG system ⏱ 1 Week 🟡 Intermediate 🔧 ChromaDB ·…"
domain: ai-ml
track: ai-ml-engineering
module: part5-rag
order: 515
url: /learning/ai-ml/part5-rag/p5-m15-embeddings-vectordb/
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
/* embedding viz */
.embed-viz{display:flex;align-items:center;gap:.5rem;margin:.8rem 0;flex-wrap:wrap}
.ev-word{background:#ecfdf5;border:1.5px solid #6ee7b7;border-radius:8px;padding:.5rem .9rem;font-family:monospace;font-size:.85rem;font-weight:700;color:#065f46}
.ev-arrow{color:#059669;font-size:1.2rem;font-weight:700}
.ev-vec{background:#0a1e14;border-radius:8px;padding:.4rem .8rem;font-family:monospace;font-size:.78rem;color:#6ee7b7;white-space:nowrap}
/* vdb comparison */
.vdb-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.8rem;margin:.8rem 0}
.vdb-card{border-radius:10px;padding:1rem 1.1rem;border:1.5px solid}
.vdb-card h4{font-size:.9rem;font-weight:700;margin-bottom:.5rem;border:none}
.vdb-card p{font-size:.82rem;line-height:1.6;margin:0;color:var(--text-color,#444)}
.vdb-card .badge{display:inline-block;font-size:.68rem;font-family:monospace;font-weight:700;padding:1px 7px;border-radius:4px;margin-bottom:.4rem}
.vc-chroma{background:#ecfdf5;border-color:#6ee7b7}.vc-chroma h4{color:#065f46}.vc-chroma .badge{background:#6ee7b7;color:#065f46}
.vc-pinecone{background:#eef2ff;border-color:#818cf8}.vc-pinecone h4{color:#3730a3}.vc-pinecone .badge{background:#818cf8;color:#fff}
.vc-qdrant{background:#faeee4;border-color:#fdba74}.vc-qdrant h4{color:#9a3412}.vc-qdrant .badge{background:#fdba74;color:#7c2d12}
.vc-pgvector{background:#fdf4dc;border-color:#fcd34d}.vc-pgvector h4{color:#92400e}.vc-pgvector .badge{background:#fcd34d;color:#78350f}
.vc-faiss{background:#ede8f5;border-color:#c4b5fd}.vc-faiss h4{color:#5b21b6}.vc-faiss .badge{background:#c4b5fd;color:#4c1d95}
</style>

<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 5 — RAG Systems &nbsp;·&nbsp; Module 15 of 18</div>
  <div class="mod-title">Embeddings &amp; Vector Databases</div>
  <div class="mod-subtitle">Turn text into searchable numbers — the foundation of every RAG system</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 ChromaDB · Pinecone · pgvector · FAISS</span>
    <span class="mod-pill">📋 Prerequisite: P4 Complete</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🔢 Embeddings</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔍 Similarity Search</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🗄 Vector Databases</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🟢 ChromaDB</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📌 Pinecone & Qdrant</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🐘 pgvector & FAISS</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>


<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-emerald">RAG Foundation</span></div>
  <div class="cp-body">
    <p>RAG (Retrieval-Augmented Generation) lets LLMs answer questions about your own documents. The foundation of RAG is embeddings — mathematical representations of text that capture meaning — and vector databases that store and search them efficiently. This module teaches you everything you need to build the retrieval layer.</p>
    <ul>
      <li><strong>Embeddings</strong> — what they are, how they encode meaning, why similar texts produce similar vectors</li>
      <li><strong>Embedding models</strong> — OpenAI text-embedding-3, Cohere embed, HuggingFace sentence-transformers</li>
      <li><strong>Similarity metrics</strong> — cosine similarity, dot product, Euclidean distance — when to use each</li>
      <li><strong>Vector databases</strong> — ChromaDB, Pinecone, Qdrant, pgvector, FAISS — how to choose</li>
      <li><strong>Indexing and querying</strong> — adding documents, querying by semantic similarity, filtering with metadata</li>
      <li><strong>Embedding costs and performance</strong> — batch embedding, caching, model selection</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>Where This Fits in RAG</h3><span class="tag tag-blue">Architecture</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># The full RAG pipeline — this module covers the RETRIEVAL box</span>
<span class="ck">#</span>
<span class="ck"># INDEXING (offline):                RETRIEVAL (online, per query):</span>
<span class="ck">#</span>
<span class="ck"># Documents                          User Question</span>
<span class="ck">#    ↓                                    ↓</span>
<span class="ck"># Chunking (M16)           →    Embed question (this module)</span>
<span class="ck">#    ↓                                    ↓</span>
<span class="ck"># Embed chunks (this module) →   Search vector DB (this module)</span>
<span class="ck">#    ↓                                    ↓</span>
<span class="ck"># Store in Vector DB (this) →    Top-K chunks returned</span>
<span class="ck">#                                         ↓</span>
<span class="ck">#                               Reranking (M17)</span>
<span class="ck">#                                         ↓</span>
<span class="ck">#                               LLM generates answer (M18)</span></pre></div>
  </div>
</div>

</div><!-- end t0 -->


<!-- ══════════ TAB 1 — EMBEDDINGS ══════════ -->
<div id="t1" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>What Are Embeddings?</h3><span class="tag tag-emerald">Concept First</span></div>
  <div class="cp-body">
    <p>An embedding is a list of floating-point numbers (a vector) that represents the <strong>meaning</strong> of a piece of text. The embedding model maps semantically similar texts to nearby points in vector space — so "dog" and "canine" are close together, but "dog" and "database" are far apart.</p>
    <div class="embed-viz">
      <div class="ev-word">"dog"</div>
      <div class="ev-arrow">→</div>
      <div class="ev-vec">[0.82, -0.14, 0.33, 0.67, ...]<br>1536 dimensions</div>
    </div>
    <div class="embed-viz">
      <div class="ev-word">"canine"</div>
      <div class="ev-arrow">→</div>
      <div class="ev-vec">[0.79, -0.11, 0.31, 0.71, ...]<br>← very close to "dog"</div>
    </div>
    <div class="embed-viz">
      <div class="ev-word">"database"</div>
      <div class="ev-arrow">→</div>
      <div class="ev-vec">[-0.23, 0.88, -0.45, 0.12, ...]<br>← far from "dog"</div>
    </div>
    <div class="ins"><p>💡 <strong>The key insight:</strong> you never look at the actual numbers. The magic is that vector distance corresponds to semantic similarity. Two passages about the same topic will have similar vectors even if they use completely different words — enabling semantic search that keyword search cannot match.</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Generating Embeddings — OpenAI, Cohere, HuggingFace</h3><span class="tag tag-blue">Code</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install openai cohere sentence-transformers

<span class="ck"># ── OpenAI Embeddings ─────────────────────────────────</span>
from openai import OpenAI
client = OpenAI()

def embed_openai(texts: list[str], model: str = <span class="cs">"text-embedding-3-small"</span>) -> list[list[float]]:
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]

<span class="ck"># Single text</span>
vec = embed_openai([<span class="cs">"What is DPDK?"</span>])[<span class="cv">0</span>]
print(<span class="cs">f"Dimensions: {len(vec)}"</span>)   <span class="ck"># 1536 for text-embedding-3-small</span>

<span class="ck"># Batch — much more efficient (one API call for many texts)</span>
docs = [<span class="cs">"DPDK is a packet processing framework"</span>,
        <span class="cs">"VPP runs on DPDK for high-performance networking"</span>,
        <span class="cs">"Machine learning uses gradient descent"</span>]
vecs = embed_openai(docs)   <span class="ck"># 3 embeddings, 1 API call</span>

<span class="ck"># ── Cohere Embeddings ─────────────────────────────────</span>
import cohere
co = cohere.Client()   <span class="ck"># COHERE_API_KEY from environment</span>

response = co.embed(
    texts=docs,
    model=<span class="cs">"embed-english-v3.0"</span>,
    input_type=<span class="cs">"search_document"</span>   <span class="ck"># "search_document" for indexing, "search_query" for queries</span>
)
vecs = response.embeddings   <span class="ck"># list of lists</span>

<span class="ck"># ── HuggingFace Sentence Transformers (free, local) ───</span>
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(<span class="cs">"all-MiniLM-L6-v2"</span>)   <span class="ck"># 384 dims, fast, free</span>
vecs = model.encode(docs, show_progress_bar=<span class="cv">True</span>)   <span class="ck"># numpy arrays</span>
print(vecs.shape)   <span class="ck"># (3, 384)</span>

<span class="ck"># Better quality, slower:</span>
model = SentenceTransformer(<span class="cs">"BAAI/bge-large-en-v1.5"</span>)   <span class="ck"># 1024 dims, SOTA free model</span></pre></div>

    <table style="width:100%;border-collapse:collapse;font-size:.84rem;margin:.8rem 0">
      <thead><tr style="background:#0a2040;color:#d1fae5"><th style="padding:.55rem .8rem;text-align:left">Model</th><th style="padding:.55rem .8rem">Dims</th><th style="padding:.55rem .8rem">Cost</th><th style="padding:.55rem .8rem">Best For</th></tr></thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>text-embedding-3-small</strong></td><td style="padding:.55rem .8rem">1536</td><td style="padding:.55rem .8rem">$0.02/1M tokens</td><td style="padding:.55rem .8rem">Default choice — great quality, cheap</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>text-embedding-3-large</strong></td><td style="padding:.55rem .8rem">3072</td><td style="padding:.55rem .8rem">$0.13/1M tokens</td><td style="padding:.55rem .8rem">Highest quality, higher cost</td></tr>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>embed-english-v3.0 (Cohere)</strong></td><td style="padding:.55rem .8rem">1024</td><td style="padding:.55rem .8rem">$0.10/1M tokens</td><td style="padding:.55rem .8rem">Best with Cohere reranker (M17)</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>all-MiniLM-L6-v2</strong></td><td style="padding:.55rem .8rem">384</td><td style="padding:.55rem .8rem">Free (local)</td><td style="padding:.55rem .8rem">Prototyping, offline, no API cost</td></tr>
        <tr><td style="padding:.55rem .8rem"><strong>BAAI/bge-large-en-v1.5</strong></td><td style="padding:.55rem .8rem">1024</td><td style="padding:.55rem .8rem">Free (local)</td><td style="padding:.55rem .8rem">Best free model quality — production with GPU</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">💡</span><h3>Embedding Best Practices</h3><span class="tag tag-teal">Production</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># 1. Always batch — never embed one text at a time in a loop</span>
<span class="ck"># BAD: 1000 API calls</span>
vecs = [embed_openai([text])[<span class="cv">0</span>] for text in texts]

<span class="ck"># GOOD: 1 API call (batch up to 2048 texts)</span>
<span class="ck"># Batch into chunks of 500 to stay within API limits</span>
def embed_batch(texts: list[str], batch_size: int = <span class="cv">500</span>) -> list[list[float]]:
    all_embeddings = []
    for i in range(<span class="cv">0</span>, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(input=batch, model=<span class="cs">"text-embedding-3-small"</span>)
        all_embeddings.extend([item.embedding for item in response.data])
    return all_embeddings

<span class="ck"># 2. Cache embeddings — never re-embed the same text twice</span>
import hashlib, json, sqlite3

def cached_embed(text: str) -> list[float]:
    key = hashlib.md5(text.encode()).hexdigest()
    with sqlite3.connect(<span class="cs">"embeddings.db"</span>) as conn:
        conn.execute(<span class="cs">"CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, vec TEXT)"</span>)
        row = conn.execute(<span class="cs">"SELECT vec FROM cache WHERE key=?"</span>, (key,)).fetchone()
        if row:
            return json.loads(row[<span class="cv">0</span>])
        vec = embed_openai([text])[<span class="cv">0</span>]
        conn.execute(<span class="cs">"INSERT INTO cache VALUES (?,?)"</span>, (key, json.dumps(vec)))
        return vec

<span class="ck"># 3. Use the right input_type (Cohere only)</span>
<span class="ck"># Documents being indexed: input_type="search_document"</span>
<span class="ck"># User queries: input_type="search_query"</span>
<span class="ck"># Using the wrong type degrades retrieval quality</span>

<span class="ck"># 4. Normalise embeddings before cosine similarity (optional but consistent)</span>
import numpy as np

def normalise(vec: list[float]) -> list[float]:
    arr = np.array(vec)
    return (arr / np.linalg.norm(arr)).tolist()</pre></div>
  </div>
</div>

</div><!-- end t1 -->


<!-- ══════════ TAB 2 — SIMILARITY SEARCH ══════════ -->
<div id="t2" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Similarity Metrics — Cosine, Dot Product, Euclidean</h3><span class="tag tag-emerald">Core Math</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import numpy as np

def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Angle between vectors. Range: -1 to 1. 1 = identical direction."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def dot_product(a: list[float], b: list[float]) -> float:
    """Dot product. Equivalent to cosine if vectors are normalised."""
    return float(np.dot(np.array(a), np.array(b)))

def euclidean_distance(a: list[float], b: list[float]) -> float:
    """Straight-line distance. Lower = more similar. Range: 0 to inf."""
    return float(np.linalg.norm(np.array(a) - np.array(b)))

<span class="ck"># Demonstrate: semantically similar texts should be close</span>
vecs = embed_openai([
    <span class="cs">"DPDK is a fast packet processing framework"</span>,
    <span class="cs">"FD.io DPDK provides high-speed networking"</span>,
    <span class="cs">"Machine learning uses gradient descent optimisation"</span>
])

print(cosine_similarity(vecs[<span class="cv">0</span>], vecs[<span class="cv">1</span>]))  <span class="ck"># ~0.91 — very similar</span>
print(cosine_similarity(vecs[<span class="cv">0</span>], vecs[<span class="cv">2</span>]))  <span class="ck"># ~0.18 — very different</span></pre></div>

    <table style="width:100%;border-collapse:collapse;font-size:.84rem;margin:.8rem 0">
      <thead><tr style="background:#0a2040;color:#d1fae5"><th style="padding:.55rem .8rem;text-align:left">Metric</th><th style="padding:.55rem .8rem">Range</th><th style="padding:.55rem .8rem">More Similar =</th><th style="padding:.55rem .8rem">Use When</th></tr></thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>Cosine Similarity</strong></td><td style="padding:.55rem .8rem">-1 to 1</td><td style="padding:.55rem .8rem">Higher (→ 1)</td><td style="padding:.55rem .8rem">Default for text. Ignores vector magnitude.</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.55rem .8rem"><strong>Dot Product</strong></td><td style="padding:.55rem .8rem">−∞ to ∞</td><td style="padding:.55rem .8rem">Higher</td><td style="padding:.55rem .8rem">When vectors are normalised (= cosine). Fastest.</td></tr>
        <tr><td style="padding:.55rem .8rem"><strong>Euclidean Distance</strong></td><td style="padding:.55rem .8rem">0 to ∞</td><td style="padding:.55rem .8rem">Lower (→ 0)</td><td style="padding:.55rem .8rem">Image embeddings, when magnitude matters.</td></tr>
      </tbody>
    </table>
    <div class="ins"><p>💡 <strong>Use cosine similarity for text embeddings by default.</strong> OpenAI recommends it for text-embedding-3 models. Most vector databases default to cosine. Dot product is equivalent and faster when vectors are L2-normalised — many embedding models output normalised vectors.</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Brute-Force vs ANN — How Vector DBs Search at Scale</h3><span class="tag tag-blue">Performance</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Brute-force: compare query to EVERY stored vector</span>
<span class="ck"># O(n × d) — works fine for &lt; 100k vectors, slow for millions</span>
def brute_force_search(query_vec, stored_vecs, top_k=5):
    scores = [(cosine_similarity(query_vec, v), i)
              for i, v in enumerate(stored_vecs)]
    scores.sort(reverse=<span class="cv">True</span>)
    return scores[:top_k]

<span class="ck"># ANN (Approximate Nearest Neighbor) — index structure for fast search</span>
<span class="ck"># HNSW (Hierarchical Navigable Small World) — used by ChromaDB, Qdrant, Weaviate</span>
<span class="ck"># IVF (Inverted File Index) — used by FAISS</span>
<span class="ck"># ANNOY — used by Spotify, disk-friendly</span>

<span class="ck"># ANN trade-off: slightly approximate results, but 100-1000x faster</span>
<span class="ck"># In practice: ANN accuracy is &gt;99% with right parameters</span>

<span class="ck"># Rule of thumb:</span>
<span class="ck"># &lt; 100k vectors:   brute force fine (ChromaDB default)</span>
<span class="ck"># 100k - 10M:       HNSW index (Qdrant, Weaviate)</span>
<span class="ck"># &gt; 10M:            FAISS IVF or managed service (Pinecone)</span></pre></div>
  </div>
</div>

</div><!-- end t2 -->


<!-- ══════════ TAB 3 — VECTOR DATABASES ══════════ -->
<div id="t3" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🗄</span><h3>Choosing a Vector Database</h3><span class="tag tag-emerald">Decision Guide</span></div>
  <div class="cp-body">
    <div class="vdb-grid">
      <div class="vdb-card vc-chroma">
        <span class="badge">Local / OSS</span>
        <h4>ChromaDB</h4>
        <p>Zero-setup local vector DB. In-memory or persisted. Perfect for prototyping and small-scale RAG. No server needed.</p>
      </div>
      <div class="vdb-card vc-pinecone">
        <span class="badge">Managed Cloud</span>
        <h4>Pinecone</h4>
        <p>Fully managed, serverless. Free tier. Best for production with no infra overhead. Up to billions of vectors.</p>
      </div>
      <div class="vdb-card vc-qdrant">
        <span class="badge">OSS / Cloud</span>
        <h4>Qdrant</h4>
        <p>Best open-source production option. Rich filtering, HNSW, Rust performance. Self-host or use Qdrant Cloud.</p>
      </div>
      <div class="vdb-card vc-pgvector">
        <span class="badge">PostgreSQL</span>
        <h4>pgvector</h4>
        <p>Vector search inside PostgreSQL. Best when your data is already in Postgres. No new infra to manage.</p>
      </div>
      <div class="vdb-card vc-faiss">
        <span class="badge">Library</span>
        <h4>FAISS</h4>
        <p>Meta's vector similarity library. Not a DB — needs wrapping. Fastest raw search for large in-memory indexes.</p>
      </div>
    </div>

    <table style="width:100%;border-collapse:collapse;font-size:.83rem;margin:.8rem 0">
      <thead><tr style="background:#0a2040;color:#d1fae5"><th style="padding:.5rem .8rem;text-align:left">Use Case</th><th style="padding:.5rem .8rem">Recommended</th><th style="padding:.5rem .8rem">Why</th></tr></thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Prototype / learning</td><td style="padding:.5rem .8rem"><strong>ChromaDB</strong></td><td style="padding:.5rem .8rem">pip install, no server, works in 5 lines</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Production (managed)</td><td style="padding:.5rem .8rem"><strong>Pinecone</strong></td><td style="padding:.5rem .8rem">No infra, scales to billions, SLA</td></tr>
        <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Production (self-hosted)</td><td style="padding:.5rem .8rem"><strong>Qdrant</strong></td><td style="padding:.5rem .8rem">Best OSS quality, rich filters, Docker deploy</td></tr>
        <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Already using Postgres</td><td style="padding:.5rem .8rem"><strong>pgvector</strong></td><td style="padding:.5rem .8rem">Reuse existing DB, ACID, familiar SQL</td></tr>
        <tr><td style="padding:.5rem .8rem">Max performance (large scale)</td><td style="padding:.5rem .8rem"><strong>FAISS</strong></td><td style="padding:.5rem .8rem">Fastest raw search, GPU support</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- end t3 -->


<!-- ══════════ TAB 4 — CHROMADB ══════════ -->
<div id="t4" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🟢</span><h3>ChromaDB — Start Here for Every RAG Project</h3><span class="tag tag-emerald">Prototype to Production</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install chromadb openai

import chromadb
from chromadb.utils import embedding_functions

<span class="ck"># ── In-memory (for tests / notebooks) ────────────────</span>
client = chromadb.Client()

<span class="ck"># ── Persistent (survives restarts) ───────────────────</span>
client = chromadb.PersistentClient(path=<span class="cs">"./chroma_db"</span>)

<span class="ck"># ── Use OpenAI embeddings automatically ──────────────</span>
oai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ[<span class="cs">"OPENAI_API_KEY"</span>],
    model_name=<span class="cs">"text-embedding-3-small"</span>
)

<span class="ck"># Create or get a collection</span>
collection = client.get_or_create_collection(
    name=<span class="cs">"docs"</span>,
    embedding_function=oai_ef,           <span class="ck"># auto-embeds on add/query</span>
    metadata={<span class="cs">"hnsw:space"</span>: <span class="cs">"cosine"</span>}   <span class="ck"># use cosine similarity</span>
)

<span class="ck"># Add documents — Chroma embeds them automatically</span>
collection.add(
    ids=[<span class="cs">"doc1"</span>, <span class="cs">"doc2"</span>, <span class="cs">"doc3"</span>],
    documents=[
        <span class="cs">"DPDK is a set of libraries for fast packet processing"</span>,
        <span class="cs">"VPP uses DPDK for high-performance networking in telecom"</span>,
        <span class="cs">"Python is a general-purpose programming language"</span>
    ],
    metadatas=[
        {<span class="cs">"source"</span>: <span class="cs">"dpdk_docs"</span>, <span class="cs">"year"</span>: <span class="cv">2024</span>},
        {<span class="cs">"source"</span>: <span class="cs">"vpp_docs"</span>,  <span class="cs">"year"</span>: <span class="cv">2024</span>},
        {<span class="cs">"source"</span>: <span class="cs">"python_docs"</span>, <span class="cs">"year"</span>: <span class="cv">2023</span>},
    ]
)

<span class="ck"># Query — semantic search</span>
results = collection.query(
    query_texts=[<span class="cs">"how does packet processing work?"</span>],
    n_results=<span class="cv">2</span>,
    include=[<span class="cs">"documents"</span>, <span class="cs">"metadatas"</span>, <span class="cs">"distances"</span>]
)
for doc, meta, dist in zip(
    results[<span class="cs">"documents"</span>][<span class="cv">0</span>],
    results[<span class="cs">"metadatas"</span>][<span class="cv">0</span>],
    results[<span class="cs">"distances"</span>][<span class="cv">0</span>]
):
    print(<span class="cs">f"Score: {1-dist:.3f} | Source: {meta['source']} | {doc[:60]}"</span>)</pre></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Metadata Filtering — Combine Semantic + Structured Search</h3><span class="tag tag-blue">Power Feature</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Filter by metadata BEFORE semantic search</span>
<span class="ck"># This is critical for multi-tenant apps or date-filtered search</span>

<span class="ck"># Only search within dpdk_docs source</span>
results = collection.query(
    query_texts=[<span class="cs">"packet processing"</span>],
    n_results=<span class="cv">5</span>,
    where={<span class="cs">"source"</span>: <span class="cs">"dpdk_docs"</span>}   <span class="ck"># metadata filter</span>
)

<span class="ck"># Numeric comparison filters</span>
results = collection.query(
    query_texts=[<span class="cs">"networking architecture"</span>],
    n_results=<span class="cv">5</span>,
    where={<span class="cs">"year"</span>: {<span class="cs">"$gte"</span>: <span class="cv">2024</span>}}   <span class="ck"># year >= 2024</span>
)

<span class="ck"># Boolean operators</span>
results = collection.query(
    query_texts=[<span class="cs">"high performance networking"</span>],
    n_results=<span class="cv">5</span>,
    where={<span class="cs">"$and"</span>: [
        {<span class="cs">"source"</span>: {<span class="cs">"$in"</span>: [<span class="cs">"dpdk_docs"</span>, <span class="cs">"vpp_docs"</span>]}},
        {<span class="cs">"year"</span>: {<span class="cs">"$gte"</span>: <span class="cv">2023</span>}}
    ]}
)

<span class="ck"># Update and delete</span>
collection.update(ids=[<span class="cs">"doc1"</span>], metadatas=[{<span class="cs">"year"</span>: <span class="cv">2025</span>}])
collection.delete(ids=[<span class="cs">"doc3"</span>])
print(collection.count())   <span class="ck"># current document count</span></pre></div>
  </div>
</div>

</div><!-- end t4 -->


<!-- ══════════ TAB 5 — PINECONE & QDRANT ══════════ -->
<div id="t5" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">📌</span><h3>Pinecone — Managed Vector DB</h3><span class="tag tag-emerald">Cloud Production</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install pinecone-client

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=os.environ[<span class="cs">"PINECONE_API_KEY"</span>])

<span class="ck"># Create index (one-time setup)</span>
pc.create_index(
    name=<span class="cs">"my-rag-index"</span>,
    dimension=<span class="cv">1536</span>,            <span class="ck"># must match embedding model dimension</span>
    metric=<span class="cs">"cosine"</span>,
    spec=ServerlessSpec(cloud=<span class="cs">"aws"</span>, region=<span class="cs">"us-east-1"</span>)
)

index = pc.Index(<span class="cs">"my-rag-index"</span>)

<span class="ck"># Upsert vectors (create or update)</span>
vectors = embed_batch(documents)
index.upsert(vectors=[
    {
        <span class="cs">"id"</span>:     <span class="cs">f"doc_{i}"</span>,
        <span class="cs">"values"</span>: vec,
        <span class="cs">"metadata"</span>: {<span class="cs">"text"</span>: doc, <span class="cs">"source"</span>: <span class="cs">"docs"</span>, <span class="cs">"chunk_idx"</span>: i}
    }
    for i, (vec, doc) in enumerate(zip(vectors, documents))
])

<span class="ck"># Query</span>
query_vec = embed_openai([<span class="cs">"packet processing performance"</span>])[<span class="cv">0</span>]
results = index.query(
    vector=query_vec,
    top_k=<span class="cv">5</span>,
    include_metadata=<span class="cv">True</span>,
    filter={<span class="cs">"source"</span>: {<span class="cs">"$eq"</span>: <span class="cs">"docs"</span>}}
)

for match in results[<span class="cs">"matches"</span>]:
    print(<span class="cs">f"Score: {match['score']:.3f} | {match['metadata']['text'][:60]}"</span>)

<span class="ck"># Index stats</span>
print(index.describe_index_stats())</pre></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔷</span><h3>Qdrant — Best Self-Hosted Option</h3><span class="tag tag-orange">OSS Production</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install qdrant-client

<span class="ck"># Start Qdrant locally with Docker:</span>
<span class="ck"># docker run -p 6333:6333 qdrant/qdrant</span>

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

client = QdrantClient(host=<span class="cs">"localhost"</span>, port=<span class="cv">6333</span>)

<span class="ck"># Create collection</span>
client.create_collection(
    collection_name=<span class="cs">"docs"</span>,
    vectors_config=VectorParams(size=<span class="cv">1536</span>, distance=Distance.COSINE),
)

<span class="ck"># Upsert points</span>
vectors = embed_batch(documents)
client.upsert(
    collection_name=<span class="cs">"docs"</span>,
    points=[
        PointStruct(
            id=i,
            vector=vec,
            payload={<span class="cs">"text"</span>: doc, <span class="cs">"source"</span>: <span class="cs">"dpdk_docs"</span>}
        )
        for i, (vec, doc) in enumerate(zip(vectors, documents))
    ]
)

<span class="ck"># Semantic search with metadata filter</span>
query_vec = embed_openai([<span class="cs">"DPDK performance"</span>])[<span class="cv">0</span>]
results = client.search(
    collection_name=<span class="cs">"docs"</span>,
    query_vector=query_vec,
    limit=<span class="cv">5</span>,
    query_filter=Filter(
        must=[FieldCondition(key=<span class="cs">"source"</span>, match=MatchValue(value=<span class="cs">"dpdk_docs"</span>))]
    ),
    with_payload=<span class="cv">True</span>
)
for hit in results:
    print(<span class="cs">f"Score: {hit.score:.3f} | {hit.payload['text'][:60]}"</span>)</pre></div>
  </div>
</div>

</div><!-- end t5 -->


<!-- ══════════ TAB 6 — PGVECTOR & FAISS ══════════ -->
<div id="t6" class="tab-pane">

<div class="cp p-emerald">
  <div class="cp-hdr"><span class="ico">🐘</span><h3>pgvector — Vector Search in PostgreSQL</h3><span class="tag tag-emerald">SQL + Vectors</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Install pgvector extension in PostgreSQL</span>
<span class="ck"># docker run -e POSTGRES_PASSWORD=pass -p 5432:5432 pgvector/pgvector:pg16</span>

pip install psycopg2-binary pgvector

import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np

conn = psycopg2.connect(<span class="cs">"postgresql://postgres:pass@localhost/ragdb"</span>)
register_vector(conn)

<span class="ck"># Enable extension and create table</span>
with conn.cursor() as cur:
    cur.execute(<span class="cs">"CREATE EXTENSION IF NOT EXISTS vector"</span>)
    cur.execute(<span class="cs">"""
        CREATE TABLE IF NOT EXISTS documents (
            id      SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            source  TEXT,
            embedding vector(1536)
        )
    """</span>)
    cur.execute(<span class="cs">"CREATE INDEX IF NOT EXISTS docs_embedding_idx ON documents USING ivfflat (embedding vector_cosine_ops)"</span>)
    conn.commit()

<span class="ck"># Insert documents with embeddings</span>
def insert_docs(texts: list[str], source: str):
    vecs = embed_batch(texts)
    with conn.cursor() as cur:
        cur.executemany(<span class="cs">"""
            INSERT INTO documents (content, source, embedding)
            VALUES (%s, %s, %s)
        """</span>, [(text, source, vec) for text, vec in zip(texts, vecs)])
    conn.commit()

<span class="ck"># Semantic search — pure SQL!</span>
def semantic_search(query: str, top_k: int = <span class="cv">5</span>, source: str = None) -> list[dict]:
    query_vec = embed_openai([query])[<span class="cv">0</span>]
    source_filter = <span class="cs">"AND source = %s"</span> if source else <span class="cs">""</span>
    params = [query_vec, top_k] if not source else [query_vec, source, top_k]

    with conn.cursor() as cur:
        cur.execute(<span class="cs">f"""
            SELECT content, source,
                   1 - (embedding &lt;=&gt; %s::vector) AS similarity
            FROM documents
            {f"WHERE source = %s" if source else ""}
            ORDER BY embedding &lt;=&gt; %s::vector
            LIMIT %s
        """</span>, [query_vec] + ([source] if source else []) + [query_vec, top_k])
        rows = cur.fetchall()
    return [{<span class="cs">"content"</span>: r[<span class="cv">0</span>], <span class="cs">"source"</span>: r[<span class="cv">1</span>], <span class="cs">"similarity"</span>: r[<span class="cv">2</span>]} for r in rows]

<span class="ck"># pgvector distance operators:</span>
<span class="ck"># &lt;-&gt;   Euclidean distance</span>
<span class="ck"># &lt;=&gt;   Cosine distance (1 - cosine_similarity)</span>
<span class="ck"># &lt;#&gt;   Negative dot product</span></pre></div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>FAISS — Maximum Performance Library</h3><span class="tag tag-purple">High Scale</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install faiss-cpu   <span class="ck"># or faiss-gpu for GPU</span>

import faiss
import numpy as np

<span class="ck"># Build an index</span>
dimension = <span class="cv">1536</span>

<span class="ck"># Flat (brute force) — exact, best for &lt; 100k vectors</span>
index = faiss.IndexFlatIP(dimension)   <span class="ck"># Inner Product (= cosine for normalised)</span>

<span class="ck"># IVF (Inverted File) — fast approximate, for &gt; 100k vectors</span>
nlist = <span class="cv">100</span>   <span class="ck"># number of clusters</span>
quantiser = faiss.IndexFlatIP(dimension)
index = faiss.IndexIVFFlat(quantiser, dimension, nlist, faiss.METRIC_INNER_PRODUCT)

<span class="ck"># Add vectors (normalised for cosine similarity)</span>
vecs = np.array(embed_batch(documents), dtype=<span class="cs">'float32'</span>)
faiss.normalize_L2(vecs)   <span class="ck"># in-place L2 normalisation</span>

if isinstance(index, faiss.IndexIVFFlat):
    index.train(vecs)   <span class="ck"># IVF index must be trained first</span>
index.add(vecs)

<span class="ck"># Search</span>
query_vec = np.array(embed_openai([<span class="cs">"packet processing"</span>]), dtype=<span class="cs">'float32'</span>)
faiss.normalize_L2(query_vec)
distances, indices = index.search(query_vec, k=<span class="cv">5</span>)

for dist, idx in zip(distances[<span class="cv">0</span>], indices[<span class="cv">0</span>]):
    if idx != -<span class="cv">1</span>:   <span class="ck"># -1 means not enough results</span>
        print(<span class="cs">f"Score: {dist:.3f} | {documents[idx][:60]}"</span>)

<span class="ck"># Save and load index</span>
faiss.write_index(index, <span class="cs">"docs.faiss"</span>)
index = faiss.read_index(<span class="cs">"docs.faiss"</span>)</pre></div>
    <div class="warn"><p>⚠️ <strong>FAISS does not store document text — only vectors and integer IDs.</strong> You must maintain a separate mapping from FAISS index position → document text (a Python list or SQLite table). This is the most common FAISS mistake.</p></div>
  </div>
</div>

</div><!-- end t6 -->


<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Article</td><td><a href="https://platform.openai.com/docs/guides/embeddings" target="_blank" rel="noopener">OpenAI Embeddings Guide — platform.openai.com/docs/guides/embeddings</a></td><td>Best introduction to text embeddings. Covers use cases, models, and similarity metrics with examples.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.trychroma.com/" target="_blank" rel="noopener">ChromaDB Documentation — docs.trychroma.com</a></td><td>Complete ChromaDB reference. Start with the Getting Started guide.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://qdrant.tech/documentation/" target="_blank" rel="noopener">Qdrant Documentation — qdrant.tech/documentation</a></td><td>Production-quality vector DB. Excellent filtering and performance documentation.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://huggingface.co/blog/getting-started-with-embeddings" target="_blank" rel="noopener">HuggingFace: Getting Started with Embeddings — huggingface.co/blog</a></td><td>Free embedding models with sentence-transformers. Hands-on with real code.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://github.com/pgvector/pgvector" target="_blank" rel="noopener">pgvector — github.com/pgvector/pgvector</a></td><td>Vector search in PostgreSQL. README covers all operators and index types.</td></tr>
  </tbody>
</table>
</div><!-- end t7 -->


<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>

<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Semantic Document Search Engine</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Build a complete semantic search engine over a collection of real documents — the foundation layer for your RAG system in M18.</p>
    <h4>Requirements</h4>
    <ul>
      <li>Index at least 50 real documents (PDF or text files from any domain you care about)</li>
      <li>Embed all documents using OpenAI text-embedding-3-small with batch embedding and caching</li>
      <li>Store in ChromaDB with metadata: source, date, category, chunk_idx</li>
      <li>Build a query function: <code>search(query, top_k=5, filter_source=None)</code> → returns ranked results with similarity scores</li>
      <li>Compare semantic search vs keyword search on 10 queries — show where semantic wins</li>
      <li>FastAPI endpoint: <code>POST /search</code> with Pydantic request/response models</li>
    </ul>
    <h4>Stretch Goals</h4>
    <ul>
      <li>Add a second collection using a free HuggingFace model — compare retrieval quality</li>
      <li>Implement the same search in pgvector — compare query time for 1000 documents</li>
      <li>Add an embedding cache to SQLite — verify zero API calls on re-indexing same documents</li>
    </ul>
    <p><strong>Skills:</strong> OpenAI embeddings, ChromaDB, batch processing, metadata filtering, FastAPI, Pydantic</p>
  </div>
</div>
</div><!-- end t8 -->


<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Visualise the Embedding Space — Make Semantic Similarity Concrete</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> See embeddings as geometry — observe that similar texts cluster together in vector space.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create 15 texts in 3 clusters: 5 about networking/DPDK, 5 about machine learning, 5 about cooking. Embed all 15 with OpenAI or a free HuggingFace model.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Compute the full 15×15 cosine similarity matrix. Print it as a formatted table. Observe: within-cluster scores should be 0.7–0.95, cross-cluster scores should be 0.1–0.4.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Use PCA to reduce to 2D: <code>from sklearn.decomposition import PCA; coords = PCA(n_components=2).fit_transform(vecs)</code>. Print the 2D coordinates for each text. Do texts cluster as expected?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Now embed 3 query texts: "What is packet processing?", "How does gradient descent work?", "How do I make pasta?". For each query, compute similarity to all 15 texts. Verify the top results match the expected cluster.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Bonus:</strong> Add 2 ambiguous texts that belong to two clusters simultaneously (e.g. "AI-powered network packet classification"). Where do they land in the similarity matrix?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>ChromaDB Full Lifecycle — Index, Query, Filter, Update</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build fluency with ChromaDB by exercising every operation.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a persistent ChromaDB collection with OpenAI embeddings. Add 30 documents from at least 3 different sources (e.g. DPDK docs, Python docs, cooking recipes). Store source, date, and category in metadata.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run these 5 query scenarios and verify results make sense: (a) semantic only — top 5 for a domain query. (b) semantic + source filter. (c) semantic + date filter. (d) semantic + $and filter combining source and category. (e) direct ID lookup: collection.get(ids=["doc1"]).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Update: change the category metadata for 3 documents. Verify with collection.get() that metadata updated but embedding is unchanged.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Delete 5 documents. Verify collection.count() decreased. Verify deleted IDs no longer appear in query results.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Test persistence: stop your Python process, restart, re-create the PersistentClient with the same path. Verify all documents are still present. This is the critical test for production use.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Compare Vector DBs — Same Data, Same Queries</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Run the same workload on two different vector DBs and compare the experience.</p>
    <div class="lab-step"><div class="sn">1</div><div>Take your 30 documents from Lab 2. Index them in <strong>both</strong> ChromaDB (already done) and Qdrant (start with Docker: <code>docker run -p 6333:6333 qdrant/qdrant</code>).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run the same 5 queries on both. Compare: (a) results match? (b) query latency (time it with time.perf_counter()). (c) metadata filtering syntax differences.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Add 1000 synthetic documents to both (generate with random text + embeddings). Re-run timing. How does each DB scale?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>If you have PostgreSQL available: implement the same search with pgvector. Compare SQL query syntax to ChromaDB/Qdrant API. What are the advantages of each approach?</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Document:</strong> Based on your experience, which DB would you choose for: (a) prototype RAG with 1k docs, (b) production RAG with 100k docs self-hosted, (c) production RAG with 10M docs managed service?</div></div>
  </div>
</div>

</div><!-- end t9 -->


<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P5-M15 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain what an embedding is — a vector that captures semantic meaning — without referring to math</li>
  <li>Can generate embeddings using OpenAI, Cohere, and a free HuggingFace sentence-transformers model</li>
  <li>Always batch embed — never call the API in a per-text loop</li>
  <li>Know to cache embeddings to SQLite to avoid re-embedding the same content</li>
  <li>Know the difference between cosine similarity, dot product, and Euclidean distance — and which to use for text</li>
  <li>Can explain ANN (approximate nearest neighbor) and why it is faster than brute-force for large collections</li>
  <li>Can choose the right vector DB for a use case: ChromaDB for prototypes, Qdrant for self-hosted production, Pinecone for managed cloud, pgvector if already using Postgres</li>
  <li>Can create a ChromaDB collection, add documents with metadata, and query with semantic + metadata filtering</li>
  <li>Can use Pinecone to upsert vectors, query by similarity, and filter by metadata</li>
  <li>Can use Qdrant with Docker for self-hosted vector search with filters</li>
  <li>Know the pgvector distance operators: &lt;-&gt; (Euclidean), &lt;=&gt; (cosine), &lt;#&gt; (dot product)</li>
  <li>Know that FAISS does not store document text — you must maintain a separate ID→text mapping</li>
  <li>Know that Cohere embeddings require different input_type for documents ("search_document") vs queries ("search_query")</li>
  <li>Completed Lab 1: visualised embedding space with similarity matrix</li>
  <li>Completed Lab 2: ChromaDB full lifecycle including persistence test</li>
  <li>Completed Lab 3: compared two vector DBs on same workload</li>
  <li>Milestone project pushed to GitHub with README</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P5-M16 — Chunking &amp; Document Ingestion</strong>. Now you know how to store and search vectors — next you learn how to prepare documents before embedding them.</p>
</div>
</div><!-- end t10 -->


<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part4-llm-apis/p4-m14-reliability-security/">← P4-M14: Reliability &amp; Security</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part5-rag/p5-m16-chunking/">Next: P5-M16 — Chunking →</a>
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
    const key = 'p5m15-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
