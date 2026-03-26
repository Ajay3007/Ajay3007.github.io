---
layout: default
title: "M06 — SQL & Indexing"
permalink: /learning/backend/m06-sql-indexing/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0e0620 0%,#1a0840 35%,#200a48 70%,#120630 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c084fc;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ddd6fe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ede9fe}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0e0620;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#c084fc;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#e879f9;border-bottom-color:#e879f9}
.tab-pane{display:none}
.tab-pane.active{display:block}

/* Concept panels */
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul,.cp-body ol{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}

/* Panel colour variants */
.p-blue  .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue  .cp-hdr{background:#0d2030}
.p-teal  .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal  .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#f3e8ff}[data-theme=dark] .p-purple .cp-hdr{background:#1e0838}
.p-green  .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green  .cp-hdr{background:#0a2018}
.p-red    .cp-hdr{background:#faeaea}[data-theme=dark] .p-red    .cp-hdr{background:#2a0808}
.p-amber  .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber  .cp-hdr{background:#2a1e00}
.p-violet .cp-hdr{background:#ede9fe}[data-theme=dark] .p-violet .cp-hdr{background:#160830}

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#f0d4ff;color:#5a1a7c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}
.tag-violet{background:#ddd6fe;color:#3b0764}

/* Code blocks */
.cb{background:#0a0418;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #8b5cf6}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ddd6fe;white-space:pre}
.cm{color:#6a4a9a}.ck{color:#c084fc}.cv{color:#f0d080}.cs{color:#f0a060}
.sql-kw{color:#c084fc;font-weight:700}
.sql-fn{color:#67e8f9}
.sql-str{color:#f0d080}
.sql-num{color:#a5f3fc}
.sql-cm{color:#5a4a7a;font-style:italic}

/* EXPLAIN plan blocks */
.explain-block{background:#0a0418;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #a855f7;font-family:'Courier New',monospace;font-size:.8rem;line-height:1.7}
.ep-node{color:#c084fc;font-weight:700}
.ep-cost{color:#fbbf24}
.ep-rows{color:#86efac}
.ep-width{color:#7dd3fc}
.ep-cond{color:#ddd6fe}
.ep-bad{color:#f87171;font-weight:700}
.ep-good{color:#4ade80;font-weight:700}

/* Insight / warning / note */
.ins{background:#f3e8ff;border:1.5px solid #8b5cf6;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#160830;border-color:#6030a8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#4c1d95}
[data-theme=dark] .ins strong{color:#c084fc}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#ede9fe;border:1.5px solid #7c3aed;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#120630;border-color:#5a20b8}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#4c1d95}
[data-theme=dark] .note strong{color:#c084fc}

.analogy{background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:1.5px solid #c4b5fd;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0e0620,#160830);border-color:#4a2888}
.analogy p{margin:0;font-size:.88rem;line-height:1.7;color:var(--text-color,#222)}

/* Flow list */
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.flow-list li{display:flex;align-items:flex-start;gap:.8rem;padding:.6rem 0;border-bottom:1px dashed var(--border-color,#e4e4e4);font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.flow-list li:last-child{border-bottom:none}
.fl-step{min-width:28px;height:28px;border-radius:50%;background:#8b5cf6;color:#fff;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.1rem}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#8b5cf6;color:#fff;padding:.5rem .8rem;text-align:left;font-weight:700}
.t-table td{padding:.45rem .8rem;border-bottom:1px solid var(--border-color,#eee);vertical-align:top;color:var(--text-color,#222)}
.t-table tr:nth-child(even) td{background:rgba(139,92,246,.05)}
[data-theme=dark] .t-table th{background:#5a20b8}
[data-theme=dark] .t-table tr:nth-child(even) td{background:rgba(139,92,246,.1)}

/* Two column */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* B-tree visual */
.btree{background:#0a0418;border-radius:10px;padding:1.2rem 1.5rem;margin:1rem 0;overflow-x:auto}
.btree pre{margin:0;font-family:'Courier New',monospace;font-size:.8rem;line-height:1.8;color:#ddd6fe;white-space:pre}
.bt-node{color:#c084fc;font-weight:700}
.bt-leaf{color:#86efac}
.bt-ptr {color:#7dd3fc}

/* Isolation level matrix */
.iso-cell-yes{background:#d1fae5;color:#065f46;font-weight:700;text-align:center}
.iso-cell-no {background:#fee2e2;color:#7f1d1d;font-weight:700;text-align:center}
[data-theme=dark] .iso-cell-yes{background:#052e16;color:#4ade80}
[data-theme=dark] .iso-cell-no {background:#2d0a0a;color:#f87171}

/* Normal form steps */
.nf-step{border:1.5px solid var(--border-color,#ddd);border-radius:8px;padding:.8rem 1rem;margin:.6rem 0}
.nf-hdr{display:flex;align-items:center;gap:.6rem;margin-bottom:.4rem}
.nf-badge{font-family:monospace;font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:4px;background:#f3e8ff;color:#4c1d95}
[data-theme=dark] .nf-badge{background:#1e0838;color:#c084fc}
.nf-step h4{margin:0;font-size:.9rem;font-weight:700;color:var(--text-color,#111)}
.nf-step p{margin:.3rem 0 0;font-size:.85rem;line-height:1.6;color:var(--text-color,#555)}

/* Lab box */
.lab-box{border:2px solid #8b5cf6;border-radius:12px;overflow:hidden;margin:1.5rem 0}
.lab-hdr{background:linear-gradient(90deg,#8b5cf6,#a855f7);padding:.8rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr h3{margin:0;font-size:1rem;font-weight:800;color:#fff;border:none}
.lab-hdr .lab-tag{background:rgba(255,255,255,.25);border-radius:4px;padding:2px 8px;font-size:.7rem;font-family:monospace;color:#fff;font-weight:700}
.lab-body{padding:1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#222);margin:.4rem 0}
.lab-step{display:flex;gap:.7rem;margin:.6rem 0;align-items:flex-start;font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.sn{min-width:24px;height:24px;border-radius:50%;background:#8b5cf6;color:#fff;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.4rem 0;font-size:.88rem;line-height:1.6;color:var(--text-color,#222);border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";color:#8b5cf6;font-size:1rem;flex-shrink:0;margin-top:.05rem}

/* Module nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0;margin-top:2rem;border-top:2px solid var(--border-color,#eee);flex-wrap:wrap;gap:.8rem}
.nb{display:inline-flex;align-items:center;gap:.4rem;font-size:.85rem;font-weight:600;color:#8b5cf6;text-decoration:none;padding:.45rem .9rem;border:1.5px solid #8b5cf6;border-radius:6px;transition:background .15s,color .15s}
.nb:hover{background:#8b5cf6;color:#fff}

.sep{border:none;border-top:1.5px dashed var(--border-color,#ddd);margin:1.5rem 0}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Backend Engineering · Phase 2 · Module 6</div>
  <div class="mod-title">SQL &amp; Indexing</div>
  <div class="mod-subtitle">The difference between a query that takes 2 ms and one that takes 2 minutes is almost always an index — or the lack of one.</div>
  <div class="mod-pills">
    <span class="mod-pill">B-tree Internals</span>
    <span class="mod-pill">EXPLAIN ANALYZE</span>
    <span class="mod-pill">Index Types</span>
    <span class="mod-pill">Normalization</span>
    <span class="mod-pill">ACID</span>
    <span class="mod-pill">Isolation Levels</span>
    <span class="mod-pill">libpq / C</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t0',this)">📋 Overview</button>
  <button class="tab-btn" onclick="vt('t1',this)">📇 Indexes</button>
  <button class="tab-btn" onclick="vt('t2',this)">🔍 EXPLAIN</button>
  <button class="tab-btn" onclick="vt('t3',this)">✍️ Query Patterns</button>
  <button class="tab-btn" onclick="vt('t4',this)">📐 Normalization</button>
  <button class="tab-btn" onclick="vt('t5',this)">🔒 ACID &amp; Isolation</button>
  <button class="tab-btn" onclick="vt('t6',this)">⚙️ C with libpq</button>
  <button class="tab-btn" onclick="vt('t7',this)">🔬 Labs</button>
  <button class="tab-btn" onclick="vt('t8',this)">✅ Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════ t0 Overview -->
<div id="t0" class="tab-pane active">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🗄️</span><h3>SQL is the Most Underestimated Backend Skill</h3><span class="tag tag-violet">POSTGRESQL FOCUS</span></div>
  <div class="cp-body">
    <p>Most backend developers know SQL syntax. Very few understand what happens inside the database when a query runs. That gap is where 90% of production performance problems hide.</p>
    <p>This module covers how PostgreSQL executes queries, how indexes work at the data-structure level, how to read execution plans, and what the ACID properties and isolation levels actually guarantee — with enough depth to diagnose real production incidents.</p>
  </div>
</div>

<h3>SQL Query Execution Pipeline</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Parse</strong> — SQL text is lexed and parsed into an Abstract Syntax Tree (AST). Syntax errors are caught here. Output: parse tree.</span></li>
  <li><span class="fl-step">2</span><span><strong>Rewrite</strong> — Rule system rewrites the parse tree. Views are expanded inline. <code>ON INSERT DO INSTEAD</code> rules are applied. Output: rewritten parse tree.</span></li>
  <li><span class="fl-step">3</span><span><strong>Plan / Optimise</strong> — The query planner generates candidate execution plans, estimates cost for each using table statistics (<code>pg_statistic</code>), and picks the cheapest plan. This is where index decisions are made. Output: plan tree.</span></li>
  <li><span class="fl-step">4</span><span><strong>Execute</strong> — The executor walks the plan tree, pulling rows from leaf nodes (seq scan, index scan) up through joins, aggregates, and sorts. Output: result rows.</span></li>
</ul>

<div class="analogy"><p>📚 <strong>Analogy:</strong> The planner is like a GPS. It doesn't know the actual traffic (data) — it estimates travel time based on historical averages (statistics). Outdated statistics = bad route choice = slow query. <code>ANALYZE</code> updates the statistics. <code>VACUUM ANALYZE</code> also reclaims dead tuple space.</p></div>

<h3>Key PostgreSQL Concepts: Quick Reference</h3>
<table class="t-table">
  <thead><tr><th>Concept</th><th>What it is</th><th>Why it matters</th></tr></thead>
  <tbody>
    <tr><td><code>MVCC</code></td><td>Multi-Version Concurrency Control — each transaction sees a snapshot; old row versions kept until vacuumed</td><td>Readers never block writers; enables repeatable reads without locks</td></tr>
    <tr><td><code>pg_statistic</code></td><td>Per-column statistics: most-common values, histogram, null fraction, distinct count</td><td>Planner cost estimates depend on this; stale stats → bad plans</td></tr>
    <tr><td><code>VACUUM</code></td><td>Reclaims space from dead tuples (rows deleted/updated but still stored for MVCC visibility)</td><td>Without autovacuum, tables bloat; XID wraparound causes downtime</td></tr>
    <tr><td><code>TOAST</code></td><td>The Oversized-Attribute Storage Technique — large values (text, bytea, jsonb) stored out-of-line</td><td>Transparent; but <code>SELECT *</code> on TOAST columns adds I/O you may not expect</td></tr>
    <tr><td><code>WAL</code></td><td>Write-Ahead Log — changes written to WAL before data pages; enables crash recovery and replication</td><td>Understanding WAL is essential for replication, point-in-time recovery</td></tr>
  </tbody>
</table>

</div>

<!-- ══════════════════════════════════════════════════════ t1 Indexes -->
<div id="t1" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">📇</span><h3>What an Index Actually Is</h3><span class="tag tag-violet">DATA STRUCTURE</span></div>
  <div class="cp-body">
    <p>An index is a separate data structure that stores a subset of column values alongside physical pointers (tuple IDs / ctids) to the heap rows. The database maintains it automatically on insert/update/delete. Every index you add speeds up reads but slows writes and consumes disk + RAM.</p>
    <p><strong>PostgreSQL index types:</strong> B-tree (default), Hash, GiST, SP-GiST, GIN, BRIN. For backend engineering, B-tree covers 95% of use cases.</p>
  </div>
</div>

<h3>B-tree Internals</h3>
<div class="btree"><pre>
  Root page
  ┌─────────────────────────────────────────────────────┐
  │  <span class="bt-node">[50]  [100]  [200]</span>                                  │
  │   ↓      ↓      ↓      ↓                            │
  └─────────────────────────────────────────────────────┘
    │      │      │      │
  Inner  Inner  Inner  Inner   ← branch pages (pointers only)
  pages  pages  pages  pages
    │
  ┌─────────────────────────────────────────────────────┐
  │  Leaf page (doubly linked list ←→)                  │
  │  <span class="bt-leaf">[42, ctid(0,5)] [43, ctid(2,1)] [44, ctid(1,8)]</span>     │
  │  <span class="bt-ptr">→ heap page 0, tuple 5</span>                              │
  └─────────────────────────────────────────────────────┘
</pre></div>

<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Root → inner pages → leaf pages:</strong> B-tree is balanced — every leaf is at the same depth. Lookup is O(log N). For 1 million rows with 100 entries per page, depth ≈ 3. That's 3 page reads for any lookup.</span></li>
  <li><span class="fl-step">2</span><span><strong>Leaf pages are doubly linked</strong> — range scans (<code>WHERE id BETWEEN 100 AND 200</code>) walk the linked list after finding the start, without re-traversing from root.</span></li>
  <li><span class="fl-step">3</span><span><strong>Each leaf entry stores: key value + ctid</strong> (physical location: page number, tuple offset in page). The executor fetches the heap page using the ctid.</span></li>
  <li><span class="fl-step">4</span><span><strong>Index-only scan:</strong> If all needed columns are in the index (covering index), the heap page fetch is skipped entirely. Check: <code>EXPLAIN</code> shows "Index Only Scan".</span></li>
</ul>

<h3>Index Types Reference</h3>
<table class="t-table">
  <thead><tr><th>Type</th><th>Operators supported</th><th>Best for</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><strong>B-tree</strong></td><td><code>=, &lt;, &lt;=, &gt;, &gt;=, BETWEEN, LIKE 'foo%'</code></td><td>Most use cases; equality and range queries</td><td>Default. Supports <code>ORDER BY</code> without sort node.</td></tr>
    <tr><td><strong>Hash</strong></td><td><code>=</code> only</td><td>Pure equality on large text keys</td><td>Faster than B-tree for equality only. No range. Not WAL-logged before PG10 (avoid pre-10).</td></tr>
    <tr><td><strong>GIN</strong></td><td><code>@&gt;, &lt;@, &amp;&amp;, @@</code></td><td>JSONB containment, full-text search, array overlap</td><td>Inverted index. Fast reads, slow updates. Use <code>gin_pending_list_limit</code>.</td></tr>
    <tr><td><strong>GiST</strong></td><td>Geometric, range types, full-text</td><td>PostGIS (geography), range overlaps, nearest-neighbour</td><td>Extensible. Slower build than B-tree.</td></tr>
    <tr><td><strong>BRIN</strong></td><td>Range queries on physically ordered data</td><td>Time-series, append-only tables (created_at)</td><td>Very small index (stores min/max per block range). Useless if data not correlated with physical order.</td></tr>
  </tbody>
</table>

<h3>Composite Indexes: Column Order Matters</h3>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📐</span><h3>The Left-Prefix Rule</h3><span class="tag tag-purple">CRITICAL</span></div>
  <div class="cp-body">
    <p>A composite index <code>(a, b, c)</code> can satisfy queries that filter on: <code>a</code>, <code>(a, b)</code>, or <code>(a, b, c)</code>. It <strong>cannot</strong> be used for queries that only filter on <code>b</code> or <code>c</code> alone, because the B-tree is sorted by <code>a</code> first.</p>
    <div class="cb"><pre><span class="sql-cm">-- Index: (user_id, status, created_at)</span>

<span class="sql-cm">-- ✅ Uses index (full prefix)</span>
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> orders
<span class="sql-kw">WHERE</span> user_id = <span class="sql-num">42</span> <span class="sql-kw">AND</span> status = <span class="sql-str">'pending'</span>
<span class="sql-kw">ORDER BY</span> created_at <span class="sql-kw">DESC</span>;

<span class="sql-cm">-- ✅ Uses index (partial prefix, range on last)</span>
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> orders
<span class="sql-kw">WHERE</span> user_id = <span class="sql-num">42</span> <span class="sql-kw">AND</span> created_at > <span class="sql-str">'2026-01-01'</span>;

<span class="sql-cm">-- ❌ Cannot use this index (no leading column)</span>
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> orders
<span class="sql-kw">WHERE</span> status = <span class="sql-str">'pending'</span>;  <span class="sql-cm">-- needs separate index on (status)</span></pre></div>
    <p><strong>Rule of thumb:</strong> Put the most selective column first (highest cardinality — most distinct values). Equality columns before range columns. The range column should be last — once you hit a range condition, the remaining columns in the index cannot be used for filtering.</p>
  </div>
</div>

<h3>Partial Indexes</h3>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>Index Only the Rows You Query</h3><span class="tag tag-green">PERFORMANCE</span></div>
  <div class="cp-body">
    <p>A partial index includes only rows matching a <code>WHERE</code> clause. Smaller, faster to maintain, and can enforce constraints on subsets of data.</p>
    <div class="cb"><pre><span class="sql-cm">-- Index only unprocessed jobs (99% of queries target this subset)</span>
<span class="sql-kw">CREATE INDEX</span> idx_jobs_pending
  <span class="sql-kw">ON</span> jobs(created_at)
  <span class="sql-kw">WHERE</span> status = <span class="sql-str">'pending'</span>;

<span class="sql-cm">-- Partial unique constraint: only one active record per user</span>
<span class="sql-kw">CREATE UNIQUE INDEX</span> idx_subscriptions_active_user
  <span class="sql-kw">ON</span> subscriptions(user_id)
  <span class="sql-kw">WHERE</span> cancelled_at <span class="sql-kw">IS NULL</span>;

<span class="sql-cm">-- Query MUST include the partial index predicate to use it</span>
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> jobs
<span class="sql-kw">WHERE</span> status = <span class="sql-str">'pending'</span> <span class="sql-kw">AND</span> created_at < now() - interval <span class="sql-str">'5 minutes'</span>;</pre></div>
  </div>
</div>

<h3>Expression Indexes</h3>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔣</span><h3>Indexing the Result of a Function</h3><span class="tag tag-blue">FUNCTIONAL INDEXES</span></div>
  <div class="cp-body">
    <p>When queries apply a function to a column in <code>WHERE</code>, a plain column index is useless — the function result isn't in the index. Expression indexes solve this.</p>
    <div class="cb"><pre><span class="sql-cm">-- ❌ Index on email NOT used — function applied to column</span>
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> users <span class="sql-kw">WHERE</span> <span class="sql-fn">lower</span>(email) = <span class="sql-str">'alice@example.com'</span>;

<span class="sql-cm">-- ✅ Create expression index to match the query</span>
<span class="sql-kw">CREATE INDEX</span> idx_users_email_lower
  <span class="sql-kw">ON</span> users(<span class="sql-fn">lower</span>(email));

<span class="sql-cm">-- Now the query above uses the index.
-- The index stores lower(email) values, not raw email values.</span>

<span class="sql-cm">-- Other common examples:</span>
<span class="sql-kw">CREATE INDEX</span> ON events(date_trunc(<span class="sql-str">'day'</span>, created_at));
<span class="sql-kw">CREATE INDEX</span> ON products((metadata->>
<span class="sql-str">'sku'</span>));  <span class="sql-cm">-- JSONB field extraction</span></pre></div>
  </div>
</div>

<h3>The Real Cost of Indexes</h3>
<table class="t-table">
  <thead><tr><th>Operation</th><th>Impact</th></tr></thead>
  <tbody>
    <tr><td><code>INSERT</code></td><td>Every index on the table gets an entry inserted. 5 indexes = 5 B-tree insertions + potential page splits.</td></tr>
    <tr><td><code>UPDATE</code></td><td>If the indexed column changes: old entry deleted + new entry inserted in every affected index. Heap-only tuple (HOT) update avoids this if the page has space and no indexed column changes.</td></tr>
    <tr><td><code>DELETE</code></td><td>Index entries marked dead; not removed until VACUUM runs.</td></tr>
    <tr><td>Disk space</td><td>A B-tree index on a 100M-row integer column ≈ 2–3 GB. JSONB GIN indexes can be 2–5× the table size.</td></tr>
    <tr><td>Cache pollution</td><td>Indexes compete with table data for <code>shared_buffers</code>. Unused indexes evict useful data.</td></tr>
  </tbody>
</table>

<div class="warn"><p>⚠️ <strong>Find and drop unused indexes:</strong> <code>SELECT indexrelname, idx_scan FROM pg_stat_user_indexes WHERE idx_scan = 0 AND schemaname = 'public';</code> — Zero scans since last stats reset means the index is dead weight. Drop it.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t2 EXPLAIN -->
<div id="t2" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Reading Query Plans</h3><span class="tag tag-violet">EXPLAIN ANALYZE</span></div>
  <div class="cp-body">
    <p><code>EXPLAIN</code> shows the plan the planner chose with estimated costs. <code>EXPLAIN ANALYZE</code> executes the query and shows actual runtime. Always use <code>EXPLAIN (ANALYZE, BUFFERS)</code> in production diagnosis — <code>BUFFERS</code> reveals cache hits vs disk reads.</p>
    <div class="cb"><pre><span class="sql-kw">EXPLAIN</span> (<span class="sql-kw">ANALYZE</span>, <span class="sql-kw">BUFFERS</span>, FORMAT TEXT)
<span class="sql-kw">SELECT</span> u.name, <span class="sql-fn">count</span>(o.id) <span class="sql-kw">AS</span> total_orders
<span class="sql-kw">FROM</span> users u
<span class="sql-kw">JOIN</span>  orders o <span class="sql-kw">ON</span> o.user_id = u.id
<span class="sql-kw">WHERE</span> u.status = <span class="sql-str">'active'</span>
<span class="sql-kw">GROUP BY</span> u.name
<span class="sql-kw">ORDER BY</span> total_orders <span class="sql-kw">DESC</span>
<span class="sql-kw">LIMIT</span> <span class="sql-num">10</span>;</pre></div>
  </div>
</div>

<h3>Anatomy of an EXPLAIN Output</h3>
<div class="explain-block"><pre>
<span class="ep-node">Limit</span>  (cost=<span class="ep-cost">1240.50..1240.53</span> rows=<span class="ep-rows">10</span> width=<span class="ep-width">40</span>)
         (actual time=<span class="ep-cost">18.432..18.435</span> rows=<span class="ep-rows">10</span> loops=<span class="ep-rows">1</span>)
  ->  <span class="ep-node">Sort</span>  (cost=<span class="ep-cost">1240.50..1242.00</span> rows=<span class="ep-rows">600</span> width=<span class="ep-width">40</span>)
            (actual time=<span class="ep-cost">18.428..18.430</span> rows=<span class="ep-rows">10</span> loops=<span class="ep-rows">1</span>)
        Sort Key: (count(o.id)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
      ->  <span class="ep-node">HashAggregate</span>  (cost=<span class="ep-cost">1200.00..1215.00</span> rows=<span class="ep-rows">600</span> width=<span class="ep-width">40</span>)
                         (actual time=<span class="ep-cost">17.900..18.100</span> rows=<span class="ep-rows">621</span> loops=<span class="ep-rows">1</span>)
            Group Key: u.name
          ->  <span class="ep-node">Hash Join</span>  (cost=<span class="ep-cost">85.00..1125.00</span> rows=<span class="ep-rows">15000</span> width=<span class="ep-width">16</span>)
                         (actual time=<span class="ep-cost">1.200..14.800</span> rows=<span class="ep-rows">14832</span> loops=<span class="ep-rows">1</span>)
                Hash Cond: (o.user_id = u.id)
              ->  <span class="ep-node">Seq Scan on orders o</span>  (cost=<span class="ep-cost">0.00..890.00</span> rows=<span class="ep-rows">50000</span> width=<span class="ep-width">8</span>)
                                       (actual time=<span class="ep-cost">0.050..6.400</span> rows=<span class="ep-rows">50000</span> loops=<span class="ep-rows">1</span>)
              ->  <span class="ep-node">Hash</span>  (cost=<span class="ep-cost">75.00..75.00</span> rows=<span class="ep-rows">800</span> width=<span class="ep-width">8</span>)
                         (actual time=<span class="ep-cost">0.900..0.900</span> rows=<span class="ep-rows">823</span> loops=<span class="ep-rows">1</span>)
                    Buckets: 1024  Batches: 1  Memory Usage: 42kB
                  ->  <span class="ep-node">Index Scan on users u</span>  (cost=<span class="ep-cost">0.29..75.00</span> rows=<span class="ep-rows">800</span> width=<span class="ep-width">8</span>)
                                            (actual time=<span class="ep-cost">0.060..0.800</span> rows=<span class="ep-rows">823</span> loops=<span class="ep-rows">1</span>)
                         Index Cond: (status = 'active')

Planning Time: 0.842 ms
Execution Time: <span class="ep-good">18.521 ms</span>
</pre></div>

<h3>How to Read It</h3>
<table class="t-table">
  <thead><tr><th>Field</th><th>Meaning</th><th>What to watch for</th></tr></thead>
  <tbody>
    <tr><td><code>cost=X..Y</code></td><td>X = startup cost (first row), Y = total cost (arbitrary planner units). Lower is better. Used for plan comparison only — not ms.</td><td>Very high total cost vs actual time can indicate stale statistics.</td></tr>
    <tr><td><code>rows=N</code></td><td>Estimated (in cost line) vs actual (in actual time line) row count.</td><td><strong>Large estimate vs actual mismatch</strong> → run <code>ANALYZE</code>. Bad estimates cascade into bad join/sort choices.</td></tr>
    <tr><td><code>loops=N</code></td><td>How many times this node executed. Nested loops execute inner node once per outer row.</td><td>High loops × high rows = N+1 problem at the SQL level.</td></tr>
    <tr><td><code>Seq Scan</code></td><td>Full table scan — reads every page.</td><td>Expected on small tables or when fetching most rows. Bad on large tables with selective WHERE clause.</td></tr>
    <tr><td><code>Index Scan</code></td><td>B-tree traversal + heap fetches for each found row.</td><td>Good. If many rows fetched: consider <code>Bitmap Index Scan</code> which batches heap fetches.</td></tr>
    <tr><td><code>Bitmap Heap Scan</code></td><td>Builds bitmap of matching heap pages, then fetches them in order (reduces random I/O).</td><td>Usually good for medium selectivity (5–20% of rows).</td></tr>
    <tr><td><code>Hash Join</code></td><td>Build hash table from smaller relation, probe with larger.</td><td>Good for large joins. Needs <code>work_mem</code>; if batches &gt; 1 it spills to disk.</td></tr>
    <tr><td><code>Nested Loop</code></td><td>For each outer row, scan inner. O(N×M) worst case.</td><td>Good when outer is small + inner has an index. Bad on large tables without index.</td></tr>
  </tbody>
</table>

<h3>Warning Signs in Plans</h3>
<div class="two-col">
  <div class="cp p-red" style="margin:0">
    <div class="cp-hdr"><span class="ico">🚨</span><h3>Red Flags</h3></div>
    <div class="cp-body">
      <ul>
        <li><strong>Seq Scan on large table</strong> with low actual rows → missing index</li>
        <li><strong>Estimated rows ≫ actual rows</strong> → stale stats, run <code>ANALYZE</code></li>
        <li><strong>Nested Loop with loops &gt; 1000</strong> → N+1 pattern in SQL</li>
        <li><strong>Sort with external merge</strong> → <code>work_mem</code> too low for sort</li>
        <li><strong>Hash Batches &gt; 1</strong> → hash join spilling to disk</li>
        <li><strong>Filter rows ≫ 0</strong> after Index Scan → over-fetching, index not selective enough</li>
      </ul>
    </div>
  </div>
  <div class="cp p-green" style="margin:0">
    <div class="cp-hdr"><span class="ico">✅</span><h3>Good Signs</h3></div>
    <div class="cp-body">
      <ul>
        <li><strong>Index Only Scan</strong> → all columns in index, heap not touched</li>
        <li><strong>Bitmap Index Scan + Bitmap Heap Scan</strong> → efficient bulk access</li>
        <li><strong>Hash Join with Batches=1</strong> → fits in memory</li>
        <li><strong>Estimated ≈ actual rows</strong> → planner has accurate stats</li>
        <li><strong>Planning time &lt; 1ms</strong> → query is not overly complex</li>
        <li><strong>Execution time consistent</strong> → data fits in <code>shared_buffers</code> (Buffers: hit)</li>
      </ul>
    </div>
  </div>
</div>

<div class="ins"><p><strong>Use <a href="https://explain.dalibo.com" target="_blank" rel="noopener noreferrer">explain.dalibo.com</a></strong> to paste <code>EXPLAIN (FORMAT JSON)</code> output and get a visual, colour-coded plan tree. Far easier to navigate than text format for complex queries.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t3 Query Patterns -->
<div id="t3" class="tab-pane">

<h3>The N+1 Query Problem</h3>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🐛</span><h3>N+1: The Silent Performance Killer</h3><span class="tag tag-red">ANTI-PATTERN</span></div>
  <div class="cp-body">
    <p>N+1 occurs when you fetch a list of N items then issue a separate query for each item. The result is N+1 round trips to the database instead of 1 or 2.</p>
    <div class="cb"><pre><span class="sql-cm">-- ❌ N+1: fetch 100 users, then 1 query per user for their posts</span>
users = <span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> users <span class="sql-kw">LIMIT</span> <span class="sql-num">100</span>;        <span class="sql-cm">-- 1 query</span>
<span class="sql-kw">FOR</span> u <span class="sql-kw">IN</span> users:
    posts = <span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> posts <span class="sql-kw">WHERE</span> user_id = u.id;  <span class="sql-cm">-- 100 queries</span>
<span class="sql-cm">-- Total: 101 queries. On 50ms RTT: ~5 seconds.</span>

<span class="sql-cm">-- ✅ Solution 1: JOIN</span>
<span class="sql-kw">SELECT</span> u.*, p.title, p.created_at
<span class="sql-kw">FROM</span> users u
<span class="sql-kw">LEFT JOIN</span> posts p <span class="sql-kw">ON</span> p.user_id = u.id
<span class="sql-kw">LIMIT</span> <span class="sql-num">100</span>;  <span class="sql-cm">-- 1 query</span>

<span class="sql-cm">-- ✅ Solution 2: Batch load (IN clause)</span>
user_ids = [1, 2, 3, ..., 100];
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> posts
<span class="sql-kw">WHERE</span> user_id = <span class="sql-kw">ANY</span>($1);  <span class="sql-cm">-- 2 total queries</span></pre></div>
  </div>
</div>

<h3>JOIN Types</h3>
<table class="t-table">
  <thead><tr><th>JOIN Type</th><th>Returns</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><code>INNER JOIN</code></td><td>Rows with matching keys in both tables</td><td>Both sides must exist. Most common.</td></tr>
    <tr><td><code>LEFT JOIN</code></td><td>All rows from left + matching from right (NULLs where no match)</td><td>Optional relationship: user may or may not have a profile.</td></tr>
    <tr><td><code>RIGHT JOIN</code></td><td>All rows from right + matching from left</td><td>Rare; rewrite as LEFT JOIN with tables swapped.</td></tr>
    <tr><td><code>FULL OUTER JOIN</code></td><td>All rows from both, NULLs where no match</td><td>Reconciliation queries, finding unmatched rows on either side.</td></tr>
    <tr><td><code>CROSS JOIN</code></td><td>Cartesian product (M × N rows)</td><td>Generating test data, pairing every item with every other. Dangerous on large tables.</td></tr>
    <tr><td><code>LATERAL JOIN</code></td><td>Subquery that can reference outer query's columns</td><td>"For each user, get their 3 most recent orders" — correlated subquery without N+1.</td></tr>
  </tbody>
</table>

<h3>CTEs vs Subqueries</h3>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Common Table Expressions</h3><span class="tag tag-blue">WITH CLAUSE</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="sql-cm">-- Subquery (inline, can be optimised away by planner)</span>
<span class="sql-kw">SELECT</span> u.name, o.total
<span class="sql-kw">FROM</span> users u
<span class="sql-kw">JOIN</span> (<span class="sql-kw">SELECT</span> user_id, <span class="sql-fn">sum</span>(amount) <span class="sql-kw">AS</span> total
      <span class="sql-kw">FROM</span> orders <span class="sql-kw">GROUP BY</span> user_id) o
<span class="sql-kw">ON</span> o.user_id = u.id;

<span class="sql-cm">-- CTE (WITH) — same query, more readable</span>
<span class="sql-kw">WITH</span> order_totals <span class="sql-kw">AS</span> (
  <span class="sql-kw">SELECT</span> user_id, <span class="sql-fn">sum</span>(amount) <span class="sql-kw">AS</span> total
  <span class="sql-kw">FROM</span> orders
  <span class="sql-kw">GROUP BY</span> user_id
)
<span class="sql-kw">SELECT</span> u.name, ot.total
<span class="sql-kw">FROM</span> users u
<span class="sql-kw">JOIN</span> order_totals ot <span class="sql-kw">ON</span> ot.user_id = u.id;

<span class="sql-cm">-- Recursive CTE: walk a tree/graph (org hierarchy, comments thread)</span>
<span class="sql-kw">WITH RECURSIVE</span> org_tree <span class="sql-kw">AS</span> (
  <span class="sql-kw">SELECT</span> id, name, manager_id, <span class="sql-num">0</span> <span class="sql-kw">AS</span> depth
  <span class="sql-kw">FROM</span> employees <span class="sql-kw">WHERE</span> manager_id <span class="sql-kw">IS NULL</span>  <span class="sql-cm">-- anchor</span>
  <span class="sql-kw">UNION ALL</span>
  <span class="sql-kw">SELECT</span> e.id, e.name, e.manager_id, ot.depth + <span class="sql-num">1</span>
  <span class="sql-kw">FROM</span> employees e
  <span class="sql-kw">JOIN</span> org_tree ot <span class="sql-kw">ON</span> e.manager_id = ot.id    <span class="sql-cm">-- recursive</span>
)
<span class="sql-kw">SELECT</span> * <span class="sql-kw">FROM</span> org_tree <span class="sql-kw">ORDER BY</span> depth;</pre></div>
    <div class="note"><p><strong>PostgreSQL ≥ 12:</strong> CTEs are inlined by default (treated as subqueries, planner can optimise through them). Use <code>WITH ... AS MATERIALIZED</code> to force the old behaviour — the CTE is executed once and cached, which can be faster when referenced multiple times.</p></p></div>
  </div>
</div>

<h3>Window Functions</h3>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🪟</span><h3>Aggregates Without Collapsing Rows</h3><span class="tag tag-amber">OVER CLAUSE</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="sql-cm">-- Rank users by order count within each country</span>
<span class="sql-kw">SELECT</span>
  name,
  country,
  order_count,
  <span class="sql-fn">rank</span>() <span class="sql-kw">OVER</span> (
    <span class="sql-kw">PARTITION BY</span> country
    <span class="sql-kw">ORDER BY</span> order_count <span class="sql-kw">DESC</span>
  ) <span class="sql-kw">AS</span> country_rank
<span class="sql-kw">FROM</span> users;

<span class="sql-cm">-- Running total (cumulative sum)</span>
<span class="sql-kw">SELECT</span>
  created_at::date,
  revenue,
  <span class="sql-fn">sum</span>(revenue) <span class="sql-kw">OVER</span> (<span class="sql-kw">ORDER BY</span> created_at::date) <span class="sql-kw">AS</span> running_total
<span class="sql-kw">FROM</span> daily_sales;

<span class="sql-cm">-- Row number for cursor pagination (stable ordering)</span>
<span class="sql-kw">SELECT</span> *, <span class="sql-fn">row_number</span>() <span class="sql-kw">OVER</span> (<span class="sql-kw">ORDER BY</span> id) <span class="sql-kw">AS</span> rn
<span class="sql-kw">FROM</span> events
<span class="sql-kw">WHERE</span> id > :last_cursor
<span class="sql-kw">LIMIT</span> <span class="sql-num">50</span>;

<span class="sql-cm">-- Lag/Lead: compare row with previous/next</span>
<span class="sql-kw">SELECT</span>
  date,
  price,
  <span class="sql-fn">lag</span>(price, <span class="sql-num">1</span>) <span class="sql-kw">OVER</span> (<span class="sql-kw">ORDER BY</span> date) <span class="sql-kw">AS</span> prev_price,
  price - <span class="sql-fn">lag</span>(price, <span class="sql-num">1</span>) <span class="sql-kw">OVER</span> (<span class="sql-kw">ORDER BY</span> date) <span class="sql-kw">AS</span> change
<span class="sql-kw">FROM</span> stock_prices;</pre></div>
  </div>
</div>

<h3>UPSERT and Conflict Handling</h3>
<div class="cb"><pre><span class="sql-cm">-- Insert or update on conflict (upsert)</span>
<span class="sql-kw">INSERT INTO</span> user_stats (user_id, login_count, last_seen)
<span class="sql-kw">VALUES</span> ($1, <span class="sql-num">1</span>, now())
<span class="sql-kw">ON CONFLICT</span> (user_id) <span class="sql-kw">DO UPDATE</span>
  <span class="sql-kw">SET</span> login_count = user_stats.login_count + <span class="sql-num">1</span>,
      last_seen   = <span class="sql-kw">EXCLUDED</span>.last_seen;  <span class="sql-cm">-- EXCLUDED = the rejected row</span>

<span class="sql-cm">-- Insert and ignore duplicates</span>
<span class="sql-kw">INSERT INTO</span> events (id, payload)
<span class="sql-kw">VALUES</span> ($1, $2)
<span class="sql-kw">ON CONFLICT</span> (id) <span class="sql-kw">DO NOTHING</span>;

<span class="sql-cm">-- Returning the affected rows (useful for getting auto-generated IDs)</span>
<span class="sql-kw">INSERT INTO</span> users (name, email)
<span class="sql-kw">VALUES</span> ($1, $2)
<span class="sql-kw">RETURNING</span> id, created_at;</pre></div>

</div>

<!-- ══════════════════════════════════════════════════════ t4 Normalization -->
<div id="t4" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Normalization: Eliminating Redundancy</h3><span class="tag tag-violet">DATA MODELLING</span></div>
  <div class="cp-body">
    <p>Normalization is the process of structuring tables to minimise data redundancy and prevent update anomalies. Each normal form adds a constraint. In practice, design to 3NF/BCNF and deliberately denormalize specific hot paths with explicit justification.</p>
  </div>
</div>

<h3>Normal Forms</h3>

<div class="nf-step">
  <div class="nf-hdr"><span class="nf-badge">1NF</span><h4>First Normal Form — Atomic Values</h4></div>
  <p><strong>Rule:</strong> Each column holds a single, indivisible value. No repeating groups (multiple phone numbers in one column). Each row is uniquely identifiable (primary key exists).</p>
  <p><strong>Violation:</strong> <code>users(id, name, phones="555-1234,555-5678")</code> — comma-delimited phones in one column.</p>
  <p><strong>Fix:</strong> Separate <code>user_phones(user_id, phone_number)</code> table with one row per phone.</p>
</div>

<div class="nf-step">
  <div class="nf-hdr"><span class="nf-badge">2NF</span><h4>Second Normal Form — No Partial Dependencies</h4></div>
  <p><strong>Rule:</strong> Must be 1NF. Every non-key column must depend on the <em>whole</em> primary key, not just part of it. Only relevant for tables with composite primary keys.</p>
  <p><strong>Violation:</strong> <code>order_items(order_id, product_id, quantity, product_name)</code> — <code>product_name</code> depends only on <code>product_id</code>, not the full <code>(order_id, product_id)</code> key.</p>
  <p><strong>Fix:</strong> Move <code>product_name</code> to the <code>products</code> table. <code>order_items</code> keeps only <code>quantity</code>.</p>
</div>

<div class="nf-step">
  <div class="nf-hdr"><span class="nf-badge">3NF</span><h4>Third Normal Form — No Transitive Dependencies</h4></div>
  <p><strong>Rule:</strong> Must be 2NF. No non-key column depends on another non-key column (transitive dependency).</p>
  <p><strong>Violation:</strong> <code>employees(id, dept_id, dept_name, salary)</code> — <code>dept_name</code> depends on <code>dept_id</code>, not directly on <code>id</code>.</p>
  <p><strong>Fix:</strong> Extract <code>departments(dept_id, dept_name)</code>. <code>employees</code> keeps only <code>dept_id</code> as a foreign key.</p>
</div>

<div class="nf-step">
  <div class="nf-hdr"><span class="nf-badge">BCNF</span><h4>Boyce-Codd Normal Form — Every Determinant Is a Candidate Key</h4></div>
  <p><strong>Rule:</strong> Stricter than 3NF. For every functional dependency X → Y, X must be a superkey (uniquely identifies rows). Fixes edge cases in 3NF with overlapping composite candidate keys.</p>
  <p><strong>Violation:</strong> <code>course_teachers(student, course, teacher)</code> where a teacher teaches only one course but a course can have multiple teachers. The dependency <code>teacher → course</code> exists, but <code>teacher</code> is not a key.</p>
  <p><strong>Fix:</strong> Decompose into <code>teacher_courses(teacher, course)</code> and <code>student_courses(student, course)</code>.</p>
</div>

<h3>When to Denormalize</h3>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Deliberate Denormalization</h3><span class="tag tag-amber">TRADE-OFF</span></div>
  <div class="cp-body">
    <p>Normalization optimises for write integrity. Denormalization trades integrity for read performance. Denormalize only when you have a measured performance problem and accept the consistency maintenance burden.</p>
    <table class="t-table">
      <thead><tr><th>Pattern</th><th>What it does</th><th>Maintenance cost</th></tr></thead>
      <tbody>
        <tr><td><strong>Cached count</strong></td><td>Store <code>posts.comment_count</code> alongside the post; increment/decrement via trigger or application logic</td><td>Must update on every insert/delete to comments</td></tr>
        <tr><td><strong>Materialized view</strong></td><td>Pre-computed JOIN result stored as a table (<code>CREATE MATERIALIZED VIEW</code>); refreshed on schedule or trigger</td><td><code>REFRESH MATERIALIZED VIEW CONCURRENTLY</code> — doesn't block reads</td></tr>
        <tr><td><strong>Duplicated columns</strong></td><td>Copy <code>user.name</code> into <code>orders.user_name</code> to avoid JOIN on every order list</td><td>Must sync on user name change (rare)</td></tr>
        <tr><td><strong>JSONB for variable attributes</strong></td><td>Store flexible/sparse attributes in a JSONB column instead of an EAV table</td><td>No schema enforcement; use GIN index for querying</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t5 ACID & Isolation -->
<div id="t5" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>ACID: Four Guarantees</h3><span class="tag tag-violet">CORRECTNESS</span></div>
  <div class="cp-body">
    <p>ACID is the contract a database makes about what happens to your data, even in the face of crashes, errors, and concurrent access. Understanding each property tells you what you can and cannot rely on.</p>
  </div>
</div>

<ul class="flow-list">
  <li><span class="fl-step">A</span><span><strong>Atomicity</strong> — A transaction is all-or-nothing. If any statement within a transaction fails, <em>all</em> changes are rolled back. There is no partial transaction. Implemented via the WAL: on crash, incomplete transactions are rolled back during recovery using the WAL log.</span></li>
  <li><span class="fl-step">C</span><span><strong>Consistency</strong> — The database moves from one valid state to another. Constraints (FK, NOT NULL, CHECK, UNIQUE) are enforced at commit time. The application is responsible for domain-level consistency (business rules).</span></li>
  <li><span class="fl-step">I</span><span><strong>Isolation</strong> — Concurrent transactions behave as if they ran serially. The degree of isolation is configurable (see isolation levels below). Full isolation is expensive; databases offer weaker but faster levels.</span></li>
  <li><span class="fl-step">D</span><span><strong>Durability</strong> — Committed transactions survive crashes. Achieved by flushing WAL to disk before acknowledging the commit. <code>synchronous_commit = off</code> trades durability for latency (risk: last few milliseconds of commits lost on crash).</span></li>
</ul>

<h3>Read Phenomena (What Can Go Wrong)</h3>
<table class="t-table">
  <thead><tr><th>Phenomenon</th><th>Description</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td><strong>Dirty Read</strong></td><td>Read uncommitted data from another transaction that may roll back</td><td>T1 reads a balance modified by T2 before T2 commits. T2 rolls back — T1 read phantom data.</td></tr>
    <tr><td><strong>Non-repeatable Read</strong></td><td>Re-reading the same row within a transaction returns different data</td><td>T1 reads price=10. T2 updates price=20 and commits. T1 re-reads: price=20. Same query, different result.</td></tr>
    <tr><td><strong>Phantom Read</strong></td><td>Re-executing a range query returns different rows</td><td>T1 counts orders WHERE status='pending': 5 rows. T2 inserts a new pending order. T1 re-counts: 6 rows.</td></tr>
    <tr><td><strong>Serialisation Anomaly</strong></td><td>Result is inconsistent with any serial order of the transactions</td><td>Write skew: two doctors both read "at least 1 on call", both go off-call — result: zero doctors on call.</td></tr>
  </tbody>
</table>

<h3>Isolation Levels</h3>
<table class="t-table">
  <thead>
    <tr>
      <th>Level</th>
      <th>Dirty Read</th>
      <th>Non-Repeatable</th>
      <th>Phantom</th>
      <th>Serialisation Anomaly</th>
      <th>PostgreSQL default?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Read Uncommitted</strong></td>
      <td class="iso-cell-no">Possible</td>
      <td class="iso-cell-no">Possible</td>
      <td class="iso-cell-no">Possible</td>
      <td class="iso-cell-no">Possible</td>
      <td>No (PG treats as Read Committed)</td>
    </tr>
    <tr>
      <td><strong>Read Committed</strong></td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-no">Possible</td>
      <td class="iso-cell-no">Possible</td>
      <td class="iso-cell-no">Possible</td>
      <td>✅ Default</td>
    </tr>
    <tr>
      <td><strong>Repeatable Read</strong></td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-yes">Not possible*</td>
      <td class="iso-cell-no">Possible</td>
      <td>No</td>
    </tr>
    <tr>
      <td><strong>Serializable</strong></td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-yes">Not possible</td>
      <td class="iso-cell-yes">Not possible</td>
      <td>No (highest cost)</td>
    </tr>
  </tbody>
</table>

<div class="note"><p>*PostgreSQL's Repeatable Read uses snapshot isolation which prevents phantoms too — stronger than the SQL standard requires. PG's Serializable uses Serializable Snapshot Isolation (SSI), a lock-free algorithm that detects and aborts transactions that would create anomalies.</p></p></div>

<h3>Deadlocks</h3>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">💀</span><h3>Deadlock Detection and Prevention</h3><span class="tag tag-red">CONCURRENCY</span></div>
  <div class="cp-body">
    <p>A deadlock occurs when two (or more) transactions each hold a lock the other needs, creating a circular wait.</p>
    <div class="cb"><pre><span class="sql-cm">-- T1                              T2</span>
<span class="sql-kw">BEGIN</span>;                           <span class="sql-kw">BEGIN</span>;
<span class="sql-kw">UPDATE</span> accounts <span class="sql-kw">SET</span> bal=bal-100   <span class="sql-kw">UPDATE</span> accounts <span class="sql-kw">SET</span> bal=bal+100
<span class="sql-kw">WHERE</span> id=<span class="sql-num">1</span>;  <span class="sql-cm">-- locks row 1</span>       <span class="sql-kw">WHERE</span> id=<span class="sql-num">2</span>;  <span class="sql-cm">-- locks row 2</span>
<span class="sql-kw">UPDATE</span> accounts <span class="sql-kw">SET</span> bal=bal+100   <span class="sql-kw">UPDATE</span> accounts <span class="sql-kw">SET</span> bal=bal-100
<span class="sql-kw">WHERE</span> id=<span class="sql-num">2</span>;  <span class="sql-cm">-- waits for row 2</span>   <span class="sql-kw">WHERE</span> id=<span class="sql-num">1</span>;  <span class="sql-cm">-- waits for row 1 ← DEADLOCK</span></pre></div>
    <p>PostgreSQL detects deadlocks automatically (within <code>deadlock_timeout</code>, default 1s) and aborts one transaction with: <code>ERROR: deadlock detected</code>. The other continues normally.</p>
    <h4>Prevention Strategies</h4>
    <ul>
      <li><strong>Consistent lock ordering:</strong> always lock resources in the same order (e.g., always lock lower ID first). Eliminates the circular wait condition.</li>
      <li><strong><code>SELECT FOR UPDATE SKIP LOCKED</code>:</strong> skip rows locked by other transactions instead of waiting. Useful for job queues.</li>
      <li><strong><code>NOWAIT</code>:</strong> fail immediately if lock cannot be acquired: <code>SELECT ... FOR UPDATE NOWAIT</code> → returns error, never waits.</li>
      <li><strong>Short transactions:</strong> the shorter a transaction, the shorter the lock hold time, the lower the probability of deadlock.</li>
    </ul>
  </div>
</div>

<h3>Advisory Locks</h3>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔑</span><h3>Application-Level Mutex via PostgreSQL</h3><span class="tag tag-blue">DISTRIBUTED LOCKING</span></div>
  <div class="cp-body">
    <p>Advisory locks are arbitrary integer locks managed by the application — PostgreSQL doesn't tie them to any table row. Useful for distributed mutual exclusion (e.g., ensuring only one instance runs a cron job).</p>
    <div class="cb"><pre><span class="sql-cm">-- Acquire exclusive advisory lock (blocks if held by another session)</span>
<span class="sql-kw">SELECT</span> pg_advisory_lock(<span class="sql-num">12345</span>);

<span class="sql-cm">-- Non-blocking try: returns true/false</span>
<span class="sql-kw">SELECT</span> pg_try_advisory_lock(<span class="sql-num">12345</span>);

<span class="sql-cm">-- Transaction-scoped (auto-released on commit/rollback)</span>
<span class="sql-kw">SELECT</span> pg_advisory_xact_lock(<span class="sql-num">12345</span>);

<span class="sql-cm">-- Release session-scoped lock explicitly</span>
<span class="sql-kw">SELECT</span> pg_advisory_unlock(<span class="sql-num">12345</span>);</pre></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t6 C with libpq -->
<div id="t6" class="tab-pane">

<h3>Connecting to PostgreSQL with libpq</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;libpq-fe.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdlib.h&gt;</span>

<span class="cm">/* Compile: gcc db.c -lpq -o db
   Requires: libpq-dev package (apt install libpq-dev)  */</span>

PGconn *db_connect(<span class="ck">const char</span> *connstr) {
    PGconn *conn = PQconnectdb(connstr);
    <span class="ck">if</span> (PQstatus(conn) != CONNECTION_OK) {
        fprintf(stderr, <span class="cs">"Connection failed: %s\n"</span>, PQerrorMessage(conn));
        PQfinish(conn);
        <span class="ck">return</span> <span class="cs">NULL</span>;
    }
    <span class="ck">return</span> conn;
}

<span class="ck">int</span> main(<span class="ck">void</span>) {
    <span class="cm">/* Connection string: can also use env vars PGHOST, PGPORT, PGUSER etc */</span>
    PGconn *conn = db_connect(
        <span class="cs">"host=localhost port=5432 dbname=myapp user=myuser password=secret"</span>
    );
    <span class="ck">if</span> (!conn) <span class="ck">return</span> <span class="cv">1</span>;

    printf(<span class="cs">"Connected to PostgreSQL %s\n"</span>, PQparameterStatus(conn, <span class="cs">"server_version"</span>));
    PQfinish(conn);
    <span class="ck">return</span> <span class="cv">0</span>;
}</pre></div>

<h3>Prepared Statements (Parameterised Queries)</h3>
<div class="cb"><pre><span class="cm">/* Always use prepared statements — never string-concatenate user input */</span>

<span class="ck">int</span> get_user_by_id(PGconn *conn, <span class="ck">int</span> user_id) {
    <span class="cm">/* Prepare once, execute many times */</span>
    PGresult *prep = PQprepare(conn,
        <span class="cs">"get_user"</span>,                         <span class="cm">/* statement name */</span>
        <span class="cs">"SELECT id, name, email FROM users WHERE id = $1"</span>,
        <span class="cv">1</span>,                                   <span class="cm">/* number of params */</span>
        <span class="cs">NULL</span>                                 <span class="cm">/* param types (NULL = infer) */</span>
    );
    <span class="ck">if</span> (PQresultStatus(prep) != PGRES_COMMAND_OK) {
        fprintf(stderr, <span class="cs">"Prepare failed: %s\n"</span>, PQresultErrorMessage(prep));
        PQclear(prep);
        <span class="ck">return</span> -<span class="cv">1</span>;
    }
    PQclear(prep);

    <span class="cm">/* Execute: pass parameter as string (libpq converts) */</span>
    <span class="ck">char</span> id_str[<span class="cv">16</span>];
    snprintf(id_str, <span class="ck">sizeof</span>(id_str), <span class="cs">"%d"</span>, user_id);
    <span class="ck">const char</span> *params[] = { id_str };

    PGresult *res = PQexecPrepared(conn,
        <span class="cs">"get_user"</span>,   <span class="cm">/* statement name */</span>
        <span class="cv">1</span>,             <span class="cm">/* nParams */</span>
        params,        <span class="cm">/* paramValues */</span>
        <span class="cs">NULL</span>,          <span class="cm">/* paramLengths (NULL = text mode, use strlen) */</span>
        <span class="cs">NULL</span>,          <span class="cm">/* paramFormats (NULL = all text) */</span>
        <span class="cv">0</span>              <span class="cm">/* resultFormat: 0=text, 1=binary */</span>
    );

    <span class="ck">if</span> (PQresultStatus(res) != PGRES_TUPLES_OK) {
        fprintf(stderr, <span class="cs">"Query failed: %s\n"</span>, PQresultErrorMessage(res));
        PQclear(res);
        <span class="ck">return</span> -<span class="cv">1</span>;
    }

    <span class="ck">int</span> rows = PQntuples(res);
    <span class="ck">int</span> cols = PQnfields(res);
    printf(<span class="cs">"Got %d rows, %d cols\n"</span>, rows, cols);

    <span class="ck">for</span> (<span class="ck">int</span> r = <span class="cv">0</span>; r < rows; r++) {
        <span class="ck">for</span> (<span class="ck">int</span> c = <span class="cv">0</span>; c < cols; c++) {
            printf(<span class="cs">"  %s = %s\n"</span>,
                   PQfname(res, c),
                   PQgetisnull(res, r, c) ? <span class="cs">"(null)"</span> : PQgetvalue(res, r, c));
        }
    }

    PQclear(res);
    <span class="ck">return</span> rows;
}</pre></div>

<h3>Transactions in C</h3>
<div class="cb"><pre><span class="ck">int</span> transfer_funds(PGconn *conn, <span class="ck">int</span> from_id, <span class="ck">int</span> to_id, <span class="ck">int</span> amount_cents) {
    <span class="cm">/* BEGIN */</span>
    PGresult *r = PQexec(conn, <span class="cs">"BEGIN"</span>);
    <span class="ck">if</span> (PQresultStatus(r) != PGRES_COMMAND_OK) { PQclear(r); <span class="ck">return</span> -<span class="cv">1</span>; }
    PQclear(r);

    <span class="cm">/* Debit — lock the row first with FOR UPDATE */</span>
    <span class="ck">char</span> from_str[<span class="cv">16</span>], to_str[<span class="cv">16</span>], amt_str[<span class="cv">16</span>];
    snprintf(from_str, <span class="ck">sizeof</span>(from_str), <span class="cs">"%d"</span>, from_id);
    snprintf(to_str,   <span class="ck">sizeof</span>(to_str),   <span class="cs">"%d"</span>, to_id);
    snprintf(amt_str,  <span class="ck">sizeof</span>(amt_str),  <span class="cs">"%d"</span>, amount_cents);

    <span class="ck">const char</span> *debit_params[] = { amt_str, from_str };
    r = PQexecParams(conn,
        <span class="cs">"UPDATE accounts SET balance = balance - $1 WHERE id = $2 AND balance >= $1"</span>,
        <span class="cv">2</span>, <span class="cs">NULL</span>, debit_params, <span class="cs">NULL</span>, <span class="cs">NULL</span>, <span class="cv">0</span>);

    <span class="ck">if</span> (PQresultStatus(r) != PGRES_COMMAND_OK ||
        strcmp(PQcmdTuples(r), <span class="cs">"1"</span>) != <span class="cv">0</span>) {  <span class="cm">/* 0 rows = insufficient balance */</span>
        PQclear(r);
        PQexec(conn, <span class="cs">"ROLLBACK"</span>);
        <span class="ck">return</span> -<span class="cv">1</span>;
    }
    PQclear(r);

    <span class="cm">/* Credit */</span>
    <span class="ck">const char</span> *credit_params[] = { amt_str, to_str };
    r = PQexecParams(conn,
        <span class="cs">"UPDATE accounts SET balance = balance + $1 WHERE id = $2"</span>,
        <span class="cv">2</span>, <span class="cs">NULL</span>, credit_params, <span class="cs">NULL</span>, <span class="cs">NULL</span>, <span class="cv">0</span>);

    <span class="ck">if</span> (PQresultStatus(r) != PGRES_COMMAND_OK) {
        PQclear(r);
        PQexec(conn, <span class="cs">"ROLLBACK"</span>);
        <span class="ck">return</span> -<span class="cv">1</span>;
    }
    PQclear(r);

    <span class="cm">/* COMMIT */</span>
    r = PQexec(conn, <span class="cs">"COMMIT"</span>);
    <span class="ck">int</span> ok = PQresultStatus(r) == PGRES_COMMAND_OK;
    PQclear(r);
    <span class="ck">return</span> ok ? <span class="cv">0</span> : -<span class="cv">1</span>;
}</pre></div>

<h3>Minimal Connection Pool in C</h3>
<div class="cb"><pre><span class="cm">/* Production uses PgBouncer. This illustrates the concept. */</span>

<span class="ck">#define</span> POOL_SIZE <span class="cv">8</span>

<span class="ck">typedef struct</span> {
    PGconn  *conn;
    <span class="ck">int</span>      in_use;
    pthread_mutex_t lock;
} conn_slot_t;

<span class="ck">static</span> conn_slot_t pool[POOL_SIZE];
<span class="ck">static</span> pthread_mutex_t pool_lock = PTHREAD_MUTEX_INITIALIZER;

<span class="ck">void</span> pool_init(<span class="ck">const char</span> *connstr) {
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cv">0</span>; i < POOL_SIZE; i++) {
        pool[i].conn   = PQconnectdb(connstr);
        pool[i].in_use = <span class="cv">0</span>;
        pthread_mutex_init(&amp;pool[i].lock, <span class="cs">NULL</span>);
    }
}

PGconn *pool_acquire(<span class="ck">void</span>) {
    pthread_mutex_lock(&amp;pool_lock);
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cv">0</span>; i < POOL_SIZE; i++) {
        <span class="ck">if</span> (!pool[i].in_use &amp;&amp; PQstatus(pool[i].conn) == CONNECTION_OK) {
            pool[i].in_use = <span class="cv">1</span>;
            pthread_mutex_unlock(&amp;pool_lock);
            <span class="ck">return</span> pool[i].conn;
        }
    }
    pthread_mutex_unlock(&amp;pool_lock);
    <span class="ck">return</span> <span class="cs">NULL</span>;  <span class="cm">/* pool exhausted */</span>
}

<span class="ck">void</span> pool_release(PGconn *conn) {
    pthread_mutex_lock(&amp;pool_lock);
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cv">0</span>; i < POOL_SIZE; i++) {
        <span class="ck">if</span> (pool[i].conn == conn) {
            pool[i].in_use = <span class="cv">0</span>;
            <span class="ck">break</span>;
        }
    }
    pthread_mutex_unlock(&amp;pool_lock);
}</pre></div>

<div class="ins"><p><strong>In production:</strong> use <strong>PgBouncer</strong> (transaction-mode pooling) in front of PostgreSQL. It handles thousands of client connections multiplexed over a small number of server connections. Never create a new PGconn per request in a high-throughput server.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t7 Labs -->
<div id="t7" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 1 — Index Experiments on Real Data</h3>
    <span class="lab-tag">TOOLS: PostgreSQL · psql · pgbench</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Generate a large dataset and observe the before/after performance impact of indexes using EXPLAIN ANALYZE.</p>
    <div class="lab-step"><span class="sn">1</span><span>Create a test database and generate 1M rows: <br><code>createdb perflab</code><br><code>psql perflab -c "CREATE TABLE orders (id serial PRIMARY KEY, user_id int, status text, amount int, created_at timestamptz DEFAULT now());"</code><br><code>psql perflab -c "INSERT INTO orders (user_id, status, amount) SELECT (random()*10000)::int, (ARRAY['pending','complete','cancelled'])[ceil(random()*3)::int], (random()*10000)::int FROM generate_series(1,1000000);"</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span>Run a query without indexes and capture the plan: <br><code>EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE user_id = 42 AND status = 'pending';</code><br> Note: execution time, "Seq Scan", rows removed by filter.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Add an index and compare: <br><code>CREATE INDEX idx_orders_user_status ON orders(user_id, status);</code><br>Re-run the EXPLAIN. Note: execution time, node type change (Index Scan or Bitmap Index Scan), rows fetched.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Try the reverse column order: <code>CREATE INDEX idx_orders_status_user ON orders(status, user_id);</code>. Run <code>WHERE status = 'pending' AND user_id = 42</code>. Which index does the planner choose? Why?</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Test a partial index: <code>CREATE INDEX idx_orders_pending ON orders(user_id) WHERE status = 'pending';</code>. Compare plan for pending-only query vs a query across all statuses.</span></div>
    <div class="lab-step"><span class="sn">6</span><span>Find unused indexes: <code>SELECT indexrelname, idx_scan FROM pg_stat_user_indexes WHERE schemaname='public' ORDER BY idx_scan;</code>. Drop any with 0 scans.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 2 — Isolation Levels in Action</h3>
    <span class="lab-tag">TOOLS: PostgreSQL · two psql sessions</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Observe the difference between Read Committed and Repeatable Read isolation levels by running concurrent transactions in two terminal sessions.</p>
    <div class="lab-step"><span class="sn">1</span><span>Set up: <code>CREATE TABLE balances (id int PRIMARY KEY, amount int); INSERT INTO balances VALUES (1, 1000), (2, 500);</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span><strong>Non-repeatable read demo (Read Committed):</strong><br>
    Session A: <code>BEGIN; SELECT amount FROM balances WHERE id=1;</code> → 1000<br>
    Session B: <code>UPDATE balances SET amount=2000 WHERE id=1; COMMIT;</code><br>
    Session A: <code>SELECT amount FROM balances WHERE id=1;</code> → 2000 (changed!)<br>
    Session A: <code>ROLLBACK;</code></span></div>
    <div class="lab-step"><span class="sn">3</span><span><strong>Repeatable Read prevents this:</strong><br>
    Session A: <code>BEGIN ISOLATION LEVEL REPEATABLE READ; SELECT amount FROM balances WHERE id=1;</code> → 1000<br>
    Session B: <code>UPDATE balances SET amount=3000 WHERE id=1; COMMIT;</code><br>
    Session A: <code>SELECT amount FROM balances WHERE id=1;</code> → still 1000 (snapshot!)<br>
    Session A: <code>COMMIT;</code></span></div>
    <div class="lab-step"><span class="sn">4</span><span><strong>Deadlock simulation:</strong><br>
    Session A: <code>BEGIN; UPDATE balances SET amount=amount-100 WHERE id=1;</code><br>
    Session B: <code>BEGIN; UPDATE balances SET amount=amount-100 WHERE id=2;</code><br>
    Session A: <code>UPDATE balances SET amount=amount+100 WHERE id=2;</code> → waits<br>
    Session B: <code>UPDATE balances SET amount=amount+100 WHERE id=1;</code> → deadlock! One session gets: <code>ERROR: deadlock detected</code></span></div>
    <div class="lab-step"><span class="sn">5</span><span>Fix the deadlock: always update rows in a consistent order (lower id first). Rewrite both transactions to update id=1 before id=2. Verify no deadlock occurs.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 3 — libpq CRUD Application in C</h3>
    <span class="lab-tag">TOOLS: gcc · libpq-dev · PostgreSQL</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Build a command-line user management tool using libpq with prepared statements and transactions.</p>
    <div class="lab-step"><span class="sn">1</span><span>Create the schema: <code>CREATE TABLE users (id serial PRIMARY KEY, name text NOT NULL, email text UNIQUE NOT NULL, created_at timestamptz DEFAULT now());</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span>Write <code>users.c</code> using the libpq code from the Implementation tab. Implement: <code>user_create(conn, name, email)</code> → returns new id, <code>user_find(conn, id)</code> → prints user, <code>user_list(conn)</code> → prints all users.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Use <code>PQprepare</code> for all queries. Verify that SQL injection is not possible: try passing <code>name = "'; DROP TABLE users; --"</code> as the name parameter. The prepared statement should store it literally.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Implement <code>user_transfer_email(conn, from_id, to_id)</code> which copies the email from one user to another in a single transaction, verifying both users exist. Use <code>BEGIN</code> / <code>COMMIT</code> / <code>ROLLBACK</code> pattern.</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Add error handling: check <code>PQresultStatus</code> on every result. Handle <code>PGRES_FATAL_ERROR</code> (constraint violations like duplicate email) gracefully — print the error message, don't crash.</span></div>
    <div class="lab-step"><span class="sn">6</span><span><strong>Stretch:</strong> Implement the minimal connection pool from the Implementation tab. Run the tool from multiple threads simultaneously using <code>pthread_create</code>. Verify correctness under concurrent inserts.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 4 — Normalization Design Exercise</h3>
    <span class="lab-tag">TOOLS: pen &amp; paper · psql</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Take a denormalized flat table and normalize it to 3NF, then measure query performance before and after.</p>
    <div class="lab-step"><span class="sn">1</span><span>Start with this flat table: <code>CREATE TABLE flat_orders (order_id int, order_date date, customer_id int, customer_name text, customer_email text, customer_city text, product_id int, product_name text, product_category text, quantity int, unit_price numeric);</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span>Identify all functional dependencies. Which columns depend on <code>order_id</code>? On <code>customer_id</code>? On <code>product_id</code>? Map the violations of 2NF and 3NF.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Design the normalized schema: <code>customers</code>, <code>products</code>, <code>orders</code>, <code>order_items</code>. Write the <code>CREATE TABLE</code> statements with appropriate primary keys and foreign keys.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Generate 100k rows in the flat table and in the normalized schema. Write a JOIN query that produces the same output as <code>SELECT * FROM flat_orders</code>. Compare execution plans and times.</span></div>
    <div class="lab-step"><span class="sn">5</span><span><strong>Deliberate denormalization:</strong> Add a <code>total_amount</code> column to orders (computed as SUM of quantity × unit_price). Update it via a trigger. Measure query time for "get orders with total > 1000" with vs without the denormalized column.</span></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t8 Checklist -->
<div id="t8" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr"><span class="ico">✅</span><h3>Module Mastery Checklist</h3><span class="tag tag-violet">M06 COMPLETE</span></div>
  <div class="cp-body">
    <p>You have mastered this module when you can check off every item below without referring to notes.</p>
  </div>
</div>

<h3>SQL Internals</h3>
<ul class="cl">
  <li>Describe the 4 stages of SQL query execution in PostgreSQL (parse → rewrite → plan → execute)</li>
  <li>Explain what <code>pg_statistic</code> contains and why stale statistics cause bad query plans</li>
  <li>Explain MVCC: why readers don't block writers, and what VACUUM does</li>
</ul>

<h3>Indexes</h3>
<ul class="cl">
  <li>Describe the B-tree internal structure: root, inner pages, leaf pages, leaf page linked list, ctid pointers</li>
  <li>Explain why a B-tree lookup is O(log N) and state the typical depth for 1M rows</li>
  <li>Apply the left-prefix rule: given an index <code>(a, b, c)</code>, state which WHERE clauses can use it</li>
  <li>Explain why an equality column should come before a range column in a composite index</li>
  <li>Create a partial index and a functional (expression) index; state when each is appropriate</li>
  <li>State the write overhead of indexes and how to find unused indexes using <code>pg_stat_user_indexes</code></li>
  <li>Distinguish B-tree, Hash, GIN, and BRIN — name the use case each is best suited for</li>
</ul>

<h3>EXPLAIN</h3>
<ul class="cl">
  <li>Interpret an EXPLAIN output: identify seq scan vs index scan vs bitmap scan, explain cost fields, identify row count mismatch</li>
  <li>State 4 red flags in a query plan (seq scan on large table, estimate vs actual mismatch, nested loop with high loops, sort spill)</li>
  <li>Explain what <code>EXPLAIN (ANALYZE, BUFFERS)</code> adds over plain <code>EXPLAIN</code></li>
</ul>

<h3>Query Patterns</h3>
<ul class="cl">
  <li>Define the N+1 problem and write two solutions (JOIN and batch IN clause)</li>
  <li>State the difference between INNER, LEFT, FULL OUTER, and LATERAL JOIN</li>
  <li>Write a recursive CTE to traverse a parent-child hierarchy</li>
  <li>Use a window function to rank rows within a partition and compute a running total</li>
  <li>Write an UPSERT using <code>ON CONFLICT DO UPDATE</code></li>
</ul>

<h3>Normalization</h3>
<ul class="cl">
  <li>State the rules for 1NF, 2NF, 3NF, and BCNF; identify which normal form a given table violates</li>
  <li>Normalize a denormalized flat table to 3NF, producing correct FK relationships</li>
  <li>Name 3 deliberate denormalization patterns and the maintenance cost of each</li>
</ul>

<h3>ACID &amp; Isolation</h3>
<ul class="cl">
  <li>Define Atomicity, Consistency, Isolation, Durability — and state which mechanism implements each in PostgreSQL</li>
  <li>Define dirty read, non-repeatable read, phantom read, and serialisation anomaly</li>
  <li>State which read phenomena each isolation level prevents; name PostgreSQL's default isolation level</li>
  <li>Describe a deadlock scenario, how PostgreSQL detects it, and two prevention strategies</li>
  <li>Write a fund transfer in C using libpq with correct BEGIN/COMMIT/ROLLBACK error handling</li>
  <li>Explain advisory locks and give one production use case</li>
</ul>

<h3>C / libpq</h3>
<ul class="cl">
  <li>Write a libpq connection, prepared statement, and parameterised execution in C</li>
  <li>Handle <code>PQresultStatus</code> correctly for all result types (TUPLES_OK, COMMAND_OK, FATAL_ERROR)</li>
  <li>Explain why PgBouncer is needed in production rather than creating a new PGconn per request</li>
</ul>

<hr class="sep">
<div class="ins"><p><strong>Next in Phase 2:</strong> M07 covers Transactions & MVCC in depth (savepoints, advisory locks, SKIP LOCKED job queues) and M08 covers NoSQL & Redis (when to reach for a non-relational store and how to use it alongside PostgreSQL).</p></div>

</div>

<!-- Module Nav -->
<div class="mod-nav">
  <a href="{{ '/learning/backend/m03-rest/' | relative_url }}" class="nb">← M03 REST Design</a>
  <span style="font-size:.8rem;color:var(--text-color,#888);font-family:monospace">Phase 2 · Module 6 of 3</span>
  <a href="{{ '/learning/backend/backend-roadmap/' | relative_url }}" class="nb">↑ Roadmap</a>
</div>

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
