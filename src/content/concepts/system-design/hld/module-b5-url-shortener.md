---
title: "Module B5 — URL Shortener"
description: "Track B · HLD Case Study · Module B5 · Week 15 URL Shortener END-TO-END HLD CASE STUDY 300M URLS · 100:1 READ:WRITE · 10ms REDIRECT 3.5T UNIQUE CODES 150GB STORAGE 99% CACHE…"
domain: system-design
track: system-design-hld
order: 110
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b5-url-shortener/
---

<link rel="stylesheet" href="/assets/css/sd-module-b5.css">
<div class="mb5-wrap">
<header>
  <div class="hdr-rule"></div>
  <div class="hdr-inner">
<div>
<div class="hdr-eye">Track B · HLD Case Study · Module B5 · Week 15</div>
<h1>URL<br><span class="acc">Shortener</span></h1>
<div class="hdr-sub">END-TO-END HLD CASE STUDY<br>300M URLS · 100:1 READ:WRITE · &lt;10ms REDIRECT</div>
</div>
<div class="hdr-stats">
<div class="hs"><div class="hs-v">3.5T</div><div class="hs-l">UNIQUE CODES</div></div>
<div class="hs"><div class="hs-v">150GB</div><div class="hs-l">STORAGE</div></div>
<div class="hs"><div class="hs-v">99%</div><div class="hs-l">CACHE HIT</div></div>
<div class="hs"><div class="hs-v">B5</div><div class="hs-l">MODULE</div></div>
</div>
  </div>
  <div class="req-strip">
<div class="req-tag" style="border-color:var(--rust);color:var(--rust)">POST /shorten</div>
<div class="req-tag" style="border-color:var(--amber);color:var(--amber)">GET /{code} → 302</div>
<div class="req-tag" style="border-color:var(--grn);color:var(--grn)">base62 encoding</div>
<div class="req-tag" style="border-color:var(--blu);color:var(--blu)">Redis cache</div>
<div class="req-tag" style="border-color:var(--pur);color:var(--pur)">Kafka analytics</div>
<div class="req-tag" style="border-color:var(--faded);color:var(--faded)">Rate limiting</div>
<div class="req-tag" style="border-color:var(--amber);color:var(--amber)">Expiry / TTL</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="show('req',this)">Requirements</div>
  <div class="nt" onclick="show('est',this)">Estimation</div>
  <div class="nt" onclick="show('arch',this)">Architecture</div>
  <div class="nt" onclick="show('codegen',this)">Code Generation</div>
  <div class="nt" onclick="show('schema',this)">DB Schema</div>
  <div class="nt" onclick="show('cache',this)">Caching</div>
  <div class="nt" onclick="show('redirect',this)">301 vs 302</div>
  <div class="nt" onclick="show('edge',this)">Edge Cases</div>
  <div class="nt" onclick="show('framework',this)">Framework</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- REQUIREMENTS -->
<div class="view active" id="view-req">
  <div class="sh">Requirements</div>
  <div class="sr">Functional + Non-Functional — establish scope before drawing any boxes</div>
  <div class="req-grid">
<div class="req-card" style="border-top-color:var(--rust)">
<div class="rc-title" style="color:var(--rust)">Functional Requirements</div>
<div class="rc-list">
        POST /shorten → given long URL, return short code<br>
        GET /{code}   → redirect to original URL (302)<br>
        Custom alias  → user specifies their own code<br>
        TTL / expiry  → optional expiration date per URL<br>
        Analytics     → click count, referrer, geo (optional)<br><br>
<span style="color:var(--aged)">OUT OF SCOPE: user accounts, dashboard, link editing</span>
</div>
</div>
<div class="req-card" style="border-top-color:var(--amber)">
<div class="rc-title" style="color:var(--amber)">Non-Functional Requirements</div>
<div class="rc-list">
        300M URLs stored total<br>
        Write: 100 new URLs/sec (peak: 500/sec)<br>
        Read:  10,000 redirects/sec (peak: 50,000/sec)<br>
        Read:write ratio = 100:1<br>
        Redirect p99 latency &lt; 10ms<br>
        Shorten p99 latency &lt; 100ms<br>
        Availability: 99.99% (52 min downtime/year)<br>
        Durability: URLs must never be lost
</div>
</div>
  </div>
  <div class="al amb"><em>Key insight to say aloud:</em> "The 100:1 read:write ratio tells me this is a read-heavy system. My entire architecture will be optimised for fast redirects — nearly every redirect should be served from cache without touching the database."</div>
</div>
<!-- ESTIMATION -->
<div class="view" id="view-est">
  <div class="sh">Capacity Estimation</div>
  <div class="sr">Numbers first — they drive every architecture decision</div>
  <table class="est-table">
<thead><tr><th>METRIC</th><th>VALUE</th><th>CALCULATION</th></tr></thead>
<tbody>
<tr><td>Write QPS (avg)</td><td>100/sec</td><td>given requirement</td></tr>
<tr><td>Write QPS (peak)</td><td>500/sec</td><td>5× average peak factor</td></tr>
<tr><td>Read QPS (avg)</td><td>10,000/sec</td><td>100:1 ratio × 100 writes/sec</td></tr>
<tr><td>Read QPS (peak)</td><td>50,000/sec</td><td>5× average peak factor</td></tr>
<tr><td>Storage per URL</td><td>~500 bytes</td><td>7-char code + 2KB URL + metadata</td></tr>
<tr><td>Total storage</td><td>150 GB</td><td>300M × 500 bytes</td></tr>
<tr><td>Storage/year</td><td>~1.5 TB</td><td>100 URLs/sec × 86,400 × 365 × 500B</td></tr>
<tr><td>Short code length</td><td>7 chars</td><td>62^7 = 3.5 trillion unique codes</td></tr>
<tr><td>Hot cache size</td><td>~30 GB</td><td>20% of 300M URLs × 500B (80/20 rule)</td></tr>
<tr><td>App servers needed</td><td>5–10</td><td>50K peak QPS ÷ 10K/server</td></tr>
</tbody>
  </table>
  <div class="al grn"><em>Key insight to say aloud:</em> "150 GB fits comfortably on a single DB node — no sharding needed. The hot set (30 GB) fits in a Redis cluster. At this scale, the bottleneck is read latency, not storage — hence the 2-layer cache strategy."</div>
</div>
<!-- ARCHITECTURE -->
<div class="view" id="view-arch">
  <div class="sh">High-Level Architecture</div>
  <div class="sr">Two distinct paths — read (cache-first) and write (ID generation)</div>
  <div class="arch-box">
<div class="arch-title">SYSTEM ARCHITECTURE — URL SHORTENER</div>
<div class="arch-rows">
<div class="arch-row">
<div class="arch-node" style="border-color:var(--blu);color:var(--blu)">Client</div>
<div class="arch-arr">──→</div>
<div class="arch-node" style="border-color:var(--amber);color:var(--amber)">Load Balancer<br><span style="font-size:8px">L7 / HTTPS / SSL termination</span></div>
<div class="arch-arr">──→</div>
<div class="arch-node" style="border-color:var(--rust);color:var(--rust)">API Servers<br><span style="font-size:8px">stateless × 5–10</span></div>
</div>
<div style="padding:6px 0;font-family:'Inconsolata',monospace;font-size:9px;color:var(--aged)">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↙ READ PATH &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↘ WRITE PATH
</div>
<div class="arch-row">
<div style="width:300px;flex-shrink:0"></div>
<div class="arch-node" style="border-color:var(--grn);color:var(--grn);margin-right:8px">In-Process Cache<br><span style="font-size:8px">Caffeine · 10K items · 5min TTL</span></div>
<div style="margin-right:8px;font-family:'Inconsolata',monospace;font-size:11px;color:var(--aged)">miss↓</div>
<div class="arch-node" style="border-color:var(--pur);color:var(--pur)">ID Generator<br><span style="font-size:8px">auto-increment + base62</span></div>
</div>
<div class="arch-row" style="margin-top:4px">
<div style="width:300px;flex-shrink:0"></div>
<div class="arch-node" style="border-color:var(--amber);color:var(--amber);margin-right:8px">Redis Cluster<br><span style="font-size:8px">url:{code} → long_url · LRU · 24h TTL</span></div>
<div style="margin-right:8px;font-family:'Inconsolata',monospace;font-size:11px;color:var(--aged)">miss↓</div>
<div class="arch-node" style="border-color:var(--rust);color:var(--rust)">MySQL Primary<br><span style="font-size:8px">durable write · ACID</span></div>
</div>
<div class="arch-row" style="margin-top:4px">
<div style="width:300px;flex-shrink:0"></div>
<div class="arch-node" style="border-color:var(--rust);color:var(--rust);margin-right:8px">MySQL Replicas ×3<br><span style="font-size:8px">read traffic · async replication</span></div>
<div style="margin-right:8px;font-family:'Inconsolata',monospace;font-size:11px;color:var(--aged)">async↓</div>
<div class="arch-node" style="border-color:var(--faded);color:var(--faded)">Kafka: click-events<br><span style="font-size:8px">fire-and-forget analytics</span></div>
</div>
</div>
  </div>
  <div class="sh">Read Path (redirect — must be &lt;10ms)</div>
  <div class="cb"><div class="cb-top">Step-by-step redirect flow<span class="cb-l">FLOW</span></div>
<pre class="c">GET /abc1234
 
1. Check <span class="hl">in-process cache</span> (Caffeine): ~<span class="ok">100ns</span>
   HIT (60%): return HTTP 302 immediately ✅
 
2. Check <span class="hl">Redis cache</span>: ~<span class="ok">0.5ms</span>
   HIT (39%): populate L1 cache, return HTTP 302 ✅
 
3. Cache MISS (1%): query <span class="hl">MySQL read replica</span>: ~<span class="am">5ms</span>
   Populate Redis (TTL 24h), populate L1 (TTL 5min), return HTTP 302 ✅
 
4. <span class="hl">Async</span> (does NOT block redirect):
   Publish click event to Kafka → Analytics consumer updates click_count</pre>
  </div>
</div>
<!-- CODE GENERATION -->
<div class="view" id="view-codegen">
  <div class="sh">Short Code Generation</div>
  <div class="sr">Four strategies — trade-offs in uniqueness, predictability, and complexity</div>
  <div class="sc-grid">
<div class="sc-card" style="border-top-color:var(--amber)">
<div class="sc-name" style="color:var(--amber)">A: MD5 + Truncation</div>
<div class="sc-body">Hash the long URL → take first 7 chars of base62-encoded hash. Same URL always produces same code (natural dedup).</div>
<div class="sc-pros">✓ Deterministic (dedup built-in)<br>✓ Stateless, no DB for ID</div>
<div class="sc-cons">✗ Collision possible at 300M URLs<br>✗ Must detect + retry on collision<br>✗ Custom alias not supported</div>
</div>
<div class="sc-card" style="border-top-color:var(--rust)">
<div class="sc-name" style="color:var(--rust)">B: Auto-Increment + Base62 ★</div>
<div class="sc-body">DB auto-increment ID → encode to base62. ID 123456789 → "8M0kX". Monotonic → guaranteed unique. Simple.</div>
<div class="sc-pros">✓ Guaranteed unique<br>✓ Simple implementation<br>✓ Short codes for small IDs</div>
<div class="sc-cons">✗ Predictable / enumerable<br>✗ DB is ID single point of failure<br>✗ Reveals URL count to scrapers</div>
</div>
<div class="sc-card" style="border-top-color:var(--blu)">
<div class="sc-name" style="color:var(--blu)">C: Snowflake-style Distributed ID</div>
<div class="sc-body">64-bit: [41-bit timestamp][10-bit machine][12-bit seq] → base62 encode. ~4096 IDs/ms per machine. No DB dependency.</div>
<div class="sc-pros">✓ Globally unique, no DB<br>✓ Scales to any throughput<br>✓ Sortable by creation time</div>
<div class="sc-cons">✗ Requires machine ID management<br>✗ Clock skew issues<br>✗ More complex</div>
</div>
<div class="sc-card" style="border-top-color:var(--grn)">
<div class="sc-name" style="color:var(--grn)">D: Pre-generated Pool</div>
<div class="sc-body">Background job pre-generates random 7-char codes, stores as "available". API fetches and marks "used" atomically.</div>
<div class="sc-pros">✓ Random → not enumerable<br>✓ No collision risk<br>✓ Fast fetch (no computation)</div>
<div class="sc-cons">✗ Complex pre-generation logic<br>✗ Pool management overhead<br>✗ Wasted codes if URLs deleted</div>
</div>
  </div>
  <div class="sh">Base62 Implementation</div>
  <div class="cb"><div class="cb-top">Encode / decode — implement from scratch in interview<span class="cb-l">JAVA</span></div>


```java
private static final String ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
private static final int BASE = 62;

public static String encode(long id) {
    if (id == 0) return "0";
    StringBuilder sb = new StringBuilder();
    while (id > 0) {
        sb.append(ALPHABET.charAt((int)(id % BASE)));
        id /= BASE;
    }
    return sb.reverse().toString();
}

public static long decode(String code) {
    long result = 0;
    for (char c : code.toCharArray()) {
        result = result * BASE + ALPHABET.indexOf(c);
    }
    return result;
}

// encode(0)         → "0"
// encode(62)        → "10"  (like binary: 1×62 + 0)
// encode(123456789) → "8M0kX"
// decode(encode(n)) == n  ✅
// 62^7 = 3,521,614,606,208 ≈ 3.5 trillion unique 7-char codes
```


</div>
<!-- SCHEMA -->
<div class="view" id="view-schema">
  <div class="sh">Database Schema</div>
  <div class="sr">MySQL — ACID, B-tree indexes, read replicas for scale</div>
  <div class="schema-box">
<div class="schema-hdr"><span>TABLE: urls</span><span style="color:var(--rust)">MySQL / PostgreSQL</span></div>
<div class="schema-body">
<div class="col-row" style="border-bottom:2px solid var(--sand);margin-bottom:4px;padding-bottom:6px">
<div style="font-family:'Inconsolata',monospace;font-size:9px;color:var(--aged)">COLUMN</div>
<div style="font-family:'Inconsolata',monospace;font-size:9px;color:var(--aged)">TYPE</div>
<div style="font-family:'Inconsolata',monospace;font-size:9px;color:var(--aged)">NOTES</div>
</div>
<div class="col-row"><div class="col-name">id</div><div class="col-type">BIGINT</div><div class="col-note">PRIMARY KEY AUTO_INCREMENT — source of short code</div></div>
<div class="col-row"><div class="col-name">short_code</div><div class="col-type">VARCHAR(10)</div><div class="col-note">NOT NULL UNIQUE — the 7-char base62 string</div></div>
<div class="col-row"><div class="col-name">long_url</div><div class="col-type">TEXT</div><div class="col-note">NOT NULL — original URL up to 2048 chars</div></div>
<div class="col-row"><div class="col-name">user_id</div><div class="col-type">BIGINT</div><div class="col-note">NULL = anonymous; FK to users table if auth added</div></div>
<div class="col-row"><div class="col-name">created_at</div><div class="col-type">TIMESTAMP</div><div class="col-note">DEFAULT CURRENT_TIMESTAMP</div></div>
<div class="col-row"><div class="col-name">expires_at</div><div class="col-type">TIMESTAMP</div><div class="col-note">NULL = never expires; checked on every redirect</div></div>
<div class="col-row"><div class="col-name">click_count</div><div class="col-type">BIGINT</div><div class="col-note">DEFAULT 0 — updated async via Kafka consumer</div></div>
<div class="col-row"><div class="col-name">is_active</div><div class="col-type">BOOLEAN</div><div class="col-note">DEFAULT TRUE — soft delete flag</div></div>
<div class="idx-list">
<div style="font-family:'Inconsolata',monospace;font-size:9px;color:var(--aged);margin-bottom:4px;letter-spacing:1px">INDEXES</div>
<div class="idx-row" style="color:var(--rust)">UNIQUE INDEX idx_short_code ON urls(short_code) <span style="color:var(--aged)">← primary lookup, O(log N)</span></div>
<div class="idx-row" style="color:var(--blu)">INDEX idx_user ON urls(user_id) <span style="color:var(--aged)">← "my URLs" page</span></div>
<div class="idx-row" style="color:var(--grn)">PARTIAL INDEX idx_expires ON urls(expires_at) WHERE expires_at IS NOT NULL <span style="color:var(--aged)">← cleanup job</span></div>
</div>
</div>
  </div>
  <div class="al amb"><em>Why MySQL over NoSQL?</em> 150GB fits on one node. Access pattern is pure primary-key lookup — no scatter-gather needed. ACID prevents duplicate short_code under concurrent inserts. Read replicas handle the 100:1 read:write ratio. NoSQL would work too (DynamoDB keyed on short_code) but adds operational overhead without benefit at this scale.</div>
</div>
<!-- CACHING -->
<div class="view" id="view-cache">
  <div class="sh">Caching Strategy</div>
  <div class="sr">Two layers — achieving 99%+ cache hit rate for redirects</div>
  <div class="cache-stack">
<div class="cl" style="border-left-color:var(--rust)">
<div class="cl-name">In-Process (L1)</div>
<div class="cl-desc">Caffeine cache in JVM heap. Top 10K URLs per server. Zero network. Sub-microsecond lookup.</div>
<div class="cl-lat" style="color:var(--rust)">~100 ns</div>
<div class="cl-rate">~60% hit rate</div>
</div>
<div class="cl" style="border-left-color:var(--amber)">
<div class="cl-name">Redis (L2)</div>
<div class="cl-desc">Shared across all app servers. Key: "url:{code}" → long_url. 30 GB hot set. allkeys-lru eviction.</div>
<div class="cl-lat" style="color:var(--amber)">~0.5 ms</div>
<div class="cl-rate">~39% hit rate</div>
</div>
<div class="cl" style="border-left-color:var(--faded)">
<div class="cl-name">MySQL Replica</div>
<div class="cl-desc">Only 1% of traffic reaches DB. SELECT long_url FROM urls WHERE short_code = ? Populate both cache layers on miss.</div>
<div class="cl-lat" style="color:var(--faded)">~5 ms</div>
<div class="cl-rate">~1% (cache miss)</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Cache read + invalidation pattern<span class="cb-l">JAVA</span></div>


```java
public String getLongUrl(String shortCode) {
    // L1: in-process
    String url = l1Cache.getIfPresent(shortCode);
    if (url != null) return url;

    // L2: Redis
    url = redis.get("url:" + shortCode);
    if (url != null) {
        l1Cache.put(shortCode, url);    // populate L1
        return url;
    }

    // DB: only 1% of traffic
    UrlRecord rec = db.findByShortCode(shortCode);
    if (rec == null || rec.isExpired()) return null;
    redis.setex("url:" + shortCode, 86400, rec.longUrl); // 24h TTL
    l1Cache.put(shortCode, rec.longUrl);
    return rec.longUrl;
}

// Invalidation: on URL delete
public void deleteUrl(String shortCode) {
    db.softDelete(shortCode);
    redis.del("url:" + shortCode);
    l1Cache.invalidate(shortCode);  // invalidate all instances via broadcast
}
```


</div>
<!-- REDIRECT -->
<div class="view" id="view-redirect">
  <div class="sh">301 vs 302 Redirect</div>
  <div class="sr">An explicit trade-off — analytics vs server load</div>
  <div class="redir-grid">
<div class="redir-card">
<div class="redir-code" style="color:var(--faded)">301</div>
<div class="redir-sub">MOVED PERMANENTLY</div>
<div style="font-size:12px;color:var(--faded);line-height:1.6;margin-bottom:10px">Browser caches the redirect. Subsequent visits from same browser skip your server entirely.</div>
<div class="redir-pro">✓ Browser caches → lower server load<br>✓ Reduced latency for repeat visits<br>✓ CDN can cache the response</div>
<div class="redir-con" style="margin-top:6px">✗ Can't track repeat clicks<br>✗ Can't update long URL after caching<br>✗ Analytics are incomplete</div>
</div>
<div class="redir-card" style="border-top:2px solid var(--rust)">
<div class="redir-code" style="color:var(--rust)">302</div>
<div class="redir-sub">FOUND (TEMPORARY) — RECOMMENDED ★</div>
<div style="font-size:12px;color:var(--faded);line-height:1.6;margin-bottom:10px">Browser does NOT cache. Every click hits your server. Full analytics visibility.</div>
<div class="redir-pro">✓ Full click analytics (every visit)<br>✓ Can update long URL at any time<br>✓ A/B testing possible</div>
<div class="redir-con" style="margin-top:6px">✗ Higher server load (every click)<br>✗ Slightly higher latency<br>✗ No browser-level caching</div>
</div>
  </div>
  <div class="al amb"><em>Interview answer:</em> "I'll use 302 by default because analytics are a core requirement. If a URL provider wants maximum performance and no analytics tracking, we can expose a '301 mode' as an opt-in option. The trade-off is explicit and user-controlled."</div>
</div>
<!-- EDGE CASES -->
<div class="view" id="view-edge">
  <div class="sh">Edge Cases & Deep Dives</div>
  <div class="sr">What separates a good answer from a great one</div>
  <div class="edge-grid">
<div class="ec" style="border-left-color:var(--amber)">
<div class="ec-title">URL Expiry</div>
<div class="ec-body">URLs with expires_at set should return 410 Gone after expiry.</div>
<div class="ec-sol" style="color:var(--amber)">Lazy check: on redirect, if expires_at &lt; NOW() → 410.<br>Background job: daily DELETE WHERE expires_at &lt; NOW().<br>Redis TTL: set same TTL as URL expiry on cache key.</div>
</div>
<div class="ec" style="border-left-color:var(--rust)">
<div class="ec-title">Custom Aliases</div>
<div class="ec-body">User requests /my-campaign. Must be unique, safe, and not clash with system routes.</div>
<div class="ec-sol" style="color:var(--rust)">UNIQUE constraint handles conflict → 409 response.<br>Blocklist: reserve "api", "health", "admin".<br>Regex validate: alphanumeric + hyphens only.</div>
</div>
<div class="ec" style="border-left-color:var(--blu)">
<div class="ec-title">Rate Limiting</div>
<div class="ec-body">Prevent URL bombing and redirect abuse from single IPs.</div>
<div class="ec-sol" style="color:var(--blu)">Redis counter: INCR rate:shorten:{ip}:{hour}<br>EXPIRE 3600 → if &gt;100 → 429 Too Many Requests.<br>Separate limits for /shorten vs GET /{code}.</div>
</div>
<div class="ec" style="border-left-color:var(--grn)">
<div class="ec-title">Viral URL (Hotkey)</div>
<div class="ec-body">Taylor Swift tweets /abc1234 → 1M req/sec hits one URL.</div>
<div class="ec-sol" style="color:var(--grn)">L1 in-process cache absorbs burst (no Redis roundtrip).<br>If insufficient: replicate key to N Redis shards.<br>CDN 301 caching as last resort (lose analytics).</div>
</div>
<div class="ec" style="border-left-color:var(--pur)">
<div class="ec-title">URL Validation</div>
<div class="ec-body">Malicious URLs, redirect chains, oversized inputs.</div>
<div class="ec-sol" style="color:var(--pur)">Parse URL (valid http/https scheme).<br>Check against phishing/malware blocklist.<br>Detect redirect loops (sho.rt → sho.rt).<br>Max long URL: 2048 chars.</div>
</div>
<div class="ec" style="border-left-color:var(--faded)">
<div class="ec-title">Analytics Lag</div>
<div class="ec-body">Kafka consumer falls behind → click_count is stale.</div>
<div class="ec-sol" style="color:var(--faded)">click_count is "approximate" by design — user expectation set.<br>Monitor consumer lag: alert if &gt;100K backlog.<br>Scale consumer group (add instances up to numPartitions).</div>
</div>
  </div>
</div>
<!-- FRAMEWORK -->
<div class="view" id="view-framework">
  <div class="sh">7-Step Framework Applied</div>
  <div class="sr">How to present URL Shortener in 45 minutes in a FAANG interview</div>
  <div class="fw-row">
<div class="fw-step"><div class="fw-n">01</div><div class="fw-t">REQUIREMENTS (5m)</div><div class="fw-b">Shorten + redirect. 300M URLs. 100:1 read:write. &lt;10ms redirect. 99.99% uptime. Analytics optional.</div></div>
<div class="fw-step"><div class="fw-n">02</div><div class="fw-t">ESTIMATION (5m)</div><div class="fw-b">150GB storage. 50K peak QPS. 30GB hot set. 3.5T unique codes. No sharding needed at this scale.</div></div>
<div class="fw-step"><div class="fw-n">03</div><div class="fw-t">HLD (10m)</div><div class="fw-b">Client→LB→API servers→[L1 cache→Redis→MySQL replica]. Write: API→MySQL primary (auto-ID→base62). Analytics: Kafka async.</div></div>
<div class="fw-step"><div class="fw-n">04</div><div class="fw-t">DEEP DIVE (15m)</div><div class="fw-b">Code generation (base62 + auto-increment). 2-layer cache (L1+Redis). Schema with partial index. 302 vs 301 trade-off.</div></div>
<div class="fw-step"><div class="fw-n">05</div><div class="fw-t">BOTTLENECKS (5m)</div><div class="fw-b">Cache hit rate (99%+ target). Hotkeys (viral URLs → L1 absorbs). ID generation (MySQL SPOF → use Snowflake at 10× scale).</div></div>
<div class="fw-step"><div class="fw-n">06</div><div class="fw-t">FAILURES (3m)</div><div class="fw-b">Redis down: fall through to DB (~5ms, acceptable). DB primary down: serve from cache + replicas. Analytics lag: non-blocking.</div></div>
<div class="fw-step"><div class="fw-n">07</div><div class="fw-t">SCALE UP (2m)</div><div class="fw-b">10× URLs → shard by hash(short_code). Multi-region → geo DNS + regional MySQL + cross-region replication. CDN for 301 redirects.</div></div>
  </div>
  <div class="al grn"><em>Numbers to say aloud:</em> "150 GB fits on a single node — no sharding." · "62^7 = 3.5 trillion codes — won't exhaust for centuries." · "99% cache hit rate means 1% of redirects touch MySQL." · "302 because analytics is a requirement, with a 301 opt-in for CDN offload."</div>
</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-lbl">Implement Base62 Encode / Decode</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Write base62 encode and decode in Java (or your language of choice):</p>
<ul>
<li>Handle edge cases: encode(0), encode(1), encode(62), encode(62^7 - 1)</li>
<li>Verify roundtrip: assert decode(encode(n)) == n for 1000 random values</li>
<li>How many chars does encode(300_000_000) produce?</li>
<li>Extend: implement MD5 + truncation approach. Write the collision detection retry loop.</li>
</ul>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-lbl">Extended Schema Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Extend the base schema to support:</p>
<ol>
<li><strong>User accounts</strong> owning URLs — with "my URLs" listing page (paginated, sorted by created_at)</li>
<li><strong>URL groups / campaigns</strong> — tag multiple URLs together (e.g., "summer-sale")</li>
<li><strong>Per-URL hourly analytics</strong> — click count broken down by hour-of-day</li>
<li><strong>A/B testing</strong> — one short code routes 50% to URL-A, 50% to URL-B</li>
</ol>
<p style="margin-top:8px">For each: write the CREATE TABLE SQL, necessary indexes, and explain the query pattern.</p>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-lbl">Failure Scenario Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Design the failure handling for each scenario. What does the system do? What does the user experience?</p>
<ol>
<li>Redis cluster completely unavailable</li>
<li>MySQL primary goes down mid-write (during shorten request)</li>
<li>ID generator service (if using external Snowflake service) is unreachable</li>
<li>Analytics Kafka topic has 5-minute lag — consumer backlog of 3M events</li>
<li>A single URL (/abc1234) receives 1M requests/sec (DDoS via viral celebrity tweet)</li>
</ol>
</div>
</div>
<div class="task-card" style="border-top:2px solid var(--rust)">
<div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--rust)">★</div><div class="t-lbl">Multi-Region Redesign (US + EU + APAC)</div><div class="t-meta">~3 hrs · full redesign</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Redesign for global deployment with these constraints:</p>
<ul>
<li>Users in each region get &lt;5ms redirect latency</li>
<li>URLs created in US accessible from EU within 1 second</li>
<li>Unified analytics across all regions</li>
<li>No EU user data may leave EU (GDPR compliance)</li>
<li>System remains available if one entire region goes down</li>
</ul>
<p style="margin-top:8px">Design: DNS routing strategy, data replication model, consistency choice for URL creation, analytics aggregation, GDPR compliance approach.</p>
</div>
</div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 15 completed</span><span style="font-family:'Inconsolata',monospace">MODULE B5 · URL SHORTENER</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can state all functional + non-functional requirements from memory</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Capacity estimation in &lt;5 min: 150GB, 100:1, 30GB hot set, 3.5T codes</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can draw full architecture diagram: LB → API → L1/L2 cache → DB → Kafka</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">All 4 short code generation strategies and their trade-offs</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can implement base62 encode/decode from scratch in an interview</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">DB schema: correct columns, UNIQUE index on short_code, partial index on expires_at</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">2-layer cache: in-process (L1) + Redis (L2), TTLs, hit rates, invalidation</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">301 vs 302 trade-off: analytics vs CDN offload — say the trade-off explicitly</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Async analytics: Kafka click events, fire-and-forget, doesn't block redirect</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Edge cases: expiry, custom aliases, rate limiting, URL validation, hotkeys</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Failure handling: Redis down → DB fallback; DB primary down → replicas</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can apply full 7-step framework to URL shortener in 45 minutes</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: base62 implementation with roundtrip test</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: extended schema (users, campaigns, analytics, A/B)</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): multi-region redesign with GDPR compliance</div></div>
  </div>
  <div style="margin-top:28px;background:var(--cream);border:1px solid var(--sand);padding:22px;border-top:3px double var(--rust)">
<div style="font-family:'Inconsolata',monospace;font-size:8px;color:var(--aged);letter-spacing:2px;margin-bottom:8px">NEXT MODULE</div>
<div style="font-family:'Oswald',sans-serif;font-size:28px;font-weight:700;color:var(--ink);margin-bottom:6px">B6 — Design Twitter/X Feed</div>
<div style="font-family:'Inconsolata',monospace;font-size:9px;color:var(--faded);line-height:2">
      Social graph · Fan-out on write vs fan-out on read<br>
      Home timeline generation · Celebrity problem · News feed ranking<br>
      Push vs pull model · Redis timeline cache · Hybrid approach
</div>
  </div>
</div>
</div>
</div>
<!-- Bottom Navigation -->
<div class="mb5-bottom-nav">
  <a href="/learning/system-design/hld/module-b4-message-queues/" class="mb5-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    B4: Message Queues
  </a>
  <a href="/learning/system-design/hld/module-b5-notes/" class="mb5-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb5-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b6-twitter-feed/" class="mb5-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    B6: Twitter Feed
  </a>
</div>
<script src="/assets/js/sd-module-b5.js"></script>
