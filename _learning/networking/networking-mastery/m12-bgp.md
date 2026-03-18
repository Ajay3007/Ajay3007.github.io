---
layout: default
title: "M12 - BGP Internals"
permalink: /learning/networking-mastery/m12-bgp/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#8c3a0a 70%,#6a2800 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0c880;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f8dfa8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#faecc8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f0c880;border-bottom-color:#f0c880}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #8c3a0a}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0dfa8;white-space:pre}
.cm{color:#8a6030}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#fdf8e8;border:1.5px solid #c09030;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#2a1e00;border-color:#c09030}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#7a5800}
[data-theme=dark] .ins strong{color:#f0c880}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1cm;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#6a2800;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#8c3a0a}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #8c3a0a;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#8c3a0a;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#8c3a0a;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#8c3a0a;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 3 · MODULE 12 · WEEK 10</div>
  <div class="mod-title">🌍 BGP Internals</div>
  <div class="mod-subtitle">eBGP vs iBGP · Path attributes · Best-path selection · Route policy · Communities · BGP security</div>
  <div class="mod-pills">
    <span class="mod-pill">Intermediate → Advanced</span>
    <span class="mod-pill">Prerequisite: M10, M11</span>
    <span class="mod-pill">RFC 4271</span>
    <span class="mod-pill">Internet Routing Protocol</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">BGP Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">eBGP vs iBGP</button>
  <button class="tab-btn" onclick="vt(event,'t2')">BGP Session</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Path Attributes</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Best-Path Selection</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Route Policy</button>
  <button class="tab-btn" onclick="vt(event,'t6')">BGP Security</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>


<!-- ════ TAB 0 — BGP OVERVIEW ════ -->
<div id="t0" class="tab-pane active">
<p class="sep">BGP — THE ROUTING PROTOCOL OF THE INTERNET</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🌍</span><h3>What Makes BGP Different</h3><span class="tag tag-orange">OVERVIEW</span></div>
  <div class="cp-body">
    <p>BGP (Border Gateway Protocol, RFC 4271) is the routing protocol that makes the internet work. It is the only EGP (Exterior Gateway Protocol) in use today — it connects the ~75,000 Autonomous Systems (ASes) that make up the global internet. Unlike OSPF which optimises for fastest path, <strong>BGP is a policy-driven protocol</strong>: its primary goal is to express complex business routing policies, not to find the mathematically shortest path.</p>
    <p><strong>BGP's defining characteristics:</strong></p>
    <ul>
      <li><strong>Path-vector protocol</strong> — routes carry the full AS-PATH (list of ASes the prefix has traversed). Loop prevention is achieved by rejecting routes that already contain your own AS number in the path</li>
      <li><strong>TCP-based</strong> — sessions run over TCP port 179. The reliability and ordering of TCP replace BGP's need for its own retransmission mechanism</li>
      <li><strong>Rich attribute system</strong> — routes carry attributes (AS-PATH, NEXT-HOP, LOCAL-PREF, MED, COMMUNITY) that encode routing policy</li>
      <li><strong>Scales to internet size</strong> — the global BGP table contains ~950,000 prefixes (2024) carried by route reflectors and confederation hierarchies</li>
      <li><strong>Incremental updates</strong> — BGP sends only changes (UPDATE messages), not full table re-advertisements like distance-vector protocols</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏢</span><h3>Autonomous Systems — The BGP Addressing Model</h3><span class="tag tag-blue">AS MODEL</span></div>
  <div class="cp-body">
    <p>The internet is divided into <strong>Autonomous Systems (ASes)</strong> — networks under a single administrative control (an ISP, a company, a university). Each AS is assigned a unique AS Number (ASN) by a Regional Internet Registry (RIR like APNIC for Asia-Pacific). Jio Platforms' ASN is <strong>AS55836</strong>.</p>
<div class="cb"><pre><span class="cm">/* ASN ranges */</span>
16-bit ASNs (legacy): 1–65535
  Private range:      64512–65535 (like RFC 1918 for IPs)
  Public range:       1–64511

32-bit ASNs (modern): 1–4294967295
  Private range:      4200000000–4294967294
  Public range:       everything else

<span class="cm">/* AS relationships */</span>
Transit:   AS-A pays AS-B to carry traffic to/from the internet
           (customer → provider relationship)
Peering:   AS-A and AS-B exchange traffic for free
           (both benefit — settlement-free peering)
IXP:       Internet Exchange Point — physical location where
           many ASes peer simultaneously (AMS-IX, DE-CIX, NIXI)

<span class="cm">/* Look up any ASN */</span>
whois -h whois.radb.net AS55836
bgp.he.net/AS55836   <span class="cm"># HE BGP toolkit</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 1 — eBGP vs iBGP ════ -->
<div id="t1" class="tab-pane">
<p class="sep">eBGP vs iBGP — EXTERNAL AND INTERNAL BGP</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚖️</span><h3>The Critical Difference Between eBGP and iBGP</h3><span class="tag tag-teal">COMPARISON</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Property</th><th>eBGP (External)</th><th>iBGP (Internal)</th></tr></thead>
      <tbody>
        <tr><td>Between</td><td>Routers in <strong>different</strong> ASes</td><td>Routers in the <strong>same</strong> AS</td></tr>
        <tr><td>Default TTL</td><td>1 (must be directly connected)</td><td>255 (can be multiple hops away)</td></tr>
        <tr><td>AS-PATH handling</td><td>Prepends own AS number to AS-PATH</td><td>Does NOT modify AS-PATH</td></tr>
        <tr><td>NEXT-HOP handling</td><td>Sets NEXT-HOP to own IP address</td><td>Does NOT change NEXT-HOP (leaves as eBGP learned next-hop)</td></tr>
        <tr><td>Route propagation rule</td><td>Routes can be sent to any eBGP peer</td><td><strong>iBGP split-horizon</strong>: routes learned from iBGP peer NOT re-advertised to another iBGP peer</td></tr>
        <tr><td>Full mesh requirement</td><td>No — each AS has its own eBGP peers</td><td>Yes — requires full mesh OR Route Reflectors OR Confederation</td></tr>
        <tr><td>Administrative Distance</td><td>20 (preferred over IGP routes)</td><td>200 (least preferred)</td></tr>
        <tr><td>LOCAL-PREF</td><td>Not sent between ASes</td><td>Shared between all iBGP peers in AS</td></tr>
      </tbody>
    </table>

    <div class="ins"><p>💡 <strong>iBGP split-horizon is the key scaling challenge.</strong> Because iBGP routes can't be re-advertised between iBGP peers, every router must have a direct iBGP session with every other router — O(N²) sessions. With 100 BGP routers in an AS: 4950 sessions. Solutions: <strong>Route Reflectors</strong> (a designated RR re-advertises iBGP routes to all clients) or <strong>Confederation</strong> (divide the AS into sub-ASes with eBGP between them).</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Route Reflectors — Solving the Full-Mesh Problem</h3><span class="tag tag-blue">ROUTE REFLECTORS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Without Route Reflector (full mesh required) */</span>
R1 ←→ R2, R1 ←→ R3, R1 ←→ R4
R2 ←→ R3, R2 ←→ R4
R3 ←→ R4
Total: N(N-1)/2 = 6 sessions for 4 routers

<span class="cm">/* With Route Reflector RR */</span>
R1 (RR) ←→ R2 (client)
R1 (RR) ←→ R3 (client)
R1 (RR) ←→ R4 (client)
Total: N-1 = 3 sessions!

RR re-advertises routes received from:
  - iBGP client → to ALL other iBGP clients and eBGP peers
  - eBGP peer   → to ALL iBGP clients
  - Non-client iBGP → to clients only (NOT to other non-clients)

<span class="cm">/* RR adds ORIGINATOR-ID and CLUSTER-LIST attributes to prevent loops */</span>
ORIGINATOR-ID: Router-ID of the original route source
CLUSTER-LIST:  List of route reflector clusters the route passed through
If router receives a route with its own Router-ID in ORIGINATOR-ID → discard

<span class="cm">/* FRR BGP Route Reflector config */</span>
router bgp 65001
  neighbor 10.0.0.2 remote-as 65001
  neighbor 10.0.0.2 route-reflector-client  <span class="cm"># make this peer a RR client</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 2 — BGP SESSION ════ -->
<div id="t2" class="tab-pane">
<p class="sep">BGP SESSION ESTABLISHMENT AND MESSAGE TYPES</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>BGP Session Establishment</h3><span class="tag tag-blue">SESSION</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* BGP uses TCP port 179 — sessions are manually configured */</span>
<span class="cm">/* Unlike OSPF (auto-discovers neighbours), BGP peers must be explicitly configured */</span>

<span class="cm">/* BGP FSM (Finite State Machine) */</span>
Idle        → (start) → Connect
Connect     → TCP connection attempt → (success) OpenSent / (fail) Active
Active      → retry TCP connection
OpenSent    → TCP connected, OPEN sent, waiting for peer's OPEN
OpenConfirm → Both OPENs received, waiting for KEEPALIVE
Established → Session up! Exchanging routes via UPDATE messages

<span class="cm">/* BGP OPEN message fields */</span>
Version:        4 (BGPv4)
My AS:          local AS number
Hold Time:      max seconds between messages (negotiate min of peers' values)
BGP Identifier: router-id (32-bit)
Optional Params: capabilities (4-octet ASN, route-refresh, multiprotocol)

<span class="cm">/* BGP Message Types */</span>
OPEN:        Session establishment — exchange capabilities
UPDATE:      Route advertisements and withdrawals
KEEPALIVE:   Heartbeat — prevents Hold Timer expiry (default every HoldTime/3)
NOTIFICATION:Error notification — followed by TCP teardown
ROUTE-REFRESH: Request peer to re-send full routing table (RFC 2918)

<span class="cm">/* BGP timers */</span>
Connect Retry: 120s (retry TCP connect after failure)
Hold Timer:    90s default (reset on any BGP message)
Keepalive:     HoldTime/3 = 30s default

<span class="cm">/* FRR BGP basic config */</span>
router bgp 65001
  bgp router-id 1.1.1.1
  neighbor 203.0.113.1 remote-as 65002       <span class="cm"># eBGP peer</span>
  neighbor 10.0.0.2    remote-as 65001       <span class="cm"># iBGP peer</span>
  neighbor 10.0.0.2    update-source lo      <span class="cm"># use loopback for iBGP</span>
  !
  address-family ipv4 unicast
    network 192.0.2.0/24                      <span class="cm"># advertise this prefix</span>
    neighbor 203.0.113.1 activate
    neighbor 10.0.0.2 activate
    neighbor 10.0.0.2 next-hop-self          <span class="cm"># fix iBGP next-hop issue</span>
  exit-address-family</pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 3 — PATH ATTRIBUTES ════ -->
<div id="t3" class="tab-pane">
<p class="sep">BGP PATH ATTRIBUTES — THE ROUTING POLICY TOOLKIT</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📋</span><h3>BGP Path Attributes Reference</h3><span class="tag tag-orange">ATTRIBUTES</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attribute</th><th>Type</th><th>Values</th><th>Used For</th></tr></thead>
      <tbody>
        <tr><td><strong>ORIGIN</strong></td><td>Well-known mandatory</td><td>IGP(i), EGP(e), Incomplete(?)</td><td>How the prefix entered BGP. IGP = best, Incomplete = redistributed from IGP or static</td></tr>
        <tr><td><strong>AS-PATH</strong></td><td>Well-known mandatory</td><td>Sequence of AS numbers: [65001, 65002, 65003]</td><td>Loop prevention + path selection (shorter = preferred) + policy matching</td></tr>
        <tr><td><strong>NEXT-HOP</strong></td><td>Well-known mandatory</td><td>IP address of next-hop router</td><td>Tells receiver which router to send traffic to. Key iBGP problem: may not be reachable without IGP.</td></tr>
        <tr><td><strong>LOCAL-PREF</strong></td><td>Well-known discretionary</td><td>0–4294967295 (default 100)</td><td>Prefer exit point within an AS. Higher = preferred. NOT sent to eBGP peers.</td></tr>
        <tr><td><strong>MED</strong></td><td>Optional non-transitive</td><td>0–4294967295 (default 0)</td><td>Multi-Exit Discriminator — hint to neighbor AS about preferred entry point. Lower = preferred. Compared only between routes from same AS.</td></tr>
        <tr><td><strong>COMMUNITY</strong></td><td>Optional transitive</td><td>32-bit: ASN:value (e.g., 65001:100)</td><td>Tag routes for policy matching. Common: no-export(65535:65281), no-advertise(65535:65282), blackhole(65535:666)</td></tr>
        <tr><td><strong>ATOMIC-AGGREGATE</strong></td><td>Well-known discretionary</td><td>Flag (present/absent)</td><td>Indicates the route is an aggregate and specific routes exist that were lost during aggregation</td></tr>
        <tr><td><strong>AGGREGATOR</strong></td><td>Optional transitive</td><td>ASN + IP</td><td>Identifies which router created an aggregate route</td></tr>
        <tr><td><strong>ORIGINATOR-ID</strong></td><td>Optional non-transitive</td><td>Router-ID (32-bit)</td><td>Route Reflector: identifies original route source for loop detection</td></tr>
        <tr><td><strong>CLUSTER-LIST</strong></td><td>Optional non-transitive</td><td>List of cluster IDs</td><td>Route Reflector: prevents loops between route reflectors</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════ TAB 4 — BEST-PATH SELECTION ════ -->
<div id="t4" class="tab-pane">
<p class="sep">BGP BEST-PATH SELECTION — THE 13-STEP ALGORITHM</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏆</span><h3>BGP Best-Path Decision Process</h3><span class="tag tag-blue">BEST PATH</span></div>
  <div class="cp-body">
    <p>When BGP receives multiple paths to the same prefix, it selects one "best path" to install in the FIB and advertise to peers. The selection follows a strict ordered list of criteria — evaluated in sequence, stopping at the first differentiating criterion.</p>
<div class="cb"><pre><span class="cm">/* BGP best-path selection — in order (Cisco/FRR) */</span>
<span class="cm">/* Mnemonic: "We Love Oranges As Oranges Mean Pure Refreshment" */</span>

1.  Weight           (Cisco proprietary) — higher preferred. Local to router.
2.  LOCAL-PREF       Higher preferred. Shared within AS.
3.  Locally Originated  Routes originated by this router preferred.
4.  AS-PATH length   Shorter (fewer hops) preferred.
5.  ORIGIN code      IGP(i) < EGP(e) < Incomplete(?)
6.  MED              Lower preferred (only compared within same AS).
7.  eBGP over iBGP   eBGP-learned routes preferred over iBGP.
8.  IGP metric       to NEXT-HOP — lower preferred (closest exit).
9.  Oldest eBGP path If all equal so far — oldest (most stable) preferred.
10. Lowest Router-ID of advertising router.
11. Shortest CLUSTER-LIST length (Route Reflector environments).
12. Lowest neighbour IP address (tie-break).

<span class="cm">/* Verify best path selection */</span>
show ip bgp 10.0.0.0/8          <span class="cm"># show all paths, best marked with ">"</span>
show ip bgp 10.0.0.0/8 bestpath <span class="cm"># show why this path was chosen</span>

<span class="cm">/* Policy knobs to influence best-path */</span>
LOCAL-PREF: control which exit from your AS preferred (inbound traffic)
AS-PATH prepend: make your AS look farther away (discourage inbound traffic on a path)
MED: influence which of your routers a neighbour enters through
Communities: tag routes and have neighbours apply policy based on tags</pre></div>

    <div class="ins"><p>💡 <strong>The most important attributes for enterprise policy:</strong> LOCAL-PREF controls <em>outbound</em> traffic (which exit path your AS uses for a destination). AS-PATH prepending controls <em>inbound</em> traffic (which path remote ASes use to reach you). MED provides a hint to directly connected neighbours about preferred entry points but is often ignored or overridden.</p></div>
  </div>
</div>
</div>


<!-- ════ TAB 5 — ROUTE POLICY ════ -->
<div id="t5" class="tab-pane">
<p class="sep">BGP ROUTE POLICY — FILTERING AND MANIPULATION</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Route Maps and Filtering Tools</h3><span class="tag tag-green">POLICY</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* BGP filtering tools */</span>

1. Prefix lists — match by prefix/length
   ip prefix-list BLOCK-DEFAULT seq 5 deny 0.0.0.0/0
   ip prefix-list ALLOW-ALL    seq 10 permit 0.0.0.0/0 le 32

2. AS-PATH access lists — match by regex on AS-PATH
   ip as-path access-list 1 permit ^65002$    <span class="cm"># only AS 65002</span>
   ip as-path access-list 2 permit ^65002_    <span class="cm"># originated by 65002</span>
   ip as-path access-list 3 deny .*           <span class="cm"># deny all</span>

3. Community lists — match by community value
   ip community-list 1 permit 65001:100

4. Route maps — combine match + set operations
   route-map POLICY permit 10
     match ip address prefix-list MY-PREFIXES
     set local-preference 200
     set community 65001:100 additive
   route-map POLICY deny 20  <span class="cm"># deny everything else</span>

<span class="cm">/* Apply to BGP peer */</span>
router bgp 65001
  neighbor 203.0.113.1 route-map POLICY in   <span class="cm"># filter incoming updates</span>
  neighbor 203.0.113.1 route-map POLICY out  <span class="cm"># filter outgoing updates</span>

<span class="cm">/* AS-PATH prepending — make path look longer to discourage use */</span>
route-map SET-PREPEND permit 10
  set as-path prepend 65001 65001 65001  <span class="cm"># prepend own AS 3 times</span>
<span class="cm"># Result: route appears 3 hops further away on this path</span>

<span class="cm">/* Communities for ISP signaling */</span>
<span class="cm"># Send community 65002:100 to ISP → they set your LOCAL-PREF to 100 (low)</span>
<span class="cm"># Send community 65002:200 → they set LOCAL-PREF to 200 (high = prefer this path)</span>
<span class="cm"># BGP Blackhole community (RFC 7999): 65535:666</span>
<span class="cm"># Most ISPs: if you advertise a /32 with 65535:666, they null-route it → DDoS mitigation</span></pre></div>
  </div>
</div>
</div>


<!-- ════ TAB 6 — BGP SECURITY ════ -->
<div id="t6" class="tab-pane">
<p class="sep">BGP SECURITY — ROUTE HIJACKING, RPKI, AND PROTECTION</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>BGP Attacks — Route Hijacking and Leaks</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attack</th><th>How It Happens</th><th>Impact</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td><strong>Prefix Hijacking</strong></td><td>AS announces a prefix it doesn't own. BGP prefers more-specific prefixes — attacker announces /24 of a /16 they don't own. Their announcement wins globally.</td><td>Traffic for the victim prefix redirected to attacker (interception or blackhole)</td><td>Pakistan Telecom 2008 hijacked YouTube's prefixes for 2 hours</td></tr>
        <tr><td><strong>Route Leak</strong></td><td>AS re-advertises routes it shouldn't — e.g., customer leaks provider's full table to another provider, causing traffic to flow through the customer (sub-optimal or broken)</td><td>Traffic disruption, possible interception</td><td>Cloudflare 2019: AS routing leak from Verizon caused widespread outage</td></tr>
        <tr><td><strong>BGP Session Hijacking</strong></td><td>Attacker spoofs TCP RST to tear down a BGP session, disrupting routing updates</td><td>BGP convergence event, potential route withdrawal causing traffic drops</td><td>RFC 4953 — mitigated by MD5/TCP-AO authentication</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>RPKI — Resource Public Key Infrastructure</h3><span class="tag tag-teal">RPKI</span></div>
  <div class="cp-body">
    <p>RPKI (RFC 6480) is the cryptographic solution to BGP prefix hijacking. IP address holders (using their RIR account) create signed certificates called <strong>Route Origin Authorizations (ROAs)</strong> that state "AS X is authorised to originate prefix P/len". Routers with RPKI-enabled BGP validate incoming routes against the ROA database.</p>
<div class="cb"><pre><span class="cm">/* RPKI Route Origin Validation (ROV) */</span>

ROA: "192.0.2.0/24 may be originated by AS64496, max-length /24"
Signed by: the IP address holder's RIR certificate chain

Router receives BGP update: 192.0.2.0/24 from AS64497
  RPKI check:
    Valid:   prefix+origin matches a ROA → install, prefer
    Invalid: prefix+origin contradicts ROA (wrong AS) → DROP (or low pref)
    Unknown: no ROA exists for this prefix → accept (no info)

<span class="cm">/* Validation states */</span>
Valid:   Route passes RPKI validation — safe to use
Invalid: Route fails RPKI — likely hijack → should be dropped
Unknown: No ROA exists — treat as before RPKI (accept, lower preference)

<span class="cm">/* FRR RPKI config */</span>
rpki
  rpki cache rpki.example.com 3323 preference 1  <span class="cm"># RTR server</span>

router bgp 65001
  bgp bestpath prefix-validate allow-invalid     <span class="cm"># don't drop invalid (log only)</span>
  <span class="cm"># For production: configure route-map to drop invalid routes</span>

route-map FROM-PEER deny 5
  match rpki invalid   <span class="cm"># drop RPKI-invalid routes</span>
route-map FROM-PEER permit 10

<span class="cm">/* Check RPKI status */</span>
show bgp ipv4 unicast 192.0.2.0/24  <span class="cm"># shows "rpki: valid/invalid/not found"</span></pre></div>

    <div class="warn"><p>⚠️ <strong>BGP session authentication.</strong> Always configure MD5 or TCP-AO authentication on BGP sessions to prevent session teardown via spoofed RST packets: <code>neighbor 203.0.113.1 password strongpassword</code>. MD5 has weaknesses but is widely deployed; TCP-AO (RFC 5925) is the modern replacement.</p></div>
  </div>
</div>
</div>


<!-- ════ TAB 7 — LABS ════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>BGP Peering with FRR — eBGP Between Two ASes</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Configure eBGP peering between two Linux VMs running FRR. Advertise prefixes, observe path attributes, and manipulate best-path selection.</p>
    <div class="lab-step"><div class="sn">1</div><div>Set up two VMs: AS65001 (10.1.0.1) and AS65002 (10.1.0.2) on a shared /30 segment. Install FRR on both. Configure eBGP: on AS65001: <code>neighbor 10.1.0.2 remote-as 65002</code>; on AS65002: <code>neighbor 10.1.0.1 remote-as 65001</code>. Verify session reaches Established: <code>show bgp summary</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Advertise a loopback prefix on each side: <code>network 192.0.2.0/24</code> (AS65001) and <code>network 198.51.100.0/24</code> (AS65002). Verify routes are received: <code>show bgp ipv4 unicast</code>. Examine the UPDATE: note AS-PATH, NEXT-HOP, ORIGIN attributes.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test LOCAL-PREF: on AS65001, add a second path via a third router (AS65003). Apply a route-map to set LOCAL-PREF=200 on routes from AS65003 and LOCAL-PREF=100 on routes from AS65002. Verify AS65001 prefers AS65003 for routes it can reach via either.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Test AS-PATH prepending: on AS65001, apply a route-map outbound to AS65002 that prepends your AS three times. Verify AS65002 sees your AS in the path as "65001 65001 65001 65001" and prefers the shorter path via AS65003.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>BGP Route Filtering and Community Tagging</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement prefix-list and community-based filtering. Practice the route policy tools used in production ISP and enterprise BGP configurations.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a prefix-list that accepts only /24 or longer prefixes (reject /8–/23): <code>ip prefix-list ACCEPT-SPECIFICS permit 0.0.0.0/0 ge 24</code>. Apply inbound. Verify: attempt to advertise a /22 from the peer — it should be filtered.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Tag all received routes with a community: route-map that sets community 65001:100 on all routes from AS65002. Apply on inbound. Verify: <code>show bgp ipv4 unicast 198.51.100.0/24</code> shows community value.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Use community for conditional policy: create a route-map that sets LOCAL-PREF=150 for routes with community 65001:100, and LOCAL-PREF=50 for community 65001:200. Advertise two prefixes with different communities from AS65002 and verify AS65001 applies different preferences.</div></div>
  </div>
</div>
</div>


<!-- ════ TAB 8 — CHECKLIST ════ -->
<div id="t8" class="tab-pane">
<p class="sep">M12 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know BGP is a path-vector EGP: carries full AS-PATH, policy-driven, connects ASes on the internet</li>
  <li>Know BGP uses TCP 179 (reliable transport, manually configured peers)</li>
  <li>Know Autonomous System (AS) concept, ASN ranges, private ASNs (64512–65535)</li>
  <li>Know eBGP vs iBGP: different ASes vs same AS; TTL 1 vs 255; AS-PATH modified vs not; NEXT-HOP modified vs not</li>
  <li>Know iBGP split-horizon: routes from iBGP peers NOT re-advertised to other iBGP peers</li>
  <li>Know why full-mesh iBGP is unscalable: N(N-1)/2 sessions</li>
  <li>Know Route Reflectors: one RR re-advertises iBGP routes to all clients; ORIGINATOR-ID and CLUSTER-LIST for loop prevention</li>
  <li>Know the 6 BGP FSM states: Idle, Connect, Active, OpenSent, OpenConfirm, Established</li>
  <li>Know 5 BGP message types: OPEN, UPDATE, KEEPALIVE, NOTIFICATION, ROUTE-REFRESH</li>
  <li>Know mandatory BGP attributes: ORIGIN (i/e/?), AS-PATH, NEXT-HOP</li>
  <li>Know LOCAL-PREF: higher preferred, within AS only, controls outbound traffic exit</li>
  <li>Know MED: lower preferred, hint to neighbor AS about preferred entry, only compared within same AS</li>
  <li>Know COMMUNITY: 32-bit tags, used for policy matching and signaling between ASes</li>
  <li>Know well-known communities: no-export(65535:65281), no-advertise(65535:65282), blackhole(65535:666)</li>
  <li>Can recall BGP best-path selection order: Weight → LOCAL-PREF → Locally Originated → AS-PATH length → ORIGIN → MED → eBGP over iBGP → IGP metric → Router-ID</li>
  <li>Know how to influence inbound traffic: LOCAL-PREF (within AS), AS-PATH prepending (to other ASes)</li>
  <li>Know route-map components: match conditions (prefix-list, community, as-path) + set actions (local-pref, community, prepend)</li>
  <li>Know BGP prefix hijacking: attacker announces specific prefix it doesn't own; more-specific wins globally</li>
  <li>Know RPKI and ROAs: cryptographic proof that ASN X can originate prefix P; states = Valid/Invalid/Unknown</li>
  <li>Know BGP authentication: MD5 or TCP-AO prevents session teardown via spoofed RST</li>
  <li>Completed Lab 1: configured eBGP between two FRR instances, tested LOCAL-PREF and AS-PATH prepending</li>
  <li>Completed Lab 2: implemented prefix-list filtering and community-based policy</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M13 - MPLS, VxLAN, GRE and Tunneling</strong> — the final Phase 3 module covering overlay networks and tunnelling mechanisms critical to modern data centres and VPN deployments.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/networking-mastery/m11-ospf/' | relative_url }}">← M11 OSPF</a>
  <a href="{{ '/learning/networking-mastery/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m13-tunneling/' | relative_url }}">Next: M13 - Tunneling →</a>
</div>

<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
