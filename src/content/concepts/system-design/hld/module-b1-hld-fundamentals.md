---
title: "Module B1 — HLD Fundamentals | HLD Track"
description: "SYSTEM DESIGN MASTERY COURSE TRACK B · HIGH-LEVEL DESIGN · MODULE B1 · WEEK 11 BEGINS TRACK B High-Level Design · Distributed Systems Foundations HLD Fundamentals CAP Theorem ·…"
domain: system-design
track: system-design-hld
order: 102
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b1-hld-fundamentals/
---

<link rel="stylesheet" href="/assets/css/sd-module-b1.css">

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Crimson+Pro:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<!-- HEADER -->
<header>
  <div class="compass-bar">
    <span>SYSTEM DESIGN MASTERY COURSE</span>
    <span>TRACK B · HIGH-LEVEL DESIGN · MODULE B1 · WEEK 11</span>
    <span>BEGINS TRACK B</span>
  </div>
  <div class="hdr-body">
    <div class="hdr-left">
      <div class="hdr-kicker">High-Level Design · Distributed Systems Foundations</div>
      <h1>HLD<br><em>Fundamentals</em></h1>
      <p class="hdr-desc">CAP Theorem · Consistency Models · Availability Patterns · Load Balancing · Latency Numbers · Back-of-Envelope · The 7-Step Framework</p>
    </div>
    <!-- Compass rose SVG -->
    <div class="compass">
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" fill="none" stroke="#b5440a" stroke-width="1.5" opacity="0.4"/>
        <circle cx="50" cy="50" r="36" fill="none" stroke="#b5440a" stroke-width="0.8" opacity="0.3"/>
        <polygon points="50,4 54,50 50,46 46,50" fill="#b5440a"/>
        <polygon points="50,96 54,50 50,54 46,50" fill="#8a7060"/>
        <polygon points="4,50 50,46 54,50 50,54" fill="#8a7060"/>
        <polygon points="96,50 50,46 54,50 50,54" fill="#8a7060"/>
        <text x="50" y="18" text-anchor="middle" font-family="'Courier Prime',monospace" font-size="7" fill="#b5440a">N</text>
        <text x="50" y="88" text-anchor="middle" font-family="'Courier Prime',monospace" font-size="7" fill="#8a7060">S</text>
        <text x="12"  y="53" text-anchor="middle" font-family="'Courier Prime',monospace" font-size="7" fill="#8a7060">W</text>
        <text x="88"  y="53" text-anchor="middle" font-family="'Courier Prime',monospace" font-size="7" fill="#8a7060">E</text>
        <circle cx="50" cy="50" r="4" fill="#b5440a" opacity="0.6"/>
      </svg>
    </div>
  </div>
  <div class="stats-row">
    <div class="stat-cell"><div class="stat-val">8</div><div class="stat-lbl">Topics</div></div>
    <div class="stat-cell"><div class="stat-val">4</div><div class="stat-lbl">Tasks</div></div>
    <div class="stat-cell"><div class="stat-val">7</div><div class="stat-lbl">Framework Steps</div></div>
    <div class="stat-cell"><div class="stat-val">B1</div><div class="stat-lbl">Module</div></div>
    <div class="stat-cell"><div class="stat-val">12</div><div class="stat-lbl">Checklist Items</div></div>
  </div>
</header>
<nav class="nav">
  <div class="nav-tab active" onclick="show('cap',this)">CAP Theorem</div>
  <div class="nav-tab" onclick="show('consistency',this)">Consistency</div>
  <div class="nav-tab" onclick="show('availability',this)">Availability</div>
  <div class="nav-tab" onclick="show('lb',this)">Load Balancing</div>
  <div class="nav-tab" onclick="show('latency',this)">Latency & Throughput</div>
  <div class="nav-tab" onclick="show('estimation',this)">Estimation</div>
  <div class="nav-tab" onclick="show('framework',this)">Framework</div>
  <div class="nav-tab" onclick="show('tasks',this)">Tasks</div>
  <div class="nav-tab" onclick="show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- ══════════════════════════════════════════ CAP ══════════════════════════════════════════ -->
<div class="view active" id="view-cap">
  <div class="sec-hd">CAP Theorem</div>
  <div class="sec-rule">In a distributed system, you can guarantee at most 2 of 3 properties</div>
  <div class="cap-container">
    <div class="cap-venn">
      <div class="cap-circle cap-c">C — Consistency</div>
      <div class="cap-circle cap-a">A — Availability</div>
      <div class="cap-circle cap-p">P — Partition Tolerance</div>
      <div class="cap-label cap-ca" style="color:var(--c-cap)">CA<br><span style="font-size:8px">Traditional RDBMS<br>(single node)</span></div>
      <div class="cap-label cap-cp" style="color:var(--c-avail)">CP<br><span style="font-size:8px">HBase · ZooKeeper<br>MongoDB (strong)</span></div>
      <div class="cap-label cap-ap" style="color:var(--c-cons)">AP<br><span style="font-size:8px">Cassandra · DynamoDB<br>CouchDB · DNS</span></div>
    </div>
    <div class="cap-legend">
      <div class="cap-row" style="border-left-color:var(--c-cap)">
        <div class="cap-row-title" style="color:var(--c-cap)">The Key Insight</div>
        <div class="cap-row-body">Network partitions <em style="color:var(--ink);font-style:normal;font-weight:600">will happen</em>. P is not optional in a real distributed system. The real choice is between C and A <em style="color:var(--ink);font-style:normal;font-weight:600">when a partition occurs.</em></div>
      </div>
      <div class="cap-row" style="border-left-color:var(--c-avail)">
        <div class="cap-row-title" style="color:var(--c-avail)">CP — Consistent + Partition Tolerant</div>
        <div class="cap-row-body">Rejects requests during a partition to guarantee data consistency. Used when: bank transfers, inventory reservation, ticket booking, distributed locks.</div>
      </div>
      <div class="cap-row" style="border-left-color:var(--c-cons)">
        <div class="cap-row-title" style="color:var(--c-cons)">AP — Available + Partition Tolerant</div>
        <div class="cap-row-body">Accepts reads/writes during partition — may return stale data. Used when: social media likes, user profiles, DNS, shopping carts, analytics.</div>
      </div>
    </div>
  </div>
  <div class="callout rust">
    <em>The interview one-liner:</em> "During a network partition, I can either reject requests to guarantee consistency (CP), or serve potentially stale data to stay available (AP). Since partitions are inevitable, the real design question is: for this use case, which failure is more acceptable?"
  </div>
  <div class="sec-hd" style="margin-top:28px">PACELC — The Extension</div>
  <div class="sec-rule">CAP only covers partitions. PACELC adds the non-partition case.</div>
<pre class="mono"><span class="hl-rust">P → Partition: choose A or C  (same as CAP)</span>
<span class="hl-och">E → Else (no partition): choose Latency or Consistency</span>
 
PACELC(P:A/C ; E:L/C)
 
Cassandra:   <span class="hl-fad">PA/EL</span>  — available during partition; low latency normally
DynamoDB:    <span class="hl-fad">PA/EL</span>  — same profile as Cassandra
HBase:       <span class="hl-fad">PC/EC</span>  — consistent always; accepts higher latency
Zookeeper:   <span class="hl-fad">PC/EC</span>  — built for coordination, strong guarantees
MySQL:       <span class="hl-fad">PC/EC</span>  — ACID, consistent always</pre>
  <div class="sec-hd" style="margin-top:28px">CP vs AP — When to Choose</div>
  <table class="lat-table">
    <thead><tr><th>SCENARIO</th><th>CHOOSE</th><th>REASON</th></tr></thead>
    <tbody>
      <tr><td>Bank account balance check before debit</td><td><span style="color:var(--c-avail);font-family:'Courier Prime',monospace;font-weight:700">CP</span></td><td>Wrong balance → real financial harm</td></tr>
      <tr><td>Facebook likes on viral post</td><td><span style="color:var(--c-cons);font-family:'Courier Prime',monospace;font-weight:700">AP</span></td><td>Approximate count is fine; accuracy not critical</td></tr>
      <tr><td>Hotel room reservation (last room)</td><td><span style="color:var(--c-avail);font-family:'Courier Prime',monospace;font-weight:700">CP</span></td><td>Double-booking is catastrophic</td></tr>
      <tr><td>User profile picture update</td><td><span style="color:var(--c-cons);font-family:'Courier Prime',monospace;font-weight:700">AP</span></td><td>Slightly stale photo is acceptable</td></tr>
      <tr><td>Stock trade order placement</td><td><span style="color:var(--c-avail);font-family:'Courier Prime',monospace;font-weight:700">CP</span></td><td>Price must be accurate; regulatory requirement</td></tr>
      <tr><td>DNS lookups</td><td><span style="color:var(--c-cons);font-family:'Courier Prime',monospace;font-weight:700">AP</span></td><td>Stale DNS record better than no answer</td></tr>
    </tbody>
  </table>
</div>
<!-- ══════════════════════════════════════════ CONSISTENCY ══════════════════════════════════════════ -->
<div class="view" id="view-consistency">
  <div class="sec-hd">Consistency Models</div>
  <div class="sec-rule">From strongest guarantees to weakest — each a deliberate trade-off</div>
  <div class="spectrum">
    <div style="display:flex;justify-content:space-between;font-family:'Courier Prime',monospace;font-size:9px;color:var(--aged);margin-bottom:6px;">
      <span>← STRONGER CONSISTENCY (Higher Latency)</span>
      <span>(Lower Latency, Higher Availability) WEAKER →</span>
    </div>
    <div class="spec-track">
      <div class="spec-labels">
        <span>Linearizable</span>
        <span>Sequential</span>
        <span>Causal</span>
        <span>Read-Your-Writes</span>
        <span>Eventual</span>
      </div>
    </div>
    <div class="spec-cards">
      <div class="spec-card" style="border-top-color:var(--rust)">
        <div class="spec-name" style="color:var(--rust)">Linearizable</div>
        <div class="spec-body">Operations appear atomic in real-time wall-clock order. Strongest guarantee. Every observer sees the same history.</div>
        <div class="spec-eg">etcd, Zookeeper — distributed locks, leader election</div>
      </div>
      <div class="spec-card" style="border-top-color:var(--terra)">
        <div class="spec-name" style="color:var(--terra)">Sequential</div>
        <div class="spec-body">All nodes agree on operation order but not necessarily real-time. Order preserved, clock may lag.</div>
        <div class="spec-eg">Some multi-CPU memory models, academic systems</div>
      </div>
      <div class="spec-card" style="border-top-color:var(--ochre)">
        <div class="spec-name" style="color:var(--ochre)">Causal</div>
        <div class="spec-body">Causally related ops seen in correct order. Concurrent ops may differ across nodes. Reply always after parent post.</div>
        <div class="spec-eg">DynamoDB streams, MongoDB read concern "majority"</div>
      </div>
      <div class="spec-card" style="border-top-color:var(--c-lb)">
        <div class="spec-name" style="color:var(--c-lb)">Read-Your-Writes</div>
        <div class="spec-body">You always see your own writes, even if others don't yet. Route user reads to their write replica, or use sticky sessions.</div>
        <div class="spec-eg">Social networks — you see your own tweet immediately</div>
      </div>
      <div class="spec-card" style="border-top-color:var(--c-avail)">
        <div class="spec-name" style="color:var(--c-avail)">Eventual</div>
        <div class="spec-body">No new updates → all replicas converge. No WHEN guarantee. Reads may be stale. Writes never rejected.</div>
        <div class="spec-eg">Cassandra, DynamoDB, DNS propagation, S3</div>
      </div>
    </div>
  </div>
  <div class="callout och">
    <em>Common interview mistake:</em> "Eventual consistency is bad." It's a deliberate trade-off. Facebook doesn't need strong consistency for Like counts — the 1% accuracy cost buys massive availability and throughput gains.
  </div>
  <div class="sec-hd" style="margin-top:28px">Consistency vs Latency Trade-off</div>
<pre class="mono"><span class="hl-fad">Strong consistency (Paxos/Raft):</span>
  Requires majority quorum before returning → adds 1+ network round trips
  Typical latency: 5–50ms extra per operation
  <span class="hl-grn">✓</span> Correct always  <span class="hl-rust">✗</span> Slower
 
<span class="hl-fad">Eventual consistency (async replication):</span>
  Write returns immediately after local write → low latency
  Replicas catch up asynchronously
  <span class="hl-grn">✓</span> Fast, available  <span class="hl-rust">✗</span> Reads may be stale (replication lag)
 
<span class="hl-fad">Tunable consistency (Cassandra):</span>
  Per-query consistency level: ONE, QUORUM, ALL
  QUORUM write + QUORUM read → strong consistency
  ONE write + ONE read → eventual
  Trade-off per operation based on use case</pre>
</div>
<!-- ══════════════════════════════════════════ AVAILABILITY ══════════════════════════════════════════ -->
<div class="view" id="view-availability">
  <div class="sec-hd">Availability Patterns</div>
  <div class="sec-rule">Measuring and achieving the nines</div>
  <div class="nines-grid">
    <div class="nine-card">
      <div class="nine-pct">99%</div>
      <div class="nine-down">87.6 hrs / year</div>
      <div class="nine-lbl">2 nines — not acceptable for production</div>
    </div>
    <div class="nine-card">
      <div class="nine-pct">99.9%</div>
      <div class="nine-down">8.7 hrs / year</div>
      <div class="nine-lbl">3 nines — typical for internal services</div>
    </div>
    <div class="nine-card" style="border-color:var(--rust)">
      <div class="nine-pct" style="color:var(--ochre)">99.99%</div>
      <div class="nine-down" style="color:var(--rust)">52.6 min / year</div>
      <div class="nine-lbl">4 nines — typical commercial SLA</div>
    </div>
    <div class="nine-card">
      <div class="nine-pct">99.999%</div>
      <div class="nine-down">5.3 min / year</div>
      <div class="nine-lbl">5 nines — telecom / financial grade</div>
    </div>
  </div>
  <div class="callout och">
    <em>Compounding availability:</em> If your system has 3 services in sequence each at 99.9%, the end-to-end availability is 0.999³ = 99.7%. More services in the request path → lower total availability. Prefer parallel over sequential for resilience.
  </div>
  <div class="sec-hd" style="margin-top:24px">Active-Passive (Failover)</div>
<pre class="mono">Normal:    [Client] ──→ [Active Node]      [Passive] (standby, synced)
Failover:  [Client] ──→ [Passive Node]     [Active]  (dead/recovering)
 
Variants:
  Hot standby:  Passive running + synced → failover in seconds
  Warm standby: Passive needs startup → minutes
  Cold standby: Passive needs provisioning → minutes to hours
 
<span class="hl-rust">Challenge: Split-brain</span>
  Network partition → both nodes think they're active primary
  Both accept writes → divergent, irreconcilable state
  Prevention: Quorum (majority must agree) + Fencing tokens</pre>
  <div class="sec-hd" style="margin-top:24px">Active-Active (Load Sharing)</div>
<pre class="mono">Normal: [Client] ──→ [Load Balancer] ──→ Node A (active, serving)
                                     ──→ Node B (active, serving)
                                     ──→ Node C (active, serving)
 
All nodes handle reads AND writes simultaneously.
Conflict resolution required:
  - Last-write-wins (timestamp)
  - CRDTs (Conflict-free Replicated Data Types)
  - Application-level merge logic
 
Used in: Cassandra, DynamoDB, Akamai CDN, most NoSQL at scale</pre>
</div>
<!-- ══════════════════════════════════════════ LB ══════════════════════════════════════════ -->
<div class="view" id="view-lb">
  <div class="sec-hd">Load Balancing</div>
  <div class="sec-rule">Distributing traffic across a fleet · L4 vs L7 · six algorithms</div>
  <table class="lat-table">
    <thead><tr><th>FEATURE</th><th>L4 — Transport Layer</th><th>L7 — Application Layer</th></tr></thead>
    <tbody>
      <tr><td>Works on</td><td>TCP/UDP packets</td><td>HTTP/HTTPS requests</td></tr>
      <tr><td>Routing basis</td><td>IP address + port</td><td>URL path, headers, cookies, body</td></tr>
      <tr><td>Speed</td><td>Very fast (no content inspection)</td><td>Slower (parses full HTTP request)</td></tr>
      <tr><td>SSL termination</td><td>No — passes through encrypted</td><td>Yes — decrypts once at LB</td></tr>
      <tr><td>Smart routing</td><td>No — IP-based only</td><td>Yes — /api → API servers, /images → CDN</td></tr>
      <tr><td>Examples</td><td>AWS NLB, HAProxy (L4 mode)</td><td>AWS ALB, NGINX, Envoy, Caddy</td></tr>
    </tbody>
  </table>
  <div class="sec-hd" style="margin-top:24px">Load Balancing Algorithms</div>
  <div class="lb-grid">
    <div class="lb-card">
      <div class="lb-name">Round Robin</div>
      <div class="lb-body">Requests distributed evenly in rotation: A → B → C → A → B → C. Simple, assumes equal server capacity.</div>
      <div class="lb-use">USE WHEN: homogeneous fleet, short equal requests</div>
    </div>
    <div class="lb-card">
      <div class="lb-name">Weighted Round Robin</div>
      <div class="lb-body">Servers with higher weight get proportionally more requests. Weight 3:2:1 → A gets 3 per cycle, B gets 2, C gets 1.</div>
      <div class="lb-use">USE WHEN: heterogeneous fleet (some servers bigger)</div>
    </div>
    <div class="lb-card">
      <div class="lb-name">Least Connections</div>
      <div class="lb-body">New request → server with fewest active connections. Better than round-robin when request duration varies significantly.</div>
      <div class="lb-use">USE WHEN: long-lived connections, variable processing time</div>
    </div>
    <div class="lb-card">
      <div class="lb-name">Least Response Time</div>
      <div class="lb-body">Routes to server with lowest latency + fewest connections. Requires health-check latency monitoring overhead.</div>
      <div class="lb-use">USE WHEN: latency-sensitive, servers have variable performance</div>
    </div>
    <div class="lb-card">
      <div class="lb-name">IP Hash (Sticky)</div>
      <div class="lb-body">Hash(client IP) mod N → always same server. Guarantees same client always hits same server. Breaks if server count changes.</div>
      <div class="lb-use">USE WHEN: avoiding external session store (prefer Redis instead)</div>
    </div>
    <div class="lb-card">
      <div class="lb-name">Consistent Hashing</div>
      <div class="lb-body">Map servers and requests to same hash ring. Adding/removing a server only remaps K/N keys (where K=keys, N=servers). Minimal disruption.</div>
      <div class="lb-use">USE WHEN: distributed caches, CDN routing, sharded databases</div>
    </div>
  </div>
  <div class="callout rust">
    <em>Interview trap on sticky sessions:</em> IP Hash is a workaround for stateful servers. The correct solution is to make servers stateless by externalising session state to Redis. Then any server can handle any request — no stickiness needed.
  </div>
</div>
<!-- ══════════════════════════════════════════ LATENCY ══════════════════════════════════════════ -->
<div class="view" id="view-latency">
  <div class="sec-hd">Latency & Throughput</div>
  <div class="sec-rule">Numbers every engineer should know by heart</div>
  <table class="lat-table">
    <thead><tr><th>OPERATION</th><th>LATENCY</th><th>RELATIVE SCALE</th><th>NOTE</th></tr></thead>
    <tbody>
      <tr>
        <td>L1 cache reference</td><td>0.5 ns</td>
        <td class="lat-bar-cell"><div class="lat-bar" style="width:1px"></div></td>
        <td>CPU register-speed</td>
      </tr>
      <tr>
        <td>L2 cache reference</td><td>7 ns</td>
        <td><div class="lat-bar" style="width:2px"></div></td>
        <td>14× slower than L1</td>
      </tr>
      <tr>
        <td>RAM access</td><td>100 ns</td>
        <td><div class="lat-bar" style="width:4px"></div></td>
        <td>Baseline for in-memory ops</td>
      </tr>
      <tr>
        <td>SSD random read</td><td>0.1 ms</td>
        <td><div class="lat-bar" style="width:20px"></div></td>
        <td>1000× slower than RAM</td>
      </tr>
      <tr>
        <td>Network within datacenter</td><td>0.5 ms</td>
        <td><div class="lat-bar" style="width:50px"></div></td>
        <td>Same-AZ latency</td>
      </tr>
      <tr>
        <td>HDD random read</td><td>10 ms</td>
        <td><div class="lat-bar" style="width:80px"></div></td>
        <td>Mechanical seek time</td>
      </tr>
      <tr>
        <td>Intra-region (cross-AZ)</td><td>1–5 ms</td>
        <td><div class="lat-bar" style="width:60px"></div></td>
        <td>Same region, different AZ</td>
      </tr>
      <tr>
        <td>Cross-region (US → EU)</td><td>~100 ms</td>
        <td><div class="lat-bar" style="width:160px"></div></td>
        <td>Speed of light across Atlantic</td>
      </tr>
    </tbody>
  </table>
  <div class="sec-hd" style="margin-top:24px">Little's Law</div>
<pre class="mono">L = λ × W
 
L  =  average items in system (queue depth)
λ  =  arrival rate (throughput, requests/sec)
W  =  average time in system (latency, seconds)
 
<span class="hl-rust">Example:</span>
  Service handles 100 req/sec (λ = 100)
  Average latency is 50ms   (W = 0.05s)
  Avg concurrent requests:  L = 100 × 0.05 = <span class="hl-och">5 concurrent requests</span>
<span class="hl-rust">Key insight:</span>
  If latency grows (W↑) and arrival rate stays constant (λ=const),
  queue depth grows (L↑). Eventually queue overflows → system collapse.
  <span class="hl-grn">→ Latency spikes are early warning signs of capacity problems.</span></pre>
  <div class="callout och">
    <em>Latency vs Throughput trade-off:</em> Processing requests in larger batches increases throughput but adds per-request latency (waiting to fill the batch). Streaming one-at-a-time minimises latency but reduces throughput. Choose based on SLA: batch for analytics pipelines, stream for user-facing APIs.
  </div>
</div>
<!-- ══════════════════════════════════════════ ESTIMATION ══════════════════════════════════════════ -->
<div class="view" id="view-estimation">
  <div class="sec-hd">Back-of-Envelope Estimation</div>
  <div class="sec-rule">Show your math · round aggressively · use powers of 10</div>
  <div class="est-box">
    <div class="est-title">The 5-Step Estimation Framework</div>
    <div class="est-step"><div class="est-num">1</div><div class="est-body">Clarify scale: DAU, requests per user per day, retention period</div></div>
    <div class="est-step"><div class="est-num">2</div><div class="est-body">Peak QPS = (DAU × req/day) ÷ 86,400 × 2–3 (peak factor)</div></div>
    <div class="est-step"><div class="est-num">3</div><div class="est-body">Storage = items/day × item_size × retention_days</div></div>
    <div class="est-step"><div class="est-num">4</div><div class="est-body">Bandwidth = peak_QPS × avg_payload_size</div></div>
    <div class="est-step"><div class="est-num">5</div><div class="est-body">Servers = peak_QPS ÷ capacity_per_server (typically 10K–100K rps/server)</div></div>
  </div>
  <div class="est-box">
    <div class="est-title">Worked Example — Twitter Scale</div>
<pre class="mono">Assumptions:
  300M DAU
  Reads: 100 tweets/user/day
  Writes: 2 tweets/user/day
  Avg tweet size: ~1 KB (text + metadata)
 
<span class="hl-rust">Read QPS:</span>    300M × 100 ÷ 86,400 ≈ <span class="hl-och">350,000 reads/sec</span>
             Peak (3×): ~1M reads/sec
 
<span class="hl-rust">Write QPS:</span>   300M × 2 ÷ 86,400 ≈ <span class="hl-och">7,000 writes/sec</span>
             Peak (3×): ~21,000 writes/sec
 
<span class="hl-rust">Storage (5 years):</span>
  300M × 2 tweets/day × 365 × 5 × 1 KB
  = 300M × 3,650 × 1,000 bytes
  ≈ <span class="hl-och">1.1 PB</span> (tweets only, excluding media)
 
<span class="hl-rust">Bandwidth:</span>
  Reads:  1M req/s × 1 KB = <span class="hl-och">1 GB/sec</span>
  Writes: 21K req/s × 1 KB ≈ <span class="hl-och">21 MB/sec</span></pre>
  </div>
  <div class="est-box">
    <div class="est-title">Storage Cheat Sheet</div>
<pre class="mono">Character (ASCII):   1 byte       Integer:    4 bytes     Long:      8 bytes
UUID:               16 bytes      Timestamp:  4 bytes
Image (compressed): 100 KB – 5 MB
HD video 1 min:     ~60 MB (H.264 compressed)
4K video 1 min:     ~375 MB
 
<span class="hl-rust">Units:</span>   1 KB = 10³    1 MB = 10⁶    1 GB = 10⁹    1 TB = 10¹²    1 PB = 10¹⁵
 
<span class="hl-rust">Rule of 86,400:</span>  1 req/sec → 86,400 req/day ≈ 100K req/day
<span class="hl-rust">Rule of 30M:</span>     1 req/sec → ~2.5M req/month ≈ 30M req/year</pre>
  </div>
</div>
<!-- ══════════════════════════════════════════ FRAMEWORK ══════════════════════════════════════════ -->
<div class="view" id="view-framework">
  <div class="sec-hd">The 7-Step HLD Interview Framework</div>
  <div class="sec-rule">Apply this to every system design question · 45 minutes total</div>
  <div class="fw-steps">
    <div class="fw-step">
      <div class="fw-n">01</div>
      <div class="fw-title">Requirements (5 min)</div>
      <div class="fw-body">Functional: core features, use cases, users. Non-functional: scale, latency target, availability SLA, consistency needs, geo distribution. Don't assume — ask.</div>
    </div>
    <div class="fw-step">
      <div class="fw-n">02</div>
      <div class="fw-title">Estimation (5 min)</div>
      <div class="fw-body">DAU, peak QPS, storage/year, bandwidth. Show calculations. Round aggressively. Numbers drive every architecture decision that follows.</div>
    </div>
    <div class="fw-step">
      <div class="fw-n">03</div>
      <div class="fw-title">High-Level Design (10 min)</div>
      <div class="fw-body">Draw the big boxes: clients, API gateway, services, databases, caches, queues. Identify read vs write path. Breadth first — don't go deep yet.</div>
    </div>
    <div class="fw-step">
      <div class="fw-n">04</div>
      <div class="fw-title">Deep Dive (15 min)</div>
      <div class="fw-body">Pick 1–2 most interesting components. Database schema, critical API design, specific algorithm. The part they're actually testing you on.</div>
    </div>
  </div>
  <div class="fw-steps-b">
    <div class="fw-step" style="border:1px solid var(--rust);border-top:none;border-right:none">
      <div class="fw-n">05</div>
      <div class="fw-title">Bottlenecks (5 min)</div>
      <div class="fw-body">Where is the hotspot? What breaks first at 10× scale? What trade-offs did you make and why?</div>
    </div>
    <div class="fw-step" style="border:1px solid var(--rust);border-top:none;border-right:none">
      <div class="fw-n">06</div>
      <div class="fw-title">Failure Scenarios (2 min)</div>
      <div class="fw-body">DB goes down? Cache is cold? DC failover? What is the graceful degradation story?</div>
    </div>
    <div class="fw-step" style="border:1px solid var(--rust);border-top:none;border-right:none">
      <div class="fw-n">07</div>
      <div class="fw-title">Scale Evolution (optional)</div>
      <div class="fw-body">What changes at 10× more load? Sharding strategy? CDN for static content? Read replicas?</div>
    </div>
  </div>
  <div class="sec-hd" style="margin-top:28px">Component Decision Guide</div>
  <table class="lat-table">
    <thead><tr><th>COMPONENT</th><th>USE WHEN</th><th>EXAMPLES</th></tr></thead>
    <tbody>
      <tr><td>CDN</td><td>Static content, globally read-heavy, media files</td><td>Cloudflare, Akamai, AWS CloudFront</td></tr>
      <tr><td>Load Balancer</td><td>Multiple backend instances, traffic distribution, SSL termination</td><td>AWS ALB/NLB, NGINX, HAProxy</td></tr>
      <tr><td>Cache (Redis)</td><td>Hot reads, session storage, rate limiting counters, leaderboards</td><td>Redis, Memcached, DynamoDB DAX</td></tr>
      <tr><td>Message Queue</td><td>Async processing, decouple services, event streaming, retry logic</td><td>Kafka, RabbitMQ, AWS SQS</td></tr>
      <tr><td>SQL Database</td><td>ACID transactions, complex queries, structured data, joins</td><td>PostgreSQL, MySQL, AWS Aurora</td></tr>
      <tr><td>NoSQL Database</td><td>High throughput, flexible schema, horizontal scale, simple access patterns</td><td>DynamoDB, Cassandra, MongoDB</td></tr>
      <tr><td>Object Storage</td><td>Large files, images, videos, backups, low cost</td><td>AWS S3, GCS, Azure Blob</td></tr>
      <tr><td>Search Engine</td><td>Full-text search, faceted filtering, fuzzy matching</td><td>Elasticsearch, OpenSearch, Algolia</td></tr>
    </tbody>
  </table>
  <div class="sec-hd" style="margin-top:24px">Interview Tips — Common Mistakes</div>
  <table class="tips-table">
    <thead><tr><th>MISTAKE</th><th>CORRECTION</th></tr></thead>
    <tbody>
      <tr><td>"CAP says choose 2 of 3"</td><td>CAP says choose C or A when a partition occurs. P is not optional — always required.</td></tr>
      <tr><td>"Eventual consistency is always bad"</td><td>Deliberate trade-off. Facebook likes don't need strong consistency. Know when it's acceptable.</td></tr>
      <tr><td>Jumping to DB choice first</td><td>Start with requirements → scale → access patterns → then DB choice follows naturally.</td></tr>
      <tr><td>Not estimating scale</td><td>Every HLD starts with numbers. Scale determines architecture. Always estimate.</td></tr>
      <tr><td>"Just add a cache"</td><td>Cache invalidation is one of the hardest problems. When do you invalidate? On write? TTL? Both?</td></tr>
      <tr><td>Ignoring failure scenarios</td><td>Interviewers want to see: what happens when X fails? What's the recovery path?</td></tr>
    </tbody>
  </table>
</div>
<!-- ══════════════════════════════════════════ TASKS ══════════════════════════════════════════ -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-label">CAP Theorem — 8 Scenario Analysis</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>For each scenario: identify CP or AP, justify your choice, and name the trade-off you're accepting.</p>
        <ol>
          <li>Online banking — check account balance before debit</li>
          <li>Facebook Like counter on a viral post</li>
          <li>Uber driver location updates (moves every 4 seconds)</li>
          <li>Hotel room reservation (last room available)</li>
          <li>Amazon product reviews display</li>
          <li>Stock trading platform — order placement</li>
          <li>WhatsApp message delivery status (sent/delivered/read)</li>
          <li>E-commerce shopping cart (items added by user)</li>
        </ol>
        <p style="margin-top:10px">For each: state the <strong>exact failure mode</strong> if you choose wrong (e.g., "if I choose AP for banking, a user could overdraft").</p>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-label">Back-of-Envelope — WhatsApp + YouTube</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p><strong>WhatsApp:</strong> 2B users, 100M active daily, 100 messages/user/day, avg 100 bytes/message.<br>Calculate: peak QPS, storage/year, bandwidth (in + out).</p>
        <p style="margin-top:10px"><strong>YouTube:</strong> 2B users, 500 hours of video uploaded per minute, 1B views/day, avg view 10 min at 1 Mbps.<br>Calculate: upload storage/year, CDN bandwidth for views, approximate CDN cost (assume $0.01/GB).</p>
        <p style="margin-top:10px">For each: show all steps. Identify the biggest bottleneck revealed by your numbers.</p>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-label">Consistency Model Selection — 6 Scenarios</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Choose the appropriate consistency model and justify:</p>
        <ol>
          <li>Bank ledger — transfer between two accounts</li>
          <li>User profile picture update</li>
          <li>Social media comments — replies must appear after parent</li>
          <li>Shopping cart — items added/removed</li>
          <li>Distributed lock (exactly one service holds the lock)</li>
          <li>Netflix "continue watching" progress position</li>
        </ol>
        <p style="margin-top:10px">For each: name the exact model (Linearizable / Sequential / Causal / Read-Your-Writes / Eventual), the implementation mechanism, and the failure mode if you under-constrain.</p>
      </div>
    </div>
    <div class="task-card" style="border-top:3px solid var(--rust)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--rust)">★</div><div class="t-label">HLD Framework — URL Shortener (Full Walkthrough)</div><div class="t-meta">~2 hrs · full design</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Apply all 7 steps to design TinyURL. No code — framework output only.</p>
        <ul>
          <li><strong>Scale:</strong> 300M URLs stored, 100:1 read:write ratio, 5-year retention</li>
          <li><strong>Latency target:</strong> redirect in &lt;10ms (p99)</li>
          <li><strong>Availability:</strong> 99.99%</li>
        </ul>
        <p style="margin-top:10px">Required outputs:</p>
        <ol>
          <li>Peak QPS (read + write)</li>
          <li>Storage for 5 years</li>
          <li>High-level diagram (boxes + arrows, read path + write path)</li>
          <li>DB choice + justification (CAP + access pattern reasoning)</li>
          <li>Key design decision: how do you generate unique 7-char short codes?</li>
          <li>Biggest bottleneck + how to address it</li>
          <li>Failure scenario: what if the DB is unreachable during a redirect?</li>
        </ol>
      </div>
    </div>
  </div>
</div>
<!-- ══════════════════════════════════════════ CHECKLIST ══════════════════════════════════════════ -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 12 completed</span><span style="font-family:'Courier Prime',monospace">MODULE B1 · HLD FUNDAMENTALS</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can explain CAP theorem without buzzwords — the partition choice framing</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know PACELC extension — how it covers non-partition latency/consistency</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Distinguish: Linearizable vs Causal vs Eventual — when each is appropriate</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can calculate end-to-end availability from N services in sequence</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know Active-Passive vs Active-Active tradeoffs; split-brain prevention</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know all 6 load balancing algorithms + when to use each</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">L4 vs L7 load balancers — routing basis, SSL termination, smart routing</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Memorized the latency numbers table (RAM vs SSD vs HDD vs network)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can apply Little's Law to analyse queue depth from QPS + latency</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can do back-of-envelope for any system in &lt;5 minutes</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know the 7-step HLD framework + time allocation for 45-min interview</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ All 4 tasks completed (CAP, estimation, consistency, URL shortener)</div></div>
  </div>
  <div style="margin-top:32px;background:var(--cream);border:1px solid var(--rust);padding:24px;">
    <div style="font-family:'Courier Prime',monospace;font-size:9px;letter-spacing:3px;color:var(--aged);margin-bottom:10px;">NEXT MODULE</div>
    <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:900;color:var(--ink);margin-bottom:8px;">B2 — Databases at Scale</div>
    <div style="font-family:'Crimson Pro',serif;font-size:14px;color:var(--faded);line-height:1.7;font-style:italic;">
      Indexing strategies · SQL vs NoSQL trade-offs · Sharding (horizontal partitioning) ·
      Replication (primary-replica, multi-primary) · ACID vs BASE ·
      Read replicas · Connection pooling · Database selection guide
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
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
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
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
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
<div class="b1-bottom-nav">
  <a href="/learning/system-design/lld/module-a6-case-studies/" class="b1-nav-footer-btn">← A6: LLD Case Studies</a>
  <a href="/learning/system-design/hld/module-b1-notes/" class="b1-nav-footer-btn">📄 Full Notes</a>
  <a href="/learning/system-design/system-design-roadmap/" class="b1-nav-footer-btn">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b2-databases-at-scale/" class="b1-nav-footer-btn">B2: Databases at Scale →</a>
</div>


<script src="/assets/js/sd-module-b1.js" defer></script>