---
title: "M01 - OSI and TCP/IP Model"
description: "NETWORKING MASTERY · PHASE 1 · MODULE 01 · WEEK 1 📡 OSI and TCP/IP Model How networks are structured · Layers · Encapsulation · Protocols · PDUs Beginner No prior knowledge…"
domain: networking
track: networking-mastery
order: 1
ownHeader: true
url: /learning/networking-mastery/m01-osi-tcpip/
---

<style>
/* ── Base ─────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 55%,#0f6e56 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;
  color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8cce0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8e4f4}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd6c8;border-bottom-color:#5dd6c8}
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
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #0f6e56}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8e8d8;white-space:pre}
.cm{color:#4a7a5a}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight + warning boxes */
.ins{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}
[data-theme=dark] .ins strong{color:#5dd6c8}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

/* OSI Stack visual */
.osi-stack{display:flex;flex-direction:column;gap:3px;margin:1rem 0}
.osi-layer{
  display:grid;grid-template-columns:36px 110px 1fr auto;
  align-items:center;gap:10px;
  padding:10px 14px;border-radius:8px;
  border:1.5px solid transparent;cursor:pointer;
  transition:transform .12s,box-shadow .12s;
}
.osi-layer:hover{transform:translateX(5px);box-shadow:0 2px 12px rgba(0,0,0,.08)}
.osi-layer-num{font-size:1.1rem;font-weight:800;text-align:center;font-family:monospace}
.osi-layer-name{font-size:.88rem;font-weight:700}
.osi-layer-desc{font-size:.8rem;line-height:1.5;color:var(--text-color,#444)}
.osi-layer-pdu{font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;text-align:right}

/* Layer colours */
.l7{background:#f0ecfc;border-color:#b0a0e0}.l7 .osi-layer-num{color:#5b3a8c}
.l6{background:#e8f0fc;border-color:#a0b8e8}.l6 .osi-layer-num{color:#1a3a8c}
.l5{background:#e0f0f8;border-color:#90c8e0}.l5 .osi-layer-num{color:#1a5a7c}
.l4{background:#e0f0ee;border-color:#90c8b8}.l4 .osi-layer-num{color:#0f5a48}
.l3{background:#e8f5e8;border-color:#a0d0a0}.l3 .osi-layer-num{color:#1a5a1a}
.l2{background:#fdf4dc;border-color:#e8c870}.l2 .osi-layer-num{color:#7a5800}
.l1{background:#faeee4;border-color:#e8b090}.l1 .osi-layer-num{color:#8c3a0a}
[data-theme=dark] .l7{background:#1c1030;border-color:#7060a8}
[data-theme=dark] .l6{background:#101830;border-color:#6080c0}
[data-theme=dark] .l5{background:#0c1e28;border-color:#4090b0}
[data-theme=dark] .l4{background:#0a2020;border-color:#3a9080}
[data-theme=dark] .l3{background:#0c2010;border-color:#3a8040}
[data-theme=dark] .l2{background:#201800;border-color:#c09030}
[data-theme=dark] .l1{background:#1e1000;border-color:#b06030}

/* Encapsulation diagram */
.encap-wrap{margin:1rem 0}
.encap-row{display:flex;align-items:stretch;gap:3px;margin-bottom:4px}
.encap-label{font-size:.75rem;font-family:monospace;font-weight:700;min-width:90px;display:flex;align-items:center;color:var(--light-text,#666)}
.encap-block{
  flex:1;padding:8px 10px;border-radius:6px;
  font-size:.75rem;font-weight:600;text-align:center;
  border:1.5px solid transparent;display:flex;align-items:center;justify-content:center;
}
.eb-app {background:#f0ecfc;border-color:#b0a0e0;color:#3a1a6c}
.eb-tcp {background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.eb-ip  {background:#e8f5e8;border-color:#a0d0a0;color:#1a4a1a}
.eb-eth {background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.eb-bit {background:#faeee4;border-color:#e8b090;color:#6a2800}
.eb-new {outline:2px solid #1a7a6e;outline-offset:1px}
.encap-arrow{text-align:center;font-size:1rem;color:var(--light-text,#888);padding:2px 0}
[data-theme=dark] .eb-app{background:#1c1030;border-color:#7060a8;color:#c0a8f0}
[data-theme=dark] .eb-tcp{background:#0a2020;border-color:#3a9080;color:#80d8c0}
[data-theme=dark] .eb-ip {background:#0c2010;border-color:#3a8040;color:#80d890}
[data-theme=dark] .eb-eth{background:#201800;border-color:#c09030;color:#f0d080}
[data-theme=dark] .eb-bit{background:#1e1000;border-color:#b06030;color:#f0b070}

/* TCP/IP model comparison table */
.model-compare{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.86rem}
.model-compare th{background:#1a3a5c;color:#fff;padding:.55rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.model-compare td{padding:.5rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:middle}
.model-compare tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.model-compare code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#0f6e56}

/* Analogy box */
.analogy{
  background:linear-gradient(135deg,#f0f8ff,#e8f5f0);
  border:1.5px solid #90c8d8;border-radius:10px;
  padding:1.1rem 1.2rem;margin:1rem 0;
}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1820,#0a2020);border-color:#306880}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#0f6e56;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#5dd6c8}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* Protocol examples per layer */
.proto-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.6rem;margin:.8rem 0}
.proto-card{border-radius:8px;padding:.7rem 1rem;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff)}
.proto-card-layer{font-size:.68rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.3rem}
.proto-card-items{font-size:.82rem;color:var(--text-color,#333);line-height:1.6}

/* PDU header/trailer breakdown */
.pdu-breakdown{margin:1rem 0}
.pdu-row{display:flex;gap:2px;margin-bottom:.3rem;align-items:stretch}
.pdu-field{
  border-radius:5px;padding:6px 8px;font-size:.72rem;
  font-weight:600;text-align:center;border:1.5px solid transparent;
  min-width:0;flex-shrink:0;
}
.pdu-spacer{flex:1;min-width:0}
.pdu-label{font-size:.72rem;font-family:monospace;min-width:90px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0}

/* Data path flow */
.flow-path{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fp-step{
  display:flex;gap:14px;padding:10px 14px;
  border-left:2px solid var(--border-color,#e0e0e0);
  margin-left:14px;position:relative;
}
.fp-step::before{
  content:attr(data-n);position:absolute;left:-14px;top:12px;
  width:26px;height:26px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:.72rem;font-weight:700;color:#fff;
  background:var(--step-col,#1a3a5c);
}
.fp-step:last-child{border-left-color:transparent}
.fp-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fp-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fp-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#7ab8d8;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Lab box */
.lab-box{border:2px solid #0f6e56;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#0f6e56;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#0f6e56;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#0f6e56;margin-top:-.05rem}

/* Nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}

/* Section divider */
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
</style>
<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 1 · MODULE 01 · WEEK 1</div>
  <div class="mod-title">📡 OSI and TCP/IP Model</div>
  <div class="mod-subtitle">How networks are structured · Layers · Encapsulation · Protocols · PDUs</div>
  <div class="mod-pills">
    <span class="mod-pill">Beginner</span>
    <span class="mod-pill">No prior knowledge needed</span>
    <span class="mod-pill">7 Layers</span>
    <span class="mod-pill">Encapsulation</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Why Layers?</button>
  <button class="tab-btn" onclick="vt(event,'t1')">OSI Model</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Each Layer Explained</button>
  <button class="tab-btn" onclick="vt(event,'t3')">TCP/IP Model</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Encapsulation</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Protocols per Layer</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Data Flow End-to-End</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- ══════════ TAB 0 — WHY LAYERS ══════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THE PROBLEM LAYERS SOLVE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤔</span><h3>Why Does Networking Need a Layered Model?</h3><span class="tag tag-blue">MOTIVATION</span></div>
  <div class="cp-body">
    <p>Imagine you want to send a message to a friend in another country. You don't think about the physics of radio waves, the routing protocols in backbone routers, the TCP retransmit timers, or the TLS cipher negotiation. You just type and hit send. That's possible because networking is broken into <strong>layers</strong> — each layer does one specific job and hides the complexity from the layers above and below it.</p>
    <p>Without layers, every application would need to understand every type of network hardware, every cable standard, every routing algorithm. It would be impossible to maintain. Layers solve this with a principle called <strong>separation of concerns</strong>:</p>
    <ul>
      <li>Each layer has a <strong>clearly defined job</strong>.</li>
      <li>Each layer communicates only with the <strong>layer directly above and below</strong> it.</li>
      <li>A layer can be <strong>swapped or upgraded</strong> without touching other layers. WiFi replaced Ethernet as the physical layer for laptops — no change to TCP, HTTP, or your app.</li>
      <li>When something breaks, layers tell you <strong>exactly where to look</strong>. "Is this a Layer 1 cable problem, or a Layer 3 routing problem?"</li>
    </ul>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">📮 Analogy — Sending a Physical Letter</div>
  <p>Think of layers like the postal system. You (the app) write a letter and seal it in an envelope (Layer 6/5). The envelope gets a delivery address and return address (Layer 3 — IP addressing). It gets placed in a mail bag (Layer 2 — grouped for a specific route). The mail bag travels by truck, plane, boat (Layer 1 — physical transport). At each stage, that layer's workers do their specific job without needing to read your personal letter. The letter arrives, gets opened, and you read it — each layer unwrapped in reverse. This is exactly what happens to network packets.</p>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📜</span><h3>Two Models — OSI and TCP/IP</h3><span class="tag tag-teal">OVERVIEW</span></div>
  <div class="cp-body">
    <p>There are two main layered models you'll encounter:</p>
    <ul>
      <li><strong>OSI Model (Open Systems Interconnection)</strong> — A theoretical 7-layer model created by the ISO in 1984. It is the reference standard used for understanding, teaching, and troubleshooting. You will use OSI terminology every day as a network engineer ("that's a Layer 3 issue", "this operates at Layer 4").</li>
      <li><strong>TCP/IP Model</strong> — The practical 4-layer model that describes how the actual internet works. This is what your operating system and every network device actually implements. It maps onto the OSI model but collapses some layers together.</li>
    </ul>
    <p>Both models exist for different reasons. OSI gives you precise vocabulary and troubleshooting clarity. TCP/IP tells you how real implementations work. You need to know both — and more importantly, how they map to each other.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — OSI MODEL ══════════ -->
<div id="t1" class="tab-pane">
<p class="sep">THE 7-LAYER OSI MODEL — VISUAL REFERENCE</p>
<div class="cp-body" style="padding:0">
<p style="font-size:.88rem;color:var(--text-color,#444);margin:.5rem 0 1rem;line-height:1.65">The OSI model has 7 layers numbered 1 (bottom, physical) to 7 (top, application). Each layer adds its own header/trailer to data as it travels down the stack (sender side), and strips it off as it travels up (receiver side). Click any layer to learn more.</p>
</div>
<div class="osi-stack">
  <div class="osi-layer l7" onclick="vt_direct('t2','s7')">
    <div class="osi-layer-num">7</div>
    <div class="osi-layer-name">Application</div>
    <div class="osi-layer-desc">User-facing protocols. HTTP, DNS, SMTP, FTP, SSH. Your app lives here.</div>
    <div class="osi-layer-pdu" style="background:#ede8f5;color:#3a1a6c">Data</div>
  </div>
  <div class="osi-layer l6" onclick="vt_direct('t2','s6')">
    <div class="osi-layer-num">6</div>
    <div class="osi-layer-name">Presentation</div>
    <div class="osi-layer-desc">Data format translation, encryption (TLS/SSL), compression.</div>
    <div class="osi-layer-pdu" style="background:#e8f0fc;color:#1a3a8c">Data</div>
  </div>
  <div class="osi-layer l5" onclick="vt_direct('t2','s5')">
    <div class="osi-layer-num">5</div>
    <div class="osi-layer-name">Session</div>
    <div class="osi-layer-desc">Manages sessions between applications. Setup, maintenance, teardown.</div>
    <div class="osi-layer-pdu" style="background:#e0f0f8;color:#1a5a7c">Data</div>
  </div>
  <div class="osi-layer l4" onclick="vt_direct('t2','s4')">
    <div class="osi-layer-num">4</div>
    <div class="osi-layer-name">Transport</div>
    <div class="osi-layer-desc">End-to-end delivery. TCP (reliable) and UDP (fast). Ports live here.</div>
    <div class="osi-layer-pdu" style="background:#c8e8e4;color:#0e5248">Segment</div>
  </div>
  <div class="osi-layer l3" onclick="vt_direct('t2','s3')">
    <div class="osi-layer-num">3</div>
    <div class="osi-layer-name">Network</div>
    <div class="osi-layer-desc">Logical addressing and routing. IP addresses, routers, FIB/RIB.</div>
    <div class="osi-layer-pdu" style="background:#c8e8c8;color:#1a4a1a">Packet</div>
  </div>
  <div class="osi-layer l2" onclick="vt_direct('t2','s2')">
    <div class="osi-layer-num">2</div>
    <div class="osi-layer-name">Data Link</div>
    <div class="osi-layer-desc">Node-to-node delivery on same network. MAC addresses, Ethernet frames, switches.</div>
    <div class="osi-layer-pdu" style="background:#fae8a0;color:#5a3800">Frame</div>
  </div>
  <div class="osi-layer l1" onclick="vt_direct('t2','s1')">
    <div class="osi-layer-num">1</div>
    <div class="osi-layer-name">Physical</div>
    <div class="osi-layer-desc">Raw bits over physical medium. Cables, optical fibre, radio waves, voltages.</div>
    <div class="osi-layer-pdu" style="background:#fad8b8;color:#6a2800">Bits</div>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>Memory trick — "Please Do Not Throw Sausage Pizza Away"</strong> (Physical, Data Link, Network, Transport, Session, Presentation, Application — bottom to top). Or top-to-bottom: "All People Seem To Need Data Processing". Either works — pick one and stick to it.</p>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📦</span><h3>PDU — Protocol Data Unit</h3><span class="tag tag-orange">KEY TERM</span></div>
  <div class="cp-body">
    <p>Each layer has a specific name for the chunk of data it works with. These are called <strong>PDUs (Protocol Data Units)</strong>:</p>
    <ul>
      <li><strong>Layer 7/6/5</strong> — just called <strong>Data</strong> (your application message)</li>
      <li><strong>Layer 4</strong> — <strong>Segment</strong> (TCP) or <strong>Datagram</strong> (UDP)</li>
      <li><strong>Layer 3</strong> — <strong>Packet</strong> (IP packet)</li>
      <li><strong>Layer 2</strong> — <strong>Frame</strong> (Ethernet frame)</li>
      <li><strong>Layer 1</strong> — <strong>Bits</strong> (1s and 0s on the wire)</li>
    </ul>
    <p>In network engineering conversations, using the right PDU name matters. A "packet" is specifically an L3 PDU. Calling an Ethernet frame a "packet" is technically wrong and can confuse your team when debugging.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 2 — EACH LAYER EXPLAINED ══════════ -->
<div id="t2" class="tab-pane">
<p class="sep">EACH LAYER — WHAT IT DOES, WHAT PROTOCOLS LIVE HERE</p>
<!-- Layer 7 -->
<div id="s7" class="cp p-purple">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Layer 7 — Application Layer</h3><span class="tag tag-purple">L7 · DATA</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Provides network services directly to user applications. This is the layer your code interacts with when you call <code>curl</code>, open a browser, or write a socket program.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li>Defines the <strong>syntax and semantics</strong> of the messages exchanged (e.g., HTTP request format: <code>GET /index.html HTTP/1.1</code>)</li>
      <li>Handles <strong>application-level authentication</strong> (HTTP Basic Auth, API keys)</li>
      <li>No header is added by the OS at this layer — the application itself constructs the message</li>
    </ul>
    <p><strong>Protocols:</strong> HTTP/HTTPS, DNS, SMTP, FTP, SSH, Telnet, DHCP, SNMP, LDAP, SIP, RTP</p>
    <p><strong>NGFW relevance:</strong> This is where DPI (Deep Packet Inspection) operates. An NGFW inspects L7 content to identify applications, detect malware payloads, and enforce URL/content policies.</p>
  </div>
</div>
<!-- Layer 6 -->
<div id="s6" class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>Layer 6 — Presentation Layer</h3><span class="tag tag-blue">L6 · DATA</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Translates data between the format the network uses and the format the application needs. Acts as a <strong>data translator</strong>.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li><strong>Encryption / Decryption</strong> — TLS/SSL encrypts data at this layer before it goes down to L4/L3</li>
      <li><strong>Compression</strong> — HTTP compression (gzip, brotli) is a Layer 6 function</li>
      <li><strong>Data format translation</strong> — Converting between character encodings (ASCII vs UTF-8), serialisation formats (JSON → binary)</li>
    </ul>
    <p><strong>Real-world note:</strong> In practice, the OSI Presentation layer is not implemented as a distinct OS layer. TLS runs as a library your application calls (OpenSSL, mbedTLS). The <em>concept</em> is still useful — when you say "TLS is a Layer 6 function", everyone understands you mean it handles the encryption/format translation concern, not transport or routing.</p>
    <p><strong>NGFW relevance:</strong> SSL inspection (decrypting HTTPS traffic for inspection) is a Layer 6 operation.</p>
  </div>
</div>
<!-- Layer 5 -->
<div id="s5" class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Layer 5 — Session Layer</h3><span class="tag tag-teal">L5 · DATA</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Establishes, manages, and terminates <strong>sessions</strong> — logical conversations between two applications.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li><strong>Session establishment</strong> — setting up a logical connection before data flows</li>
      <li><strong>Session maintenance</strong> — keeping the session alive (keepalives), handling disconnects and reconnects</li>
      <li><strong>Synchronisation</strong> — checkpointing long transfers so they can resume after interruption</li>
      <li><strong>Dialog control</strong> — managing half-duplex vs full-duplex communication</li>
    </ul>
    <p><strong>Real-world note:</strong> Like Layer 6, Session is not a distinct OS layer in practice. The functionality is handled by TCP (connection state), TLS (session tickets for resumption), and application-level session management (HTTP cookies, WebSocket sessions). You'll use Layer 5 as a concept more than as a distinct implementation concern.</p>
    <p><strong>Protocols:</strong> NetBIOS, PPTP, RPC session management, SQL session management</p>
  </div>
</div>
<!-- Layer 4 -->
<div id="s4" class="cp p-green">
  <div class="cp-hdr"><span class="ico">🚚</span><h3>Layer 4 — Transport Layer</h3><span class="tag tag-green">L4 · SEGMENT</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Reliable (or unreliable) end-to-end delivery of data between two processes on different hosts. This is where <strong>ports</strong> live — they are how Layer 4 distinguishes which application a packet belongs to.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li><strong>Port numbers</strong> — Source port + destination port identify the application. Port 80 = HTTP, 443 = HTTPS, 22 = SSH, 53 = DNS (UDP)</li>
      <li><strong>Segmentation</strong> — Large application messages are broken into segments. Each segment is numbered so the receiver can reassemble them in order</li>
      <li><strong>Flow control</strong> — TCP adjusts the sending rate so the receiver isn't overwhelmed</li>
      <li><strong>Error detection</strong> — Checksum verifies data wasn't corrupted in transit</li>
      <li><strong>Multiplexing</strong> — Multiple applications can use the network simultaneously because they each have unique port numbers</li>
    </ul>
    <p><strong>Two protocols:</strong></p>
    <ul>
      <li><strong>TCP (Transmission Control Protocol)</strong> — Reliable, ordered, connection-oriented. Guarantees delivery. Used by HTTP, SMTP, SSH. Slower but safe.</li>
      <li><strong>UDP (User Datagram Protocol)</strong> — Unreliable, connectionless, no ordering. Fast, no overhead. Used by DNS, video streaming, VoIP, gaming. You handle reliability yourself if you need it.</li>
    </ul>
    <p><strong>NGFW relevance:</strong> Stateful firewalls operate at Layer 4. Connection tracking matches packets to established sessions by (src_ip, src_port, dst_ip, dst_port, proto) — the 5-tuple.</p>
  </div>
</div>
<!-- Layer 3 -->
<div id="s3" class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>Layer 3 — Network Layer</h3><span class="tag tag-amber">L3 · PACKET</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Logical addressing and routing of packets across multiple networks. This is the layer that makes the <strong>internet</strong> possible — the ability to send data from any network to any other network, potentially traversing dozens of routers in between.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li><strong>IP addressing</strong> — Assigns logical addresses (IPv4: 192.168.1.1, IPv6: 2001:db8::1) that identify hosts globally, not just on a local network</li>
      <li><strong>Routing</strong> — Determines the best path for a packet to travel. Routers operate at Layer 3, reading the destination IP and consulting their routing table (FIB) to decide the next hop</li>
      <li><strong>Fragmentation</strong> — If a packet is too large for a network link's MTU (Maximum Transmission Unit), Layer 3 fragments it into smaller packets</li>
      <li><strong>TTL (Time To Live)</strong> — Each packet has a TTL counter decremented by each router. When it hits 0 the packet is discarded — prevents loops</li>
    </ul>
    <p><strong>Protocols:</strong> IPv4, IPv6, ICMP, OSPF, BGP, EIGRP, ARP (technically L2/L3 boundary)</p>
    <p><strong>Devices at this layer:</strong> Routers, Layer 3 switches, firewalls (packet inspection)</p>
    <p><strong>NGFW relevance:</strong> Every packet processed by a firewall goes through Layer 3 — source/destination IP ACLs, routing decisions, and IP-based threat intelligence all live here.</p>
  </div>
</div>
<!-- Layer 2 -->
<div id="s2" class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Layer 2 — Data Link Layer</h3><span class="tag tag-orange">L2 · FRAME</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Node-to-node delivery of data on the <em>same</em> physical network. While Layer 3 handles routing across many networks, Layer 2 handles the hop-by-hop delivery on each individual link.</p>
    <p><strong>What it does:</strong></p>
    <ul>
      <li><strong>MAC addressing</strong> — Uses hardware (MAC) addresses to identify devices on the same network segment. Unlike IP addresses, MAC addresses are burned into the NIC at manufacture (though they can be spoofed)</li>
      <li><strong>Framing</strong> — Wraps Layer 3 packets in a frame with MAC src/dst header and a trailer containing a CRC checksum for error detection</li>
      <li><strong>Error detection</strong> — The CRC (Cyclic Redundancy Check) in the Ethernet trailer detects corrupted frames. Corrupted frames are silently dropped (error recovery is Layer 4's job)</li>
      <li><strong>Access control</strong> — CSMA/CD (old Ethernet) and CSMA/CA (WiFi) decide who can transmit when</li>
    </ul>
    <p><strong>Two sub-layers (important for NGFW):</strong></p>
    <ul>
      <li><strong>LLC (Logical Link Control)</strong> — flow control and error notification to upper layers</li>
      <li><strong>MAC (Media Access Control)</strong> — hardware addressing and media access</li>
    </ul>
    <p><strong>Protocols:</strong> Ethernet (802.3), WiFi (802.11), PPP, VLAN (802.1Q), STP (802.1D), ARP</p>
    <p><strong>Devices:</strong> Network switches, bridges, NICs, WiFi access points</p>
  </div>
</div>
<!-- Layer 1 -->
<div id="s1" class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Layer 1 — Physical Layer</h3><span class="tag tag-red">L1 · BITS</span></div>
  <div class="cp-body">
    <p><strong>Job:</strong> Transmit raw bits (1s and 0s) over a physical medium. This layer knows nothing about addresses, protocols, or meaning — it just pushes electrical signals, light pulses, or radio waves.</p>
    <p><strong>What it defines:</strong></p>
    <ul>
      <li><strong>Physical connectors</strong> — RJ45 (Ethernet), SFP (fibre), coaxial</li>
      <li><strong>Cable types</strong> — Cat5e, Cat6, Cat6A (copper), single-mode, multi-mode fibre</li>
      <li><strong>Signal encoding</strong> — How bits 0 and 1 are represented as voltages, light intensity, or radio frequency</li>
      <li><strong>Bit rate</strong> — 100 Mbps, 1 Gbps, 10 Gbps, 100 Gbps</li>
      <li><strong>Duplex mode</strong> — Half-duplex (one direction at a time) vs full-duplex (both directions simultaneously)</li>
    </ul>
    <p><strong>Devices:</strong> Hubs, repeaters, cables, optical transceivers, modems, NICs (the physical signalling part)</p>
    <p><strong>Troubleshooting:</strong> "Is the cable plugged in? Is the link light on?" — these are Layer 1 questions. In DPDK and VPP, <code>show interface</code> reports link state as "up" or "down" — this is a Layer 1 status.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 3 — TCP/IP MODEL ══════════ -->
<div id="t3" class="tab-pane">
<p class="sep">THE TCP/IP MODEL — HOW THE REAL INTERNET IS STRUCTURED</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>Why the TCP/IP Model Exists</h3><span class="tag tag-blue">BACKGROUND</span></div>
  <div class="cp-body">
    <p>The TCP/IP model (also called the Internet model or DoD model) was developed in the 1970s by DARPA as the actual protocol suite for ARPANET — the precursor to the internet. Unlike OSI, it wasn't a theoretical standard first — it was built pragmatically around the two core protocols: IP and TCP.</p>
    <p>It has <strong>4 layers</strong> instead of 7, collapsing the top three OSI layers into one and the bottom two into one. This reflects how implementations actually work — operating systems don't have separate Session and Presentation modules; they're handled by libraries your app calls.</p>
  </div>
</div>
<p class="sep">OSI vs TCP/IP — MAPPING</p>
<table class="model-compare">
  <thead>
    <tr>
      <th>TCP/IP Layer</th>
      <th>OSI Equivalent</th>
      <th>What It Covers</th>
      <th>Key Protocols</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="font-weight:700;background:#f0ecfc;color:#3a1a6c">Application</td>
      <td>L7 Application<br>L6 Presentation<br>L5 Session</td>
      <td>Everything from the OS socket API upward — your app, its data format, session management</td>
      <td><code>HTTP</code> <code>DNS</code> <code>SMTP</code> <code>FTP</code> <code>SSH</code> <code>TLS</code></td>
    </tr>
    <tr>
      <td style="font-weight:700;background:#e0f0ee;color:#0a3a30">Transport</td>
      <td>L4 Transport</td>
      <td>End-to-end data delivery between processes. Ports, reliability, flow control</td>
      <td><code>TCP</code> <code>UDP</code> <code>QUIC</code> <code>SCTP</code></td>
    </tr>
    <tr>
      <td style="font-weight:700;background:#e8f5e8;color:#1a4a1a">Internet</td>
      <td>L3 Network</td>
      <td>Logical addressing and routing across multiple networks</td>
      <td><code>IPv4</code> <code>IPv6</code> <code>ICMP</code> <code>OSPF</code> <code>BGP</code></td>
    </tr>
    <tr>
      <td style="font-weight:700;background:#fdf4dc;color:#5a3800">Network Access<br><span style="font-weight:400;font-size:.8rem">(Link Layer)</span></td>
      <td>L2 Data Link<br>L1 Physical</td>
      <td>Physical transmission and local network delivery</td>
      <td><code>Ethernet</code> <code>WiFi</code> <code>ARP</code> <code>PPP</code></td>
    </tr>
  </tbody>
</table>
<div class="ins">
  <p>💡 <strong>Which model do engineers actually use?</strong> Both, depending on context. When troubleshooting or talking to vendors, engineers use OSI layer numbers ("is this a L2 or L3 issue?"). When writing code and reading RFCs, you use TCP/IP model terminology. In NGFW development specifically, you'll hear "L3 ACL", "L4 stateful inspection", "L7 DPI" — these are OSI layer numbers applied to firewall feature descriptions.</p>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Where Does Each Protocol Actually Run?</h3><span class="tag tag-teal">REAL MAPPING</span></div>
  <div class="cp-body">
    <p>Understanding which layer a protocol belongs to is crucial — it tells you which device processes it, what header format to look for, and what tools to use for debugging.</p>
<div class="cb"><pre><span class="cm">/* In your OS — the TCP/IP stack as seen by a C program */</span>
 
Your application code
    ↓ calls socket(), send(), recv()
<span class="ck">OS socket API</span>          <span class="cm">← TCP/IP Application layer boundary</span>
    ↓
<span class="ck">TCP or UDP</span>             <span class="cm">← Transport layer (adds src/dst port, seq, ack)</span>
    ↓
<span class="ck">IP</span>                     <span class="cm">← Internet layer (adds src/dst IP, TTL, proto)</span>
    ↓
<span class="ck">Ethernet driver</span>        <span class="cm">← Network Access (adds MAC src/dst, type, CRC)</span>
    ↓
<span class="ck">NIC hardware</span>           <span class="cm">← Physical (converts to electrical/optical signals)</span>
    ↓
<span class="cs">wire / fibre / air</span></pre></div>
    <p>When you call <code>send(sockfd, buf, len, 0)</code> in C, the OS kernel handles everything below the socket API. Your app only touches the Application layer. The kernel builds the TCP segment, IP packet, and Ethernet frame automatically.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 4 — ENCAPSULATION ══════════ -->
<div id="t4" class="tab-pane">
<p class="sep">ENCAPSULATION AND DE-ENCAPSULATION</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>What is Encapsulation?</h3><span class="tag tag-blue">CORE CONCEPT</span></div>
  <div class="cp-body">
    <p>Encapsulation is the process of <strong>wrapping data with a header (and sometimes trailer) at each layer</strong> as it travels down the stack from the sending application to the physical wire. Each layer adds its own control information (addressing, error detection, sequencing) without modifying the data from the layer above.</p>
    <p>Think of it as nested envelopes — you put a letter in an envelope, then put that envelope in a padded mailer, then put that in a shipping box. Each wrapper adds information the relevant handler needs, without touching the inner contents.</p>
    <p>On the receiving end, the process reverses — each layer strips off its own header and passes the inner data up. This is called <strong>de-encapsulation</strong>.</p>
  </div>
</div>
<p class="sep">ENCAPSULATION STEP BY STEP — SENDING AN HTTP REQUEST</p>
<div class="encap-wrap">
  <div class="encap-row">
    <div class="encap-label">L7 App</div>
    <div class="encap-block eb-app eb-new" style="flex:4">HTTP Request: "GET /index.html HTTP/1.1\r\nHost: example.com\r\n"</div>
  </div>
  <div class="encap-arrow">↓ Transport layer wraps with TCP header</div>
  <div class="encap-row">
    <div class="encap-label">L4 Segment</div>
    <div class="encap-block eb-tcp eb-new" style="flex:1">TCP Header<br><span style="font-size:.65rem">src:52341 dst:80<br>seq:1001 ack:0<br>flags:PSH|ACK</span></div>
    <div class="encap-block eb-app" style="flex:4">HTTP Data</div>
  </div>
  <div class="encap-arrow">↓ Network layer wraps with IP header</div>
  <div class="encap-row">
    <div class="encap-label">L3 Packet</div>
    <div class="encap-block eb-ip eb-new" style="flex:1">IP Header<br><span style="font-size:.65rem">src:10.0.0.5<br>dst:93.184.216.34<br>TTL:64 proto:TCP</span></div>
    <div class="encap-block eb-tcp" style="flex:1">TCP Hdr</div>
    <div class="encap-block eb-app" style="flex:3">HTTP Data</div>
  </div>
  <div class="encap-arrow">↓ Data Link layer wraps with Ethernet header + trailer</div>
  <div class="encap-row">
    <div class="encap-label">L2 Frame</div>
    <div class="encap-block eb-eth eb-new" style="flex:1">Eth Header<br><span style="font-size:.65rem">dst MAC<br>src MAC<br>Type:0x0800</span></div>
    <div class="encap-block eb-ip" style="flex:1">IP Hdr</div>
    <div class="encap-block eb-tcp" style="flex:.8">TCP Hdr</div>
    <div class="encap-block eb-app" style="flex:2.5">HTTP Data</div>
    <div class="encap-block eb-eth eb-new" style="flex:.6">CRC<br><span style="font-size:.65rem">4 bytes</span></div>
  </div>
  <div class="encap-arrow">↓ Physical layer converts to bits on the wire</div>
  <div class="encap-row">
    <div class="encap-label">L1 Bits</div>
    <div class="encap-block eb-bit eb-new">01001000 01010100 01010100 01010000 ... (everything above as raw bits)</div>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>Important:</strong> The highlighted (outlined) blocks show what each layer <em>added</em>. Notice that each layer treats everything from the layer above as opaque data — IP does not look inside the TCP header; Ethernet does not look inside the IP header. This is the fundamental principle that makes the internet extensible — you can run any Layer 4 protocol over IP, and any Layer 3 protocol over Ethernet.</p>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📖</span><h3>Header Fields — What Each Layer Adds</h3><span class="tag tag-teal">REFERENCE</span></div>
  <div class="cp-body">
    <h4>Ethernet Frame Header (14 bytes)</h4>
    <div class="pdu-breakdown">
      <div class="pdu-row">
        <div class="pdu-label">Ethernet</div>
        <div class="pdu-field eb-eth" style="flex:3">Destination MAC<br><span style="font-size:.65rem;font-weight:400">6 bytes</span></div>
        <div class="pdu-field eb-eth" style="flex:3">Source MAC<br><span style="font-size:.65rem;font-weight:400">6 bytes</span></div>
        <div class="pdu-field eb-eth" style="flex:1.5">EtherType<br><span style="font-size:.65rem;font-weight:400">2 bytes</span></div>
        <div class="pdu-spacer" style="flex:2;font-size:.72rem;display:flex;align-items:center;padding:0 8px;color:var(--light-text,#888)">Payload (up to 1500B)</div>
        <div class="pdu-field eb-eth" style="flex:1">CRC<br><span style="font-size:.65rem;font-weight:400">4 bytes</span></div>
      </div>
    </div>
    <h4>IPv4 Header (20 bytes minimum)</h4>
    <div class="pdu-breakdown">
      <div class="pdu-row">
        <div class="pdu-label">IPv4</div>
        <div class="pdu-field eb-ip" style="flex:1">Ver/IHL<br><span style="font-size:.62rem;font-weight:400">1B</span></div>
        <div class="pdu-field eb-ip" style="flex:1">DSCP<br><span style="font-size:.62rem;font-weight:400">1B</span></div>
        <div class="pdu-field eb-ip" style="flex:1.5">Total Length<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-ip" style="flex:1.5">ID<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-ip" style="flex:1">TTL<br><span style="font-size:.62rem;font-weight:400">1B</span></div>
        <div class="pdu-field eb-ip" style="flex:1">Proto<br><span style="font-size:.62rem;font-weight:400">1B</span></div>
        <div class="pdu-field eb-ip" style="flex:1.5">Checksum<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-ip" style="flex:3">Source IP<br><span style="font-size:.62rem;font-weight:400">4 bytes</span></div>
        <div class="pdu-field eb-ip" style="flex:3">Dest IP<br><span style="font-size:.62rem;font-weight:400">4 bytes</span></div>
      </div>
    </div>
    <h4>TCP Header (20 bytes minimum)</h4>
    <div class="pdu-breakdown">
      <div class="pdu-row">
        <div class="pdu-label">TCP</div>
        <div class="pdu-field eb-tcp" style="flex:2">Src Port<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-tcp" style="flex:2">Dst Port<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-tcp" style="flex:3">Sequence Number<br><span style="font-size:.62rem;font-weight:400">4 bytes</span></div>
        <div class="pdu-field eb-tcp" style="flex:3">Ack Number<br><span style="font-size:.62rem;font-weight:400">4 bytes</span></div>
        <div class="pdu-field eb-tcp" style="flex:1.5">Flags<br><span style="font-size:.62rem;font-weight:400">1B</span></div>
        <div class="pdu-field eb-tcp" style="flex:2">Window<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
        <div class="pdu-field eb-tcp" style="flex:2">Checksum<br><span style="font-size:.62rem;font-weight:400">2B</span></div>
      </div>
    </div>
    <p style="font-size:.82rem;color:var(--light-text,#777);margin-top:.5rem">Each header will be dissected in detail in its own module — M02 for Ethernet, M03 for IPv4, M05 for TCP.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 5 — PROTOCOLS PER LAYER ══════════ -->
<div id="t5" class="tab-pane">
<p class="sep">PROTOCOLS MAPPED TO OSI LAYERS</p>
<div class="cp-body" style="padding:0 0 .5rem">
  <p style="font-size:.88rem;color:var(--text-color,#444);line-height:1.65">This is your reference map — every protocol you'll encounter in networking and NGFW development, mapped to the OSI layer it operates at. Study this until it's second nature.</p>
</div>
<div class="proto-grid">
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#5b3a8c">Layer 7 — Application</div>
    <div class="proto-card-items">HTTP · HTTPS · DNS · SMTP · FTP · SFTP · SSH · Telnet · DHCP · SNMP · LDAP · SIP · RTP · RTSP · NTP · POP3 · IMAP</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#1a3a8c">Layer 6 — Presentation</div>
    <div class="proto-card-items">TLS · SSL · MIME · ASCII · UTF-8 · JPEG · MPEG · gzip · XDR · ASN.1</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#1a5a7c">Layer 5 — Session</div>
    <div class="proto-card-items">NetBIOS · PPTP · SAP · SDP · NFS (session part) · SQL session · RPC</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#0f5a48">Layer 4 — Transport</div>
    <div class="proto-card-items">TCP · UDP · QUIC · SCTP · DCCP · SPX</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#1a5a1a">Layer 3 — Network</div>
    <div class="proto-card-items">IPv4 · IPv6 · ICMP · ICMPv6 · OSPF · EIGRP · BGP · IS-IS · RIP · MPLS · IPsec (tunnel mode) · GRE · ARP (boundary)</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#7a5800">Layer 2 — Data Link</div>
    <div class="proto-card-items">Ethernet (802.3) · WiFi (802.11) · PPP · HDLC · Frame Relay · ATM · VLAN (802.1Q) · STP (802.1D) · LACP (802.3ad) · ARP · NDP</div>
  </div>
  <div class="proto-card">
    <div class="proto-card-layer" style="color:#6a2800">Layer 1 — Physical</div>
    <div class="proto-card-items">Ethernet physical (100BASE-T, 1000BASE-T, 10GBASE-SR) · USB · RS-232 · DSL · SONET · OTN · Bluetooth (PHY) · 802.11 (radio PHY)</div>
  </div>
</div>
<div class="warn">
  <p>⚠️ <strong>Some protocols span multiple layers.</strong> ARP bridges L2 and L3 — it uses Ethernet frames (L2) to resolve IP addresses (L3). MPLS is sometimes called "Layer 2.5". IPsec in tunnel mode wraps an entire IP packet (L3) inside a new IP packet (L3) — it straddles L3 and L4. The OSI model is a framework; real protocols don't always fit neatly into one box.</p>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔥</span><h3>NGFW — Which Layer Does Each Feature Operate At?</h3><span class="tag tag-green">NGFW MAP</span></div>
  <div class="cp-body">
    <table class="model-compare">
      <thead><tr><th>NGFW Feature</th><th>OSI Layer</th><th>What It Inspects</th></tr></thead>
      <tbody>
        <tr><td>Packet filtering (ACL)</td><td>L3 / L4</td><td>IP src/dst, protocol, port numbers</td></tr>
        <tr><td>Stateful inspection</td><td>L4</td><td>TCP/UDP connection state (5-tuple)</td></tr>
        <tr><td>NAT (Network Address Translation)</td><td>L3 / L4</td><td>IP address and port rewriting</td></tr>
        <tr><td>Deep Packet Inspection (DPI)</td><td>L7</td><td>Application payload, protocol signatures</td></tr>
        <tr><td>URL filtering</td><td>L7</td><td>HTTP Host header, TLS SNI</td></tr>
        <tr><td>DNS filtering / sinkholing</td><td>L7</td><td>DNS query names, response IPs</td></tr>
        <tr><td>SSL inspection</td><td>L6 / L7</td><td>TLS handshake, certificate, decrypted payload</td></tr>
        <tr><td>IDS / IPS</td><td>L4 – L7</td><td>Packet content, protocol anomalies, signatures</td></tr>
        <tr><td>QoS / traffic shaping</td><td>L3 / L4</td><td>DSCP markings, port-based prioritisation</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>
<!-- ══════════ TAB 6 — DATA FLOW END-TO-END ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">END-TO-END DATA FLOW — HTTP REQUEST ACROSS TWO NETWORKS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>The Full Journey of a Packet</h3><span class="tag tag-blue">WALKTHROUGH</span></div>
  <div class="cp-body">
    <p>Scenario: Your laptop (<code>10.0.0.5</code>) sends an HTTP GET request to a web server (<code>93.184.216.34</code>) on the internet. There is one router between you and the internet. Let's trace every layer.</p>
  </div>
</div>
<div class="flow-path">
  <div class="fp-step" data-n="1" style="--step-col:#5b3a8c">
    <div>
      <div class="fp-title">Your Browser — L7 Application</div>
      <div class="fp-detail">Browser constructs an HTTP GET request: <code>GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n</code>. This is pure application data — no headers from lower layers yet. Passed down to the OS via the socket API.</div>
      <div class="fp-code">send(sockfd, "GET /index.html HTTP/1.1\r\n...", len, 0)</div>
    </div>
  </div>
  <div class="fp-step" data-n="2" style="--step-col:#0f5a48">
    <div>
      <div class="fp-title">OS Kernel — L4 Transport (TCP)</div>
      <div class="fp-detail">Kernel wraps the HTTP data in a TCP segment. Adds: source port (e.g. 52341, random ephemeral), destination port (80), sequence number (for ordering), flags (PSH+ACK). TCP ensures reliable delivery and handles retransmission if needed.</div>
      <div class="fp-code">[TCP hdr: sport=52341 dport=80 seq=1001 flags=PSH|ACK] + [HTTP data]</div>
    </div>
  </div>
  <div class="fp-step" data-n="3" style="--step-col:#1a5a1a">
    <div>
      <div class="fp-title">OS Kernel — L3 Network (IP)</div>
      <div class="fp-detail">IP layer wraps the TCP segment in an IP packet. Adds: source IP (10.0.0.5), destination IP (93.184.216.34), TTL (64), protocol (6 = TCP). The kernel consults the routing table: destination is not local, so next hop = default gateway (router at 10.0.0.1).</div>
      <div class="fp-code">[IP hdr: src=10.0.0.5 dst=93.184.216.34 TTL=64 proto=6] + [TCP] + [HTTP]</div>
    </div>
  </div>
  <div class="fp-step" data-n="4" style="--step-col:#7a5800">
    <div>
      <div class="fp-title">NIC Driver — L2 Data Link (Ethernet)</div>
      <div class="fp-detail">Ethernet layer wraps the IP packet in a frame. ARP resolves the router's MAC address (10.0.0.1 → aa:bb:cc:dd:ee:01). Adds: dst MAC (router's MAC), src MAC (your NIC's MAC), EtherType (0x0800 = IPv4), CRC trailer.</div>
      <div class="fp-code">[Eth: dst=aa:bb:cc:dd:ee:01 src=your_mac type=0x0800] + [IP] + [TCP] + [HTTP] + [CRC]</div>
    </div>
  </div>
  <div class="fp-step" data-n="5" style="--step-col:#6a2800">
    <div>
      <div class="fp-title">NIC Hardware — L1 Physical</div>
      <div class="fp-detail">The NIC converts the frame to electrical signals (or light pulses for fibre) and transmits them on the wire. The signals travel to the router's port.</div>
      <div class="fp-code">01001000 01010100 01010100... (raw bits on wire)</div>
    </div>
  </div>
  <div class="fp-step" data-n="6" style="--step-col:#1a3a5c">
    <div>
      <div class="fp-title">Router — L2 De-encapsulation + L3 Processing</div>
      <div class="fp-detail">Router receives bits → reassembles frame → checks CRC (drops if corrupt) → strips Ethernet header → reads IP header. Decrements TTL (64→63). Looks up destination IP (93.184.216.34) in its routing table → routes to ISP next hop. <strong>Builds a NEW Ethernet frame</strong> with the router's WAN MAC as source and the next-hop router's MAC as destination. The IP packet is unchanged (only TTL decremented).</div>
      <div class="fp-code">New Eth frame: [dst=isp_router_mac src=router_wan_mac] + [IP TTL=63] + [TCP] + [HTTP]</div>
    </div>
  </div>
  <div class="fp-step" data-n="7" style="--step-col:#0f6e56">
    <div>
      <div class="fp-title">Web Server — De-encapsulation (all layers)</div>
      <div class="fp-detail">Packet arrives at the server. NIC receives bits → Ethernet driver strips frame header/trailer → IP layer strips IP header (checks TTL, checksum, delivers to TCP) → TCP layer strips TCP header (checks sequence, sends ACK, passes data to socket buffer) → Application reads from socket → HTTP server processes GET request → sends response.</div>
      <div class="fp-code">recv(sockfd, buf, len, 0) → buf = "GET /index.html HTTP/1.1\r\nHost: example.com..."</div>
    </div>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>Key insight — the router only processes L1, L2, and L3.</strong> It strips the Ethernet frame, reads the IP destination, decrements TTL, builds a new Ethernet frame for the next hop, and forwards. It never looks at TCP or HTTP content. A firewall doing deep packet inspection is special because it deliberately reaches up to L4–L7 — which is why DPI is computationally expensive compared to simple IP routing.</p>
</div>
</div>
<!-- ══════════ TAB 7 — LABS ══════════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Packet Dissection with Wireshark</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Capture live traffic and identify every OSI layer in a real packet. See exactly how encapsulation looks on the wire.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install Wireshark on Linux: <code>sudo apt install wireshark</code>. On the first run, add your user to the wireshark group: <code>sudo usermod -aG wireshark $USER</code>, then log out and back in.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Open Wireshark. Select your active network interface (usually <code>eth0</code> or <code>wlan0</code>). Click the blue shark fin to start capture.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Open a terminal and run: <code>curl http://example.com</code>. This sends a plain HTTP request (not HTTPS — we want to see the payload).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>In Wireshark, type this filter in the filter bar and press Enter: <code>http and ip.dst == 93.184.216.34</code>. You should see the HTTP GET packet appear.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Click the packet. In the bottom panel, expand each layer: <strong>Frame</strong> (L2), <strong>Internet Protocol</strong> (L3), <strong>Transmission Control Protocol</strong> (L4), <strong>Hypertext Transfer Protocol</strong> (L7). For each layer, identify: header fields, their values, and their size in bytes.</div></div>
    <div class="lab-step"><div class="sn">6</div><div>Answer these questions from what you see: What is the source and destination MAC address? What is the TTL in the IP header? What are the source and destination ports? What HTTP method and path is being requested? Is there a TCP sequence number — what is it?</div></div>
    <div class="lab-step"><div class="sn">7</div><div><strong>Bonus:</strong> Right-click the packet and select "Follow > TCP Stream". See the full HTTP conversation — request and response — reassembled by Wireshark from multiple packets. Notice that Wireshark stripped all headers for you, showing only the L7 application data.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Trace a Packet with tcpdump and Identify Layers</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Use the command-line tool tcpdump to capture and decode packets. tcpdump is your primary diagnostic tool as a network application developer — learn it well.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install tcpdump: <code>sudo apt install tcpdump</code>. Run it with verbose output: <code>sudo tcpdump -i eth0 -v -n 'port 80'</code>. The <code>-v</code> flag shows L3 details, <code>-n</code> disables hostname resolution, <code>'port 80'</code> filters to HTTP traffic.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>In another terminal, run: <code>curl http://example.com</code>. Watch tcpdump output. You should see the TCP 3-way handshake (SYN → SYN-ACK → ACK) followed by the HTTP request and response.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run with the <code>-vv</code> flag for even more detail: <code>sudo tcpdump -i eth0 -vv -n 'port 80'</code>. Now capture to a file: <code>sudo tcpdump -i eth0 -w /tmp/http_capture.pcap 'port 80'</code>. Then curl again and stop tcpdump with Ctrl-C.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Read the captured file: <code>tcpdump -r /tmp/http_capture.pcap -vv -n</code>. Now try adding the <code>-e</code> flag to also show Layer 2 (Ethernet) MAC addresses: <code>tcpdump -r /tmp/http_capture.pcap -evvn</code>.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Open the .pcap file in Wireshark for a visual view: <code>wireshark /tmp/http_capture.pcap</code>. Compare the Wireshark layer tree with what tcpdump showed on the command line.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus challenge:</strong> Write a 10-line Python script using the <code>scapy</code> library (<code>pip install scapy</code>) that constructs a raw Ethernet + IP + TCP + HTTP frame from scratch and prints each layer's fields. This directly demonstrates encapsulation in code:<br><code>from scapy.all import *</code><br><code>pkt = Ether()/IP(dst="93.184.216.34")/TCP(dport=80)/Raw(b"GET / HTTP/1.0\r\n\r\n")</code><br><code>pkt.show()</code></div></div>
  </div>
</div>
</div>
<!-- ══════════ TAB 8 — CHECKLIST ══════════ -->
<div id="t8" class="tab-pane">
<p class="sep">M01 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain why layered models exist and name the two key benefits: separation of concerns and interchangeability</li>
  <li>Can name all 7 OSI layers in order (both top-to-bottom and bottom-to-top) without looking</li>
  <li>Know the correct PDU name for each layer: Data (L7-5), Segment (L4), Packet (L3), Frame (L2), Bits (L1)</li>
  <li>Can describe the job of each OSI layer in one sentence</li>
  <li>Know at least 3 protocols that operate at each OSI layer</li>
  <li>Understand the 4-layer TCP/IP model and how it maps to the 7-layer OSI model</li>
  <li>Can explain encapsulation: what happens at each layer as data travels down the stack on the sending side</li>
  <li>Can explain de-encapsulation: how each layer strips its header on the receiving side</li>
  <li>Know the three main headers added during encapsulation: Ethernet (L2), IP (L3), TCP/UDP (L4)</li>
  <li>Know the key fields in each header: Ethernet (dst/src MAC, EtherType, CRC), IP (src/dst IP, TTL, protocol), TCP (src/dst port, seq, ack, flags)</li>
  <li>Understand why a router only processes L1–L3 but a firewall with DPI processes up to L7</li>
  <li>Know the NGFW feature-to-layer mapping: packet filtering (L3/L4), stateful inspection (L4), DPI (L7), SSL inspection (L6/L7)</li>
  <li>Completed Lab 1: captured and identified all layers in a real HTTP packet using Wireshark</li>
  <li>Completed Lab 2: used tcpdump to capture traffic, saved to .pcap, and compared with Wireshark output</li>
  <li>Completed Bonus: constructed a raw Ethernet/IP/TCP packet in Scapy and identified each layer's fields</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M02 - Ethernet and L2</strong>. You've seen the Ethernet header in this module — M02 goes deep on it: MAC addressing, ARP, VLANs, 802.1Q tagging, STP, and Layer 2 switching internals.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/">← Roadmap</a>
  <a href="/learning/networking-mastery/">🗺️ All Modules</a>
  <a class="nb" href="/learning/networking-mastery/m02-ethernet-l2/">Next: M02 - Ethernet and L2 →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
function vt_direct(tabId, sectionId) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  const pane = document.getElementById(tabId);
  if (pane) pane.classList.add('active');
  const tabIndex = ['t0','t1','t2','t3','t4','t5','t6','t7','t8'].indexOf(tabId);
  const btns = document.querySelectorAll('.tab-btn');
  if (btns[tabIndex]) btns[tabIndex].classList.add('active');
  setTimeout(() => {
    const el = document.getElementById(sectionId);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 80);
}
</script>
