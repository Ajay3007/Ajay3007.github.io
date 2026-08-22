---
title: "M06 - UDP and ICMP"
description: "NETWORKING MASTERY · PHASE 2 · MODULE 06 · WEEK 5 📦 UDP and ICMP UDP header · Use cases · IGMP · Multicast · ICMP deep dive · Traceroute internals · NGFW policy Beginner…"
domain: networking
track: networking-mastery
order: 6
ownHeader: true
url: /learning/networking-mastery/m06-udp-icmp/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#c05e1b 75%,#8c3a0a 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0c880;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f8dfa8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#faecc8}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f0c880;border-bottom-color:#f0c880}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #c05e1b}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0dfa8;white-space:pre}
.cm{color:#8a6a30}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#fdf8e8;border:1.5px solid #c09030;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#2a1e00;border-color:#c09030}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#7a5800}
[data-theme=dark] .ins strong{color:#f0c880}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#1a3a5c}
[data-theme=dark] .note strong{color:#7ab8d8}

/* Analogy */
.analogy{background:linear-gradient(135deg,#fff8ee,#fdf0dc);border:1.5px solid #e8b870;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#1e1200,#1a1000);border-color:#b07820}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#7a5800;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#f0c880}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* Header diagrams */
.hdr-diagram{margin:1rem 0;overflow-x:auto}
.hdr-row{display:flex;gap:2px;min-width:420px;margin-bottom:3px;align-items:stretch}
.hdr-label{font-size:.7rem;font-family:monospace;min-width:76px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:4px}
.hf{border-radius:5px;padding:7px 5px;font-size:.7rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.hf-bytes{font-size:.62rem;font-weight:400;opacity:.8;margin-top:2px}
.hf-sp{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-dp{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-ln{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.hf-ck{background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.hf-ud{background:#e8f5e8;border-color:#90d890;color:#1a5a1a}

/* UDP vs TCP comparison */
.cmp-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.cmp-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.cmp-table td{padding:.5rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.cmp-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.cmp-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px}

/* Protocol cards */
.proto-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.8rem;margin:1rem 0}
.proto-card{border-radius:9px;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff);padding:.9rem 1rem;overflow:hidden}
.proto-card-name{font-size:.82rem;font-weight:700;font-family:monospace;margin-bottom:.25rem}
.proto-card-port{font-size:.72rem;font-family:monospace;padding:2px 6px;border-radius:4px;display:inline-block;margin-bottom:.4rem;font-weight:700}
.proto-card-desc{font-size:.8rem;color:var(--text-color,#444);line-height:1.55}

/* ICMP types table */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#c05e1b;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#c05e1b}

/* Multicast diagram */
.mc-diagram{display:flex;flex-direction:column;gap:6px;margin:1rem 0;padding:1rem;background:var(--bg-color,#f8f8f8);border-radius:10px;border:1.5px solid var(--border-color,#e0e0e0)}
.mc-row{display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap}
.mc-box{border-radius:8px;padding:.5rem .9rem;text-align:center;font-size:.8rem;font-weight:600;border:1.5px solid;min-width:80px}
.mc-arrow{font-size:1.1rem;color:var(--light-text,#888)}

/* Flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#c05e1b)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#f0c880;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#c05e1b;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#c05e1b;margin-top:-.05rem}

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
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 2 · MODULE 06 · WEEK 5</div>
  <div class="mod-title">📦 UDP and ICMP</div>
  <div class="mod-subtitle">UDP header · Use cases · IGMP · Multicast · ICMP deep dive · Traceroute internals · NGFW policy</div>
  <div class="mod-pills">
<span class="mod-pill">Beginner</span>
<span class="mod-pill">Prerequisite: M03 IPv4, M05 TCP</span>
<span class="mod-pill">RFC 768 · RFC 792</span>
<span class="mod-pill">DNS / VoIP / Gaming</span>
<span class="mod-pill">2 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">UDP Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">UDP Header</button>
  <button class="tab-btn" onclick="vt(event,'t2')">UDP Use Cases</button>
  <button class="tab-btn" onclick="vt(event,'t3')">UDP in NGFW</button>
  <button class="tab-btn" onclick="vt(event,'t4')">ICMP Overview</button>
  <button class="tab-btn" onclick="vt(event,'t5')">ICMP Types Deep Dive</button>
  <button class="tab-btn" onclick="vt(event,'t6')">IGMP and Multicast</button>
  <button class="tab-btn" onclick="vt(event,'t7')">ICMP in NGFW</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- ════════════ TAB 0 — UDP OVERVIEW ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">UDP — SIMPLICITY BY DESIGN</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>What UDP Is — and Why It Exists</h3><span class="tag tag-orange">OVERVIEW</span></div>
  <div class="cp-body">
<p>UDP (User Datagram Protocol, RFC 768) is the other Layer 4 transport alongside TCP. Where TCP spends its 20+ byte header providing reliability, ordering, and flow control, UDP provides just enough to identify sender and receiver: <strong>source port, destination port, length, and checksum</strong> — 8 bytes total. That's it.</p>
<p>UDP offers:</p>
<ul>
<li><strong>No connection setup</strong> — send a datagram immediately, no handshake overhead</li>
<li><strong>No reliability</strong> — datagrams can be lost, duplicated, or reordered; UDP won't notice or care</li>
<li><strong>No ordering</strong> — datagrams arrive in whatever order the network delivers them</li>
<li><strong>No flow control</strong> — sender can transmit as fast as it wants</li>
<li><strong>Message-oriented</strong> — one write() = one datagram = one recv(). Unlike TCP's byte stream, UDP preserves message boundaries</li>
<li><strong>Low latency</strong> — no head-of-line blocking, no retransmit delays</li>
</ul>
<p>UDP's "limitations" are actually features for the right use cases. DNS needs a single round-trip — TCP's 3-way handshake would be 50% overhead. Video streaming works better with the occasional dropped frame than with a stutter caused by TCP retransmission. Gaming needs the most recent position, not a reliable stream of every old position.</p>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">📮 Analogy — Postcards vs Registered Letters</div>
  <p>TCP is a registered letter: you get confirmation of delivery, the post office retransmits if it gets lost, and letters arrive in order. UDP is a postcard: you write it, drop it in the postbox, and move on. You don't know if it arrived, you don't get a receipt, and if you send ten postcards they might arrive in any order. For a love letter you want confirmation. For a party invite where you're sending hundreds — a lost postcard doesn't matter, and the savings in overhead (no tracking, no confirmation wait) let you send far more, far faster.</p>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚖️</span><h3>UDP vs TCP — The Full Comparison</h3><span class="tag tag-blue">COMPARISON</span></div>
  <div class="cp-body">
<table class="cmp-table">
<thead><tr><th>Property</th><th>UDP</th><th>TCP</th></tr></thead>
<tbody>
<tr><td><strong>Connection</strong></td><td>Connectionless — no setup, no teardown</td><td>Connection-oriented — 3-way handshake + 4-way teardown</td></tr>
<tr><td><strong>Reliability</strong></td><td>None — send and forget</td><td>Guaranteed delivery with retransmission</td></tr>
<tr><td><strong>Ordering</strong></td><td>Not guaranteed — app handles if needed</td><td>Guaranteed in-order delivery</td></tr>
<tr><td><strong>Message boundaries</strong></td><td>Preserved — 1 send = 1 recv</td><td>Stream — application must frame messages</td></tr>
<tr><td><strong>Header overhead</strong></td><td>8 bytes</td><td>20–60 bytes</td></tr>
<tr><td><strong>Latency</strong></td><td>Minimal — no handshake, no wait</td><td>At least 1 RTT for handshake before first data</td></tr>
<tr><td><strong>Head-of-line blocking</strong></td><td>No — each datagram independent</td><td>Yes — retransmit stalls all subsequent data</td></tr>
<tr><td><strong>Congestion control</strong></td><td>None built-in — app responsible</td><td>Built-in — cwnd, slow start, etc.</td></tr>
<tr><td><strong>Broadcast/Multicast</strong></td><td>Supported natively</td><td>Not supported</td></tr>
<tr><td><strong>Use cases</strong></td><td>DNS, DHCP, TFTP, VoIP, video streaming, gaming, NTP, QUIC, SNMP, RADIUS</td><td>HTTP/HTTPS, SSH, SMTP, FTP, database connections</td></tr>
</tbody>
</table>
<div class="ins"><p>💡 <strong>Application-level reliability over UDP:</strong> Many protocols build their own reliability on top of UDP — QUIC (HTTP/3), DTLS (datagram TLS), game engines (custom ACK systems), and WebRTC all run over UDP but implement their own packet ordering, loss detection, and retransmission tailored to their specific needs. This gives them the best of both worlds: the low overhead and control of UDP plus the reliability features they actually need.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 1 — UDP HEADER ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">UDP HEADER — 8 BYTES, THE SMALLEST TRANSPORT HEADER</p>
<div class="hdr-diagram">
  <div class="hdr-row">
<div class="hdr-label">Row 1</div>
<div class="hf hf-sp" style="flex:2">Source Port<div class="hf-bytes">16 bits — 0 if unused</div></div>
<div class="hf hf-dp" style="flex:2">Destination Port<div class="hf-bytes">16 bits</div></div>
  </div>
  <div class="hdr-row">
<div class="hdr-label">Row 2</div>
<div class="hf hf-ln" style="flex:2">Length<div class="hf-bytes">16 bits — header + data</div></div>
<div class="hf hf-ck" style="flex:2">Checksum<div class="hf-bytes">16 bits — optional in IPv4</div></div>
  </div>
  <div class="hdr-row">
<div class="hdr-label">Data</div>
<div class="hf hf-ud" style="flex:4">UDP Payload<div class="hf-bytes">0 to 65,527 bytes (65,535 − 8 byte header)</div></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Every Field Explained</h3><span class="tag tag-blue">FIELD REFERENCE</span></div>
  <div class="cp-body">
<h4>Source Port (16 bits)</h4>
<p>Identifies the sending application's port. <strong>Optional in UDP</strong> — can be set to 0 if the sender doesn't need a reply (broadcast announcements, one-way telemetry). When set, the receiver can use it to send a reply to the correct client port. Client applications use ephemeral source ports (49152–65535, assigned by the OS) just like TCP.</p>
<h4>Destination Port (16 bits)</h4>
<p>Identifies the target application. Standard UDP ports: <code>53</code>=DNS, <code>67/68</code>=DHCP, <code>123</code>=NTP, <code>161</code>=SNMP, <code>500</code>=IKEv2 (IPsec key exchange), <code>4500</code>=IPsec NAT-T, <code>5060</code>=SIP (VoIP), <code>443</code>=QUIC (HTTP/3).</p>
<h4>Length (16 bits)</h4>
<p>Total length of the UDP datagram including the 8-byte header. Minimum value: 8 (header only, zero payload). Maximum: 65,535. In practice, UDP datagrams larger than ~1472 bytes (MTU 1500 minus 20 IP header minus 8 UDP header) will be fragmented by IP — generally undesirable. DNS limits responses to 512 bytes over UDP historically (EDNS0 extends this to 4096).</p>
<h4>Checksum (16 bits)</h4>
<p>Computed over a pseudo-header (same as TCP: IP src, IP dst, Protocol=17, UDP length) plus the entire UDP header and payload. In IPv4, the checksum is <strong>optional</strong> — a value of 0x0000 means "no checksum computed". In IPv6, it is mandatory (IPv6 has no IP header checksum, so UDP checksum is the only protection). Modern NICs offload UDP checksum computation to hardware.</p>
<div class="cb"><pre><span class="cm">/* UDP socket programming in C — minimal server */</span>
<span class="ck">int</span> sock = socket(AF_INET, SOCK_DGRAM, 0);   <span class="cm">/* SOCK_DGRAM for UDP */</span>
<span class="ck">struct</span> sockaddr_in addr = {0};
addr.sin_family      = AF_INET;
addr.sin_port        = htons(53);            <span class="cm">/* DNS port */</span>
addr.sin_addr.s_addr = INADDR_ANY;
bind(sock, (<span class="ck">struct</span> sockaddr *)&addr, <span class="ck">sizeof</span>(addr));
 
<span class="cm">/* Receive a datagram — one call = one complete message */</span>
<span class="ck">char</span> buf[512];
<span class="ck">struct</span> sockaddr_in client;
socklen_t clen = <span class="ck">sizeof</span>(client);
ssize_t n = recvfrom(sock, buf, <span class="ck">sizeof</span>(buf), 0,
                     (<span class="ck">struct</span> sockaddr *)&client, &clen);
<span class="cm">/* n = exact bytes in this datagram — complete message, no framing needed */</span>
<span class="cm">/* Send reply to same client */</span>
sendto(sock, response, resp_len, 0,
       (<span class="ck">struct</span> sockaddr *)&client, clen);
 
<span class="cm">/* Key: no connect(), no accept(), no listen() — stateless */</span>
<span class="cm">/* One socket can handle multiple clients simultaneously */</span></pre></div>
<div class="ins"><p>💡 <strong>recvfrom vs recv:</strong> UDP uses <code>recvfrom()</code> to get both the datagram AND the sender's address in one call. With TCP you call <code>accept()</code> once per connection and get a dedicated socket. With UDP a single socket handles all clients — you use the sender's address from recvfrom to send replies to the right client.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">💻</span><h3>UDP Header in C — Parsing Raw Packets</h3><span class="tag tag-teal">CODE</span></div>
  <div class="cp-body">


```cpp
#include <netinet/udp.h>  /* struct udphdr */

/* Parse UDP header from raw packet bytes */
void parse_udp(const uint8_t *ip_payload, uint16_t ip_payload_len) {
    const struct udphdr *udp = (const struct udphdr *)ip_payload;

    uint16_t src_port = ntohs(udp->uh_sport);   /* or source */
    uint16_t dst_port = ntohs(udp->uh_dport);   /* or dest */
    uint16_t length   = ntohs(udp->uh_ulen);    /* total datagram length */
    uint16_t checksum = ntohs(udp->uh_sum);     /* 0 = disabled */

    uint16_t data_len = length - 8;             /* subtract header */
    const uint8_t *payload = ip_payload + 8;    /* payload after 8-byte header */

    printf("UDP: %u → %u  len=%u  cksum=0x%04x\n",
           src_port, dst_port, length, checksum);

    /* Dispatch to upper-layer handlers */
    switch (dst_port) {
        case 53:  handle_dns(payload, data_len);  break;
        case 67:  handle_dhcp(payload, data_len); break;
        case 123: handle_ntp(payload, data_len);  break;
        default:  handle_unknown(payload, data_len);
    }
}

/* In VPP: UDP header accessed via vlib_buffer_get_current() */
/* after ip4-input has advanced past IP header */
udp_header_t *udp = vlib_buffer_get_current(b0);
u16 dst_port = clib_net_to_host_u16(udp->dst_port);
```


  </div>
</div>
</div>
<!-- ════════════ TAB 2 — UDP USE CASES ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">KEY UDP-BASED PROTOCOLS — WHY EACH CHOSE UDP</p>
<div class="proto-grid">
  <div class="proto-card">
<div class="proto-card-name">DNS</div>
<div class="proto-card-port" style="background:#e8f1f9;color:#1a3a5c">UDP 53</div>
<div class="proto-card-desc">Query-response fits in one datagram. No handshake = lower latency. Falls back to TCP for responses &gt;512B (EDNS0 extends to 4096B over UDP). TCP also used for zone transfers.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">DHCP</div>
<div class="proto-card-port" style="background:#e0f0ee;color:#0a3a30">UDP 67/68</div>
<div class="proto-card-desc">Client has no IP yet — can't use TCP. Client sends on 68, server listens on 67. Uses broadcast (255.255.255.255) to reach server before IP assignment.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">NTP</div>
<div class="proto-card-port" style="background:#e2f0e8;color:#1a4a1a">UDP 123</div>
<div class="proto-card-desc">Time sync needs a single packet exchange. TCP overhead and retransmit delays would corrupt the precision timing calculation. Each packet carries a timestamp.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">SNMP</div>
<div class="proto-card-port" style="background:#fdf4dc;color:#5a3800">UDP 161/162</div>
<div class="proto-card-desc">Simple polling protocol. Manager queries agent (161), agent sends traps to manager (162). Low overhead for network monitoring. SNMP v3 adds encryption over UDP.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">TFTP</div>
<div class="proto-card-port" style="background:#ede8f5;color:#3a1a6c">UDP 69</div>
<div class="proto-card-desc">Trivial FTP — used in PXE boot and router firmware upgrades. Deliberately simple: implements its own stop-and-wait reliability over UDP. No authentication.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">SIP / VoIP</div>
<div class="proto-card-port" style="background:#faeae4;color:#6a2800">UDP 5060</div>
<div class="proto-card-desc">Voice packets are time-sensitive. A retransmitted voice packet arrives too late to be useful — better to drop and let the codec handle it. Real-time media uses RTP over UDP.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">QUIC / HTTP/3</div>
<div class="proto-card-port" style="background:#e8f5e8;color:#1a5a1a">UDP 443</div>
<div class="proto-card-desc">QUIC implements its own reliability, ordering, and congestion control over UDP — getting all of TCP's features without TCP's head-of-line blocking. The future of web transport.</div>
  </div>
  <div class="proto-card">
<div class="proto-card-name">IKEv2 / IPsec</div>
<div class="proto-card-port" style="background:#e8f1f9;color:#1a3a5c">UDP 500 / 4500</div>
<div class="proto-card-desc">IPsec key exchange (IKEv2) runs over UDP 500. When NAT is present, uses port 4500 (NAT-T — NAT Traversal). ESP traffic also gets encapsulated in UDP for NAT compatibility.</div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📺</span><h3>Real-Time Media — Why UDP Fits Video and Audio</h3><span class="tag tag-orange">MEDIA STREAMING</span></div>
  <div class="cp-body">
<p>Video and audio streaming have unique requirements that make UDP far superior to TCP:</p>
<ul>
<li><strong>Timeliness over completeness</strong> — a voice packet that arrives 300ms late is worse than a dropped packet. Modern codecs (Opus, H.264) handle packet loss with error concealment — the quality degrades gracefully. TCP's retransmission would cause a stutter heard by the user.</li>
<li><strong>No head-of-line blocking</strong> — with TCP, if one packet is lost, all subsequent packets are held in the buffer until the missing one arrives (or is retransmitted). For video this means the entire stream freezes. With UDP each packet is independent — a loss is just a momentary artefact.</li>
<li><strong>Sender controls pacing</strong> — video encoders produce frames at a known rate. With UDP the sender decides exactly when to send each packet, matching the media timing. TCP's window management can cause bursts and gaps.</li>
</ul>
<p><strong>RTP (Real-time Transport Protocol)</strong> — the standard protocol for audio/video over UDP. Adds: sequence numbers (for ordering/loss detection), timestamp (for playback synchronisation), SSRC (identifies the media source). RTCP (RTP Control Protocol) provides quality feedback — packet loss rate, jitter, round-trip delay — used to adapt codec bitrate.</p>
<div class="cb"><pre><span class="cm">/* RTP Header (12 bytes) over UDP */</span>
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|V=2|P|X|  CC   |M|     PT      |       Sequence Number         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           Timestamp                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Synchronization Source (SSRC) identifier           |
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
|            Media payload (audio/video encoded data)           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 
<span class="cm">/* PT = Payload Type: 0=PCMU audio, 8=PCMA, 96-127=dynamic (H.264, Opus) */</span>
<span class="cm">/* Stack: Ethernet → IP → UDP → RTP → H.264 video frames */</span></pre></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 3 — UDP IN NGFW ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">UDP IN AN NGFW — STATELESS TRACKING AND COMMON THREATS</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>How NGFWs Handle UDP — Pseudo-Stateful Tracking</h3><span class="tag tag-teal">STATEFUL UDP</span></div>
  <div class="cp-body">
<p>UDP has no handshake and no connection state — every datagram is independent. So how does a stateful NGFW track UDP "sessions"? By treating a group of UDP datagrams between the same 5-tuple within a timeout window as a session, even though UDP itself has no concept of sessions.</p>


```yaml
/* UDP pseudo-session in NGFW conntrack */
typedef struct {
    ip4_address_t  src_ip, dst_ip;
    uint16_t       src_port, dst_port;
    uint8_t        proto;                /* 17 = UDP */

    uint64_t       first_seen;           /* timestamp of first datagram */
    uint64_t       last_seen;            /* updated on each datagram */
    uint64_t       bytes_fwd;            /* client → server bytes */
    uint64_t       bytes_rev;            /* server → client bytes */
    uint8_t        state;                /* NEW / ESTABLISHED / TIMEOUT */
    uint32_t       timeout_sec;          /* idle timeout */
} udp_session_t;

/* UDP session lifecycle */
First datagram from client → create entry (state=NEW), apply policy
Reply datagram from server  → find entry by reversed 5-tuple, state=ESTABLISHED
No more datagrams for 30s  → sweep timer removes entry (default UDP timeout)

/* Different timeouts for different UDP protocols */
DNS:          5  seconds   /* DNS is one query + one reply */
DHCP:         30 seconds
NTP:          30 seconds
VoIP/RTP:    180 seconds   /* ongoing media stream */
Generic UDP:  30 seconds   /* catch-all default */
```


<div class="note"><p>💡 <strong>The reply problem:</strong> When a client sends a DNS query, the NGFW sees the outbound UDP packet and creates a session entry. When the DNS server replies, the NGFW sees a datagram with reversed 5-tuple — it must allow this even though no "connection" was established. This is handled by matching the reversed 5-tuple against the existing session table entry. Without this, return traffic would be blocked.</p></div>
  </div>
</div>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>UDP-Based Attacks and NGFW Defences</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Attack</th><th>Mechanism</th><th>NGFW Defence</th></tr></thead>
<tbody>
<tr>
<td><strong>UDP Flood</strong></td>
<td>Attacker sends massive volume of UDP datagrams to random ports, saturating bandwidth and forcing server to send ICMP Port Unreachable for each</td>
<td>Rate-limit UDP per source IP per second. Drop excessive datagrams. BPF/XDP-based ingress rate limiting</td>
</tr>
<tr>
<td><strong>UDP Amplification (DRDoS)</strong></td>
<td>Attacker sends small spoofed requests to DNS/NTP/SSDP servers with victim's IP as source. Server sends large replies to victim. DNS: 28B → 3000B = 100× amplification</td>
<td>Block spoofed source IPs (BCP38/uRPF). Rate-limit DNS response size. Disable open resolvers. Block NTP monlist command</td>
</tr>
<tr>
<td><strong>DNS Amplification</strong></td>
<td>Specific case of amplification using ANY queries to open resolvers</td>
<td>Block ANY query responses &gt;512B. Respond with TRUNCATED flag to force TCP fallback for large answers</td>
</tr>
<tr>
<td><strong>UDP Port Scan</strong></td>
<td>Attacker sends UDP datagrams to all ports; closed ports return ICMP Port Unreachable, open ports return nothing or a response</td>
<td>Rate-limit ICMP Port Unreachable generation. Track scan patterns (many different dst ports from same src)</td>
</tr>
<tr>
<td><strong>Fragmented UDP</strong></td>
<td>Attacker sends fragmented UDP to hide payload content from stateless inspection</td>
<td>Reassemble all IP fragments before L4/L7 inspection</td>
</tr>
<tr>
<td><strong>TFTP Abuse</strong></td>
<td>TFTP has no authentication — arbitrary file read/write if exposed</td>
<td>Block UDP 69 at internet perimeter. Only allow internally for PXE boot from specific subnets</td>
</tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- ════════════ TAB 4 — ICMP OVERVIEW ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">ICMP — THE NETWORK'S DIAGNOSTIC AND ERROR SYSTEM</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📨</span><h3>What ICMP Is — The Network's Nervous System</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
<p>ICMP (Internet Control Message Protocol, RFC 792) is IP's built-in error reporting and diagnostic protocol. It travels inside IP packets (Protocol number = 1) but is not a transport layer protocol — it has no ports, no concept of connections or streams. Every network device generates and consumes ICMP messages.</p>
<p>ICMP enables network troubleshooting tools like <code>ping</code> and <code>traceroute</code>, and also carries critical error notifications that the network depends on for correct operation (Path MTU Discovery, Redirect, etc.).</p>
<p><strong>ICMP message structure:</strong> Every ICMP message has an 8-byte fixed header:</p>
<div class="hdr-diagram">
<div class="hdr-row">
<div class="hdr-label">ICMP hdr</div>
<div class="hf" style="flex:1;background:#faeee4;border-color:#e8b090;color:#6a2800">Type<div class="hf-bytes">8 bits</div></div>
<div class="hf" style="flex:1;background:#faeee4;border-color:#e8b090;color:#6a2800">Code<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-ck" style="flex:2">Checksum<div class="hf-bytes">16 bits</div></div>
<div class="hf" style="flex:2;background:#e8f5e8;border-color:#90d890;color:#1a5a1a">Type-specific data<div class="hf-bytes">32 bits</div></div>
</div>
<div class="hdr-row">
<div class="hdr-label">Payload</div>
<div class="hf" style="flex:4;background:var(--bg-color,#f5f5f5);border-color:var(--border-color,#e0e0e0);color:var(--light-text,#666)">Variable data (depends on Type — often includes original IP header + 8 bytes of original payload)</div>
</div>
</div>
<ul>
<li><strong>Type</strong> — identifies the ICMP message category (0=Echo Reply, 3=Unreachable, 8=Echo Request, 11=Time Exceeded, etc.)</li>
<li><strong>Code</strong> — sub-type within the Type. Type 3 has 16 different codes (0=Net Unreach, 1=Host Unreach, 3=Port Unreach, 4=Frag Needed...)</li>
<li><strong>Checksum</strong> — covers entire ICMP message</li>
<li><strong>Type-specific data</strong> — varies: Echo uses Identifier+Sequence, Unreachable has unused field, Redirect has gateway address</li>
<li><strong>Payload</strong> — error messages include the original IP header + first 8 bytes of original payload (so sender can identify which packet caused the error)</li>
</ul>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>Ping — How It Works Internally</h3><span class="tag tag-teal">PING</span></div>
  <div class="cp-body">
<p>Ping is the simplest network diagnostic: send an ICMP Echo Request, receive an ICMP Echo Reply, measure round-trip time. Simple — but the implementation details matter.</p>


```bash
/* ICMP Echo Request (Type 8, Code 0) */
Type:       8
Code:       0
Checksum:   [computed]
Identifier: [process ID — matches request to reply if multiple pings running]
Sequence:   [increments with each ping — 1, 2, 3...]
Data:       [arbitrary payload — default 56 bytes on Linux = 64B ICMP total]

/* ICMP Echo Reply (Type 0, Code 0) */
Type:       0
Code:       0
Checksum:   [computed]
Identifier: [same as request]
Sequence:   [same as request]
Data:       [same bytes echoed back]

/* ping command usage */
ping -c 4 8.8.8.8           # send 4 pings
ping -s 1400 8.8.8.8        # send 1400-byte payload (test MTU)
ping -f -s 1472 8.8.8.8    # flood ping at max MTU size
ping -M do -s 1473 8.8.8.8  # force DF=1, will get "Frag needed" if MTU exceeded
ping6 2001:4860:4860::8888  # IPv6 ping (ICMPv6 Type 128/129)

/* Interpreting ping output */
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=12.4 ms
#                                         ↑ TTL at receiver (started at some value, decremented by hops)
#                                                         ↑ round-trip time in ms

/* TTL tricks */
# TTL=117 → started at 128 (Windows hop) → 11 hops away
# TTL=52  → started at 64  (Linux hop)   → 12 hops away
# TTL=245 → started at 255 (router)      → 10 hops away
```


  </div>
</div>
</div>
<!-- ════════════ TAB 5 — ICMP TYPES DEEP DIVE ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">ICMP TYPES — COMPLETE REFERENCE WITH CONTEXT</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📋</span><h3>All ICMP Types — What Each Does</h3><span class="tag tag-orange">REFERENCE</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Type</th><th>Code</th><th>Name</th><th>Generated By</th><th>Purpose and Details</th></tr></thead>
<tbody>
<tr>
<td><code>0</code></td><td>0</td><td>Echo Reply</td><td>Destination host</td>
<td>Response to Echo Request (ping). Echoes the exact Identifier, Sequence Number, and data payload. Round-trip time calculated from timestamp in data.</td>
</tr>
<tr>
<td rowspan="9"><code>3</code></td><td>0</td><td>Net Unreachable</td><td>Router</td>
<td>No route to the destination network in routing table.</td>
</tr>
<tr><td>1</td><td>Host Unreachable</td><td>Router</td><td>Route to network exists but no route to specific host. ARP for host failed.</td></tr>
<tr><td>2</td><td>Protocol Unreachable</td><td>Destination</td><td>Host doesn't support the L4 protocol (IP Protocol field) in the packet.</td></tr>
<tr><td>3</td><td>Port Unreachable</td><td>Destination</td><td>No process is listening on the destination UDP port. Key for UDP port scanning detection.</td></tr>
<tr><td>4</td><td>Fragmentation Needed</td><td>Router</td><td><strong>Critical for PMTUD.</strong> Packet too large for outgoing link and DF=1 set. Message includes the MTU of the outgoing link. Must never be filtered at NGFW.</td></tr>
<tr><td>5</td><td>Source Route Failed</td><td>Router</td><td>Strict source routing failed — specified route is not available.</td></tr>
<tr><td>9</td><td>Dest Net Admin Prohibited</td><td>Router/FW</td><td>Firewall/ACL denied the packet to this destination network. Sent when firewall wants to inform sender.</td></tr>
<tr><td>10</td><td>Dest Host Admin Prohibited</td><td>Router/FW</td><td>Firewall denied packet to specific host.</td></tr>
<tr><td>13</td><td>Communication Admin Prohibited</td><td>Router/FW</td><td>Generic "blocked by admin policy" — most common NGFW rejection response.</td></tr>
<tr>
<td><code>4</code></td><td>0</td><td>Source Quench</td><td>Router/Host</td>
<td><strong>Deprecated (RFC 6633).</strong> Originally used to signal congestion — "slow down". Replaced by ECN and TCP congestion control. Drop these if received.</td>
</tr>
<tr>
<td rowspan="4"><code>5</code></td><td>0</td><td>Redirect — Network</td><td>Router</td>
<td>A better route exists for this destination network via a different gateway on the same segment.</td>
</tr>
<tr><td>1</td><td>Redirect — Host</td><td>Router</td><td>Better route for this specific host.</td></tr>
<tr><td>2</td><td>Redirect — TOS+Network</td><td>Router</td><td>Better route for this TOS+network combination.</td></tr>
<tr><td>3</td><td>Redirect — TOS+Host</td><td>Router</td><td>Better route for this TOS+host combination.</td></tr>
<tr>
<td><code>8</code></td><td>0</td><td>Echo Request</td><td>Any host</td>
<td>The "ping" packet. Destination should respond with Type 0 Echo Reply. Contains Identifier and Sequence Number for tracking.</td>
</tr>
<tr>
<td><code>9</code></td><td>0</td><td>Router Advertisement</td><td>Router</td>
<td>Part of the ICMP Router Discovery Protocol (IRDP). Router announces itself. Less common — RIP/OSPF/BGP have replaced this for most routing.</td>
</tr>
<tr>
<td><code>10</code></td><td>0</td><td>Router Solicitation</td><td>Host</td>
<td>Host asks "any routers out there?". Triggers Router Advertisement response. Mostly replaced by DHCP for gateway discovery.</td>
</tr>
<tr>
<td rowspan="2"><code>11</code></td><td>0</td><td>TTL Exceeded in Transit</td><td>Router</td>
<td><strong>The traceroute mechanism.</strong> Router decremented TTL to 0 and discarded the packet. Returns original IP header + first 8 bytes of original payload so sender knows which packet was dropped.</td>
</tr>
<tr><td>1</td><td>Fragment Reassembly Timeout</td><td>Destination</td><td>Not all fragments arrived before the reassembly timer expired. All collected fragments discarded.</td></tr>
<tr>
<td><code>12</code></td><td>0–2</td><td>Parameter Problem</td><td>Router/Host</td>
<td>IP header field has an invalid value. Code 0: pointer to the offending byte. Code 1: missing required option. Code 2: bad length.</td>
</tr>
<tr>
<td><code>13</code></td><td>0</td><td>Timestamp</td><td>Any host</td>
<td>Used for clock synchronisation — requests timestamps from target. Largely replaced by NTP (UDP 123).</td>
</tr>
<tr>
<td><code>17</code></td><td>0</td><td>Address Mask Request</td><td>Host</td>
<td>Host asks for its subnet mask. Deprecated — use DHCP or manual configuration.</td>
</tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>Traceroute — Complete Internal Mechanism</h3><span class="tag tag-teal">TRACEROUTE</span></div>
  <div class="cp-body">
<p>Traceroute is one of the most elegant network tools — it discovers every router hop between you and a destination using nothing but ICMP Type 11 and TTL manipulation. Understanding it deeply tells you a lot about how routing works in practice.</p>


```python
/* Linux traceroute algorithm (UDP mode, default) */
for ttl in 1..max_hops:
    send 3 UDP packets:
        IP: TTL = ttl, dst = target
        UDP: dst_port = 33434 + (ttl-1)*3  # incrementing port per probe
    wait for response:
        ICMP Type 11 Code 0 → TTL expired at THIS router
        ICMP Type 3 Code 3  → Port Unreachable from TARGET (destination reached)
        no reply within timeout → print "* * *"

    print: ttl, router_ip (from ICMP source), 3 RTTs

/* Windows tracert algorithm (ICMP mode) */
for ttl in 1..max_hops:
    send 3 ICMP Echo Request: TTL = ttl
    ICMP Type 11 Code 0 → intermediate router
    ICMP Type 0 → destination replied (done)

/* mtr (my traceroute) — continuous real-time version */
mtr --report --report-cycles 10 8.8.8.8

/* Interpreting traceroute anomalies */
Hop 5: * * *           # ICMP blocked or rate-limited — does NOT mean broken path
                        # subsequent hops may show fine
Hop 7: 192.168.x.x    # private address — NAT or misconfigured router
RTT spike at hop 8     # congestion at or beyond hop 8
RTT lower at hop 9     # asymmetric routing — return path is shorter
Same IP twice          # routing loop (rare with modern routing protocols)
Hop 3 → Hop 5 jump    # some hops don't respond to ICMP — skipped
```



<div class="ins"><p>💡 <strong>Why UDP for Linux traceroute?</strong> By using UDP to high port numbers (33434+), Linux traceroute gets a reliable "destination reached" signal — when the packet finally arrives at the target with a valid TTL, the host returns ICMP Port Unreachable (nobody listens on port 33434+). If ICMP Echo Requests were used, the target might silently discard them if ping is blocked — giving a false "not reached" result.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 6 — IGMP AND MULTICAST ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">IGMP AND IP MULTICAST — ONE-TO-MANY EFFICIENT DELIVERY</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📡</span><h3>What Multicast Is and Why It Matters</h3><span class="tag tag-purple">MULTICAST CONCEPT</span></div>
  <div class="cp-body">
<p>Multicast allows one sender to efficiently deliver to multiple receivers without sending a separate copy to each — the network itself handles replication. Compare with:</p>
<div class="two-col">
<div>
<h4>Without multicast (unicast to N receivers)</h4>
<p>Sender sends N identical copies. Network carries N×traffic. At 1000 receivers watching a live video: 1000 separate streams. Server bandwidth: 1000 × 4 Mbps = 4 Gbps.</p>
</div>
<div>
<h4>With multicast (one multicast group)</h4>
<p>Sender sends 1 copy to multicast address. Routers replicate only where paths diverge. At 1000 receivers: 1 stream until last router, then per-branch copies. Server bandwidth: 1 × 4 Mbps = 4 Mbps.</p>
</div>
</div>
<p><strong>IP multicast address range: 224.0.0.0/4</strong> (Class D — first 4 bits are 1110). Routers forward multicast packets only to interfaces with interested receivers. Ethernet multicast uses a MAC prefix of 01:00:5E:xx:xx:xx (lower 23 bits of IP multicast address mapped to MAC).</p>
<p><strong>Important multicast addresses:</strong></p>
<ul>
<li><code>224.0.0.1</code> — All Hosts on this subnet (local link only)</li>
<li><code>224.0.0.2</code> — All Routers on this subnet</li>
<li><code>224.0.0.5</code> — OSPF All Routers</li>
<li><code>224.0.0.6</code> — OSPF Designated Routers</li>
<li><code>224.0.0.9</code> — RIPv2 routers</li>
<li><code>224.0.0.18</code> — VRRP</li>
<li><code>239.0.0.0/8</code> — Organisation-local scope (private multicast)</li>
</ul>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📋</span><h3>IGMP — Internet Group Management Protocol</h3><span class="tag tag-green">IGMP</span></div>
  <div class="cp-body">
<p>IGMP (RFC 3376, version 3) is how hosts tell their local router "I want to receive traffic for multicast group 224.x.x.x". Routers use this to decide which interfaces need multicast traffic forwarded to them.</p>
<table class="t-table">
<thead><tr><th>IGMP Version</th><th>Key Feature</th><th>Message Types</th></tr></thead>
<tbody>
<tr><td><code>IGMPv1</code> (RFC 1112)</td><td>Basic group membership. Leave by timeout only.</td><td>Membership Query, Membership Report</td></tr>
<tr><td><code>IGMPv2</code> (RFC 2236)</td><td>Adds explicit Leave Group message. Faster leave processing.</td><td>+ Leave Group, Group-Specific Query</td></tr>
<tr><td><code>IGMPv3</code> (RFC 3376)</td><td>Source-specific multicast (SSM). Receiver can specify which sources to accept from.</td><td>+ Group-and-Source-Specific Query</td></tr>
</tbody>
</table>



```python
/* IGMP exchange — host joins multicast group */
1. Host wants to join 224.1.2.3:
   sends IGMP Membership Report → dst IP: 224.1.2.3 (the group itself)
   Router sees report → starts forwarding 224.1.2.3 to this interface

2. Router sends periodic Membership Query → dst IP: 224.0.0.1 (all hosts)
   "Who still wants which groups?"
   Hosts reply with their active groups

3. Host wants to leave:
   sends IGMP Leave Group → dst IP: 224.0.0.2 (all routers)
   Router sends Group-Specific Query to confirm no remaining members
   If no reply → stops forwarding to this interface

/* IGMP Snooping — switches track IGMP to avoid flooding */
# Without IGMP snooping: multicast = flood to all ports (like broadcast)
# With IGMP snooping: switch tracks which ports have interested hosts
#   → forwards multicast only to ports with IGMP reports
#   → dramatically reduces unnecessary traffic on switched networks

# Linux: join a multicast group from a socket
struct ip_mreq mreq;
mreq.imr_multiaddr.s_addr = inet_addr("224.1.2.3");
mreq.imr_interface.s_addr = INADDR_ANY;
setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, &mreq, sizeof(mreq));
```



<div class="mc-diagram">
<div class="mc-row">
<div class="mc-box" style="background:#e8f5e8;border-color:#90d890;color:#1a5a1a">Source<div style="font-size:.65rem;font-weight:400">224.1.2.3 stream</div></div>
<div class="mc-arrow">→</div>
<div class="mc-box" style="background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c">Core Router<div style="font-size:.65rem;font-weight:400">replicates at branch</div></div>
<div class="mc-arrow">→</div>
<div class="mc-box" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">Edge Router A<div style="font-size:.65rem;font-weight:400">2 members</div></div>
</div>
<div class="mc-row" style="justify-content:flex-end;padding-right:20px">
<div class="mc-arrow" style="transform:rotate(90deg)">↓</div>
</div>
<div class="mc-row" style="justify-content:flex-end">
<div class="mc-box" style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c">Edge Router B<div style="font-size:.65rem;font-weight:400">3 members</div></div>
<div class="mc-arrow">← no traffic here (no members)</div>
<div class="mc-box" style="background:#f0f0f0;border-color:#c0c0c0;color:#555">Edge Router C<div style="font-size:.65rem;font-weight:400">0 members</div></div>
</div>
</div>
  </div>
</div>
</div>
<!-- ════════════ TAB 7 — ICMP IN NGFW ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">ICMP IN AN NGFW — WHAT TO ALLOW, WHAT TO BLOCK, AND WHY</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>The Wrong Way: Block All ICMP</h3><span class="tag tag-red">COMMON MISTAKE</span></div>
  <div class="cp-body">
<p>Many firewall administrators, in an attempt to "harden" the network, block all ICMP traffic. This is a mistake that causes subtle, hard-to-diagnose problems:</p>
<ul>
<li><strong>Broken PMTUD</strong> — blocking ICMP Type 3 Code 4 (Fragmentation Needed) breaks Path MTU Discovery. Large TCP connections work fine for small data but silently stall when they try to send large payloads. Users see "web pages partially load" or "large file downloads hang at X%".</li>
<li><strong>No traceroute</strong> — blocks network troubleshooting, makes diagnosing outages much harder for your team and your customers.</li>
<li><strong>Broken IPv6</strong> — ICMPv6 is fundamental to IPv6 operation (NDP, RA, Packet Too Big). Blocking all ICMPv6 breaks IPv6 connectivity entirely.</li>
</ul>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">✅</span><h3>Correct NGFW ICMP Policy</h3><span class="tag tag-teal">BEST PRACTICE</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>ICMP Type/Code</th><th>Direction</th><th>Action</th><th>Reason</th></tr></thead>
<tbody>
<tr style="background:#e8f5e8"><td>Type 3, Code 4 (Frag Needed)</td><td>Both</td><td><strong>ALWAYS ALLOW</strong></td><td>PMTUD — blocking breaks large TCP connections silently</td></tr>
<tr style="background:#e8f5e8"><td>Type 11 (TTL Exceeded)</td><td>Inbound</td><td><strong>ALLOW</strong></td><td>Return traffic for traceroute, debugging</td></tr>
<tr style="background:#e8f5e8"><td>Type 0 (Echo Reply)</td><td>Inbound</td><td>Allow (stateful)</td><td>Return traffic for outbound pings from internal hosts</td></tr>
<tr style="background:#e8f5e8"><td>Type 3, Code 0–3 (Unreachable)</td><td>Inbound</td><td>Allow (stateful)</td><td>Error responses for established connections</td></tr>
<tr style="background:#faeaea"><td>Type 8 (Echo Request)</td><td>Inbound from internet</td><td>Block or rate-limit</td><td>Reduces attack surface, prevents network mapping. Allow from trusted sources for monitoring.</td></tr>
<tr style="background:#faeaea"><td>Type 5 (Redirect)</td><td>Inbound from internet</td><td><strong>BLOCK</strong></td><td>ICMP Redirect attacks can reroute traffic through attacker's host</td></tr>
<tr style="background:#faeaea"><td>Type 9 (Router Advert)</td><td>Inbound from internet</td><td><strong>BLOCK</strong></td><td>Rogue router advertisement attacks</td></tr>
<tr style="background:#faeaea"><td>Type 4 (Source Quench)</td><td>Both</td><td>Drop</td><td>Deprecated (RFC 6633) — no modern implementation uses this</td></tr>
<tr style="background:#e8f5e8"><td>All ICMP types</td><td>Outbound</td><td>Allow</td><td>Internal users need full diagnostic capability</td></tr>
<tr style="background:#e8f5e8"><td>Type 3, Code 3 (Port Unreachable)</td><td>Outbound</td><td>Allow</td><td>Legitimate response to UDP packets on closed ports</td></tr>
</tbody>
</table>
<div class="warn"><p>⚠️ <strong>ICMP rate limiting is better than blocking.</strong> Rather than blocking ICMP Type 8 (Echo Request) entirely, rate-limit it: allow 10 pings per second from any source. This allows legitimate connectivity testing and monitoring while preventing ICMP flood attacks and network mapping. Most enterprise NGFWs implement rate limiting per source IP.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>ICMP-Based Attacks</h3><span class="tag tag-orange">ATTACK TYPES</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Attack</th><th>ICMP Type Used</th><th>Mechanism</th><th>NGFW Defence</th></tr></thead>
<tbody>
<tr><td><strong>Ping Flood</strong></td><td>Type 8 (Echo Request)</td><td>Attacker sends thousands of pings/second, overwhelming target's CPU and bandwidth processing replies</td><td>Rate-limit ICMP per source IP. Block large ICMP payloads from internet</td></tr>
<tr><td><strong>Smurf Attack</strong></td><td>Type 8 spoofed to broadcast</td><td>Attacker sends Echo Requests to broadcast address with victim's IP as source. All hosts on segment reply to victim. Amplification ×N hosts</td><td>Block directed broadcasts (RFC 2644). BCP38 anti-spoofing</td></tr>
<tr><td><strong>Ping of Death</strong></td><td>Type 8 oversized</td><td>Sends fragmented ICMP payload &gt;65535 bytes. Reassembly overflow crashed old OSes. Mostly historical.</td><td>Modern OSes immune. Still filter at NGFW for defence-in-depth</td></tr>
<tr><td><strong>ICMP Redirect Attack</strong></td><td>Type 5</td><td>Forged Redirect message tricks host into routing traffic through attacker's host (man-in-the-middle)</td><td>Block ICMP Type 5 from external sources</td></tr>
<tr><td><strong>ICMP Tunnelling</strong></td><td>Type 8/0 (Echo)</td><td>Data exfiltration by encoding payload in the "data" field of ping packets. Bypasses DNS/HTTP-based content filters</td><td>Deep inspect ICMP data field. Detect non-standard ICMP payload (e.g., non-zero data, large payloads, high frequency)</td></tr>
<tr><td><strong>OS Fingerprinting</strong></td><td>Type 8 + responses</td><td>Different OSes have slightly different ICMP behaviours (TTL starting values, window sizes, flags in unreachable messages). Used to identify OS without connecting</td><td>Normalise ICMP responses (strip OS-identifying quirks)</td></tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- ════════════ TAB 8 — LABS ════════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Build a UDP Echo Server and Analyse Traffic</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write a UDP echo server in C, send datagrams to it, capture the traffic, and compare the overhead profile against TCP. Understand message-boundary preservation and stateless operation.</p>
<div class="lab-step"><div class="sn">1</div><div>Write a UDP echo server in C: create AF_INET SOCK_DGRAM socket, bind to port 9000, loop on recvfrom() and sendto() the data back. Compile and run: <code>gcc -o udp_echo server.c && ./udp_echo</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Send test datagrams with netcat: <code>echo "Hello UDP" | nc -u 127.0.0.1 9000</code>. Send multiple: <code>for i in $(seq 1 5); do echo "msg $i" | nc -u 127.0.0.1 9000; done</code>. Capture with Wireshark filter: <code>udp.port == 9000</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div><strong>Compare overhead:</strong> Count bytes per message. A "Hello UDP" message (9 bytes) over UDP: 8B UDP + 20B IP + 14B Ethernet = 42B overhead + 9B data = 51B total. Same message over TCP would need: 3-way handshake (3 packets × ~60B each = ~180B) + data segment + FIN sequence (~240B). For a single short message, UDP is vastly more efficient.</div></div>
<div class="lab-step"><div class="sn">4</div><div><strong>Message boundary test:</strong> In your server, call recvfrom() once. Send three messages rapidly from the client. Observe that recvfrom() returns exactly one message per call — each sendto() is a distinct datagram. Compare: with TCP read(), you'd need to implement your own message framing (length prefix, newline delimiter, etc.).</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Packet loss simulation:</strong> Add simulated packet loss with netem: <code>sudo tc qdisc add dev lo root netem loss 30%</code>. Run your test again. Some messages are lost — neither client nor server notices or retransmits. This is UDP's behaviour by design. Remove with: <code>sudo tc qdisc del dev lo root</code>.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus — QUIC comparison:</strong> Install quiche or ngtcp2 library, or simply observe that QUIC (HTTP/3) runs on UDP 443. Use: <code>curl --http3 https://cloudflare.com</code> (if your curl supports HTTP/3). Capture with Wireshark — filter <code>udp.port == 443</code>. You'll see QUIC's own reliability and multiplexing running on top of raw UDP datagrams.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>ICMP Deep Analysis — Ping, Traceroute, and PMTUD</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Capture and fully decode ICMP messages. Understand every field in Echo Request, Time Exceeded, and Destination Unreachable. Test PMTUD with DF=1 pings. Detect ICMP tunnelling.</p>
<div class="lab-step"><div class="sn">1</div><div><strong>Echo Request/Reply decode:</strong> Start Wireshark with filter <code>icmp</code>. Run <code>ping -c 3 8.8.8.8</code>. For each Echo Request packet: find Type (8), Code (0), Identifier, Sequence Number, payload bytes. For each Echo Reply: verify same Identifier and Sequence. Measure RTT from Wireshark timestamps vs ping output — they should match.</div></div>
<div class="lab-step"><div class="sn">2</div><div><strong>Traceroute decode:</strong> Run <code>sudo traceroute -n 8.8.8.8</code> while capturing with filter <code>icmp or udp.port >= 33434</code>. For each TTL-Exceeded reply: expand the ICMP payload — find the embedded original IP header and first 8 bytes of the original UDP datagram. This is how the sender knows which probe triggered the error.</div></div>
<div class="lab-step"><div class="sn">3</div><div><strong>PMTUD test:</strong> Try <code>ping -M do -s 1473 8.8.8.8</code> (DF=1, payload 1473 bytes = 1501B IP packet, exceeds 1500 MTU). You should get "Frag needed" ICMP Type 3 Code 4 back from your router. Capture it. In the ICMP message, find the "Next-Hop MTU" field — it tells you the MTU of the problematic link.</div></div>
<div class="lab-step"><div class="sn">4</div><div><strong>Port Unreachable (UDP probe):</strong> Send a UDP packet to a closed port: <code>nc -u 8.8.8.8 9999</code> then type anything and Enter. Capture the ICMP Type 3 Code 3 response. Expand it: find the original UDP header embedded in the ICMP payload — verify src_port, dst_port=9999.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>ICMP tunnelling demo:</strong> Use hping3 to put arbitrary data in ICMP packets: <code>sudo hping3 -1 --icmp-type 8 --data 64 -e "SECRET DATA" 127.0.0.1</code>. Capture with Wireshark. In the hex dump of the ICMP payload, find your "SECRET DATA" string. This is exactly how ICMP tunnelling tools (like icmptunnel or ptunnel) exfiltrate data — the NGFW must inspect the ICMP data field.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Scapy ICMP crafting:</strong> <code>from scapy.all import *; send(IP(dst="127.0.0.1")/ICMP(type=5, code=1, gw="10.0.0.254")/IP(dst="8.8.8.8")/UDP())</code> — this crafts an ICMP Redirect message. Observe what the Linux kernel does with it (it may update the routing cache). This is the ICMP Redirect attack vector — your NGFW should block Type 5 from external sources.</div></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 9 — CHECKLIST ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">M06 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain UDP's 6 properties: connectionless, unreliable, unordered, message-oriented, no flow control, no congestion control</li>
  <li>Know the 4 UDP header fields and sizes: Source Port(16), Dest Port(16), Length(16), Checksum(16) = 8 bytes total</li>
  <li>Know that UDP checksum is optional in IPv4 (0=disabled) but mandatory in IPv6</li>
  <li>Know that Source Port can be 0 in UDP (sender doesn't need replies)</li>
  <li>Understand the recvfrom/sendto pattern for UDP: no connect(), no accept(), one socket handles all clients</li>
  <li>Know why message boundaries are preserved in UDP: 1 sendto() = 1 recvfrom(), unlike TCP streams</li>
  <li>Know 8+ protocols that use UDP and why each chose UDP over TCP (DNS, DHCP, NTP, SNMP, TFTP, SIP/VoIP, QUIC, IKEv2)</li>
  <li>Understand RTP: sequence numbers + timestamps + SSRC over UDP for real-time media</li>
  <li>Know how NGFWs track "stateless" UDP: pseudo-session by 5-tuple + idle timeout</li>
  <li>Know different UDP idle timeouts: DNS(5s), VoIP(180s), generic(30s)</li>
  <li>Know 6 UDP attack types: UDP flood, amplification/DRDoS, DNS amplification, port scan, fragmented UDP, TFTP abuse</li>
  <li>Know ICMP message structure: Type(8), Code(8), Checksum(16), Type-specific(32) + variable payload</li>
  <li>Know all key ICMP types by number: 0=Echo Reply, 3=Unreachable, 4=Source Quench(deprecated), 5=Redirect, 8=Echo Request, 11=TTL Exceeded, 12=Parameter Problem</li>
  <li>Know the 4 most important Type 3 codes: 0=Net, 1=Host, 3=Port, 4=Frag Needed</li>
  <li>Know why Type 3 Code 4 (Frag Needed) must never be blocked: PMTUD depends on it</li>
  <li>Can explain exactly how traceroute works: TTL=1,2,3... probes, collect ICMP Type 11 from each hop, detect destination by ICMP Type 3 Code 3 (or Type 0 for ICMP mode)</li>
  <li>Know what "* * *" means in traceroute: ICMP blocked/rate-limited at that hop, NOT necessarily broken path</li>
  <li>Know the RTT interpretation tricks: TTL at receiver reveals starting TTL and hop count</li>
  <li>Know the multicast address range: 224.0.0.0/4 (Class D)</li>
  <li>Know 6 important multicast addresses: 224.0.0.1 (all hosts), 224.0.0.2 (all routers), 224.0.0.5 (OSPF), 224.0.0.6 (OSPF DR), 224.0.0.18 (VRRP), 239.0.0.0/8 (org-local)</li>
  <li>Know IGMP's role: hosts join/leave multicast groups, routers track membership per interface</li>
  <li>Know 3 IGMP versions and the key addition in each: v1=basic, v2=Leave Group, v3=source-specific</li>
  <li>Know the correct NGFW ICMP policy: always allow Type 3 Code 4, block Type 5 (Redirect), rate-limit Type 8 (Echo Request)</li>
  <li>Know 6 ICMP attack types: Ping Flood, Smurf, Ping of Death, Redirect Attack, ICMP Tunnelling, OS Fingerprinting</li>
  <li>Know how to detect ICMP tunnelling: non-standard data field content, large payload size, high frequency of pings</li>
  <li>Completed Lab 1: built UDP echo server in C, verified message boundaries, tested packet loss with netem</li>
  <li>Completed Lab 2: decoded ICMP Echo/TTL-Exceeded/Port-Unreachable in Wireshark, tested PMTUD, demonstrated ICMP tunnelling and Redirect crafting with Scapy</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M07 - DNS</strong>. DNS is one of the most important protocols for NGFW — DNS-based filtering, sinkholing, and exfiltration detection are major NGFW features. DNS runs over UDP (primarily) but uses TCP for large responses, and its query/response format is a common DPI target.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m05-tcp/">← M05 TCP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m07-dns/">Next: M07 - DNS →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
