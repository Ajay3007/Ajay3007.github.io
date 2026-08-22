---
title: "Module B2 — Databases at Scale | HLD Track"
description: "Track B · HLD · Module B2 · Week 12 Databases at Scale Indexing · ACID vs BASE · SQL vs NoSQL Replication · Sharding · Read Replicas · Selection Guide 7 TOPICS 4 TASKS 5 NOSQL…"
domain: system-design
track: system-design-hld
order: 104
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b2-databases-at-scale/
---

<link rel="stylesheet" href="/assets/css/sd-module-b2.css">

<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Source+Code+Pro:wght@300;400;600&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">

<header>
  <div class="hdr-accent"></div>
  <div class="hdr-inner">
    <div>
      <div class="hdr-kicker">Track B · HLD · Module B2 · Week 12</div>
      <h1>Databases<br><em>at Scale</em></h1>
      <div class="hdr-sub">
        Indexing · ACID vs BASE · SQL vs NoSQL<br>
        Replication · Sharding · Read Replicas · Selection Guide
      </div>
    </div>
    <div class="hdr-stats">
      <div class="hs-box"><div class="hs-val">7</div><div class="hs-lbl">TOPICS</div></div>
      <div class="hs-box"><div class="hs-val">4</div><div class="hs-lbl">TASKS</div></div>
      <div class="hs-box"><div class="hs-val">5</div><div class="hs-lbl">NOSQL MODELS</div></div>
      <div class="hs-box"><div class="hs-val">B2</div><div class="hs-lbl">MODULE</div></div>
    </div>
  </div>
  <div class="topic-strip">
    <div class="topic-pill" style="border-color:var(--ice);color:var(--ice)">B-Tree Index</div>
    <div class="topic-pill" style="border-color:var(--mint);color:var(--mint)">ACID / BASE</div>
    <div class="topic-pill" style="border-color:var(--gold);color:var(--gold)">SQL vs NoSQL</div>
    <div class="topic-pill" style="border-color:var(--sky);color:var(--sky)">Replication</div>
    <div class="topic-pill" style="border-color:var(--violet);color:var(--violet)">Sharding</div>
    <div class="topic-pill" style="border-color:var(--coral);color:var(--coral)">Hotkey</div>
    <div class="topic-pill" style="border-color:var(--lime);color:var(--lime)">DB Selection</div>
  </div>
</header>

<nav class="nav">
  <div class="nav-tab active" onclick="show('index',this)">Indexing</div>
  <div class="nav-tab" onclick="show('acid',this)">ACID vs BASE</div>
  <div class="nav-tab" onclick="show('sqlnosql',this)">SQL vs NoSQL</div>
  <div class="nav-tab" onclick="show('replication',this)">Replication</div>
  <div class="nav-tab" onclick="show('sharding',this)">Sharding</div>
  <div class="nav-tab" onclick="show('dbselect',this)">DB Selection</div>
  <div class="nav-tab" onclick="show('tasks',this)">Tasks</div>
  <div class="nav-tab" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- ══ INDEXING ══ -->
<div class="view active" id="view-index">
  <div class="sec-h">Indexing</div>
  <div class="sec-sub">Why queries go from O(n) to O(log n) — and what it costs</div>

  <div class="idx-grid">
    <div class="idx-card" style="border-top-color:var(--ice)">
      <div class="idx-name">B-Tree Index</div>
      <div class="idx-body">Balanced search tree of (key → row pointer) pairs. Keys sorted → enables range queries, ORDER BY, binary search in O(log n).</div>
      <div class="idx-use" style="color:var(--ice)">USE: equality (=), range (&lt;, &gt;, BETWEEN), ORDER BY, JOIN ON<br>DEFAULT: PostgreSQL, MySQL, Oracle</div>
    </div>
    <div class="idx-card" style="border-top-color:var(--gold)">
      <div class="idx-name">Hash Index</div>
      <div class="idx-body">Hash map of key → row pointer. O(1) exact lookup. Keys unordered — range queries impossible.</div>
      <div class="idx-use" style="color:var(--gold)">USE: equality only (=). Never for ranges.<br>EXAMPLES: Memcached, Redis, MySQL MEMORY engine</div>
    </div>
    <div class="idx-card" style="border-top-color:var(--mint)">
      <div class="idx-name">Composite Index</div>
      <div class="idx-body">Index on (col_A, col_B). Left-most prefix rule: queries must start with col_A to use the index. Most selective column goes first.</div>
      <div class="idx-use" style="color:var(--mint)">INDEX(user_id, created_at)<br>✓ WHERE user_id=5<br>✓ WHERE user_id=5 AND created_at&gt;X<br>✗ WHERE created_at&gt;X (skips prefix)</div>
    </div>
  </div>

  <div class="code-wrap">
    <div class="code-top">Covering Index — query satisfied entirely from index<span class="code-lang">SQL</span></div>
<pre class="code"><span class="cm">-- Table: orders (10M rows)</span>
<span class="cm">-- Query: SELECT user_id, created_at FROM orders WHERE user_id = 5</span>
 
<span class="cm">-- Regular index on user_id:</span>
<span class="cm">--   1. B-tree lookup → row pointer</span>
<span class="cm">--   2. Fetch row from heap (random disk I/O) to read created_at</span>
 
<span class="cm">-- Covering index on (user_id, created_at):</span>
<span class="kw">CREATE INDEX</span> idx_covering <span class="kw">ON</span> orders(user_id, created_at);
<span class="cm">--   1. B-tree lookup → both columns found IN the index leaf</span>
<span class="cm">--   2. NO heap access at all → drastically reduced I/O</span>
<span class="cm">--   ✅ PostgreSQL calls this "Index Only Scan"</span>
 
<span class="cm">-- Index design for common queries:</span>
<span class="kw">CREATE INDEX</span> idx_user   <span class="kw">ON</span> orders(user_id);                  <span class="cm">-- Q1: orders by user</span>
<span class="kw">CREATE INDEX</span> idx_rest_t <span class="kw">ON</span> orders(restaurant_id, created_at); <span class="cm">-- Q2: restaurant + time range</span>
<span class="kw">CREATE INDEX</span> idx_status <span class="kw">ON</span> orders(status) <span class="kw">WHERE</span> status = <span class="str">'pending'</span>; <span class="cm">-- Q3: partial index!</span>
<span class="kw">CREATE INDEX</span> idx_user_d <span class="kw">ON</span> orders(user_id, created_at);      <span class="cm">-- Q4: user + date range</span></pre>
  </div>

  <div class="alert gold"><em>Index cost trade-off:</em> Every write (INSERT/UPDATE/DELETE) must update all indexes on that table. A table with 10 indexes needs 10 B-tree updates per write. Index only columns used in WHERE, JOIN ON, ORDER BY. Low-cardinality columns (boolean, status with 3 values) often give poor selectivity — the optimizer may prefer a full scan.</div>
</div>

<!-- ══ ACID vs BASE ══ -->
<div class="view" id="view-acid">
  <div class="sec-h">ACID vs BASE</div>
  <div class="sec-sub">The consistency guarantee spectrum — choose based on use case</div>

  <div class="ab-grid">
    <div class="ab-card">
      <div class="ab-hdr" style="background:rgba(96,208,255,0.06)">
        <div class="ab-title">ACID</div>
        <div class="ab-tag">RELATIONAL DATABASES · STRONG GUARANTEES</div>
      </div>
      <div class="ab-body">
        <div class="ab-row"><div class="ab-letter">A</div><div class="ab-def"><strong>Atomicity</strong> — Transaction is all-or-nothing. Transfer $100: if debit succeeds but credit fails, both are rolled back. No partial writes survive.</div></div>
        <div class="ab-row"><div class="ab-letter">C</div><div class="ab-def"><strong>Consistency</strong> — DB transitions from one valid state to another. Constraints (FK, UNIQUE, NOT NULL, CHECK) always satisfied post-transaction.</div></div>
        <div class="ab-row"><div class="ab-letter">I</div><div class="ab-def"><strong>Isolation</strong> — Concurrent transactions don't see each other's in-progress writes. Levels: READ COMMITTED (default PG) → REPEATABLE READ → SERIALIZABLE.</div></div>
        <div class="ab-row"><div class="ab-letter">D</div><div class="ab-def"><strong>Durability</strong> — Committed transactions survive crashes. Guaranteed via WAL (write-ahead log) + fsync to disk before confirming commit.</div></div>
      </div>
    </div>
    <div class="ab-card">
      <div class="ab-hdr" style="background:rgba(160,96,240,0.06)">
        <div class="ab-title">BASE</div>
        <div class="ab-tag">NOSQL / DISTRIBUTED · AVAILABLE BY DESIGN</div>
      </div>
      <div class="ab-body">
        <div class="ab-row"><div class="ab-letter" style="color:var(--violet)">B</div><div class="ab-def"><strong>Basically Available</strong> — System always responds, even if response is partial or stale. Rejects requests only in extreme failure, not during replication lag.</div></div>
        <div class="ab-row"><div class="ab-letter" style="color:var(--violet)">S</div><div class="ab-def"><strong>Soft State</strong> — System state can change over time even without new inputs. Replicas catching up, caches expiring, tombstones propagating.</div></div>
        <div class="ab-row"><div class="ab-letter" style="color:var(--violet)">E</div><div class="ab-def"><strong>Eventually Consistent</strong> — Given no new updates, all replicas converge to the same state. No guarantee on when. Reads may return stale data.</div></div>
        <div style="margin-top:12px;font-family:'Source Code Pro',monospace;font-size:10px;color:var(--faded);line-height:1.7">
          BASE is not "broken ACID" — it's a deliberate design choice.<br>
          Cassandra, DynamoDB, CouchDB are BASE by design.<br>
          Trade: strong consistency → availability + throughput
        </div>
      </div>
    </div>
  </div>

  <div class="sec-h" style="margin-top:24px">Isolation Levels Deep-Dive</div>
  <table class="big-table">
    <thead><tr><th>ISOLATION LEVEL</th><th>DIRTY READ</th><th>NON-REPEATABLE</th><th>PHANTOM READ</th><th>DEFAULT IN</th></tr></thead>
    <tbody>
      <tr><td>READ UNCOMMITTED</td><td class="noo">Allowed</td><td class="noo">Allowed</td><td class="noo">Allowed</td><td>—</td></tr>
      <tr><td>READ COMMITTED</td><td class="yes">Prevented</td><td class="noo">Allowed</td><td class="noo">Allowed</td><td>PostgreSQL</td></tr>
      <tr><td>REPEATABLE READ</td><td class="yes">Prevented</td><td class="yes">Prevented</td><td class="noo">Allowed</td><td>MySQL InnoDB</td></tr>
      <tr><td>SERIALIZABLE</td><td class="yes">Prevented</td><td class="yes">Prevented</td><td class="yes">Prevented</td><td>Highest isolation</td></tr>
    </tbody>
  </table>
  <div class="alert ice"><em>Interview pattern:</em> Higher isolation level = fewer anomalies but more locking = lower throughput. Most applications run at READ COMMITTED. SERIALIZABLE is used for financial systems where phantom reads would cause incorrect calculations (e.g., calculating remaining inventory before inserting an order).</div>
</div>

<!-- ══ SQL vs NOSQL ══ -->
<div class="view" id="view-sqlnosql">
  <div class="sec-h">SQL vs NoSQL</div>
  <div class="sec-sub">Not a religion — a trade-off based on access patterns and consistency needs</div>

  <table class="big-table">
    <thead><tr><th>DIMENSION</th><th>SQL (Relational)</th><th>NoSQL (Distributed)</th></tr></thead>
    <tbody>
      <tr><td>Data model</td><td>Tables, rows, strict schema, FK constraints</td><td>Documents, KV, wide-column, graph — flexible</td></tr>
      <tr><td>Query language</td><td>SQL — JOIN, GROUP BY, window functions</td><td>Simple API: Get/Put/Scan or limited query DSL</td></tr>
      <tr><td>Consistency</td><td>ACID transactions guaranteed</td><td>BASE; tunable per-operation (Cassandra)</td></tr>
      <tr><td>Scaling</td><td>Vertical + read replicas; sharding is hard</td><td>Horizontal sharding built in (designed for it)</td></tr>
      <tr><td>Use when</td><td>Complex queries, JOINs, transactions, stable schema</td><td>Known simple access patterns, massive scale, flexible schema</td></tr>
      <tr><td>Examples</td><td>PostgreSQL, MySQL, Aurora, SQLite</td><td>DynamoDB, Cassandra, MongoDB, Redis, Neo4j</td></tr>
    </tbody>
  </table>

  <div class="sec-h" style="margin-top:22px">The 5 NoSQL Data Models</div>
  <div class="shard-grid" style="grid-template-columns:repeat(3,1fr)">
    <div class="shard-card">
      <div class="shard-hdr" style="border-left:3px solid var(--ice)">
        <div class="shard-name">Key-Value</div>
        <div class="shard-tag">SIMPLEST · FASTEST</div>
      </div>
      <div class="shard-body">
        Hash map: key → opaque value (string, binary, JSON). O(1) get/put. No query on value internals.
        <div class="shard-pro" style="margin-top:8px">Redis, DynamoDB, Riak<br>Sessions, caching, shopping carts</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr" style="border-left:3px solid var(--mint)">
        <div class="shard-name">Document</div>
        <div class="shard-tag">FLEXIBLE SCHEMA</div>
      </div>
      <div class="shard-body">
        Nested JSON/BSON. Query any field. Schema per document. Partial updates. No joins across documents.
        <div class="shard-pro" style="margin-top:8px">MongoDB, CouchDB, Firestore<br>Catalogs, user profiles, CMS</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr" style="border-left:3px solid var(--gold)">
        <div class="shard-name">Wide-Column</div>
        <div class="shard-tag">WRITE-HEAVY · TIME-SERIES</div>
      </div>
      <div class="shard-body">
        Row key → sorted map of column families. Sparse columns. Efficient range scans on row key. Designed for high-write workloads.
        <div class="shard-pro" style="margin-top:8px">Cassandra, HBase, Bigtable<br>IoT telemetry, analytics, messaging</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr" style="border-left:3px solid var(--violet)">
        <div class="shard-name">Graph</div>
        <div class="shard-tag">RELATIONSHIPS FIRST</div>
      </div>
      <div class="shard-body">
        Nodes (entities) + edges (relationships) + properties. Traverse relationships in O(1) per hop (not O(n) JOIN).
        <div class="shard-pro" style="margin-top:8px">Neo4j, Amazon Neptune, Dgraph<br>Social networks, fraud detection, recommendations</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr" style="border-left:3px solid var(--coral)">
        <div class="shard-name">Time-Series</div>
        <div class="shard-tag">TIMESTAMP OPTIMISED</div>
      </div>
      <div class="shard-body">
        Timestamp + measurement pairs. Optimised for time-range queries, aggregations, and downsampling. Automatic compression.
        <div class="shard-pro" style="margin-top:8px">InfluxDB, TimescaleDB, Prometheus<br>Metrics, monitoring, IoT, financial ticks</div>
      </div>
    </div>
  </div>
</div>

<!-- ══ REPLICATION ══ -->
<div class="view" id="view-replication">
  <div class="sec-h">Replication</div>
  <div class="sec-sub">How to survive node failures and serve more reads</div>

  <div class="rep-diagram">
    <div style="font-family:'Source Code Pro',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;margin-bottom:14px">// PRIMARY-REPLICA (LEADER-FOLLOWER)</div>
    <div class="rep-row">
      <div class="rep-node" style="border-color:var(--coral);color:var(--coral)">WRITE<br>CLIENT</div>
      <div class="rep-arrow">──→</div>
      <div class="rep-node" style="border-color:var(--ice);color:var(--ice)">PRIMARY<br>(accepts writes)</div>
      <div class="rep-arrow">──async──→</div>
      <div class="rep-node" style="border-color:var(--mint);color:var(--mint)">REPLICA 1</div>
      <div class="rep-arrow" style="color:var(--muted)">←── READ CLIENT</div>
    </div>
    <div class="rep-row">
      <div style="width:120px;flex-shrink:0"></div>
      <div style="width:24px;flex-shrink:0"></div>
      <div style="width:130px;flex-shrink:0"></div>
      <div class="rep-arrow">──async──→</div>
      <div class="rep-node" style="border-color:var(--mint);color:var(--mint)">REPLICA 2</div>
      <div class="rep-arrow" style="color:var(--muted)">←── READ CLIENT</div>
    </div>
    <div style="margin-top:12px;font-family:'Source Code Pro',monospace;font-size:9px;color:var(--faded)">
      <span style="color:var(--mint)">✓</span> Scales reads horizontally (add more replicas) &nbsp;
      <span style="color:var(--coral)">✗</span> Replication lag: reads from replica may be stale &nbsp;
      <span style="color:var(--coral)">✗</span> Primary is still single write point
    </div>
  </div>

  <div class="sec-h">Replication Lag — Solutions</div>
  <div class="code-wrap">
    <div class="code-top">Strategies to handle stale reads<span class="code-lang">PATTERNS</span></div>
<pre class="code"><span class="cm">Problem: User updates profile → reads from replica → sees old data (lag ~100ms–2s)</span>
 
<span class="hl">Strategy 1: Read-your-own-writes</span>
  <span class="cm">Route user's reads to PRIMARY for their own data only.</span>
  <span class="cm">How: track last_write_time per user; if recent → route to primary.</span>
  <span class="cm">Cost: extra load on primary for the write author's reads.</span>
 
<span class="hl">Strategy 2: Monotonic Reads</span>
  <span class="cm">Always route same user to same replica.</span>
  <span class="cm">Prevents user seeing data "go backwards" (newer on one replica, older on next).</span>
  <span class="cm">How: Hash(userId) % numReplicas → sticky routing.</span>
 
<span class="hl">Strategy 3: Semi-Synchronous Replication</span>
  <span class="cm">Primary waits for ACK from at least 1 replica before confirming write.</span>
  <span class="cm">Zero data loss on primary crash (at least 1 replica has the write).</span>
  <span class="cm">Cost: write latency += 1 network RTT to replica.</span>
 
<span class="hl">Strategy 4: Route critical paths to primary</span>
  <span class="cm">Payment confirmation, inventory check → always read from primary.</span>
  <span class="cm">Profile photos, comment counts → can read from replica.</span></pre>
  </div>

  <div class="sec-h" style="margin-top:22px">Multi-Primary (Active-Active) Replication</div>
  <table class="big-table">
    <thead><tr><th>ASPECT</th><th>PRIMARY-REPLICA</th><th>MULTI-PRIMARY</th></tr></thead>
    <tbody>
      <tr><td>Write acceptance</td><td>Only primary accepts writes</td><td>Any node accepts writes</td></tr>
      <tr><td>Write scaling</td><td>Limited to primary capacity</td><td>Writes scale across all nodes</td></tr>
      <tr><td>Conflict risk</td><td>None (single writer)</td><td>High — concurrent writes to same row</td></tr>
      <tr><td>Conflict resolution</td><td>N/A</td><td>LWW timestamp, CRDTs, app-level merge</td></tr>
      <tr><td>Use case</td><td>Read-heavy web apps</td><td>Geo-distributed active-active, Cassandra</td></tr>
    </tbody>
  </table>
</div>

<!-- ══ SHARDING ══ -->
<div class="view" id="view-sharding">
  <div class="sec-h">Sharding (Horizontal Partitioning)</div>
  <div class="sec-sub">Distributing rows across multiple DB nodes — when one machine isn't enough</div>

  <div class="shard-grid">
    <div class="shard-card">
      <div class="shard-hdr">
        <div class="shard-name">Range-Based</div>
        <div class="shard-tag">ORDERED · SIMPLE</div>
      </div>
      <div class="shard-body">
        Partition by value range of shard key.<br><br>
        Shard 0: user_id 1–25M<br>
        Shard 1: user_id 25M–50M<br>
        Shard 2: user_id 50M–75M
      </div>
      <div style="padding:0 14px 12px">
        <div class="shard-pro">✓ Range queries on one or few shards<br>✓ Easy to add new shards at tail</div>
        <div class="shard-con">✗ Hot spots if recent data is most active<br>✗ Uneven load if data is skewed</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr">
        <div class="shard-name">Hash-Based</div>
        <div class="shard-tag">EVEN DISTRIBUTION</div>
      </div>
      <div class="shard-body">
        shard = hash(key) % N<br><br>
        user_12345 → hash(12345)%4 → Shard 2<br>
        Uniformly distributes keys regardless of value patterns.
      </div>
      <div style="padding:0 14px 12px">
        <div class="shard-pro">✓ Even distribution, no hot spots<br>✓ Simple deterministic routing</div>
        <div class="shard-con">✗ Range queries → scatter-gather all shards<br>✗ Resharding remaps all keys (painful)</div>
      </div>
    </div>
    <div class="shard-card">
      <div class="shard-hdr">
        <div class="shard-name">Consistent Hashing</div>
        <div class="shard-tag">MINIMAL REHASH · RING</div>
      </div>
      <div class="shard-body">
        Map servers + keys to same hash ring (0→2³²). Each key → nearest server clockwise.<br><br>
        Add/remove server → only K/N keys remapped (vs N times more with mod hash).
      </div>
      <div style="padding:0 14px 12px">
        <div class="shard-pro">✓ Adding/removing nodes is non-disruptive<br>✓ Virtual nodes for even distribution</div>
        <div class="shard-con">✗ More complex to implement<br>✗ Still no range query support</div>
      </div>
    </div>
  </div>

  <div class="alert coral"><em>The Hotkey Problem:</em> A single shard key (Taylor Swift's user_id during a concert drop) gets 100× more traffic than others. Solutions: (1) Key suffixing — distribute post_id_0...post_id_9 across shards; (2) Cache in Redis; (3) Per-shard read replicas. Design your shard key to co-locate related data and distribute write load.</div>

  <div class="sec-h" style="margin-top:22px">Cross-Shard Query Problem</div>
  <div class="code-wrap">
    <div class="code-top">Strategies for queries that span shards<span class="code-lang">PATTERNS</span></div>
<pre class="code"><span class="cm">Problem: SELECT COUNT(*) FROM orders GROUP BY restaurant_id</span>
<span class="cm">         orders are sharded by user_id → restaurant data is spread across all shards</span>
<span class="cm">         → Must query ALL shards and merge results in application layer</span>
 
<span class="hl">Solution 1: Denormalise (NoSQL pattern)</span>
  <span class="cm">Embed related data in the same document.</span>
  <span class="cm">User document includes their recent orders → no cross-shard JOIN needed.</span>
 
<span class="hl">Solution 2: Co-locate by access pattern</span>
  <span class="cm">Shard ALL of a user's data by user_id.</span>
  <span class="cm">Query "all my orders" stays on one shard.</span>
  <span class="cm">But "all orders for this restaurant" still requires scatter-gather.</span>
 
<span class="hl">Solution 3: Separate analytics store</span>
  <span class="cm">Write events to Kafka → consume into data warehouse (BigQuery, Redshift).</span>
  <span class="cm">Cross-tenant/cross-shard analytics run on the warehouse, not the OLTP DB.</span>
 
<span class="hl">Solution 4: Accept scatter-gather for rare queries</span>
  <span class="cm">Fan out to all shards, merge in application layer, cache the result aggressively.</span></pre>
  </div>
</div>

<!-- ══ DB SELECTION ══ -->
<div class="view" id="view-dbselect">
  <div class="sec-h">Database Selection Guide</div>
  <div class="sec-sub">The right database for the right job — based on access patterns, not familiarity</div>

  <div class="db-select">
    <div class="dbs-card"><div class="dbs-q">Need ACID + complex JOINs?</div><div class="dbs-a">PostgreSQL / MySQL / Aurora</div></div>
    <div class="dbs-card"><div class="dbs-q">Need massive write throughput (millions/sec)?</div><div class="dbs-a">Cassandra / DynamoDB</div></div>
    <div class="dbs-card"><div class="dbs-q">Need flexible JSON schema per document?</div><div class="dbs-a">MongoDB / CouchDB / Firestore</div></div>
    <div class="dbs-card"><div class="dbs-q">Need graph traversal (friends-of-friends)?</div><div class="dbs-a">Neo4j / Amazon Neptune</div></div>
    <div class="dbs-card"><div class="dbs-q">Need time-series metrics + monitoring?</div><div class="dbs-a">InfluxDB / TimescaleDB / Prometheus</div></div>
    <div class="dbs-card"><div class="dbs-q">Need full-text search + facets?</div><div class="dbs-a">Elasticsearch / OpenSearch / Algolia</div></div>
    <div class="dbs-card"><div class="dbs-q">Need distributed SQL (geo-global)?</div><div class="dbs-a">CockroachDB / Google Spanner</div></div>
    <div class="dbs-card"><div class="dbs-q">Need in-memory cache / pub-sub / leaderboard?</div><div class="dbs-a">Redis / Memcached</div></div>
  </div>

  <div class="sec-h" style="margin-top:22px">Comparison Matrix</div>
  <table class="big-table">
    <thead><tr><th>DATABASE</th><th>TYPE</th><th>CONSISTENCY</th><th>SCALE</th><th>BEST FOR</th></tr></thead>
    <tbody>
      <tr><td>PostgreSQL</td><td>Relational</td><td>ACID</td><td>Vertical + read replicas</td><td>Complex queries, transactions, analytics</td></tr>
      <tr><td>MySQL / Aurora</td><td>Relational</td><td>ACID</td><td>Vertical + read replicas</td><td>Web apps, proven reliability, Aurora serverless</td></tr>
      <tr><td>MongoDB</td><td>Document</td><td>Tunable</td><td>Horizontal sharding</td><td>Flexible schema, catalogs, user profiles</td></tr>
      <tr><td>Cassandra</td><td>Wide-column</td><td>Eventual / Tunable</td><td>Horizontal (massive)</td><td>High-write IoT, time-series, messaging</td></tr>
      <tr><td>DynamoDB</td><td>KV / Document</td><td>Eventual / Strong</td><td>Horizontal (managed)</td><td>Serverless, variable load, simple access patterns</td></tr>
      <tr><td>Redis</td><td>Key-Value</td><td>Strong (single node)</td><td>Cluster mode</td><td>Cache, sessions, pub/sub, sorted sets</td></tr>
      <tr><td>Elasticsearch</td><td>Search</td><td>Eventual</td><td>Horizontal</td><td>Full-text search, log analysis, facets</td></tr>
      <tr><td>InfluxDB</td><td>Time-series</td><td>Eventual</td><td>Horizontal</td><td>Metrics, monitoring, IoT telemetry</td></tr>
    </tbody>
  </table>

  <div class="sec-h" style="margin-top:22px">Interview Tips</div>
  <table class="big-table">
    <thead><tr><th>QUESTION</th><th>STRONG ANSWER</th></tr></thead>
    <tbody>
      <tr><td>"SQL or NoSQL?"</td><td>Depends on access patterns. Complex JOINs + ACID → SQL. Known simple key lookups + horizontal scale → NoSQL. Tell me the access patterns first.</td></tr>
      <tr><td>"How does B-tree indexing work?"</td><td>Balanced tree keeps keys sorted. Binary search on keys = O(log n). Range queries traverse adjacent leaves. Cost: every write updates all indexes.</td></tr>
      <tr><td>"How to handle a hotkey?"</td><td>Cache in Redis (avoid DB entirely), key suffixing (distribute load across N keys), or per-shard read replicas for the hot shard.</td></tr>
      <tr><td>"Primary vs replica reads?"</td><td>Replica reads are faster but may be stale by replication lag. Use primary for user's own writes (read-your-writes) and financial data. Replica is fine for other users' public data.</td></tr>
      <tr><td>"ACID vs BASE?"</td><td>ACID: all-or-nothing transactions, strong consistency — right for banking, booking. BASE: available, eventually consistent — right for social likes, analytics.</td></tr>
    </tbody>
  </table>
</div>

<!-- ══ TASKS ══ -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-label">Index Design — Orders Table</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
<pre>CREATE TABLE orders (
    id            BIGINT PRIMARY KEY,
    user_id       INT,
    restaurant_id INT,
    status        VARCHAR(20),  -- 'pending', 'delivered', 'cancelled'
    total         DECIMAL(10,2),
    created_at    TIMESTAMP
);
 
Query patterns:
  Q1: All orders for a specific user (most frequent)
  Q2: Recent orders for a restaurant ordered by time
  Q3: All pending orders (dashboard refresh every 5s)
  Q4: Orders by user in a date range
 
For each query:
  1. Design the optimal index (name columns + order)
  2. Explain the B-tree traversal path
  3. Identify if a covering index is possible
  4. Explain the INSERT/UPDATE cost of your index choice
  Bonus: Q3 — would a partial index help? Why?</pre>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-label">Sharding Design — Multi-Tenant SaaS</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>10,000 business tenants, each with 10K–1M records. Most queries scoped to single tenant. 3 large tenants = 60% of traffic. Occasional cross-tenant analytics.</p>
        <ol>
          <li>What is the shard key? Why?</li>
          <li>Which sharding strategy: range, hash, or consistent hashing? Why?</li>
          <li>How do you handle the 3 hot tenants without letting them overload one shard?</li>
          <li>How do you serve cross-tenant analytics without scatter-gathering all shards?</li>
          <li>What happens when a tenant grows 10× — does your design need changes?</li>
        </ol>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-label">Replication Lag Decision Scenarios</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Social media platform: primary DB for writes, 3 read replicas, replication lag 100ms–2s.</p>
        <p>For each, decide: <strong>primary or replica</strong>? Justify with the consistency model needed.</p>
        <ol>
          <li>User views their own profile immediately after updating it</li>
          <li>User views another user's follower count</li>
          <li>User's home feed (posts from people they follow)</li>
          <li>Payment confirmation page after completing a purchase</li>
          <li>Admin dashboard showing total active users (refreshed every 5 min)</li>
        </ol>
      </div>
    </div>

    <div class="task-card" style="border-top:2px solid var(--ice)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--ice)">★</div><div class="t-label">Design Instagram's Storage Layer</div><div class="t-meta">~3 hrs · full HLD</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Design complete storage for Instagram. For each data type: DB choice, CAP position, sharding key, storage estimate.</p>
        <ul>
          <li>User accounts (500M users)</li>
          <li>Photos/Videos (100B media files, avg 3 MB)</li>
          <li>Comments (10B comments)</li>
          <li>Likes (500B likes — read-heavy, approximate count OK)</li>
          <li>Follow relationships (avg 500 followers/user)</li>
          <li>Feed (posts from people you follow — fan-out on write vs read)</li>
        </ul>
        <p style="margin-top:8px">Required: draw the storage architecture diagram, estimate total storage, identify the hardest consistency challenge.</p>
      </div>
    </div>
  </div>
</div>

<!-- ══ CHECKLIST ══ -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 14 completed</span><span>MODULE B2 · DATABASES AT SCALE</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">B-tree indexing: O(log n), left-most prefix rule, range query support</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Composite and covering indexes — when and how to design them</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">ACID — all 4 properties in depth, including isolation levels</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">BASE — deliberate trade-off, when it's the right choice</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">SQL vs NoSQL decision: based on access patterns, not preference</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">All 5 NoSQL data models: KV, Document, Wide-column, Graph, Time-series</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Primary-replica replication + replication lag solutions (4 strategies)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Multi-primary replication — conflict resolution strategies</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Range vs hash vs consistent hashing sharding — trade-offs of each</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Hotkey problem — 3 solutions: cache, key suffixing, read replicas per shard</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Cross-shard query problem and solutions (denorm, co-locate, analytics store)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can pick the right DB for any scenario in the selection guide</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–3 completed (index design, sharding, replication lag)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Capstone: Instagram storage layer — full design with estimates</div></div>
  </div>

  <div style="margin-top:32px;background:var(--panel);border:1px solid var(--bord2);padding:24px;border-top:2px solid var(--ice)">
    <div style="font-family:'Source Code Pro',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;margin-bottom:10px">// NEXT MODULE</div>
    <div style="font-family:'DM Serif Display',serif;font-size:30px;color:var(--bright);margin-bottom:8px">B3 — Caching</div>
    <div style="font-family:'Source Code Pro',monospace;font-size:11px;color:var(--faded);line-height:2">
      Redis data structures · CDN · Cache-aside · Write-through · Write-back<br>
      Cache invalidation strategies · TTL vs eviction · Cache stampede<br>
      Read-through cache · Consistent hashing for distributed cache
    </div>
  </div>
</div>

</div>

<script>
function show(tab, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}
function tt(hd) {
  const bd = hd.nextElementSibling, arr = hd.querySelector('.t-arr');
  bd.classList.toggle('open', !bd.classList.contains('open'));
  arr.classList.toggle('open', !arr.classList.contains('open'));
}
function tick(el) {
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.chk').length;
  const done  = document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done/total)*100}%`;
}
</script>

<script>
function show(tab, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}
function tt(hd) {
  const bd = hd.nextElementSibling, arr = hd.querySelector('.t-arr');
  bd.classList.toggle('open', !bd.classList.contains('open'));
  arr.classList.toggle('open', !arr.classList.contains('open'));
}
function tick(el) {
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.chk').length;
  const done  = document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done/total)*100}%`;
}
</script>

<div class="b2-bottom-nav">
  <a href="/learning/system-design/hld/module-b1-hld-fundamentals/" class="b2-nav-footer-btn">← B1: HLD Fundamentals</a>
  <a href="/learning/system-design/hld/module-b2-notes/" class="b2-nav-footer-btn">📄 Full Notes</a>
  <a href="/learning/system-design/system-design-roadmap/" class="b2-nav-footer-btn">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b3-caching/" class="b2-nav-footer-btn">B3: Caching →</a>
</div>


<script src="/assets/js/sd-module-b2.js" defer></script>