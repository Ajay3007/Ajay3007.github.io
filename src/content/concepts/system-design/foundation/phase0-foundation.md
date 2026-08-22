---
title: "Phase 0 — Foundation Primer"
description: "// system design mastery phase 0 Foundation Primer Weeks 1 2 Topics 5 Tasks 5 Track Universal All Learners & 127760; Internet & 9881; OS Fundamentals & 128451; Database Basics…"
domain: system-design
order: 99
chrome: bare
ownHeader: true
url: /learning/system-design/foundation/phase0-foundation/
---

<link rel="stylesheet" href="/assets/css/sd-phase0.css">

<div class="header">
  <div class="eyebrow">// system design mastery &middot; phase 0</div>
  <h1>Foundation Primer</h1>
  <div class="chips">
    <div class="chip">Weeks <b>1&ndash;2</b></div>
    <div class="chip">Topics <b>5</b></div>
    <div class="chip">Tasks <b>5</b></div>
    <div class="chip">Track <b>Universal &mdash; All Learners</b></div>
  </div>
</div>

<div class="nav">
  <div class="tab active" onclick="show('internet',this)">&#127760; Internet</div>
  <div class="tab" onclick="show('os',this)">&#9881; OS Fundamentals</div>
  <div class="tab" onclick="show('db',this)">&#128451; Database Basics</div>
  <div class="tab" onclick="show('framework',this)">&#129517; SD Framework</div>
  <div class="tab" onclick="show('estimation',this)">&#128208; Estimation</div>
  <div class="tab" onclick="show('tradeoffs',this)">&#9878; Trade-offs</div>
  <div class="tab" onclick="show('checklist',this)">&#9989; Checklist</div>
</div>

<!-- INTERNET -->
<div class="sec active" id="s-internet">
  <div class="sec-title">How the Internet Works</div>
  <div class="sec-sub">Topic 0.1 &middot; DNS &middot; TCP/IP &middot; HTTP &middot; WebSocket</div>
  <div class="grid3">
    <div class="card" style="border-top:3px solid var(--amber)">
      <div class="card-label" style="color:var(--amber)">DNS</div>
      <b style="font-size:15px">The Phone Book</b>
      <p style="margin:8px 0;font-size:13px;color:var(--ink2)">Hierarchical distributed cache. TTL controls freshness. Propagation lag matters for zero-downtime deploys.</p>
      <pre>Browser cache
&#8594; OS cache
&#8594; Recursive Resolver
&#8594; Root NS &#8594; TLD NS
&#8594; Authoritative NS</pre>
    </div>
    <div class="card" style="border-top:3px solid var(--blue)">
      <div class="card-label" style="color:var(--blue)">TCP/IP</div>
      <b style="font-size:15px">The Reliable Pipe</b>
      <p style="margin:8px 0;font-size:13px;color:var(--ink2)">Ordered reliable delivery via 3-way handshake, ACKs, retransmission, flow + congestion control.</p>
      <pre><span class="cg">SYN</span> &#8594; <span class="ca">SYN-ACK</span> &#8594; <span class="cg">ACK</span>
<span class="cm">&#91;connected&#93;</span>
 
TCP: reliable &#8594; <span class="cm">HTTP, DB</span>
UDP: fast &#8594; <span class="cm">video, DNS</span></pre>
    </div>
    <div class="card" style="border-top:3px solid var(--green)">
      <div class="card-label" style="color:var(--green)">HTTP Methods</div>
      <b style="font-size:15px">Idempotency</b>
      <pre><span class="ca">GET</span>    idempotent, safe
<span class="ca">POST</span>   NOT idempotent
<span class="ca">PUT</span>    idempotent
<span class="ca">PATCH</span>  NOT idempotent
<span class="ca">DELETE</span> idempotent</pre>
    </div>
  </div>
  <div class="card">
    <div class="card-label">HTTP Status Codes &mdash; Memorize These</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px;margin-top:8px">
      <div><span class="badge bg">2xx SUCCESS</span><pre style="margin-top:6px">200 OK
201 Created
204 No Content</pre></div>
      <div><span class="badge bb">3xx REDIRECT</span><pre style="margin-top:6px">301 Moved Permanently
302 Found
304 Not Modified</pre></div>
      <div><span class="badge ba">4xx CLIENT</span><pre style="margin-top:6px">400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
<span class="ca">429 Too Many Reqs</span></pre></div>
      <div><span class="badge br">5xx SERVER</span><pre style="margin-top:6px">500 Internal Error
502 Bad Gateway
<span class="ca">503 Unavailable</span>
504 Gateway Timeout</pre></div>
    </div>
  </div>
  <div class="tip"><span class="tip-n">01</span>When asked "walk me through what happens when you type a URL" &mdash; DNS is step 1. Interviewers notice when candidates skip it.</div>
  <div class="tip"><span class="tip-n">02</span><b>429</b> (rate limiting) and <b>503</b> (service overload) appear in nearly every SD discussion. Know them cold.</div>
  <div class="tip"><span class="tip-n">03</span>Use WebSocket for real-time bidirectional (chat, live scores). Use long-polling for infrequent server push. Never WebSocket for simple CRUD &mdash; unnecessary overhead.</div>
</div>

<!-- OS -->
<div class="sec" id="s-os">
  <div class="sec-title">OS Fundamentals</div>
  <div class="sec-sub">Topic 0.2 &middot; Processes &middot; Threads &middot; I/O Models &middot; Memory Latency</div>
  <div class="grid2">
    <div class="card">
      <div class="card-label" style="color:var(--blue)">Process</div>
      <pre><span class="cg">+</span> Independent memory space
<span class="cg">+</span> Crash isolation
<span class="cg">+</span> IPC: pipes, sockets
<span class="cr">-</span> Heavy context switch ~1-10&#956;s
<span class="cr">-</span> Expensive to spawn</pre>
    </div>
    <div class="card">
      <div class="card-label" style="color:var(--green)">Thread</div>
      <pre><span class="cg">+</span> Shared heap memory
<span class="cg">+</span> Fast context switch
<span class="cg">+</span> Cheap to spawn
<span class="cr">-</span> One crash kills process
<span class="cr">-</span> Needs synchronization</pre>
    </div>
  </div>
  <div class="card" style="margin-bottom:20px">
    <div class="card-label">Blocking vs Non-Blocking I/O</div>
    <div class="grid2" style="margin-top:12px;margin-bottom:0">
      <div>
        <div style="font-weight:600;color:var(--red);margin-bottom:6px">&#10060; Blocking</div>
        <pre>Thread &#8594; I/O request
Thread <span class="cr">WAITS</span> (idle)
I/O completes
Thread continues
 
10K connections
= 10K idle threads
= ~10 GB RAM wasted</pre>
      </div>
      <div>
        <div style="font-weight:600;color:var(--green);margin-bottom:6px">&#9989; Non-Blocking</div>
        <pre>Thread &#8594; I/O request
Thread continues work
OS notifies on complete
(callback / future)
 
10K connections
= 1 thread handles all
= minimal RAM used</pre>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-label">Memory Latency &mdash; MEMORIZE THIS</div>
    <p style="font-size:12px;color:var(--muted);margin:6px 0 18px">These numbers are your interview ammunition. Know them by heart.</p>
    <div class="lat-row"><div class="lat-lbl">Registers</div><div class="lat-bg"><div class="lat-fill" style="width:0.4%;background:#2a6b4a"></div></div><div class="lat-val">~1 ns</div></div>
    <div class="lat-row"><div class="lat-lbl">L1 Cache</div><div class="lat-bg"><div class="lat-fill" style="width:0.8%;background:#2a6b4a"></div></div><div class="lat-val">~4 ns</div></div>
    <div class="lat-row"><div class="lat-lbl">L2 Cache</div><div class="lat-bg"><div class="lat-fill" style="width:1.5%;background:#3d7a5a"></div></div><div class="lat-val">~12 ns</div></div>
    <div class="lat-row"><div class="lat-lbl">L3 Cache</div><div class="lat-bg"><div class="lat-fill" style="width:2.5%;background:#4a8a6a"></div></div><div class="lat-val">~40 ns</div></div>
    <div class="lat-row"><div class="lat-lbl" style="color:var(--amber);font-weight:600">RAM &#9733;</div><div class="lat-bg"><div class="lat-fill" style="width:5%;background:var(--amber)"></div></div><div class="lat-val" style="color:var(--amber);font-weight:600">~100 ns</div></div>
    <div class="lat-row"><div class="lat-lbl">SSD</div><div class="lat-bg"><div class="lat-fill" style="width:40%;background:#a05a2a"></div></div><div class="lat-val" style="color:var(--red)">~100 &#956;s</div></div>
    <div class="lat-row"><div class="lat-lbl">HDD</div><div class="lat-bg"><div class="lat-fill" style="width:80%;background:#8a2020"></div></div><div class="lat-val" style="color:var(--red)">~10 ms</div></div>
    <div class="lat-row"><div class="lat-lbl">Network LAN</div><div class="lat-bg"><div class="lat-fill" style="width:30%;background:var(--blue)"></div></div><div class="lat-val">~1 ms</div></div>
    <div class="lat-row"><div class="lat-lbl">Network WAN</div><div class="lat-bg"><div class="lat-fill" style="width:68%;background:var(--purple)"></div></div><div class="lat-val">~100 ms</div></div>
    <div class="tip" style="margin-top:16px"><span class="tip-n">&#9733;</span>RAM is <b>1,000&#215; faster than SSD</b> and <b>100,000&#215; faster than HDD</b>. This single fact justifies every caching layer ever built.</div>
  </div>
</div>

<!-- DB -->
<div class="sec" id="s-db">
  <div class="sec-title">Database Basics</div>
  <div class="sec-sub">Topic 0.3 &middot; ACID &middot; Indexing &middot; Isolation Levels &middot; SQL vs NoSQL</div>
  <div class="card" style="margin-bottom:20px">
    <div class="card-label">ACID Properties</div>
    <div class="grid4" style="margin-top:14px">
      <div class="acidsq" style="background:var(--amber-light)">
        <div style="font-family:'DM Serif Display',serif;font-size:36px;color:var(--amber)">A</div>
        <div style="font-weight:600;margin:6px 0">Atomicity</div>
        <div style="font-size:12px;color:var(--ink2)">All succeed or ALL fail. No partial writes.</div>
      </div>
      <div class="acidsq" style="background:var(--green-light)">
        <div style="font-family:'DM Serif Display',serif;font-size:36px;color:var(--green)">C</div>
        <div style="font-weight:600;margin:6px 0">Consistency</div>
        <div style="font-size:12px;color:var(--ink2)">DB moves between valid states. Constraints hold.</div>
      </div>
      <div class="acidsq" style="background:var(--blue-light)">
        <div style="font-family:'DM Serif Display',serif;font-size:36px;color:var(--blue)">I</div>
        <div style="font-weight:600;margin:6px 0">Isolation</div>
        <div style="font-size:12px;color:var(--ink2)">Concurrent tx don't interfere with each other.</div>
      </div>
      <div class="acidsq" style="background:var(--purple-light)">
        <div style="font-family:'DM Serif Display',serif;font-size:36px;color:var(--purple)">D</div>
        <div style="font-weight:600;margin:6px 0">Durability</div>
        <div style="font-size:12px;color:var(--ink2)">Committed data survives crashes (WAL).</div>
      </div>
    </div>
    <pre style="margin-top:16px">Bank transfer: Debit $100 from A &rarr; Credit $100 to B
Without Atomicity:  Debit <span class="cg">&#10003;</span> + Credit <span class="cr">&#10005;</span> = $100 <span class="cr">disappears</span>
Without Isolation:  Third tx reads mid-transfer = <span class="cr">wrong balance</span></pre>
  </div>
  <div class="grid2">
    <div class="card">
      <div class="card-label">B-Tree Indexing</div>
      <pre>No index:
SELECT * WHERE email='x@y.com'
&rarr; full table scan &rarr; <span class="cr">O(n)</span>
 
With B-tree index:
&rarr; tree traversal &rarr; <span class="cg">O(log n)</span>
 
Composite index (A,B,C):
<span class="cg">&#10003;</span> query on A
<span class="cg">&#10003;</span> query on (A,B)
<span class="cg">&#10003;</span> query on (A,B,C)
<span class="cr">&#10005;</span> query on B alone</pre>
    </div>
    <div class="card">
      <div class="card-label">Isolation Levels</div>
      <table>
        <tr><th>Level</th><th>Dirty?</th><th>NRR?</th><th>Speed</th></tr>
        <tr><td>Read Uncommitted</td><td style="color:var(--red)">Yes</td><td style="color:var(--red)">Yes</td><td style="color:var(--green)">Fastest</td></tr>
        <tr><td>Read Committed</td><td style="color:var(--green)">No</td><td style="color:var(--red)">Yes</td><td style="color:var(--green)">Fast</td></tr>
        <tr><td>Repeatable Read</td><td style="color:var(--green)">No</td><td style="color:var(--green)">No</td><td>Moderate</td></tr>
        <tr><td>Serializable</td><td style="color:var(--green)">No</td><td style="color:var(--green)">No</td><td style="color:var(--red)">Slowest</td></tr>
      </table>
      <div class="tip" style="margin-top:10px"><span class="tip-n">&#9432;</span>Most DBs default to Read Committed or Repeatable Read.</div>
    </div>
  </div>
  <div class="card">
    <div class="card-label">SQL vs NoSQL &mdash; First Mental Model</div>
    <table style="margin-top:10px">
      <tr><th>Dimension</th><th>SQL</th><th>NoSQL</th></tr>
      <tr><td>ACID</td><td style="color:var(--green)">&#10003; Full</td><td style="color:var(--amber)">&#9888; Varies</td></tr>
      <tr><td>Joins</td><td style="color:var(--green)">&#10003; Native</td><td style="color:var(--red)">&#10005; Limited</td></tr>
      <tr><td>Horizontal scale</td><td style="color:var(--red)">&#10005; Hard</td><td style="color:var(--green)">&#10003; Native</td></tr>
      <tr><td>Schema</td><td>Rigid</td><td>Flexible</td></tr>
      <tr><td>Best for</td><td>Finance, accounts, inventory</td><td>Feeds, sessions, IoT, search</td></tr>
    </table>
    <div class="tip" style="margin-top:12px"><span class="tip-n">&rarr;</span>Deep dive in <b>Module B6</b>: sharding, replication, leader election. This is just the mental model.</div>
  </div>
</div>

<!-- FRAMEWORK -->
<div class="sec" id="s-framework">
  <div class="sec-title">The SD Interview Framework</div>
  <div class="sec-sub">Topic 0.4 &middot; 5 steps &middot; 45 minutes &middot; Applied to every system in this course</div>
  <div class="card" style="background:var(--ink);color:var(--bg);margin-bottom:24px">
    <div style="display:flex;justify-content:space-around;flex-wrap:wrap;gap:8px;text-align:center">
      <div><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#f0d98a">5</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">REQUIREMENTS</div></div>
      <div style="font-size:24px;color:rgba(255,255,255,0.2);align-self:center">+</div>
      <div><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#f0d98a">5</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">ESTIMATION</div></div>
      <div style="font-size:24px;color:rgba(255,255,255,0.2);align-self:center">+</div>
      <div><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#f0d98a">15</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">HLD</div></div>
      <div style="font-size:24px;color:rgba(255,255,255,0.2);align-self:center">+</div>
      <div><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#f0d98a">15</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">DEEP DIVE</div></div>
      <div style="font-size:24px;color:rgba(255,255,255,0.2);align-self:center">+</div>
      <div><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#f0d98a">5</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">TRADE-OFFS</div></div>
      <div style="font-size:24px;color:rgba(255,255,255,0.2);align-self:center">=</div>
      <div style="background:rgba(255,255,255,0.08);padding:8px 16px;border-radius:4px"><div style="font-family:'DM Serif Display',serif;font-size:32px;color:#7ec994">45 min</div><div style="font-size:10px;font-family:'DM Mono',monospace;color:rgba(255,255,255,0.45);letter-spacing:1px">TOTAL</div></div>
    </div>
  </div>
  <div class="fw-step" onclick="this.classList.toggle('open')">
    <div class="fw-num">1</div>
    <div>
      <div class="fw-title">Clarify Requirements</div>
      <div class="fw-time">~5 min &mdash; Never skip this step</div>
      <div class="fw-detail"><b>Functional:</b> Top 3 features? Who are users? Read/write ratio? Priority flows?<br><br><b>Non-functional:</b> DAU/QPS/data? Availability SLA (99.9% = 8.7 hr downtime/yr)? Latency target? Consistency? Global or single-region?<br><br><b>Tip:</b> Interviewers leave requirements vague intentionally. Asking these IS the evaluation.</div>
    </div>
  </div>
  <div class="fw-step" onclick="this.classList.toggle('open')">
    <div class="fw-num">2</div>
    <div>
      <div class="fw-title">Back-of-Envelope Estimation</div>
      <div class="fw-time">~5 min &mdash; Numbers drive architecture</div>
      <div class="fw-detail">Write QPS = DAU &times; writes/day / 86,400 &nbsp;|&nbsp; Read QPS = DAU &times; reads/day / 86,400<br>Peak QPS = Avg &times; 3 &nbsp;|&nbsp; Storage/day = writes/day &times; avg size &nbsp;|&nbsp; Storage/5yr = /day &times; 1,825<br><br><b>Rule:</b> Every number must drive a design decision. If it doesn't &mdash; skip the calculation.</div>
    </div>
  </div>
  <div class="fw-step" onclick="this.classList.toggle('open')">
    <div class="fw-num">3</div>
    <div>
      <div class="fw-title">High-Level Design</div>
      <div class="fw-time">~15 min &mdash; System at 30,000 feet</div>
      <div class="fw-detail">Standard topology: Client &rarr; CDN &rarr; Load Balancer &rarr; App Servers &rarr; Cache &rarr; Database &rarr; Queue &rarr; Workers<br><br><b>Rule:</b> Every box you draw must be justifiable. Don't add components for decoration.</div>
    </div>
  </div>
  <div class="fw-step" onclick="this.classList.toggle('open')">
    <div class="fw-num">4</div>
    <div>
      <div class="fw-title">Deep Dive (2&ndash;3 components)</div>
      <div class="fw-time">~15 min &mdash; Go deep where it matters</div>
      <div class="fw-detail">Common targets: DB schema + indexing &middot; Cache eviction/invalidation &middot; Queue delivery guarantees &middot; API + rate limiting &middot; Sharding strategy<br><br><b>Tip:</b> Lead toward your strongest area. "I'd like to deep dive sharding &mdash; that's where the interesting trade-offs are."</div>
    </div>
  </div>
  <div class="fw-step" onclick="this.classList.toggle('open')">
    <div class="fw-num">5</div>
    <div>
      <div class="fw-title">Trade-offs &amp; Bottlenecks</div>
      <div class="fw-time">~5 min &mdash; Close every design with this</div>
      <div class="fw-detail">1. <b>Bottlenecks:</b> SPOFs, hot partitions, slow queries<br>2. <b>Trade-offs:</b> What you sacrificed (consistency vs availability, cost vs performance)<br>3. <b>Next steps:</b> Monitoring, alerting, gradual rollout<br><br><b>Tip:</b> Proactively identifying weaknesses signals maturity. Never claim your design is perfect.</div>
    </div>
  </div>
</div>

<!-- ESTIMATION -->
<div class="sec" id="s-estimation">
  <div class="sec-title">Estimation Calculator</div>
  <div class="sec-sub">Topic 0.5 &middot; Interactive 7-metric tool &middot; Use for every system you design</div>
  <div class="card" style="margin-bottom:20px">
    <div class="card-label">System Parameters</div>
    <div style="margin-top:16px">
      <div class="calc-row"><div class="calc-lbl">Daily Active Users</div><input class="calc-inp" id="dau" value="300000000"></div>
      <div class="calc-row"><div class="calc-lbl">Writes per user/day</div><input class="calc-inp" id="wpd" value="2"></div>
      <div class="calc-row"><div class="calc-lbl">Reads per user/day</div><input class="calc-inp" id="rpd" value="10"></div>
      <div class="calc-row"><div class="calc-lbl">Avg write size (bytes)</div><input class="calc-inp" id="ws" value="300"></div>
      <div class="calc-row"><div class="calc-lbl">Avg read response (bytes)</div><input class="calc-inp" id="rs" value="1000"></div>
      <div class="calc-row"><div class="calc-lbl">Retention years</div><input class="calc-inp" id="yr" value="5"></div>
      <button class="calc-btn" onclick="calc()">Calculate &rarr;</button>
    </div>
  </div>
  <div id="cres" style="display:none">
    <div class="card-label" style="margin-bottom:12px">Results</div>
    <div class="results-grid" id="rgrid"></div>
    <div id="impl" style="margin-top:20px"></div>
  </div>
  <div class="card" style="margin-top:20px">
    <div class="card-label">Mental Math Shortcuts</div>
    <pre>86,400 sec/day &asymp; <span class="ca">100,000</span>   (always round up)
1M DAU &times; 1 req/day  &asymp; <span class="ca">12 QPS</span>
1B DAU &times; 1 req/day  &asymp; <span class="ca">12,000 QPS</span>
1 KB &times; 1M writes/day = <span class="cg">1 GB/day</span>
1 MB &times; 1M writes/day = <span class="cg">1 TB/day</span>
Peak &asymp; Average &times; <span class="ca">3</span></pre>
  </div>
</div>

<!-- TRADEOFFS -->
<div class="sec" id="s-tradeoffs">
  <div class="sec-title">Trade-off Summary</div>
  <div class="sec-sub">Core decision frameworks &mdash; referenced throughout the entire course</div>
  <div style="margin-bottom:20px">
    <div class="trrow trhead"><div>Concept</div><div>Option A</div><div>Option B</div><div>Decision Rule</div></div>
    <div class="trrow"><div style="font-weight:600">TCP vs UDP</div><div><span class="badge bb">TCP</span><br><small>Reliable, ordered</small></div><div><span class="badge ba">UDP</span><br><small>Fast, unreliable</small></div><div style="font-size:12px">TCP when correctness &gt; speed. UDP when latency &gt; reliability.</div></div>
    <div class="trrow"><div style="font-weight:600">Blocking vs Async I/O</div><div><span class="badge ba">Blocking</span><br><small>Simple code</small></div><div><span class="badge bg">Non-blocking</span><br><small>High throughput</small></div><div style="font-size:12px">Async when handling 100s+ concurrent connections.</div></div>
    <div class="trrow"><div style="font-weight:600">Process vs Thread</div><div><span class="badge bb">Process</span><br><small>Crash isolation</small></div><div><span class="badge bg">Thread</span><br><small>Shared memory</small></div><div style="font-size:12px">Process when stability matters. Thread when performance is critical.</div></div>
    <div class="trrow"><div style="font-weight:600">Index vs No Index</div><div><span class="badge bg">Index</span><br><small>Fast reads O(log n)</small></div><div><span class="badge ba">No Index</span><br><small>Fast writes</small></div><div style="font-size:12px">Index WHERE, JOIN, ORDER BY columns. Don't over-index.</div></div>
    <div class="trrow"><div style="font-weight:600">SQL vs NoSQL</div><div><span class="badge bb">SQL</span><br><small>ACID, joins</small></div><div><span class="badge ba">NoSQL</span><br><small>Scale, flex</small></div><div style="font-size:12px">SQL for finance/accounts. NoSQL for feeds/sessions/IoT.</div></div>
    <div class="trrow"><div style="font-weight:600">Consistency</div><div><span class="badge bb">Strong</span><br><small>Always correct</small></div><div><span class="badge ba">Eventual</span><br><small>Always available</small></div><div style="font-size:12px">Strong for banking/inventory. Eventual for likes/feeds/counters.</div></div>
  </div>
  <div class="tip"><span class="tip-n">&#9733;</span><b>The master rule:</b> "It depends" is always the right start. Follow with "on X and Y &mdash; let me clarify the requirements." This single habit separates strong SD candidates from weak ones.</div>
</div>

<!-- CHECKLIST -->
<div class="sec" id="s-checklist">
  <div class="sec-title">Phase 0 Completion Checklist</div>
  <div class="sec-sub">Track your progress &middot; Click items to mark complete</div>
  <div style="margin-bottom:24px">
    <div style="display:flex;justify-content:space-between;font-family:'DM Mono',monospace;font-size:11px;color:var(--muted);margin-bottom:6px">
      <span>Progress</span><span id="ptxt">0 / 9 complete</span>
    </div>
    <div class="prog-bar"><div class="prog-fill" id="pfill" style="width:0%"></div></div>
  </div>
  <div class="card">
    <ul class="checklist" id="cl">
      <li onclick="chk(this)"><div class="chk"></div><span>Trace URL end-to-end: DNS &rarr; TCP handshake &rarr; HTTP &rarr; Response</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>TCP vs UDP tradeoffs cold &mdash; when to use each without hesitation</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>Explain blocking vs non-blocking I/O with a concurrency comparison + math</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>Memorized latency table: RAM (~100ns) &rarr; SSD (~100&#956;s) &rarr; HDD (~10ms)</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>Explain all 4 ACID properties with a bank transfer example</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>Design a DB schema with justified indexes for a simple system</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>&#9999; Task 0.4: Applied the 5-step SD Framework to Pastebin</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>&#9999; Task 0.5: Estimation sprint &mdash; Instagram, WhatsApp, YouTube tables complete</span></li>
      <li onclick="chk(this)"><div class="chk"></div><span>Can fill the 7-metric estimation table for any system in under 5 minutes</span></li>
    </ul>
  </div>
</div>

<div style="margin-top:40px;display:flex;justify-content:center;gap:16px;flex-wrap:wrap;padding: 24px 0; border-top: 1px solid var(--border-color); font-family:'IBM Plex Mono',monospace; font-size:13px;">
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid var(--border-color);border-radius:4px;color:var(--text-color);text-decoration:none;transition:all 0.2s;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a1-solid/" style="padding:12px 24px;border:1px solid #7c6fff;background:rgba(124,111,255,0.1);color:#7c6fff;border-radius:4px;text-decoration:none;font-weight:600;transition:all 0.2s;">NEXT: LLD A1 — SOLID →</a>
</div>


<script src="/assets/js/sd-phase0.js" defer></script>