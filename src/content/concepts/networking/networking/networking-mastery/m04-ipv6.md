---
title: "M04 - IPv6"
description: "NETWORKING MASTERY · PHASE 1 · MODULE 04 · WEEK 3 🔵 IPv6 128-bit addressing · Header format · Address types · NDP · SLAAC · Dual-stack · Transition mechanisms Beginner →…"
domain: networking
track: networking-mastery
order: 4
ownHeader: true
url: /learning/networking-mastery/m04-ipv6/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#5b3a8c 75%,#3a1a6c 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c0a8f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#dcc8f8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ecdcff}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#c0a8f0;border-bottom-color:#c0a8f0}
.tab-pane{display:none}
.tab-pane.active{display:block}

/* Concept panels */
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

/* Panel colour variants */
.p-blue  .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue  .cp-hdr{background:#0d2030}
.p-teal  .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal  .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green  .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green  .cp-hdr{background:#0a2018}
.p-red    .cp-hdr{background:#faeaea}[data-theme=dark] .p-red    .cp-hdr{background:#2a0808}
.p-amber  .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber  .cp-hdr{background:#2a1e00}

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}

/* Code blocks */
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #5b3a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dcc8f8;white-space:pre}
.cm{color:#6a5a80}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#f0ecfc;border:1.5px solid #5b3a8c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e1028;border-color:#7060a8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3a1a6c}
[data-theme=dark] .ins strong{color:#c0a8f0}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0a2420;border-color:#2a9a8e}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#0e5248}
[data-theme=dark] .note strong{color:#5dd6c8}

/* Analogy */
.analogy{background:linear-gradient(135deg,#f5f0ff,#ede8fc);border:1.5px solid #b090e0;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#180828,#1c1030);border-color:#6050a0}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#3a1a6c;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#c0a8f0}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* IPv6 address visual */
.v6-addr{display:flex;gap:2px;align-items:stretch;margin:.8rem 0;flex-wrap:wrap;overflow-x:auto}
.v6-group{
  border-radius:6px;padding:7px 10px;text-align:center;
  font-family:monospace;font-size:.9rem;font-weight:700;
  border:1.5px solid;min-width:52px;
}
.v6-sep{display:flex;align-items:center;font-size:1.2rem;color:var(--light-text,#aaa);padding:0 1px;font-family:monospace}
.v6-lbl{font-size:.65rem;font-family:monospace;color:var(--light-text,#666);margin-top:3px;text-align:center}
.v6-col{display:flex;flex-direction:column;align-items:center}

/* Header diagram */
.hdr-diagram{margin:1rem 0;overflow-x:auto}
.hdr-row{display:flex;gap:2px;min-width:580px;margin-bottom:3px;align-items:stretch}
.hdr-label{font-size:.7rem;font-family:monospace;min-width:76px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:4px}
.hf{border-radius:5px;padding:7px 5px;font-size:.7rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.hf-ver{background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.hf-tc {background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.hf-fl {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-pl {background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.hf-nh {background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.hf-hl {background:#faeee4;border-color:#e8b090;color:#6a2800}
.hf-sa {background:#f0ecfc;border-color:#b090e0;color:#3a1a6c}
.hf-da {background:#f0ecfc;border-color:#b090e0;color:#3a1a6c}
.hf-bytes{font-size:.62rem;font-weight:400;opacity:.8;margin-top:2px}

/* Addr type table */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#5b3a8c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#5b3a8c}

/* Compare table */
.cmp-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.cmp-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.cmp-table td{padding:.5rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.cmp-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.cmp-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a3a5c}
.good{color:#1a5a1a;font-weight:600}
.bad{color:#6c1a1a;font-weight:600}

/* NDP flow */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#5b3a8c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#c0a8f0;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Dual-stack diagram */
.ds-diagram{display:flex;flex-direction:column;gap:6px;margin:1rem 0;padding:1rem;background:var(--bg-color,#f8f8f8);border-radius:10px;border:1.5px solid var(--border-color,#e0e0e0)}
.ds-row{display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap}
.ds-box{border-radius:8px;padding:.5rem .9rem;text-align:center;font-size:.8rem;font-weight:600;border:1.5px solid;min-width:90px}
.ds-arrow{font-size:1rem;color:var(--light-text,#888)}
.ds-label{font-size:.68rem;font-family:monospace;color:var(--light-text,#666);text-align:center;margin-top:2px}

/* Lab box */
.lab-box{border:2px solid #5b3a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#5b3a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#5b3a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#5b3a8c;margin-top:-.05rem}

/* Nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 1 · MODULE 04 · WEEK 3</div>
  <div class="mod-title">🔵 IPv6</div>
  <div class="mod-subtitle">128-bit addressing · Header format · Address types · NDP · SLAAC · Dual-stack · Transition mechanisms</div>
  <div class="mod-pills">
<span class="mod-pill">Beginner → Intermediate</span>
<span class="mod-pill">Prerequisite: M03 IPv4</span>
<span class="mod-pill">RFC 8200</span>
<span class="mod-pill">128-bit addresses</span>
<span class="mod-pill">No broadcast</span>
<span class="mod-pill">2 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Why IPv6?</button>
  <button class="tab-btn" onclick="vt(event,'t1')">IPv6 Header</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Address Format</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Address Types</button>
  <button class="tab-btn" onclick="vt(event,'t4')">NDP and ICMPv6</button>
  <button class="tab-btn" onclick="vt(event,'t5')">SLAAC and DHCPv6</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Dual-Stack and Transition</button>
  <button class="tab-btn" onclick="vt(event,'t7')">IPv4 vs IPv6 Comparison</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- ════════════ TAB 0 — WHY IPv6 ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THE ADDRESS EXHAUSTION PROBLEM AND THE IPv6 SOLUTION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📉</span><h3>IPv4 Address Exhaustion</h3><span class="tag tag-purple">MOTIVATION</span></div>
  <div class="cp-body">
<p>IPv4 uses 32-bit addresses — providing a theoretical maximum of <strong>2³² = 4,294,967,296</strong> (about 4.3 billion) unique addresses. When IPv4 was designed in 1981, this seemed enormous. But the explosive growth of the internet — billions of smartphones, IoT devices, cloud servers, home routers — consumed this space far faster than anticipated.</p>
<p><strong>IANA (the global IP address authority) exhausted its IPv4 pool on 3 February 2011.</strong> Regional registries ran out of free allocations between 2011–2019. Today, obtaining new public IPv4 addresses requires buying them on the secondary market at premium prices.</p>
<p>Several stopgap measures delayed the crisis:</p>
<ul>
<li><strong>CIDR</strong> — replaced wasteful classful allocation, made address usage more efficient</li>
<li><strong>RFC 1918 private addresses + NAT</strong> — allowed millions of devices to share a single public IP. A home router with one public IP can serve 100+ internal devices. This is why your home network uses <code>192.168.x.x</code></li>
<li><strong>CGN (Carrier-Grade NAT)</strong> — ISPs now put entire neighbourhoods behind a single public IPv4 address</li>
</ul>
<p>NAT solved the exhaustion problem temporarily, but at a cost: it breaks end-to-end connectivity, complicates application protocols (FTP, SIP, WebRTC need ALGs to work through NAT), and adds latency. IPv6 eliminates NAT by giving every device a globally unique address.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>IPv6 — The Long-Term Solution</h3><span class="tag tag-blue">SOLUTION</span></div>
  <div class="cp-body">
<p>IPv6 (Internet Protocol version 6) was standardised in RFC 2460 (1998), updated by RFC 8200 (2017). It solves address exhaustion and simultaneously redesigns several IPv4 pain points:</p>
<div class="two-col">
<div>
<h4>What IPv6 Fixes</h4>
<ul>
<li><strong>128-bit addresses</strong> — 2¹²⁸ ≈ 3.4 × 10³⁸ unique addresses. Enough to give every atom on Earth its own IP address</li>
<li><strong>No broadcast</strong> — IPv4 broadcast is replaced with targeted multicast, reducing noise on large networks</li>
<li><strong>Built-in security</strong> — IPsec support is mandatory in the specification (optional in IPv4)</li>
<li><strong>Simplified header</strong> — fixed 40-byte header, no checksum, no fragmentation in transit, cleaner extension header chain</li>
<li><strong>Stateless autoconfiguration (SLAAC)</strong> — devices can configure their own addresses without a DHCP server</li>
<li><strong>No NAT required</strong> — every device gets a globally routable address</li>
</ul>
</div>
<div>
<h4>IPv6 Adoption Today</h4>
<ul>
<li>Google reports ~45% of global traffic over IPv6 (2024)</li>
<li>Mobile networks (Jio, T-Mobile, AT&T) are predominantly IPv6-only internally</li>
<li>All major cloud providers (AWS, GCP, Azure) fully support IPv6</li>
<li>Most modern OSes (Linux, Windows, macOS, Android, iOS) prefer IPv6 when available</li>
<li>For NGFW development, IPv6 support is not optional — your firewall must handle both</li>
</ul>
</div>
</div>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">📏 Analogy — Street Addresses</div>
  <p>IPv4 is like a city with 4.3 billion street addresses that is now completely full — every address is taken. To fit more people, residents are crammed into apartment buildings (NAT) where many people share one address and are distinguished by their apartment number (port). IPv6 is like being given an entirely new planet with 340 undecillion addresses — so vast that every grain of sand on Earth gets its own unique address, with quintillions to spare. No apartments needed: every person (device) gets their own unique address.</p>
</div>
</div>
<!-- ════════════ TAB 1 — IPv6 HEADER ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">IPv6 HEADER — 40 BYTES FIXED, SIMPLER THAN IPv4</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📦</span><h3>IPv6 Header Layout</h3><span class="tag tag-purple">HEADER FORMAT</span></div>
  <div class="cp-body">
<p>The IPv6 header is always exactly <strong>40 bytes</strong> — fixed, no options, no IHL field. This simplicity is intentional: routers can process it faster because they always know exactly where the header ends. IPv4 options (rare but requiring variable-length parsing) are replaced by a clean <strong>extension header chain</strong>.</p>
  </div>
</div>
<div class="hdr-diagram">
  <div class="hdr-row">
<div class="hdr-label">Row 1</div>
<div class="hf hf-ver" style="flex:.5">Ver<div class="hf-bytes">4 bits = 6</div></div>
<div class="hf hf-tc"  style="flex:.8">Traffic Class<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-fl"  style="flex:2.7">Flow Label<div class="hf-bytes">20 bits</div></div>
  </div>
  <div class="hdr-row">
<div class="hdr-label">Row 2</div>
<div class="hf hf-pl" style="flex:2">Payload Length<div class="hf-bytes">16 bits</div></div>
<div class="hf hf-nh" style="flex:1">Next Header<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-hl" style="flex:1">Hop Limit<div class="hf-bytes">8 bits</div></div>
  </div>
  <div class="hdr-row">
<div class="hdr-label">Rows 3–6</div>
<div class="hf hf-sa" style="flex:4">Source IPv6 Address<div class="hf-bytes">128 bits — 16 bytes</div></div>
  </div>
  <div class="hdr-row">
<div class="hdr-label">Rows 7–10</div>
<div class="hf hf-da" style="flex:4">Destination IPv6 Address<div class="hf-bytes">128 bits — 16 bytes</div></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Every Field Explained</h3><span class="tag tag-blue">FIELD REFERENCE</span></div>
  <div class="cp-body">
<h4>Version (4 bits) = 0110 = 6</h4>
<p>Always 6 for IPv6. Receivers check this first to know which IP version to process. Same position as IPv4's Version field — allows a parser to distinguish v4 from v6 without any other context.</p>
<h4>Traffic Class (8 bits)</h4>
<p>Equivalent to IPv4's DSCP/TOS field. The upper 6 bits are DSCP for QoS marking; the lower 2 bits are ECN. Same semantics as IPv4 — allows routers to prioritise packets based on service class. Your NGFW policy engine uses this for QoS marking.</p>
<h4>Flow Label (20 bits) — NEW in IPv6</h4>
<p>A 20-bit value identifying a specific flow (sequence of packets from the same source to the same destination, e.g., a single TCP connection or video stream). Routers can use it for <strong>fast-path flow-based forwarding</strong> without inspecting the full address pair on every packet. This is particularly valuable for ECMP (Equal-Cost Multi-Path) load balancing — all packets of the same flow get the same hash → same path → in-order delivery.</p>
<p>For your DPDK/VPP work: the Flow Label is used in RSS (Receive Side Scaling) hash computation to distribute flows across worker threads.</p>
<h4>Payload Length (16 bits)</h4>
<p>Length of everything after the 40-byte fixed header — extension headers + upper-layer data. Unlike IPv4's Total Length (which included the header), Payload Length excludes the fixed header. Maximum: 65,535 bytes. For Jumbograms (packets >65,535 bytes), this is set to 0 and a Jumbo Payload option in an extension header carries the actual length.</p>
<h4>Next Header (8 bits) — Replaces IPv4 Protocol field</h4>
<p>Identifies what follows the fixed IPv6 header. Uses the same protocol number values as IPv4's Protocol field, plus new values for extension headers:</p>
<ul>
<li><code>6</code> — TCP (directly follows)</li>
<li><code>17</code> — UDP (directly follows)</li>
<li><code>58</code> — ICMPv6 (directly follows)</li>
<li><code>43</code> — Routing extension header follows</li>
<li><code>44</code> — Fragment extension header follows</li>
<li><code>0</code>  — Hop-by-Hop Options header follows</li>
<li><code>59</code> — No next header (empty payload)</li>
<li><code>50</code> — ESP (IPsec, directly follows)</li>
</ul>
<p>Extension headers form a <strong>chain</strong>: each extension header has its own Next Header field pointing to the next. The last in the chain points to the actual L4 protocol (TCP=6, UDP=17).</p>
<h4>Hop Limit (8 bits) — IPv4's TTL, renamed</h4>
<p>Same semantics as IPv4 TTL: decremented by 1 at each router hop, packet discarded when it reaches 0. Renamed "Hop Limit" because it is now accurately named — it was never a time limit, always a hop count.</p>
<h4>Source and Destination Addresses (128 bits each = 16 bytes each)</h4>
<p>The IPv6 addresses. At 16 bytes each, they dominate the header — 32 of the 40 bytes are just addresses. This is the cost of the larger address space.</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Extension Headers — Replacing IPv4 Options</h3><span class="tag tag-teal">EXTENSION HEADERS</span></div>
  <div class="cp-body">
<p>IPv4 had an Options field in the main header — complex, variable-length, required all routers to check it. IPv6 replaces this with a cleaner chain of extension headers that most routers skip entirely (only the destination processes most of them):</p>
<table class="t-table">
<thead><tr><th>Extension Header</th><th>Next Header Value</th><th>Purpose</th><th>Processed by</th></tr></thead>
<tbody>
<tr><td>Hop-by-Hop Options</td><td><code>0</code></td><td>Options every router must read (rare — e.g., Router Alert for RSVP)</td><td>Every router</td></tr>
<tr><td>Destination Options</td><td><code>60</code></td><td>Options for the destination host only</td><td>Destination only</td></tr>
<tr><td>Routing Header</td><td><code>43</code></td><td>Loose/strict source routing — list of intermediate nodes</td><td>Each listed node</td></tr>
<tr><td>Fragment Header</td><td><code>44</code></td><td>Fragmentation info (IPv6 only fragments at source)</td><td>Destination only</td></tr>
<tr><td>Auth Header (AH)</td><td><code>51</code></td><td>IPsec authentication</td><td>Destination only</td></tr>
<tr><td>ESP Header</td><td><code>50</code></td><td>IPsec encryption</td><td>Destination only</td></tr>
</tbody>
</table>
<div class="ins"><p>💡 <strong>Key difference from IPv4:</strong> In IPv6, <strong>routers do not fragment packets</strong>. If a packet is too large for a link, the router drops it and sends ICMPv6 "Packet Too Big" (Type 2) back to the source. Only the source can fragment, using the Fragment extension header. This puts fragmentation complexity at endpoints where it belongs, keeping routers fast.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 2 — ADDRESS FORMAT ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">IPv6 ADDRESS FORMAT — 128 BITS, 8 GROUPS OF 16 BITS</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>IPv6 Address Notation</h3><span class="tag tag-purple">FORMAT</span></div>
  <div class="cp-body">
<p>An IPv6 address is 128 bits written as <strong>8 groups of 4 hexadecimal digits</strong>, separated by colons. Each group represents 16 bits (2 bytes):</p>
<div style="text-align:center;margin:1rem 0">
<div class="v6-addr" style="justify-content:center">
<div class="v6-col"><div class="v6-group" style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c">2001</div><div class="v6-lbl">bits 0–15</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c">0db8</div><div class="v6-lbl">bits 16–31</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c">85a3</div><div class="v6-lbl">bits 32–47</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c">0000</div><div class="v6-lbl">bits 48–63</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">0000</div><div class="v6-lbl">bits 64–79</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">8a2e</div><div class="v6-lbl">bits 80–95</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a">0370</div><div class="v6-lbl">bits 96–111</div></div>
<div class="v6-sep">:</div>
<div class="v6-col"><div class="v6-group" style="background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a">7334</div><div class="v6-lbl">bits 112–127</div></div>
</div>
<div style="font-size:.75rem;font-family:monospace;color:var(--light-text,#666);margin-top:4px">Full address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334</div>
</div>
<h4>Abbreviation Rules (RFC 5952)</h4>
<p>IPv6 addresses are long — two abbreviation rules make them manageable:</p>
<p><strong>Rule 1 — Drop leading zeros within each group:</strong></p>
<ul>
<li><code>0db8</code> → <code>db8</code></li>
<li><code>0000</code> → <code>0</code></li>
<li><code>0001</code> → <code>1</code></li>
</ul>
<p><strong>Rule 2 — Replace longest consecutive run of all-zero groups with <code>::</code> (only once per address):</strong></p>



```yaml
/* Full notation */
2001:0db8:85a3:0000:0000:8a2e:0370:7334

/* Step 1: Drop leading zeros in each group */
2001:db8:85a3:0:0:8a2e:370:7334

/* Step 2: Compress the run of zeros (0:0) with :: */
2001:db8:85a3::8a2e:370:7334  ← final compressed form

/* More examples */
fe80:0000:0000:0000:0204:61ff:fe9d:f156
→  fe80::204:61ff:fe9d:f156           # 4 consecutive zero groups compressed

0000:0000:0000:0000:0000:0000:0000:0001
→  ::1                                 # loopback address

0000:0000:0000:0000:0000:0000:0000:0000
→  ::                                  # unspecified address

/* :: can only be used ONCE per address */
2001:db8::1:0:0:1   # valid — one :: compresses middle zeros
2001::db8::1        # INVALID — two :: is ambiguous

/* Prefix notation — same as IPv4 CIDR */
2001:db8::/32       # network prefix /32 bits
fe80::/10           # link-local prefix
2001:db8::1/128     # single host (/128 = one address)
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>IPv6 in C — Structures and Functions</h3><span class="tag tag-blue">CODE</span></div>
  <div class="cp-body">


```cpp
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>

/* IPv6 address structure: 16 bytes = 128 bits */
struct in6_addr addr;

/* Parse a string into binary */
inet_pton(AF_INET6, "2001:db8::1", &addr);

/* Print binary as string */
char buf[INET6_ADDRSTRLEN];   /* 46 bytes: enough for any IPv6 string */
inet_ntop(AF_INET6, &addr, buf, sizeof(buf));
printf("%s\n", buf);           /* prints: 2001:db8::1 */

/* Access raw bytes (useful for masking) */
uint8_t *bytes = addr.s6_addr;  /* 16-byte array */
printf("First byte: %02x\n", bytes[0]);

/* Check if address is in a prefix (e.g., fe80::/10 link-local) */
int is_link_local(struct in6_addr *a) {
    /* fe80::/10 — first 10 bits = 1111 1110 10 */
    return (a->s6_addr[0] == 0xfe) && ((a->s6_addr[1] & 0xc0) == 0x80);
}

/* sockaddr for IPv6 connections */
struct sockaddr_in6 sa6 = {0};
sa6.sin6_family = AF_INET6;
sa6.sin6_port   = htons(80);
inet_pton(AF_INET6, "2001:db8::1", &sa6.sin6_addr);
connect(sock, (struct sockaddr *)&sa6, sizeof(sa6));
```


  </div>
</div>
</div>
<!-- ════════════ TAB 3 — ADDRESS TYPES ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">IPv6 ADDRESS TYPES — NO BROADCAST, THREE MAIN TYPES</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🗂️</span><h3>Three Address Types — Unicast, Multicast, Anycast</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
<p>IPv6 eliminates broadcast entirely. The three address types are:</p>
<ul>
<li><strong>Unicast</strong> — one sender to one specific receiver. The majority of IPv6 traffic.</li>
<li><strong>Multicast</strong> — one sender to a group of receivers (all addresses starting <code>FF</code>). Replaces broadcast for all use cases.</li>
<li><strong>Anycast</strong> — one sender to the nearest of multiple receivers sharing the same address. Used for DNS root servers, CDN edge nodes.</li>
</ul>
<p><strong>There is no broadcast in IPv6.</strong> What used to be broadcast (e.g., ARP requests) is now done with targeted multicast (NDP Solicited-Node multicast). This is one of the most important architectural improvements.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Unicast Address Types — Know Each One</h3><span class="tag tag-blue">UNICAST</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Type</th><th>Prefix</th><th>Example</th><th>Scope</th><th>Use</th></tr></thead>
<tbody>
<tr><td><strong>Global Unicast (GUA)</strong></td><td><code>2000::/3</code></td><td><code>2001:db8::1</code></td><td>Internet-wide</td><td>Publicly routable addresses — the IPv6 equivalent of public IPv4</td></tr>
<tr><td><strong>Link-Local</strong></td><td><code>fe80::/10</code></td><td><code>fe80::1</code></td><td>Single link only</td><td>Automatically configured on every IPv6 interface. Used for NDP, router discovery. Never routed beyond a single link.</td></tr>
<tr><td><strong>Unique Local (ULA)</strong></td><td><code>fc00::/7</code> (usually <code>fd00::/8</code>)</td><td><code>fd00::1</code></td><td>Organisation-wide</td><td>IPv6's equivalent of RFC 1918 private addresses. Not routable on internet. Used for internal networks.</td></tr>
<tr><td><strong>Loopback</strong></td><td><code>::1/128</code></td><td><code>::1</code></td><td>Host-local</td><td>Equivalent to 127.0.0.1. Used for local host communication.</td></tr>
<tr><td><strong>Unspecified</strong></td><td><code>::/128</code></td><td><code>::</code></td><td>N/A</td><td>Equivalent to 0.0.0.0. Used before address assignment.</td></tr>
<tr><td><strong>IPv4-Mapped</strong></td><td><code>::ffff:0:0/96</code></td><td><code>::ffff:192.0.2.1</code></td><td>N/A</td><td>Represents an IPv4 address in IPv6 notation. Used by dual-stack APIs.</td></tr>
</tbody>
</table>
<h4>Global Unicast Address Structure</h4>
<p>A GUA is divided into three parts:</p>
<div class="cb"><pre><span class="cm">/* Global Unicast Address: 2001:db8:1234:5678:abcd:ef01:2345:6789 */</span>
 
|←── Global Routing Prefix ──→|←─ Subnet ID ─→|←───── Interface ID ─────→|
  2001 : 0db8 : 1234            : 5678            : abcd : ef01 : 2345 : 6789
  (assigned by ISP/RIR)          (you define)       (interface-specific)
  typically 48 bits               16 bits            64 bits
 
<span class="cm">/* The /64 boundary is the standard interface prefix */</span>
<span class="cm">/* Network: 2001:db8:1234:5678::/64 */</span>
<span class="cm">/* Host:    anything in the lower 64 bits */</span></pre></div>
<div class="ins"><p>💡 <strong>Why /64 everywhere?</strong> The 64-bit interface ID boundary is standard in IPv6 for several reasons: SLAAC (address autoconfiguration) uses a 64-bit EUI-64 derived from the MAC address as the interface ID; NDP Solicited-Node multicast uses the lower 24 bits of the interface ID; and /64 subnets give enough space that you'll never run out of host addresses within a subnet.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📣</span><h3>Multicast Addresses — Replacing Broadcast</h3><span class="tag tag-teal">MULTICAST</span></div>
  <div class="cp-body">
<p>All IPv6 multicast addresses start with <code>FF</code>. The second byte encodes the <strong>lifetime</strong> (permanent vs transient) and <strong>scope</strong> (how far the multicast travels):</p>
<table class="t-table">
<thead><tr><th>Address</th><th>Name</th><th>Replaces (IPv4)</th><th>Used by</th></tr></thead>
<tbody>
<tr><td><code>ff02::1</code></td><td>All-nodes (link-local)</td><td>255.255.255.255 broadcast</td><td>General link-local broadcast equivalent</td></tr>
<tr><td><code>ff02::2</code></td><td>All-routers (link-local)</td><td>224.0.0.2</td><td>Router discovery, DHCPv6 relay</td></tr>
<tr><td><code>ff02::5</code></td><td>OSPFv3 All-routers</td><td>224.0.0.5</td><td>OSPFv3 hello packets</td></tr>
<tr><td><code>ff02::6</code></td><td>OSPFv3 DR/BDR</td><td>224.0.0.6</td><td>OSPFv3 DR/BDR</td></tr>
<tr><td><code>ff02::1:ff00:0/104</code></td><td>Solicited-Node Multicast</td><td>ARP broadcast</td><td>NDP — neighbour address resolution</td></tr>
<tr><td><code>ff05::2</code></td><td>All-routers (site-local)</td><td>N/A</td><td>Router discovery across site</td></tr>
</tbody>
</table>
<h4>Solicited-Node Multicast — The ARP Replacement</h4>
<p>This is how IPv6 avoids broadcast for address resolution. Each interface automatically joins a Solicited-Node multicast group derived from its own IPv6 address:</p>


```yaml
/* Solicited-Node Multicast formula */
Prefix: ff02::1:ff00:0/104
Last 24 bits: lower 24 bits of the interface's IPv6 address

/* Example */
Interface IPv6: 2001:db8::abcd:ef01
Lower 24 bits:  cd:ef:01
Solicited-Node: ff02::1:ffcd:ef01

/* Why this is better than ARP broadcast */
ARP: sent to FF:FF:FF:FF:FF:FF — EVERY device on the segment must wake up and process it
NDP: sent to ff02::1:ffcd:ef01 multicast — only devices whose address ends in cd:ef:01 process it
     (statistically, only 1–2 devices on any given segment share the same lower 24 bits)
     Much lower CPU overhead on large segments
```


  </div>
</div>
</div>
<!-- ════════════ TAB 4 — NDP AND ICMPv6 ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">NDP — NEIGHBOUR DISCOVERY PROTOCOL (REPLACES ARP + MORE)</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>NDP — IPv6's Supercharged ARP</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
<p>Neighbour Discovery Protocol (NDP, RFC 4861) replaces ARP and adds additional functions that required separate protocols in IPv4. It runs over ICMPv6 (Type 133–137) and uses multicast instead of broadcast.</p>
<p>NDP provides five functions:</p>
<ul>
<li><strong>Address Resolution</strong> — maps IPv6 address to MAC address (replaces ARP)</li>
<li><strong>Router Discovery</strong> — hosts find routers and their prefixes automatically</li>
<li><strong>Prefix Discovery</strong> — hosts learn the network prefix for SLAAC autoconfiguration</li>
<li><strong>Redirect</strong> — routers inform hosts of better first-hop routes</li>
<li><strong>Duplicate Address Detection (DAD)</strong> — verifies an address is unique before using it</li>
</ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>NDP Message Types</h3><span class="tag tag-blue">MESSAGES</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>ICMPv6 Type</th><th>Name</th><th>Direction</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td><code>133</code></td><td>Router Solicitation (RS)</td><td>Host → All-routers (ff02::2)</td><td>Host asks "any routers out there?" on startup</td></tr>
<tr><td><code>134</code></td><td>Router Advertisement (RA)</td><td>Router → All-nodes (ff02::1)</td><td>Router announces prefix, MTU, default gateway, flags</td></tr>
<tr><td><code>135</code></td><td>Neighbour Solicitation (NS)</td><td>Host → Solicited-Node multicast</td><td>Address resolution (like ARP request) + DAD</td></tr>
<tr><td><code>136</code></td><td>Neighbour Advertisement (NA)</td><td>Host → Requester (unicast)</td><td>Address resolution reply (like ARP reply)</td></tr>
<tr><td><code>137</code></td><td>Redirect</td><td>Router → Host</td><td>Better route available via different next-hop</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>NDP Address Resolution — Step by Step</h3><span class="tag tag-teal">PROCESS</span></div>
  <div class="cp-body">
<p>Scenario: Host A (<code>2001:db8::1</code>) wants to send a packet to Host B (<code>2001:db8::2</code>). It doesn't know B's MAC address.</p>
<div class="flow-list">
<div class="fl-step" data-n="1" style="--sc:#5b3a8c">
<div>
<div class="fl-title">A checks its Neighbour Cache</div>
<div class="fl-detail">Linux maintains a Neighbour Cache (equivalent to IPv4 ARP cache) mapping IPv6 → MAC. If a valid entry for 2001:db8::2 exists, skip to step 5.</div>
<div class="fl-code">ip -6 neigh show</div>
</div>
</div>
<div class="fl-step" data-n="2" style="--sc:#5b3a8c">
<div>
<div class="fl-title">A computes B's Solicited-Node Multicast address</div>
<div class="fl-detail">B's address ends in <code>00:00:02</code> → Solicited-Node = <code>ff02::1:ff00:0002</code>. The Ethernet multicast MAC for this is derived as <code>33:33:ff:00:00:02</code> (IPv6 multicast MAC prefix is 33:33 followed by the last 4 bytes of the multicast group).</div>
</div>
</div>
<div class="fl-step" data-n="3" style="--sc:#5b3a8c">
<div>
<div class="fl-title">A sends Neighbour Solicitation (NS)</div>
<div class="fl-detail">ICMPv6 Type 135: Target = 2001:db8::2. Source link-layer option = A's MAC. Sent to Solicited-Node multicast (not broadcast!). Only B — and any other device whose address ends in 00:02 — receives this.</div>
<div class="fl-code">ICMPv6 NS: src=2001:db8::1 dst=ff02::1:ff00:2 target=2001:db8::2</div>
</div>
</div>
<div class="fl-step" data-n="4" style="--sc:#5b3a8c">
<div>
<div class="fl-title">B sends Neighbour Advertisement (NA)</div>
<div class="fl-detail">ICMPv6 Type 136: Target = 2001:db8::2, Target link-layer option = B's MAC. Sent directly to A's unicast address (not multicast).</div>
<div class="fl-code">ICMPv6 NA: src=2001:db8::2 dst=2001:db8::1 MAC=bb:bb:bb:bb:bb:bb</div>
</div>
</div>
<div class="fl-step" data-n="5" style="--sc:#5b3a8c">
<div>
<div class="fl-title">A caches the mapping and sends the original packet</div>
<div class="fl-detail">Neighbour cache entry: 2001:db8::2 → bb:bb:bb:bb:bb:bb (REACHABLE). All subsequent packets use this cache entry until it expires (default 30 seconds before reachability probe).</div>
</div>
</div>
</div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Duplicate Address Detection (DAD)</h3><span class="tag tag-orange">DAD</span></div>
  <div class="cp-body">
<p>Before using a new IPv6 address, a host <strong>must verify it's unique</strong> on the link via DAD. This is especially important for SLAAC-derived addresses (two devices could theoretically derive the same EUI-64 from different MAC addresses, though this is extremely rare).</p>



```python
/* DAD process */
1. Host tentatively assigns the address (marks as TENTATIVE in neighbour cache)
2. Host sends NS with:
   - Source IP = :: (unspecified — not yet using the new address)
   - Destination = Solicited-Node multicast of the tentative address
   - Target = the tentative address itself
3. If no NA is received within RetransTimer (1 second default):
   → Address is unique → set to PREFERRED state → use it
4. If an NA IS received (someone already has this address):
   → Address conflict detected → DAD fails
   → Interface stays without this address
   → Kernel logs: "IPv6: DAD failed for address 2001:db8::1"

/* On Linux you can observe DAD: */
$ ip -6 addr show dev eth0
   inet6 2001:db8::1/64 scope global tentative  ← DAD in progress
   inet6 2001:db8::1/64 scope global            ← DAD passed, address active
```


  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Router Advertisement — The Key to Autoconfiguration</h3><span class="tag tag-green">RA MESSAGE</span></div>
  <div class="cp-body">
<p>Router Advertisements (ICMPv6 Type 134) are sent periodically by routers to <code>ff02::1</code> (all-nodes) and contain everything a host needs to configure itself:</p>


```python
/* Key fields in a Router Advertisement */
Cur Hop Limit:    64        # recommended Hop Limit for outgoing packets
Flags:            M=0 O=0  # M=1: use DHCPv6 for address; O=1: use DHCPv6 for options
Router Lifetime:  1800s     # how long to use this router as default gateway
Reachable Time:   0         # time to assume neighbour is reachable after last confirmation

Prefix Information Option:
  Prefix:         2001:db8::/64
  Valid Lifetime: 2592000s  # 30 days
  Preferred Lifetime: 604800s # 7 days
  L flag = 1                # prefix is on-link
  A flag = 1                # use for SLAAC autoconfiguration

MTU Option:       1500      # link MTU
Source Link-Layer: aa:bb:cc:dd:ee:ff  # router's MAC

# Receiving host uses this to:
# 1. Know it's on prefix 2001:db8::/64
# 2. Auto-configure its own address (SLAAC)
# 3. Set the router as default gateway (fe80::router_mac)
```


  </div>
</div>
</div>
<!-- ════════════ TAB 5 — SLAAC AND DHCPv6 ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">SLAAC AND DHCPv6 — ADDRESS AUTOCONFIGURATION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>SLAAC — Stateless Address Autoconfiguration</h3><span class="tag tag-purple">SLAAC</span></div>
  <div class="cp-body">
<p>SLAAC (RFC 4862) is IPv6's mechanism for devices to configure their own IP address <strong>without any server</strong>. A device with just a MAC address and a connected link can generate a globally routable IPv6 address in seconds — no DHCP server, no manual configuration.</p>
<p><strong>SLAAC process:</strong></p>
<div class="flow-list">
<div class="fl-step" data-n="1" style="--sc:#5b3a8c">
<div>
<div class="fl-title">Interface comes up — auto-configure Link-Local address</div>
<div class="fl-detail">Every IPv6 interface automatically generates a Link-Local address (fe80::/10) using EUI-64 from the MAC address (see below). This address is used for NDP before any global address is assigned.</div>
<div class="fl-code">fe80::[EUI-64 derived from MAC]</div>
</div>
</div>
<div class="fl-step" data-n="2" style="--sc:#5b3a8c">
<div>
<div class="fl-title">DAD on Link-Local address</div>
<div class="fl-detail">Sends NS with src=:: to the Solicited-Node multicast of the tentative fe80 address. If no conflict: Link-Local address becomes PREFERRED.</div>
</div>
</div>
<div class="fl-step" data-n="3" style="--sc:#5b3a8c">
<div>
<div class="fl-title">Send Router Solicitation</div>
<div class="fl-detail">ICMPv6 Type 133 sent to ff02::2 (all-routers): "Any routers? Please send me a Router Advertisement."</div>
<div class="fl-code">RS: src=fe80::[eui64] dst=ff02::2</div>
</div>
</div>
<div class="fl-step" data-n="4" style="--sc:#5b3a8c">
<div>
<div class="fl-title">Receive Router Advertisement</div>
<div class="fl-detail">Router replies with RA containing the network prefix (e.g., 2001:db8::/64), MTU, and configuration flags. Host records the router's link-local address as the default gateway.</div>
<div class="fl-code">RA: prefix=2001:db8::/64 A=1 L=1</div>
</div>
</div>
<div class="fl-step" data-n="5" style="--sc:#5b3a8c">
<div>
<div class="fl-title">Generate Global Unicast Address</div>
<div class="fl-detail">Combine the /64 prefix from RA with the EUI-64 interface identifier: 2001:db8::[EUI-64]. This is the SLAAC address. Run DAD before using it.</div>
<div class="fl-code">GUA = prefix (64 bits) + EUI-64 (64 bits)</div>
</div>
</div>
</div>
<h4>EUI-64 Interface Identifier Generation</h4>


```bash
/* Derive 64-bit EUI-64 from 48-bit MAC address */

MAC:    aa:bb:cc : dd:ee:ff
        ↓
Split:  aa:bb:cc | dd:ee:ff
Insert: aa:bb:cc : ff:fe : dd:ee:ff    # insert ff:fe in the middle
Flip:   a8:bb:cc : ff:fe : dd:ee:ff    # flip bit 6 (Universal/Local bit) of first byte
                                        # aa = 10101010 → bit 6 flip → 10101000 = a8

/* Example */
MAC:          00:1a:2b:3c:4d:5e
EUI-64:       02:1a:2b:ff:fe:3c:4d:5e
Link-Local:   fe80::021a:2bff:fe3c:4d5e

/* Privacy concern */
# EUI-64 embeds the MAC — tracking device across networks
# RFC 8981 "Temporary Address Extensions" generates random interface IDs
# Linux uses privacy extensions by default: random interface ID, rotated periodically
$ sysctl net.ipv6.conf.eth0.use_tempaddr   # 2 = prefer temporary addresses
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🖥️</span><h3>DHCPv6 — Stateful and Stateless</h3><span class="tag tag-blue">DHCPv6</span></div>
  <div class="cp-body">
<p>DHCPv6 (RFC 8415) provides more control than SLAAC. It comes in two modes, controlled by flags in the Router Advertisement:</p>
<div class="two-col">
<div>
<h4>Stateless DHCPv6 (O flag = 1)</h4>
<p>Host uses SLAAC for its address but queries DHCPv6 for additional configuration: DNS server addresses, domain search list, NTP servers. The DHCPv6 server doesn't track assignments.</p>
<p><strong>Use when:</strong> You want SLAAC's simplicity but need to push DNS/NTP config centrally.</p>
</div>
<div>
<h4>Stateful DHCPv6 (M flag = 1)</h4>
<p>Host gets its entire address from DHCPv6 server (not SLAAC). Server maintains a lease database. Gives full control over address assignment — needed for environments requiring fixed address-to-host mapping.</p>
<p><strong>Use when:</strong> You need to control exactly which address each device gets (servers, NGFW trusted hosts).</p>
</div>
</div>
  </div>
</div>
</div>
<!-- ════════════ TAB 6 — DUAL-STACK AND TRANSITION ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">DUAL-STACK AND IPv4-to-IPv6 TRANSITION MECHANISMS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Dual-Stack — Running Both Simultaneously</h3><span class="tag tag-blue">DUAL-STACK</span></div>
  <div class="cp-body">
<p>The most common and recommended transition approach is <strong>dual-stack</strong>: every node runs both IPv4 and IPv6 simultaneously. Each interface has both an IPv4 address and one or more IPv6 addresses. Applications connect using whichever version the network supports for the destination, with IPv6 preferred (Happy Eyeballs algorithm, RFC 8305).</p>
<div class="ds-diagram">
<div class="ds-row">
<div class="ds-box" style="background:#f0ecfc;border-color:#c0a8e8;color:#3a1a6c">Application<div class="ds-label">HTTP, SSH, DNS</div></div>
</div>
<div class="ds-row">
<div class="ds-box" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">TCP/UDP<div class="ds-label">Transport</div></div>
</div>
<div class="ds-row">
<div class="ds-box" style="background:#e8f5e8;border-color:#90d890;color:#1a5a1a">IPv4<div class="ds-label">10.0.0.5</div></div>
<div class="ds-arrow">+</div>
<div class="ds-box" style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c">IPv6<div class="ds-label">2001:db8::5</div></div>
</div>
<div class="ds-row">
<div class="ds-box" style="background:#fdf4dc;border-color:#e8c870;color:#5a3800">Ethernet NIC<div class="ds-label">Single interface, one MAC</div></div>
</div>
</div>



```bash
# Configure dual-stack on Linux
ip addr add 10.0.0.5/24   dev eth0    # IPv4
ip addr add 2001:db8::5/64 dev eth0    # IPv6 (manual)
# Or let SLAAC configure IPv6 automatically

# Check dual-stack status
ip addr show eth0
# inet  10.0.0.5/24 brd 10.0.0.255 scope global eth0
# inet6 2001:db8::5/64 scope global
# inet6 fe80::a00:27ff:fe4e:66a1/64 scope link

# Connect to a dual-stack server — OS picks IPv6 first (Happy Eyeballs)
curl -v https://google.com
# Look for: Connected to google.com (2a00:1450:4009:820::200e) port 443

# Force IPv4
curl -4 https://google.com
# Force IPv6
curl -6 https://google.com
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🌉</span><h3>Transition Mechanisms — When Dual-Stack Isn't Available</h3><span class="tag tag-teal">TUNNELLING</span></div>
  <div class="cp-body">
<p>Sometimes you need IPv6 connectivity over an IPv4-only network, or vice versa. Several tunnelling and translation mechanisms handle this:</p>
<table class="t-table">
<thead><tr><th>Mechanism</th><th>Type</th><th>How It Works</th><th>Use Case</th></tr></thead>
<tbody>
<tr><td><strong>6in4 (SIT tunnel)</strong></td><td>Tunnel</td><td>IPv6 packet encapsulated in IPv4 (Protocol 41). Manual configuration of endpoints.</td><td>Connecting IPv6 islands over IPv4 backbone</td></tr>
<tr><td><strong>6to4</strong></td><td>Tunnel</td><td>Automatic encapsulation using anycast relay. Embeds IPv4 address in IPv6 prefix 2002::/16.</td><td>Legacy — largely deprecated</td></tr>
<tr><td><strong>Teredo</strong></td><td>Tunnel</td><td>IPv6 over UDP/IPv4. Works through NAT. Used by Windows historically.</td><td>Legacy — deprecated</td></tr>
<tr><td><strong>ISATAP</strong></td><td>Tunnel</td><td>Intra-Site Automatic Tunnel — IPv6 over IPv4 within an organisation.</td><td>Enterprise internal tunnelling</td></tr>
<tr><td><strong>DS-Lite</strong></td><td>Tunnel</td><td>IPv4-in-IPv6 tunnelling + NAT. ISPs deploy this to serve IPv4 over IPv6-only infrastructure.</td><td>ISP transition — CGN replacement</td></tr>
<tr><td><strong>NAT64 + DNS64</strong></td><td>Translation</td><td>NAT64 translates IPv6 packets to IPv4 and back. DNS64 synthesises AAAA records for IPv4-only hosts. IPv6-only clients can reach IPv4 servers.</td><td>IPv6-only mobile networks accessing IPv4 internet</td></tr>
<tr><td><strong>MAP-T / MAP-E</strong></td><td>Translation / Tunnel</td><td>Stateless mapping between IPv4 and IPv6 — no per-connection state in the provider network.</td><td>Modern ISP deployment at scale</td></tr>
</tbody>
</table>
<div class="note"><p>💡 <strong>For your NGFW:</strong> NAT64 and DNS64 are the most important transition mechanisms to support. Mobile operators (Jio included) run IPv6-only core networks with NAT64 gateways to reach IPv4 content. Your NGFW must be capable of processing both IPv6 traffic and NAT64-translated traffic correctly.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 7 — IPv4 vs IPv6 ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">IPv4 vs IPv6 — SIDE-BY-SIDE COMPARISON</p>
<table class="cmp-table">
  <thead>
<tr>
<th>Feature</th>
<th>IPv4</th>
<th>IPv6</th>
</tr>
  </thead>
  <tbody>
<tr>
<td><strong>Address size</strong></td>
<td>32 bits (4 bytes)</td>
<td>128 bits (16 bytes)</td>
</tr>
<tr>
<td><strong>Address space</strong></td>
<td>~4.3 billion</td>
<td>~3.4 × 10³⁸ (340 undecillion)</td>
</tr>
<tr>
<td><strong>Header size</strong></td>
<td>20–60 bytes (variable — IHL)</td>
<td>40 bytes (fixed)</td>
</tr>
<tr>
<td><strong>Header checksum</strong></td>
<td>Yes — recomputed at every hop (TTL change)</td>
<td><span class="good">No</span> — removed. Upper layers have their own checksum</td>
</tr>
<tr>
<td><strong>Fragmentation</strong></td>
<td>By any router along the path</td>
<td><span class="good">Source only</span> — routers send ICMPv6 Packet Too Big</td>
</tr>
<tr>
<td><strong>Broadcast</strong></td>
<td>Yes — 255.255.255.255 and subnet broadcast</td>
<td><span class="good">No broadcast</span> — replaced by targeted multicast</td>
</tr>
<tr>
<td><strong>Address resolution</strong></td>
<td>ARP (L2 broadcast)</td>
<td>NDP (ICMPv6 multicast — more targeted)</td>
</tr>
<tr>
<td><strong>Address configuration</strong></td>
<td>Manual or DHCP</td>
<td>Manual, SLAAC (automatic), or DHCPv6</td>
</tr>
<tr>
<td><strong>NAT</strong></td>
<td>Required (address exhaustion)</td>
<td><span class="good">Not needed</span> — every device gets global address</td>
</tr>
<tr>
<td><strong>IPsec</strong></td>
<td>Optional</td>
<td><span class="good">Mandatory</span> (specification requires support)</td>
</tr>
<tr>
<td><strong>Router discovery</strong></td>
<td>Manual or DHCP option 3 (default gateway)</td>
<td>SLAAC via RA — automatic, no DHCP needed</td>
</tr>
<tr>
<td><strong>Options/extensions</strong></td>
<td>In-header options (variable length, every router reads)</td>
<td>Extension headers (separate, most routers skip)</td>
</tr>
<tr>
<td><strong>TTL/Hop Limit</strong></td>
<td>TTL (8 bits)</td>
<td>Hop Limit (8 bits) — same mechanism, better name</td>
</tr>
<tr>
<td><strong>Flow identification</strong></td>
<td>No dedicated field</td>
<td>20-bit Flow Label — enables hardware-accelerated per-flow routing</td>
</tr>
<tr>
<td><strong>Link-local addresses</strong></td>
<td>169.254.0.0/16 (APIPA, failure indicator)</td>
<td>fe80::/10 — always present, used for NDP/routing</td>
</tr>
<tr>
<td><strong>Loopback</strong></td>
<td>127.0.0.1 (127.0.0.0/8)</td>
<td>::1/128 (single address)</td>
</tr>
<tr>
<td><strong>NGFW complexity</strong></td>
<td>Well-understood, mature tooling</td>
<td>Extension header chain requires careful inspection to avoid evasion</td>
</tr>
  </tbody>
</table>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>IPv6 Security Considerations for NGFW</h3><span class="tag tag-red">NGFW SECURITY</span></div>
  <div class="cp-body">
<p>IPv6 introduces new attack surfaces that NGFWs must handle. Many legacy firewalls only inspect IPv4 — IPv6 traffic passes uninspected, creating a bypass route. This is called an <strong>"IPv6 dark hole"</strong>.</p>
<ul>
<li><strong>Extension header abuse</strong> — attackers can hide payload content or confuse stateless firewalls by inserting many extension headers (Hop-by-Hop with large options, multiple Destination headers). NGFW must traverse the full extension header chain to find L4 headers.</li>
<li><strong>Routing Header type 0 (RH0)</strong> — deprecated (RFC 5095) but still sent by attackers. Allowed source routing of packets through arbitrary nodes — a DDoS amplification vector. Drop all packets with RH0.</li>
<li><strong>ICMPv6 must be allowed selectively</strong> — unlike IPv4 where you can block most ICMP, IPv6 depends on ICMPv6 for basic operation (NDP). Blocking it entirely breaks the network. Allow: Types 133–136 (NDP), 2 (Packet Too Big). Block: Type 137 (Redirect from external).</li>
<li><strong>Rogue RA attacks</strong> — any device can send a Router Advertisement claiming to be the default gateway, redirecting all traffic through itself. NGFW/switches should implement RA Guard (RFC 6105).</li>
<li><strong>Tunnelled IPv6 (6in4, Teredo)</strong> — IPv6-in-IPv4 tunnels can bypass IPv6 firewall rules. Inspect Protocol 41 packets and block unauthorised 6in4 tunnels at the perimeter.</li>
<li><strong>IPv6 fragmentation attacks</strong> — overlapping fragments, tiny fragments hiding L4 headers. NGFW must fully reassemble IPv6 fragments before inspection.</li>
</ul>
  </div>
</div>
</div>
<!-- ════════════ TAB 8 — LABS ════════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Explore IPv6 on Linux — Addresses, NDP, and SLAAC</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Examine a live IPv6 stack, observe NDP in action, understand SLAAC address generation, and decode IPv6 packets with Wireshark.</p>
<div class="lab-step"><div class="sn">1</div><div>Check your IPv6 addresses: <code>ip -6 addr show</code>. Identify: which are link-local (fe80::), which are global unicast (2001: or similar), which are temporary privacy addresses. If no global address exists, check if your router sends RAs: <code>sudo rdisc6 eth0</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Manually derive your expected link-local EUI-64 from your MAC: take <code>ip link show eth0</code> MAC address, split it in half, insert <code>ff:fe</code> in the middle, flip bit 6 of the first byte, prepend <code>fe80::</code>. Compare with the actual fe80 address shown in <code>ip addr</code>. Do they match? If not, Linux privacy extensions may be in use.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Observe the NDP neighbour cache: <code>ip -6 neigh show</code>. Ping your IPv6 default gateway (from <code>ip -6 route show default</code>) and watch the neighbour cache update. Compare with IPv4: <code>ip neigh show</code> — notice the structural similarity (IPv6 neigh = IPv4 ARP cache).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Capture NDP in Wireshark: filter <code>icmpv6</code>. Run <code>sudo ip -6 neigh flush all</code> to clear the cache, then <code>ping6 -c 1 [your_gateway_ipv6]</code>. You should see: NS (Neighbour Solicitation) to the Solicited-Node multicast, NA (Neighbour Advertisement) back. Expand each message and identify all ICMPv6 fields.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Capture a Router Advertisement: filter <code>icmpv6.type == 134</code> in Wireshark. You may need to wait up to 200 seconds for the next periodic RA, or trigger one with <code>sudo ndisc6 eth0 ff02::2</code>. Expand the RA and find: Prefix Information option (prefix, valid/preferred lifetime, A flag), MTU option, source link-layer address.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus — Send a manual Router Solicitation with Scapy:</strong> <code>from scapy.all import *; sendp(Ether(dst="33:33:00:00:00:02")/IPv6(dst="ff02::2")/ICMPv6ND_RS(), iface="eth0")</code>. Capture the RA response that follows — you triggered SLAAC manually.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>IPv6 Socket Programming and Dual-Stack in C</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write a dual-stack TCP server in C that accepts both IPv4 and IPv6 connections. Understand the AF_INET6 socket API and how IPv4-mapped addresses work.</p>
<div class="lab-step"><div class="sn">1</div><div>Write a minimal IPv6 TCP server. Create socket with <code>AF_INET6, SOCK_STREAM</code>. Bind to <code>::</code> (all interfaces, both IPv4 and IPv6) on port 8080. On Linux, binding to <code>::</code> with <code>IPV6_V6ONLY=0</code> creates a dual-stack socket that accepts both IPv4 and IPv6 connections.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Key code pattern:
<div class="cb"><pre><span class="ck">int</span> sock = socket(AF_INET6, SOCK_STREAM, 0);
<span class="ck">int</span> v6only = 0;
setsockopt(sock, IPPROTO_IPV6, IPV6_V6ONLY, &v6only, <span class="ck">sizeof</span>(v6only));
<span class="ck">struct</span> sockaddr_in6 addr = {0};
addr.sin6_family = AF_INET6;
addr.sin6_port = htons(8080);
addr.sin6_addr = in6addr_any;   <span class="cm">/* :: — listen on all interfaces */</span>
bind(sock, (<span class="ck">struct</span> sockaddr *)&addr, <span class="ck">sizeof</span>(addr));
listen(sock, 10);</pre></div>
Compile and run. Connect with <code>telnet localhost 8080</code> (IPv4) and <code>telnet -6 ::1 8080</code> (IPv6).</div></div>
<div class="lab-step"><div class="sn">3</div><div>In the accept() loop, print the connecting client's address. When an IPv4 client connects to the dual-stack socket, its address appears as an IPv4-mapped IPv6 address: <code>::ffff:127.0.0.1</code>. Detect and distinguish IPv4 vs IPv6 clients by checking the first 12 bytes of the address for the IPv4-mapped prefix (<code>::ffff:0:0/96</code>).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Capture the connections in Wireshark. The IPv4 connection uses a regular TCP/IPv4 packet. The IPv6 connection uses TCP/IPv6. Compare the packet sizes: IPv6 header is 40 bytes (fixed) vs IPv4 header 20 bytes (minimum) — IPv6 packets have 20 more bytes of overhead per packet just from the larger addresses.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Bonus — getaddrinfo for protocol-agnostic code:</strong> Replace direct socket creation with <code>getaddrinfo(NULL, "8080", &hints, &res)</code> where <code>hints.ai_family = AF_UNSPEC</code>. This returns both IPv4 and IPv6 addresses — loop through and bind to all. This is how production servers handle dual-stack without caring about the specific protocol.</div></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 9 — CHECKLIST ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">M04 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain why IPv6 was created: IPv4 exhaustion, NAT limitations, and the design improvements</li>
  <li>Know that IPv6 has 128-bit addresses (2¹²⁸ ≈ 3.4 × 10³⁸) and can articulate why this is "enough"</li>
  <li>Can write and abbreviate IPv6 addresses correctly using both abbreviation rules (leading zero dropping, :: compression)</li>
  <li>Know the IPv6 header is fixed at 40 bytes and can name all 8 fields</li>
  <li>Know what the Flow Label is and why it helps with ECMP/RSS flow balancing</li>
  <li>Know that IPv6 uses Next Header (not Protocol) and can name key Next Header values: 6=TCP, 17=UDP, 58=ICMPv6, 44=Fragment</li>
  <li>Understand the extension header chain concept and why it is better than IPv4 options</li>
  <li>Know that IPv6 routers do NOT fragment — source-only fragmentation via Fragment extension header</li>
  <li>Can name the 6 unicast address types: GUA, Link-Local, ULA, Loopback, Unspecified, IPv4-Mapped</li>
  <li>Know the prefixes for each type by heart: GUA=2000::/3, link-local=fe80::/10, ULA=fd00::/8, loopback=::1</li>
  <li>Know the /64 boundary convention and why it is used universally for interface subnets</li>
  <li>Know that IPv6 has no broadcast — replaced by multicast (ff02::1 all-nodes, ff02::2 all-routers, Solicited-Node)</li>
  <li>Can explain the Solicited-Node multicast address construction and why it's more efficient than ARP broadcast</li>
  <li>Know NDP's 5 functions: address resolution, router discovery, prefix discovery, redirect, DAD</li>
  <li>Know the 5 NDP ICMPv6 message types and their numbers: RS(133), RA(134), NS(135), NA(136), Redirect(137)</li>
  <li>Understand SLAAC end-to-end: link-local generation → DAD → RS → RA → GUA generation → DAD</li>
  <li>Know EUI-64 derivation: split MAC, insert ff:fe, flip bit 6 of first byte</li>
  <li>Understand the difference between stateless DHCPv6 (O flag — options only) and stateful DHCPv6 (M flag — address + options)</li>
  <li>Know dual-stack: both IPv4 and IPv6 on same interface, Happy Eyeballs prefers IPv6</li>
  <li>Know NAT64+DNS64: IPv6-only clients reach IPv4 servers — critical for mobile (Jio) networks</li>
  <li>Know key IPv6 NGFW security concerns: extension header evasion, RH0 (drop it), Rogue RA, ICMPv6 filtering rules</li>
  <li>Know to allow ICMPv6 Types 133–136 (NDP) and 2 (Packet Too Big) — never block all ICMPv6</li>
  <li>Completed Lab 1: observed SLAAC, NDP, and RA in Wireshark; decoded NS/NA messages</li>
  <li>Completed Lab 2: wrote dual-stack C TCP server; understood IPv4-mapped addresses in AF_INET6</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>Phase 1 Complete!</strong> You now have solid L1–L3 foundations: OSI model, Ethernet/L2, IPv4, and IPv6. Move to <strong>Phase 2 — Transport and Application Protocols</strong>, starting with <strong>M05 - TCP Internals</strong>. TCP is the most important transport protocol to understand deeply — it underpins HTTP, TLS, SSH, and every stateful NGFW connection.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m03-ipv4/">← M03 IPv4</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m05-tcp/">Next: M05 - TCP Internals →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
