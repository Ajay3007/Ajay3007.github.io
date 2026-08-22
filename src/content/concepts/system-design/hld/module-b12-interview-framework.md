---
title: "Module B12: System Design Interview Framework"
description: "SYSTEM DESIGN MASTERY · TRACK B · MODULE B12 · WEEK 22 INTERVIEW FRAMEWORK · MOCK INTERVIEWS · CAPSTONE TRACK B CAPSTONE · 45-MINUTE FRAMEWORK · 6 MOCK INTERVIEWS SYSTEM DESIGN…"
domain: system-design
track: system-design-hld
order: 124
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b12-interview-framework/
---

<link rel="stylesheet" href="/assets/css/sd-module-b12.css">
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Source+Code+Pro:wght@300;400;600&display=swap" rel="stylesheet">
<div class="sd-module-b12">
<header>
  <div class="hdr-stamp">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B12 · WEEK 22</span>
    <span>INTERVIEW FRAMEWORK · MOCK INTERVIEWS · CAPSTONE</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">TRACK B CAPSTONE · 45-MINUTE FRAMEWORK · 6 MOCK INTERVIEWS</div>
      <h1>SYSTEM DESIGN<br>INTERVIEW<br><span class="acc">FRAMEWORK</span></h1>
      <div class="hdr-sub">7-STEP FRAMEWORK · TIME MANAGEMENT · CAPACITY MATH<br>COMMUNICATION PATTERNS · COMMON MISTAKES · MOCK DRILLS</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">7</div><div class="hs-l">FRAMEWORK STEPS</div></div>
      <div class="hs"><div class="hs-v">45m</div><div class="hs-l">INTERVIEW WINDOW</div></div>
      <div class="hs"><div class="hs-v">6</div><div class="hs-l">MOCK INTERVIEWS</div></div>
      <div class="hs"><div class="hs-v">B12</div><div class="hs-l">FINAL MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg">7-Step Framework</div>
    <div class="tg" style="color:var(--red)">Requirements</div>
    <div class="tg" style="color:var(--blu)">Capacity Estimation</div>
    <div class="tg" style="color:var(--grn)">Communication</div>
    <div class="tg" style="color:var(--ora)">7 Mistakes</div>
    <div class="tg" style="color:var(--pur)">6 Mock Problems</div>
    <div class="tg">Quick Answers</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="mb12_show('framework',this)">7-Step Framework</div>
  <div class="nt" onclick="mb12_show('timer',this)">Time Map</div>
  <div class="nt" onclick="mb12_show('estimation',this)">Capacity Math</div>
  <div class="nt" onclick="mb12_show('communication',this)">Communication</div>
  <div class="nt" onclick="mb12_show('mistakes',this)">7 Mistakes</div>
  <div class="nt" onclick="mb12_show('mocks',this)">6 Mock Interviews</div>
  <div class="nt" onclick="mb12_show('quickanswers',this)">Quick Answers</div>
  <div class="nt" onclick="mb12_show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- FRAMEWORK -->
<div class="view active" id="view-framework">
  <div class="sh">The 7-Step Framework</div>
  <div class="sr">Use this structure for every system design interview — consistently</div>
  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-body">
        <div class="step-title">Requirements Clarification <span class="step-time">5 min</span></div>
        <p>Never start designing before you understand the problem. Interviewers will give partial information intentionally.</p>
        <span class="q">→ "How many daily active users are we targeting?"</span>
        <span class="q">→ "What is the read-to-write ratio?"</span>
        <span class="q">→ "Is this globally distributed or single-region?"</span>
        <span class="q">→ "What's the acceptable latency for the critical read path?"</span>
        <span class="q">→ "Strong consistency or eventual consistency acceptable?"</span>
        <span class="q">→ "What's the data retention period?"</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-body">
        <div class="step-title">Capacity Estimation <span class="step-time">5 min</span></div>
        <p>Rough numbers that constrain your design choices. Do the math out loud — it shows structured thinking.</p>
        <span class="q">→ QPS = daily_requests / 86,400 × peak_multiplier (3×)</span>
        <span class="q">→ Storage = writes/day × object_size × retention_years</span>
        <span class="q">→ Cache = total_hot_data × 0.2 (80/20 rule)</span>
        <span class="q">→ Bandwidth = peak_QPS × avg_response_size</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-body">
        <div class="step-title">High-Level Design <span class="step-time">10 min</span></div>
        <p>Draw the major components at box-and-arrow level. Cover both write path and read path. Don't over-detail yet.</p>
        <span class="q">→ Client → Load Balancer → Service(s) → Cache → DB</span>
        <span class="q">→ Identify: where does data enter, where does it get served</span>
        <span class="q">→ Mention async paths (queues) vs synchronous paths</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div class="step-body">
        <div class="step-title">Data Model &amp; API Design <span class="step-time">5 min</span></div>
        <p>Only the tables/schemas that matter for your deep dive. Core API endpoints — method, URL, key fields.</p>
        <span class="q">→ Don't design ALL tables. 2–3 critical ones only.</span>
        <span class="q">→ Show partition key / shard key choice</span>
        <span class="q">→ API: GET /timeline/{userId}?cursor=X&amp;limit=20</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">5</div>
      <div class="step-body">
        <div class="step-title">Deep Dive <span class="step-time">15 min</span></div>
        <p>This is where B1–B11 knowledge pays off. Pick 2–3 hard problems in your design and go deep. Show trade-off thinking.</p>
        <span class="q">→ Typical: hot read path, write bottleneck, consistency challenge</span>
        <span class="q">→ "For the fan-out problem, I see two approaches..."</span>
        <span class="q">→ "The cache invalidation here is tricky because..."</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">6</div>
      <div class="step-body">
        <div class="step-title">Bottlenecks &amp; Scaling <span class="step-time">4 min</span></div>
        <p>Where does your design break at 10× current scale? Address the biggest SPOFs and hot spots.</p>
        <span class="q">→ Single DB primary → add replicas, then shard</span>
        <span class="q">→ Single cache → Redis Cluster</span>
        <span class="q">→ Single region → multi-region with data replication</span>
      </div>
    </div>
    <div class="step">
      <div class="step-num">7</div>
      <div class="step-body">
        <div class="step-title">Summary <span class="step-time">1 min</span></div>
        <p>Restate the 3 key decisions you made and why. Mention what you'd do with more time. Leave a strong final impression.</p>
        <span class="q">→ "The three key decisions were: fan-out-on-write for the feed, Redis for the hot cache layer, and Cassandra for write-heavy storage."</span>
        <span class="q">→ "With more time, I'd explore multi-region replication."</span>
      </div>
    </div>
  </div>
</div>
<!-- TIMER -->
<div class="view" id="view-timer">
  <div class="sh">45-Minute Time Map</div>
  <div class="sr">The distribution that works — stick to it even under pressure</div>
  <div class="timer-grid">
    <div class="tm" style="border-color:var(--blu)">
      <div class="tm-min" style="color:var(--blu)">5m</div>
      <div class="tm-lbl">REQUIREMENTS<br>CLARIFICATION</div>
    </div>
    <div class="tm" style="border-color:var(--grn)">
      <div class="tm-min" style="color:var(--grn)">5m</div>
      <div class="tm-lbl">CAPACITY<br>ESTIMATION</div>
    </div>
    <div class="tm" style="border-color:var(--ink)">
      <div class="tm-min">10m</div>
      <div class="tm-lbl">HIGH-LEVEL<br>DESIGN</div>
    </div>
    <div class="tm" style="border-color:var(--ora)">
      <div class="tm-min" style="color:var(--ora)">5m</div>
      <div class="tm-lbl">DATA MODEL<br>&amp; API</div>
    </div>
    <div class="tm" style="border-color:var(--red);border-width:3px">
      <div class="tm-min" style="color:var(--red)">15m</div>
      <div class="tm-lbl">DEEP DIVE<br>← KEY ★</div>
    </div>
    <div class="tm" style="border-color:var(--pur)">
      <div class="tm-min" style="color:var(--pur)">4m</div>
      <div class="tm-lbl">BOTTLENECKS<br>&amp; SCALING</div>
    </div>
    <div class="tm" style="border-color:var(--muted)">
      <div class="tm-min" style="color:var(--muted)">1m</div>
      <div class="tm-lbl">SUMMARY<br>&amp; CLOSE</div>
    </div>
  </div>
  <div class="al ink"><em>The Deep Dive is where you are judged.</em> Steps 1–4 are table stakes — everyone can draw boxes. Steps 5–6 (deep dive + scaling) is where senior candidates separate themselves. Protect those 15 minutes fiercely. If you're still doing requirements at minute 10, cut it short and move on.</div>
</div>
<!-- ESTIMATION -->
<div class="view" id="view-estimation">
  <div class="sh">Capacity Estimation Cheat Sheet</div>
  <div class="sr">The numbers you need to have memorized before any interview</div>
  <table class="est-table">
    <thead><tr><th>CONVERSION</th><th>SHORTCUT</th><th>EXAMPLE</th></tr></thead>
    <tbody>
      <tr><td>1M req/day → QPS</td><td>= 12 QPS sustained; 36 QPS peak</td><td>Instagram 100M req/day = 1,200 QPS sustained</td></tr>
      <tr><td>1B req/day → QPS</td><td>= 12,000 QPS sustained; 36,000 peak</td><td>Twitter read traffic ~35K QPS</td></tr>
      <tr><td>1 day</td><td>≈ 86,400s (use 100K for rough math)</td><td>Never say "there are 1000 minutes in a day"</td></tr>
      <tr><td>1M users × 1KB</td><td>= 1 GB</td><td>100M users × 500 bytes = 50 GB</td></tr>
      <tr><td>1B users × 1KB</td><td>= 1 TB</td><td>YouTube metadata: 5B videos × 1KB = 5 TB</td></tr>
      <tr><td>1 photo avg</td><td>= 1 MB (thumbnail: 50KB)</td><td>Instagram 100M uploads/day = 100 TB/day</td></tr>
      <tr><td>1 video avg</td><td>= 50–500 MB</td><td>YouTube 500hr/min upload = ~90 TB/day</td></tr>
      <tr><td>1 tweet/message</td><td>= 140 bytes – 1 KB</td><td>Twitter 500M tweets/day = ~70 GB/day</td></tr>
    </tbody>
  </table>
  <div class="cb"><div class="cb-top">Worked example: Twitter-scale estimation out loud<span class="cb-l">TECHNIQUE</span></div>
<pre class="c"><span class="cm">// Question: Design Twitter. "Let me estimate scale first."</span>
 
DAU: 300M users
Tweets written: each user tweets 0.5×/day avg → 150M tweets/day
Reads: 100:1 ratio → 15B reads/day → 15B/86400 ≈ <span class="hl">180K read QPS</span>
Writes: 150M/86400 ≈ <span class="hl">1,750 write QPS</span> ≈ 2K write QPS
 
Storage per tweet: content 140B + metadata 100B + indices ~300B ≈ <span class="hl">550 bytes</span>
Daily storage: 150M × 550B = <span class="hl">82 GB/day</span>
10 years: 82 × 365 × 10 ≈ 300 TB (just tweet text, no media)
 
Cache for hot tweets: 20% of reads hit 80% of data (Pareto)
Hot set: cache 20% of daily reads = 20% × 180K QPS × avg 500B = <span class="hl">~18 GB hot set</span>
<span class="cm">// Now I know: I need a system handling 180K reads/sec, 2K writes/sec,</span>
<span class="cm">// ~80 GB/day new storage, 18 GB hot cache. This drives my design choices.</span></pre>
  </div>
</div>
<!-- COMMUNICATION -->
<div class="view" id="view-communication">
  <div class="sh">Communication Patterns</div>
  <div class="sr">What interviewers actually listen for — and what signals seniority</div>
  <div class="gb">
    <div class="gb-col">
      <div class="gb-head" style="color:var(--red)">❌ JUNIOR PATTERN</div>
      <div class="gb-body">
        "I'll use Kafka."<br><br>
        "Redis is the best option here."<br><br>
        "MySQL for the database."<br><br>
        [silence — drawing without explanation]<br><br>
        [waits for interviewer to ask about failures]
      </div>
    </div>
    <div class="gb-col">
      <div class="gb-head" style="color:var(--grn)">✓ SENIOR PATTERN</div>
      <div class="gb-body">
        "For 50K write QPS with at-least-once delivery, Kafka fits — though it adds operational complexity."<br><br>
        "Redis solves the hot-read problem here. The trade-off is cache invalidation complexity and sizing."<br><br>
        "For this read:write ratio and need for flexible queries, PostgreSQL — we can shard by user_id later."<br><br>
        "I'm adding a cache here because the read path is 100:1 over writes and most reads are for recent data..."<br><br>
        "Let me think about failure modes. If this service goes down, I want the write path to still work..."
      </div>
    </div>
  </div>
  <div class="al grn"><em>The senior-signal question:</em> Before committing to any technology, say: "I see two approaches here — [A] and [B]. [A] gives us [benefit] but costs [trade-off]. [B] is simpler but doesn't handle [edge case]. Given [constraint from requirements], I'll go with [A]." This shows that you considered alternatives — which is what senior engineers actually do.</div>
</div>
<!-- MISTAKES -->
<div class="view" id="view-mistakes">
  <div class="sh">7 Common Mistakes</div>
  <div class="sr">Every one of these has caused otherwise-qualified candidates to fail</div>
  <div class="mistake-list">
    <div class="mk"><div class="mk-num">1</div><div class="mk-body"><div class="mk-title">JUMPING TO SOLUTIONS WITHOUT REQUIREMENTS</div><div class="mk-fix">Fix: Force yourself to spend 5 full minutes on requirements. Repeat back: "So I'm building a system for X users, Y QPS, with Z consistency requirement — is that correct?" Get explicit confirmation before drawing anything.</div></div></div>
    <div class="mk"><div class="mk-num">2</div><div class="mk-body"><div class="mk-title">DESIGNING FOR ONE SERVER</div><div class="mk-fix">Fix: Always think distributed by default. Even for "simple" systems, ask about scale first. A system with 10K QPS requires load balancing, connection pooling, and at least 2 servers. Assume you need to scale.</div></div></div>
    <div class="mk"><div class="mk-num">3</div><div class="mk-body"><div class="mk-title">AVOIDING TRADE-OFFS — "THIS SOLUTION HANDLES EVERYTHING"</div><div class="mk-fix">Fix: Every technology choice has costs. If you pick Kafka: mention the latency overhead, operational complexity, at-least-once semantics. If you pick Cassandra: mention you can't do JOINs, no strong consistency. Acknowledging trade-offs shows maturity.</div></div></div>
    <div class="mk"><div class="mk-num">4</div><div class="mk-body"><div class="mk-title">NOT KNOWING THE NUMBERS</div><div class="mk-fix">Fix: Memorize the estimation table. Doing math out loud (even approximations) shows discipline. "1B req/day ÷ 100K seconds = 10K QPS × 3 peak = 30K peak QPS" said in 10 seconds is far more impressive than "should be fine."</div></div></div>
    <div class="mk"><div class="mk-num">5</div><div class="mk-body"><div class="mk-title">DESIGNING ALONE, NOT COLLABORATING</div><div class="mk-fix">Fix: Check in every 5–8 minutes. "I'm thinking of separating read and write paths here — does that seem like the right direction to explore?" Interviewing is a collaborative exercise. Interviewers want to see how you work with others.</div></div></div>
    <div class="mk"><div class="mk-num">6</div><div class="mk-body"><div class="mk-title">SPENDING 20 MINUTES ON CRUD</div><div class="mk-fix">Fix: Cover the obvious parts quickly: "Standard REST CRUD, JWT auth, HTTPS everywhere — 2 minutes." Save your time for the hard distributed systems problems: fan-out, consistency, failure handling. That's where the interview is won or lost.</div></div></div>
    <div class="mk"><div class="mk-num">7</div><div class="mk-body"><div class="mk-title">NO FAILURE HANDLING IN THE DESIGN</div><div class="mk-fix">Fix: Proactively discuss failures. "What if the cache is unavailable? I'd add a circuit breaker and fall back to DB reads." "What if the notification service is slow? I'd make it async with a queue and retry." Cover the top 2–3 failure scenarios before being asked.</div></div></div>
  </div>
</div>
<!-- MOCKS -->
<div class="view" id="view-mocks">
  <div class="sh">6 Mock Interview Problems</div>
  <div class="sr">One per day — timed, 45 minutes, no notes until after</div>
  <div class="mock-grid">
    <div class="mc" style="border-top-color:var(--grn)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 1 · DAY 1 · WARMUP</div>
        <div class="mc-title">Design Pastebin / URL Shortener</div>
        <div class="mc-diff" style="color:var(--grn);border-color:var(--grn)">EASY</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">1M pastes/day · 100M reads/day · max 10 MB paste</div>
        <div class="mc-keys">Key decisions: ID generation (base62), text in S3 vs DB, expiry strategy, CDN for large pastes, async analytics.</div>
        <div class="mc-deep">Deep dive: cache tier for popular pastes, ID collision handling, lazy vs background expiry cleanup</div>
      </div>
    </div>
    <div class="mc" style="border-top-color:var(--blu)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 2 · DAY 2 · COMPONENT</div>
        <div class="mc-title">Design a Notification System</div>
        <div class="mc-diff" style="color:var(--blu);border-color:var(--blu)">MEDIUM</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">10M notifications/day · push + email + SMS · &lt;30s delivery</div>
        <div class="mc-keys">Key decisions: channel routing (FCM/APNs/SES/Twilio), priority queues, user preferences, retry + fallback logic, deduplication.</div>
        <div class="mc-deep">Deep dive: retry/fallback when push fails → SMS, dedup across channels, delivery receipts</div>
      </div>
    </div>
    <div class="mc" style="border-top-color:var(--ora)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 3 · DAY 3 · DISTRIBUTED</div>
        <div class="mc-title">Distributed Job Scheduler</div>
        <div class="mc-diff" style="color:var(--ora);border-color:var(--ora)">MEDIUM-HARD</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">1M jobs · 1K jobs/sec peak triggering · at-most-once execution</div>
        <div class="mc-keys">Key decisions: storage (DB partitioned by scheduled_time), time-wheel vs priority queue, leader election, exactly-once execution, dead job recovery.</div>
        <div class="mc-deep">Deep dive: preventing two nodes from running same job, crash recovery, cron expression parsing</div>
      </div>
    </div>
    <div class="mc" style="border-top-color:var(--red)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 4 · DAY 4 · HARD</div>
        <div class="mc-title">Design Google Drive / Dropbox</div>
        <div class="mc-diff" style="color:var(--red);border-color:var(--red)">HARD</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">50M DAU · 100M uploads/day · avg 500KB · 10 PB total</div>
        <div class="mc-keys">Key decisions: chunked upload (4MB chunks, SHA-256 dedup), delta sync (changed chunks only), metadata DB + S3, sync protocol, conflict resolution.</div>
        <div class="mc-deep">Deep dive: chunk deduplication across users, delta sync algorithm, last-write-wins vs OT conflict resolution</div>
      </div>
    </div>
    <div class="mc" style="border-top-color:var(--pur)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 5 · DAY 5 · HARD</div>
        <div class="mc-title">Live Streaming Platform</div>
        <div class="mc-diff" style="color:var(--pur);border-color:var(--pur)">HARD</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">1K streamers · 10M viewers · 100K viewers/top stream · &lt;10s latency</div>
        <div class="mc-keys">Key decisions: RTMP ingest → HLS transcode, CDN fan-out, WebSocket chat, viewer count (HyperLogLog), HLS vs WebRTC latency trade-off.</div>
        <div class="mc-deep">Deep dive: transcoding pipeline parallelism, chat fan-out at 100K viewers, approximate viewer count</div>
      </div>
    </div>
    <div class="mc" style="border-top-color:var(--muted)">
      <div class="mc-hdr">
        <div class="mc-label">MOCK 6 · DAY 6 · SYNTHESIS</div>
        <div class="mc-title">Search Autocomplete</div>
        <div class="mc-diff" style="color:var(--muted);border-color:var(--muted)">MEDIUM</div>
      </div>
      <div class="mc-body">
        <div class="mc-scale">10K autocomplete QPS · 100M unique queries/day in logs · top-10 suggestions</div>
        <div class="mc-keys">Key decisions: trie vs inverted index, precompute top-N per prefix, daily batch update pipeline from logs, shard trie by prefix range.</div>
        <div class="mc-deep">Deep dive: trie sharding, pre-computation vs on-the-fly, unicode + multilingual handling</div>
      </div>
    </div>
  </div>
  <div class="al ink"><em>Practice protocol:</em> Set a 45-minute timer. Draw on paper or a whiteboard. No notes. After time is up, review against the module notes and identify the 2–3 things you missed. Do NOT review the answer before attempting — the discomfort of not knowing is the practice.</div>
</div>
<!-- QUICK ANSWERS -->
<div class="view" id="view-quickanswers">
  <div class="sh">Quick Answer Cheat Sheet</div>
  <div class="sr">Interviewer probes — have these answers ready in 30 seconds</div>
  <div class="qa-list">
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you handle hot partitions / hot keys?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Add a random suffix (0–9) to the partition key to spread load across 10× more partitions. Combine results at read time. Alternatively, cache hot keys separately in Redis with a short TTL. For write-heavy hot keys, use a write-behind cache. Consistent hashing with virtual nodes also mitigates hot spots by distributing keys more evenly.</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you prevent thundering herd on cache expiry?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Three approaches: (1) Probabilistic early expiration — with probability proportional to time-to-expiry, refresh early before expiry hits all at once. (2) Mutex/lock on cache miss — first thread refreshes, others wait. Use Redis SETNX as a distributed lock with short TTL. (3) Background refresh — proactively refresh popular keys before expiry, keeping them always warm.</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you achieve exactly-once processing in Kafka?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Kafka delivers at-least-once by default. To achieve effectively-once: use idempotent consumers — check an idempotency key in the DB before processing, and store it atomically with the result. For stricter needs, Kafka Transactions (EOS — exactly-once semantics) enable atomic produce+consume operations. The outbox pattern (B11) combined with idempotent consumers gives effectively-exactly-once end-to-end.</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you handle cascading failures between services?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Circuit breaker pattern: after N consecutive failures to a downstream service, the circuit "opens" — requests fail fast without hitting the service. After a timeout, a "half-open" probe is sent; if it succeeds, circuit closes. Bulkhead pattern: isolate thread pools per downstream service so one slow service doesn't exhaust the shared pool. Timeout + retry with exponential backoff for transient failures. Fallback: cached result, degraded response, or graceful error.</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How would you design for multi-region?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Active-active: both regions serve reads and writes, data replicated asynchronously (DynamoDB Global Tables, CockroachDB). Conflict resolution needed. Active-passive: primary region handles writes, secondary is hot standby — failover when primary goes down. Latency-based routing (Route 53) sends users to nearest region. GDPR: EU user data must stay in EU region — use regional data classification. RPO/RTO: async replication has seconds of potential data loss (RPO); failover automation targets minutes (RTO).</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you do zero-downtime schema migrations?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Expand-contract (also called parallel change): Step 1 — Add new column (nullable, no default); existing code ignores it. Step 2 — Dual-write: new code writes to both old and new columns. Step 3 — Backfill: migrate old data to new column via background job. Step 4 — Switch reads: code now reads from new column. Step 5 — Stop writing to old column. Step 6 — Drop old column. Never run ALTER TABLE on a large live table without this — it takes an exclusive lock and blocks all queries.</div></div>
    <div class="qa"><div class="qa-hd" onclick="mb12_qa(this)"><div class="qa-q">"How do you ensure high availability for stateful services?"</div><div class="qa-arr">›</div></div><div class="qa-bd">Run multiple instances behind a load balancer. For sessions: externalize state to Redis (stateless app servers). For leader election (e.g., Saga Orchestrator): use Zookeeper ephemeral nodes or etcd leases — leader holds a lease, followers compete to acquire it on expiry. Health checks: remove unhealthy instances from rotation within 10–30 seconds. DB: primary-replica with automatic failover (RDS Multi-AZ, Patroni for Postgres).</div></div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 13 completed</span><span style="font-family:'Source Code Pro',monospace">MODULE B12 · INTERVIEW FRAMEWORK</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">7-step framework memorized — can recite steps + time allocations without notes</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">6 requirements questions to always ask (DAU, ratio, latency, consistency, geo, retention)</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Capacity math: 1B/day = 12K QPS, 1M users × 1KB = 1GB, 1 photo = 1MB</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Communication: state reasoning before answer, proactive trade-offs, drive conversation</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">7 mistakes internalized — know what symptom looks like and how to avoid it</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Quick answers: hot partitions, thundering herd, exactly-once, cascading failures, multi-region</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 1 (Pastebin) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 2 (Notifications) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 3 (Job Scheduler) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 4 (Google Drive) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 5 (Live Streaming) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mock 6 (Autocomplete) — 45-min timed session completed</div></div>
    <div class="chk" onclick="mb12_tick(this)"><div class="chk-box"></div><div class="chk-lbl">All 6 mocks reviewed against module notes — gaps identified and studied</div></div>
  </div>
  <div style="margin-top:32px;background:var(--ink);color:var(--bg);padding:28px;text-align:center">
    <div style="font-family:'Source Code Pro',monospace;font-size:8px;letter-spacing:3px;color:var(--faded);margin-bottom:10px">TRACK B — COMPLETE</div>
    <div style="font-family:'Special Elite',cursive;font-size:32px;margin-bottom:12px">Track B: HLD Mastered</div>
    <div style="font-family:'Source Code Pro',monospace;font-size:10px;color:var(--faded);line-height:2.2;margin-bottom:16px">
      B1 Fundamentals · B2 Databases · B3 Caching · B4 Message Queues<br>
      B5 URL Shortener · B6 Twitter Feed · B7 WhatsApp · B8 YouTube<br>
      B9 Rate Limiter · B10 Consistent Hashing · B11 Distributed Tx · B12 Interview Framework
    </div>
    <div style="font-family:'Source Code Pro',monospace;font-size:8px;letter-spacing:2px;color:var(--faded);border-top:1px solid rgba(255,255,255,.2);padding-top:12px">
      NEXT: Track A (LLD) Complete · Track B (HLD) Complete · Ready for FAANG Interviews
    </div>
  </div>
</div>
</div>
<!-- Bottom Navigation (3-button — final module) -->
<div class="mb12-bottom-nav">
  <a href="/learning/system-design/hld/module-b11-distributed-tx/" class="mb12-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb12-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    PREVIOUS: B11
  </a>
  <a href="/learning/system-design/hld/module-b12-notes/" class="mb12-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb12-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb12-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb12-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b13-ml-systems/" class="mb12-nav-footer-btn">
    NEXT: B13 ML SYSTEMS
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb12-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>
</div>
<script src="/assets/js/sd-module-b12.js"></script>
