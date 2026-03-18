---
layout: default
title: "M11 - OSPF Internals"
permalink: /learning/networking-mastery/m11-ospf/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#5b3a8c 70%,#3a1a6c 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c0a8f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#dcc8f8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ecdcff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#c0a8f0;border-bottom-color:#c0a8f0}
.tab-pane{display:none}
.tab-pane.active{display:block}
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
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.tag-blue{background:#d0e8f8;color:#1a4a7c}
.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #5b3a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dcc8f8;white-space:pre}
.cm{color:#7a5a90}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f0ecfc;border:1.5px solid #5b3a8c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e1028;border-color:#7060a8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3a1a6c}
[data-theme=dark] .ins strong{color:#c0a8f0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#3a1a6c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#5b3a8c}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#3a1a6c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#c0a8f0;padding:2px 8px;border-radius:4px;margin-top:.3rem}
.lab-box{border:2px solid #5b3a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#5b3a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#5b3a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#5b3a8c;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 3 · MODULE 11 · WEEK 9</div>
  <div class="mod-title">🔄 OSPF Internals</div>
  <div class="mod-subtitle">Link-state routing · LSA types · SPF algorithm · Areas · DR/BDR election · Convergence · OSPFv3</div>
  <div class="mod-pills">
    <span class="mod-pill">Intermediate</span>
    <span class="mod-pill">Prerequisite: M10 Routing</span>
    <span class="mod-pill">RFC 2328 · RFC 5340</span>
    <span class="mod-pill">Enterprise IGP</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">OSPF Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Neighbour Formation</button>
  <button class="tab-btn" onclick="vt(event,'t2')">LSA Types</button>
  <button class="tab-btn" onclick="vt(event,'t3')">SPF Algorithm</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Areas and DR/BDR</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Convergence and Timers</button>
  <button class="tab-btn" onclick="vt(event,'t6')">OSPFv3</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>


<!-- ════ TAB 0 — OSPF OVERVIEW ════ -->
<div id="t0" class="tab-pane active">
<p class="sep">OSPF — OPEN SHORTEST PATH FIRST</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>What OSPF Is — Link-State Routing</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
    <p>OSPF (Open Shortest Path First, RFC 2328) is the dominant Interior Gateway Protocol (IGP) in enterprise and service-provider networks. It is a <strong>link-state routing protocol</strong> — each router builds a complete topological map of the network (the Link State Database, LSDB) and runs Dijkstra's shortest path algorithm on it to compute optimal routes.</p>
    <p><strong>Why link-state outperforms distance-vector (RIP):</strong></p>
    <ul>
      <li><strong>No routing loops</strong> — each router has the full topology and computes paths independently; it doesn't relay information it learned from neighbours (which is how distance-vector creates loops)</li>
      <li><strong>Fast convergence</strong> — topology changes propagate as flooded LSAs; SPF recalculation can complete in milliseconds with incremental SPF</li>
      <li><strong>Scales to large networks</strong> — hierarchical areas limit LSDB size and SPF scope</li>
      <li><strong>Cost-based metric</strong> — OSPF cost is proportional to interface bandwidth; optimal path is truly the lowest-cost path, not just the fewest hops</li>
    </ul>
    <p>OSPF runs over IP directly (Protocol 89) — not TCP or UDP. Uses multicast for most communication: <code>224.0.0.5</code> (all OSPF routers) and <code>224.0.0.6</code> (DR/BDR only).</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>OSPF Cost — The Routing Metric</h3><span class="tag tag-blue">METRIC</span></div>
  <div class="cp-body">
    <p>OSPF uses <strong>cost</strong> as its metric. The default cost formula is <code>10^8 / interface_bandwidth_bps</code>. Lower cost = better path. The cost of a route is the sum of costs of all outgoing interfaces on the path from source to destination.</p>
<div class="cb"><pre><span class="cm">/* Default OSPF costs (reference bandwidth = 100 Mbps) */</span>
10 Mbps  Ethernet:  10^8 / 10^7  = 10
100 Mbps Ethernet:  10^8 / 10^8  = 1   (minimum default)
1 Gbps   Ethernet:  10^8 / 10^9  = 0.1 → rounds up to 1 (same as 100M!)
10 Gbps  Ethernet:  10^8 / 10^10 = 0.01 → rounds up to 1 (same!)

<span class="cm">/* Problem: default reference bandwidth doesn't differentiate fast links */</span>
<span class="cm">/* Solution: increase reference bandwidth to 100 Gbps */</span>

auto-cost reference-bandwidth 100000  <span class="cm"># Cisco IOS (Mbps)</span>
ip ospf cost 10                       <span class="cm"># manual cost per interface</span>

<span class="cm">/* With 100G reference bandwidth */</span>
1 Gbps:  10^11 / 10^9  = 100
10 Gbps: 10^11 / 10^10 = 10
100 Gbps: 10^11 / 10^11 = 1

<span class="cm">/* Linux FRR OSPF */</span>
vtysh
  router ospf
    ospf router-id 1.1.1.1
    network 192.168.0.0/24 area 0
    auto-cost reference-bandwidth 100000</pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 1 — NEIGHBOUR FORMATION ════ -->
<div id="t1" class="tab-pane">
<p class="sep">OSPF NEIGHBOUR STATES — FROM DOWN TO FULL</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>OSPF Neighbour State Machine</h3><span class="tag tag-blue">STATES</span></div>
  <div class="cp-body">
    <p>OSPF neighbours must exchange the full LSDB before routing can start. This process goes through a defined sequence of states. Understanding these states is essential for troubleshooting OSPF — "stuck in 2-Way" or "stuck in Exstart" are common failure modes.</p>

<div class="cb"><pre><span class="cm">/* OSPF Neighbour States */</span>

DOWN        No Hello received. Initial state or after timeout.

INIT        Hello received from neighbour, but our Router-ID
            not yet in their neighbour list.

2-WAY       Our Router-ID seen in neighbour's Hello.
            Bidirectional communication confirmed.
            On broadcast networks: DR/BDR election happens here.
            Non-DR/BDR neighbours stop here (2-Way with DR/BDR → Full).

EXSTART     Master/Slave election via DBD packets.
            Higher Router-ID becomes Master, controls sequence numbers.

EXCHANGE    Routers exchange Database Description (DBD) packets —
            summaries of their LSDB (LSA headers only, not full LSAs).

LOADING     Router sends LSR (Link State Request) for LSAs it's missing.
            Neighbour sends LSU (Link State Update) with the requested LSAs.

FULL        LSDBs are synchronised. Routing table can be computed.
            This is the healthy operational state.

<span class="cm">/* Hello packet fields that must match for neighbour formation */</span>
Area ID:             must be identical
Authentication:      must match (none/simple/MD5)
Hello interval:      must match (default 10s point-to-point, 10s broadcast)
Dead interval:       must match (default 40s = 4 × hello)
Subnet mask:         must match (point-to-point links exempt)
Stub area flag:      must match

<span class="cm">/* Troubleshooting stuck neighbours */</span>
show ip ospf neighbor           <span class="cm"># current state</span>
show ip ospf neighbor detail    <span class="cm"># full detail including timers</span>
debug ip ospf adj               <span class="cm"># live adjacency events</span>

<span class="cm">/* Stuck in EXSTART: MTU mismatch — one side has jumbo frames, other doesn't */</span>
<span class="cm"># DBD packets use the interface MTU — if mismatched, packets get fragmented</span>
<span class="cm"># Fix: ip ospf mtu-ignore  (or fix the MTU)</span></pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Hello Protocol — The OSPF Heartbeat</h3><span class="tag tag-teal">HELLO</span></div>
  <div class="cp-body">
    <p>OSPF Hello packets are sent periodically to discover and maintain neighbour relationships. Sent to multicast 224.0.0.5 (all OSPF routers) on broadcast networks, or unicast on point-to-point links.</p>
<div class="cb"><pre><span class="cm">/* Hello packet key fields */</span>
Router ID:       4-byte identifier for this router (highest loopback IP, or manually set)
Area ID:         which OSPF area this interface belongs to
Auth Type/Data:  authentication (0=none, 1=cleartext, 2=MD5 hmac)
Hello Interval:  how often this router sends Hellos (default 10s)
Dead Interval:   time without Hello before declaring neighbour dead (default 40s)
DR:              IP of current Designated Router (0.0.0.0 if unknown)
BDR:             IP of current Backup DR
Neighbour List:  Router IDs of all neighbours from whom we've heard Hellos

<span class="cm">/* Timers — trade-off between convergence speed and CPU load */</span>
Default:      Hello=10s, Dead=40s   → convergence after 40s
Fast:         Hello=1s,  Dead=4s    → convergence after 4s (higher CPU)
BFD:          sub-second detection  → millisecond convergence (separate protocol)

<span class="cm">/* Linux FRR — configure OSPF timers per interface */</span>
interface eth0
  ip ospf hello-interval 1
  ip ospf dead-interval 4</pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 2 — LSA TYPES ════ -->
<div id="t2" class="tab-pane">
<p class="sep">LSA TYPES — THE BUILDING BLOCKS OF THE LINK STATE DATABASE</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📋</span><h3>LSA Types — What Each Describes</h3><span class="tag tag-purple">LSA REFERENCE</span></div>
  <div class="cp-body">
    <p>Link State Advertisements (LSAs) are the data records in OSPF's distributed database. Each LSA describes a piece of the network topology. Routers flood LSAs throughout the network (or area) so every router has an identical copy of the LSDB.</p>

    <table class="t-table">
      <thead><tr><th>Type</th><th>Name</th><th>Generated By</th><th>Flooded To</th><th>Describes</th></tr></thead>
      <tbody>
        <tr><td><code>1</code></td><td>Router LSA</td><td>Every router</td><td>Within area</td><td>Router's own links (interfaces), their types, and costs. Every router generates one Type 1 LSA per area it belongs to.</td></tr>
        <tr><td><code>2</code></td><td>Network LSA</td><td>DR only</td><td>Within area</td><td>List of all routers attached to a multi-access (broadcast) segment. Only generated when DR exists (broadcast/NBMA networks).</td></tr>
        <tr><td><code>3</code></td><td>Summary LSA</td><td>ABR (Area Border Router)</td><td>Between areas</td><td>Prefix reachability information from one area advertised into other areas. ABR summarises intra-area prefixes as inter-area routes.</td></tr>
        <tr><td><code>4</code></td><td>ASBR Summary LSA</td><td>ABR</td><td>Between areas</td><td>Tells other areas how to reach an ASBR (AS Boundary Router — a router that redistributes external routes into OSPF).</td></tr>
        <tr><td><code>5</code></td><td>External LSA (AS External)</td><td>ASBR</td><td>Entire OSPF domain</td><td>External routes redistributed into OSPF (from BGP, static, RIP, connected). Type E1 includes OSPF path cost; Type E2 does not.</td></tr>
        <tr><td><code>7</code></td><td>NSSA External LSA</td><td>ASBR in NSSA</td><td>NSSA area only → converted to Type 5 at ABR</td><td>External routes in Not-So-Stubby Areas. Allows external route origination without flooding Type 5 into the stub area.</td></tr>
        <tr><td><code>9/10/11</code></td><td>Opaque LSA</td><td>Any router</td><td>Link/Area/Domain scope</td><td>Extension mechanism for OSPF — carries TE (Traffic Engineering) extensions, MPLS TE, Segment Routing info.</td></tr>
      </tbody>
    </table>

    <div class="ins"><p>💡 <strong>Type 1 and Type 2 build the intra-area topology map.</strong> Type 3 extends reachability between areas. Type 5 brings external routes into OSPF. The SPF algorithm uses Types 1 and 2 to compute shortest paths. Types 3, 4, 5 are handled with Bellman-Ford style processing (not Dijkstra — they're already summarised distances, not raw topology).</p></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>LSA Flooding and Reliability</h3><span class="tag tag-teal">FLOODING</span></div>
  <div class="cp-body">
    <p>OSPF uses <strong>reliable flooding</strong> to ensure every router in the area gets every LSA. When a router receives a new or updated LSA, it floods it out all interfaces except the one it arrived on. Receivers acknowledge receipt with explicit LSAck packets.</p>
<div class="cb"><pre><span class="cm">/* LSA versioning — Sequence Number + Age */</span>
LSA fields for version control:
  Sequence Number:  32-bit counter, starts at 0x80000001, increments on each update
                    Higher = newer. MaxSequenceNumber (0x7FFFFFFF) triggers refresh.
  LSA Age:          seconds since originated. Incremented by each router in transit.
                    MaxAge (3600s) = LSA is stale, should be purged.
  LS Checksum:      integrity check over LSA (excluding Age field)

<span class="cm">/* Database Exchange summary */</span>
show ip ospf database          <span class="cm"># list all LSAs in LSDB</span>
show ip ospf database router   <span class="cm"># Type 1 LSAs only</span>
show ip ospf database summary  <span class="cm"># Type 3 LSAs only</span>
show ip ospf database external <span class="cm"># Type 5 LSAs</span>

<span class="cm">/* LSA refresh — prevent premature aging */</span>
<span class="cm"># Each router re-originates its own LSAs every 30 minutes (LSRefreshTime)</span>
<span class="cm"># This resets the Age counter so they don't expire (MaxAge = 3600s)</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 3 — SPF ALGORITHM ════ -->
<div id="t3" class="tab-pane">
<p class="sep">SPF — DIJKSTRA'S SHORTEST PATH FIRST ALGORITHM</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>How Dijkstra's SPF Works in OSPF</h3><span class="tag tag-blue">ALGORITHM</span></div>
  <div class="cp-body">
    <p>After collecting all LSAs and building the LSDB (the complete topological graph), each router independently runs Dijkstra's SPF algorithm to compute the shortest (lowest-cost) path to every destination. The algorithm is deterministic — given the same LSDB, every router computes identical results.</p>
<div class="cb"><pre><span class="cm">/* Dijkstra's algorithm — simplified */</span>
Input:  LSDB (directed graph of routers and links with costs)
Output: Shortest Path Tree (SPT) rooted at this router

1. Mark all routers with distance = ∞, except self = 0.
2. Put all routers in a priority queue (tentative set), keyed by distance.
3. While priority queue not empty:
   a. Extract router R with minimum distance from queue
   b. Mark R as "confirmed" (add to SPT)
   c. For each neighbour N of R (from R's Router LSA):
      new_dist = dist(R) + cost(R→N)
      if new_dist < dist(N):
          dist(N) = new_dist
          predecessor(N) = R
          Update N's priority in queue
4. SPT complete — predecessor array gives next-hop for each destination.

<span class="cm">/* Worked example */</span>
Network:  R1─(1)─R2─(1)─R4
           └─(10)─────────R3─(1)─R4

Computing SPT from R1:
Confirmed: {R1=0}
Tentative: {R2=1, R3=10}

Extract R2 (cost 1):
  Confirmed: {R1=0, R2=1}
  R4 via R2: cost = 1+1 = 2 → add R4=2
  Tentative: {R3=10, R4=2}

Extract R4 (cost 2):
  Confirmed: {R1=0, R2=1, R4=2}
  R3 via R4: cost = 2+1 = 3 → update R3=3 (was 10!)
  Tentative: {R3=3}

Extract R3 (cost 3):
  Confirmed: {R1=0, R2=1, R4=2, R3=3}

Result:
  R4 → via R2 (cost 2) — NOT via R3 (cost 11)
  R3 → via R2→R4 (cost 3) — NOT direct (cost 10)</pre></div>

    <div class="ins"><p>💡 <strong>SPF can be computationally expensive</strong> on large networks. A full SPF run on a 1000-router network takes milliseconds, but running it for every link flap would be unacceptable. OSPF uses <strong>SPF throttling</strong>: the first SPF runs immediately, subsequent SPF runs are delayed increasingly (1s, 5s, 10s…) to batch multiple topology changes. Incremental SPF (partial SPF) only recomputes paths affected by the changed LSA — much faster.</p></div>
  </div>
</div>
</div>


<!-- ════ TAB 4 — AREAS AND DR/BDR ════ -->
<div id="t4" class="tab-pane">
<p class="sep">OSPF AREAS AND DR/BDR ELECTION</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>OSPF Areas — Hierarchical Scaling</h3><span class="tag tag-purple">AREAS</span></div>
  <div class="cp-body">
    <p>A single OSPF domain with thousands of routers would have a massive LSDB and run SPF constantly. OSPF uses <strong>areas</strong> to divide the network hierarchically, limiting LSDB size and SPF scope within each area.</p>

    <table class="t-table">
      <thead><tr><th>Area Type</th><th>Contains</th><th>Accepts</th><th>Use Case</th></tr></thead>
      <tbody>
        <tr><td><strong>Backbone (Area 0)</strong></td><td>All Type 1,2,3,5 LSAs</td><td>All LSA types</td><td>Core transit area — all areas must connect to it (directly or virtually)</td></tr>
        <tr><td><strong>Regular Area</strong></td><td>Type 1,2,3,5 LSAs</td><td>All LSA types</td><td>Standard non-backbone area with external routes</td></tr>
        <tr><td><strong>Stub Area</strong></td><td>Type 1,2,3 LSAs (no Type 5)</td><td>No external LSAs; default route injected instead</td><td>Leaf areas with no external connectivity; reduces LSDB size</td></tr>
        <tr><td><strong>Totally Stubby</strong></td><td>Type 1,2 LSAs only</td><td>No Type 3 or 5; only default route</td><td>Maximum LSDB reduction for hub-and-spoke leaves</td></tr>
        <tr><td><strong>NSSA</strong></td><td>Type 1,2,3,7 LSAs</td><td>External routes via Type 7 (converted to Type 5 at ABR)</td><td>Stub area that needs to originate external routes (e.g., redistributed connected routes)</td></tr>
      </tbody>
    </table>

<div class="cb"><pre><span class="cm">/* Router roles in OSPF */</span>
Internal Router:    all interfaces in same area
ABR (Area Border):  interfaces in multiple areas — sits on area boundary
ASBR (AS Boundary): redistributes routes from/to external protocols (BGP, static)
Backbone Router:    has at least one interface in Area 0

<span class="cm">/* Virtual links — connect non-adjacent areas to Area 0 */</span>
router ospf 1
  area 2 virtual-link 3.3.3.3  <span class="cm"># create virtual link through area 2 to router 3.3.3.3</span></pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">👑</span><h3>DR and BDR Election — Reducing Adjacencies on Broadcast Networks</h3><span class="tag tag-teal">DR/BDR</span></div>
  <div class="cp-body">
    <p>On a broadcast segment (Ethernet) with N routers, forming full-mesh adjacencies requires N×(N-1)/2 adjacency pairs — with 10 routers that's 45 full adjacencies, each exchanging the full LSDB. OSPF solves this with a Designated Router (DR) and Backup Designated Router (BDR):</p>
    <ul>
      <li>All routers form full adjacency with the DR and BDR only</li>
      <li>Non-DR/BDR routers reach state 2-WAY with each other — not FULL</li>
      <li>All LSA flooding goes through the DR (sent to 224.0.0.5, DR forwards to 224.0.0.6)</li>
      <li>With 10 routers: only 2×(N-1) = 18 adjacencies instead of 45</li>
    </ul>

<div class="cb"><pre><span class="cm">/* DR/BDR Election process */</span>
1. All routers send Hellos with their Priority and Router-ID
2. Router with highest Priority wins DR election (default priority = 1)
3. Tie-break: highest Router-ID wins
4. Second-highest priority/RID wins BDR
5. Priority 0 = ineligible for DR/BDR (always a DROther)

<span class="cm">/* Important: DR election is NOT preemptive */</span>
<span class="cm"># Even if a router with higher priority joins later, the current DR stays</span>
<span class="cm"># DR changes only when current DR fails</span>
<span class="cm"># This prevents constant re-election on flapping networks</span>

<span class="cm">/* Setting DR priority */</span>
interface GigabitEthernet0/0
  ip ospf priority 100   <span class="cm"># make this the preferred DR</span>
  ip ospf priority 0     <span class="cm"># never become DR</span>

<span class="cm">/* Verify DR/BDR */</span>
show ip ospf interface GigabitEthernet0/0
<span class="cm"># "Designated Router (ID) 2.2.2.2, Interface address 192.168.1.2"</span>
<span class="cm"># "Backup Designated router (ID) 1.1.1.1, Interface address 192.168.1.1"</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 5 — CONVERGENCE AND TIMERS ════ -->
<div id="t5" class="tab-pane">
<p class="sep">OSPF CONVERGENCE — TIMERS, FAILURE DETECTION, AND TUNING</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>OSPF Convergence Timeline</h3><span class="tag tag-orange">CONVERGENCE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* What happens when a link fails */</span>

T=0:       Link goes down
T=0:       Router detects link down (interface state change — instantaneous)
T=0:       Router generates new Router LSA (Type 1) marking the link as failed
T=0–0.1:   LSA flooded to all routers in the area
T=0–0.1:   Each router runs incremental SPF
T=0–0.1:   FIB updated — traffic rerouted
           Total: sub-second convergence for link-down detection!

<span class="cm">/* What happens when a router fails (link stays up, router crashes) */</span>

T=0:       Router crashes
T=0–40:    Other routers still send Hellos, get no response
T=40:      Dead interval expires — router declared dead
T=40:      LSA generated removing dead router
T=40:      LSA flooded + SPF runs
T=40+:     Routes converged
           Total: default 40 seconds! Much slower.

<span class="cm">/* Solutions for fast failure detection */</span>

Option 1: Reduce timers (Hello=1s, Dead=4s)
  Con: 4x more Hello processing; sensitive to packet loss

Option 2: BFD (Bidirectional Forwarding Detection)
  Sub-second (ms) failure detection, separate from OSPF
  OSPF reacts when BFD reports peer down (before Dead interval)
  bfd interval 100 min_rx 100 multiplier 3   <span class="cm"># 300ms detection</span>

Option 3: OSPF Fast Hello (hello every 1 second, dead 4 seconds)
  interface eth0
    ip ospf dead-interval minimal hello-multiplier 4  <span class="cm"># hello = dead/4 = 250ms</span></pre></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Key OSPF Timers</h3><span class="tag tag-green">TIMERS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Timer</th><th>Default</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td>Hello Interval</td><td>10s (broadcast), 30s (NBMA)</td><td>How often Hello packets are sent</td></tr>
        <tr><td>Dead Interval</td><td>4 × Hello (40s or 120s)</td><td>How long to wait before declaring neighbour dead</td></tr>
        <tr><td>Retransmit Interval</td><td>5s</td><td>How long to wait for LSAck before retransmitting LSU</td></tr>
        <tr><td>SPF Delay</td><td>5s</td><td>Delay before running SPF after topology change (prevents SPF thrashing)</td></tr>
        <tr><td>SPF Hold Time</td><td>10s</td><td>Minimum time between successive full SPF runs</td></tr>
        <tr><td>LSA Refresh Time</td><td>30 min</td><td>How often routers re-originate their own LSAs to prevent aging out</td></tr>
        <tr><td>MaxAge</td><td>3600s (1 hr)</td><td>LSA expires and is purged after this age</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════ TAB 6 — OSPFv3 ════ -->
<div id="t6" class="tab-pane">
<p class="sep">OSPFv3 — OSPF FOR IPv6 (RFC 5340)</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔵</span><h3>OSPFv3 vs OSPFv2 — Key Differences</h3><span class="tag tag-blue">OSPFv3</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Feature</th><th>OSPFv2</th><th>OSPFv3</th></tr></thead>
      <tbody>
        <tr><td>IP version</td><td>IPv4</td><td>IPv6 (also supports IPv4 with address families)</td></tr>
        <tr><td>Transport</td><td>IP Protocol 89</td><td>IPv6 Protocol 89</td></tr>
        <tr><td>Router ID</td><td>32-bit IPv4 address</td><td>32-bit value (looks like IPv4 but is just an ID, not an address)</td></tr>
        <tr><td>Addressing in packets</td><td>IPv4 addresses in LSAs</td><td>Link-local addresses for neighbour communication; global addresses in separate LSA types</td></tr>
        <tr><td>Authentication</td><td>Built-in (cleartext or MD5)</td><td>Uses IPsec AH/ESP (authentication outsourced)</td></tr>
        <tr><td>New LSA types</td><td>Type 1–5, 7</td><td>Adds Type 8 (Link LSA), Type 9 (Intra-Area Prefix LSA). Type 1/2 no longer carry IP prefixes.</td></tr>
        <tr><td>Multiple instances</td><td>One per link</td><td>Multiple OSPFv3 instances per link (different instance IDs)</td></tr>
      </tbody>
    </table>

<div class="cb"><pre><span class="cm">/* Linux FRR: configure OSPFv3 */</span>
vtysh
  router ospf6
    ospf6 router-id 1.1.1.1   <span class="cm"># must set manually (no IPv4 to borrow)</span>
    interface eth0 area 0.0.0.0

  interface eth0
    ipv6 ospf6 area 0.0.0.0

show ipv6 ospf6 neighbor
show ipv6 ospf6 database
show ipv6 ospf6 route

<span class="cm">/* Verify OSPFv3 uses link-local source addresses */</span>
<span class="cm"># Hellos sent from fe80::... not global unicast</span>
<span class="cm"># Link-local = no router will forward these beyond the segment</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 7 — LABS ════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>OSPF with FRR on Linux — Full Network Simulation</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a 3-router OSPF topology using Linux network namespaces and FRR. Observe neighbour formation, LSDB contents, SPF computation, and convergence on link failure.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install FRR: <code>sudo apt install frr</code>. Enable OSPF: in <code>/etc/frr/daemons</code>, set <code>ospfd=yes</code>. Restart: <code>sudo systemctl restart frr</code>. Access FRR CLI: <code>sudo vtysh</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Create 3 network namespaces as routers using veth pairs. Configure IP addresses: R1(10.0.12.1/30 ↔ R2(10.0.12.2/30), R2(10.0.23.1/30) ↔ R3(10.0.23.2/30), R1 has loopback 1.1.1.1/32, R3 has loopback 3.3.3.3/32.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Configure OSPF on all three: <code>router ospf; ospf router-id X.X.X.X; network 0.0.0.0/0 area 0</code>. Verify neighbours reach FULL state: <code>show ip ospf neighbor</code>. Observe the 4-state transition in logs.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Examine the LSDB: <code>show ip ospf database</code>. Identify: how many Type 1 LSAs? Which router generated the Type 2 LSA? What prefixes appear in the database?</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Test reachability: from R1, <code>ping 3.3.3.3</code>. Verify route learned: <code>show ip route ospf</code>. Now simulate link failure: <code>ip link set veth12 down</code>. Watch convergence — how long until ping recovers?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Dijkstra SPF Implementation</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement Dijkstra's algorithm in Python to simulate what OSPF's SPF calculation does, given a network topology described as a graph.</p>
    <div class="lab-step"><div class="sn">1</div><div>Represent a network as an adjacency list: <code>graph = {'R1': [('R2',1),('R3',10)], 'R2': [('R1',1),('R4',1)], 'R3': [('R1',10),('R4',1)], 'R4': [('R2',1),('R3',1)]}</code>. Implement Dijkstra using a priority queue (heapq).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Output the shortest path tree from R1: for each destination, print the path (sequence of routers) and total cost. Verify: R1→R4 should go R1→R2→R4 (cost 2), not R1→R3→R4 (cost 11).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Simulate link failure: remove the R1↔R2 link. Re-run Dijkstra. Verify R4 is now reached via R1→R3→R4 (cost 11). This is what OSPF SPF re-computes after a topology change.</div></div>
  </div>
</div>
</div>


<!-- ════ TAB 8 — CHECKLIST ════ -->
<div id="t8" class="tab-pane">
<p class="sep">M11 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know OSPF is a link-state protocol: each router builds a complete topology map (LSDB) and runs Dijkstra SPF independently</li>
  <li>Know OSPF uses IP Protocol 89 (not TCP/UDP), multicast 224.0.0.5 (all routers) and 224.0.0.6 (DR/BDR)</li>
  <li>Know OSPF cost formula: 10^8 / bandwidth; know why default reference bandwidth fails for GigE+ links</li>
  <li>Know the 7 OSPF neighbour states: DOWN, INIT, 2-WAY, EXSTART, EXCHANGE, LOADING, FULL</li>
  <li>Know Hello parameters that must match: Area ID, authentication, hello interval, dead interval, subnet mask, stub flag</li>
  <li>Know what causes stuck-in-EXSTART: MTU mismatch between neighbours</li>
  <li>Know the 6 primary LSA types: 1=Router, 2=Network(DR), 3=Summary(ABR), 4=ASBR Summary, 5=External(ASBR), 7=NSSA External</li>
  <li>Know which LSAs are flooded where: Type 1/2 = within area, Type 3/4 = between areas, Type 5 = entire OSPF domain</li>
  <li>Know LSA fields for versioning: Sequence Number (increments), Age (increments), MaxAge=3600s</li>
  <li>Know Dijkstra SPF: start at self=0, iteratively add minimum-cost unconfirmed node, update neighbours</li>
  <li>Know SPF throttling: delays between SPF runs prevent thrashing on unstable networks</li>
  <li>Know OSPF area types: Backbone (Area 0), Regular, Stub (no Type 5), Totally Stubby (no Type 3/5), NSSA</li>
  <li>Know router roles: Internal, ABR (Area Border), ASBR (AS Boundary), Backbone</li>
  <li>Know why DR/BDR exist: reduce N×(N-1)/2 adjacencies to 2×(N-1) on broadcast segments</li>
  <li>Know DR election: highest priority wins, then highest Router-ID; NOT preemptive</li>
  <li>Know convergence timeline: link-down = sub-second; router crash = Dead Interval (40s default)</li>
  <li>Know BFD: sub-millisecond failure detection independent of OSPF Hello timers</li>
  <li>Know OSPFv3 key differences: IPv6 transport, link-local addressing, IPsec auth, new LSA types 8/9</li>
  <li>Completed Lab 1: built 3-router OSPF network with FRR, observed LSDB, tested convergence on link failure</li>
  <li>Completed Lab 2: implemented Dijkstra SPF in Python, verified path computation and re-convergence after failure</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M12 - BGP Internals</strong>. Where OSPF is the IGP within an organisation's network, BGP is the EGP that connects organisations together across the internet — and is also used within large networks (iBGP) for scalability.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/networking-mastery/m10-routing-fundamentals/' | relative_url }}">← M10 Routing</a>
  <a href="{{ '/learning/networking-mastery/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m12-bgp/' | relative_url }}">Next: M12 - BGP →</a>
</div>

<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
