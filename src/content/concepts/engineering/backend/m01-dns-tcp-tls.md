---
title: "M01 — DNS, TCP & TLS Deep Dive"
description: "Backend Engineering · Phase 0 · Module 1 DNS, TCP TLS Deep Dive Every HTTP request starts with three invisible handshakes — understand them end-to-end before writing a single…"
domain: engineering
track: backend
order: 1
ownHeader: true
url: /learning/backend/m01-dns-tcp-tls/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#061a1a 0%,#0a2a28 35%,#0a2a38 70%,#061a2a 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#5dd6c8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8e8e0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8f0ec}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#061a1a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#5dd6c8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#00e5cc;border-bottom-color:#00e5cc}
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
.cb{background:#0a1e1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #00c9a7}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#a8e8e0;white-space:pre}
.cm{color:#4a9a80}.ck{color:#5dd6c8}.cv{color:#f0d080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#e0f5f2;border:1.5px solid #00c9a7;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#00a88c}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#006050}
[data-theme=dark] .ins strong{color:#5dd6c8}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e0f5f8;border:1.5px solid #00b4d8;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#082030;border-color:#008ab0}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#005a78}
[data-theme=dark] .note strong{color:#5dd6c8}

.analogy{background:linear-gradient(135deg,#eefaf8,#e4f8f0);border:1.5px solid #80d8c8;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1e1e,#0a2020);border-color:#306870}
.analogy p{margin:0;font-size:.88rem;line-height:1.7;color:var(--text-color,#222)}

/* Flow / sequence diagrams */
.seq-diagram{background:#0a1e1e;border-radius:10px;padding:1.2rem 1.5rem;margin:1rem 0;overflow-x:auto}
.seq-diagram pre{margin:0;font-family:'Courier New',monospace;font-size:.8rem;line-height:1.8;color:#a8e8e0;white-space:pre}
.seq-hl{color:#00e5cc;font-weight:700}
.seq-comment{color:#5a8a80;font-style:italic}

/* Flow list */
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.flow-list li{display:flex;align-items:flex-start;gap:.8rem;padding:.6rem 0;border-bottom:1px dashed var(--border-color,#e4e4e4);font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.flow-list li:last-child{border-bottom:none}
.fl-step{min-width:28px;height:28px;border-radius:50%;background:#00c9a7;color:#fff;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.1rem}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#00c9a7;color:#fff;padding:.5rem .8rem;text-align:left;font-weight:700}
.t-table td{padding:.45rem .8rem;border-bottom:1px solid var(--border-color,#eee);vertical-align:top;color:var(--text-color,#222)}
.t-table tr:nth-child(even) td{background:rgba(0,201,167,.05)}
[data-theme=dark] .t-table th{background:#007a60}
[data-theme=dark] .t-table tr:nth-child(even) td{background:rgba(0,201,167,.08)}

/* Two column */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #00c9a7;border-radius:12px;overflow:hidden;margin:1.5rem 0}
.lab-hdr{background:linear-gradient(90deg,#00c9a7,#00b4d8);padding:.8rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr h3{margin:0;font-size:1rem;font-weight:800;color:#fff;border:none}
.lab-hdr .lab-tag{background:rgba(255,255,255,.25);border-radius:4px;padding:2px 8px;font-size:.7rem;font-family:monospace;color:#fff;font-weight:700}
.lab-body{padding:1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#222);margin:.4rem 0}
.lab-step{display:flex;gap:.7rem;margin:.6rem 0;align-items:flex-start;font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.sn{min-width:24px;height:24px;border-radius:50%;background:#00c9a7;color:#fff;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.4rem 0;font-size:.88rem;line-height:1.6;color:var(--text-color,#222);border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";color:#00c9a7;font-size:1rem;flex-shrink:0;margin-top:.05rem}

/* States grid */
.states-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.7rem;margin:.8rem 0}
.state-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#ddd);border-radius:8px;padding:.6rem .8rem}
.state-box .st-name{font-family:monospace;font-size:.82rem;font-weight:700;color:#00c9a7;margin-bottom:.3rem}
.state-box .st-desc{font-size:.78rem;line-height:1.5;color:var(--text-color,#555)}
[data-theme=dark] .state-box{background:#0a1e1e;border-color:#1a3a38}

/* Record type badges */
.rec-type{display:inline-block;font-family:monospace;font-size:.72rem;font-weight:700;padding:2px 7px;border-radius:4px;background:#c8e8e4;color:#0e5248;margin:1px}

/* Module nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0;margin-top:2rem;border-top:2px solid var(--border-color,#eee);flex-wrap:wrap;gap:.8rem}
.nb{display:inline-flex;align-items:center;gap:.4rem;font-size:.85rem;font-weight:600;color:#00c9a7;text-decoration:none;padding:.45rem .9rem;border:1.5px solid #00c9a7;border-radius:6px;transition:background .15s,color .15s}
.nb:hover{background:#00c9a7;color:#fff}

/* Section separator */
.sep{border:none;border-top:1.5px dashed var(--border-color,#ddd);margin:1.5rem 0}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Backend Engineering · Phase 0 · Module 1</div>
  <div class="mod-title">DNS, TCP &amp; TLS Deep Dive</div>
  <div class="mod-subtitle">Every HTTP request starts with three invisible handshakes — understand them end-to-end before writing a single line of server code.</div>
  <div class="mod-pills">
    <span class="mod-pill">DNS Resolution</span>
    <span class="mod-pill">TCP 3-Way Handshake</span>
    <span class="mod-pill">TCP State Machine</span>
    <span class="mod-pill">TLS 1.3</span>
    <span class="mod-pill">POSIX Sockets</span>
    <span class="mod-pill">OpenSSL</span>
    <span class="mod-pill">C/C++</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t0',this)">📋 Overview</button>
  <button class="tab-btn" onclick="vt('t1',this)">🌐 DNS</button>
  <button class="tab-btn" onclick="vt('t2',this)">🤝 TCP Handshake</button>
  <button class="tab-btn" onclick="vt('t3',this)">🔄 TCP States</button>
  <button class="tab-btn" onclick="vt('t4',this)">🔒 TLS 1.3</button>
  <button class="tab-btn" onclick="vt('t5',this)">⚙️ C Implementation</button>
  <button class="tab-btn" onclick="vt('t6',this)">🔬 Labs</button>
  <button class="tab-btn" onclick="vt('t7',this)">✅ Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════ t0 Overview -->
<div id="t0" class="tab-pane active">

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>The Hidden Cost of "Hello, Server"</h3><span class="tag tag-teal">MENTAL MODEL</span></div>
  <div class="cp-body">
    <p>Before your code sends a single byte of application data, the OS and network stack silently complete three distinct protocol exchanges. A backend engineer who doesn't understand these layers will misdiagnose latency, misconfig TLS, and write servers that break under load.</p>
    <p>This module gives you full mental ownership of the connection lifecycle — from the moment a hostname is typed to the moment encrypted application data flows.</p>
  </div>
</div>

<h3>Connection Lifecycle: Cold Start</h3>
<div class="seq-diagram"><pre>
  Client                      DNS Resolver          TCP Stack         TLS Stack        Server App
    │                              │                    │                 │                 │
    │──── getaddrinfo("api.io") ──▶│                    │                 │                 │
    │     (recursive query chain)  │                    │                 │                 │
    │◀─── IP: 1.2.3.4 ────────────│                    │                 │                 │
    │                              │                    │                 │                 │
    │──── SYN ──────────────────────────────────────────────────────────────────────────────▶
    │◀─── SYN-ACK ──────────────────────────────────────────────────────────────────────────
    │──── ACK ──────────────────────────────────────────────────────────────────────────────▶
    │                              │                    │  TCP ESTABLISHED│                 │
    │──── ClientHello ──────────────────────────────────────────────────────────────────────▶
    │◀─── ServerHello + Cert + Finished ────────────────────────────────────────────────────
    │──── Finished ─────────────────────────────────────────────────────────────────────────▶
    │                              │                    │                 │  TLS ESTABLISHED │
    │══════════════════════ Encrypted Application Data ═══════════════════════════════════▶│
</pre></div>

<h3>Latency Budget: Cold vs Warm</h3>
<table class="t-table">
  <thead><tr><th>Phase</th><th>Cold start</th><th>Warm (cached/reused)</th><th>Where saved</th></tr></thead>
  <tbody>
    <tr><td>DNS resolution</td><td>20–100 ms</td><td>0 ms</td><td>OS/stub resolver TTL cache</td></tr>
    <tr><td>TCP handshake</td><td>1 × RTT</td><td>0 (connection pool)</td><td>Connection pooling / keep-alive</td></tr>
    <tr><td>TLS 1.3 handshake</td><td>1 × RTT</td><td>0 (0-RTT resumption)</td><td>Session tickets / PSK</td></tr>
    <tr><td>First byte of response</td><td>1 × RTT</td><td>1 × RTT</td><td>Always paid</td></tr>
    <tr><td><strong>Total cold</strong></td><td colspan="3"><strong>≈ 3–4 RTT + DNS. On 50 ms RTT link: ~200 ms before any data.</strong></td></tr>
  </tbody>
</table>

<div class="ins"><p><strong>Key insight:</strong> TLS 1.3 reduced handshake cost from 2 RTT (TLS 1.2) to 1 RTT — and 0-RTT resumption eliminates it entirely for repeat connections. This is why upgrading TLS version has measurable user-facing impact.</p></div>

<h3>Why Each Layer Exists</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>DNS</strong> — humans use names; routers use IPs. DNS is the distributed phonebook that maps one to the other. It also carries routing policy (round-robin, geo, health-check failover) via multiple A/AAAA records.</span></li>
  <li><span class="fl-step">2</span><span><strong>TCP</strong> — IP is unreliable and unordered. TCP adds reliability (retransmission), ordering (sequence numbers), and flow + congestion control. The 3-way handshake establishes shared state (ISNs) before data flows.</span></li>
  <li><span class="fl-step">3</span><span><strong>TLS</strong> — TCP provides delivery but not privacy or authenticity. TLS negotiates cipher suites, authenticates the server via certificates, and derives symmetric session keys — turning a transparent pipe into an encrypted tunnel.</span></li>
</ul>

</div>

<!-- ══════════════════════════════════════════════════════ t1 DNS -->
<div id="t1" class="tab-pane">

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>DNS Architecture</h3><span class="tag tag-blue">DISTRIBUTED SYSTEM</span></div>
  <div class="cp-body">
    <p>DNS is a globally distributed, hierarchical, eventually-consistent key-value store. It is the largest distributed database on the internet. Understanding its resolution chain is essential for diagnosing outages and designing resilient services.</p>
  </div>
</div>

<h3>Recursive Resolution Chain</h3>
<div class="seq-diagram"><pre>
  Browser/App          Stub Resolver       Recursive Resolver      Root NS       TLD NS (.io)    Auth NS (api.io)
      │                     │                     │                   │               │                 │
      │─ gethostbyname() ──▶│                     │                   │               │                 │
      │                     │──── Query: api.io ─▶│                   │               │                 │
      │                     │                     │── Who knows .io? ─▶               │                 │
      │                     │                     │◀─ Try ns1.nic.io ──               │                 │
      │                     │                     │──────────────────── api.io A? ───▶│                 │
      │                     │                     │◀─────────────────── Try ns1.api ──│                 │
      │                     │                     │──────────────────────────────────── api.io A? ─────▶
      │                     │                     │◀─────────────────────────────────── 1.2.3.4 TTL=300
      │◀──── 1.2.3.4 ───────│◀──── 1.2.3.4 ──────│                   │               │                 │
      │                     │  (cached for 300s)  │                   │               │                 │
</pre></div>

<div class="analogy"><p>🏢 <strong>Analogy:</strong> Ask reception (stub resolver) for "Bob in Engineering". Reception calls the central operator (recursive resolver) who consults the building directory (root), which points to the floor directory (.io TLD), which finally has Bob's desk number (authoritative NS returns the IP).</p></div>

<h3>DNS Record Types</h3>
<table class="t-table">
  <thead><tr><th>Type</th><th>Purpose</th><th>Example value</th><th>Backend use</th></tr></thead>
  <tbody>
    <tr><td><span class="rec-type">A</span></td><td>IPv4 address</td><td><code>1.2.3.4</code></td><td>Server IP resolution</td></tr>
    <tr><td><span class="rec-type">AAAA</span></td><td>IPv6 address</td><td><code>2001:db8::1</code></td><td>Dual-stack support</td></tr>
    <tr><td><span class="rec-type">CNAME</span></td><td>Canonical alias</td><td><code>api.io → lb-123.aws.com</code></td><td>CDN, load balancer aliasing</td></tr>
    <tr><td><span class="rec-type">MX</span></td><td>Mail exchange</td><td><code>10 mail.api.io</code></td><td>Email routing</td></tr>
    <tr><td><span class="rec-type">TXT</span></td><td>Arbitrary text</td><td><code>v=spf1 include:...</code></td><td>SPF/DKIM, ownership proof</td></tr>
    <tr><td><span class="rec-type">SRV</span></td><td>Service location</td><td><code>_http._tcp 80 host</code></td><td>Service discovery (gRPC/K8s)</td></tr>
    <tr><td><span class="rec-type">PTR</span></td><td>Reverse lookup</td><td><code>4.3.2.1.in-addr.arpa</code></td><td>Log enrichment, spam checks</td></tr>
    <tr><td><span class="rec-type">NS</span></td><td>Authoritative nameservers</td><td><code>ns1.cloudflare.com</code></td><td>Delegation chain</td></tr>
    <tr><td><span class="rec-type">SOA</span></td><td>Zone authority</td><td>Serial, refresh, retry, expire</td><td>Zone transfer, negative TTL</td></tr>
  </tbody>
</table>

<h3>DNS Message Format</h3>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Wire Format (RFC 1035)</h3><span class="tag tag-teal">BINARY PROTOCOL</span></div>
  <div class="cp-body">
    <p>DNS messages are binary, typically UDP (port 53), falling back to TCP for responses > 512 bytes or zone transfers. Each message has a fixed 12-byte header followed by variable sections.</p>
    <table class="t-table">
      <thead><tr><th>Section</th><th>Size</th><th>Content</th></tr></thead>
      <tbody>
        <tr><td>Header</td><td>12 bytes</td><td>ID (2B), Flags (2B), QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT (2B each)</td></tr>
        <tr><td>Question</td><td>variable</td><td>QNAME (label encoding), QTYPE (2B), QCLASS (2B)</td></tr>
        <tr><td>Answer</td><td>variable</td><td>NAME, TYPE, CLASS, TTL (4B), RDLENGTH, RDATA</td></tr>
        <tr><td>Authority</td><td>variable</td><td>NS records for zone delegation</td></tr>
        <tr><td>Additional</td><td>variable</td><td>Glue records (A for the NS itself)</td></tr>
      </tbody>
    </table>
    <p><strong>Label encoding:</strong> <code>api.io</code> becomes <code>\x03api\x02io\x00</code> — each label prefixed with its length byte, terminated with zero byte. DNS uses pointer compression (2-byte offset) to avoid repeating names.</p>
  </div>
</div>

<h3>TTL and Caching Behaviour</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Stub resolver</strong> (in libc) — caches based on TTL. <code>nscd</code> or <code>systemd-resolved</code> may add another caching layer. Call <code>getaddrinfo()</code> — never roll your own DNS in production.</span></li>
  <tr></tr>
  <li><span class="fl-step">2</span><span><strong>Negative caching</strong> (NXDOMAIN) — the SOA record's MINIMUM field caps negative TTL. A wrong hostname lookup causes a 60-second penalty per resolver, per negative TTL.</span></li>
  <li><span class="fl-step">3</span><span><strong>TTL strategy:</strong> During normal operation use 300s–3600s. During deployments or planned failovers, lower TTL to 30–60s <em>before</em> the change, then restore after.</span></li>
</ul>

<h3>Security: DNS Cache Poisoning</h3>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Kaminsky Attack (2008)</h3><span class="tag tag-red">ATTACK VECTOR</span></div>
  <div class="cp-body">
    <p>An attacker can inject forged DNS responses by racing the legitimate response. Classic UDP DNS used predictable transaction IDs (16-bit, ~65K space) — an attacker sending spoofed responses for all 65K IDs had a good chance of winning the race.</p>
    <h4>Defences</h4>
    <ul>
      <li><strong>Source port randomisation</strong> — expands guessing space from 65K to 65K × 65K ≈ 4 billion</li>
      <li><strong>DNSSEC</strong> — cryptographic signatures on DNS records; validates chain of trust from root to zone</li>
      <li><strong>DNS-over-HTTPS (DoH) / DNS-over-TLS (DoT)</strong> — prevents on-path eavesdropping and tampering</li>
      <li><strong>0x20 encoding</strong> — randomise case in query name; attacker must match exact case in response</li>
    </ul>
  </div>
</div>

<h3>C Code: <code>getaddrinfo()</code></h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;sys/types.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netdb.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;arpa/inet.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
 
<span class="cm">/* Resolve hostname → IP(s), prefer IPv4 */</span>
<span class="ck">int</span> resolve_host(<span class="ck">const char</span> *host, <span class="ck">char</span> out_ip[<span class="cv">INET6_ADDRSTRLEN</span>]) {
    <span class="ck">struct</span> addrinfo hints, *res, *rp;
    <span class="ck">memset</span>(&amp;hints, <span class="cv">0</span>, <span class="ck">sizeof</span>(hints));
    hints.ai_family   = AF_UNSPEC;    <span class="cm">/* IPv4 or IPv6 */</span>
    hints.ai_socktype = SOCK_STREAM;  <span class="cm">/* TCP */</span>
 
    <span class="ck">int</span> rc = getaddrinfo(host, <span class="cs">NULL</span>, &amp;hints, &amp;res);
    <span class="ck">if</span> (rc != <span class="cv">0</span>) {
        fprintf(stderr, <span class="cs">"getaddrinfo: %s\n"</span>, gai_strerror(rc));
        <span class="ck">return</span> -<span class="cv">1</span>;
    }
 
    <span class="ck">for</span> (rp = res; rp != <span class="cs">NULL</span>; rp = rp->ai_next) {
        <span class="ck">void</span> *addr;
        <span class="ck">if</span> (rp->ai_family == AF_INET) {
            <span class="ck">struct</span> sockaddr_in *ipv4 = (<span class="ck">struct</span> sockaddr_in *)rp->ai_addr;
            addr = &amp;ipv4->sin_addr;
        } <span class="ck">else</span> {
            <span class="ck">struct</span> sockaddr_in6 *ipv6 = (<span class="ck">struct</span> sockaddr_in6 *)rp->ai_addr;
            addr = &amp;ipv6->sin6_addr;
        }
        inet_ntop(rp->ai_family, addr, out_ip, INET6_ADDRSTRLEN);
        printf(<span class="cs">"Resolved %s → %s\n"</span>, host, out_ip);
        <span class="ck">break</span>;  <span class="cm">/* take first result */</span>
    }
 
    freeaddrinfo(res);
    <span class="ck">return</span> <span class="cv">0</span>;
}</pre></div>

<div class="warn"><p>⚠️ <strong>Never call <code>gethostbyname()</code></strong> — it is not thread-safe (returns pointer to static buffer), doesn't support IPv6, and is deprecated in POSIX.1-2008. Always use <code>getaddrinfo()</code>.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t2 TCP Handshake -->
<div id="t2" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Why a 3-Way Handshake?</h3><span class="tag tag-teal">RELIABILITY</span></div>
  <div class="cp-body">
    <p>TCP is connection-oriented: both sides must agree on initial sequence numbers (ISNs) before data can flow. The 3-way handshake achieves this with the minimum number of round trips needed to confirm bidirectional reachability and synchronise state.</p>
    <p>A 2-way handshake would suffice for the client to know the server is reachable — but the server wouldn't know the client received the SYN-ACK. The third ACK closes this gap.</p>
  </div>
</div>

<h3>3-Way Handshake in Detail</h3>
<div class="seq-diagram"><pre>
  Client (CLOSED)                                    Server (LISTEN)
       │                                                    │
       │── SYN (seq=ISN_c, SYN=1) ──────────────────────────▶
       │   [client → SYN_SENT]                              │ [server → SYN_RCVD]
       │                                                    │
       │◀── SYN-ACK (seq=ISN_s, ack=ISN_c+1, SYN=1,ACK=1)──│
       │   [client → ESTABLISHED]                           │
       │                                                    │
       │── ACK (seq=ISN_c+1, ack=ISN_s+1, ACK=1) ───────────▶
       │                                              [server → ESTABLISHED]
       │                                                    │
       │══════════════ DATA FLOWS ══════════════════════════▶│
</pre></div>

<h3>Initial Sequence Number (ISN) Randomness</h3>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🎲</span><h3>Why ISNs Must Be Random</h3><span class="tag tag-orange">SECURITY</span></div>
  <div class="cp-body">
    <p>Early TCP implementations used predictable ISNs (incrementing counters). This allowed <strong>TCP session hijacking</strong>: an attacker who could predict the server's ISN could forge an ACK and inject data into a connection without being on the network path.</p>
    <p>Modern kernels (Linux, BSD) use ISNs derived from a keyed hash of the 4-tuple (src-ip, src-port, dst-ip, dst-port) plus a secret key and timestamp — making ISNs unpredictable while still monotonically increasing within a connection.</p>
  </div>
</div>

<h3>TCP Options Negotiated During Handshake</h3>
<table class="t-table">
  <thead><tr><th>Option</th><th>Kind</th><th>Purpose</th><th>Default if absent</th></tr></thead>
  <tbody>
    <tr><td><strong>MSS</strong></td><td>2</td><td>Maximum Segment Size — largest payload per segment, usually 1460 on Ethernet (1500 MTU − 40B IP+TCP)</td><td>536 bytes (safe minimum)</td></tr>
    <tr><td><strong>SACK</strong></td><td>4/5</td><td>Selective Acknowledgement — receiver tells sender exactly which segments arrived; avoids retransmitting already-received data</td><td>Go-Back-N (retransmit from gap)</td></tr>
    <tr><td><strong>Window Scale</strong></td><td>3</td><td>Shifts the 16-bit window field left by N bits, allowing windows up to 1 GB. Essential for high-bandwidth long-distance links (bandwidth-delay product)</td><td>64 KB max window</td></tr>
    <tr><td><strong>Timestamps</strong></td><td>8</td><td>RTT measurement + PAWS (Protection Against Wrapped Sequence numbers). Also mitigates blind RST injection</td><td>No RTT measurement from headers</td></tr>
  </tbody>
</table>

<h3>Connection Teardown: FIN vs RST</h3>
<div class="two-col">
  <div>
    <h4>Graceful: FIN (4-way)</h4>
    <div class="seq-diagram"><pre>
  Active closer          Passive closer
      │                       │
      │── FIN ────────────────▶ [CLOSE_WAIT]
      │  [FIN_WAIT_1]          │
      │◀── ACK ────────────────│
      │  [FIN_WAIT_2]          │ (may send more data)
      │◀── FIN ────────────────│ [LAST_ACK]
      │  [TIME_WAIT]           │
      │── ACK ────────────────▶│ [CLOSED]
      │  (wait 2×MSL)          │
      │  [CLOSED]              │</pre></div>
    <p style="font-size:.82rem;color:var(--text-color,#555)">Half-close allows server to finish sending before closing.</p>
  </div>
  <div>
    <h4>Abortive: RST</h4>
    <div class="cp p-red" style="margin:0">
      <div class="cp-body">
        <p>RST immediately terminates connection — no graceful drain. Caused by:</p>
        <ul>
          <li>Port not listening (<code>Connection refused</code>)</li>
          <li><code>SO_LINGER</code> with <code>l_linger=0</code></li>
          <li>Out-of-window segment received</li>
          <li>Application crash without <code>close()</code></li>
          <li>Firewall/middlebox injecting RST</li>
        </ul>
        <p>RST causes <code>ECONNRESET</code> on the peer's next read/write.</p>
      </div>
    </div>
  </div>
</div>

<h3>Key Socket Options</h3>
<table class="t-table">
  <thead><tr><th>Option</th><th>Level</th><th>Effect</th><th>When to use</th></tr></thead>
  <tbody>
    <tr><td><code>SO_REUSEADDR</code></td><td>SOL_SOCKET</td><td>Allows bind to a port in TIME_WAIT state. Essential for servers that restart quickly</td><td>Always set on server sockets</td></tr>
    <tr><td><code>SO_REUSEPORT</code></td><td>SOL_SOCKET</td><td>Multiple sockets can bind same port; kernel load-balances incoming connections across them</td><td>Multi-process/multi-thread servers</td></tr>
    <tr><td><code>TCP_NODELAY</code></td><td>IPPROTO_TCP</td><td>Disables Nagle's algorithm — sends small packets immediately rather than buffering</td><td>Interactive protocols (SSH, Redis), latency-sensitive RPCs</td></tr>
    <tr><td><code>SO_KEEPALIVE</code></td><td>SOL_SOCKET</td><td>OS sends keepalive probes after idle period to detect dead peers</td><td>Long-lived connections (DB pools)</td></tr>
    <tr><td><code>TCP_FASTOPEN</code></td><td>IPPROTO_TCP</td><td>Send data in SYN packet on repeat connections — saves 1 RTT</td><td>Latency-critical repeat connections</td></tr>
    <tr><td><code>SO_LINGER</code></td><td>SOL_SOCKET</td><td>Controls close() behaviour: wait for drain vs send RST immediately</td><td>Set <code>l_linger=0</code> only when intentionally aborting</td></tr>
  </tbody>
</table>

<h3>C: TCP Server Skeleton</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netinet/in.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netinet/tcp.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;unistd.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
 
<span class="ck">int</span> main(<span class="ck">void</span>) {
    <span class="cm">/* 1. Create socket */</span>
    <span class="ck">int</span> server_fd = socket(AF_INET, SOCK_STREAM, <span class="cv">0</span>);
 
    <span class="cm">/* 2. Allow port reuse (survive TIME_WAIT on restart) */</span>
    <span class="ck">int</span> opt = <span class="cv">1</span>;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &amp;opt, <span class="ck">sizeof</span>(opt));
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEPORT, &amp;opt, <span class="ck">sizeof</span>(opt));
 
    <span class="cm">/* 3. Bind to port 8080, all interfaces */</span>
    <span class="ck">struct</span> sockaddr_in addr = {
        .sin_family      = AF_INET,
        .sin_port        = htons(<span class="cv">8080</span>),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(server_fd, (<span class="ck">struct</span> sockaddr *)&amp;addr, <span class="ck">sizeof</span>(addr));
 
    <span class="cm">/* 4. Mark as passive; backlog=128 = max pending SYNs in accept queue */</span>
    listen(server_fd, <span class="cv">128</span>);
    printf(<span class="cs">"Listening on :8080\n"</span>);
 
    <span class="ck">while</span> (<span class="cv">1</span>) {
        <span class="cm">/* 5. Accept — blocks until 3-way handshake completes */</span>
        <span class="ck">struct</span> sockaddr_in client_addr;
        socklen_t client_len = <span class="ck">sizeof</span>(client_addr);
        <span class="ck">int</span> conn_fd = accept(server_fd,
                             (<span class="ck">struct</span> sockaddr *)&amp;client_addr,
                             &amp;client_len);
 
        <span class="cm">/* 6. Disable Nagle for low-latency responses */</span>
        setsockopt(conn_fd, IPPROTO_TCP, TCP_NODELAY, &amp;opt, <span class="ck">sizeof</span>(opt));
 
        <span class="cm">/* 7. Read request (simplified — real code loops until \r\n\r\n) */</span>
        <span class="ck">char</span> buf[<span class="cv">4096</span>];
        ssize_t n = recv(conn_fd, buf, <span class="ck">sizeof</span>(buf) - <span class="cv">1</span>, <span class="cv">0</span>);
        buf[n] = <span class="cv">'\0'</span>;
 
        <span class="cm">/* 8. Send response */</span>
        <span class="ck">const char</span> *resp = <span class="cs">"HTTP/1.1 200 OK\r\nContent-Length: 5\r\n\r\nHello"</span>;
        send(conn_fd, resp, strlen(resp), <span class="cv">0</span>);
 
        <span class="cm">/* 9. Graceful close — sends FIN, drains */</span>
        close(conn_fd);
    }
}</pre></div>

<div class="note"><p><strong>accept() backlog:</strong> The backlog parameter to <code>listen()</code> limits the number of completed-but-not-yet-accepted connections in the kernel's accept queue. Under SYN flood, the incomplete SYN queue fills first. Set <code>net.ipv4.tcp_syncookies=1</code> to handle SYN floods without dropping legitimate connections.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t3 TCP States -->
<div id="t3" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>TCP State Machine</h3><span class="tag tag-teal">11 STATES</span></div>
  <div class="cp-body">
    <p>TCP is a finite state machine. Each connection independently transitions through states based on segments received and API calls made. Knowing these states helps you diagnose stuck connections, TIME_WAIT accumulation, and FIN_WAIT_2 leaks using <code>ss</code> or <code>netstat</code>.</p>
  </div>
</div>

<div class="states-grid">
  <div class="state-box">
    <div class="st-name">CLOSED</div>
    <div class="st-desc">Initial state. No connection. No resources allocated.</div>
  </div>
  <div class="state-box">
    <div class="st-name">LISTEN</div>
    <div class="st-desc">Server waiting for SYN. Socket bound and listening.</div>
  </div>
  <div class="state-box">
    <div class="st-name">SYN_SENT</div>
    <div class="st-desc">Client sent SYN, waiting for SYN-ACK.</div>
  </div>
  <div class="state-box">
    <div class="st-name">SYN_RCVD</div>
    <div class="st-desc">Server received SYN, sent SYN-ACK, waiting for ACK.</div>
  </div>
  <div class="state-box">
    <div class="st-name">ESTABLISHED</div>
    <div class="st-desc">Handshake complete. Data can flow in both directions.</div>
  </div>
  <div class="state-box">
    <div class="st-name">FIN_WAIT_1</div>
    <div class="st-desc">Sent FIN. Waiting for ACK or FIN from peer.</div>
  </div>
  <div class="state-box">
    <div class="st-name">FIN_WAIT_2</div>
    <div class="st-desc">Received ACK for our FIN. Waiting for peer's FIN.</div>
  </div>
  <div class="state-box">
    <div class="st-name">CLOSE_WAIT</div>
    <div class="st-desc">Received peer's FIN. App must now call close().</div>
  </div>
  <div class="state-box">
    <div class="st-name">CLOSING</div>
    <div class="st-desc">Simultaneous close: both sides sent FIN. Rare.</div>
  </div>
  <div class="state-box">
    <div class="st-name">LAST_ACK</div>
    <div class="st-desc">Passive closer sent FIN. Waiting for final ACK.</div>
  </div>
  <div class="state-box">
    <div class="st-name">TIME_WAIT</div>
    <div class="st-desc">Active closer waits 2×MSL (≈60s) before CLOSED.</div>
  </div>
</div>

<h3>Diagnosing with <code>ss</code></h3>
<table class="t-table">
  <thead><tr><th>Command</th><th>Shows</th></tr></thead>
  <tbody>
    <tr><td><code>ss -tan</code></td><td>All TCP sockets with state (numeric addresses)</td></tr>
    <tr><td><code>ss -tan state established</code></td><td>Only ESTABLISHED connections</td></tr>
    <tr><td><code>ss -tan state time-wait | wc -l</code></td><td>Count of TIME_WAIT sockets</td></tr>
    <tr><td><code>ss -tlnp</code></td><td>Listening servers with PID</td></tr>
    <tr><td><code>ss -s</code></td><td>Summary statistics per state</td></tr>
  </tbody>
</table>

<h3>TIME_WAIT Deep Dive</h3>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>Why TIME_WAIT Exists and Why It Matters</h3><span class="tag tag-orange">COMMON ISSUE</span></div>
  <div class="cp-body">
    <h4>Purpose of TIME_WAIT (2 × MSL ≈ 60 seconds)</h4>
    <ol>
      <li><strong>Ensure the final ACK reaches the peer</strong> — if the peer's FIN is not ACK'd it will retransmit; TIME_WAIT allows us to re-ACK it.</li>
      <li><strong>Prevent old segments from corrupting new connections</strong> — a new connection on the same 4-tuple must not see segments from the old connection (MSL = Maximum Segment Lifetime).</li>
    </ol>
    <h4>When TIME_WAIT Becomes a Problem</h4>
    <p>Each TIME_WAIT socket holds a 4-tuple (src-ip, src-port, dst-ip, dst-port). A server making many short outbound connections (HTTP/1.0 clients, aggressive connection teardown) can exhaust the ephemeral port range (~28K ports by default on Linux).</p>
    <h4>Solutions</h4>
    <ul>
      <li><strong>HTTP keep-alive / connection pooling</strong> — reuse connections, avoid teardown</li>
      <li><code>net.ipv4.tcp_tw_reuse=1</code> — allows reuse of TIME_WAIT connections for outbound; safe for clients</li>
      <li><code>SO_REUSEADDR</code> — allows server to bind to a port that has TIME_WAIT connections</li>
      <li>Increase ephemeral port range: <code>net.ipv4.ip_local_port_range = 1024 65535</code></li>
    </ul>
    <div class="warn"><p>⚠️ <strong>Do NOT set <code>tcp_tw_recycle</code></strong> — it was removed in Linux 4.12 because it breaks clients behind NAT (multiple clients appear to have same IP, causing packets to be dropped).</p></div>
  </div>
</div>

<h3>CLOSE_WAIT Accumulation: A Common Bug</h3>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🐛</span><h3>CLOSE_WAIT Leak</h3><span class="tag tag-red">BUG PATTERN</span></div>
  <div class="cp-body">
    <p>If <code>ss</code> shows many <strong>CLOSE_WAIT</strong> sockets, the peer has sent FIN but your application has not called <code>close()</code> on the socket. This is almost always a resource leak — your code received EOF but didn't clean up.</p>
    <p><strong>Root causes:</strong> forgetting to close the fd in error paths, connection not removed from a pool on EOF, async handler not calling close() after reading 0 bytes from recv().</p>
    <p><strong>Diagnosis:</strong> <code>ss -tanp state close-wait</code> to find which process, then check the source for missing <code>close()</code> calls after <code>recv() == 0</code>.</p>
  </div>
</div>

<h3>Half-Open Connections and Keepalive</h3>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">💤</span><h3>Dead Peer Detection</h3><span class="tag tag-blue">RELIABILITY</span></div>
  <div class="cp-body">
    <p>A <strong>half-open connection</strong> occurs when one side crashes without sending FIN (power loss, kernel panic, network cable unplugged). The surviving side believes the connection is ESTABLISHED but the peer is gone.</p>
    <p>Without keepalive, this connection stays ESTABLISHED forever — wasting file descriptors and thread/process resources.</p>
    <h4>TCP Keepalive Settings (Linux)</h4>
    <table class="t-table">
      <thead><tr><th>Sysctl</th><th>Default</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td><code>tcp_keepalive_time</code></td><td>7200s</td><td>Idle time before first probe</td></tr>
        <tr><td><code>tcp_keepalive_intvl</code></td><td>75s</td><td>Interval between probes</td></tr>
        <tr><td><code>tcp_keepalive_probes</code></td><td>9</td><td>Probes before giving up</td></tr>
      </tbody>
    </table>
    <p>Per-socket override (much faster than system defaults):</p>
    <div class="cb"><pre><span class="ck">int</span> idle = <span class="cv">10</span>, intvl = <span class="cv">5</span>, cnt = <span class="cv">3</span>;
setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &amp;(<span class="ck">int</span>){<span class="cv">1</span>}, <span class="ck">sizeof</span>(<span class="ck">int</span>));
setsockopt(fd, IPPROTO_TCP, TCP_KEEPIDLE,  &amp;idle,  <span class="ck">sizeof</span>(idle));
setsockopt(fd, IPPROTO_TCP, TCP_KEEPINTVL, &amp;intvl, <span class="ck">sizeof</span>(intvl));
setsockopt(fd, IPPROTO_TCP, TCP_KEEPCNT,   &amp;cnt,   <span class="ck">sizeof</span>(cnt));
<span class="cm">/* Now dead peer detected in 10 + 5×3 = 25 seconds */</span></pre></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t4 TLS 1.3 -->
<div id="t4" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>TLS 1.3: Why It Matters</h3><span class="tag tag-teal">RFC 8446</span></div>
  <div class="cp-body">
    <p>TLS 1.3 (2018) is a ground-up redesign of TLS 1.2. It removes legacy cruft (RSA key exchange, CBC mode ciphers, compression, renegotiation), cuts handshake latency from 2 RTT to 1 RTT, and mandates forward secrecy on every connection.</p>
    <table class="t-table">
      <thead><tr><th>Property</th><th>TLS 1.2</th><th>TLS 1.3</th></tr></thead>
      <tbody>
        <tr><td>Handshake RTTs</td><td>2 RTT</td><td><strong>1 RTT</strong> (0-RTT for resumption)</td></tr>
        <tr><td>Key exchange</td><td>RSA (static) or ECDHE</td><td><strong>ECDHE only</strong> (forward secrecy mandatory)</td></tr>
        <tr><td>Cipher suites</td><td>37+ (many weak)</td><td><strong>5</strong> (all AEAD: AES-GCM, ChaCha20-Poly1305)</td></tr>
        <tr><td>Certificate encryption</td><td>No</td><td><strong>Yes</strong> (cert sent after key exchange)</td></tr>
        <tr><td>Renegotiation</td><td>Supported (CVE source)</td><td><strong>Removed</strong></td></tr>
        <tr><td>Compression</td><td>Optional (CRIME attack)</td><td><strong>Removed</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>

<h3>TLS 1.3 Handshake: 1-RTT</h3>
<div class="seq-diagram"><pre>
  Client                                                      Server
    │                                                            │
    │── ClientHello ─────────────────────────────────────────────▶
    │   • supported_versions: TLS 1.3                            │
    │   • key_share: client ECDHE public key (e.g. X25519)       │
    │   • supported_groups, signature_algorithms                  │
    │   • psk_key_exchange_modes (for 0-RTT)                     │
    │                                                            │
    │◀── ServerHello ─────────────────────────────────────────────
    │    • key_share: server ECDHE public key                     │
    │    • selected cipher suite                                  │
    │                                                            │
    │  [Both sides derive handshake traffic secrets via HKDF]    │
    │                                                            │
    │◀── {EncryptedExtensions} ───────────────────────────────────
    │◀── {Certificate} ───────────────────────────────────────────
    │◀── {CertificateVerify} ─────────────────────────────────────
    │◀── {Finished} ──────────────────────────────────────────────
    │    [server auth complete at this point]                     │
    │                                                            │
    │── {Finished} ──────────────────────────────────────────────▶
    │   [client auth if mutual TLS]                              │
    │                                                            │
    │  [Both derive application traffic secrets]                  │
    │                                                            │
    │══ {Application Data} ═══════════════════════════════════▶│◀│
    │   (first app data can go with Finished — effectively 1 RTT) │
</pre></div>

<h3>ECDHE: Forward Secrecy Explained</h3>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔑</span><h3>Ephemeral Diffie-Hellman (ECDHE)</h3><span class="tag tag-purple">FORWARD SECRECY</span></div>
  <div class="cp-body">
    <p>In old RSA key exchange, the client encrypted the session key with the server's public RSA key. If the server's private key was later stolen, all past recorded traffic could be decrypted.</p>
    <p>ECDHE generates <strong>fresh key pairs per connection</strong>. Both sides exchange their ephemeral public keys; each derives the shared secret using their own private key and the peer's public key. The private key is never transmitted and is discarded after the handshake.</p>
    <p><strong>Result:</strong> Compromising the server's long-term certificate key cannot decrypt past sessions — each session's secret was derived from ephemeral keys that no longer exist.</p>
    <div class="note"><p><strong>Common curves in TLS 1.3:</strong> X25519 (preferred, fast, safe), P-256, P-384. X25519 is a modern curve with better performance and simpler implementation than NIST curves.</p></div>
  </div>
</div>

<h3>Certificate Chain Validation</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Receive cert chain</strong> — server sends its certificate and any intermediate CA certs. Leaf cert → intermediate → root CA.</span></li>
  <li><span class="fl-step">2</span><span><strong>Verify signatures</strong> — each cert is signed by the one above it. Verify each signature up to a trusted root.</span></li>
  <li><span class="fl-step">3</span><span><strong>Check trust anchor</strong> — root CA must be in the system trust store (<code>/etc/ssl/certs/</code> on Linux). Browsers ship their own trust store.</span></li>
  <li><span class="fl-step">4</span><span><strong>Verify hostname (SNI)</strong> — leaf cert's Subject Alternative Names (SANs) must match the hostname being connected to.</span></li>
  <li><span class="fl-step">5</span><span><strong>Check revocation</strong> — via CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol). Browsers may use OCSP stapling to speed this up.</span></li>
  <li><span class="fl-step">6</span><span><strong>Check validity period</strong> — cert must not be expired or not-yet-valid. Short-lived certs (90 days from Let's Encrypt) are best practice.</span></li>
</ul>

<h3>SNI and ALPN</h3>
<div class="two-col">
  <div class="cp p-blue" style="margin:0">
    <div class="cp-hdr"><span class="ico">🏷️</span><h3>SNI</h3><span class="tag tag-blue">SERVER NAME INDICATION</span></div>
    <div class="cp-body">
      <p>SNI allows a single server IP to host multiple TLS domains. The client sends the desired hostname in ClientHello <em>before</em> the server has selected a certificate — so the server can return the right cert.</p>
      <p>In TLS 1.3, SNI is encrypted (via Encrypted Client Hello / ECH) to prevent observers from seeing which domain you're connecting to.</p>
    </div>
  </div>
  <div class="cp p-green" style="margin:0">
    <div class="cp-hdr"><span class="ico">📋</span><h3>ALPN</h3><span class="tag tag-green">APPLICATION LAYER PROTOCOL NEGOTIATION</span></div>
    <div class="cp-body">
      <p>ALPN lets the client advertise which application protocols it supports (<code>h2</code>, <code>http/1.1</code>, <code>h3</code>) in ClientHello. The server picks one and includes it in ServerHello.</p>
      <p>This is how a single port 443 server can serve both HTTP/1.1 and HTTP/2 connections without a separate port per protocol.</p>
    </div>
  </div>
</div>

<h3>0-RTT Session Resumption</h3>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>0-RTT (Early Data)</h3><span class="tag tag-amber">PERFORMANCE vs SECURITY</span></div>
  <div class="cp-body">
    <p>After a 1-RTT handshake, the server sends a <strong>session ticket</strong> — a blob the client can present in the next ClientHello to skip the handshake entirely and send application data immediately.</p>
    <h4>Mechanism</h4>
    <p>Server encrypts a PSK (Pre-Shared Key) with its own ticket key and sends it in a <code>NewSessionTicket</code> message. On reconnect, the client sends this ticket + early data in the first message.</p>
    <h4>Security Trade-off: Replay Attacks</h4>
    <p>0-RTT data has <strong>no replay protection</strong>. An attacker who captures the first flight can replay it to a different server. Therefore:</p>
    <ul>
      <li>Never allow 0-RTT for non-idempotent operations (POST, DELETE, payments)</li>
      <li>Safe for: GET requests, read-only operations, connection warm-up</li>
      <li>Servers should use single-use tickets or replay caches to mitigate</li>
    </ul>
  </div>
</div>

<h3>Common TLS Mistakes</h3>
<table class="t-table">
  <thead><tr><th>Mistake</th><th>Risk</th><th>Fix</th></tr></thead>
  <tbody>
    <tr><td>Disabling cert verification (<code>SSL_VERIFY_NONE</code>)</td><td>MITM attacks, impersonation</td><td>Always verify in production; use <code>SSL_VERIFY_PEER</code></td></tr>
    <tr><td>Allowing TLS 1.0/1.1</td><td>POODLE, BEAST, other protocol attacks</td><td>Set minimum to TLS 1.2; prefer TLS 1.3 only</td></tr>
    <tr><td>Not checking hostname in SAN</td><td>Any cert from any CA accepted</td><td>Use <code>SSL_set_hostflags + SSL_set1_host</code> or verify via library</td></tr>
    <tr><td>Hardcoded cipher suites with RC4/DES/3DES</td><td>Brute-forceable in hours</td><td>Use <code>TLS_AES_128_GCM_SHA256</code> / <code>TLS_CHACHA20_POLY1305_SHA256</code></td></tr>
    <tr><td>Ignoring cert expiry in automation</td><td>Outages when cert expires (famous ones every year)</td><td>Set up auto-renewal (certbot), alert at 30 days</td></tr>
    <tr><td>Using self-signed certs in prod</td><td>Clients reject or users click through warnings</td><td>Use Let's Encrypt (free, 90-day, automatable)</td></tr>
  </tbody>
</table>

</div>

<!-- ══════════════════════════════════════════════════════ t5 C Implementation -->
<div id="t5" class="tab-pane">

<h3>TCP Client (C)</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netdb.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;unistd.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;errno.h&gt;</span>
 
<span class="ck">int</span> tcp_connect(<span class="ck">const char</span> *host, <span class="ck">const char</span> *port) {
    <span class="ck">struct</span> addrinfo hints = {
        .ai_family   = AF_UNSPEC,
        .ai_socktype = SOCK_STREAM
    };
    <span class="ck">struct</span> addrinfo *res;
 
    <span class="ck">int</span> rc = getaddrinfo(host, port, &amp;hints, &amp;res);
    <span class="ck">if</span> (rc) { fprintf(stderr, <span class="cs">"DNS: %s\n"</span>, gai_strerror(rc)); <span class="ck">return</span> -<span class="cv">1</span>; }
 
    <span class="ck">int</span> fd = -<span class="cv">1</span>;
    <span class="ck">for</span> (<span class="ck">struct</span> addrinfo *rp = res; rp; rp = rp->ai_next) {
        fd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        <span class="ck">if</span> (fd < <span class="cv">0</span>) <span class="ck">continue</span>;
        <span class="ck">if</span> (connect(fd, rp->ai_addr, rp->ai_addrlen) == <span class="cv">0</span>) <span class="ck">break</span>;
        close(fd); fd = -<span class="cv">1</span>;
    }
    freeaddrinfo(res);
    <span class="ck">if</span> (fd < <span class="cv">0</span>) perror(<span class="cs">"connect"</span>);
    <span class="ck">return</span> fd;
}
 
<span class="ck">int</span> main(<span class="ck">void</span>) {
    <span class="ck">int</span> fd = tcp_connect(<span class="cs">"httpbin.org"</span>, <span class="cs">"80"</span>);
    <span class="ck">if</span> (fd < <span class="cv">0</span>) <span class="ck">return</span> <span class="cv">1</span>;
 
    <span class="ck">const char</span> *req = <span class="cs">"GET /get HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"</span>;
    write(fd, req, strlen(req));
 
    <span class="ck">char</span> buf[<span class="cv">4096</span>];
    ssize_t n;
    <span class="ck">while</span> ((n = read(fd, buf, <span class="ck">sizeof</span>(buf))) > <span class="cv">0</span>)
        fwrite(buf, <span class="cv">1</span>, n, stdout);
 
    close(fd);
}</pre></div>

<h3>TLS Client with OpenSSL</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;openssl/ssl.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;openssl/err.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netdb.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;unistd.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
 
<span class="cm">/* Compile: gcc tls_client.c -lssl -lcrypto -o tls_client */</span>
 
<span class="ck">static int</span> tcp_connect_fd(<span class="ck">const char</span> *host, <span class="ck">const char</span> *port);  <span class="cm">/* as above */</span>
 
<span class="ck">int</span> main(<span class="ck">int</span> argc, <span class="ck">char</span> **argv) {
    <span class="ck">const char</span> *host = argc > <span class="cv">1</span> ? argv[<span class="cv">1</span>] : <span class="cs">"example.com"</span>;
 
    <span class="cm">/* 1. Init OpenSSL */</span>
    SSL_library_init();
    SSL_load_error_strings();
    OpenSSL_add_all_algorithms();
 
    <span class="cm">/* 2. Create TLS context — prefer TLS 1.3 */</span>
    SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
    SSL_CTX_set_min_proto_version(ctx, TLS1_2_VERSION);
 
    <span class="cm">/* 3. Load system CA bundle for cert verification */</span>
    SSL_CTX_set_default_verify_paths(ctx);
    SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL);
 
    <span class="cm">/* 4. TCP connect */</span>
    <span class="ck">int</span> fd = tcp_connect_fd(host, <span class="cs">"443"</span>);
    <span class="ck">if</span> (fd < <span class="cv">0</span>) { SSL_CTX_free(ctx); <span class="ck">return</span> <span class="cv">1</span>; }
 
    <span class="cm">/* 5. Wrap socket in SSL */</span>
    SSL *ssl = SSL_new(ctx);
    SSL_set_fd(ssl, fd);
 
    <span class="cm">/* 6. Set SNI so server returns correct cert */</span>
    SSL_set_tlsext_host_name(ssl, host);
 
    <span class="cm">/* 7. Set hostname for cert validation */</span>
    SSL_set_hostflags(ssl, X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS);
    SSL_set1_host(ssl, host);
 
    <span class="cm">/* 8. TLS handshake */</span>
    <span class="ck">int</span> err = SSL_connect(ssl);
    <span class="ck">if</span> (err != <span class="cv">1</span>) {
        ERR_print_errors_fp(stderr);
        <span class="ck">goto</span> cleanup;
    }
 
    <span class="cm">/* 9. Print negotiated cipher and protocol */</span>
    printf(<span class="cs">"TLS version : %s\n"</span>, SSL_get_version(ssl));
    printf(<span class="cs">"Cipher suite: %s\n"</span>, SSL_get_cipher(ssl));
 
    <span class="cm">/* 10. Print server cert info */</span>
    X509 *cert = SSL_get_peer_certificate(ssl);
    <span class="ck">if</span> (cert) {
        <span class="ck">char</span> buf[<span class="cv">256</span>];
        X509_NAME_oneline(X509_get_subject_name(cert), buf, <span class="ck">sizeof</span>(buf));
        printf(<span class="cs">"Cert subject: %s\n"</span>, buf);
        X509_NAME_oneline(X509_get_issuer_name(cert), buf, <span class="ck">sizeof</span>(buf));
        printf(<span class="cs">"Cert issuer : %s\n"</span>, buf);
        X509_free(cert);
    }
 
    <span class="cm">/* 11. Send HTTP request */</span>
    <span class="ck">char</span> req[<span class="cv">512</span>];
    snprintf(req, <span class="ck">sizeof</span>(req),
             <span class="cs">"GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n"</span>, host);
    SSL_write(ssl, req, strlen(req));
 
    <span class="cm">/* 12. Read response */</span>
    <span class="ck">char</span> rbuf[<span class="cv">4096</span>];
    <span class="ck">int</span> n;
    <span class="ck">while</span> ((n = SSL_read(ssl, rbuf, <span class="ck">sizeof</span>(rbuf))) > <span class="cv">0</span>)
        fwrite(rbuf, <span class="cv">1</span>, n, stdout);
 
cleanup:
    SSL_shutdown(ssl);
    SSL_free(ssl);
    close(fd);
    SSL_CTX_free(ctx);
    <span class="ck">return</span> <span class="cv">0</span>;
}</pre></div>

<h3>TCP Server with Concurrent Connections (pthreads)</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;netinet/in.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;pthread.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;unistd.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
 
<span class="ck">static void</span> *handle_client(<span class="ck">void</span> *arg) {
    <span class="ck">int</span> fd = (<span class="ck">int</span>)(intptr_t)arg;
    pthread_detach(pthread_self());  <span class="cm">/* auto-reclaim resources */</span>
 
    <span class="ck">char</span> buf[<span class="cv">4096</span>];
    ssize_t n;
    <span class="ck">while</span> ((n = recv(fd, buf, <span class="ck">sizeof</span>(buf), <span class="cv">0</span>)) > <span class="cv">0</span>) {
        <span class="cm">/* Echo back */</span>
        send(fd, buf, n, <span class="cv">0</span>);
    }
    <span class="cm">/* n == 0: peer closed; n < 0: error */</span>
    close(fd);
    <span class="ck">return</span> <span class="cs">NULL</span>;
}
 
<span class="ck">int</span> main(<span class="ck">void</span>) {
    <span class="ck">int</span> srv = socket(AF_INET, SOCK_STREAM, <span class="cv">0</span>);
    setsockopt(srv, SOL_SOCKET, SO_REUSEADDR, &amp;(<span class="ck">int</span>){<span class="cv">1</span>}, <span class="ck">sizeof</span>(<span class="ck">int</span>));
 
    <span class="ck">struct</span> sockaddr_in a = {AF_INET, htons(<span class="cv">8080</span>), .sin_addr.s_addr=INADDR_ANY};
    bind(srv, (<span class="ck">struct</span> sockaddr *)&amp;a, <span class="ck">sizeof</span>(a));
    listen(srv, <span class="cv">128</span>);
    printf(<span class="cs">"Echo server :8080\n"</span>);
 
    <span class="ck">while</span> (<span class="cv">1</span>) {
        <span class="ck">int</span> conn = accept(srv, <span class="cs">NULL</span>, <span class="cs">NULL</span>);
        <span class="ck">if</span> (conn < <span class="cv">0</span>) { perror(<span class="cs">"accept"</span>); <span class="ck">continue</span>; }
        pthread_t t;
        pthread_create(&amp;t, <span class="cs">NULL</span>, handle_client, (<span class="ck">void</span> *)(intptr_t)conn);
        <span class="cm">/* thread detached inside handle_client */</span>
    }
}</pre></div>

<div class="warn"><p>⚠️ <strong>Thread-per-connection</strong> doesn't scale beyond a few thousand connections — each thread uses ~8 MB stack by default. For high concurrency, use <strong>epoll + event loop</strong> (covered in Phase 4 — I/O Multiplexing). This example is correct for understanding the basic model.</p></div>

<h3>Error Handling Patterns</h3>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Handling EINTR, EAGAIN, Partial Reads/Writes</h3><span class="tag tag-orange">RELIABILITY</span></div>
  <div class="cp-body">
    <h4>EINTR — Interrupted System Call</h4>
    <p>Signal delivery can interrupt blocking I/O. Always restart on EINTR:</p>
    <div class="cb"><pre><span class="ck">ssize_t</span> safe_read(<span class="ck">int</span> fd, <span class="ck">void</span> *buf, <span class="ck">size_t</span> len) {
    <span class="ck">ssize_t</span> n;
    <span class="ck">do</span> { n = read(fd, buf, len); } <span class="ck">while</span> (n == -<span class="cv">1</span> &amp;&amp; errno == EINTR);
    <span class="ck">return</span> n;
}</pre></div>
    <h4>Partial Reads/Writes on TCP</h4>
    <p>TCP is a byte stream — <code>send()</code> may transfer fewer bytes than requested. Always loop:</p>
    <div class="cb"><pre><span class="ck">ssize_t</span> send_all(<span class="ck">int</span> fd, <span class="ck">const void</span> *buf, <span class="ck">size_t</span> len) {
    <span class="ck">size_t</span> sent = <span class="cv">0</span>;
    <span class="ck">while</span> (sent < len) {
        <span class="ck">ssize_t</span> n = send(fd, (<span class="ck">const char</span>*)buf + sent, len - sent, MSG_NOSIGNAL);
        <span class="ck">if</span> (n <= <span class="cv">0</span>) <span class="ck">return</span> n;
        sent += n;
    }
    <span class="ck">return</span> sent;
}
<span class="cm">/* MSG_NOSIGNAL: don't raise SIGPIPE on broken pipe — return EPIPE instead */</span></pre></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t6 Labs -->
<div id="t6" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 1 — Wireshark: Observe DNS + TCP + TLS</h3>
    <span class="lab-tag">TOOLS: Wireshark · curl</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Capture and annotate all three protocol phases for a single HTTPS request. See the latency budget with your own eyes.</p>
    <div class="lab-step"><span class="sn">1</span><span>Install Wireshark. Start a capture on your active interface (en0/eth0). Apply display filter: <code>dns or tcp.port == 443</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span>In another terminal, flush DNS cache and make a request: <br><code>sudo systemd-resolve --flush-caches &amp;&amp; curl -v https://example.com 2&gt;&amp;1 | head -40</code></span></div>
    <div class="lab-step"><span class="sn">3</span><span>Stop capture. In Wireshark, find the DNS query/response pair. Note the TTL in the answer section. Measure the DNS latency (time between query and response).</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Find the TCP SYN, SYN-ACK, ACK sequence. Measure the RTT (time between SYN and SYN-ACK). Note the TCP options in the SYN (MSS, SACK permitted, Window Scale, Timestamps).</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Find the TLS ClientHello. Right-click → Follow → TLS Stream. Identify: supported TLS versions, client key share (X25519), cipher suites offered, SNI extension, ALPN extension.</span></div>
    <div class="lab-step"><span class="sn">6</span><span>Find ServerHello. Note: selected TLS version (should be TLS 1.3), selected cipher, server key share. Count the total RTTs from SYN to first application data.</span></div>
    <p><strong>Expected findings:</strong> DNS: ~20–100 ms. TCP: 1 RTT. TLS 1.3: 1 RTT. Total before first byte ≈ DNS + 2 RTTs. TLS ClientHello and Certificate records are visible; application data is opaque (encrypted).</p>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 2 — TCP Echo Server in C</h3>
    <span class="lab-tag">TOOLS: gcc · telnet · netcat · ss</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Build and test the echo server, then observe TCP state transitions in real time.</p>
    <div class="lab-step"><span class="sn">1</span><span>Copy the "TCP Server with pthreads" code from the Implementation tab. Save as <code>echo.c</code>. Compile: <code>gcc echo.c -lpthread -o echo</code></span></div>
    <div class="lab-step"><span class="sn">2</span><span>Run: <code>./echo &amp;</code>. Check it's listening: <code>ss -tlnp | grep 8080</code></span></div>
    <div class="lab-step"><span class="sn">3</span><span>Connect with netcat: <code>nc localhost 8080</code>. Type lines — each should echo back. In another terminal: <code>ss -tan | grep 8080</code>. Observe ESTABLISHED state.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Close nc (Ctrl+C). Immediately run <code>ss -tan | grep 8080</code> multiple times. Observe TIME_WAIT appearing then disappearing after ~60s.</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Kill the echo server: <code>kill %1</code>. Try to restart immediately. Does it fail with "Address already in use"? Why? Now add <code>SO_REUSEADDR</code> if not present and retry.</span></div>
    <div class="lab-step"><span class="sn">6</span><span><strong>Challenge:</strong> Modify the server to print the client IP and port for each connection using <code>inet_ntop()</code> on the <code>sockaddr_in</code> returned by <code>accept()</code>.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 3 — TLS Client: Connect, Print Cert Chain &amp; Cipher</h3>
    <span class="lab-tag">TOOLS: gcc · OpenSSL · openssl CLI</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Build the OpenSSL TLS client, connect to a real server, and examine the full certificate chain.</p>
    <div class="lab-step"><span class="sn">1</span><span>Install OpenSSL dev headers: <code>sudo apt install libssl-dev</code> (Debian/Ubuntu) or <code>brew install openssl</code> (macOS).</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Save the "TLS Client with OpenSSL" code as <code>tls_client.c</code>. Add the <code>tcp_connect_fd()</code> implementation (from the TCP Client section). Compile: <code>gcc tls_client.c -lssl -lcrypto -o tls_client</code></span></div>
    <div class="lab-step"><span class="sn">3</span><span>Run: <code>./tls_client github.com</code>. You should see TLS version (TLS 1.3), cipher suite (e.g. TLS_AES_128_GCM_SHA256), subject, and issuer.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Print the full certificate chain. Add a loop: <code>STACK_OF(X509) *chain = SSL_get_peer_cert_chain(ssl); for(int i=0; i&lt;sk_X509_num(chain); i++) { ... }</code></span></div>
    <div class="lab-step"><span class="sn">5</span><span>Cross-check with the CLI: <code>openssl s_client -connect github.com:443 -showcerts</code>. Compare cert subjects, cipher, and protocol with your client's output.</span></div>
    <div class="lab-step"><span class="sn">6</span><span><strong>Challenge:</strong> Add SNI for a server that hosts multiple domains (try <code>cloudflare.com</code>). Then intentionally connect to a server with an expired/self-signed cert — observe the verification error. Handle it gracefully.</span></div>
    <div class="lab-step"><span class="sn">7</span><span><strong>Stretch:</strong> Add TLS 1.3 session resumption. After first connection, call <code>SSL_SESSION_print_fp()</code> to inspect the session ticket. Store it and present it on reconnect. Measure latency difference.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 4 — DNS Deep Dive with dig</h3>
    <span class="lab-tag">TOOLS: dig · tcpdump · host</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Walk the DNS resolution chain manually and understand TTLs, record types, and DNSSEC.</p>
    <div class="lab-step"><span class="sn">1</span><span>Full recursive trace: <code>dig +trace github.com A</code>. Observe: root nameservers → .com TLD → github.com authoritative. Note TTL at each level.</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Check all record types: <code>dig github.com ANY</code>. List A, AAAA, MX, NS, TXT records. What TXT records exist? (SPF? DKIM selectors?)</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Test negative caching: <code>dig nonexistent.github.com A</code>. Note NXDOMAIN and the negative TTL in the SOA record's MINIMUM field.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Check DNSSEC: <code>dig +dnssec cloudflare.com A</code>. Do you see RRSIG records? What key tag is used?</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Measure DNS latency over time: <code>for i in $(seq 10); do dig +stats github.com A | grep "Query time"; done</code>. First query is cold; subsequent should be fast (cached by resolver). Note the caching effect.</span></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t7 Checklist -->
<div id="t7" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">✅</span><h3>Module Mastery Checklist</h3><span class="tag tag-teal">M01 COMPLETE</span></div>
  <div class="cp-body">
    <p>You have mastered this module when you can check off every item below without referring to notes.</p>
  </div>
</div>

<h3>DNS</h3>
<ul class="cl">
  <li>Explain the full recursive DNS resolution chain — stub resolver → recursive resolver → root → TLD → authoritative NS</li>
  <li>State the purpose of TTL and explain the two-phase TTL strategy for planned failovers (lower TTL before, restore after)</li>
  <li>Name at least 6 DNS record types and their use cases (A, AAAA, CNAME, MX, TXT, SRV)</li>
  <li>Explain why <code>getaddrinfo()</code> must be used instead of <code>gethostbyname()</code></li>
  <li>Describe how DNS cache poisoning works and name three defences (source port randomisation, DNSSEC, DoH/DoT)</li>
  <li>Use <code>dig +trace</code> to walk the resolution chain; interpret the TTL values at each delegation level</li>
</ul>

<h3>TCP — Handshake &amp; Options</h3>
<ul class="cl">
  <li>Draw the 3-way handshake with correct flag names (SYN, SYN-ACK, ACK) and state transitions on both sides</li>
  <li>Explain why ISNs must be randomly generated and the historical attack they prevent</li>
  <li>Name the 4 TCP options negotiated during the SYN exchange and what each enables</li>
  <li>Explain the difference between FIN (graceful) and RST (abortive) teardown; name 3 causes of RST</li>
  <li>Explain <code>SO_REUSEADDR</code> and <code>SO_REUSEPORT</code> — when to use each and why</li>
  <li>Write a TCP server socket setup in C: <code>socket() → setsockopt() → bind() → listen() → accept()</code></li>
  <li>Handle partial writes correctly with a <code>send_all()</code> loop; explain MSG_NOSIGNAL</li>
</ul>

<h3>TCP — State Machine</h3>
<ul class="cl">
  <li>Name all 11 TCP states and identify the 3 most commonly encountered in production (ESTABLISHED, TIME_WAIT, CLOSE_WAIT)</li>
  <li>Explain TIME_WAIT: why it exists (2 reasons), duration (2 × MSL), and production mitigations</li>
  <li>Diagnose a CLOSE_WAIT leak: what it means, how to find it with <code>ss</code>, and what causes it in code</li>
  <li>Configure per-socket TCP keepalive to detect dead peers within 25 seconds</li>
  <li>Use <code>ss -tan</code> to count connections by state on a live server</li>
</ul>

<h3>TLS 1.3</h3>
<ul class="cl">
  <li>List 4 improvements TLS 1.3 made over TLS 1.2 (1-RTT, mandatory forward secrecy, fewer cipher suites, encrypted certs)</li>
  <li>Trace the TLS 1.3 1-RTT handshake: which messages are sent, in what order, and what each contains</li>
  <li>Explain forward secrecy: why ECDHE prevents decryption of past sessions even if the server key is compromised</li>
  <li>Explain 0-RTT resumption: how session tickets work, the replay attack risk, and which operations are safe/unsafe</li>
  <li>Explain SNI and ALPN: what problem each solves and when each is sent</li>
  <li>Write an OpenSSL TLS client that: sets <code>SSL_VERIFY_PEER</code>, sets SNI, sets hostname for cert validation, prints the cipher suite and TLS version</li>
  <li>Name 5 common TLS configuration mistakes and their consequences</li>
</ul>

<hr class="sep">
<div class="ins"><p><strong>Next module:</strong> M02 covers HTTP Internals — how HTTP/1.1, HTTP/2, and HTTP/3 use the TCP/TLS layer you just mastered. You'll understand pipelining, multiplexing, header compression (HPACK/QPACK), and QUIC's 0-RTT connection establishment.</p></div>

</div>

<!-- Module Nav -->
<div class="mod-nav">
  <a href="/learning/backend/backend-roadmap/" class="nb">← Back to Roadmap</a>
  <span style="font-size:.8rem;color:var(--text-color,#888);font-family:monospace">Phase 0 · Module 1 of 2</span>
  <a href="/learning/backend/m02-http-servers/" class="nb">M02 HTTP Internals →</a>
</div>

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
