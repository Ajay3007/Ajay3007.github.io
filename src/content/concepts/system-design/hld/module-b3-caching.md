---
title: "Module B3 — Caching | HLD Track"
description: "TRACK B · HLD · MODULE B3 · WEEK 13 CACHING Cache-Aside · Write-Through · Write-Back · Stampede Prevention LRU · LFU · TTL · Redis Structures · CDN · Rate Limiting 10 TOPICS 4…"
domain: system-design
track: system-design-hld
order: 106
url: /learning/system-design/hld/module-b3-caching/
---

<link rel="stylesheet" href="/assets/css/sd-module-b3.css">

<link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,200;0,400;0,600;0,800;1,400&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">

<header>
  <div class="bio-bar"></div>
  <div class="hdr-inner">
    <div>
      <div class="hdr-badge"><div class="pulse-dot"></div>TRACK B · HLD · MODULE B3 · WEEK 13</div>
      <h1><em>CACHING</em></h1>
      <div class="hdr-sub">
        Cache-Aside · Write-Through · Write-Back · Stampede Prevention<br>
        LRU · LFU · TTL · Redis Structures · CDN · Rate Limiting
      </div>
    </div>
    <div class="hdr-depth">
      <div class="depth-bar"><div class="depth-val">10</div><div class="depth-lbl">TOPICS</div></div>
      <div class="depth-bar"><div class="depth-val">4</div><div class="depth-lbl">TASKS</div></div>
      <div class="depth-bar"><div class="depth-val">5</div><div class="depth-lbl">REDIS STRUCTURES</div></div>
      <div class="depth-bar"><div class="depth-val">B3</div><div class="depth-lbl">MODULE</div></div>
    </div>
  </div>
  <div class="speed-strip">
    <div class="speed-item" style="width:60px">
      <div class="speed-bar-wrap"><div class="speed-bar" style="height:4px;background:var(--biolum);color:var(--biolum)"></div></div>
      <div class="speed-val" style="color:var(--biolum)">100ns</div>
      <div class="speed-lbl">RAM</div>
    </div>
    <div class="speed-item" style="width:60px">
      <div class="speed-bar-wrap"><div class="speed-bar" style="height:8px;background:var(--spark);color:var(--spark)"></div></div>
      <div class="speed-val" style="color:var(--spark)">0.5ms</div>
      <div class="speed-lbl">Redis</div>
    </div>
    <div class="speed-item" style="width:60px">
      <div class="speed-bar-wrap"><div class="speed-bar" style="height:22px;background:var(--dusk);color:var(--dusk)"></div></div>
      <div class="speed-val" style="color:var(--dusk)">1-5ms</div>
      <div class="speed-lbl">SSD DB</div>
    </div>
    <div class="speed-item" style="width:60px">
      <div class="speed-bar-wrap"><div class="speed-bar" style="height:38px;background:var(--amber);color:var(--amber)"></div></div>
      <div class="speed-val" style="color:var(--amber)">10-50ms</div>
      <div class="speed-lbl">HDD DB</div>
    </div>
    <div style="margin-left:16px;font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--faded);align-self:center;line-height:1.8">
      Redis is 10–100× faster than a DB query<br>
      In-process cache is 100,000× faster than disk<br>
      <span style="color:var(--biolum)">Cache = trading space for time</span>
    </div>
  </div>
</header>

<nav class="nav">
  <div class="nav-tab active" onclick="show('patterns',this)">Cache Patterns</div>
  <div class="nav-tab" onclick="show('eviction',this)">Eviction</div>
  <div class="nav-tab" onclick="show('invalidation',this)">Invalidation</div>
  <div class="nav-tab" onclick="show('stampede',this)">Stampede</div>
  <div class="nav-tab" onclick="show('redis',this)">Redis Structures</div>
  <div class="nav-tab" onclick="show('cdn',this)">CDN</div>
  <div class="nav-tab" onclick="show('tasks',this)">Tasks</div>
  <div class="nav-tab" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- ══ PATTERNS ══ -->
<div class="view active" id="view-patterns">
  <div class="sec-h">Cache Patterns</div>
  <div class="sec-sub">Four strategies — choose based on consistency needs and write frequency</div>

  <div class="pat-grid">

    <!-- CACHE-ASIDE -->
    <div class="pat-card">
      <div class="pat-hdr" style="border-left:3px solid var(--biolum)">
        <div class="pat-name">Cache-Aside</div>
        <div class="pat-when" style="color:var(--biolum)">MOST COMMON</div>
      </div>
      <div class="pat-body">Application controls all cache interactions. Miss → app fetches DB and populates cache. Write → app invalidates (deletes) cache key.</div>
      <div class="pat-flow">
        <div class="pat-step"><span class="n">R1</span> cache.get(key) → HIT → return</div>
        <div class="pat-step"><span class="n">R2</span> MISS → db.get(key)</div>
        <div class="pat-step"><span class="n">R3</span> cache.set(key, val, TTL)</div>
        <div class="pat-step"><span class="n">W1</span> db.update(key, val)</div>
        <div class="pat-step"><span class="n">W2</span> cache.delete(key) ← safer than update</div>
      </div>
      <div class="pat-pros">✓ Only caches requested data (no wasted memory)<br>✓ DB failures degrade gracefully</div>
      <div class="pat-cons">✗ First request after miss is slow<br>✗ Brief stale window between write and invalidation</div>
    </div>

    <!-- WRITE-THROUGH -->
    <div class="pat-card">
      <div class="pat-hdr" style="border-left:3px solid var(--algae)">
        <div class="pat-name">Write-Through</div>
        <div class="pat-when" style="color:var(--algae)">STRONG CONSISTENCY</div>
      </div>
      <div class="pat-body">Every write goes to BOTH cache and DB synchronously. Client confirmed only after both succeed. Reads always find fresh data in cache.</div>
      <div class="pat-flow">
        <div class="pat-step"><span class="n" style="color:var(--algae)">W1</span> db.write(key, val)</div>
        <div class="pat-step"><span class="n" style="color:var(--algae)">W2</span> cache.set(key, val)</div>
        <div class="pat-step"><span class="n" style="color:var(--algae)">W3</span> confirm to client</div>
        <div class="pat-step"><span class="n" style="color:var(--algae)">R1</span> cache.get(key) → always fresh</div>
      </div>
      <div class="pat-pros">✓ Read-after-write consistency guaranteed<br>✓ Cache always has latest data</div>
      <div class="pat-cons">✗ Adds latency to every write (two writes)<br>✗ Caches data that may never be re-read</div>
    </div>

    <!-- WRITE-BACK -->
    <div class="pat-card">
      <div class="pat-hdr" style="border-left:3px solid var(--amber)">
        <div class="pat-name">Write-Back</div>
        <div class="pat-when" style="color:var(--amber)">HIGH-WRITE WORKLOADS</div>
      </div>
      <div class="pat-body">Write to cache immediately (fast ACK). DB updated asynchronously in background. Risk: data loss if cache crashes before flush.</div>
      <div class="pat-flow">
        <div class="pat-step"><span class="n" style="color:var(--amber)">W1</span> cache.set(key, val) → ACK client</div>
        <div class="pat-step"><span class="n" style="color:var(--amber)">W2</span> (background) db.write(key, val)</div>
        <div class="pat-step"><span class="n" style="color:var(--amber)">R1</span> cache.get(key) → always fresh</div>
      </div>
      <div class="pat-pros">✓ Lowest write latency<br>✓ Batches DB writes (more efficient)</div>
      <div class="pat-cons">✗ Data loss if cache crashes before flush<br>✗ DB temporarily inconsistent with cache</div>
    </div>

    <!-- READ-THROUGH -->
    <div class="pat-card">
      <div class="pat-hdr" style="border-left:3px solid var(--spark)">
        <div class="pat-name">Read-Through</div>
        <div class="pat-when" style="color:var(--spark)">SIMPLE APP CODE</div>
      </div>
      <div class="pat-body">Cache layer transparently fetches from DB on miss. Application talks only to cache — never to DB directly. Cache library handles miss logic.</div>
      <div class="pat-flow">
        <div class="pat-step"><span class="n" style="color:var(--spark)">R1</span> app.get(key) → asks cache</div>
        <div class="pat-step"><span class="n" style="color:var(--spark)">R2</span> cache HIT → return val</div>
        <div class="pat-step"><span class="n" style="color:var(--spark)">R3</span> MISS → cache fetches DB</div>
        <div class="pat-step"><span class="n" style="color:var(--spark)">R4</span> cache stores + returns val</div>
      </div>
      <div class="pat-pros">✓ Simpler application code<br>✓ Cache manages all miss logic</div>
      <div class="pat-cons">✗ Cold start: all first reads slow<br>✗ Less control over what gets cached</div>
    </div>

  </div>

  <div class="code-wrap">
    <div class="code-top">Cache-Aside in Java — the full pattern<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">UserService</span> {
    <span class="kw">private final</span> <span class="cls">Cache</span>  cache;
    <span class="kw">private final</span> <span class="cls">UserDB</span> db;

    <span class="kw">public</span> <span class="cls">User</span> <span class="fn">getUser</span>(<span class="kw">long</span> userId) {
        <span class="cls">String</span> key = <span class="str">"user:"</span> + userId;

        <span class="cls">User</span> cached = cache.<span class="fn">get</span>(key);
        <span class="kw">if</span> (cached != <span class="kw">null</span>) <span class="kw">return</span> cached;   <span class="cm">// ✅ CACHE HIT</span>

        <span class="cls">User</span> user = db.<span class="fn">findById</span>(userId);        <span class="cm">// DB query</span>
        cache.<span class="fn">set</span>(key, user, <span class="cls">Duration</span>.<span class="fn">ofMinutes</span>(<span class="str">30</span>)); <span class="cm">// Populate with TTL</span>
        <span class="kw">return</span> user;                            <span class="cm">// CACHE MISS</span>
    }

    <span class="kw">public void</span> <span class="fn">updateUser</span>(<span class="kw">long</span> userId, <span class="cls">UserUpdate</span> update) {
        db.<span class="fn">update</span>(userId, update);
        cache.<span class="fn">delete</span>(<span class="str">"user:"</span> + userId); <span class="cm">// ← DELETE safer than SET (avoids stale-write race)</span>
    }
}</pre>
  </div>

  <div class="alert bio"><em>Hit rate target:</em> Cache is only worthwhile if hit rate exceeds ~80%. Monitor your cache hit rate constantly. If it's low: cache size too small, TTL too short, or you're caching long-tail data that's rarely re-read.</div>
</div>

<!-- ══ EVICTION ══ -->
<div class="view" id="view-eviction">
  <div class="sec-h">Eviction Policies</div>
  <div class="sec-sub">When the cache is full — which entry gets removed?</div>

  <div class="evict-grid">
    <div class="evict-card" style="border-top-color:var(--biolum)">
      <div class="evict-name" style="color:var(--biolum)">LRU</div>
      <div class="evict-body">Least Recently Used. Evict entry not accessed for longest time. Recently accessed = likely to be re-accessed.</div>
      <div class="evict-impl" style="color:var(--biolum)">Implementation: DoublyLinkedList + HashMap<br>O(1) get, O(1) put, O(1) evict<br>Default in Redis (allkeys-lru)</div>
    </div>
    <div class="evict-card" style="border-top-color:var(--algae)">
      <div class="evict-name" style="color:var(--algae)">LFU</div>
      <div class="evict-body">Least Frequently Used. Evict entry with fewest total accesses. Avoids cache pollution from one-time large scans.</div>
      <div class="evict-impl" style="color:var(--algae)">Implementation: HashMap + frequency heap<br>O(1) amortised with Min-Heap<br>Redis allkeys-lfu (since Redis 4.0)</div>
    </div>
    <div class="evict-card" style="border-top-color:var(--amber)">
      <div class="evict-name" style="color:var(--amber)">TTL</div>
      <div class="evict-body">Time-To-Live. Each entry has an expiry timestamp. After TTL, entry is invalid and re-fetched on next access.</div>
      <div class="evict-impl" style="color:var(--amber)">cache.set(key, val, 3600)<br>Use TTL jitter to avoid stampede:<br>TTL = base + random(0, base*0.1)</div>
    </div>
  </div>

  <div class="code-wrap">
    <div class="code-top">LRU Cache — DoublyLinkedList + HashMap (O(1) all ops)<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">LRUCache</span> {
    <span class="kw">private final int</span>                          capacity;
    <span class="kw">private final</span> <span class="cls">Map</span>&lt;<span class="kw">int</span>, <span class="cls">Node</span>&gt;             map = <span class="kw">new</span> <span class="cls">HashMap</span>&lt;&gt;();
    <span class="kw">private final</span> <span class="cls">Node</span>                        head, tail; <span class="cm">// Sentinel nodes</span>
    <span class="kw">private final</span> <span class="cls">ReentrantReadWriteLock</span>      lock = <span class="kw">new</span> <span class="cls">ReentrantReadWriteLock</span>();

    <span class="kw">public int</span> <span class="fn">get</span>(<span class="kw">int</span> key) {
        lock.<span class="fn">readLock</span>().<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="cls">Node</span> n = map.<span class="fn">get</span>(key);
            <span class="kw">if</span> (n == <span class="kw">null</span>) <span class="kw">return</span> -<span class="str">1</span>;
            <span class="fn">moveToFront</span>(n);  <span class="cm">// Most-recently-used → head</span>
            <span class="kw">return</span> n.val;
        } <span class="kw">finally</span> { lock.<span class="fn">readLock</span>().<span class="fn">unlock</span>(); }
    }

    <span class="kw">public void</span> <span class="fn">put</span>(<span class="kw">int</span> key, <span class="kw">int</span> val) {
        lock.<span class="fn">writeLock</span>().<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="kw">if</span> (map.<span class="fn">containsKey</span>(key)) {
                <span class="cls">Node</span> n = map.<span class="fn">get</span>(key); n.val = val; <span class="fn">moveToFront</span>(n);
            } <span class="kw">else</span> {
                <span class="cls">Node</span> n = <span class="kw">new</span> <span class="cls">Node</span>(key, val);
                map.<span class="fn">put</span>(key, n); <span class="fn">addToFront</span>(n);
                <span class="kw">if</span> (map.<span class="fn">size</span>() > capacity) <span class="fn">evictTail</span>(); <span class="cm">// Remove LRU</span>
            }
        } <span class="kw">finally</span> { lock.<span class="fn">writeLock</span>().<span class="fn">unlock</span>(); }
    }
}</pre>
  </div>

  <div class="alert amb"><em>TTL Jitter pattern:</em> If many cache keys share the same TTL, they all expire simultaneously → thundering herd. Always add random jitter: TTL = base_ttl + random(0, base_ttl * 0.1). This spreads expiry events across time and prevents concurrent stampedes.</div>
</div>

<!-- ══ INVALIDATION ══ -->
<div class="view" id="view-invalidation">
  <div class="sec-h">Cache Invalidation</div>
  <div class="sec-sub">"Only two hard things in CS: cache invalidation and naming things" — Phil Karlton</div>

  <div class="code-wrap">
    <div class="code-top">Three invalidation strategies compared<span class="clang">PATTERNS</span></div>
<pre class="code"><span class="hl">Strategy 1: Delete on Write (safest, most common)</span>
<span class="fn">void</span> <span class="fn">updateProduct</span>(id, product) {
    db.<span class="fn">update</span>(id, product);
    cache.<span class="fn">delete</span>(<span class="str">"product:"</span> + id);                          <span class="cm">// ← DELETE, not SET</span>
    cache.<span class="fn">delete</span>(<span class="str">"products:category:"</span> + product.categoryId); <span class="cm">// ← invalidate list too</span>
}
<span class="cm">// Next read misses → fetches fresh from DB → repopulates</span>
<span class="cm">// Safe: avoids stale-write race condition</span>

<span class="hl">Strategy 2: Version-Based Keys (no explicit invalidation)</span>
<span class="cm">// Embed version in key. When data changes, bump version.</span>
<span class="str">"product:42:v8"</span>  →  <span class="str">"product:42:v9"</span>   <span class="cm">// old key naturally expires via TTL</span>
<span class="cm">// Application always reads latest version key.</span>
<span class="cm">// Great for: config data, feature flags, rarely-changing reference data</span>

<span class="hl">Strategy 3: Event-Based (CDC + Kafka)</span>
<span class="cm">// DB → Change Data Capture → Kafka → Cache Invalidation Service → Redis.delete(key)</span>
DB_writes → Debezium/CDC → Kafka.<span class="fn">publish</span>(change_event) → CacheConsumer → cache.<span class="fn">delete</span>(key)
<span class="cm">// Decoupled, real-time, works for distributed caches</span>
<span class="cm">// Cost: more infrastructure, event delivery latency, ordering guarantees needed</span></pre>
  </div>

  <div class="code-wrap">
    <div class="code-top">The Invalidation Race Condition — and how to prevent it<span class="clang">CONCURRENT</span></div>
<pre class="code"><span class="cm">// Timeline of a nasty race:</span>
Thread A: <span class="fn">UPDATE</span> product WHERE id=42        <span class="cm">// starts write</span>
Thread B: <span class="fn">SELECT</span> product WHERE id=42 → MISS   <span class="cm">// reads old DB value (before A commits)</span>
Thread A: cache.<span class="fn">delete</span>(<span class="str">"product:42"</span>)         <span class="cm">// invalidates</span>
Thread B: cache.<span class="fn">set</span>(<span class="str">"product:42"</span>, stale_val) <span class="cm">// writes OLD value back!</span>
<span class="cm">// Result: cache holds stale data indefinitely until TTL expires 😱</span>

<span class="hl">Prevention:</span>
<span class="cm">  1. Use TTL as a safety net — even if stale, it expires eventually</span>
<span class="cm">  2. Use CAS (Compare-And-Set) — only write to cache if key still absent</span>
<span class="cm">     cache.setnx("product:42", freshVal)  ← only sets if key doesn't exist</span>
<span class="cm">  3. Use write lock during update:</span>
     db.<span class="fn">beginTransaction</span>();
     db.<span class="fn">update</span>(id, product);
     cache.<span class="fn">delete</span>(key);        <span class="cm">// ← delete INSIDE transaction before commit</span>
     db.<span class="fn">commit</span>();</pre>
  </div>

  <div class="alert bad"><em>Never "update" cache on write — always delete.</em> If you SET the cache on write and also SET it on read-miss, two concurrent operations can race to write stale vs fresh values. Deleting is atomic and safe — the next read will always get fresh data from the DB.</div>
</div>

<!-- ══ STAMPEDE ══ -->
<div class="view" id="view-stampede">
  <div class="sec-h">Cache Stampede (Thundering Herd)</div>
  <div class="sec-sub">When a popular cache key expires — 10,000 concurrent requests all hit the DB</div>

  <div class="stampede-demo">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;margin-bottom:12px">// STAMPEDE VISUALISED — popular key expires at T=0</div>
    <div class="stamp-row">
      <div class="stamp-lbl">DB load</div>
      <div class="stamp-track"><div class="stamp-fill sf1"></div></div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--danger);width:60px">OVERLOAD</div>
    </div>
    <div class="stamp-row">
      <div class="stamp-lbl">Latency</div>
      <div class="stamp-track"><div class="stamp-fill sf2"></div></div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--amber);width:60px">SPIKING</div>
    </div>
    <div class="stamp-row">
      <div class="stamp-lbl">Cache hit</div>
      <div class="stamp-track"><div class="stamp-fill sf3"></div></div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--biolum);width:60px">RESTORING</div>
    </div>
    <div style="margin-top:10px;font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--danger)">⚡ All concurrent misses pile onto DB simultaneously → overload → latency cascade</div>
  </div>

  <div class="code-wrap">
    <div class="code-top">Three stampede prevention strategies<span class="clang">PATTERNS</span></div>
<pre class="code"><span class="hl">Strategy 1: Mutex/Lock on Miss (most reliable)</span>
<span class="cls">String</span> <span class="fn">get</span>(<span class="cls">String</span> key) {
    <span class="cls">String</span> val = cache.<span class="fn">get</span>(key);
    <span class="kw">if</span> (val != <span class="kw">null</span>) <span class="kw">return</span> val;                 <span class="cm">// HIT — fast path</span>

    <span class="cm">// MISS — exactly ONE thread refreshes; others wait</span>
    <span class="kw">boolean</span> locked = cache.<span class="fn">setnx</span>(<span class="str">"lock:"</span>+key, <span class="str">"1"</span>, <span class="str">10_seconds</span>);
    <span class="kw">if</span> (locked) {
        <span class="kw">try</span> {
            val = db.<span class="fn">get</span>(key);
            cache.<span class="fn">set</span>(key, val, TTL);
            <span class="kw">return</span> val;
        } <span class="kw">finally</span> { cache.<span class="fn">delete</span>(<span class="str">"lock:"</span>+key); }
    } <span class="kw">else</span> {
        <span class="cls">Thread</span>.<span class="fn">sleep</span>(<span class="str">50</span>); <span class="kw">return</span> <span class="fn">get</span>(key); <span class="cm">// Retry — lock holder will populate cache</span>
    }
}

<span class="hl">Strategy 2: Probabilistic Early Expiration (PER)</span>
<span class="cm">// Before TTL expires, probabilistically start refreshing</span>
<span class="kw">if</span> (ttlRemaining &lt; -<span class="fn">Math.log</span>(<span class="fn">random</span>()) * recomputeTime) {
    <span class="fn">refresh</span>(); <span class="cm">// One request triggers early refresh; others get (slightly stale) cached value</span>
}

<span class="hl">Strategy 3: Background Refresh (keep popular keys always warm)</span>
<span class="cm">// Scheduled job: refresh popular keys 30s before TTL expires</span>
<span class="cm">// Requires: popularity tracking (hit count per key)</span>
scheduler.<span class="fn">scheduleAtFixedRate</span>(() -> hotKeys.<span class="fn">forEach</span>(k -> cache.<span class="fn">refresh</span>(k)), <span class="str">30</span>, <span class="str">30</span>, SECONDS);</pre>
  </div>

  <div class="alert bio"><em>CDN stale-while-revalidate:</em> Modern CDNs support Cache-Control: stale-while-revalidate=30 — serve stale content immediately while refreshing in background. This eliminates cache misses for CDN-served content entirely. The same principle applies to application-level caches.</div>
</div>

<!-- ══ REDIS ══ -->
<div class="view" id="view-redis">
  <div class="sec-h">Redis Data Structures</div>
  <div class="sec-sub">Five structures — each optimised for a specific access pattern</div>

  <div class="redis-grid">
    <div class="redis-card">
      <div class="redis-hdr" style="border-left:3px solid var(--biolum)">
        <div class="redis-icon">🔑</div>
        <div>
          <div class="redis-name">String</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--faded)">KEY → VALUE</div>
        </div>
      </div>
      <div class="redis-cmds">
SET  user:42:name "Ajay"<br>
GET  user:42:name<br>
INCR view_count:post:123<br>
SETEX session:abc 3600 data
      </div>
      <div class="redis-use" style="color:var(--biolum)">USE: Counters, flags, sessions, rate limit tokens, feature flags</div>
    </div>

    <div class="redis-card">
      <div class="redis-hdr" style="border-left:3px solid var(--algae)">
        <div class="redis-icon">📦</div>
        <div>
          <div class="redis-name">Hash</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--faded)">KEY → {FIELD: VALUE}</div>
        </div>
      </div>
      <div class="redis-cmds">
HSET user:42 name "Ajay" tier "pro"<br>
HGET user:42 name<br>
HMGET user:42 name tier email<br>
HINCRBY user:42 login_count 1
      </div>
      <div class="redis-use" style="color:var(--algae)">USE: User profiles, config objects, shopping carts — fetch individual fields</div>
    </div>

    <div class="redis-card">
      <div class="redis-hdr" style="border-left:3px solid var(--spark)">
        <div class="redis-icon">📋</div>
        <div>
          <div class="redis-name">List</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--faded)">ORDERED · DUPLICATES OK</div>
        </div>
      </div>
      <div class="redis-cmds">
RPUSH queue:email email1 email2<br>
LPOP  queue:email<br>
LRANGE feed:user:42 0 49<br>
LLEN  queue:email
      </div>
      <div class="redis-use" style="color:var(--spark)">USE: Job queues (FIFO), activity feeds, recent items, notifications</div>
    </div>

    <div class="redis-card">
      <div class="redis-hdr" style="border-left:3px solid var(--amber)">
        <div class="redis-icon">🎯</div>
        <div>
          <div class="redis-name">Set</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--faded)">UNIQUE MEMBERS</div>
        </div>
      </div>
      <div class="redis-cmds">
SADD  active_users 42 88 123<br>
SISMEMBER active_users 42<br>
SUNION  tags:post:1 tags:post:2<br>
SINTER  followers:A followers:B
      </div>
      <div class="redis-use" style="color:var(--amber)">USE: Tagging, unique visitor tracking, mutual friends, union/intersection</div>
    </div>

    <div class="redis-card">
      <div class="redis-hdr" style="border-left:3px solid var(--danger)">
        <div class="redis-icon">🏆</div>
        <div>
          <div class="redis-name">Sorted Set</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--faded)">SCORE-RANKED MEMBERS</div>
        </div>
      </div>
      <div class="redis-cmds">
ZADD  leaderboard 9800 "alice"<br>
ZRANGE lb 0 9 WITHSCORES REV<br>
ZADD  rate:user:42 {ts} {reqId}<br>
ZRANGEBYSCORE rate:user:42 (now-60) now
      </div>
      <div class="redis-use" style="color:var(--danger)">USE: Leaderboards, sliding window rate limiting, priority queues, geo proximity</div>
    </div>
  </div>

  <div class="code-wrap">
    <div class="code-top">Sliding Window Rate Limiter — Redis Sorted Set<span class="clang">REDIS</span></div>
<pre class="code"><span class="cm">// Per-user: 100 requests per 60-second window</span>
<span class="cm">// ZADD rate_limit:{userId} {timestamp_ms} {unique_request_id}</span>
<span class="cm">// ZRANGEBYSCORE rate_limit:{userId} (now-60000) now → requests in last 60s</span>

<span class="kw">boolean</span> <span class="fn">isAllowed</span>(<span class="cls">String</span> userId, <span class="kw">int</span> limit, <span class="kw">long</span> windowMs) {
    <span class="kw">long</span>   now        = <span class="cls">System</span>.<span class="fn">currentTimeMillis</span>();
    <span class="kw">long</span>   windowStart = now - windowMs;
    <span class="cls">String</span> key        = <span class="str">"rate:"</span> + userId;

    <span class="kw">return</span> redis.<span class="fn">pipeline</span>(pipe -> {
        pipe.<span class="fn">zremrangebyscore</span>(key, <span class="str">0</span>, windowStart);          <span class="cm">// Remove expired entries</span>
        pipe.<span class="fn">zadd</span>(key, now, <span class="cls">UUID</span>.<span class="fn">randomUUID</span>().<span class="fn">toString</span>()); <span class="cm">// Add this request</span>
        pipe.<span class="fn">zcard</span>(key);                                       <span class="cm">// Count in window</span>
        pipe.<span class="fn">expire</span>(key, windowMs / <span class="str">1000</span>);                    <span class="cm">// Auto-expire key</span>
    }).<span class="fn">getCard</span>() &lt;= limit;
}
<span class="cm">// ✅ Exact sliding window · ✅ Multi-server safe (shared Redis)</span>
<span class="cm">// Memory: O(requests in window) per user — scale with caution for large limits</span></pre>
  </div>
</div>

<!-- ══ CDN ══ -->
<div class="view" id="view-cdn">
  <div class="sec-h">CDN — Content Delivery Network</div>
  <div class="sec-sub">Geographic caching at the edge — serving content from nearest node</div>

  <div class="cdn-diagram">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;margin-bottom:16px">// WITHOUT CDN vs WITH CDN</div>
    <div class="cdn-row">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--faded);width:100px">No CDN:</div>
      <div class="cdn-node" style="border-color:var(--biolum);color:var(--biolum)">User<br>(Mumbai)</div>
      <div class="cdn-arr">──────────────────────→</div>
      <div class="cdn-node" style="border-color:var(--amber);color:var(--amber)">Origin<br>(US-East)</div>
      <div style="margin-left:12px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--danger)">~200ms every request</div>
    </div>
    <div class="cdn-row" style="margin-top:14px">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--faded);width:100px">With CDN:</div>
      <div class="cdn-node" style="border-color:var(--biolum);color:var(--biolum)">User<br>(Mumbai)</div>
      <div class="cdn-arr">──→</div>
      <div class="cdn-node" style="border-color:var(--algae);color:var(--algae)">CDN Edge<br>(Singapore)</div>
      <div class="cdn-arr">← HIT</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--algae);margin-left:8px">~15ms ✅</div>
    </div>
    <div class="cdn-row">
      <div style="width:100px"></div>
      <div style="width:90px"></div>
      <div style="width:20px"></div>
      <div class="cdn-node" style="border-color:var(--algae);color:var(--algae)">CDN Edge<br>(Singapore)</div>
      <div class="cdn-arr">──MISS──→</div>
      <div class="cdn-node" style="border-color:var(--amber);color:var(--amber)">Origin<br>(US-East)</div>
      <div style="margin-left:8px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--faded)">~200ms (first time only)</div>
    </div>
  </div>

  <div class="code-wrap">
    <div class="code-top">Cache-Control headers for static vs dynamic vs private<span class="clang">HTTP</span></div>
<pre class="code"><span class="cm">// STATIC content (images, CSS, JS, fonts)</span>
<span class="hl">Cache-Control: max-age=31536000, immutable</span>
<span class="cm">// CDN caches for 1 year. Use hash-based filenames for cache busting.</span>
app.js → app.<span class="str">8f3d92ab</span>.js   <span class="cm">// Content hash in filename → new deploy = new URL = fresh CDN cache</span>

<span class="cm">// DYNAMIC content (API responses, partially personalised pages)</span>
<span class="hl">Cache-Control: max-age=60, stale-while-revalidate=30</span>
<span class="cm">// CDN caches for 60s. During next 30s after expiry, serve stale while fetching fresh.</span>
<span class="cm">// Eliminates miss latency for CDN — no thundering herd at origin.</span>

<span class="cm">// PRIVATE content (user-specific responses)</span>
<span class="hl">Cache-Control: private, no-store</span>
<span class="cm">// CDN does NOT cache. Request always reaches origin. Each user's data is unique.</span>

<span class="cm">// Vary header — separate cache per encoding/format</span>
<span class="hl">Vary: Accept-Encoding</span>
<span class="cm">// CDN stores separate versions for gzip and uncompressed.</span></pre>
  </div>

  <div class="tips-tbl" style="margin-top:20px">
    <caption style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;text-align:left;padding-bottom:8px;caption-side:top">INTERVIEW TIPS — CACHING</caption>
  </div>
  <table class="tips-tbl">
    <thead><tr><th>QUESTION</th><th>STRONG ANSWER</th></tr></thead>
    <tbody>
      <tr><td>"How does cache-aside work?"</td><td>Application checks cache; on miss queries DB and populates with TTL. On write, deletes (not updates) cache key. Delete is safer — avoids stale-write race.</td></tr>
      <tr><td>"What is thundering herd?"</td><td>Popular key expires → thousands of concurrent misses all query DB simultaneously → overload. Prevention: mutex lock on miss, probabilistic early expiration, or background refresh.</td></tr>
      <tr><td>"Write-through vs write-back?"</td><td>Write-through: strong consistency, adds write latency. Write-back: fast writes, risk of data loss if cache crashes before flush. Use write-back for non-critical high-frequency counters (view counts).</td></tr>
      <tr><td>"Redis data structure for rate limiting?"</td><td>Sorted Set with score=timestamp, member=requestId. Sliding window: ZRANGEBYSCORE in (now-window, now) + ZCARD = count in window. Atomic with pipeline.</td></tr>
      <tr><td>"How to handle cache invalidation?"</td><td>Delete on write is safest. TTL as safety net. For complex dependencies, event-based invalidation via CDC + Kafka. Never set stale value — always delete and let next read fetch fresh.</td></tr>
    </tbody>
  </table>
</div>

<!-- ══ TASKS ══ -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-label">Cache Strategy Selection — 6 Scenarios</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>For each: choose cache-aside / write-through / write-back / no-cache. Justify including the consistency trade-off you're accepting.</p>
        <ol>
          <li>E-commerce product page (price + inventory — overselling is bad)</li>
          <li>Social media post like count (500M likes/day)</li>
          <li>Bank account balance before authorising a debit</li>
          <li>User authentication session (JWT + server-side session)</li>
          <li>Trending hashtags computed every 5 minutes</li>
          <li>Real-time stock price feed (traders need latest price)</li>
        </ol>
        <p style="margin-top:10px">For each wrong choice: what bad outcome would it cause?</p>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-label">Thread-Safe LRU Cache with TTL</div><div class="t-meta">~2 hrs · code</div><div class="t-arr">›</div></div>
      <div class="task-bd">
<pre>API:
  int get(int key)                          → -1 if absent or expired
  void put(int key, int value, long ttlMs)  → evict LRU if at capacity

Requirements:
  - O(1) get and put (DoublyLinkedList + HashMap)
  - Thread-safe: concurrent get/put from multiple threads
  - TTL per entry: expired entries not returned, evicted lazily on access
  - Bonus: background sweeper thread evicts expired entries proactively

Test: 8 threads × 100K ops, verify:
  - Zero ConcurrentModificationException
  - Eviction order correct (LRU evicted first, not MRU)
  - TTL respected: entries expired after their TTL not returned</pre>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-label">Cache Stampede Prevention Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>A news website homepage is cached in Redis with TTL=60s. The homepage is computed from 50 DB queries taking 500ms. The site has 1M concurrent users.</p>
        <p style="margin-top:8px">Problem: Every 60 seconds, a stampede floods the DB with 50K simultaneous queries.</p>
        <p style="margin-top:8px">Design a solution that:</p>
        <ol>
          <li>Eliminates the stampede completely</li>
          <li>Keeps homepage latency &lt;50ms for 99% of requests</li>
          <li>Handles Redis failure gracefully (fallback strategy)</li>
          <li>Explain the consistency trade-off you're making</li>
        </ol>
        <p style="margin-top:8px">Pick one of the three strategies (mutex, PER, background refresh) and justify why it's best for this scenario.</p>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--biolum)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--biolum)">★</div><div class="t-label">Distributed Rate Limiter — 3 Algorithms</div><div class="t-meta">~2 hrs · code</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Implement a distributed rate limiter: 100 requests per 60-second window per user. Multi-server deployment with shared Redis.</p>
<pre>Implement all three and compare:

A) Fixed Window Counter:
   INCR rate:{userId}:{minute}
   EXPIRE rate:{userId}:{minute} 60
   Simple but allows burst at window boundary:
   100 at 0:59 + 100 at 1:00 = 200 requests in 2 seconds

B) Sliding Window Log (Sorted Set):
   ZADD rate:{userId} {timestamp} {requestId}
   ZREMRANGEBYSCORE to remove old entries
   ZCARD for count in window
   Exact but O(requests) memory per user

C) Sliding Window Counter (hybrid):
   Count of previous window × (1 - elapsed/window) + current window count
   Approximate but O(1) memory

For each:
  - Show Redis commands
  - Time complexity per request
  - Memory per user
  - Accuracy at window boundary
  - When to use in production</pre>
      </div>
    </div>
  </div>
</div>

<!-- ══ CHECKLIST ══ -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 13 completed</span><span>MODULE B3 · CACHING</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know the latency numbers: RAM vs Redis vs DB — WHY cache works</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Cache-aside: full read + write path, why delete is safer than update</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Write-through vs write-back: trade-offs and when each is appropriate</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">LRU: DoublyLinkedList + HashMap implementation, O(1) all ops</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">LFU vs LRU: when LFU is better (avoids cache pollution from scans)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">TTL jitter: why it prevents stampede and how to implement</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Cache invalidation race condition: why delete is safe, update is not</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Cache stampede: 3 prevention strategies (mutex, PER, background refresh)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">All 5 Redis data structures + their use cases</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sliding window rate limiter using Redis Sorted Set</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">CDN: static vs dynamic caching, cache busting, stale-while-revalidate</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–3: strategy selection, LRU with TTL, stampede design</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Capstone: distributed rate limiter — all 3 algorithms implemented</div></div>
  </div>

  <div style="margin-top:32px;background:var(--abyss);border:1px solid var(--edge);padding:24px;border-top:2px solid var(--biolum)">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--faded);letter-spacing:2px;margin-bottom:10px">// NEXT MODULE</div>
    <div style="font-family:'Exo 2',sans-serif;font-size:28px;font-weight:800;color:var(--bright);margin-bottom:8px">B4 — Message Queues</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--faded);line-height:2">
      Why async messaging · Kafka architecture + partitions + consumer groups<br>
      RabbitMQ vs Kafka · At-least-once vs exactly-once · Dead letter queues<br>
      Fan-out patterns · Event sourcing · CQRS · Backpressure
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

<div class="b3-bottom-nav">
  <a href="/learning/system-design/hld/module-b2-databases-at-scale/" class="b3-nav-footer-btn">← B2: Databases at Scale</a>
  <a href="/learning/system-design/hld/module-b3-notes/" class="b3-nav-footer-btn">📄 Full Notes</a>
  <a href="/learning/system-design/system-design-roadmap/" class="b3-nav-footer-btn">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b4-message-queues/" class="b3-nav-footer-btn">B4: Message Queues →</a>
</div>


<script src="/assets/js/sd-module-b3.js" defer></script>