---
layout: learning
title: "M07 — NoSQL: Redis, MongoDB & Cassandra"
description: "NoSQL taxonomy and tradeoffs, Redis data structures with complexity guarantees, caching patterns, persistence, pub/sub, Lua scripting, rate limiting, MongoDB aggregation pipeline, Cassandra data modeling, and hiredis in C."
---

<style>
/* ── Module shell ───────────────────────────────────────────── */
.mod-header{background:linear-gradient(135deg,#1e1b4b 0%,#2e1065 100%);color:#fff;
  padding:2.4rem 2rem 2rem;border-radius:14px;margin-bottom:1.6rem;
  border-left:5px solid #8b5cf6;}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;}
.mod-header p{margin:0;opacity:.85;font-size:.97rem;}
.mod-badge{display:inline-block;background:rgba(139,92,246,.35);
  border:1px solid #8b5cf6;border-radius:20px;padding:.2rem .75rem;
  font-size:.78rem;margin:.5rem .3rem 0 0;}

/* ── Tabs ───────────────────────────────────────────────────── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.2rem;}
.tab-btn{padding:.45rem 1rem;border:2px solid #8b5cf6;border-radius:20px;
  background:transparent;color:#8b5cf6;cursor:pointer;font-size:.85rem;
  transition:all .2s;}
.tab-btn.active{background:linear-gradient(135deg,#8b5cf6,#a855f7);
  color:#fff;border-color:transparent;}
.tab-pane{display:none;}.tab-pane.active{display:block;}

/* ── Panels ─────────────────────────────────────────────────── */
.cp{border-radius:10px;margin-bottom:1.2rem;overflow:hidden;}
.cp-hdr{padding:.7rem 1.1rem;font-weight:700;font-size:.92rem;display:flex;align-items:center;gap:.5rem;}
.cp-body{padding:1rem 1.2rem;}
.p-violet{border:1px solid #8b5cf6;}.p-violet .cp-hdr{background:#ede9fe;color:#5b21b6;}
.p-purple{border:1px solid #a855f7;}.p-purple .cp-hdr{background:#f3e8ff;color:#7e22ce;}
.p-blue{border:1px solid #3b82f6;}.p-blue .cp-hdr{background:#eff6ff;color:#1e40af;}
.p-indigo{border:1px solid #6366f1;}.p-indigo .cp-hdr{background:#eef2ff;color:#3730a3;}
.p-green{border:1px solid #22c55e;}.p-green .cp-hdr{background:#f0fdf4;color:#166534;}
.p-orange{border:1px solid #f97316;}.p-orange .cp-hdr{background:#fff7ed;color:#9a3412;}
.p-red{border:1px solid #ef4444;}.p-red .cp-hdr{background:#fef2f2;color:#991b1b;}
.p-teal{border:1px solid #14b8a6;}.p-teal .cp-hdr{background:#f0fdfa;color:#134e4a;}
.p-amber{border:1px solid #f59e0b;}.p-amber .cp-hdr{background:#fffbeb;color:#92400e;}
.p-cyan{border:1px solid #06b6d4;}.p-cyan .cp-hdr{background:#ecfeff;color:#164e63;}
.p-slate{border:1px solid #64748b;}.p-slate .cp-hdr{background:#f8fafc;color:#1e293b;}

/* ── Callouts ───────────────────────────────────────────────── */
.ins{background:#f0fdf4;border-left:4px solid #22c55e;padding:.8rem 1rem;border-radius:6px;margin:.8rem 0;}
.warn{background:#fff7ed;border-left:4px solid #f97316;padding:.8rem 1rem;border-radius:6px;margin:.8rem 0;}
.note{background:#eff6ff;border-left:4px solid #3b82f6;padding:.8rem 1rem;border-radius:6px;margin:.8rem 0;}
.analogy{background:#fdf4ff;border-left:4px solid #c026d3;padding:.8rem 1rem;border-radius:6px;margin:.8rem 0;}

/* ── Code blocks ────────────────────────────────────────────── */
.cb{background:#0f172a;color:#e2e8f0;border-radius:8px;padding:1.1rem 1.3rem;
  overflow-x:auto;font-size:.83rem;line-height:1.6;margin:.6rem 0;}
.cm{color:#64748b;font-style:italic;} /* comment */
.ck{color:#f472b6;}                   /* keyword */
.cv{color:#38bdf8;}                   /* variable / identifier */
.cs{color:#a3e635;}                   /* string */
.cn{color:#fb923c;}                   /* number / constant */
.cf{color:#facc15;}                   /* function */
.co{color:#c084fc;}                   /* operator / punctuation */
.cg{color:#34d399;}                   /* type / generic */

/* ── Tables ─────────────────────────────────────────────────── */
.t-table{width:100%;border-collapse:collapse;font-size:.88rem;margin:.6rem 0;}
.t-table th{background:#ede9fe;color:#4c1d95;padding:.55rem .8rem;text-align:left;border-bottom:2px solid #8b5cf6;}
.t-table td{padding:.5rem .8rem;border-bottom:1px solid #e5e7eb;vertical-align:top;}
.t-table tr:last-child td{border-bottom:none;}
.t-table tr:nth-child(even) td{background:#faf5ff;}

/* ── Flow list ──────────────────────────────────────────────── */
.flow-list{list-style:none;padding:0;margin:.6rem 0;}
.fl-step{display:flex;gap:.8rem;align-items:flex-start;margin-bottom:.7rem;}
.fl-num{background:linear-gradient(135deg,#8b5cf6,#a855f7);color:#fff;border-radius:50%;
  min-width:1.7rem;height:1.7rem;display:flex;align-items:center;justify-content:center;
  font-weight:700;font-size:.8rem;}

/* ── Two-col ────────────────────────────────────────────────── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.6rem 0;}
@media(max-width:640px){.two-col{grid-template-columns:1fr;}}

/* ── Lab box ────────────────────────────────────────────────── */
.lab-box{border:2px solid #8b5cf6;border-radius:10px;margin-bottom:1.2rem;overflow:hidden;}
.lab-hdr{background:linear-gradient(135deg,#8b5cf6,#a855f7);color:#fff;padding:.7rem 1.1rem;font-weight:700;}
.lab-body{padding:1rem 1.2rem;}
.lab-step{display:flex;gap:.7rem;margin-bottom:.5rem;align-items:flex-start;}
.sn{background:#8b5cf6;color:#fff;border-radius:50%;min-width:1.5rem;height:1.5rem;
  display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;}

/* ── Checklist ──────────────────────────────────────────────── */
.cl{list-style:none;padding:0;}
.cl li{padding:.35rem 0;border-bottom:1px solid #f3f4f6;display:flex;gap:.6rem;align-items:flex-start;}
.cl li:last-child{border-bottom:none;}
.cl li::before{content:"☐";color:#8b5cf6;font-size:1.1rem;line-height:1.2;}

/* ── Nav ────────────────────────────────────────────────────── */
.mod-nav{display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem;
  margin-top:2rem;padding-top:1rem;border-top:1px solid #e5e7eb;}
.nb{background:#8b5cf6;color:#fff;padding:.5rem 1.1rem;border-radius:20px;
  text-decoration:none;font-size:.87rem;font-weight:600;}
.nb:hover{background:#7c3aed;}

/* ── Diagram ────────────────────────────────────────────────── */
.diagram-box{background:#1e1b4b;color:#c4b5fd;border-radius:8px;padding:1.1rem 1.3rem;
  font-family:monospace;font-size:.82rem;line-height:1.7;overflow-x:auto;margin:.6rem 0;}

.sep{border:none;border-top:1px solid #e5e7eb;margin:1.2rem 0;}
</style>

<div class="mod-header">
  <h1>M07 — NoSQL: Redis, MongoDB &amp; Cassandra</h1>
  <p>NoSQL taxonomy, Redis data structures with complexity guarantees, caching patterns, persistence &amp; pub/sub, Lua scripting, rate limiting, MongoDB aggregation pipeline, Cassandra data modeling by access pattern, and hiredis in C.</p>
  <span class="mod-badge">Phase 2 — Databases &amp; Storage</span>
  <span class="mod-badge">~5 hrs</span>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('redis-fundamentals',this)">Redis Fundamentals</button>
  <button class="tab-btn" onclick="vt('caching',this)">Caching Patterns</button>
  <button class="tab-btn" onclick="vt('redis-advanced',this)">Redis Advanced</button>
  <button class="tab-btn" onclick="vt('mongodb',this)">MongoDB</button>
  <button class="tab-btn" onclick="vt('cassandra',this)">Cassandra</button>
  <button class="tab-btn" onclick="vt('c-hiredis',this)">C &amp; hiredis</button>
  <button class="tab-btn" onclick="vt('labs',this)">Labs &amp; Checklist</button>
</div>

<!-- ═══════════════════════════════════════════════════════════ TAB 1: OVERVIEW -->
<div id="tab-overview" class="tab-pane active">

<div class="cp p-violet">
  <div class="cp-hdr">🗺️ NoSQL Taxonomy — When to Choose What</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Category</th><th>Model</th><th>Flagship</th><th>Strength</th><th>Weakness</th><th>Sweet Spot</th></tr></thead>
<tbody>
<tr><td><strong>Key-Value</strong></td><td>Hash map</td><td>Redis, DynamoDB</td><td>Sub-ms reads; simple</td><td>No relational query</td><td>Sessions, caches, counters</td></tr>
<tr><td><strong>Document</strong></td><td>JSON/BSON tree</td><td>MongoDB, Couchbase</td><td>Flexible schema; rich queries</td><td>Multi-doc transactions costly</td><td>Catalogs, user profiles, CMS</td></tr>
<tr><td><strong>Wide-Column</strong></td><td>Partition → rows</td><td>Cassandra, HBase</td><td>Write-optimized; linear scale</td><td>Query-driven design required</td><td>Time-series, IoT, activity feeds</td></tr>
<tr><td><strong>Graph</strong></td><td>Vertices + edges</td><td>Neo4j, Amazon Neptune</td><td>Relationship traversal</td><td>Doesn't scale as wide</td><td>Social graphs, recommendations</td></tr>
<tr><td><strong>Time-Series</strong></td><td>Timestamped metrics</td><td>InfluxDB, TimescaleDB</td><td>Compression, retention policies</td><td>Poor ad-hoc relational queries</td><td>Monitoring, telemetry</td></tr>
</tbody>
</table>

  </div>
</div>

<div class="cp p-indigo">
  <div class="cp-hdr">⚖️ CAP Theorem — The Impossibility Triangle</div>
  <div class="cp-body">
<p>In a network partition you must choose between <strong>Consistency</strong> and <strong>Availability</strong>. You can never have all three simultaneously.</p>

<div class="diagram-box">
<pre>
          Consistency
          (every read sees
           latest write)
              /\
             /  \
            /    \
           /  CA  \        ← no real-world distributed system
          /--------\
         / CP  | AP \
        /      |     \
Partition ─────────── Availability
Tolerance              (always responds,
(nodes can             may be stale)
 fail/split)

CP examples: HBase, Zookeeper, Redis Cluster (default)
AP examples: Cassandra (tunable), DynamoDB, CouchDB
CA example:  Single-node PostgreSQL (no partition tolerance)
</pre>
  </div>

<div class="warn"><strong>PACELC extension:</strong> Even without a partition (P), there is a latency (L) vs consistency (C) tradeoff. Cassandra lets you tune this per-query with consistency levels (ONE → QUORUM → ALL).</div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔄 SQL vs NoSQL — Decision Checklist</div>
  <div class="cp-body">

<div class="two-col">
<div>
<strong>Choose SQL when:</strong>
<ul>
  <li>Data is naturally relational with many joins</li>
  <li>ACID transactions across multiple entities are required</li>
  <li>Schema is stable and well-understood</li>
  <li>Complex ad-hoc reporting or analytics</li>
  <li>Team is familiar with SQL tooling</li>
</ul>
</div>
<div>
<strong>Choose NoSQL when:</strong>
<ul>
  <li>Access pattern is known and narrow (read by key)</li>
  <li>Horizontal scale > vertical scale (write throughput)</li>
  <li>Schema evolves rapidly (document stores)</li>
  <li>Geo-distributed with tunable consistency</li>
  <li>Specific data model fits: graph, time-series, cache</li>
</ul>
</div>
</div>

<div class="analogy"><strong>Analogy:</strong> SQL is a Swiss Army knife — powerful for unknown problems. NoSQL tools are surgical instruments — each optimized for one job. Use the right tool.</div>
  </div>
</div>

</div><!-- /tab-overview -->

<!-- ═══════════════════════════════════════════════════════════ TAB 2: REDIS FUNDAMENTALS -->
<div id="tab-redis-fundamentals" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">🏗️ Redis Architecture — Single-Threaded Event Loop</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Client 1 ──┐
Client 2 ──┤   TCP socket   ┌─────────────────────────────────┐
Client 3 ──┼───────────────►│  I/O Multiplexer (epoll/kqueue) │
   ...      │               │  ─────────────────────────────  │
            └───────────────►│  Command Queue (FIFO)           │
                            │  ─────────────────────────────  │
                            │  Single Worker Thread            │
                            │    executes commands serially    │
                            │    → no locking needed          │
                            │  ─────────────────────────────  │
                            │  In-Memory Data Structures       │
                            │  (dict, quicklist, listpack,    │
                            │   skiplist, rax, stream)         │
                            └─────────────────────────────────┘
                                        │
                                  Background threads:
                                  • AOF fsync
                                  • RDB fork + write
                                  • Lazy free (UNLINK)
</pre>
  </div>
<div class="note">Because the main thread is single-threaded, a slow command (e.g., <code>KEYS *</code> on a large dataset) blocks all other clients. Never run <code>KEYS</code> in production — use <code>SCAN</code> with a cursor instead.</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📦 Data Structures — Commands &amp; Complexity</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Type</th><th>Key Commands</th><th>Complexity</th><th>Internal Encoding</th><th>Use Case</th></tr></thead>
<tbody>
<tr>
  <td><strong>String</strong></td>
  <td><code>SET/GET</code>, <code>INCR</code>, <code>MSET/MGET</code>, <code>SETNX</code>, <code>SETEX</code></td>
  <td>O(1)</td>
  <td>SDS (simple dynamic string)</td>
  <td>Counters, cache values, distributed lock tokens</td>
</tr>
<tr>
  <td><strong>Hash</strong></td>
  <td><code>HSET/HGET</code>, <code>HMSET</code>, <code>HGETALL</code>, <code>HINCRBY</code>, <code>HDEL</code></td>
  <td>O(1) field ops; O(n) HGETALL</td>
  <td>listpack (small) → dict (large)</td>
  <td>User profile fields, config objects</td>
</tr>
<tr>
  <td><strong>List</strong></td>
  <td><code>LPUSH/RPUSH</code>, <code>LPOP/RPOP</code>, <code>LRANGE</code>, <code>BLPOP</code></td>
  <td>O(1) push/pop; O(n) LRANGE</td>
  <td>listpack (small) → quicklist</td>
  <td>Task queues, recent activity feeds</td>
</tr>
<tr>
  <td><strong>Set</strong></td>
  <td><code>SADD/SREM</code>, <code>SISMEMBER</code>, <code>SUNION/SINTER/SDIFF</code></td>
  <td>O(1) SADD/SREM; O(n) SUNION</td>
  <td>listpack (small) → intset → dict</td>
  <td>Unique visitors, tags, friend lists</td>
</tr>
<tr>
  <td><strong>Sorted Set</strong></td>
  <td><code>ZADD</code>, <code>ZRANGE</code>, <code>ZRANGEBYSCORE</code>, <code>ZRANK</code>, <code>ZINCRBY</code></td>
  <td>O(log n) ZADD/ZRANK; O(log n + m) ZRANGE</td>
  <td>listpack (small) → skiplist + dict</td>
  <td>Leaderboards, delayed job queues, rate limiting windows</td>
</tr>
<tr>
  <td><strong>Stream</strong></td>
  <td><code>XADD</code>, <code>XREAD</code>, <code>XRANGE</code>, <code>XGROUP CREATE</code>, <code>XACK</code></td>
  <td>O(1) XADD; O(n) XRANGE</td>
  <td>listpack + rax (radix tree)</td>
  <td>Event log, message bus, audit trail</td>
</tr>
<tr>
  <td><strong>Bitmap</strong></td>
  <td><code>SETBIT/GETBIT</code>, <code>BITCOUNT</code>, <code>BITOP</code></td>
  <td>O(1) SETBIT; O(n) BITCOUNT</td>
  <td>String (bit-addressed)</td>
  <td>Feature flags, daily active user tracking</td>
</tr>
<tr>
  <td><strong>HyperLogLog</strong></td>
  <td><code>PFADD</code>, <code>PFCOUNT</code>, <code>PFMERGE</code></td>
  <td>O(1), uses ~12KB max</td>
  <td>Probabilistic sketch</td>
  <td>Unique count estimates (± 0.81% error)</td>
</tr>
</tbody>
</table>

  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔑 Key Patterns &amp; Naming Conventions</div>
  <div class="cp-body">

<div class="cb"><span class="cm"># Naming: use colon-separated namespaces</span>
<span class="cv">user</span><span class="co">:</span><span class="cn">42</span><span class="co">:</span><span class="cv">profile</span>          <span class="cm"># Hash — user 42's profile fields</span>
<span class="cv">session</span><span class="co">:</span><span class="cs">abc123</span>          <span class="cm"># String — session token → user_id mapping</span>
<span class="cv">post</span><span class="co">:</span><span class="cn">7</span><span class="co">:</span><span class="cv">views</span>              <span class="cm"># String — view counter for post 7</span>
<span class="cv">leaderboard</span><span class="co">:</span><span class="cs">"2026-03"</span>  <span class="cm"># Sorted Set — monthly leaderboard</span>
<span class="cv">queue</span><span class="co">:</span><span class="cv">email</span>              <span class="cm"># List — email job queue</span>

<span class="cm"># Setting a value with TTL (session expires in 30 min)</span>
<span class="ck">SET</span> <span class="cv">session</span><span class="co">:</span><span class="cs">abc123</span> <span class="cn">42</span> <span class="ck">EX</span> <span class="cn">1800</span>

<span class="cm"># Atomic increment — safe without transactions</span>
<span class="ck">INCR</span> <span class="cv">post</span><span class="co">:</span><span class="cn">7</span><span class="co">:</span><span class="cv">views</span>          <span class="cm"># returns new value, atomic</span>

<span class="cm"># Hash — store object fields separately (partial updates)</span>
<span class="ck">HSET</span> <span class="cv">user</span><span class="co">:</span><span class="cn">42</span><span class="co">:</span><span class="cv">profile</span>  name <span class="cs">"Alice"</span>  email <span class="cs">"alice@example.com"</span>  age <span class="cn">28</span>
<span class="ck">HGET</span> <span class="cv">user</span><span class="co">:</span><span class="cn">42</span><span class="co">:</span><span class="cv">profile</span>  name       <span class="cm"># → "Alice"</span>
<span class="ck">HINCRBY</span> <span class="cv">user</span><span class="co">:</span><span class="cn">42</span><span class="co">:</span><span class="cv">profile</span>  age  <span class="cn">1</span>   <span class="cm"># happy birthday — no read-modify-write</span>

<span class="cm"># Sorted set leaderboard</span>
<span class="ck">ZADD</span> <span class="cv">leaderboard</span><span class="co">:</span><span class="cs">"2026-03"</span>  <span class="cn">1500</span>  <span class="cs">"alice"</span>
<span class="ck">ZADD</span> <span class="cv">leaderboard</span><span class="co">:</span><span class="cs">"2026-03"</span>  <span class="cn">2200</span>  <span class="cs">"bob"</span>
<span class="ck">ZRANGE</span> <span class="cv">leaderboard</span><span class="co">:</span><span class="cs">"2026-03"</span>  <span class="cn">0</span>  <span class="cn">-1</span>  <span class="ck">REV WITHSCORES</span>
<span class="cm"># → [bob 2200, alice 1500]  (descending)</span></div>

<div class="warn"><strong>Key expiry gotcha:</strong> Redis TTL applies to the top-level key, not fields. If you store user fields in <code>user:42:profile</code> hash, setting TTL on the hash expires ALL fields at once. There is no per-field TTL.</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🚫 Commands to Avoid in Production</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Dangerous Command</th><th>Why Dangerous</th><th>Safe Alternative</th></tr></thead>
<tbody>
<tr><td><code>KEYS pattern</code></td><td>O(n) — scans all keys; blocks event loop</td><td><code>SCAN 0 MATCH pattern COUNT 100</code></td></tr>
<tr><td><code>FLUSHALL</code></td><td>Deletes every key in all databases</td><td><code>SCAN</code> + targeted <code>DEL</code>; or <code>FLUSHDB ASYNC</code></td></tr>
<tr><td><code>DEBUG SLEEP</code></td><td>Explicitly blocks the server</td><td>Never in production</td></tr>
<tr><td><code>DEL big-key</code></td><td>O(n) — synchronous deletion blocks loop</td><td><code>UNLINK big-key</code> (async lazy-free)</td></tr>
<tr><td><code>LRANGE 0 -1</code> on huge list</td><td>Transfers entire list over network</td><td>Paginate with <code>LRANGE 0 99</code>, then next page</td></tr>
<tr><td><code>SMEMBERS big-set</code></td><td>O(n) — returns all members</td><td><code>SSCAN</code> with cursor</td></tr>
</tbody>
</table>

  </div>
</div>

</div><!-- /tab-redis-fundamentals -->

<!-- ═══════════════════════════════════════════════════════════ TAB 3: CACHING PATTERNS -->
<div id="tab-caching" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">🔄 Cache-Aside (Lazy Loading) — Most Common Pattern</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Application                   Cache (Redis)           Database
     │                              │                     │
     │──── GET user:42 ────────────►│                     │
     │                              │ MISS                │
     │◄─── nil ─────────────────────│                     │
     │                              │                     │
     │──── SELECT * FROM users ───────────────────────────►│
     │◄─── row {id:42, name:...} ──────────────────────────│
     │                              │                     │
     │──── SET user:42 ... EX 300 ─►│                     │
     │                              │ stored              │
     │  (later)                     │                     │
     │──── GET user:42 ────────────►│                     │
     │◄─── {id:42, name:...} ───────│   HIT — no DB call  │
</pre>
  </div>

<div class="cb"><span class="cm">// Node.js pseudo-code</span>
<span class="ck">async function</span> <span class="cf">getUser</span>(<span class="cv">userId</span>) {
  <span class="ck">const</span> <span class="cv">key</span> = <span class="cs">`user:<span class="co">${</span><span class="cv">userId</span><span class="co">}</span>`</span>;
  <span class="ck">const</span> <span class="cv">cached</span> = <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">get</span>(<span class="cv">key</span>);
  <span class="ck">if</span> (<span class="cv">cached</span>) <span class="ck">return</span> <span class="cv">JSON</span>.<span class="cf">parse</span>(<span class="cv">cached</span>);

  <span class="ck">const</span> <span class="cv">user</span> = <span class="ck">await</span> <span class="cv">db</span>.<span class="cf">query</span>(<span class="cs">'SELECT * FROM users WHERE id = $1'</span>, [<span class="cv">userId</span>]);
  <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">set</span>(<span class="cv">key</span>, <span class="cv">JSON</span>.<span class="cf">stringify</span>(<span class="cv">user</span>), <span class="cs">'EX'</span>, <span class="cn">300</span>); <span class="cm">// TTL 5 min</span>
  <span class="ck">return</span> <span class="cv">user</span>;
}

<span class="cm">// On update: invalidate the cache</span>
<span class="ck">async function</span> <span class="cf">updateUser</span>(<span class="cv">userId</span>, <span class="cv">data</span>) {
  <span class="ck">await</span> <span class="cv">db</span>.<span class="cf">query</span>(<span class="cs">'UPDATE users SET name=$1 WHERE id=$2'</span>, [<span class="cv">data</span>.<span class="cv">name</span>, <span class="cv">userId</span>]);
  <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">del</span>(<span class="cs">`user:<span class="co">${</span><span class="cv">userId</span><span class="co">}</span>`</span>); <span class="cm">// evict stale entry</span>
}</div>

  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📊 All Four Caching Patterns Compared</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Pattern</th><th>Who Manages Cache</th><th>On Read Miss</th><th>On Write</th><th>Consistency</th><th>Best For</th></tr></thead>
<tbody>
<tr>
  <td><strong>Cache-Aside</strong></td>
  <td>Application</td>
  <td>App reads DB, populates cache</td>
  <td>App updates DB, deletes/updates cache</td>
  <td>Eventual (TTL-bounded)</td>
  <td>General-purpose, read-heavy</td>
</tr>
<tr>
  <td><strong>Read-Through</strong></td>
  <td>Cache library/proxy</td>
  <td>Cache fetches from DB automatically</td>
  <td>App writes to cache; cache syncs DB</td>
  <td>Eventual</td>
  <td>When you can plug in a cache provider</td>
</tr>
<tr>
  <td><strong>Write-Through</strong></td>
  <td>Cache library/proxy</td>
  <td>Cache fetches from DB</td>
  <td>Write to cache AND DB synchronously</td>
  <td>Strong (but higher write latency)</td>
  <td>Read-heavy, strong consistency needed</td>
</tr>
<tr>
  <td><strong>Write-Behind</strong></td>
  <td>Cache library/proxy</td>
  <td>Cache fetches from DB</td>
  <td>Write to cache only; async flush to DB</td>
  <td>Weak (data loss risk on crash)</td>
  <td>Write-heavy, can tolerate brief loss</td>
</tr>
</tbody>
</table>

  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🗑️ Eviction Policies — What Happens When Memory Is Full</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Policy</th><th>Behavior</th><th>When to Use</th></tr></thead>
<tbody>
<tr><td><code>noeviction</code></td><td>Return error on write when memory full</td><td>When data loss is unacceptable (primary store)</td></tr>
<tr><td><code>allkeys-lru</code></td><td>Evict least-recently-used key across all keys</td><td>General cache — frequently accessed items stay hot</td></tr>
<tr><td><code>volatile-lru</code></td><td>Evict LRU key only from keys with TTL set</td><td>Mix of persistent + cached keys in same instance</td></tr>
<tr><td><code>allkeys-lfu</code></td><td>Evict least-frequently-used (Redis 4+)</td><td>Better than LRU for skewed access distributions</td></tr>
<tr><td><code>volatile-ttl</code></td><td>Evict key with shortest remaining TTL first</td><td>When shorter-lived items are more "disposable"</td></tr>
<tr><td><code>allkeys-random</code></td><td>Evict random key — no intelligence</td><td>Uniform access patterns (rare)</td></tr>
</tbody>
</table>

<div class="cb"><span class="cm"># redis.conf</span>
maxmemory <span class="cn">2gb</span>
maxmemory-policy <span class="cv">allkeys-lru</span></div>

  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">⚠️ Cache Stampede (Thundering Herd) &amp; Fixes</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Scenario: popular cache key expires at T=0

T=0:  100 requests hit cache → all MISS
      → all 100 simultaneously query DB
      → DB overwhelmed, latency spikes

Fix 1: Probabilistic early re-computation
  When remaining TTL < threshold: randomly re-cache
  → one request re-caches while others still get old value

Fix 2: Lock / Mutex (Redis SET NX)
  First miss acquires distributed lock → fetches DB
  Others wait → then all read from cache (or retry)

Fix 3: Background refresh
  Scheduled job refreshes cache before TTL expires
  → cache never actually empty for popular keys
</pre>
  </div>

<div class="cb"><span class="cm">// Redis distributed lock for cache stampede prevention</span>
<span class="ck">const</span> <span class="cv">lockKey</span> = <span class="cs">`lock:user:<span class="co">${</span><span class="cv">userId</span><span class="co">}</span>`</span>;
<span class="ck">const</span> <span class="cv">token</span>   = <span class="cv">crypto</span>.<span class="cf">randomUUID</span>();

<span class="cm">// SET NX EX — atomic: only succeeds if key doesn't exist</span>
<span class="ck">const</span> <span class="cv">acquired</span> = <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">set</span>(<span class="cv">lockKey</span>, <span class="cv">token</span>, <span class="cs">'NX'</span>, <span class="cs">'EX'</span>, <span class="cn">5</span>);
<span class="ck">if</span> (<span class="cv">acquired</span>) {
  <span class="ck">const</span> <span class="cv">user</span> = <span class="ck">await</span> <span class="cv">db</span>.<span class="cf">fetchUser</span>(<span class="cv">userId</span>);
  <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">set</span>(<span class="cs">`user:<span class="co">${</span><span class="cv">userId</span><span class="co">}</span>`</span>, <span class="cv">JSON</span>.<span class="cf">stringify</span>(<span class="cv">user</span>), <span class="cs">'EX'</span>, <span class="cn">300</span>);
  <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">del</span>(<span class="cv">lockKey</span>);   <span class="cm">// release lock</span>
} <span class="ck">else</span> {
  <span class="cm">// Another request is fetching — wait & retry</span>
  <span class="ck">await</span> <span class="cf">sleep</span>(<span class="cn">50</span>);
  <span class="ck">return</span> <span class="cf">getUser</span>(<span class="cv">userId</span>);    <span class="cm">// retry</span>
}</div>

  </div>
</div>

</div><!-- /tab-caching -->

<!-- ═══════════════════════════════════════════════════════════ TAB 4: REDIS ADVANCED -->
<div id="tab-redis-advanced" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">💾 Persistence — RDB vs AOF</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th></th><th>RDB (Redis Database)</th><th>AOF (Append-Only File)</th></tr></thead>
<tbody>
<tr><td><strong>Mechanism</strong></td><td>Periodic fork + full memory snapshot to <code>.rdb</code> file</td><td>Log every write command; replay on restart</td></tr>
<tr><td><strong>Trigger</strong></td><td><code>save 900 1</code> (after 1 change in 15 min), <code>BGSAVE</code></td><td>Every write; fsync configurable</td></tr>
<tr><td><strong>Restart speed</strong></td><td>Fast (load binary snapshot)</td><td>Slow if AOF is huge (replay all commands)</td></tr>
<tr><td><strong>Data loss risk</strong></td><td>Up to snapshot interval (minutes)</td><td>Up to 1 second (<code>appendfsync everysec</code>)</td></tr>
<tr><td><strong>File size</strong></td><td>Compact binary</td><td>Grows; periodically compacted with <code>BGREWRITEAOF</code></td></tr>
<tr><td><strong>Production rec.</strong></td><td>Use for backups / fast restarts</td><td>Use for durability (near-zero data loss)</td></tr>
</tbody>
</table>

<div class="ins"><strong>Best practice:</strong> Run both. RDB for point-in-time backups; AOF with <code>appendfsync everysec</code> for durability. Redis docs call this "the best of both worlds."</div>

<div class="cb"><span class="cm"># redis.conf — recommended production settings</span>
<span class="cm"># RDB</span>
save <span class="cn">900 1</span>       <span class="cm"># snapshot if ≥1 change in 900s</span>
save <span class="cn">300 10</span>      <span class="cm"># snapshot if ≥10 changes in 300s</span>
save <span class="cn">60  10000</span>   <span class="cm"># snapshot if ≥10000 changes in 60s</span>

<span class="cm"># AOF</span>
appendonly <span class="cv">yes</span>
appendfsync <span class="cv">everysec</span>       <span class="cm"># balance: 1s max loss</span>
auto-aof-rewrite-percentage <span class="cn">100</span>  <span class="cm"># rewrite when AOF doubles</span>
auto-aof-rewrite-min-size  <span class="cn">64mb</span></div>

  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📢 Pub/Sub — Fire-and-Forget Messaging</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Publisher                    Redis                     Subscribers
    │                          │                           │
    │── PUBLISH notifications  │                           │
    │   "{"type":"like",...}" ─►│                           │
    │                          │──► "{"type":"like",...}" ─►│ Sub A
    │                          │──► "{"type":"like",...}" ─►│ Sub B
    │                          │                           │
    │ (publisher doesn't know  │ (no message persistence   │
    │  who is subscribed)      │  — if sub is offline,     │
    │                          │  message is LOST)         │
</pre>
  </div>

<div class="cb"><span class="cm">// Publisher (Node.js)</span>
<span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">publish</span>(<span class="cs">'notifications'</span>, <span class="cv">JSON</span>.<span class="cf">stringify</span>({ type: <span class="cs">'like'</span>, postId: <span class="cn">7</span>, userId: <span class="cn">42</span> }));

<span class="cm">// Subscriber (must use a separate connection — SUBSCRIBE blocks it)</span>
<span class="ck">const</span> <span class="cv">sub</span> = <span class="cv">redis</span>.<span class="cf">duplicate</span>();
<span class="ck">await</span> <span class="cv">sub</span>.<span class="cf">subscribe</span>(<span class="cs">'notifications'</span>, (<span class="cv">message</span>) => {
  <span class="ck">const</span> <span class="cv">event</span> = <span class="cv">JSON</span>.<span class="cf">parse</span>(<span class="cv">message</span>);
  <span class="cv">console</span>.<span class="cf">log</span>(<span class="cs">'Received:'</span>, <span class="cv">event</span>);
});</div>

<div class="warn"><strong>Pub/Sub vs Streams:</strong> Pub/Sub has no persistence and no consumer groups. If a subscriber is down, messages are lost. For reliable messaging with replay and consumer groups, use <strong>Redis Streams</strong> (<code>XADD</code>/<code>XREAD</code>/<code>XGROUP</code>).</div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">⚙️ Lua Scripting — Atomic Multi-Command Operations</div>
  <div class="cp-body">

<p>Redis executes Lua scripts atomically — no other command runs between script operations. This is the safe way to implement read-modify-write patterns without transactions.</p>

<div class="cb"><span class="cm">-- Lua: atomic check-and-set with condition</span>
<span class="cm">-- KEYS[1] = key, ARGV[1] = expected value, ARGV[2] = new value</span>
<span class="ck">local</span> <span class="cv">current</span> = redis.<span class="cf">call</span>(<span class="cs">'GET'</span>, KEYS[<span class="cn">1</span>])
<span class="ck">if</span> <span class="cv">current</span> == ARGV[<span class="cn">1</span>] <span class="ck">then</span>
  redis.<span class="cf">call</span>(<span class="cs">'SET'</span>, KEYS[<span class="cn">1</span>], ARGV[<span class="cn">2</span>])
  <span class="ck">return</span> <span class="cn">1</span>
<span class="ck">end</span>
<span class="ck">return</span> <span class="cn">0</span></div>

<div class="cb"><span class="cm">// Node.js: run the Lua script (EVAL)</span>
<span class="ck">const</span> <span class="cv">script</span> = <span class="cs">`
  local current = redis.call('GET', KEYS[1])
  if current == ARGV[1] then
    redis.call('SET', KEYS[1], ARGV[2])
    return 1
  end
  return 0
`</span>;
<span class="ck">const</span> <span class="cv">result</span> = <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">eval</span>(<span class="cv">script</span>, <span class="cn">1</span>, <span class="cs">'mykey'</span>, <span class="cs">'old-value'</span>, <span class="cs">'new-value'</span>);</div>

  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🚦 Rate Limiting with Redis</div>
  <div class="cp-body">

<p><strong>Pattern 1 — Fixed Window (INCR + EXPIRE)</strong></p>
<div class="cb"><span class="cm">// Allow 100 requests per minute per IP</span>
<span class="ck">async function</span> <span class="cf">isAllowed</span>(<span class="cv">ip</span>) {
  <span class="ck">const</span> <span class="cv">window</span> = <span class="cv">Math</span>.<span class="cf">floor</span>(<span class="cv">Date</span>.<span class="cf">now</span>() / <span class="cn">60000</span>);   <span class="cm">// 1-minute window</span>
  <span class="ck">const</span> <span class="cv">key</span>    = <span class="cs">`ratelimit:<span class="co">${</span><span class="cv">ip</span><span class="co">}</span>:<span class="co">${</span><span class="cv">window</span><span class="co">}</span>`</span>;
  <span class="ck">const</span> <span class="cv">count</span>  = <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">incr</span>(<span class="cv">key</span>);
  <span class="ck">if</span> (<span class="cv">count</span> === <span class="cn">1</span>) <span class="ck">await</span> <span class="cv">redis</span>.<span class="cf">expire</span>(<span class="cv">key</span>, <span class="cn">60</span>);  <span class="cm">// set TTL on first request</span>
  <span class="ck">return</span> <span class="cv">count</span> <= <span class="cn">100</span>;
}</div>

<p><strong>Pattern 2 — Sliding Window (Sorted Set)</strong></p>
<div class="cb"><span class="cm">// More accurate: tracks exact timestamps of requests</span>
<span class="ck">async function</span> <span class="cf">isAllowedSliding</span>(<span class="cv">ip</span>, <span class="cv">limit</span> = <span class="cn">100</span>, <span class="cv">windowMs</span> = <span class="cn">60000</span>) {
  <span class="ck">const</span> <span class="cv">now</span>       = <span class="cv">Date</span>.<span class="cf">now</span>();
  <span class="ck">const</span> <span class="cv">key</span>       = <span class="cs">`ratelimit:sliding:<span class="co">${</span><span class="cv">ip</span><span class="co">}</span>`</span>;
  <span class="ck">const</span> <span class="cv">pipeline</span>  = <span class="cv">redis</span>.<span class="cf">multi</span>();
  <span class="cv">pipeline</span>.<span class="cf">zremrangebyscore</span>(<span class="cv">key</span>, <span class="cn">0</span>, <span class="cv">now</span> - <span class="cv">windowMs</span>);  <span class="cm">// evict old entries</span>
  <span class="cv">pipeline</span>.<span class="cf">zadd</span>(<span class="cv">key</span>, <span class="cv">now</span>, <span class="cv">now</span>.<span class="cf">toString</span>());          <span class="cm">// add current request</span>
  <span class="cv">pipeline</span>.<span class="cf">zcard</span>(<span class="cv">key</span>);                                <span class="cm">// count in window</span>
  <span class="cv">pipeline</span>.<span class="cf">expire</span>(<span class="cv">key</span>, <span class="cv">Math</span>.<span class="cf">ceil</span>(<span class="cv">windowMs</span> / <span class="cn">1000</span>));    <span class="cm">// auto-cleanup</span>
  <span class="ck">const</span> <span class="cv">results</span> = <span class="ck">await</span> <span class="cv">pipeline</span>.<span class="cf">exec</span>();
  <span class="ck">const</span> <span class="cv">count</span>   = <span class="cv">results</span>[<span class="cn">2</span>][<span class="cn">1</span>];   <span class="cm">// ZCARD result</span>
  <span class="ck">return</span> <span class="cv">count</span> <= <span class="cv">limit</span>;
}</div>

<div class="note">Fixed window is simpler but has a boundary burst problem: 100 requests at 0:59 and 100 at 1:01 = 200 requests in 2 seconds. Sliding window prevents this at the cost of more memory per key.</div>
  </div>
</div>

</div><!-- /tab-redis-advanced -->

<!-- ═══════════════════════════════════════════════════════════ TAB 5: MONGODB -->
<div id="tab-mongodb" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">📄 Document Model — BSON &amp; Schema Design</div>
  <div class="cp-body">

<div class="cb"><span class="cm">// BSON document example (stored as blog post)</span>
{
  <span class="cv">_id</span>: <span class="cf">ObjectId</span>(<span class="cs">"65e3f1a2b4c8d9e0f1234567"</span>),  <span class="cm">// 12-byte: timestamp+machine+pid+counter</span>
  <span class="cv">title</span>: <span class="cs">"Understanding Redis"</span>,
  <span class="cv">slug</span>:  <span class="cs">"understanding-redis"</span>,
  <span class="cv">author</span>: {
    <span class="cv">id</span>: <span class="cf">ObjectId</span>(<span class="cs">"..."</span>),
    <span class="cv">name</span>: <span class="cs">"Alice"</span>   <span class="cm">// denormalized — avoid join</span>
  },
  <span class="cv">tags</span>: [<span class="cs">"redis"</span>, <span class="cs">"backend"</span>, <span class="cs">"caching"</span>],
  <span class="cv">publishedAt</span>: <span class="cf">ISODate</span>(<span class="cs">"2026-03-27T10:00:00Z"</span>),
  <span class="cv">stats</span>: { <span class="cv">views</span>: <span class="cn">1502</span>, <span class="cv">likes</span>: <span class="cn">87</span> },
  <span class="cv">status</span>: <span class="cs">"published"</span>
}</div>

<p><strong>Embedding vs Referencing — the core schema decision:</strong></p>
<table class="t-table">
<thead><tr><th>Embed when…</th><th>Reference when…</th></tr></thead>
<tbody>
<tr><td>Data is always accessed together (post + author preview)</td><td>Data has its own lifecycle independent of parent</td></tr>
<tr><td>The embedded array has bounded size (≤ a few hundred items)</td><td>Array could grow unbounded (post comments → millions)</td></tr>
<tr><td>Update pattern writes the whole document</td><td>Many documents share the same sub-document</td></tr>
</tbody>
</table>

<div class="warn"><strong>16 MB document limit:</strong> MongoDB caps documents at 16 MB. Embedding unbounded arrays (e.g., all comments in a post document) will hit this limit. Use references + separate collection for comments.</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔍 Indexes in MongoDB</div>
  <div class="cp-body">

<div class="cb"><span class="cm">// Single field index — ascending (1) or descending (-1)</span>
db.posts.<span class="cf">createIndex</span>({ <span class="cv">slug</span>: <span class="cn">1</span> }, { <span class="cv">unique</span>: <span class="ck">true</span> });

<span class="cm">// Compound index — left-prefix rule applies (same as SQL)</span>
db.posts.<span class="cf">createIndex</span>({ <span class="cv">status</span>: <span class="cn">1</span>, <span class="cv">publishedAt</span>: <span class="cn">-1</span> });
<span class="cm">// Supports: {status}, {status, publishedAt}  NOT: {publishedAt} alone</span>

<span class="cm">// Multikey index — automatically created when field is an array</span>
db.posts.<span class="cf">createIndex</span>({ <span class="cv">tags</span>: <span class="cn">1</span> });
<span class="cm">// Allows: db.posts.find({ tags: "redis" })  ← single element match</span>

<span class="cm">// Text index — full-text search</span>
db.posts.<span class="cf">createIndex</span>({ <span class="cv">title</span>: <span class="cs">"text"</span>, <span class="cv">body</span>: <span class="cs">"text"</span> });
db.posts.<span class="cf">find</span>({ <span class="co">$</span><span class="cv">text</span>: { <span class="co">$</span><span class="cv">search</span>: <span class="cs">"redis caching"</span> } });

<span class="cm">// Partial index — only index documents matching filter (saves space)</span>
db.posts.<span class="cf">createIndex</span>(
  { <span class="cv">publishedAt</span>: <span class="cn">-1</span> },
  { <span class="cv">partialFilterExpression</span>: { <span class="cv">status</span>: <span class="cs">"published"</span> } }
);

<span class="cm">// Explain query plan</span>
db.posts.<span class="cf">find</span>({ <span class="cv">status</span>: <span class="cs">"published"</span> }).<span class="cf">explain</span>(<span class="cs">"executionStats"</span>);</div>

  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔗 Aggregation Pipeline — Multi-Stage Transforms</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Collection → [$match] → [$lookup] → [$unwind] → [$group] → [$sort] → [$limit] → Result
               filter    join        flatten     aggregate   order     paginate
</pre>
  </div>

<div class="cb">db.posts.<span class="cf">aggregate</span>([
  <span class="cm">// Stage 1: filter published posts from 2026</span>
  { <span class="co">$</span><span class="cv">match</span>: {
    <span class="cv">status</span>: <span class="cs">"published"</span>,
    <span class="cv">publishedAt</span>: { <span class="co">$</span><span class="cv">gte</span>: <span class="ck">new</span> <span class="cf">Date</span>(<span class="cs">"2026-01-01"</span>) }
  }},

  <span class="cm">// Stage 2: join with users collection</span>
  { <span class="co">$</span><span class="cv">lookup</span>: {
    <span class="cv">from</span>:         <span class="cs">"users"</span>,
    <span class="cv">localField</span>:   <span class="cs">"author.id"</span>,
    <span class="cv">foreignField</span>: <span class="cs">"_id"</span>,
    <span class="cv">as</span>:           <span class="cs">"authorDoc"</span>
  }},

  <span class="cm">// Stage 3: group by tag to count posts per tag</span>
  { <span class="co">$</span><span class="cv">unwind</span>: <span class="cs">"$tags"</span> },
  { <span class="co">$</span><span class="cv">group</span>: {
    <span class="cv">_id</span>:   <span class="cs">"$tags"</span>,
    <span class="cv">count</span>: { <span class="co">$</span><span class="cv">sum</span>: <span class="cn">1</span> },
    <span class="cv">totalViews</span>: { <span class="co">$</span><span class="cv">sum</span>: <span class="cs">"$stats.views"</span> }
  }},

  <span class="cm">// Stage 4: sort by count descending, return top 10</span>
  { <span class="co">$</span><span class="cv">sort</span>:  { <span class="cv">count</span>: <span class="cn">-1</span> } },
  { <span class="co">$</span><span class="cv">limit</span>: <span class="cn">10</span> }
]);</div>

<div class="note"><strong>$match early:</strong> Always put <code>$match</code> stages as early as possible in the pipeline to reduce documents flowing through subsequent stages. MongoDB can use indexes for the first <code>$match</code> stage.</div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">✏️ Write Operations &amp; Operators</div>
  <div class="cp-body">

<div class="cb"><span class="cm">// insertOne / insertMany</span>
<span class="ck">await</span> <span class="cv">db</span>.<span class="cf">collection</span>(<span class="cs">'posts'</span>).<span class="cf">insertOne</span>({ <span class="cv">title</span>: <span class="cs">"New Post"</span>, <span class="cv">status</span>: <span class="cs">"draft"</span> });

<span class="cm">// updateOne — $set updates specific fields, $inc increments atomically</span>
<span class="ck">await</span> <span class="cv">db</span>.<span class="cf">collection</span>(<span class="cs">'posts'</span>).<span class="cf">updateOne</span>(
  { <span class="cv">_id</span>: <span class="cv">postId</span> },
  {
    <span class="co">$</span><span class="cv">set</span>: { <span class="cv">status</span>: <span class="cs">"published"</span>, <span class="cv">publishedAt</span>: <span class="ck">new</span> <span class="cf">Date</span>() },
    <span class="co">$</span><span class="cv">inc</span>: { <span class="cs">'stats.views'</span>: <span class="cn">1</span> },        <span class="cm">// atomic increment</span>
    <span class="co">$</span><span class="cv">push</span>: { <span class="cv">tags</span>: <span class="cs">"featured"</span> }         <span class="cm">// append to array</span>
  }
);

<span class="cm">// findOneAndUpdate — atomic read + update</span>
<span class="ck">const</span> <span class="cv">updated</span> = <span class="ck">await</span> <span class="cv">db</span>.<span class="cf">collection</span>(<span class="cs">'tasks'</span>).<span class="cf">findOneAndUpdate</span>(
  { <span class="cv">status</span>: <span class="cs">"pending"</span> },
  { <span class="co">$</span><span class="cv">set</span>: { <span class="cv">status</span>: <span class="cs">"processing"</span>, <span class="cv">lockedAt</span>: <span class="ck">new</span> <span class="cf">Date</span>() } },
  { <span class="cv">sort</span>: { <span class="cv">createdAt</span>: <span class="cn">1</span> }, <span class="cv">returnDocument</span>: <span class="cs">"after"</span> }  <span class="cm">// FIFO queue claim</span>
);</div>

  </div>
</div>

</div><!-- /tab-mongodb -->

<!-- ═══════════════════════════════════════════════════════════ TAB 6: CASSANDRA -->
<div id="tab-cassandra" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">🏛️ Cassandra Architecture — Write-Optimized, Distributed</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Cassandra Cluster (3 nodes, replication_factor=3)

Write path:
  Client → Coordinator Node
    → hash(partition_key) → token ring → target nodes
    → Commit Log (WAL) + Memtable
    → Memtable flush → SSTable on disk

Read path:
  Client → Coordinator → target nodes
    → Row Cache (if enabled)
    → Bloom Filter (fast "definitely not here" check)
    → Key Cache → SSTable index → SSTable data

Compaction:
  SSTables merge periodically → remove tombstones (deletes)
  → smaller read amplification

Token Ring (consistent hashing):
  Each node owns a range of tokens
  Replication: each row copied to RF=3 consecutive nodes
  Coordinator routes any write to correct nodes
</pre>
  </div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔑 Data Modeling — Partition Key, Clustering Key</div>
  <div class="cp-body">

<p>Cassandra schema design is <strong>query-driven</strong>: design your table for one specific query. Joins do not exist; denormalization is expected.</p>

<div class="cb"><span class="cm">-- Schema for: "get user's posts, ordered by date descending"</span>
<span class="cm">-- Query pattern: WHERE user_id = ? ORDER BY created_at DESC LIMIT 20</span>

<span class="ck">CREATE TABLE</span> posts_by_user (
  user_id     uuid,
  created_at  timestamp,   <span class="cm">-- clustering key: sorted on disk</span>
  post_id     uuid,
  title       text,
  status      text,
  <span class="ck">PRIMARY KEY</span> ((user_id), created_at, post_id)
  <span class="cm">-- ─────────────  ──────────────────────────</span>
  <span class="cm">-- partition key  clustering keys (sort order)</span>
) <span class="ck">WITH</span> CLUSTERING ORDER BY (created_at DESC, post_id ASC)
  <span class="ck">AND</span> COMPACTION = {'class': 'TimeWindowCompactionStrategy', 'compaction_window_size': 1, 'compaction_window_unit': 'DAYS'};
<span class="cm">-- TWCS: optimized for time-series (SSTable per time window)</span></div>

<div class="two-col">
<div>
<strong>Partition Key</strong>
<ul>
  <li>Determines which node(s) store the row</li>
  <li>All rows with same partition key → same partition</li>
  <li>Must appear in every query (no full-table scans)</li>
  <li>Keep partitions balanced — hot partition = hot node</li>
  <li>Partition size limit: ~100 MB recommended</li>
</ul>
</div>
<div>
<strong>Clustering Key</strong>
<ul>
  <li>Defines sort order within a partition</li>
  <li>Enables range queries on clustering columns</li>
  <li>Can query <code>WHERE created_at &gt; X</code> within a partition</li>
  <li>Cannot skip clustering keys in WHERE clause</li>
  <li>Choose DESC if you mostly read recent data first</li>
</ul>
</div>
</div>

  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">📊 Consistency Levels — Tunable per Query</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Level</th><th>Writes to</th><th>Reads from</th><th>Tradeoff</th></tr></thead>
<tbody>
<tr><td><code>ONE</code></td><td>1 node</td><td>1 node</td><td>Fastest; may read stale data</td></tr>
<tr><td><code>QUORUM</code></td><td>RF/2+1 nodes</td><td>RF/2+1 nodes</td><td>Strong consistency (write+read quorum overlap); balanced</td></tr>
<tr><td><code>LOCAL_QUORUM</code></td><td>Quorum in local DC</td><td>Quorum in local DC</td><td>Strong consistency within DC; avoids cross-DC latency</td></tr>
<tr><td><code>ALL</code></td><td>All RF nodes</td><td>All RF nodes</td><td>Strongest; unavailable if any node down</td></tr>
<tr><td><code>ANY</code></td><td>At least 1 (hint OK)</td><td>N/A (write only)</td><td>Highest availability; weakest durability</td></tr>
</tbody>
</table>

<div class="ins"><strong>Strong consistency formula:</strong> Write CL + Read CL > RF<br>
Example with RF=3: QUORUM write (2) + QUORUM read (2) = 4 > 3 ✓ → guaranteed to see latest write.</div>

<div class="cb"><span class="cm">-- CQL: set consistency level per query in cqlsh</span>
<span class="ck">CONSISTENCY</span> QUORUM;
<span class="ck">SELECT</span> * <span class="ck">FROM</span> posts_by_user <span class="ck">WHERE</span> user_id = <span class="cn">abc123</span> <span class="ck">LIMIT</span> <span class="cn">20</span>;</div>

  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">⚠️ Common Cassandra Anti-Patterns</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th>Anti-Pattern</th><th>Why It Fails</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>ALLOW FILTERING in queries</td><td>Forces full partition scan; slow at scale</td><td>Redesign table for the query; use secondary index carefully</td></tr>
<tr><td>Unbounded partition growth</td><td>Single partition → single node bottleneck; &gt;2GB bad</td><td>Add time bucket to partition key (user_id + year_month)</td></tr>
<tr><td>High-cardinality secondary indexes</td><td>Distributed index = scatter-gather on every node</td><td>Materialize a separate table for each query pattern</td></tr>
<tr><td>Large IN queries</td><td>Coordinator fans out to many nodes; serial waits</td><td>Async parallel queries; smaller batch sizes</td></tr>
<tr><td>Logged batches for performance</td><td>Batches add coordinator overhead; not for performance, only for atomicity across tables</td><td>Use unlogged batches only for same-partition multi-row writes</td></tr>
</tbody>
</table>

  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🆚 MongoDB vs Cassandra vs Redis — Quick Reference</div>
  <div class="cp-body">

<table class="t-table">
<thead><tr><th></th><th>Redis</th><th>MongoDB</th><th>Cassandra</th></tr></thead>
<tbody>
<tr><td><strong>Model</strong></td><td>Key-value / data structures</td><td>Document (BSON)</td><td>Wide-column (partitioned rows)</td></tr>
<tr><td><strong>Query</strong></td><td>Key lookup; limited range</td><td>Rich ad-hoc; aggregation pipeline</td><td>Query-driven; CQL; no ad-hoc</td></tr>
<tr><td><strong>Transactions</strong></td><td>MULTI/EXEC; Lua scripts; limited</td><td>Multi-document ACID (v4+)</td><td>Lightweight transactions (LWT); limited</td></tr>
<tr><td><strong>Scale</strong></td><td>Cluster mode (hash slots)</td><td>Replica sets; sharded clusters</td><td>Linear horizontal scale; no master</td></tr>
<tr><td><strong>Consistency</strong></td><td>Strong within shard</td><td>Strong (primary); eventual (secondaries)</td><td>Tunable per query (ONE → ALL)</td></tr>
<tr><td><strong>Best for</strong></td><td>Caching, sessions, rate limiting</td><td>Flexible catalogs, CMS, user data</td><td>Time-series, activity feeds, IoT</td></tr>
</tbody>
</table>

  </div>
</div>

</div><!-- /tab-cassandra -->

<!-- ═══════════════════════════════════════════════════════════ TAB 7: C & HIREDIS -->
<div id="tab-c-hiredis" class="tab-pane">

<div class="cp p-violet">
  <div class="cp-hdr">⚙️ hiredis — Redis Client in C</div>
  <div class="cp-body">

<p>hiredis is the official, lightweight C client for Redis. It provides a synchronous API for simple use cases and an async API (libevent/libev/libuv adapters) for non-blocking I/O.</p>

<div class="cb"><span class="cm">/* hiredis_demo.c — connect, set, get, expire, hash ops */</span>
<span class="ck">#include</span> <span class="cs">&lt;hiredis/hiredis.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdlib.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>

<span class="cm">/* Helper: check reply type and abort on error */</span>
<span class="ck">static void</span> <span class="cf">check</span>(<span class="cg">redisReply</span> <span class="co">*</span>r, <span class="ck">const char</span> <span class="co">*</span>label) {
    <span class="ck">if</span> (!r) { <span class="cf">fprintf</span>(stderr, <span class="cs">"%s: null reply\n"</span>, label); <span class="cf">exit</span>(<span class="cn">1</span>); }
    <span class="ck">if</span> (r<span class="co">-&gt;</span>type <span class="co">==</span> REDIS_REPLY_ERROR) {
        <span class="cf">fprintf</span>(stderr, <span class="cs">"%s error: %s\n"</span>, label, r<span class="co">-&gt;</span>str);
        <span class="cf">freeReplyObject</span>(r);
        <span class="cf">exit</span>(<span class="cn">1</span>);
    }
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="cm">/* Connect */</span>
    <span class="cg">redisContext</span> <span class="co">*</span>c = <span class="cf">redisConnect</span>(<span class="cs">"127.0.0.1"</span>, <span class="cn">6379</span>);
    <span class="ck">if</span> (!c <span class="co">||</span> c<span class="co">-&gt;</span>err) {
        <span class="cf">fprintf</span>(stderr, <span class="cs">"Connect error: %s\n"</span>, c ? c<span class="co">-&gt;</span>errstr : <span class="cs">"OOM"</span>);
        <span class="cf">exit</span>(<span class="cn">1</span>);
    }
    <span class="cf">printf</span>(<span class="cs">"Connected to Redis\n"</span>);

    <span class="cg">redisReply</span> <span class="co">*</span>reply;

    <span class="cm">/* SET with EX (expire in 300 seconds) */</span>
    reply = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c, <span class="cs">"SET user:42 Alice EX 300"</span>);
    <span class="cf">check</span>(reply, <span class="cs">"SET"</span>);
    <span class="cf">printf</span>(<span class="cs">"SET: %s\n"</span>, reply<span class="co">-&gt;</span>str);  <span class="cm">/* "OK" */</span>
    <span class="cf">freeReplyObject</span>(reply);

    <span class="cm">/* GET */</span>
    reply = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c, <span class="cs">"GET user:42"</span>);
    <span class="cf">check</span>(reply, <span class="cs">"GET"</span>);
    <span class="cf">printf</span>(<span class="cs">"GET user:42 = %s\n"</span>, reply<span class="co">-&gt;</span>type <span class="co">==</span> REDIS_REPLY_NIL ? <span class="cs">"(nil)"</span> : reply<span class="co">-&gt;</span>str);
    <span class="cf">freeReplyObject</span>(reply);

    <span class="cm">/* INCR — atomic counter */</span>
    reply = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c, <span class="cs">"INCR post:7:views"</span>);
    <span class="cf">check</span>(reply, <span class="cs">"INCR"</span>);
    <span class="cf">printf</span>(<span class="cs">"post:7:views = %lld\n"</span>, reply<span class="co">-&gt;</span>integer);
    <span class="cf">freeReplyObject</span>(reply);

    <span class="cm">/* HSET — store object fields */</span>
    reply = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c,
        <span class="cs">"HSET user:42:profile name Alice email alice@example.com age 28"</span>);
    <span class="cf">check</span>(reply, <span class="cs">"HSET"</span>);
    <span class="cf">printf</span>(<span class="cs">"HSET: added %lld fields\n"</span>, reply<span class="co">-&gt;</span>integer);
    <span class="cf">freeReplyObject</span>(reply);

    <span class="cm">/* HGETALL — read all hash fields */</span>
    reply = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c, <span class="cs">"HGETALL user:42:profile"</span>);
    <span class="cf">check</span>(reply, <span class="cs">"HGETALL"</span>);
    <span class="cf">printf</span>(<span class="cs">"Profile fields:\n"</span>);
    <span class="ck">for</span> (<span class="cg">size_t</span> i = <span class="cn">0</span>; i <span class="co">+</span> <span class="cn">1</span> <span class="co">&lt;</span> reply<span class="co">-&gt;</span>elements; i <span class="co">+=</span> <span class="cn">2</span>)
        <span class="cf">printf</span>(<span class="cs">"  %s = %s\n"</span>, reply<span class="co">-&gt;</span>element[i]<span class="co">-&gt;</span>str, reply<span class="co">-&gt;</span>element[i<span class="co">+</span><span class="cn">1</span>]<span class="co">-&gt;</span>str);
    <span class="cf">freeReplyObject</span>(reply);

    <span class="cf">redisFree</span>(c);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>

<div class="cb"><span class="cm"># Compile: link against hiredis</span>
gcc -o hiredis_demo hiredis_demo.c -lhiredis</div>

  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔢 Pipelining — Batch Commands Without Round-Trips</div>
  <div class="cp-body">

<div class="diagram-box">
<pre>
Without pipelining (N commands = N round-trips):
  Client ──SET──► Server ──OK──► Client ──INCR──► Server ──1──► Client ...
  RTT: N × (50ms) = 500ms for 10 commands

With pipelining (N commands = 1 round-trip):
  Client ──[SET, INCR, HSET, ...]──► Server
  Server ──[OK, 1, 3, ...]──────────► Client
  RTT: 1 × 50ms = 50ms for 10 commands
</pre>
  </div>

<div class="cb"><span class="cm">/* hiredis pipelining — queue commands, flush once */</span>
<span class="ck">void</span> <span class="cf">pipeline_demo</span>(<span class="cg">redisContext</span> <span class="co">*</span>c) {
    <span class="cm">/* Queue commands without waiting for reply */</span>
    <span class="cf">redisAppendCommand</span>(c, <span class="cs">"SET key1 val1"</span>);
    <span class="cf">redisAppendCommand</span>(c, <span class="cs">"SET key2 val2"</span>);
    <span class="cf">redisAppendCommand</span>(c, <span class="cs">"INCR counter"</span>);
    <span class="cf">redisAppendCommand</span>(c, <span class="cs">"EXPIRE key1 3600"</span>);

    <span class="cm">/* Flush and collect replies */</span>
    <span class="cg">redisReply</span> <span class="co">*</span>r;
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i <span class="co">&lt;</span> <span class="cn">4</span>; i<span class="co">++</span>) {
        <span class="cf">redisGetReply</span>(c, (<span class="ck">void</span> <span class="co">**</span>)<span class="co">&amp;</span>r);
        <span class="ck">if</span> (r) {
            <span class="ck">if</span> (r<span class="co">-&gt;</span>type <span class="co">==</span> REDIS_REPLY_INTEGER)
                <span class="cf">printf</span>(<span class="cs">"reply[%d] = %lld\n"</span>, i, r<span class="co">-&gt;</span>integer);
            <span class="ck">else if</span> (r<span class="co">-&gt;</span>type <span class="co">==</span> REDIS_REPLY_STATUS)
                <span class="cf">printf</span>(<span class="cs">"reply[%d] = %s\n"</span>, i, r<span class="co">-&gt;</span>str);
            <span class="cf">freeReplyObject</span>(r);
        }
    }
}</div>

  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔒 Distributed Lock in C (Redlock-lite)</div>
  <div class="cp-body">

<div class="cb"><span class="cm">/* Simple Redis distributed lock using SET NX EX */</span>
<span class="ck">#include</span> <span class="cs">&lt;hiredis/hiredis.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;time.h&gt;</span>

<span class="cm">/* Returns 1 if lock acquired, 0 otherwise.
   token must be unique per lock-holder (used to safely release) */</span>
<span class="ck">int</span> <span class="cf">redis_lock</span>(<span class="cg">redisContext</span> <span class="co">*</span>c, <span class="ck">const char</span> <span class="co">*</span>key, <span class="ck">const char</span> <span class="co">*</span>token, <span class="ck">int</span> ttl_sec) {
    <span class="cg">redisReply</span> <span class="co">*</span>r = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c,
        <span class="cs">"SET %s %s NX EX %d"</span>, key, token, ttl_sec);
    <span class="ck">int</span> acquired = (r <span class="co">&amp;&amp;</span> r<span class="co">-&gt;</span>type <span class="co">==</span> REDIS_REPLY_STATUS
                      <span class="co">&amp;&amp;</span> <span class="cf">strcmp</span>(r<span class="co">-&gt;</span>str, <span class="cs">"OK"</span>) <span class="co">==</span> <span class="cn">0</span>);
    <span class="ck">if</span> (r) <span class="cf">freeReplyObject</span>(r);
    <span class="ck">return</span> acquired;
}

<span class="cm">/* Release only if our token matches (Lua ensures atomicity) */</span>
<span class="ck">void</span> <span class="cf">redis_unlock</span>(<span class="cg">redisContext</span> <span class="co">*</span>c, <span class="ck">const char</span> <span class="co">*</span>key, <span class="ck">const char</span> <span class="co">*</span>token) {
    <span class="ck">const char</span> <span class="co">*</span>lua =
        <span class="cs">"if redis.call('GET',KEYS[1])==ARGV[1] then "</span>
        <span class="cs">"  return redis.call('DEL',KEYS[1]) "</span>
        <span class="cs">"else return 0 end"</span>;
    <span class="cg">redisReply</span> <span class="co">*</span>r = (<span class="cg">redisReply</span> <span class="co">*</span>)<span class="cf">redisCommand</span>(c,
        <span class="cs">"EVAL %s 1 %s %s"</span>, lua, key, token);
    <span class="ck">if</span> (r) <span class="cf">freeReplyObject</span>(r);
}

<span class="cm">/* Usage */</span>
<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="cg">redisContext</span> <span class="co">*</span>c = <span class="cf">redisConnect</span>(<span class="cs">"127.0.0.1"</span>, <span class="cn">6379</span>);
    <span class="ck">const char</span> <span class="co">*</span>lock_key   = <span class="cs">"lock:job:42"</span>;
    <span class="ck">const char</span> <span class="co">*</span>lock_token = <span class="cs">"unique-token-abc"</span>;  <span class="cm">/* use UUID in practice */</span>

    <span class="ck">if</span> (<span class="cf">redis_lock</span>(c, lock_key, lock_token, <span class="cn">5</span>)) {
        <span class="cf">printf</span>(<span class="cs">"Lock acquired — doing work\n"</span>);
        <span class="cm">/* ... critical section ... */</span>
        <span class="cf">redis_unlock</span>(c, lock_key, lock_token);
        <span class="cf">printf</span>(<span class="cs">"Lock released\n"</span>);
    } <span class="ck">else</span> {
        <span class="cf">printf</span>(<span class="cs">"Could not acquire lock — another process holds it\n"</span>);
    }
    <span class="cf">redisFree</span>(c);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>

  </div>
</div>

</div><!-- /tab-c-hiredis -->

<!-- ═══════════════════════════════════════════════════════════ TAB 8: LABS -->
<div id="tab-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 1 — Redis Caching Layer for a REST API</div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Add cache-aside caching to an Express.js API, measure cache hit rate.</p>
    <div class="lab-step"><div class="sn">1</div><div>Spin up Redis locally: <code>docker run -p 6379:6379 redis:7-alpine</code></div></div>
    <div class="lab-step"><div class="sn">2</div><div>Create an Express endpoint <code>GET /users/:id</code> that hits a PostgreSQL DB.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Wrap the handler with cache-aside logic: check Redis first, populate on miss, TTL = 300s.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add a middleware that increments <code>cache:hits</code> and <code>cache:misses</code> counters in Redis.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Load test with <code>wrk -t4 -c100 -d30s http://localhost:3000/users/42</code>.</div></div>
    <div class="lab-step"><div class="sn">6</div><div>Check hit rate: <code>redis-cli GET cache:hits</code> vs <code>GET cache:misses</code>. Expect &gt;95% hits after warm-up.</div></div>
    <div class="lab-step"><div class="sn">7</div><div>Test invalidation: update user in DB, verify Redis key is deleted, next request repopulates.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 2 — Rate Limiter Middleware (Sliding Window)</div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Implement a sliding-window rate limiter in Redis; test boundary behavior.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the <code>isAllowedSliding(ip, limit=10, windowMs=60000)</code> function using Redis sorted sets.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Wire it as Express middleware: return <code>429 Too Many Requests</code> with <code>Retry-After</code> header when over limit.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Verify: send 10 rapid requests — all succeed. Send 11th — gets 429.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify sliding window: wait 30s, send 5 more requests — all succeed (window slid, old entries purged).</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Inspect Redis: <code>ZSCORE ratelimit:sliding:127.0.0.1</code> — confirm timestamps are in sorted set.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 3 — MongoDB Aggregation: Top Tags Report</div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Build an aggregation pipeline that computes per-tag post counts and total views.</p>
    <div class="lab-step"><div class="sn">1</div><div>Insert 50 sample posts with <code>mongosh</code> using a seed script. Include varied tags and view counts.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write the pipeline: <code>$match</code> (published) → <code>$unwind</code> (tags) → <code>$group</code> (count, sumViews) → <code>$sort</code> → <code>$limit 10</code>.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run with <code>.explain("executionStats")</code> — confirm the initial <code>$match</code> uses an index.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Create the compound index <code>{status:1, publishedAt:-1}</code> and re-run explain — compare <code>totalDocsExamined</code>.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Cache the result in Redis as <code>report:top-tags</code> with TTL 3600. Serve from cache on repeat requests.</div></div>
  </div>
</div>

<hr class="sep"/>

<div class="cp p-violet">
  <div class="cp-hdr">✅ Module Mastery Checklist</div>
  <div class="cp-body">
<ul class="cl">
  <li>Explain the five NoSQL categories and give a use case for each</li>
  <li>Describe CAP theorem and classify Redis, MongoDB, and Cassandra under it</li>
  <li>List all six Redis data types, their O() complexities, and one use case each</li>
  <li>Implement cache-aside pattern with correct TTL invalidation on write</li>
  <li>Contrast cache-aside vs write-through vs write-behind consistency guarantees</li>
  <li>Explain cache stampede and implement the SET NX lock pattern to prevent it</li>
  <li>Configure Redis maxmemory and choose appropriate eviction policy</li>
  <li>Describe RDB vs AOF persistence trade-offs and recommend correct production config</li>
  <li>Implement a fixed-window rate limiter using INCR + EXPIRE</li>
  <li>Implement a sliding-window rate limiter using a Sorted Set</li>
  <li>Use Lua scripting in Redis for an atomic read-modify-write operation</li>
  <li>Explain MongoDB embedding vs referencing decision criteria</li>
  <li>Write a MongoDB aggregation pipeline with $match, $lookup, $group, $sort</li>
  <li>Define Cassandra partition key, clustering key, and explain query-driven design</li>
  <li>Calculate whether QUORUM reads + QUORUM writes guarantee strong consistency for a given RF</li>
</ul>
  </div>
</div>

</div><!-- /tab-labs -->

<div class="mod-nav">
  <a href="{{ '/learning/backend/m06-sql-indexing/' | relative_url }}" class="nb">← M06 SQL Indexing</a>
  <a href="{{ '/learning/backend/backend-roadmap/' | relative_url }}" class="nb">↑ Roadmap</a>
  <span class="nb" style="opacity:.55;cursor:default;">M08 DB Scaling · soon</span>
</div>

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}
</script>
