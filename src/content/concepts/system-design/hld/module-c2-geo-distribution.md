---
title: "Module C2: Geo-Distribution & Multi-Region Architecture"
description: "SYSTEM DESIGN MASTERY · TRACK C · MODULE C2 · WEEK 26 GEO-DISTRIBUTION · ACTIVE-ACTIVE · CRDTS · GDPR · RPO/RTO Advanced Distributed Systems · Multi-Region · Data Residency…"
domain: system-design
track: system-design-hld
order: 204
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-c2-geo-distribution/
---

<link rel="stylesheet" href="/assets/css/sd-module-c2.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;600&family=DM+Serif+Display&display=swap" rel="stylesheet">
<header>
  <div class="hdr-bar"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK C · MODULE C2 · WEEK 26</span>
    <span>GEO-DISTRIBUTION · ACTIVE-ACTIVE · CRDTS · GDPR · RPO/RTO</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">Advanced Distributed Systems · Multi-Region · Data Residency</div>
      <h1>Geo&#8209;<span class="acc">Distribution</span><br>& Multi&#8209;Region<br>Architecture</h1>
      <div class="hdr-sub">ACTIVE-PASSIVE · ACTIVE-ACTIVE · CRDTs<br>DYNAMODB GLOBAL · COCKROACHDB · GDPR · RPO/RTO</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">~85ms</div><div class="hs-l">US ↔ EU RTT</div></div>
      <div class="hs"><div class="hs-v">7</div><div class="hs-l">CRDT TYPES</div></div>
      <div class="hs"><div class="hs-v">RPO=0</div><div class="hs-l">SYNC REPLICATION</div></div>
      <div class="hs"><div class="hs-v">C2</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--tea)">Speed of Light</div>
    <div class="tg" style="color:var(--grn)">Active-Passive</div>
    <div class="tg" style="color:var(--yel)">Active-Active</div>
    <div class="tg" style="color:var(--bri)">CRDTs</div>
    <div class="tg" style="color:var(--pur)">GDPR</div>
    <div class="tg" style="color:var(--ora)">DynamoDB Global</div>
    <div class="tg" style="color:var(--tea)">CockroachDB</div>
    <div class="tg" style="color:var(--grn)">RPO / RTO</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="show('why',this)">Why Multi-Region</div>
  <div class="nt" onclick="show('latency',this)">Speed of Light</div>
  <div class="nt" onclick="show('patterns',this)">Active-Passive vs Active-Active</div>
  <div class="nt" onclick="show('crdts',this)">CRDTs</div>
  <div class="nt" onclick="show('dynamo',this)">DynamoDB Global</div>
  <div class="nt" onclick="show('cockroach',this)">CockroachDB Multi-Region</div>
  <div class="nt" onclick="show('gdpr',this)">GDPR & Data Residency</div>
  <div class="nt" onclick="show('rpo',this)">RPO / RTO</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- WHY -->
<div class="view active" id="view-why">
  <div class="sh">Why Go Multi-Region?</div>
  <div class="sr">Three distinct motivations — each requires a different solution</div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--red);padding:14px">
      <div style="font-family:'Playfair Display',serif;font-size:17px;color:var(--white);margin-bottom:6px">Availability</div>
      <div style="font-family:'Space Mono',monospace;font-size:8px;color:var(--red);letter-spacing:1px;margin-bottom:8px">SURVIVE REGION OUTAGE</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">AWS us-east-1 has gone down multiple times (2017, 2021, 2023). A single-region system goes down with it.</div>
      <div style="font-family:'Space Mono',monospace;font-size:9px;color:var(--muted)">Solution:<br>Active-passive failover<br>Active-active with replication</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--tea);padding:14px">
      <div style="font-family:'Playfair Display',serif;font-size:17px;color:var(--white);margin-bottom:6px">Latency</div>
      <div style="font-family:'Space Mono',monospace;font-size:8px;color:var(--tea);letter-spacing:1px;margin-bottom:8px">SERVE NEARBY USERS</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">Tokyo user hitting us-east-1: ~140ms. Tokyo user hitting ap-northeast-1: ~5ms. For writes: 28× difference.</div>
      <div style="font-family:'Space Mono',monospace;font-size:9px;color:var(--muted)">Solution:<br>Read replicas in each region<br>Regional active-active writes</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--pur);padding:14px">
      <div style="font-family:'Playfair Display',serif;font-size:17px;color:var(--white);margin-bottom:6px">Compliance</div>
      <div style="font-family:'Space Mono',monospace;font-size:8px;color:var(--pur);letter-spacing:1px;margin-bottom:8px">DATA RESIDENCY LAWS</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">GDPR (EU), India PDPB, China PIPL all require personal data to remain within borders. Violating = large fines.</div>
      <div style="font-family:'Space Mono',monospace;font-size:9px;color:var(--muted)">Solution:<br>Regional data partitioning<br>Geo-routing + KMS per region</div>
    </div>
  </div>
  <div class="al tea"><em>Interview clarifying question:</em> "Before I design the multi-region architecture — which of these are we solving? Availability requires hot standby and automatic failover. Latency requires regional replicas or active-active. Compliance requires strict data partitioning and geo-routing. They have very different solutions and cost profiles."</div>
</div>
<!-- LATENCY -->
<div class="view" id="view-latency">
  <div class="sh">Speed of Light</div>
  <div class="sr">The unavoidable physical constraint — these numbers drive every multi-region decision</div>
  <div class="rtt-map">
    <div class="rtt-label">// REAL-WORLD ROUND-TRIP TIMES (approximate)</div>
    <div class="rtt-grid">
      <div class="rtt-cell"><div class="rtt-from">Within AZ</div><div class="rtt-to">~0.5ms</div><div class="rtt-val" style="color:var(--grn)">baseline</div></div>
      <div class="rtt-cell"><div class="rtt-from">Cross-AZ</div><div class="rtt-to">~1–2ms</div><div class="rtt-val" style="color:var(--grn)">fast</div></div>
      <div class="rtt-cell"><div class="rtt-from">US-East ↔ US-West</div><div class="rtt-to">~70ms</div><div class="rtt-val" style="color:var(--yel)">noticeable</div></div>
      <div class="rtt-cell"><div class="rtt-from">US-East ↔ EU-West</div><div class="rtt-to">~85ms</div><div class="rtt-val" style="color:var(--yel)">slow</div></div>
      <div class="rtt-cell"><div class="rtt-from">US-East ↔ APAC</div><div class="rtt-to">~140ms</div><div class="rtt-val" style="color:var(--red)">very slow</div></div>
      <div class="rtt-cell"><div class="rtt-from">EU-West ↔ APAC</div><div class="rtt-to">~130ms</div><div class="rtt-val" style="color:var(--red)">very slow</div></div>
      <div class="rtt-cell"><div class="rtt-from">EU-West ↔ EU-Central</div><div class="rtt-to">~20ms</div><div class="rtt-val" style="color:var(--grn)">ok</div></div>
      <div class="rtt-cell"><div class="rtt-from">Within APAC</div><div class="rtt-to">~50–80ms</div><div class="rtt-val" style="color:var(--yel)">varies</div></div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Latency math: why synchronous global consensus is impractical<span class="cb-l">CALCULATION</span></div>
<pre class="c"><span class="cm">// Raft cluster: US-East (leader), EU-West, AP-Southeast</span>
<span class="cm">// Quorum = 2 of 3. Client writes from US-East.</span>
 
Write latency = time until quorum ACK
  US-East → EU-West round trip:  <span class="te">~85ms</span>
  US-East → AP-Southeast RT:     <span class="te">~140ms</span>
 
Quorum write latency = min(EU-West RTT, AP-Southeast RTT) = <span class="er">~85ms</span>
<span class="cm">// must wait for 1 of 2 remote nodes to ACK</span>
<span class="cm">// This means every write to your database takes 85ms minimum.</span>
<span class="cm">// A 10ms SLA is IMPOSSIBLE with synchronous global Raft.</span>
<span class="cm">// Solution: non-voting replicas (CockroachDB style)</span>
<span class="cm">// US-East: 2 voting replicas (quorum = 2, all local → ~1ms write latency)</span>
<span class="cm">// EU-West: 1 non-voting replica (async replication, ~1s lag)</span>
<span class="cm">// AP-Southeast: 1 non-voting replica (async replication, ~1s lag)</span>
<span class="cm">// Write latency: ~1ms (local quorum) ✓</span>
<span class="cm">// EU/APAC reads: served locally (slightly stale) ✓</span></pre>
  </div>
</div>
<!-- PATTERNS -->
<div class="view" id="view-patterns">
  <div class="sh">Active-Passive vs Active-Active</div>
  <div class="sr">The fundamental choice — consistency vs availability under partition</div>
  <div class="ap-grid">
    <div class="ap-col" style="background:rgba(32,208,128,.02)">
      <div class="ap-name">Active-Passive</div>
      <div class="ap-sub">ONE PRIMARY · N STANDBYS</div>
      <div class="ap-body">Primary serves all reads and writes. Standby(s) replicate from primary but serve nothing normally. On primary failure: standby is promoted.</div>
      <div class="ap-body"><strong style="color:var(--white)">Sync replication:</strong> primary waits for standby ACK before committing. RPO=0, but adds cross-region latency to every write.</div>
      <div class="ap-body"><strong style="color:var(--white)">Async replication:</strong> primary commits immediately, replication in background. RPO=seconds, no write latency penalty. Standard choice.</div>
      <div class="ap-pros">✓ Simple to reason about<br>✓ No conflict resolution needed<br>✓ Strong consistency always</div>
      <div class="ap-cons">✗ All writes go to one region<br>✗ Remote users pay write latency<br>✗ Failover gap: 30s–minutes<br>✗ Risk: split-brain on failover</div>
    </div>
    <div class="ap-col" style="background:rgba(0,184,200,.02)">
      <div class="ap-name">Active-Active</div>
      <div class="ap-sub">ALL REGIONS READ + WRITE</div>
      <div class="ap-body">Multiple regions all serve reads AND writes. No primary. All regions are peers. Writes in different regions must converge.</div>
      <div class="ap-body"><strong style="color:var(--white)">Conflict resolution required:</strong> Last-Write-Wins (LWW), vector clocks, CRDTs, or Operational Transform. Each has different trade-offs.</div>
      <div class="ap-body"><strong style="color:var(--white)">Eventually consistent:</strong> after a write in EU, the US region may be ~1s behind. Briefly inconsistent across regions.</div>
      <div class="ap-pros">✓ Low write latency everywhere<br>✓ Survives full region loss<br>✓ No bottleneck primary region</div>
      <div class="ap-cons">✗ Conflict resolution complexity<br>✗ Eventually consistent<br>✗ Some conflicts = silent data loss (LWW)<br>✗ Harder to debug</div>
    </div>
  </div>
  <table class="reg-table" style="margin-top:14px">
    <thead><tr><th>CONFLICT STRATEGY</th><th>HOW IT WORKS</th><th>DATA LOSS?</th><th>BEST FOR</th></tr></thead>
    <tbody>
      <tr><td>Last-Write-Wins</td><td>Highest timestamp wins on conflict</td><td>Yes — concurrent write silently lost</td><td>Sessions, caches, preferences</td></tr>
      <tr><td>Vector Clocks</td><td>Track causality; surface conflicts to app</td><td>No — app resolves explicitly</td><td>Shopping carts (Dynamo original)</td></tr>
      <tr><td>CRDTs</td><td>Mathematically conflict-free merge</td><td>Never — by design</td><td>Counters, sets, collaborative editing</td></tr>
      <tr><td>Operational Transform</td><td>Transform ops against concurrent ops</td><td>Never — but complex</td><td>Real-time collaborative text (Google Docs)</td></tr>
    </tbody>
  </table>
</div>
<!-- CRDTS -->
<div class="view" id="view-crdts">
  <div class="sh">CRDTs — Conflict-Free Replicated Data Types</div>
  <div class="sr">Mathematical guarantee: any two replicas merged in any order → same result</div>
  <div class="al tea"><em>The three properties:</em> merge must be <strong>Commutative</strong> (order doesn't matter), <strong>Associative</strong> (grouping doesn't matter), <strong>Idempotent</strong> (merging twice = merging once). Any data structure satisfying these three is a CRDT — concurrent updates across replicas always converge.</div>
  <div class="crdt-grid">
    <div class="cc" style="border-top-color:var(--grn)">
      <div class="cc-name">G-Counter</div>
      <div class="cc-type">GROW-ONLY COUNTER</div>
      <div class="cc-body">Vector of counts, one slot per node. Node i only increments slot i. Merge = max of each slot. Value = sum all slots.</div>
      <div class="cc-merge" style="color:var(--grn)">State: [3, 5, 2]<br>Merge: max per slot<br>Value: sum = 10</div>
      <div class="cc-use">view counts, like counts, event totals</div>
    </div>
    <div class="cc" style="border-top-color:var(--tea)">
      <div class="cc-name">PN-Counter</div>
      <div class="cc-type">INCREMENT + DECREMENT</div>
      <div class="cc-body">Two G-Counters: P (increments) and N (decrements). Value = sum(P) - sum(N). Allows decrement while remaining CRDT.</div>
      <div class="cc-merge" style="color:var(--tea)">P: [3,5,2] N: [1,2,0]<br>Value = 10 - 3 = 7</div>
      <div class="cc-use">shopping cart quantities, inventory approximation</div>
    </div>
    <div class="cc" style="border-top-color:var(--yel)">
      <div class="cc-name">G-Set</div>
      <div class="cc-type">GROW-ONLY SET</div>
      <div class="cc-body">Elements can only be added, never removed. Merge = union of both sets. Trivially conflict-free.</div>
      <div class="cc-merge" style="color:var(--yel)">A: {x,y} B: {y,z}<br>Merge: {x,y,z}</div>
      <div class="cc-use">tag sets, immutable membership lists</div>
    </div>
    <div class="cc" style="border-top-color:var(--ora)">
      <div class="cc-name">2P-Set</div>
      <div class="cc-type">ADD + PERMANENT REMOVE</div>
      <div class="cc-body">Two G-Sets: Add-set A and Remove-set R. Element present if: in A AND NOT in R. Once removed, cannot re-add.</div>
      <div class="cc-merge" style="color:var(--ora)">Present = A \ R<br>Remove is permanent</div>
      <div class="cc-use">when re-add not needed: banned users, archived items</div>
    </div>
    <div class="cc" style="border-top-color:var(--bri)">
      <div class="cc-name">OR-Set</div>
      <div class="cc-type">OBSERVED-REMOVE SET</div>
      <div class="cc-body">Each add tagged with unique ID. Remove only removes elements with that specific tag. Allows correct add-remove-add cycles.</div>
      <div class="cc-merge" style="color:var(--bri)">add(x, id1) → remove(x, id1)<br>add(x, id2) → x still present</div>
      <div class="cc-use">collaborative editing, presence systems</div>
    </div>
    <div class="cc" style="border-top-color:var(--pur)">
      <div class="cc-name">Sequence CRDT</div>
      <div class="cc-type">RGA / LSEQ (TEXT EDITING)</div>
      <div class="cc-body">Positions in sequence assigned unique IDs. Insert/delete at ID works regardless of concurrent operations on same text. Used in collaborative editors.</div>
      <div class="cc-merge" style="color:var(--pur)">Insert at pos-ID<br>Concurrent inserts merge correctly</div>
      <div class="cc-use">Apple Notes, Figma, Notion, Google Docs (OT variant)</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">G-Counter CRDT — concrete implementation<span class="cb-l">PYTHON</span></div>
<pre class="c"><span class="kw">class</span> <span class="fn">GCounter</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, node_id, num_nodes):
        self.node_id = node_id
        self.counts = [<span class="te">0</span>] * num_nodes   <span class="cm"># slot per node</span>
    <span class="kw">def</span> <span class="fn">increment</span>(self):
        self.counts[self.node_id] += <span class="te">1</span>  <span class="cm"># only increment OWN slot</span>
    <span class="kw">def</span> <span class="fn">value</span>(self):
        <span class="kw">return</span> <span class="fn">sum</span>(self.counts)
 
    <span class="kw">def</span> <span class="fn">merge</span>(self, other):             <span class="cm"># merge another replica</span>
        self.counts = [<span class="fn">max</span>(a, b)
            <span class="kw">for</span> a, b <span class="kw">in</span> <span class="fn">zip</span>(self.counts, other.counts)]
 
<span class="cm"># Simulation: 3 nodes</span>
A = <span class="fn">GCounter</span>(<span class="te">0</span>, <span class="te">3</span>); A.<span class="fn">increment</span>(); A.<span class="fn">increment</span>(); A.<span class="fn">increment</span>()  <span class="cm"># [3,0,0]</span>
B = <span class="fn">GCounter</span>(<span class="te">1</span>, <span class="te">3</span>); B.<span class="fn">increment</span>(); B.<span class="fn">increment</span>()                 <span class="cm"># [0,2,0]</span>
C = <span class="fn">GCounter</span>(<span class="te">2</span>, <span class="te">3</span>); C.<span class="fn">increment</span>()                                <span class="cm"># [0,0,1]</span>
 
A.<span class="fn">merge</span>(B); A.<span class="fn">merge</span>(C)  <span class="cm"># [3,2,1] → value = 6</span>
B.<span class="fn">merge</span>(A); B.<span class="fn">merge</span>(C)  <span class="cm"># [3,2,1] → value = 6</span>
<span class="cm"># All replicas converge to 6 regardless of merge order ✓</span></pre>
  </div>
</div>
<!-- DYNAMO -->
<div class="view" id="view-dynamo">
  <div class="sh">DynamoDB Global Tables</div>
  <div class="sr">AWS managed active-active — LWW conflict resolution, ~1s replication lag</div>
  <div class="cb"><div class="cb-top">DynamoDB Global Tables — what it does and doesn't handle<span class="cb-l">AWS</span></div>
<pre class="c"><span class="cm">// Architecture: table replicated across N AWS regions</span>
<span class="cm">// Each region: accepts reads AND writes independently</span>
<span class="cm">// Replication: asynchronous, bidirectional, ~1s lag</span>
<span class="cm">// Conflict resolution: LAST-WRITE-WINS (timestamp-based)</span>
<span class="cm">// GOOD USES (LWW acceptable):</span>
<span class="ok">✓</span> User sessions: {user_id → session_token, last_seen}
<span class="ok">✓</span> User preferences: {user_id → theme, language, notifications}
<span class="ok">✓</span> Shopping cart: {user_id → cart_items} (last write wins per user)
<span class="ok">✓</span> Configuration flags: {feature_flag → enabled/disabled}
 
<span class="cm">// BAD USES (LWW causes data loss):</span>
<span class="er">✗</span> Financial balances: concurrent increments → one lost
  User in US adds $100, user in EU adds $50 simultaneously
  One write wins → balance shows +$100 OR +$50, not +$150
<span class="er">✗</span> Inventory: concurrent decrements → overselling
<span class="er">✗</span> Leaderboard rankings: concurrent score updates
 
<span class="cm">// For counters: use DynamoDB Streams + Lambda to consolidate</span>
<span class="cm">// Or: use a CRDT service (PN-Counter semantics)</span>
<span class="cm">// Or: route all writes for a given key to its "home" region</span>
<span class="cm">// Cost: each additional replica region ≈ 2× storage + throughput costs</span>
<span class="cm">// Replication lag: typically ~1s, can spike to ~5s under high load</span></pre>
  </div>
</div>
<!-- COCKROACHDB -->
<div class="view" id="view-cockroach">
  <div class="sh">CockroachDB Multi-Region</div>
  <div class="sr">Designed for multi-region from the ground up — regional row placement, non-voting replicas</div>
  <div class="cb"><div class="cb-top">Table locality modes — the key CockroachDB multi-region concept<span class="cb-l">COCKROACHDB SQL</span></div>
<pre class="c"><span class="cm">-- Set survival goal: lose an entire region without data loss</span>
ALTER DATABASE mydb SURVIVE REGION FAILURE;
 
<span class="cm">-- REGIONAL BY ROW: each row pinned to its home region</span>
<span class="cm">-- EU user's rows stored in EU region → EU reads/writes at 5ms latency</span>
ALTER TABLE users SET LOCALITY REGIONAL BY ROW AS region;
 
<span class="cm">-- User in EU: crdb_region='eu-west-1' → row stored in EU → fast local access</span>
INSERT INTO users (id, name, crdb_region) VALUES (1, 'Alice', 'eu-west-1');
 
<span class="cm">-- REGIONAL TABLE: entire table anchored to one region</span>
<span class="cm">-- Good for: tables only accessed from one region</span>
ALTER TABLE eu_compliance_log SET LOCALITY REGIONAL IN 'eu-west-1';
 
<span class="cm">-- GLOBAL: replicated everywhere, optimized for reads everywhere</span>
<span class="cm">-- Writes need global consensus (slower), reads are local (fast)</span>
<span class="cm">-- Good for: product catalog, reference data, configuration</span>
ALTER TABLE product_catalog SET LOCALITY GLOBAL;
 
<span class="cm">-- Follower reads: slightly stale (~4.8s) but instant from any region</span>
<span class="cm">-- Good for: analytics, dashboards, non-critical reads</span>
SELECT * FROM orders AS OF SYSTEM TIME follower_read_timestamp()
WHERE user_id = 123;</pre>
  </div>
  <div class="al tea"><em>Non-voting replicas:</em> Standard Raft requires write quorum. If 2 voting replicas are in US-East and 1 is in EU-West, every write must wait for the EU-West ACK (~85ms). Non-voting replicas participate in reads but NOT in write quorum — so US-East can commit with local quorum (~1ms) while EU-West asynchronously catches up for local reads.</div>
</div>
<!-- GDPR -->
<div class="view" id="view-gdpr">
  <div class="sh">GDPR & Data Residency</div>
  <div class="sr">EU personal data must stay within EU — five concrete architecture implications</div>
  <div class="gdpr-list">
    <div class="gl">
      <div class="gl-num">1</div>
      <div class="gl-body">
        <div class="gl-title">DATA CLASSIFICATION</div>
        Identify what is "personal data" under GDPR before designing storage. Name, email, IP address, location, device IDs, behavioral data, and any data that can identify a person.
        <div class="gl-code">Personal: name, email, ip_address, location, user_id<br>Non-personal: aggregated counts, anonymized analytics</div>
      </div>
    </div>
    <div class="gl">
      <div class="gl-num">2</div>
      <div class="gl-body">
        <div class="gl-title">REGIONAL PARTITIONING + GEO-ROUTING</div>
        EU users' personal data must be stored only in EU region. DNS geolocation routing (Route 53) sends EU requests to EU region. JWT contains region claim — services route accordingly.
        <div class="gl-code">Route53 geolocation: *.api.com → eu-west-1 (for EU IPs)<br>JWT: {"user_id": 123, "region": "eu-west-1"}<br>Service: read/write user data only from claimed region</div>
      </div>
    </div>
    <div class="gl">
      <div class="gl-num">3</div>
      <div class="gl-body">
        <div class="gl-title">NO CROSS-REGION REPLICATION OF PERSONAL DATA</div>
        EU personal data must NOT be replicated to the US region — not even for backups. Use separate S3 buckets, separate KMS keys, and separate DB clusters per region.
        <div class="gl-code">EU cluster: eu-west-1 only, KMS key: eu-west-1<br>US cluster: us-east-1 only, KMS key: us-east-1<br>Backups: encrypted with regional KMS → stays in region</div>
      </div>
    </div>
    <div class="gl">
      <div class="gl-num">4</div>
      <div class="gl-body">
        <div class="gl-title">RIGHT TO ERASURE — CRYPTOGRAPHIC DELETION</div>
        User requests deletion. Must erase from ALL replicas, caches, CDN, and backups. Cryptographic erasure: encrypt all user data with a per-user key stored in KMS. Deletion = delete the KMS key. All copies become unreadable without re-encryption.
        <div class="gl-code">Store: encrypt(user_data, kms_key_id=user_123)<br>Delete: KMS.deleteKey(user_123)<br>Result: all stored blobs are now unreadable garbage</div>
      </div>
    </div>
    <div class="gl">
      <div class="gl-num">5</div>
      <div class="gl-body">
        <div class="gl-title">THIRD-PARTY SERVICES (LOGS, MONITORING)</div>
        Datadog, Splunk, and other log aggregators that receive EU personal data must have Data Processing Agreements (DPAs) and EU data residency configured. Never log raw EU personal data — hash or pseudonymize before sending to third parties.
        <div class="gl-code">Bad:  log("user login: email=alice@eu.com ip=1.2.3.4")<br>Good: log("user login: user_id=hash(alice) region=eu")</div>
      </div>
    </div>
  </div>
</div>
<!-- RPO/RTO -->
<div class="view" id="view-rpo">
  <div class="sh">RPO & RTO Design</div>
  <div class="sr">Define requirements first — then derive replication strategy</div>
  <div class="rpo-rto">
    <div class="rr-label">// RPO — RECOVERY POINT OBJECTIVE (how much data loss is acceptable?)</div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--grn)">RPO = 0</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:100%;background:var(--grn)"></div></div>
      <div class="rr-val" style="color:var(--grn)">Sync replication</div>
    </div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--yel)">RPO = seconds</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:40%;background:var(--yel)"></div></div>
      <div class="rr-val" style="color:var(--yel)">Async replication</div>
    </div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--red)">RPO = minutes</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:15%;background:var(--red)"></div></div>
      <div class="rr-val" style="color:var(--red)">Periodic backups</div>
    </div>
  </div>
  <div class="rpo-rto" style="margin-top:8px">
    <div class="rr-label">// RTO — RECOVERY TIME OBJECTIVE (how fast must the system recover?)</div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--grn)">RTO &lt; 30s</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:100%;background:var(--grn)"></div></div>
      <div class="rr-val" style="color:var(--grn)">Hot standby + auto failover</div>
    </div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--yel)">RTO = minutes</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:50%;background:var(--yel)"></div></div>
      <div class="rr-val" style="color:var(--yel)">Warm standby + semi-auto</div>
    </div>
    <div class="rr-row">
      <div class="rr-name" style="color:var(--red)">RTO = hours</div>
      <div class="rr-bar-wrap"><div class="rr-bar" style="width:20%;background:var(--red)"></div></div>
      <div class="rr-val" style="color:var(--red)">Cold backup + manual</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Interview formula: SLA → RTO/RPO → replication strategy<span class="cb-l">DECISION LOGIC</span></div>
<pre class="c"><span class="cm">// Given: 99.99% availability SLA (52 min/year downtime budget)</span>
<span class="cm">// Incident: detect=15min, page team=5min, fix=30min → 50 min per incident</span>
<span class="cm">// → Budget allows ZERO incidents that go over 52 min/year</span>
<span class="cm">// → Need automatic failover with RTO < 30s</span>
<span class="cm">// Payment service (financial data):</span>
RPO = <span class="ok">0</span>      → synchronous replication  (zero data loss)
RTO = <span class="ok">30s</span>    → hot standby, auto-promote (no manual steps)
Cost:         higher write latency, expensive hot standby
 
<span class="cm">// Analytics service (aggregate counts):</span>
RPO = <span class="yel">minutes</span> → periodic snapshots         (some loss OK)
RTO = <span class="yel">hours</span>   → restore from snapshot      (downtime OK)
Cost:         cheap backup storage, no standby infra
 
<span class="cm">// Product catalog (semi-static data):</span>
RPO = <span class="yel">seconds</span> → async replication           (small loss OK)
RTO = <span class="yel">minutes</span> → warm standby, semi-auto    (brief outage OK)
Cost:         moderate — warm standby only</pre>
  </div>
</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">1</div><div class="t-lbl">Latency Math Across Region Topologies</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Active-active Raft cluster: US-East (leader), EU-West, AP-Southeast. Client writes from US-East. What is the minimum write latency? Show the RTT math.</li>
          <li>Same cluster but AP-Southeast is non-voting. Now what is the write latency? What does AP-Southeast contribute?</li>
          <li>Add SA-East (~90ms from US-East) as a 4th non-voting replica. Does write latency change? Does read latency for SA-East users change?</li>
          <li>Tokyo user on active-passive system (US-East is primary, AP-Southeast has read replica). RTT for a write? RTT for a read? What SLA is achievable for Tokyo reads vs writes?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">2</div><div class="t-lbl">PN-Counter CRDT Implementation</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Implement <code>PNCounter(nodeId, numNodes)</code> with <code>increment()</code>, <code>decrement()</code>, <code>merge(other)</code>, and <code>value()</code></li>
          <li>Test: Node A increments 3×, Node B increments 5× and decrements 2×. Merge A→B and B→A. Verify both show value=6.</li>
          <li>Test idempotency: merge A into B twice. Does the result change?</li>
          <li>Test commutativity: merge(A,B) == merge(B,A)?</li>
          <li>Why can a regular integer counter NOT be a CRDT? Which of the three properties (commutative, associative, idempotent) does it violate?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">3</div><div class="t-lbl">GDPR Architecture for Twitter Feed (B6)</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>List all personal data fields in the B6 Twitter design. Which must be GDPR-protected?</li>
          <li>Design regional partitioning: can an EU user's tweet be cached in a US Redis instance? Can it be in a US CDN edge node?</li>
          <li>User exercises right to erasure. Step-by-step deletion from: Cassandra (with TTR replicas), Redis timelines, ClickHouse analytics, Kafka topic logs.</li>
          <li>Design cryptographic erasure: what is the KMS key structure? Who manages keys? How long does deletion take to propagate?</li>
          <li>EU user's timeline includes tweets from a US user. Is including those tweets in EU storage a GDPR violation?</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--tea)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--tea)">★</div><div class="t-lbl">Multi-Region E-Commerce (India + EU)</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>50M India users, 20M EU users. GDPR applies to EU. Products in both India and EU warehouses.</p>
        <ol>
          <li>Product catalog (read-heavy, non-personal): which replication strategy? Active-active LWW? Read replicas? GLOBAL locality? Justify.</li>
          <li>Inventory (globally shared — 1 unit in Bangalore can be bought by India or EU user): how do you prevent overselling without a global lock?</li>
          <li>Orders: EU orders must stay in EU (GDPR). India user buys from EU warehouse — where does the order record live?</li>
          <li>RPO/RTO for each service: inventory RPO=0/RTO=30s, catalog RPO=minutes/RTO=hours, orders RPO=0/RTO=60s. Design the specific replication for each.</li>
          <li>Right to erasure for an EU user who has orders, reviews, and browsing history. What gets deleted? What can be retained (anonymized)?</li>
        </ol>
      </div>
    </div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 20 completed</span><span style="font-family:'Space Mono',monospace">MODULE C2 · GEO-DISTRIBUTION</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Three reasons for multi-region: availability, latency, compliance</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">RTT numbers: US↔EU ~85ms, US↔APAC ~140ms, cross-AZ ~1ms</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sync global Raft → write latency = furthest region RTT (85–140ms)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Non-voting replicas: local write quorum + async remote replication</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Active-passive: RPO (sync=0, async=seconds), RTO (auto=30s, manual=minutes)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Active-active conflict strategies: LWW, vector clocks, CRDTs, OT</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">CRDT properties: commutative + associative + idempotent merge</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">G-Counter: vector per node, merge=max per slot, value=sum</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">PN-Counter: two G-Counters, value = P - N</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">G-Set, 2P-Set, OR-Set — merge rules and use cases</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Sequence CRDTs (RGA/LSEQ) for collaborative text editing</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">DynamoDB Global Tables: LWW active-active, ~1s lag, bad for counters</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">CockroachDB: REGIONAL BY ROW, GLOBAL, non-voting replicas, follower reads</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">GDPR: data classification, regional partitioning, geo-routing</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">GDPR right to erasure: cryptographic erasure via KMS key deletion</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">GDPR third parties: hash/pseudonymize before sending to log aggregators</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">RPO/RTO formula: SLA → downtime budget → RTO → replication strategy</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: latency math across region topologies</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: PN-Counter CRDT implementation + property verification</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): multi-region e-commerce India + EU</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--tea)">
    <div style="font-family:'Space Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'Playfair Display',serif;font-size:24px;color:var(--white);margin-bottom:6px">C3 — ML Systems Design</div>
    <div style="font-family:'Space Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
      Feature stores · Training pipelines · Model serving infrastructure<br>
      A/B testing at scale · Shadow mode deployment · Feedback loops<br>
      Real-time vs batch inference · Model versioning · Embeddings at scale
    </div>
  </div>
</div>
</div>
<div class="mb-nav">
  <a href="/learning/system-design/hld/module-c1-consensus/">← C1 Consensus</a>
  <a href="/learning/system-design/hld/module-c2-notes/">📄 Study Notes</a>
  <a href="/learning/system-design/system-design-roadmap/">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b13-ml-systems/" class="primary">C3 ML Systems →</a>
</div>
<script src="/assets/js/sd-module-c2.js"></script>
