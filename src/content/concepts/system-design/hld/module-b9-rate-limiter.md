---
title: "Module B9: Rate Limiter"
description: "SYSTEM DESIGN MASTERY · TRACK B · MODULE B9 · WEEK 19 RATE LIMITING · TOKEN BUCKET · SLIDING WINDOW · REDIS LUA Component Design · 5 Algorithms · Distributed Limiting RATE…"
domain: system-design
track: system-design-hld
order: 118
url: /learning/system-design/hld/module-b9-rate-limiter/
---

<link rel="stylesheet" href="/assets/css/sd-module-b9.css">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600;700&family=Fira+Code:wght@300;400;600&display=swap" rel="stylesheet">

<div class="sd-module-b9">
<header>
  <div class="hdr-stripe"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B9 · WEEK 19</span>
    <span>RATE LIMITING · TOKEN BUCKET · SLIDING WINDOW · REDIS LUA</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-tag">Component Design · 5 Algorithms · Distributed Limiting</div>
      <h1>RATE<br><span class="acc">LIMITER</span></h1>
      <div class="hdr-sub">FIXED WINDOW · SLIDING WINDOW · TOKEN BUCKET<br>LEAKY BUCKET · REDIS LUA · HTTP 429 · MULTI-TIER</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">5</div><div class="hs-l">ALGORITHMS</div></div>
      <div class="hs"><div class="hs-v">O(1)</div><div class="hs-l">MEMORY TARGET</div></div>
      <div class="hs"><div class="hs-v">429</div><div class="hs-l">HTTP STATUS</div></div>
      <div class="hs"><div class="hs-v">B9</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="alg-row">
    <div class="alg-tag" style="color:var(--red)">Fixed Window</div>
    <div class="alg-tag" style="color:var(--yel)">Sliding Window Log</div>
    <div class="alg-tag" style="color:var(--grn)">Sliding Window Counter ★</div>
    <div class="alg-tag" style="color:var(--cyan)">Token Bucket</div>
    <div class="alg-tag" style="color:var(--mag)">Leaky Bucket</div>
    <div class="alg-tag" style="color:var(--ora)">Redis Lua</div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="mb9_show('why',this)">Why Rate Limit</div>
  <div class="nt" onclick="mb9_show('fixed',this)">Fixed Window</div>
  <div class="nt" onclick="mb9_show('sliding',this)">Sliding Window</div>
  <div class="nt" onclick="mb9_show('bucket',this)">Token / Leaky Bucket</div>
  <div class="nt" onclick="mb9_show('compare',this)">Comparison</div>
  <div class="nt" onclick="mb9_show('redis',this)">Redis Implementations</div>
  <div class="nt" onclick="mb9_show('distributed',this)">Distributed</div>
  <div class="nt" onclick="mb9_show('response',this)">429 Response</div>
  <div class="nt" onclick="mb9_show('multitier',this)">Multi-Tier</div>
  <div class="nt" onclick="mb9_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb9_show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- WHY -->
<div class="view active" id="view-why">
  <div class="sh">Why Rate Limit?</div>
  <div class="sr">Five problems — one solution</div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--red);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">DoS Protection</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">One bad actor exhausts server resources. Rate limiting prevents a single IP or user from dominating bandwidth.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--yel);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">Cost Control</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">Expensive APIs (OpenAI, SMS, email) must be gated. Unlimited access = unlimited cloud bill.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--grn);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">Fair Use</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">Shared infrastructure must be equitable. One user shouldn't starve others on a multi-tenant API.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--cyan);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">Tier Enforcement</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">Free: 1K req/day. Pro: 10K. Enterprise: unlimited. Rate limiting is how SaaS products enforce pricing tiers.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--mag);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">Abuse Prevention</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">Brute force login: 5 attempts/min per IP. Credential stuffing: 100 req/hr per account.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--ora);padding:13px">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:1px;color:var(--white);margin-bottom:5px">QoS Guarantee</div>
      <div style="font-size:11px;color:var(--text);line-height:1.6">Downstream services have capacity limits. Rate limit upstream to protect the service from overload.</div>
    </div>
  </div>
</div>

<!-- FIXED WINDOW -->
<div class="view" id="view-fixed">
  <div class="sh">Fixed Window Counter</div>
  <div class="sr">Simplest algorithm — and its fatal flaw</div>
  <div class="cb"><div class="cb-top">Fixed window: simple Redis INCR per time bucket<span class="cb-l">REDIS</span></div>
<pre class="c"><span class="cm">// Key: ratelimit:{userId}:{window_minute}</span>
<span class="cm">// Limit: 100 req/min</span>

<span class="kw">function</span> <span class="fn">checkLimit</span>(userId) {
  window = Math.<span class="fn">floor</span>(Date.<span class="fn">now</span>() / <span class="cy">60000</span>)   <span class="cm">// minute bucket</span>
  key = <span class="str">`rl:${userId}:${window}`</span>
  
  count = redis.<span class="fn">incr</span>(key)
  <span class="kw">if</span> (count == <span class="cy">1</span>) redis.<span class="fn">expire</span>(key, <span class="cy">120</span>)  <span class="cm">// set TTL on first request</span>
  
  <span class="kw">return</span> count <= <span class="cy">100</span>
}

<span class="cm">// Memory: O(1) — just one counter per user</span>
<span class="cm">// Speed: one INCR + one EXPIRE (conditional)</span></pre>
  </div>

  <div class="al red"><em>⚠ THE BOUNDARY BURST ATTACK:</em><br><br>
    12:00:58 → user sends 100 requests (window A, last 2 seconds)<br>
    12:01:00 → window resets to 0<br>
    12:01:01 → user sends 100 more requests (window B, first second)<br>
    <br>
    Result: 200 requests in 3 seconds — 2× the intended 100/min limit.<br>
    Fixed window counter CANNOT prevent this.
  </div>

  <div class="burst-vis">
    <div class="bv-label">// BURST ATTACK TIMELINE — 200 requests in 3 seconds</div>
    <div style="display:flex;gap:0;align-items:flex-end;height:90px;overflow-x:auto;margin-bottom:8px">
      <div style="flex:2;border-right:2px dashed var(--muted);padding:0 8px;display:flex;flex-direction:column;justify-content:flex-end">
        <div style="background:var(--muted);height:20px;width:100%;margin-bottom:2px"></div>
        <div style="background:var(--muted);height:20px;width:100%;margin-bottom:2px"></div>
        <div style="background:var(--red);height:40px;width:100%;margin-bottom:2px"></div>
        <div style="font-family:'Fira Code',monospace;font-size:7px;color:var(--muted);margin-top:4px;text-align:center">Window A 12:00-12:01<br>100 req (last 2s)</div>
      </div>
      <div style="flex:2;padding:0 8px;display:flex;flex-direction:column;justify-content:flex-end">
        <div style="background:var(--red);height:80px;width:100%;margin-bottom:2px"></div>
        <div style="font-family:'Fira Code',monospace;font-size:7px;color:var(--muted);margin-top:4px;text-align:center">Window B 12:01-12:02<br>100 req (first 1s)</div>
      </div>
    </div>
    <div class="bv-note" style="color:var(--red)">200 requests arrive in under 3 seconds — rate limit completely bypassed at the window boundary</div>
  </div>
</div>

<!-- SLIDING WINDOW -->
<div class="view" id="view-sliding">
  <div class="sh">Sliding Window Algorithms</div>
  <div class="sr">Log (exact) vs Counter (approximate) — production trade-off</div>

  <div class="sh" style="font-size:16px;margin-top:14px">Sliding Window Log (Exact)</div>
  <div class="cb"><div class="cb-top">Sorted set of timestamps — exact but memory-heavy<span class="cb-l">REDIS</span></div>
<pre class="c"><span class="cm">// Key: ratelimit:{userId} — Sorted Set, score = timestamp</span>
<span class="kw">function</span> <span class="fn">checkLimit</span>(userId) {
  now     = Date.<span class="fn">now</span>()           <span class="cm">// ms</span>
  window  = <span class="cy">60000</span>                <span class="cm">// 60s in ms</span>
  cutoff  = now - window

  redis.<span class="fn">zremrangebyscore</span>(<span class="str">`rl:${userId}`</span>, <span class="cy">0</span>, cutoff)  <span class="cm">// remove old</span>
  count = redis.<span class="fn">zcard</span>(<span class="str">`rl:${userId}`</span>)               <span class="cm">// count remaining</span>

  <span class="kw">if</span> (count >= <span class="cy">100</span>) <span class="kw">return</span> <span class="er">REJECT</span>

  redis.<span class="fn">zadd</span>(<span class="str">`rl:${userId}`</span>, now, now)             <span class="cm">// log this request</span>
  redis.<span class="fn">expire</span>(<span class="str">`rl:${userId}`</span>, <span class="cy">120</span>)              <span class="cm">// TTL cleanup</span>
  <span class="kw">return</span> <span class="ok">ALLOW</span>
}
<span class="cm">// Memory: O(N) — stores EVERY request timestamp</span>
<span class="cm">// 100 req/min × 1M users = 100M Redis entries → expensive</span></pre>
  </div>

  <div class="sh" style="font-size:16px;margin-top:18px">Sliding Window Counter ★ (Recommended)</div>
  <div class="sw-math">
    <div class="sw-label">// WEIGHTED INTERPOLATION FORMULA</div>
    <div class="sw-formula">rate = prev_count × (1 − elapsed_fraction) + curr_count</div>
    <div class="sw-ex">
Example: limit = 100 req/min, current time = 12:01:45 (45s into window)<br>
elapsed_fraction = 45s / 60s = 0.75<br>
prev_window (12:00–12:01): 80 requests<br>
curr_window (12:01–12:02): 30 requests<br><br>
estimated_rate = 80 × (1 − 0.75) + 30 = <span style="color:var(--grn)">20 + 30 = 50 → ALLOW ✓</span><br><br>
Attack scenario: prev=100, curr=95 at T=12:01:01 (elapsed=0.017)<br>
estimated_rate = 100 × 0.983 + 95 = 98.3 + 95 = <span style="color:var(--red)">193 → REJECT ✓</span> (boundary burst caught!)
    </div>
  </div>
  <div class="cb"><div class="cb-top">Sliding window counter — two Redis keys, O(1) memory<span class="cb-l">REDIS</span></div>
<pre class="c"><span class="kw">function</span> <span class="fn">checkLimit</span>(userId, limit, windowSec) {
  now     = Math.<span class="fn">floor</span>(Date.<span class="fn">now</span>() / <span class="cy">1000</span>)
  bucket  = Math.<span class="fn">floor</span>(now / windowSec)
  elapsed = (now % windowSec) / windowSec

  keyCurr = <span class="str">`rl:${userId}:${bucket}`</span>
  keyPrev = <span class="str">`rl:${userId}:${bucket - 1}`</span>

  [prevCount, currCount] = redis.<span class="fn">mget</span>(keyPrev, keyCurr)
  prevCount = prevCount || <span class="cy">0</span>
  currCount = currCount || <span class="cy">0</span>

  rate = prevCount * (<span class="cy">1</span> - elapsed) + currCount

  <span class="kw">if</span> (rate >= limit) <span class="kw">return</span> <span class="er">REJECT</span>

  redis.<span class="fn">incr</span>(keyCurr)
  redis.<span class="fn">expire</span>(keyCurr, windowSec * <span class="cy">2</span>)
  <span class="kw">return</span> <span class="ok">ALLOW</span>
}
<span class="cm">// Memory: O(1) — only 2 counter keys per user at any time</span>
<span class="cm">// Accuracy: ~99.997% vs true sliding window (0.003% error)</span></pre>
  </div>
</div>

<!-- BUCKETS -->
<div class="view" id="view-bucket">
  <div class="sh">Token Bucket &amp; Leaky Bucket</div>
  <div class="sr">When natural bursts are legitimate — or must be suppressed</div>
  <div class="alg-grid">
    <div class="ac" style="border-top-color:var(--cyan)">
      <div class="ac-name" style="color:var(--cyan)">Token Bucket</div>
      <div class="ac-tag">BURST-FRIENDLY · O(1) STATE</div>
      <div class="ac-body">Bucket holds up to N tokens. Refills at R tokens/sec. Each request consumes 1 token. Empty bucket → reject. Full bucket allows N instant requests (burst).</div>
      <div class="ac-props" style="color:var(--cyan)">
        capacity=20, rate=10/sec:<br>
        User idle 2s → bucket fills to 20<br>
        20 instant requests → all allowed (burst!)<br>
        21st → rejected<br>
        After 0.1s → 1 refilled → allow again
      </div>
    </div>
    <div class="ac" style="border-top-color:var(--mag)">
      <div class="ac-name" style="color:var(--mag)">Leaky Bucket</div>
      <div class="ac-tag">CONSTANT RATE · QUEUE-BASED</div>
      <div class="ac-body">Requests queue up in a bucket. Bucket "leaks" (processes) at constant rate R. If bucket full → drop. Output is always exactly R req/sec regardless of input.</div>
      <div class="ac-props" style="color:var(--mag)">
        Use for: payment processors,<br>
        SMS gateways, anything with<br>
        strict constant-rate downstream<br>
        ✗ Adds latency (queued requests)<br>
        ✗ Not for interactive APIs
      </div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Token bucket — Redis Lua for atomicity<span class="cb-l">LUA</span></div>
<pre class="c"><span class="cm">-- KEYS[1] = bucket key</span>
<span class="cm">-- ARGV[1] = capacity, ARGV[2] = rate/sec, ARGV[3] = now_ms</span>

<span class="kw">local</span> capacity = tonumber(ARGV[<span class="cy">1</span>])
<span class="kw">local</span> rate     = tonumber(ARGV[<span class="cy">2</span>])
<span class="kw">local</span> now      = tonumber(ARGV[<span class="cy">3</span>])

<span class="kw">local</span> bucket   = redis.<span class="fn">call</span>(<span class="str">"HMGET"</span>, KEYS[<span class="cy">1</span>], <span class="str">"tokens"</span>, <span class="str">"last"</span>)
<span class="kw">local</span> tokens   = tonumber(bucket[<span class="cy">1</span>] or capacity)
<span class="kw">local</span> last     = tonumber(bucket[<span class="cy">2</span>] or now)

<span class="kw">local</span> elapsed  = (now - last) / <span class="cy">1000</span>   <span class="cm">-- seconds</span>
tokens = math.<span class="fn">min</span>(capacity, tokens + elapsed * rate)

<span class="kw">if</span> tokens >= <span class="cy">1</span> <span class="kw">then</span>
    tokens = tokens - <span class="cy">1</span>
    redis.<span class="fn">call</span>(<span class="str">"HMSET"</span>, KEYS[<span class="cy">1</span>], <span class="str">"tokens"</span>, tokens, <span class="str">"last"</span>, now)
    redis.<span class="fn">call</span>(<span class="str">"EXPIRE"</span>, KEYS[<span class="cy">1</span>], <span class="cy">3600</span>)
    <span class="kw">return</span> <span class="cy">1</span>   <span class="cm">-- ALLOW</span>
<span class="kw">else</span>
    redis.<span class="fn">call</span>(<span class="str">"HMSET"</span>, KEYS[<span class="cy">1</span>], <span class="str">"tokens"</span>, tokens, <span class="str">"last"</span>, now)
    <span class="kw">return</span> <span class="cy">0</span>   <span class="cm">-- REJECT</span>
<span class="kw">end</span></pre>
  </div>
</div>

<!-- COMPARISON -->
<div class="view" id="view-compare">
  <div class="sh">Algorithm Comparison</div>
  <div class="sr">Choose by use case — not by complexity</div>
  <table class="ct">
    <thead><tr><th>ALGORITHM</th><th>MEMORY</th><th>BURST</th><th>ACCURACY</th><th>BEST FOR</th></tr></thead>
    <tbody>
      <tr><td>Fixed Window</td><td class="best">O(1)</td><td class="bad">✗ Boundary burst</td><td class="bad">~Approximate</td><td>Simple counters, non-critical endpoints</td></tr>
      <tr><td>Sliding Window Log</td><td class="bad">O(N) — per request</td><td class="best">✓ Exact</td><td class="best">Exact</td><td>Low-traffic strict APIs, small user base</td></tr>
      <tr><td>Sliding Window Counter ★</td><td class="best">O(1)</td><td class="best">~✓ 99.997%</td><td class="best">~Exact</td><td><strong>Production default for most APIs</strong></td></tr>
      <tr><td>Token Bucket</td><td class="best">O(1)</td><td class="best">✓ Up to capacity</td><td class="best">Exact</td><td>APIs where short bursts are legitimate</td></tr>
      <tr><td>Leaky Bucket</td><td class="med">O(queue)</td><td class="bad">✗ Queued</td><td class="best">Exact output</td><td>Constant-rate downstream (payments, SMS)</td></tr>
    </tbody>
  </table>
  <div class="al grn"><em>Interview default:</em> "I'd use Sliding Window Counter as the default — O(1) memory, no boundary burst vulnerability, 0.003% accuracy error which is negligible for rate limiting. For APIs where genuine burst traffic should be allowed (e.g., bulk file uploads), I'd switch to Token Bucket."</div>
</div>

<!-- REDIS IMPLEMENTATIONS -->
<div class="view" id="view-redis">
  <div class="sh">Redis Lua Scripts — Why Atomic?</div>
  <div class="sr">The race condition that breaks naive implementations</div>
  <div class="cb"><div class="cb-top">Race condition without Lua — two threads, one counter<span class="cb-l">RACE CONDITION</span></div>
<pre class="c"><span class="cm">// Without Lua — BROKEN under concurrency:</span>
Thread A: GET tokens → <span class="cy">1</span>             <span class="cm">// sees 1 token available</span>
Thread B: GET tokens → <span class="cy">1</span>             <span class="cm">// also sees 1 token available</span>
Thread A: SET tokens 0                 <span class="cm">// decrements to 0, allows request</span>
Thread B: SET tokens 0                 <span class="cm">// also decrements to 0, ALSO allows request</span>
<span class="er">// Result: 2 requests allowed when only 1 token existed!</span>

<span class="cm">// With Lua script — CORRECT:</span>
<span class="cm">// Redis executes Lua scripts atomically</span>
<span class="cm">// No other Redis command can interleave between Lua lines</span>
<span class="cm">// Equivalent to a Redis MULTI/EXEC transaction but faster</span>

<span class="cm">// Execute Lua script in application code:</span>
<span class="kw">const</span> script = redis.<span class="fn">createScript</span>(luaCode);
<span class="kw">const</span> result = <span class="kw">await</span> script.<span class="fn">eval</span>(
  [<span class="str">`bucket:${userId}`</span>],              <span class="cm">// KEYS[1]</span>
  [capacity, refillRate, Date.<span class="fn">now</span>()]  <span class="cm">// ARGV[1,2,3]</span>
);</pre>
  </div>
  <div class="al cy"><em>Why not MULTI/EXEC (Redis transactions)?</em> MULTI/EXEC doesn't support conditional logic — you can't say "if tokens > 0 then decrement, else reject" inside a transaction. Lua scripts can. For rate limiting, you always need the check-and-decrement to be conditional and atomic.</div>
</div>

<!-- DISTRIBUTED -->
<div class="view" id="view-distributed">
  <div class="sh">Distributed Rate Limiting</div>
  <div class="sr">Multiple API servers — shared state or local approximation?</div>
  <div class="dist-grid">
    <div class="dc" style="border-top-color:var(--grn)">
      <div class="dc-name" style="color:var(--grn)">Centralized Redis ★</div>
      <div class="dc-body">All servers read/write to same Redis. Consistent hashing: hash(userId) → specific Redis shard. Correct counts always.</div>
      <div class="dc-pro">✓ Accurate<br>✓ Simple consistency<br>✓ Works at 500K req/sec/node</div>
      <div class="dc-con">✗ Redis is bottleneck + SPOF<br>✗ +0.5ms per request (network)<br>Mitigate: replicas + circuit breaker</div>
    </div>
    <div class="dc" style="border-top-color:var(--yel)">
      <div class="dc-name" style="color:var(--yel)">Local Counters</div>
      <div class="dc-body">Each server keeps in-memory counter. Set limit = total_limit / N servers. Periodic gossip sync. No Redis dependency.</div>
      <div class="dc-pro">✓ Zero latency overhead<br>✓ No Redis dependency<br>✓ Survives Redis failure</div>
      <div class="dc-con">✗ Under-counts (each server only sees own traffic)<br>✗ Uneven traffic distribution allows over-limit<br>Use: approximate limiting acceptable</div>
    </div>
    <div class="dc" style="border-top-color:var(--cyan)">
      <div class="dc-name" style="color:var(--cyan)">API Gateway</div>
      <div class="dc-body">Apply rate limiting at NGINX/Kong/AWS API GW before request hits any app server. Gateway backed by Redis.</div>
      <div class="dc-pro">✓ Rejects before app server compute<br>✓ Centralized config (no app deploy)<br>✓ Works across heterogeneous backends</div>
      <div class="dc-con">✗ Gateway is now critical path<br>✗ Less flexibility per-endpoint<br>Best for: org-wide API rate limiting</div>
    </div>
  </div>
  <div class="sh" style="font-size:16px;margin-top:18px">Fail-Open vs Fail-Closed</div>
  <div class="cb"><div class="cb-top">What happens when Redis is unavailable?<span class="cb-l">FAILURE MODE</span></div>
<pre class="c"><span class="kw">function</span> <span class="fn">checkRateLimit</span>(userId) {
  <span class="kw">try</span> {
    <span class="kw">return</span> redis.<span class="fn">checkLimit</span>(userId)
  } <span class="kw">catch</span> (RedisUnavailable) {
    
    <span class="cm">// Option A: Fail-Open (allow all)</span>
    <span class="kw">return</span> <span class="ok">ALLOW</span>
    <span class="cm">// Pro: service stays up, users unaffected</span>
    <span class="cm">// Con: during Redis outage, limits not enforced → potential abuse</span>
    <span class="cm">// Use for: internal services, non-critical limits</span>
    
    <span class="cm">// Option B: Fail-Closed (reject all)</span>
    <span class="kw">return</span> <span class="er">REJECT</span>
    <span class="cm">// Pro: strict — no abuse during outage</span>
    <span class="cm">// Con: service degraded for ALL users when Redis is down</span>
    <span class="cm">// Use for: financial APIs, security-critical endpoints</span>
    
    <span class="cm">// Option C: Local fallback (temporary local counter)</span>
    <span class="kw">return</span> localFallback.<span class="fn">checkLimit</span>(userId)  <span class="cm">// in-memory, less accurate</span>
    <span class="cm">// Best of both worlds for most production systems</span>
  }
}</pre>
  </div>
</div>

<!-- 429 RESPONSE -->
<div class="view" id="view-response">
  <div class="sh">HTTP 429 Response Design</div>
  <div class="sr">Good API clients need these headers to behave correctly</div>
  <div class="headers-box">
    <div class="hb-top"><span>HTTP/1.1 429 Too Many Requests</span></div>
    <div class="hb-body">
      <span class="hb-key">X-RateLimit-Limit:</span>     <span class="hb-val">100</span><br>
      <span class="hb-key">X-RateLimit-Remaining:</span> <span class="hb-val">0</span><br>
      <span class="hb-key">X-RateLimit-Reset:</span>     <span class="hb-val">1700000060</span>  <span style="color:var(--muted)">← Unix timestamp when window resets</span><br>
      <span class="hb-key">Retry-After:</span>           <span class="hb-val">42</span>            <span style="color:var(--muted)">← seconds until safe to retry</span><br>
      <span class="hb-key">Content-Type:</span>          <span class="hb-val">application/json</span><br>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Response body + good client behavior<span class="cb-l">JSON + CLIENT</span></div>
<pre class="c"><span class="cm">// Response body:</span>
{
  <span class="str">"error"</span>: <span class="str">"rate_limit_exceeded"</span>,
  <span class="str">"message"</span>: <span class="str">"100 requests per minute exceeded"</span>,
  <span class="str">"retry_after_seconds"</span>: <span class="cy">42</span>,
  <span class="str">"limit"</span>: <span class="cy">100</span>,
  <span class="str">"window"</span>: <span class="str">"1 minute"</span>
}

<span class="cm">// Good client behavior (using Retry-After):</span>
<span class="kw">if</span> (response.status === <span class="cy">429</span>) {
  retryAfter = response.headers.<span class="fn">get</span>(<span class="str">'Retry-After'</span>)
  <span class="kw">await</span> <span class="fn">sleep</span>(retryAfter * <span class="cy">1000</span>)
  <span class="kw">return</span> <span class="fn">retry</span>(request)  <span class="cm">// not immediately — that hammers the server</span>
}

<span class="cm">// Include on EVERY response (not just 429):</span>
<span class="cm">// Allows clients to monitor their quota proactively</span>
X-RateLimit-Limit:     <span class="cy">100</span>
X-RateLimit-Remaining: <span class="cy">73</span>   <span class="cm">← still have 73 left</span>
X-RateLimit-Reset:     <span class="cy">1700000060</span></pre>
  </div>
</div>

<!-- MULTI-TIER -->
<div class="view" id="view-multitier">
  <div class="sh">Multi-Tier Rate Limiting</div>
  <div class="sr">Production systems apply multiple limits simultaneously</div>
  <div class="tier-stack">
    <div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted);padding:6px 0;letter-spacing:2px">// REQUEST FLOWS THROUGH ALL TIERS — first violation wins (429)</div>
    <div class="tier-row" style="border-left-color:var(--red)">
      <div class="tr-where">CDN / Edge</div>
      <div class="tr-who">IP Address</div>
      <div class="tr-what">DDoS protection. Single IP flooding the system.</div>
      <div class="tr-limit" style="color:var(--red)">1,000 req/min per IP</div>
    </div>
    <div class="tier-row" style="border-left-color:var(--ora)">
      <div class="tr-where">API Gateway</div>
      <div class="tr-who">User ID</div>
      <div class="tr-what">Abuse prevention. One user monopolizing shared resources.</div>
      <div class="tr-limit" style="color:var(--ora)">100 req/min per user</div>
    </div>
    <div class="tier-row" style="border-left-color:var(--yel)">
      <div class="tr-where">API Service</div>
      <div class="tr-who">API Key / Tier</div>
      <div class="tr-what">Quota enforcement. Free vs Pro vs Enterprise daily limits.</div>
      <div class="tr-limit" style="color:var(--yel)">1K–∞ req/day per key</div>
    </div>
    <div class="tier-row" style="border-left-color:var(--grn)">
      <div class="tr-where">Endpoint</div>
      <div class="tr-who">User + Endpoint</div>
      <div class="tr-what">Resource protection. Expensive ops individually limited.</div>
      <div class="tr-limit" style="color:var(--grn)">5/min (login), 10/hr (email)</div>
    </div>
  </div>
  <div class="al cy"><em>Key design insight:</em> Different tiers protect different concerns and are applied at different layers. IP limits live at the CDN (before hitting origin). User limits live at the gateway. Quota lives in the application. Each layer defends against a different threat model.</div>
</div>

<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="mb9_tt(this)"><div class="t-num">01</div><div class="t-lbl">Boundary Burst Attack &amp; Fix</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Draw a timeline showing the boundary burst attack: limit=100 req/min, attacker sends 100 at 12:00:58 and 100 at 12:01:01. Show the counter values at each second.</li>
          <li>Implement sliding window counter in JavaScript (no Redis — just the math logic with mocked prev/curr counts)</li>
          <li>Apply the same attack to the sliding window counter: prev=100, curr=95, elapsed=0.017 (1 second in). Does it correctly block?</li>
          <li>What is the worst-case over-limit that sliding window counter can allow? (hint: think about what happens at the start of a new window)</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb9_tt(this)"><div class="t-num">02</div><div class="t-lbl">Token Bucket Implementation</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Implement <code>TokenBucket(capacity, refillRatePerSec)</code> in Java with <code>boolean tryConsume()</code></li>
          <li>Make it thread-safe (hint: synchronized block or AtomicLong + last refill timestamp)</li>
          <li>Test: capacity=10, rate=5/sec. Assert: 10 instant calls succeed, 11th fails, wait 0.2s, 12th succeeds</li>
          <li>How do you serialize this bucket to Redis so it survives server restarts? Write the HMSET schema and the Lua reconstruction logic.</li>
          <li>If the server was down for 1 hour and bucket was at 0 — what should happen on the next request? (cap at capacity, not at hours × rate)</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb9_tt(this)"><div class="t-num">03</div><div class="t-lbl">Distributed Rate Limiter</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>20 app servers, limit=100 req/min per user. Naive: each server enforces 100/20=5 req/min locally. What goes wrong? Give a specific failure scenario.</li>
          <li>Draw the sequence diagram for centralized Redis: Server A → Redis check → allow/reject → response</li>
          <li>Demonstrate the race condition: Servers A and B both see count=99, both increment. Show why Lua prevents this.</li>
          <li>Redis becomes unavailable for 60 seconds. Argue for both fail-open and fail-closed. Which do you choose and why?</li>
          <li>Design a circuit breaker for the Redis rate limiter: when Redis is down, switch to local approximate counter automatically</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--cyan)">
      <div class="task-hd" onclick="mb9_tt(this)"><div class="t-num" style="color:var(--cyan)">★</div><div class="t-lbl">Add Rate Limiting to URL Shortener (B5 Integration)</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Revisit your URL shortener from Module B5. Add production-grade rate limiting:</p>
        <ul>
          <li><strong>POST /shorten:</strong> 100 req/hour per IP (abuse prevention)</li>
          <li><strong>GET /{code}:</strong> 1,000 req/min per IP (DDoS protection)</li>
          <li><strong>POST /shorten:</strong> 1,000 req/day per user account (quota)</li>
        </ul>
        <ol>
          <li>Design the Redis key schema for all three limits</li>
          <li>Which algorithm for each? (justify: fixed window vs sliding window counter vs token bucket)</li>
          <li>Where in the architecture is each limit applied? (CDN vs API gateway vs application code)</li>
          <li>Write the complete HTTP 429 response for a failed POST /shorten with all required headers</li>
          <li>A premium user should get 10,000 req/day instead of 1,000. How does the application look up the user's tier before applying the limit?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 17 completed</span><span style="font-family:'Fira Code',monospace">MODULE B9 · RATE LIMITER</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Fixed Window: simple INCR — but boundary burst vulnerability</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sliding Window Log: exact, ZADD/ZREMRANGEBYSCORE — O(N) memory</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sliding Window Counter formula: prev×(1−elapsed) + curr</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sliding window counter: O(1) memory, 0.003% error, production default</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Token Bucket: capacity (burst) + refill_rate (sustained) — HMSET in Redis</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Leaky Bucket: constant output rate, queue-based, for downstream rate control</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Algorithm comparison table — when to use each</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Race condition: GET + SET is broken — need Lua for atomicity</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Lua scripts are atomic in Redis — no interleaving possible</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Distributed: centralized Redis (consistent hashing per user)</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Fail-open vs fail-closed: know the trade-offs and when to choose each</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">HTTP 429 headers: X-RateLimit-Limit, Remaining, Reset, Retry-After</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Multi-tier: IP (CDN) → user (gateway) → API key (app) → endpoint (app)</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">API gateway approach: NGINX / Kong / AWS API GW + Redis backend</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: boundary burst attack + sliding window fix</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: token bucket implementation (Java, thread-safe, Redis-serialized)</div></div>
    <div class="chk" onclick="mb9_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): rate limiting added to URL shortener</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--cyan)">
    <div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:28px;letter-spacing:1px;color:var(--white);margin-bottom:6px">B10 — Consistent Hashing &amp; Service Discovery</div>
    <div style="font-family:'Fira Code',monospace;font-size:9px;color:var(--muted);line-height:2">
      Virtual nodes · Minimal key remapping on node add/remove<br>
      Load distribution · Hot spot prevention · Rendez-vous hashing<br>
      Service registry (Consul/ZooKeeper) · Health checks · DNS-based discovery
    </div>
  </div>
</div>
</div>

<!-- Bottom Navigation -->
<div class="mb9-bottom-nav">
  <a href="/learning/system-design/hld/module-b8-youtube/" class="mb9-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb9-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    PREVIOUS: B8
  </a>
  <a href="/learning/system-design/hld/module-b9-notes/" class="mb9-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb9-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb9-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb9-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b10-consistent-hashing/" class="mb9-nav-footer-btn">
    NEXT: B10
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb9-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>
</div>
<script src="/assets/js/sd-module-b9.js"></script>
