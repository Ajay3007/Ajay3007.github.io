---
title: "M07 - DNS"
description: "NETWORKING MASTERY · PHASE 2 · MODULE 07 · WEEKS 5–6 🔍 DNS Resolution process · Record types · Packet format · Caching · DNSSEC · DoH/DoT · DNS attacks · NGFW filtering…"
domain: networking
track: networking-mastery
order: 7
url: /learning/networking-mastery/m07-dns/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#1a5a8c 70%,#0d4a7a 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#90c8f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0ddf8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8eeff}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#90c8f0;border-bottom-color:#90c8f0}
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

/* Panel colours */
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a5a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c0ddf8;white-space:pre}
.cm{color:#4a6a8a}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#e8f4ff;border:1.5px solid #1a5a8c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0d2038;border-color:#2a6aac}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1a3a6c}
[data-theme=dark] .ins strong{color:#90c8f0}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0a2420;border-color:#2a9a8e}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#0e5248}
[data-theme=dark] .note strong{color:#5dd6c8}

/* Analogy */
.analogy{background:linear-gradient(135deg,#eef6ff,#e4f0fc);border:1.5px solid #90b8e0;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1828,#0d2038);border-color:#305880}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#1a3a6c;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#90c8f0}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* DNS packet diagram */
.dns-pkt{margin:1rem 0;overflow-x:auto}
.dns-row{display:flex;gap:2px;min-width:500px;margin-bottom:3px;align-items:stretch}
.dns-label{font-size:.7rem;font-family:monospace;min-width:90px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:4px}
.df{border-radius:5px;padding:7px 5px;font-size:.7rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.df-id {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.df-fl {background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.df-ct {background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.df-rr {background:#e8f5e8;border-color:#90d890;color:#1a5a1a}
.df-bytes{font-size:.62rem;font-weight:400;opacity:.8;margin-top:2px}

/* Record type cards */
.rtype-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.7rem;margin:1rem 0}
.rtype-card{border-radius:9px;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff);padding:.8rem 1rem}
.rtype-name{font-size:.88rem;font-weight:700;font-family:monospace;margin-bottom:.2rem}
.rtype-type{font-size:.68rem;font-family:monospace;padding:2px 6px;border-radius:4px;display:inline-block;margin-bottom:.35rem;font-weight:700}
.rtype-desc{font-size:.8rem;color:var(--text-color,#444);line-height:1.55}

/* Resolution steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#1a5a8c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#90c8f0;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5a8c}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #1a5a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a5a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a5a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a5a8c;margin-top:-.05rem}

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
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 2 · MODULE 07 · WEEKS 5–6</div>
  <div class="mod-title">🔍 DNS</div>
  <div class="mod-subtitle">Resolution process · Record types · Packet format · Caching · DNSSEC · DoH/DoT · DNS attacks · NGFW filtering</div>
  <div class="mod-pills">
    <span class="mod-pill">Beginner → Advanced</span>
    <span class="mod-pill">Prerequisite: M03, M06</span>
    <span class="mod-pill">RFC 1034 · RFC 1035</span>
    <span class="mod-pill">Critical for NGFW DPI</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">What is DNS?</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Resolution Process</button>
  <button class="tab-btn" onclick="vt(event,'t2')">DNS Packet Format</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Record Types</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Caching and TTL</button>
  <button class="tab-btn" onclick="vt(event,'t5')">DNSSEC</button>
  <button class="tab-btn" onclick="vt(event,'t6')">DoH, DoT, DoQ</button>
  <button class="tab-btn" onclick="vt(event,'t7')">DNS Attacks</button>
  <button class="tab-btn" onclick="vt(event,'t8')">NGFW DNS Features</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'ta')">Checklist</button>
</div>


<!-- ════════════ TAB 0 — WHAT IS DNS ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THE INTERNET'S PHONEBOOK — AND WHY IT'S CRITICAL FOR NGFW</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📖</span><h3>What DNS Does</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
    <p>DNS (Domain Name System) translates human-readable domain names (<code>google.com</code>, <code>api.jio.com</code>) into IP addresses that computers can route to. It is the first step in almost every network connection — before a browser can fetch a web page, before a mail client can send email, before your firewall can inspect traffic, DNS runs.</p>
    <p><strong>DNS is foundational to NGFW for four reasons:</strong></p>
    <ul>
      <li><strong>URL/domain filtering</strong> — blocking access to <code>malware-c2.com</code> by refusing to resolve it (DNS sinkholing) is the cheapest and most effective way to block millions of threats</li>
      <li><strong>Threat intelligence correlation</strong> — DNS queries reveal which hosts are communicating with which domains, enabling detection of command-and-control (C2) beaconing, data exfiltration, and lateral movement</li>
      <li><strong>DPI target</strong> — DNS is plaintext over UDP/TCP — your DPI engine must parse every DNS query and response to classify, filter, and log traffic</li>
      <li><strong>Evasion vector</strong> — DNS tunnelling (encoding data in DNS queries) is a major exfiltration channel; DoH (DNS-over-HTTPS) bypasses DNS inspection entirely unless your NGFW performs TLS inspection</li>
    </ul>
  </div>
</div>

<div class="analogy">
  <div class="analogy-title">📞 Analogy — Phone Directory Enquiries</div>
  <p>Before smartphones, if you wanted to call a business, you called directory enquiries and asked "What's the number for Jio Platforms in Navi Mumbai?". They looked it up and told you. You then called the number. DNS works identically: your computer asks "What's the IP for google.com?" and a DNS server looks it up and replies. The key insight is that your computer caches the answer (like writing the number down) so it doesn't have to ask again for a while — this is DNS caching with TTL. And just like a directory can have incorrect entries, or someone can give you a wrong number to trick you, DNS can be poisoned — which is what DNSSEC protects against.</p>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>DNS Hierarchy — Zones, Authoritative Servers, Resolvers</h3><span class="tag tag-teal">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>DNS is a globally distributed, hierarchical, delegated database. No single server knows all DNS records — the information is distributed across millions of servers worldwide, each authoritative for a specific portion (zone) of the namespace.</p>
<div class="cb"><pre><span class="cm">/* DNS hierarchy */</span>

.                           <span class="cm"># Root zone — 13 root server clusters (a.root-servers.net through m.)</span>
├── com.                    <span class="cm"># TLD (Top-Level Domain) — managed by Verisign</span>
│   ├── google.com.         <span class="cm"># Second-level domain — Google's zone</span>
│   │   ├── www.google.com. <span class="cm"># subdomain record</span>
│   │   └── mail.google.com.<span class="cm"># subdomain record</span>
│   └── amazon.com.         <span class="cm"># Different zone, different servers</span>
├── in.                     <span class="cm"># Country-code TLD (India)</span>
│   └── jio.in.             <span class="cm"># Jio's zone under .in</span>
└── io.                     <span class="cm"># Another TLD</span>

<span class="cm">/* Three types of DNS servers */</span>

1. Recursive Resolver (Recursor)
   - Your network's DNS server (DHCP-assigned: 8.8.8.8, 1.1.1.1, or your ISP's)
   - Does the work: queries root → TLD → authoritative on behalf of clients
   - Caches results for the TTL duration

2. Authoritative Name Server
   - Owns the actual DNS records for a zone
   - Configured by the domain owner (Google manages google.com's NS)
   - Returns definitive answers — not forwarding, not caching

3. Root Name Servers
   - 13 clusters (a through m), each replicated globally via anycast
   - Know only which TLD servers to ask — do NOT know final answers
   - Queried only when no cached TLD pointer exists (rare after warmup)</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 1 — RESOLUTION PROCESS ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">DNS RESOLUTION — FROM QUERY TO IP ADDRESS, STEP BY STEP</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Full Iterative Resolution Walkthrough</h3><span class="tag tag-blue">RESOLUTION</span></div>
  <div class="cp-body">
    <p>When your browser opens <code>www.google.com</code>, here is exactly what happens — assuming a cold cache (nothing cached):</p>

    <div class="flow-list">
      <div class="fl-step" data-n="1" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">Browser checks its own DNS cache</div>
          <div class="fl-detail">Browsers maintain an internal DNS cache separate from the OS. If <code>www.google.com</code> was recently visited and the TTL hasn't expired, use the cached IP — done, no query sent.</div>
          <div class="fl-code">Chrome: chrome://net-internals/#dns  |  about:networking (Firefox)</div>
        </div>
      </div>
      <div class="fl-step" data-n="2" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">OS checks its stub resolver cache</div>
          <div class="fl-detail">The OS maintains its own DNS cache (systemd-resolved, nscd, dnsmasq). If found and TTL valid — return to application. Also checks <code>/etc/hosts</code> first (static overrides).</div>
          <div class="fl-code">Linux: resolvectl statistics  |  systemd-resolve --statistics  |  cat /etc/hosts</div>
        </div>
      </div>
      <div class="fl-step" data-n="3" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">OS sends query to Recursive Resolver</div>
          <div class="fl-detail">Stub resolver sends a DNS query (UDP/53 or TCP/53) to the configured resolver (e.g., 8.8.8.8). This is the only DNS packet the client ever sends — all iteration happens inside the resolver.</div>
          <div class="fl-code">UDP: 192.168.1.5:54321 → 8.8.8.8:53  Query: A www.google.com</div>
        </div>
      </div>
      <div class="fl-step" data-n="4" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">Resolver checks its own cache</div>
          <div class="fl-detail">Google's resolver (8.8.8.8) has likely cached this response already — <code>www.google.com</code> is queried billions of times per day. If cached: return immediately. If not cached, proceed with iteration.</div>
        </div>
      </div>
      <div class="fl-step" data-n="5" style="--sc:#1a3a5c">
        <div>
          <div class="fl-title">Resolver queries a Root Name Server</div>
          <div class="fl-detail">Resolver asks a root server: "Who handles <code>.com</code>?" Root replies with NS records for the .com TLD servers (a.gtld-servers.net etc.) and their glue records (A records for those NS servers). Root servers are anycast — the resolver connects to the nearest of the 13 clusters.</div>
          <div class="fl-code">8.8.8.8 → a.root-servers.net: "Who handles .com?" → reply: NS for .com</div>
        </div>
      </div>
      <div class="fl-step" data-n="6" style="--sc:#1a3a5c">
        <div>
          <div class="fl-title">Resolver queries the .com TLD Server</div>
          <div class="fl-detail">Resolver asks a .com TLD server: "Who handles <code>google.com</code>?" TLD server replies with the NS records for google.com's authoritative servers (ns1.google.com, ns2.google.com etc.) plus their glue A records.</div>
          <div class="fl-code">8.8.8.8 → a.gtld-servers.net: "Who handles google.com?" → NS: ns1.google.com</div>
        </div>
      </div>
      <div class="fl-step" data-n="7" style="--sc:#1a3a5c">
        <div>
          <div class="fl-title">Resolver queries Google's Authoritative Server</div>
          <div class="fl-detail">Resolver asks Google's NS: "What is the A record for <code>www.google.com</code>?" Authoritative server has the definitive answer. Returns: A record with IP address(es) and the TTL.</div>
          <div class="fl-code">8.8.8.8 → ns1.google.com: "A www.google.com?" → 142.250.x.x TTL=300</div>
        </div>
      </div>
      <div class="fl-step" data-n="8" style="--sc:#0f6e56">
        <div>
          <div class="fl-title">Resolver returns answer to client, caches result</div>
          <div class="fl-detail">Resolver returns the IP to the client and caches the answer for TTL seconds (300 seconds = 5 minutes for google.com). All subsequent queries for www.google.com within 5 minutes get the cached answer immediately.</div>
          <div class="fl-code">8.8.8.8 → 192.168.1.5: A www.google.com = 142.250.x.x (TTL=300)</div>
        </div>
      </div>
      <div class="fl-step" data-n="9" style="--sc:#0f6e56">
        <div>
          <div class="fl-title">Browser connects to the returned IP</div>
          <div class="fl-detail">Browser now has the IP. Opens TCP connection (or QUIC/UDP) to 142.250.x.x:443 and begins the TLS handshake. Total DNS resolution time: typically 5–100ms for uncached, sub-millisecond for cached.</div>
        </div>
      </div>
    </div>

    <div class="ins"><p>💡 <strong>Recursive vs Iterative:</strong> The client → resolver step is <em>recursive</em> (client asks, resolver does all the work and returns a final answer). The resolver → root → TLD → authoritative steps are <em>iterative</em> (each server returns a referral, resolver must follow up). The client never talks to root or authoritative servers directly in the normal flow.</p></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">💻</span><h3>DNS Resolution in Code — getaddrinfo()</h3><span class="tag tag-teal">CODE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cs">#include &lt;netdb.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;arpa/inet.h&gt;</span>

<span class="cm">/* High-level: getaddrinfo() — handles DNS + IPv4/IPv6 */</span>
<span class="ck">struct</span> addrinfo hints = {0}, *res;
hints.ai_family   = AF_UNSPEC;     <span class="cm">/* IPv4 or IPv6 */</span>
hints.ai_socktype = SOCK_STREAM;   <span class="cm">/* TCP */</span>

<span class="ck">int</span> rc = getaddrinfo(<span class="cs">"www.google.com"</span>, <span class="cs">"443"</span>, &hints, &res);
<span class="ck">if</span> (rc != 0) {
    fprintf(stderr, <span class="cs">"DNS error: %s\n"</span>, gai_strerror(rc));
    <span class="ck">return</span> -1;
}

<span class="cm">/* Iterate through returned addresses (may have both A and AAAA) */</span>
<span class="ck">for</span> (<span class="ck">struct</span> addrinfo *p = res; p; p = p->ai_next) {
    <span class="ck">char</span> ipstr[INET6_ADDRSTRLEN];
    <span class="ck">void</span> *addr;
    <span class="ck">if</span> (p->ai_family == AF_INET) {
        <span class="ck">struct</span> sockaddr_in *s = (<span class="ck">struct</span> sockaddr_in *)p->ai_addr;
        addr = &s->sin_addr;
    } <span class="ck">else</span> {
        <span class="ck">struct</span> sockaddr_in6 *s = (<span class="ck">struct</span> sockaddr_in6 *)p->ai_addr;
        addr = &s->sin6_addr;
    }
    inet_ntop(p->ai_family, addr, ipstr, <span class="ck">sizeof</span>(ipstr));
    printf(<span class="cs">"Resolved: %s\n"</span>, ipstr);
}
freeaddrinfo(res);

<span class="cm">/* Low-level: res_query() for custom DNS queries */</span>
<span class="cs">#include &lt;resolv.h&gt;</span>
uint8_t answer[512];
<span class="ck">int</span> n = res_query(<span class="cs">"google.com"</span>, C_IN, T_MX, answer, <span class="ck">sizeof</span>(answer));
<span class="cm">/* Parse answer manually using ns_initparse / ns_parserr */</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 2 — DNS PACKET FORMAT ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">DNS PACKET FORMAT — HEADER, QUESTION, AND RESOURCE RECORDS</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>DNS Message Structure</h3><span class="tag tag-blue">PACKET FORMAT</span></div>
  <div class="cp-body">
    <p>Every DNS message — query or response — uses the same format. The same structure is used for both UDP (most queries) and TCP (large responses, zone transfers).</p>

    <div class="dns-pkt">
      <div class="dns-row">
        <div class="dns-label">Header</div>
        <div class="df df-id" style="flex:1">Transaction ID<div class="df-bytes">16 bits</div></div>
        <div class="df df-fl" style="flex:2">Flags<div class="df-bytes">16 bits — QR, Opcode, AA, TC, RD, RA, Z, RCODE</div></div>
        <div class="df df-ct" style="flex:1">QDCOUNT<div class="df-bytes">16 bits</div></div>
        <div class="df df-ct" style="flex:1">ANCOUNT<div class="df-bytes">16 bits</div></div>
        <div class="df df-ct" style="flex:1">NSCOUNT<div class="df-bytes">16 bits</div></div>
        <div class="df df-ct" style="flex:1">ARCOUNT<div class="df-bytes">16 bits</div></div>
      </div>
      <div class="dns-row">
        <div class="dns-label">Question</div>
        <div class="df df-fl" style="flex:3">QNAME (domain name in label format)<div class="df-bytes">variable length</div></div>
        <div class="df df-ct" style="flex:1">QTYPE<div class="df-bytes">16 bits</div></div>
        <div class="df df-ct" style="flex:1">QCLASS<div class="df-bytes">16 bits — 1=IN (Internet)</div></div>
      </div>
      <div class="dns-row">
        <div class="dns-label">Answer RR</div>
        <div class="df df-rr" style="flex:2">NAME<div class="df-bytes">variable</div></div>
        <div class="df df-rr" style="flex:1">TYPE<div class="df-bytes">16 bits</div></div>
        <div class="df df-rr" style="flex:1">CLASS<div class="df-bytes">16 bits</div></div>
        <div class="df df-rr" style="flex:1">TTL<div class="df-bytes">32 bits</div></div>
        <div class="df df-rr" style="flex:1">RDLENGTH<div class="df-bytes">16 bits</div></div>
        <div class="df df-rr" style="flex:2">RDATA<div class="df-bytes">variable — the actual answer</div></div>
      </div>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Header Flags — The Control Word</h3><span class="tag tag-teal">FLAGS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Bit(s)</th><th>Name</th><th>Values</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td>Bit 15</td><td>QR</td><td>0=Query, 1=Response</td><td>Is this a question or an answer?</td></tr>
        <tr><td>Bits 14–11</td><td>Opcode</td><td>0=QUERY, 1=IQUERY, 2=STATUS, 4=NOTIFY, 5=UPDATE</td><td>Type of DNS operation</td></tr>
        <tr><td>Bit 10</td><td>AA</td><td>0/1</td><td>Authoritative Answer — set if the responding server owns this zone</td></tr>
        <tr><td>Bit 9</td><td>TC</td><td>0/1</td><td>TrunCated — response was too large for UDP, retry with TCP</td></tr>
        <tr><td>Bit 8</td><td>RD</td><td>0/1</td><td>Recursion Desired — client requests recursive resolution</td></tr>
        <tr><td>Bit 7</td><td>RA</td><td>0/1</td><td>Recursion Available — server supports recursion</td></tr>
        <tr><td>Bit 6</td><td>Z</td><td>0</td><td>Reserved — must be 0</td></tr>
        <tr><td>Bit 5</td><td>AD</td><td>0/1</td><td>Authentic Data — DNSSEC: all data is validated</td></tr>
        <tr><td>Bit 4</td><td>CD</td><td>0/1</td><td>Checking Disabled — DNSSEC: don't validate, I'll check myself</td></tr>
        <tr><td>Bits 3–0</td><td>RCODE</td><td>0=NOERROR, 1=FORMERR, 2=SERVFAIL, 3=NXDOMAIN, 4=NOTIMP, 5=REFUSED</td><td>Response code — 3 (NXDOMAIN) = domain doesn't exist</td></tr>
      </tbody>
    </table>

    <h4>Label Format — How Domain Names Are Encoded</h4>
    <p>DNS doesn't send domain names as plain ASCII strings. It uses a length-prefixed label encoding where each label (component between dots) is preceded by its length byte, and the sequence ends with a zero byte:</p>
<div class="cb"><pre><span class="cm">/* Wire format of "www.google.com" in DNS */</span>
\x03 w  w  w          <span class="cm"># length=3, then "www"</span>
\x06 g  o  o  g  l  e <span class="cm"># length=6, then "google"</span>
\x03 c  o  m           <span class="cm"># length=3, then "com"</span>
\x00                   <span class="cm"># null terminator = root</span>

Total: 1+3 + 1+6 + 1+3 + 1 = 16 bytes

<span class="cm">/* DNS compression — avoid repeating names */</span>
<span class="cm">/* A pointer (2 bytes starting with bits 11) points to a prior occurrence */</span>
\xc0 \x0c  <span class="cm"># 0xC0 = 11000000 (pointer marker), 0x0c = offset 12 in message</span>
<span class="cm">/* "The name at offset 12 in this message" */</span>
<span class="cm">/* Greatly reduces packet size when multiple RRs share domain names */</span>

<span class="cm">/* Parse domain name in C */</span>
<span class="ck">int</span> parse_name(const uint8_t *msg, int msg_len, int offset, <span class="ck">char</span> *out) {
    <span class="ck">int</span> out_pos = 0;
    <span class="ck">while</span> (offset < msg_len && msg[offset] != 0) {
        uint8_t len = msg[offset++];
        <span class="ck">if</span> ((len & 0xC0) == 0xC0) {          <span class="cm">/* pointer */</span>
            uint16_t ptr = ((len & 0x3F) << 8) | msg[offset];
            offset = ptr;
            <span class="ck">continue</span>;
        }
        <span class="ck">if</span> (out_pos > 0) out[out_pos++] = <span class="cs">'.'</span>;
        memcpy(out + out_pos, msg + offset, len);
        out_pos += len; offset += len;
    }
    out[out_pos] = <span class="cs">'\0'</span>;
    <span class="ck">return</span> offset + 1;
}</pre></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>UDP vs TCP for DNS</h3><span class="tag tag-green">TRANSPORT</span></div>
  <div class="cp-body">
    <p>DNS uses both UDP and TCP on port 53, with specific rules governing when each is used:</p>
    <ul>
      <li><strong>UDP (most queries)</strong> — All normal queries and responses ≤512 bytes (traditional) or ≤4096 bytes with EDNS0. Preferred for speed — single round-trip, no connection setup</li>
      <li><strong>EDNS0 (Extension Mechanisms for DNS)</strong> — RFC 6891 extends the max UDP payload to 4096 bytes via an OPT pseudo-RR in the additional section. Enables DNSSEC responses (which are large), DNS cookies, and other extensions</li>
      <li><strong>TC flag = 1 → retry with TCP</strong> — If a response is larger than the advertised UDP buffer, the server sets TC=1 in the truncated response. The client must re-send the query over TCP to get the full answer</li>
      <li><strong>TCP only</strong> — Zone transfers (AXFR/IXFR) always use TCP. Responses reliably over 65KB use TCP. DNS over TLS (DoT) is always TCP 853</li>
    </ul>
<div class="cb"><pre><span class="cm"># Observe DNS in action</span>
tcpdump -i eth0 -n 'port 53' -v      <span class="cm"># capture all DNS, verbose</span>
tcpdump -i eth0 -n 'port 53 and tcp' <span class="cm"># only TCP DNS (large responses)</span>

<span class="cm"># Query DNS manually</span>
dig www.google.com                    <span class="cm"># A query, default resolver</span>
dig @8.8.8.8 www.google.com A        <span class="cm"># specify resolver and type</span>
dig @8.8.8.8 google.com MX          <span class="cm"># MX record</span>
dig +tcp @8.8.8.8 google.com DNSKEY  <span class="cm"># force TCP</span>
dig +dnssec @8.8.8.8 google.com      <span class="cm"># request DNSSEC</span>
dig -x 8.8.8.8                       <span class="cm"># reverse DNS (PTR lookup)</span>
nslookup -type=NS google.com         <span class="cm"># NS records</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 3 — RECORD TYPES ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">DNS RECORD TYPES — THE COMPLETE REFERENCE</p>

<div class="rtype-grid">
  <div class="rtype-card">
    <div class="rtype-name">A</div>
    <div class="rtype-type" style="background:#e8f1f9;color:#1a3a5c">Type 1</div>
    <div class="rtype-desc">Maps hostname to IPv4 address. The most common record. <code>www.google.com → 142.250.x.x</code>. RDATA = 4 bytes (IPv4 address).</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">AAAA</div>
    <div class="rtype-type" style="background:#ede8f5;color:#3a1a6c">Type 28</div>
    <div class="rtype-desc">Maps hostname to IPv6 address. <code>www.google.com → 2a00:1450::/32 prefix</code>. RDATA = 16 bytes (IPv6 address). "Quad-A" record.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">CNAME</div>
    <div class="rtype-type" style="background:#e0f0ee;color:#0a3a30">Type 5</div>
    <div class="rtype-desc">Canonical Name — alias to another name. <code>www.jio.com → jio.com</code>. RDATA = another domain name. Resolver must follow the chain until it hits an A/AAAA.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">NS</div>
    <div class="rtype-type" style="background:#e2f0e8;color:#1a4a1a">Type 2</div>
    <div class="rtype-desc">Name Server — which servers are authoritative for this zone. <code>google.com NS ns1.google.com</code>. Essential for the delegation chain.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">MX</div>
    <div class="rtype-type" style="background:#faeee4;color:#6a2800">Type 15</div>
    <div class="rtype-desc">Mail eXchanger — which servers receive email for a domain. Includes a priority value (lower = preferred). <code>google.com MX 10 smtp.google.com</code>.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">TXT</div>
    <div class="rtype-type" style="background:#fdf4dc;color:#5a3800">Type 16</div>
    <div class="rtype-desc">Arbitrary text. Used for: SPF (email anti-spoofing), DKIM (email signing), DMARC (email policy), domain ownership verification (Google, Azure), ACME challenge (Let's Encrypt).</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">PTR</div>
    <div class="rtype-type" style="background:#e8f5e8;color:#1a5a1a">Type 12</div>
    <div class="rtype-desc">Pointer — reverse DNS lookup. Maps IP to hostname. Stored in special <code>in-addr.arpa</code> zone. <code>34.216.184.93.in-addr.arpa → ec2-34-216-184-93.compute-1.amazonaws.com</code>.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">SOA</div>
    <div class="rtype-type" style="background:#faeaea;color:#6c1a1a">Type 6</div>
    <div class="rtype-desc">Start of Authority — one per zone. Contains: primary NS, admin email, serial number (for zone transfers), refresh/retry/expire/minimum TTL. Always present.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">SRV</div>
    <div class="rtype-type" style="background:#e8f1f9;color:#1a3a5c">Type 33</div>
    <div class="rtype-desc">Service locator — port + hostname for a service. <code>_sip._tcp.example.com SRV 10 5 5060 sip.example.com</code>. Used by SIP, XMPP, Minecraft, Kubernetes.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">CAA</div>
    <div class="rtype-type" style="background:#ede8f5;color:#3a1a6c">Type 257</div>
    <div class="rtype-desc">Certification Authority Authorization — which CAs can issue TLS certificates for this domain. NGFW-relevant: CAA prevents mis-issuance of SSL certs used in MITM attacks.</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">DNSKEY</div>
    <div class="rtype-type" style="background:#e2f0e8;color:#1a4a1a">Type 48</div>
    <div class="rtype-desc">DNSSEC public key for the zone. Two types: KSK (Key Signing Key, signs the DNSKEY RRset) and ZSK (Zone Signing Key, signs other records).</div>
  </div>
  <div class="rtype-card">
    <div class="rtype-name">RRSIG / DS / NSEC</div>
    <div class="rtype-type" style="background:#faeee4;color:#6a2800">DNSSEC</div>
    <div class="rtype-desc">DNSSEC records: RRSIG=digital signature over an RRset, DS=hash of child zone's KSK (delegation signer), NSEC/NSEC3=authenticated denial of existence.</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📧</span><h3>Email DNS Records — SPF, DKIM, DMARC</h3><span class="tag tag-teal">EMAIL SECURITY</span></div>
  <div class="cp-body">
    <p>Email authentication relies entirely on DNS TXT records. These are critical for NGFW email inspection and anti-phishing detection:</p>
<div class="cb"><pre><span class="cm">/* SPF — Sender Policy Framework (RFC 7208) */</span>
<span class="cm">/* TXT record listing authorised mail servers for a domain */</span>
google.com. TXT "v=spf1 include:_spf.google.com ~all"
<span class="cm"># ~all = softfail (mark but deliver), -all = fail (reject), +all = pass all</span>
<span class="cm"># NGFW checks: does sending server's IP match SPF? If not → suspicious</span>

<span class="cm">/* DKIM — DomainKeys Identified Mail (RFC 6376) */</span>
<span class="cm">/* TXT record holding public key for email signature verification */</span>
google._domainkey.google.com. TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqh..."
<span class="cm"># Sending server signs email header/body with private key</span>
<span class="cm"># Receiver verifies signature using public key from DNS</span>
<span class="cm"># NGFW can verify DKIM signatures on inbound email</span>

<span class="cm">/* DMARC — Domain-based Message Authentication, Reporting and Conformance */</span>
_dmarc.google.com. TXT "v=DMARC1; p=reject; rua=mailto:dmarc@google.com"
<span class="cm"># p=none/quarantine/reject — what to do with SPF/DKIM failures</span>
<span class="cm"># rua = aggregate report destination</span>
<span class="cm"># NGFW enforces DMARC policy for inbound email from external domains</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 4 — CACHING AND TTL ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">DNS CACHING, TTL, AND NEGATIVE CACHING</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">💾</span><h3>How DNS Caching Works</h3><span class="tag tag-blue">CACHING</span></div>
  <div class="cp-body">
    <p>DNS caching is what makes the internet fast. Without caching, every DNS query would traverse the full resolution chain — root → TLD → authoritative — for every single connection. Caching stores resolved answers for their TTL (Time To Live) duration, set by the domain owner in the authoritative DNS records.</p>
<div class="cb"><pre><span class="cm">/* TTL field in DNS Resource Records */</span>
www.google.com.  300 IN A 142.250.x.x
<span class="cm">#                ↑ TTL in seconds — cached for 300s (5 minutes)</span>

<span class="cm">/* When a recursive resolver returns a cached answer */</span>
Original TTL:  300 seconds
Query at T=0:  resolver caches, returns TTL=300
Query at T=60: resolver returns from cache, TTL=240  (remaining)
Query at T=300: cache expired, resolver re-queries authoritative

<span class="cm">/* TTL strategy tradeoffs */</span>
Low TTL  (60–300s):   fast failover on IP change, but more DNS queries
High TTL (3600–86400s): fewer queries, but changes take longer to propagate
TTL=0:   no caching — every query goes to authoritative (rare, special cases)

<span class="cm">/* Checking cached DNS on Linux */</span>
resolvectl query www.google.com      <span class="cm"># shows TTL remaining</span>
systemd-resolve --statistics         <span class="cm"># cache hit/miss stats</span>

<span class="cm">/* Flush DNS cache */</span>
sudo resolvectl flush-caches          <span class="cm"># systemd-resolved</span>
sudo systemctl restart nscd           <span class="cm"># nscd</span>
ipconfig /flushdns                    <span class="cm"># Windows</span></pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🚫</span><h3>Negative Caching — Caching NXDOMAIN</h3><span class="tag tag-teal">NEGATIVE CACHE</span></div>
  <div class="cp-body">
    <p>DNS also caches negative responses — when a domain doesn't exist (NXDOMAIN) or has no records of the requested type (NOERROR with empty answer). This prevents repeated queries for non-existent domains.</p>
<div class="cb"><pre><span class="cm">/* Negative caching (RFC 2308) */</span>
Query:   www.doesnotexist.example.com A
Response: RCODE=3 (NXDOMAIN)

Negative TTL: taken from SOA minimum field (often 300–3600 seconds)
Resolver caches: "www.doesnotexist.example.com A → NXDOMAIN" for TTL seconds

<span class="cm">/* Why this matters for NGFW */</span>
<span class="cm"># Malware C2 domains often use DGA (Domain Generation Algorithms)</span>
<span class="cm"># Generates thousands of random domains per day</span>
<span class="cm"># Only the attacker's active C2 domain resolves — rest return NXDOMAIN</span>
<span class="cm"># Unusually high NXDOMAIN rate from a host = potential DGA/malware indicator</span>

<span class="cm">/* NGFW DNS analytics: track per-client NXDOMAIN rate */</span>
<span class="cm"># Normal: 0–5% NXDOMAIN rate</span>
<span class="cm"># Suspicious: >20% NXDOMAIN from single host in 1 minute</span>
<span class="cm"># DGA malware: hundreds of NXDOMAIN per minute, all random names</span></pre></div>

    <div class="note"><p>💡 <strong>DNS prefetching:</strong> Modern browsers and resolvers (8.8.8.8, 1.1.1.1) prefetch DNS records before TTL expires to avoid cache misses for popular domains. The resolver re-queries the authoritative server just before expiry and refreshes the cache. This gives popular domains effectively zero DNS latency despite low TTLs.</p></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 5 — DNSSEC ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">DNSSEC — CRYPTOGRAPHIC AUTHENTICATION OF DNS RESPONSES</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>Why DNSSEC Exists — The Cache Poisoning Problem</h3><span class="tag tag-purple">MOTIVATION</span></div>
  <div class="cp-body">
    <p>Classic DNS has no authentication — a resolver has no way to verify that a response is genuine and not forged. The <strong>Kaminsky Attack</strong> (2008) demonstrated that an attacker could poison a recursive resolver's cache with forged responses in minutes, redirecting millions of users to attacker-controlled servers.</p>
    <p>The attack works because DNS uses UDP with a 16-bit Transaction ID — only 65,536 possible values. An attacker sends thousands of forged responses with random Transaction IDs, hoping to match before the legitimate response arrives. With the Kaminsky trick (forging the NS record for the whole domain, not just one hostname), this becomes devastating.</p>
    <p><strong>DNSSEC</strong> (DNS Security Extensions, RFC 4033–4035) adds digital signatures to DNS records. The resolver can cryptographically verify that a response came from the legitimate authoritative server and hasn't been tampered with.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>DNSSEC Chain of Trust</h3><span class="tag tag-blue">MECHANISM</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* DNSSEC chain of trust — from root down to leaf record */</span>

Root Zone (.)
  DNSKEY (KSK) → signed by root's private key (the "trust anchor")
  DNSKEY (ZSK) → signs all records in root zone
  DS record for .com → hash of .com's KSK, signed by root ZSK

.com TLD Zone
  DNSKEY (KSK) → matches hash in root's DS record
  DNSKEY (ZSK) → signs all records in .com zone
  DS record for google.com → hash of google.com's KSK, signed by .com ZSK

google.com Zone
  DNSKEY (KSK + ZSK) → KSK matches hash in .com's DS record
  RRSIG (www.google.com A) → digital signature over A record, signed by ZSK
  A record: www.google.com → 142.250.x.x

<span class="cm">/* Resolver validation */</span>
1. Resolver has root trust anchor pre-configured (IANA root key)
2. Verifies .com's KSK against root's DS record
3. Verifies google.com's KSK against .com's DS record
4. Verifies www.google.com A record against google.com's RRSIG
5. If all signatures valid → AD flag set in response (Authenticated Data)
6. If any signature fails → SERVFAIL returned to client (not the forged answer)

<span class="cm">/* Check DNSSEC validation */</span>
dig +dnssec @8.8.8.8 www.google.com A
<span class="cm"># Look for "ad" flag in flags section — means DNSSEC validated</span>
dig +dnssec @8.8.8.8 google.com DNSKEY
<span class="cm"># Shows KSK and ZSK public keys for the zone</span></pre></div>

    <h4>NSEC and NSEC3 — Authenticated Denial of Existence</h4>
    <p>DNSSEC must also authenticate that a domain does NOT exist (NXDOMAIN). Without this, an attacker could suppress DNSSEC responses and substitute forged unsigned records. NSEC/NSEC3 records provide signed proof that no records exist between two names in the zone — without revealing the entire zone contents (NSEC3 uses hashed names to prevent zone enumeration).</p>
  </div>
</div>
</div>


<!-- ════════════ TAB 6 — DoH, DoT, DoQ ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">ENCRYPTED DNS — DoH, DoT, AND DoQ</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>Why Encrypted DNS — The Privacy Problem with Plain DNS</h3><span class="tag tag-orange">MOTIVATION</span></div>
  <div class="cp-body">
    <p>Plain DNS (UDP/TCP port 53) is completely unencrypted. Every DNS query your device makes is visible to:</p>
    <ul>
      <li>Your ISP (can log, sell, censor, or inject responses)</li>
      <li>Any network observer on the path (coffee shop WiFi, corporate network monitoring)</li>
      <li>Your recursive resolver (if not 8.8.8.8/1.1.1.1, likely your ISP)</li>
      <li>Any on-path attacker (can perform cache poisoning even without Kaminsky)</li>
    </ul>
    <p>Encrypted DNS protocols hide the query content from all on-path observers except the recursive resolver you've chosen to trust.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Three Encrypted DNS Protocols Compared</h3><span class="tag tag-blue">COMPARISON</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Protocol</th><th>Port</th><th>Transport</th><th>Introduced</th><th>Privacy</th><th>NGFW Challenge</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>DoT — DNS over TLS</strong> (RFC 7858)</td>
          <td>TCP 853</td>
          <td>TLS 1.2/1.3 over TCP</td>
          <td>2016</td>
          <td>Hides query content, server can verify client cert (mTLS)</td>
          <td>Distinct port 853 — easy to block or intercept at NGFW. TLS inspection needed to see queries.</td>
        </tr>
        <tr>
          <td><strong>DoH — DNS over HTTPS</strong> (RFC 8484)</td>
          <td>TCP 443</td>
          <td>HTTPS (TLS+HTTP/2)</td>
          <td>2018</td>
          <td>Hides query in HTTPS traffic — looks like web browsing</td>
          <td>Same port as HTTPS — cannot block without blocking all HTTPS. Requires TLS inspection to detect. Firefox/Chrome bypass system resolver with DoH by default.</td>
        </tr>
        <tr>
          <td><strong>DoQ — DNS over QUIC</strong> (RFC 9250)</td>
          <td>UDP 853</td>
          <td>QUIC over UDP</td>
          <td>2022</td>
          <td>QUIC encryption hides DNS, lower latency than DoT</td>
          <td>Newest — detection requires QUIC DPI. Blocked by blocking UDP 853.</td>
        </tr>
      </tbody>
    </table>

    <h4>NGFW Implications of DoH — The Inspection Bypass Problem</h4>
<div class="cb"><pre><span class="cm">/* The DoH bypass problem */</span>

Traditional NGFW:
  Client → DNS query UDP 53 → NGFW intercepts/logs → Resolver
  NGFW sees: "who is resolving malware-c2.com?" → BLOCK + ALERT

With DoH (Firefox/Chrome built-in):
  Client → HTTPS to 1.1.1.1:443 → NGFW sees encrypted HTTPS → Resolver
  NGFW sees: "HTTPS traffic to 1.1.1.1" — cannot inspect query!
  malware-c2.com resolves successfully, client connects

<span class="cm">/* NGFW strategies to regain DNS visibility */</span>

Strategy 1: Block known DoH resolvers by IP
  Block 1.1.1.1 (Cloudflare), 8.8.8.8 (Google), 9.9.9.9 (Quad9) to port 443
  Force clients to use internal resolver (DNS policy in DHCP)
  Limitation: new DoH resolvers added constantly, list grows

Strategy 2: TLS inspection (SSL inspection)
  NGFW acts as MITM for all HTTPS connections
  Decrypts → inspects DNS-over-HTTPS → re-encrypts
  Limitation: requires deploying custom CA cert to all clients
  Limitation: many apps use certificate pinning (defeats MITM)

Strategy 3: Split-horizon DNS
  Internal DNS resolver configured to intercept all DNS queries
  Forward to DoH upstream, inspect responses before returning
  Clients only use internal resolver (enforced by firewall rule)

Strategy 4: Application-layer control
  Group Policy (Windows) / MDM (mobile) to disable browser DoH
  Chrome: CHROME_DNS_OVER_HTTPS=off, Firefox: network.trr.mode=0

<span class="cm"># Detect DoH in traffic — Wireshark filter</span>
<span class="cm"># HTTP/2 POST to /dns-query path = DoH</span>
http2.headers.path == "/dns-query"</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 7 — DNS ATTACKS ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">DNS ATTACKS — FROM CACHE POISONING TO DNS TUNNELLING</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>DNS Attack Taxonomy</h3><span class="tag tag-red">ATTACKS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attack</th><th>Mechanism</th><th>Impact</th><th>Defence</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>Cache Poisoning (Kaminsky)</strong></td>
          <td>Flood resolver with forged responses to win the Transaction ID race. Poison NS delegation for entire domain.</td>
          <td>Redirect all users of poisoned resolver to attacker-controlled IPs for any domain</td>
          <td>DNSSEC validation, source port randomisation (0.0.0.0:random), DNS cookies (RFC 7873)</td>
        </tr>
        <tr>
          <td><strong>DNS Amplification DDoS</strong></td>
          <td>Send ANY/DNSKEY queries to open resolvers with victim's IP spoofed. DNS replies (1000–4000 bytes) hit victim. 100× amplification.</td>
          <td>Massive inbound traffic overwhelms victim</td>
          <td>BCP38 anti-spoofing, disable open recursive resolvers, Response Rate Limiting (RRL)</td>
        </tr>
        <tr>
          <td><strong>DNS Tunnelling</strong></td>
          <td>Encode data in DNS query names: <code>aGVsbG8K.tunnel.attacker.com A?</code>. Response carries encoded data. Full TCP session over DNS.</td>
          <td>Data exfiltration bypassing HTTP/HTTPS filters, C2 communication</td>
          <td>Deep inspect DNS payload: high entropy names, unusually long labels, high query frequency, non-existent base domains</td>
        </tr>
        <tr>
          <td><strong>DNS Hijacking</strong></td>
          <td>Attacker compromises router/resolver to return false answers. ISPs sometimes redirect NXDOMAIN to ad pages.</td>
          <td>Traffic redirection, phishing, ad injection</td>
          <td>DNSSEC, DoH to trusted resolver, monitor resolver answers for deviations</td>
        </tr>
        <tr>
          <td><strong>NXDOMAIN Attack</strong></td>
          <td>Flood resolver with queries for non-existent subdomains of a legitimate domain. Forces resolver to query authoritative for every miss.</td>
          <td>Overwhelm authoritative server, degrade DNS performance for the targeted domain</td>
          <td>NXDOMAIN rate limiting, negative caching, RPZ (Response Policy Zones)</td>
        </tr>
        <tr>
          <td><strong>DGA (Domain Generation Algorithm)</strong></td>
          <td>Malware generates hundreds of random domain names daily, queries them all. Only the attacker-registered one resolves — rest are NXDOMAIN.</td>
          <td>C2 communication that's very hard to block (infinite domain supply)</td>
          <td>ML-based DGA detection (high entropy names, consistent patterns), track NXDOMAIN rate per host</td>
        </tr>
        <tr>
          <td><strong>Subdomain Takeover</strong></td>
          <td>CNAME points to a cloud service (GitHub Pages, Heroku) that the owner has abandoned. Attacker claims the service, serving content on the legitimate subdomain.</td>
          <td>Phishing, credential harvesting, cookie theft under legitimate domain</td>
          <td>Audit all CNAME records, verify targets still active, certificate transparency monitoring</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>DNS Tunnelling — Deep Dive</h3><span class="tag tag-purple">DNS TUNNELLING</span></div>
  <div class="cp-body">
    <p>DNS tunnelling is one of the most common data exfiltration techniques because DNS is almost never blocked at firewalls — it's essential for all network connectivity. Tools like <code>iodine</code>, <code>dnscat2</code>, and <code>dns2tcp</code> implement full bidirectional TCP-over-DNS tunnels.</p>
<div class="cb"><pre><span class="cm">/* How DNS tunnelling works */</span>

Attacker controls: tunnel.attacker.com NS ns.attacker.com
                   ns.attacker.com A → attacker's server

Client wants to exfiltrate: "secret data"
  Encode "secret data" as base32/base64: "ONQW2YLHEBQW4"
  Query: ONQW2YLHEBQW4.tunnel.attacker.com A

DNS recursive resolver → attacker's NS server
Attacker's NS server: "resolves" the query (reads the encoded data)
Response: 127.0.0.1 (or any IP — carries response data in AAAA/TXT/CNAME)

Client reads response:
  TXT record → encoded response data from attacker
  Bidirectional channel established!

<span class="cm">/* Detection signatures in DNS traffic */</span>

1. Label entropy:
   Normal:     www.google.com           (low entropy, readable words)
   Tunnelling: xK2mNpQr8vBz.tunnel.c2  (high entropy, random-looking)

2. Label length:
   Normal:     max 5-15 chars per label
   Tunnelling: 30-63 chars per label (max allowed by DNS)

3. Query frequency:
   Normal:     1-10 DNS queries/minute to a domain
   Tunnelling: 100-1000 queries/minute to same base domain

4. Query uniqueness:
   Normal:     mostly same hostnames repeated (cached)
   Tunnelling: every query to tunnel.c2.com has a UNIQUE subdomain

5. Response size:
   Normal:     A record = 4 bytes, AAAA = 16 bytes
   Tunnelling: TXT record with 200+ bytes of encoded data

<span class="cm">/* NGFW detection rule (pseudo-code) */</span>
if (dns_label_entropy > 3.5 AND
    subdomain_length > 30 AND
    query_rate_per_domain > 50/min):
    ALERT "Possible DNS tunnelling from " + client_ip</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 8 — NGFW DNS FEATURES ════════════ -->
<div id="t8" class="tab-pane">
<p class="sep">NGFW DNS FEATURES — FILTERING, SINKHOLING, AND THREAT INTELLIGENCE</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>DNS Sinkholing — The Most Effective NGFW DNS Feature</h3><span class="tag tag-teal">SINKHOLING</span></div>
  <div class="cp-body">
    <p>DNS sinkholing redirects DNS queries for known-malicious domains to a "sinkhole" IP — either a local server that logs the connection attempt, or 0.0.0.0 (drops silently). This is the single most cost-effective threat blocking technique: one DNS record blocks an entire attack infrastructure, stopping malware C2, phishing, and malware distribution sites before any TCP connection is made.</p>
<div class="cb"><pre><span class="cm">/* DNS sinkhole architecture */</span>

Normal:
  Client → DNS: "what is malware-c2.com?"
  Resolver → Authoritative: real answer → 185.x.x.x (C2 server)
  Client → TCP connection to 185.x.x.x → malware beacons home

With sinkhole:
  Client → DNS: "what is malware-c2.com?"
  NGFW intercepts query (transparent DNS proxy on UDP 53)
  NGFW checks: malware-c2.com is in threat feed → BLOCK
  NGFW returns: NXDOMAIN  (or sinkhole IP 10.0.0.254)
  Client: can't resolve domain → malware can't phone home
  NGFW logs: "host 10.0.0.5 queried known-malicious domain malware-c2.com"

<span class="cm">/* Implementation approaches */</span>

1. Transparent DNS proxy (most common)
   NGFW intercepts all UDP/TCP port 53 traffic
   Checks query against threat feed (bihash lookup)
   Modifies response or drops query

2. RPZ (Response Policy Zones) — RFC 8020, BIND/Unbound feature
   Operator configures "fake" DNS zone with override records
   zone "rpz.local" { type master; ... }
   Any query matching RPZ zone gets overridden response

3. DNS Firewall (inline)
   Full NGFW DNS proxy — receives queries, applies policy, forwards to upstream
   Can apply category filtering (block all "gambling", "adult content" domains)
   Can enforce SafeSearch DNS (redirect Google/YouTube to safe variants)

<span class="cm">/* Threat intelligence feeds for DNS */</span>
Malware domains:     abuse.ch URLhaus, Malware Domain List
C2 infrastructure:   Emerging Threats, Talos
Phishing:            PhishTank, OpenPhish, APWG
Botnet C2:           Bambenek Consulting, Feodo Tracker
Ad/tracking:         Pi-hole blocklists, AdGuard DNS Filter</pre></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📊</span><h3>DNS Analytics for Threat Detection</h3><span class="tag tag-orange">ANALYTICS</span></div>
  <div class="cp-body">
    <p>Logging all DNS queries produces a rich dataset for threat hunting. Key analytics to run:</p>
    <table class="t-table">
      <thead><tr><th>Metric</th><th>Normal Baseline</th><th>Anomaly Threshold</th><th>Likely Cause</th></tr></thead>
      <tbody>
        <tr><td>NXDOMAIN rate per host</td><td>&lt;5%</td><td>&gt;20% sustained</td><td>DGA malware, port scanning via DNS</td></tr>
        <tr><td>Queries to single domain per min</td><td>1–5</td><td>&gt;50/min</td><td>DNS tunnelling, beaconing</td></tr>
        <tr><td>Unique subdomains per base domain</td><td>1–20 known subdomains</td><td>&gt;100 unique in 1hr</td><td>DNS tunnelling (each query encodes data)</td></tr>
        <tr><td>Label entropy (Shannon)</td><td>1.5–2.5 (readable words)</td><td>&gt;3.5 (random chars)</td><td>DGA, DNS tunnelling</td></tr>
        <tr><td>Long labels (&gt;30 chars)</td><td>Rare (&lt;1%)</td><td>&gt;5% of queries</td><td>DNS tunnelling</td></tr>
        <tr><td>New domains first seen</td><td>Most queries to known domains</td><td>Host querying many never-before-seen domains</td><td>Malware discovery phase, beaconing to rotating C2</td></tr>
        <tr><td>TXT record queries</td><td>Occasional (SPF checking)</td><td>Frequent TXT to unusual domains</td><td>DNS tunnelling (TXT carries response data)</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Implementing a DNS Proxy in C — NGFW Core</h3><span class="tag tag-green">CODE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Minimal DNS proxy skeleton — intercept, inspect, forward or block */</span>
<span class="ck">int</span> dns_proxy_main() {
    <span class="ck">int</span> sock = socket(AF_INET, SOCK_DGRAM, 0);
    bind_to_port(sock, 53);

    <span class="ck">while</span> (1) {
        uint8_t buf[512];
        <span class="ck">struct</span> sockaddr_in client;
        socklen_t clen = <span class="ck">sizeof</span>(client);

        ssize_t n = recvfrom(sock, buf, <span class="ck">sizeof</span>(buf), 0,
                            (<span class="ck">struct</span> sockaddr *)&client, &clen);

        <span class="cm">/* Parse DNS header */</span>
        uint16_t txid  = ntohs(*(uint16_t *)buf);
        uint16_t flags = ntohs(*(uint16_t *)(buf + 2));
        <span class="ck">int</span> is_query = !(flags >> 15);   <span class="cm">/* QR bit = 0 → query */</span>

        <span class="ck">if</span> (!is_query) <span class="ck">continue</span>;         <span class="cm">/* ignore responses */</span>

        <span class="cm">/* Parse QNAME */</span>
        <span class="ck">char</span> domain[256];
        parse_name(buf, n, 12, domain);  <span class="cm">/* question starts at offset 12 */</span>

        <span class="cm">/* Check threat feed (bihash lookup by domain) */</span>
        <span class="ck">if</span> (is_malicious(domain)) {
            send_nxdomain(sock, buf, n, txid, &client, clen);
            log_blocked(client.sin_addr, domain);
            <span class="ck">continue</span>;
        }

        <span class="cm">/* Check domain category for content filtering */</span>
        <span class="ck">if</span> (category_blocked(domain, get_client_policy(&client))) {
            send_refused(sock, buf, n, txid, &client, clen);
            <span class="ck">continue</span>;
        }

        <span class="cm">/* Forward to upstream resolver */</span>
        forward_to_upstream(sock, buf, n, &client, clen);
    }
}

<span class="cm">/* Send NXDOMAIN response */</span>
<span class="ck">void</span> send_nxdomain(int sock, uint8_t *query, int qlen,
                  uint16_t txid, <span class="ck">struct</span> sockaddr_in *client,
                  socklen_t clen) {
    uint8_t resp[512];
    memcpy(resp, query, qlen);
    <span class="cm">/* Set QR=1 (response), RA=1, RCODE=3 (NXDOMAIN) */</span>
    *(uint16_t *)(resp + 2) = htons(0x8183);
    sendto(sock, resp, qlen, 0, (<span class="ck">struct</span> sockaddr *)client, clen);
}</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 9 — LABS ════════════ -->
<div id="t9" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>DNS Resolution Analysis with dig and Wireshark</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Observe the full DNS resolution chain — query, response, caching, TTL. Decode DNS packets byte by byte. Compare authoritative vs cached responses.</p>
    <div class="lab-step"><div class="sn">1</div><div>Capture all DNS traffic: <code>sudo tcpdump -i eth0 -w /tmp/dns.pcap 'port 53'</code>. In another terminal, run: <code>dig @8.8.8.8 www.google.com A +norecurse</code>. Note the difference between <code>+norecurse</code> (ask the server, don't do recursion for me) and the default. Stop capture and open in Wireshark.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>In Wireshark, expand the DNS query packet: find Transaction ID, Flags (QR=0 query, RD=1 recursion desired), QDCOUNT=1, QNAME, QTYPE=A, QCLASS=IN. For the response: find QR=1, RA=1, ANCOUNT, the A record RDATA (IP), and TTL value.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test TTL decay: <code>dig @8.8.8.8 www.google.com A</code> twice, 30 seconds apart. Compare the TTL in the answer section — it should be lower on the second query (TTL decreased). Run a third time immediately — if the same TTL appears, it was served from Google's resolver cache.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Walk the resolution chain manually — simulate what the recursive resolver does: <br><code>dig @a.root-servers.net google.com NS</code> (ask root for .com NS)<br><code>dig @a.gtld-servers.net google.com NS</code> (ask .com TLD for google.com NS)<br><code>dig @ns1.google.com www.google.com A</code> (ask authoritative for A record). This is the full iterative resolution path.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Query various record types: <code>dig google.com MX</code>, <code>dig google.com TXT</code>, <code>dig google.com NS</code>, <code>dig google.com SOA</code>, <code>dig -x 8.8.8.8</code> (reverse PTR). For the TXT record: find the SPF record. For the SOA: identify the primary NS, admin email, serial number, and minimum TTL.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus — DNSSEC verification:</strong> <code>dig +dnssec @8.8.8.8 cloudflare.com A</code>. Look for the "ad" flag (Authenticated Data) in the response header — this means DNSSEC was validated. Also request the DNSKEY: <code>dig +dnssec @8.8.8.8 cloudflare.com DNSKEY</code>. Identify the KSK and ZSK (flags field: 257=KSK, 256=ZSK).</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build a DNS Resolver in Python</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Write a Python script that constructs a raw DNS query packet, sends it over UDP, and parses the response — without using any DNS library. This forces you to understand the wire format completely.</p>
    <div class="lab-step"><div class="sn">1</div><div>Build a DNS query packet from scratch in Python. You need to construct: a 12-byte header (random Transaction ID, flags=0x0100 for RD=1, QDCOUNT=1, all others 0) followed by the QNAME in label format followed by QTYPE=1 (A) and QCLASS=1 (IN).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Encode the domain name into label format: split by '.', each label gets a length-prefix byte. End with \x00. Example for "www.google.com": <code>b'\x03www\x06google\x03com\x00'</code>. Use <code>struct.pack</code> for numeric fields. Send via <code>socket.sendto()</code> to 8.8.8.8:53.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Receive the response (512 bytes max for UDP). Parse the header: Transaction ID (bytes 0–1), Flags (2–3), ANCOUNT (6–7). Skip the question section (re-parse the QNAME to find where it ends). Parse each answer RR: NAME, TYPE, CLASS, TTL (4 bytes), RDLENGTH, RDATA.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>For A records (TYPE=1), RDATA is 4 bytes — convert to dotted decimal with <code>socket.inet_ntoa(rdata)</code>. For CNAME (TYPE=5), RDATA is a domain name in label format — parse it. Print results: "www.google.com A 142.250.x.x TTL=300".</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Extend to handle multiple answers (ANCOUNT > 1), CNAME chains (follow CNAME to next name), and the TC (truncated) flag — if TC=1, retry the same query over TCP (connect to 8.8.8.8:53, prepend 2-byte length prefix, same query body).</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus — DNS sinkhole:</strong> Run your script as a server (bind to localhost:5300, avoid privilege issues). For any query matching a hardcoded blocklist, return a NXDOMAIN response (flags=0x8183, ANCOUNT=0). For allowed queries, forward to 8.8.8.8, return the real response. Test with: <code>dig @127.0.0.1 -p 5300 google.com</code> and <code>dig @127.0.0.1 -p 5300 malware.com</code>.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Detect DNS Tunnelling Patterns</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Install a DNS tunnelling tool, generate tunnelled traffic, capture it, and write detection logic based on the anomaly signatures.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install dnscat2 client or iodine in a test VM. Alternatively, simulate DNS tunnelling by generating high-entropy DNS queries with Scapy: <code>from scapy.all import *; [send(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=os.urandom(20).hex()+".example.com"))) for _ in range(50)]</code>. Capture with tcpdump.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Analyse captured queries in Python using dpkt or scapy: for each DNS query, extract the subdomain label, calculate its Shannon entropy: <code>import math; entropy = -sum(p*math.log2(p) for c in set(s) if (p := s.count(c)/len(s)) > 0)</code>. Print entropy for each query name. Normal names should have entropy 1.5–2.5; tunnelling typically >3.5.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write a detection script that reads a pcap file and flags: (a) queries with label entropy >3.5, (b) labels longer than 30 characters, (c) more than 10 unique subdomains to the same base domain in 60 seconds. Use a sliding time window. Print alerts with the offending query and its entropy score.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Validate your detector against both normal traffic (your regular browsing pcap from Lab 1) and the tunnelling traffic. Tune the thresholds to minimise false positives while catching all tunnelling samples. Document what threshold values work best and why.</div></div>
  </div>
</div>

</div>


<!-- ════════════ TAB A — CHECKLIST ════════════ -->
<div id="ta" class="tab-pane">
<p class="sep">M07 MASTERY CHECKLIST</p>

<ul class="cl">
  <li>Can explain DNS's 4 roles in NGFW: URL filtering, threat intel correlation, DPI target, evasion vector</li>
  <li>Know the three server types: Recursive Resolver, Authoritative Name Server, Root Name Server — and what each does</li>
  <li>Can walk through the 9-step DNS resolution process: browser cache → OS cache → recursive resolver → root → TLD → authoritative → return + cache</li>
  <li>Know the difference between recursive (client asks, resolver iterates) and iterative (each server gives referral) resolution</li>
  <li>Know the DNS message structure: Header (12B fixed) + Question + Answer RRs + Authority RRs + Additional RRs</li>
  <li>Know the 6 header flag fields: QR, Opcode, AA, TC, RD, RA and the 4-bit RCODE</li>
  <li>Know the key RCODE values: 0=NOERROR, 2=SERVFAIL, 3=NXDOMAIN, 5=REFUSED</li>
  <li>Understand label format encoding: each label preceded by its length byte, terminated by \x00</li>
  <li>Understand DNS compression: pointer bytes (0xC0 prefix) reference earlier name occurrences in the message</li>
  <li>Know when DNS uses UDP vs TCP: UDP for most queries, TCP when TC=1 (truncated) or for zone transfers</li>
  <li>Know EDNS0: extends max UDP payload to 4096 bytes via OPT pseudo-RR</li>
  <li>Know 12 DNS record types and their purpose: A, AAAA, CNAME, NS, MX, TXT, PTR, SOA, SRV, CAA, DNSKEY, RRSIG</li>
  <li>Know SPF, DKIM, DMARC — what each does and which DNS record type they use (all TXT)</li>
  <li>Understand TTL: set by zone owner, controls cache duration, low=fast failover, high=fewer queries</li>
  <li>Understand negative caching: NXDOMAIN cached for SOA minimum TTL; high NXDOMAIN rate = DGA indicator</li>
  <li>Know DNSSEC's purpose: cryptographic authentication against cache poisoning (Kaminsky attack)</li>
  <li>Understand DNSSEC chain of trust: Root DNSKEY → .com DS → google.com DNSKEY → RRSIG on A record</li>
  <li>Know RRSIG (signature), DS (delegation signer hash), NSEC/NSEC3 (authenticated denial) records</li>
  <li>Know three encrypted DNS protocols: DoT (TCP 853), DoH (TCP 443 / HTTPS), DoQ (UDP 853 / QUIC)</li>
  <li>Know why DoH is an NGFW challenge: same port as HTTPS, browsers bypass system resolver by default</li>
  <li>Know 4 NGFW strategies to handle DoH: block resolver IPs, TLS inspection, split-horizon DNS, MDM policy</li>
  <li>Know 7 DNS attacks: cache poisoning, amplification DDoS, tunnelling, hijacking, NXDOMAIN flood, DGA, subdomain takeover</li>
  <li>Know DNS tunnelling detection signatures: high label entropy, long labels, many unique subdomains per domain, high TXT query rate</li>
  <li>Know DNS sinkholing: intercept query to malicious domain → return NXDOMAIN → block C2/phishing before TCP connection</li>
  <li>Know key DNS threat intelligence feeds: abuse.ch, Malware Domain List, Feodo Tracker, PhishTank</li>
  <li>Know DNS analytics anomalies to alert on: NXDOMAIN rate >20%, >50 queries/min to single domain, entropy >3.5</li>
  <li>Completed Lab 1: walked full resolution chain manually with dig, decoded packet headers, verified DNSSEC AD flag</li>
  <li>Completed Lab 2: built raw DNS resolver in Python from scratch; implemented DNS sinkhole server</li>
  <li>Completed Lab 3: generated DNS tunnelling traffic, wrote entropy-based detection script with pcap analysis</li>
</ul>

<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M08 - HTTP/1.1, HTTP/2, HTTP/3 and QUIC</strong>. HTTP carries the majority of internet traffic — it is both the primary application protocol your NGFW must inspect and the transport layer for TLS (HTTPS). Understanding HTTP deeply is essential for URL filtering, SSL inspection, and application identification.</p>
</div>
</div>


<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m06-udp-icmp/">← M06 UDP and ICMP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m08-http/">Next: M08 - HTTP →</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
