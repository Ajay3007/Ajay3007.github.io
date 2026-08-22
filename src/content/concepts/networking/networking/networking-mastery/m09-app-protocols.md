---
title: "M09 - SMTP, FTP, and DHCP"
description: "NETWORKING MASTERY · PHASE 2 · MODULE 09 · WEEK 7 · PHASE 2 FINAL 📨 SMTP, FTP, and DHCP Email delivery · FTP active/passive · DHCP DORA · ALG internals · Spoofing · NGFW email…"
domain: networking
track: networking-mastery
order: 9
ownHeader: true
url: /learning/networking-mastery/m09-app-protocols/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 30%,#1e6b3c 65%,#0a4a28 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#90e890;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0f0c0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8ffd8}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#90e890;border-bottom-color:#90e890}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1e6b3c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8f0c8;white-space:pre}
.cm{color:#4a8a50}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
/* SMTP/FTP session colours */
.sc{color:#90e890;font-weight:700}   /* server */
.cc{color:#f0c880;font-weight:700}   /* client */
.se{color:#f08080}                   /* error */
.si{color:#90c8f0}                   /* info */

/* Insight / warning / note */
.ins{background:#e8f8e8;border:1.5px solid #1e6b3c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2018;border-color:#2a8a4a}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1a5a1a}
[data-theme=dark] .ins strong{color:#90e890}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#1a3a5c}
[data-theme=dark] .note strong{color:#7ab8d8}

/* Analogy */
.analogy{background:linear-gradient(135deg,#f0fff0,#e8f8e8);border:1.5px solid #90c890;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1a0a,#0a2010);border-color:#306830}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#1a5a1a;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#90e890}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1e6b3c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1e6b3c}

/* Protocol flow (SMTP, FTP, DHCP session diagrams) */
.proto-session{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto}
.proto-session pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.8;white-space:pre;color:#c8f0c8}

/* DHCP packet fields */
.dhcp-fields{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin:.8rem 0}
@media(max-width:540px){.dhcp-fields{grid-template-columns:1fr}}
.dhcp-field{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e0e0e0);border-radius:7px;padding:.6rem .9rem}
.dhcp-field-name{font-size:.78rem;font-weight:700;font-family:monospace;color:#1e6b3c;margin-bottom:.2rem}
.dhcp-field-size{font-size:.68rem;font-family:monospace;color:var(--light-text,#888)}
.dhcp-field-desc{font-size:.8rem;color:var(--text-color,#444);line-height:1.5;margin-top:.2rem}

/* Flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#1e6b3c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#90e890;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #1e6b3c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1e6b3c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1e6b3c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1e6b3c;margin-top:-.05rem}

/* Nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}

/* Phase complete banner */
.phase-complete{
  background:linear-gradient(135deg,#0a2018,#1e6b3c);
  border-radius:10px;padding:1.4rem 1.6rem;margin:2rem 0;
  border:1.5px solid #2a9a5c;color:#fff;
}
.phase-complete h3{margin:0 0 .5rem;font-size:1.1rem;font-weight:800;color:#fff;border:none}
.phase-complete p{margin:0;font-size:.88rem;line-height:1.65;color:#c0f0c0}
</style>

<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 2 · MODULE 09 · WEEK 7 · PHASE 2 FINAL</div>
  <div class="mod-title">📨 SMTP, FTP, and DHCP</div>
  <div class="mod-subtitle">Email delivery · FTP active/passive · DHCP DORA · ALG internals · Spoofing · NGFW email inspection</div>
  <div class="mod-pills">
    <span class="mod-pill">Beginner → Intermediate</span>
    <span class="mod-pill">Prerequisite: M05 TCP, M06 UDP</span>
    <span class="mod-pill">RFC 5321 · RFC 959 · RFC 2131</span>
    <span class="mod-pill">ALG-Heavy Protocols</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">SMTP Internals</button>
  <button class="tab-btn" onclick="vt(event,'t2')">SMTP Security</button>
  <button class="tab-btn" onclick="vt(event,'t3')">FTP Internals</button>
  <button class="tab-btn" onclick="vt(event,'t4')">FTP and NAT/ALG</button>
  <button class="tab-btn" onclick="vt(event,'t5')">DHCP Internals</button>
  <button class="tab-btn" onclick="vt(event,'t6')">DHCP Security</button>
  <button class="tab-btn" onclick="vt(event,'t7')">NGFW Policy</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>


<!-- ════════════ TAB 0 — OVERVIEW ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THREE PROTOCOLS AN NGFW MUST DEEPLY UNDERSTAND</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Why These Three Protocols Together</h3><span class="tag tag-green">OVERVIEW</span></div>
  <div class="cp-body">
    <p>SMTP, FTP, and DHCP represent three different categories of protocol that an NGFW must handle in special ways. Each exposes a different class of firewall challenge:</p>
    <div class="two-col">
      <div>
        <h4>📨 SMTP (TCP 25/587/465)</h4>
        <p>Email transfer. An NGFW must parse SMTP to enforce email policies — anti-spam, anti-phishing, attachment scanning, content filtering, and sender authentication (SPF/DKIM/DMARC verification). Email is the number one attack vector for malware delivery and phishing.</p>

        <h4>📁 FTP (TCP 21 + dynamic port)</h4>
        <p>File transfer. FTP is the classic <strong>ALG challenge protocol</strong> — it uses two separate TCP connections (control on port 21, data on a negotiated dynamic port). A stateful firewall must inspect the control channel to know which data connection to permit. FTP is largely replaced by SFTP/HTTPS but still found in legacy environments and internal networks.</p>
      </div>
      <div>
        <h4>🖥️ DHCP (UDP 67/68)</h4>
        <p>IP address assignment. DHCP is the protocol that bootstraps all other protocols — a device has no IP address until DHCP assigns one. An NGFW must understand DHCP to: detect rogue DHCP servers, prevent DHCP starvation attacks, correlate IP-to-MAC-to-hostname mappings for logging, and enforce DHCP snooping.</p>

        <h4>The ALG Problem</h4>
        <p>Both SMTP and FTP embed IP addresses or port numbers inside their application payloads — information a simple L3/L4 firewall cannot see. When NAT rewrites the outer IP header, the embedded address in the payload is wrong. Application Layer Gateways (ALGs) must inspect and rewrite payload content — a stateful, deep inspection operation that lies at the heart of NGFW design.</p>
      </div>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Port and Protocol Quick Reference</h3><span class="tag tag-teal">REFERENCE</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Protocol</th><th>Port(s)</th><th>Transport</th><th>Purpose</th><th>Encrypted variant</th></tr></thead>
      <tbody>
        <tr><td><strong>SMTP</strong></td><td>25</td><td>TCP</td><td>Server-to-server mail relay (MTA to MTA)</td><td>STARTTLS (upgrades on same port)</td></tr>
        <tr><td><strong>SMTP Submission</strong></td><td>587</td><td>TCP</td><td>Client to mail server (MUA to MSA)</td><td>STARTTLS mandatory</td></tr>
        <tr><td><strong>SMTPS</strong></td><td>465</td><td>TCP</td><td>SMTP wrapped in TLS from connection start</td><td>TLS from first byte</td></tr>
        <tr><td><strong>POP3</strong></td><td>110 / 995</td><td>TCP</td><td>Download mail from server (delete from server)</td><td>POP3S on 995</td></tr>
        <tr><td><strong>IMAP</strong></td><td>143 / 993</td><td>TCP</td><td>Sync mail (leave on server)</td><td>IMAPS on 993</td></tr>
        <tr><td><strong>FTP Control</strong></td><td>21</td><td>TCP</td><td>Commands, authentication, directory listing</td><td>FTPS (explicit or implicit TLS)</td></tr>
        <tr><td><strong>FTP Data</strong></td><td>20 (active) or dynamic</td><td>TCP</td><td>Actual file transfer</td><td>Same TLS session as control</td></tr>
        <tr><td><strong>SFTP</strong></td><td>22</td><td>TCP (SSH)</td><td>Secure file transfer over SSH — not FTP at all</td><td>Always encrypted (SSH)</td></tr>
        <tr><td><strong>DHCP Server</strong></td><td>67</td><td>UDP</td><td>DHCP server listens here</td><td>No encryption (network-local)</td></tr>
        <tr><td><strong>DHCP Client</strong></td><td>68</td><td>UDP</td><td>Client sends/receives on this port</td><td>No encryption</td></tr>
        <tr><td><strong>DHCPv6</strong></td><td>546/547</td><td>UDP</td><td>IPv6 DHCP (client 546, server 547)</td><td>No encryption</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════════════ TAB 1 — SMTP INTERNALS ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">SMTP — SIMPLE MAIL TRANSFER PROTOCOL (RFC 5321)</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📧</span><h3>How Email Moves — The SMTP Pipeline</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>Email delivery involves multiple agents. Understanding which component speaks to which — and on which port — is essential for NGFW policy:</p>
<div class="cb"><pre><span class="cm">/* Email delivery pipeline */</span>
 
Your mail client (MUA — Mail User Agent)
  |
  | TCP 587 (SMTP Submission, STARTTLS + AUTH)
  ↓
Your outgoing mail server (MSA — Mail Submission Agent)
  |                     e.g., smtp.gmail.com, smtp.jio.com
  | TCP 25 (SMTP relay between servers)
  ↓
Recipient's MX server (MTA — Mail Transfer Agent)
  |                     found via DNS MX lookup on recipient domain
  | Stores in mailbox
  ↓
Recipient's mail client (MUA)
  ← TCP 993/IMAP or 995/POP3 (client downloads mail)
 
<span class="cm">/* Why three different ports? */</span>
Port 25:  Server-to-server relay. NOT for clients (ISPs block outbound 25 to prevent spam from compromised machines).
Port 587: Client submission. Requires AUTH (login). Most ISPs and firewalls allow this.
Port 465:  Legacy SMTPS — TLS from connection open. Superseded by 587+STARTTLS but still used.
 
<span class="cm">/* DNS MX lookup before SMTP connection */</span>
dig gmail.com MX
<span class="cv">; gmail.com MX 5 gmail-smtp-in.l.google.com.</span>
<span class="cv">; gmail.com MX 10 alt1.gmail-smtp-in.l.google.com.</span>
<span class="cm"># Sender's MTA connects to lowest-preference (highest priority) MX server</span></pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">💬</span><h3>SMTP Session — Command by Command</h3><span class="tag tag-teal">SESSION</span></div>
  <div class="cp-body">
    <p>SMTP is a line-oriented text protocol. Commands come from the client; replies from the server always start with a 3-digit code. Reply codes: 2xx=success, 4xx=temporary failure (retry later), 5xx=permanent failure (don't retry).</p>

    <div class="proto-session">
<pre><span class="sc">220 mail.example.com ESMTP Postfix (Ubuntu)</span>          <span class="si">← Server greeting</span>
 
<span class="cc">EHLO sending-server.jio.com</span>                           <span class="si">← Extended HELLO — announces capabilities</span>
<span class="sc">250-mail.example.com</span>
<span class="sc">250-PIPELINING</span>                                        <span class="si">← Multiple commands without waiting</span>
<span class="sc">250-SIZE 52428800</span>                                     <span class="si">← Max message size: 50 MB</span>
<span class="sc">250-STARTTLS</span>                                          <span class="si">← Can upgrade to TLS</span>
<span class="sc">250-AUTH LOGIN PLAIN XOAUTH2</span>                         <span class="si">← Supported auth mechanisms</span>
<span class="sc">250 DSN</span>                                               <span class="si">← Delivery Status Notification support</span>
 
<span class="cc">STARTTLS</span>                                              <span class="si">← Upgrade connection to TLS</span>
<span class="sc">220 2.0.0 Ready to start TLS</span>
<span class="si">[TLS handshake occurs — all subsequent SMTP is encrypted]</span>
<span class="cc">EHLO sending-server.jio.com</span>                           <span class="si">← Must re-EHLO after STARTTLS</span>
<span class="sc">250 mail.example.com ...</span>
 
<span class="cc">AUTH LOGIN</span>                                            <span class="si">← Authenticate (client to server only)</span>
<span class="sc">334 VXNlcm5hbWU6</span>                                     <span class="si">← "Username:" base64 encoded</span>
<span class="cc">YWpheUBqaW8uY29t</span>                                     <span class="si">← username base64 encoded</span>
<span class="sc">334 UGFzc3dvcmQ6</span>                                     <span class="si">← "Password:" base64 encoded</span>
<span class="cc">cGFzc3dvcmQxMjM=</span>                                     <span class="si">← password base64 encoded</span>
<span class="sc">235 2.7.0 Authentication successful</span>
 
<span class="cc">MAIL FROM:&lt;ajay@jio.com&gt;</span>                             <span class="si">← Envelope sender (RETURN-PATH)</span>
<span class="sc">250 2.1.0 Ok</span>
 
<span class="cc">RCPT TO:&lt;colleague@example.com&gt;</span>                      <span class="si">← Envelope recipient</span>
<span class="sc">250 2.1.5 Ok</span>
 
<span class="cc">RCPT TO:&lt;boss@example.com&gt;</span>                           <span class="si">← Multiple recipients allowed</span>
<span class="sc">250 2.1.5 Ok</span>
 
<span class="cc">DATA</span>                                                  <span class="si">← Start message body</span>
<span class="sc">354 End data with &lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;</span>
<span class="cc">From: Ajay Kumar &lt;ajay@jio.com&gt;</span>                      <span class="si">← Message headers (RFC 5322)</span>
<span class="cc">To: Colleague &lt;colleague@example.com&gt;</span>
<span class="cc">Subject: Meeting tomorrow</span>
<span class="cc">Date: Wed, 18 Mar 2026 10:00:00 +0530</span>
<span class="cc">MIME-Version: 1.0</span>
<span class="cc">Content-Type: text/plain; charset=UTF-8</span>
<span class="cc"></span>
<span class="cc">Hi, can we meet at 2pm tomorrow?</span>
<span class="cc">.</span>                                                     <span class="si">← Single dot on line = end of message</span>
<span class="sc">250 2.0.0 Ok: queued as A1B2C3D4</span>
 
<span class="cc">QUIT</span>
<span class="sc">221 2.0.0 Bye</span></pre>
    </div>

    <div class="ins"><p>💡 <strong>Envelope vs Message headers:</strong> SMTP has two separate sets of addressing. The <em>envelope</em> (MAIL FROM, RCPT TO commands) is what the mail servers use for routing — like the address written on the outside of a letter. The <em>message headers</em> (From:, To:, CC: inside the DATA section) are what email clients display — like the letter's own header. These can differ, which is how email spoofing works: MAIL FROM can say one address while From: header shows another.</p></div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📋</span><h3>SMTP Reply Codes — Complete Reference</h3><span class="tag tag-amber">CODES</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Code</th><th>Meaning</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td><code>220</code></td><td>Service ready</td><td>Server greeting — connection accepted</td></tr>
        <tr><td><code>221</code></td><td>Service closing</td><td>Response to QUIT</td></tr>
        <tr><td><code>235</code></td><td>Authentication successful</td><td>AUTH accepted</td></tr>
        <tr><td><code>250</code></td><td>Requested action OK</td><td>Most commands succeed with this</td></tr>
        <tr><td><code>334</code></td><td>Server AUTH challenge</td><td>Prompt for username/password (base64)</td></tr>
        <tr><td><code>354</code></td><td>Start mail input</td><td>Response to DATA — send message until "."</td></tr>
        <tr><td><code>421</code></td><td>Service unavailable</td><td>Server shutting down — retry later</td></tr>
        <tr><td><code>450</code></td><td>Mailbox unavailable</td><td>Temporary — try again (greylisting)</td></tr>
        <tr><td><code>451</code></td><td>Action aborted</td><td>Server error — retry later</td></tr>
        <tr><td><code>452</code></td><td>Insufficient storage</td><td>Server disk full — retry later</td></tr>
        <tr><td><code>500</code></td><td>Syntax error</td><td>Unrecognised command</td></tr>
        <tr><td><code>501</code></td><td>Syntax error in parameters</td><td>Bad MAIL FROM or RCPT TO format</td></tr>
        <tr><td><code>503</code></td><td>Bad sequence</td><td>Command out of order (RCPT before MAIL FROM)</td></tr>
        <tr><td><code>535</code></td><td>Authentication failed</td><td>Wrong credentials</td></tr>
        <tr><td><code>550</code></td><td>Mailbox unavailable</td><td>Permanent — user doesn't exist or blocked</td></tr>
        <tr><td><code>551</code></td><td>User not local</td><td>Relay denied — not accepting for this domain</td></tr>
        <tr><td><code>552</code></td><td>Exceeded storage allocation</td><td>Recipient mailbox full</td></tr>
        <tr><td><code>553</code></td><td>Mailbox name not allowed</td><td>Invalid email address format</td></tr>
        <tr><td><code>554</code></td><td>Transaction failed</td><td>Spam or policy rejection</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════════════ TAB 2 — SMTP SECURITY ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">SMTP SECURITY — SPOOFING, SPAM, AND AUTHENTICATION</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Email Spoofing — Why From: Can Lie</h3><span class="tag tag-red">SPOOFING</span></div>
  <div class="cp-body">
    <p>The original SMTP protocol (1982) has no authentication. Anyone can connect to a mail server and claim to be anyone. The From: header in the message body is just text — there is no cryptographic verification that the sender is who they claim to be. This enables email spoofing, which underlies nearly all phishing attacks.</p>
<div class="cb"><pre><span class="cm">/* Email spoofing — trivially easy */</span>
telnet mail.victim.com 25
<span class="sc">220 mail.victim.com ESMTP</span>
<span class="cc">EHLO legitimate-looking-domain.com</span>
<span class="sc">250 Ok</span>
<span class="cc">MAIL FROM:&lt;ceo@real-company.com&gt;</span>          <span class="si">← Envelope sender — can be anything!</span>
<span class="sc">250 Ok</span>
<span class="cc">RCPT TO:&lt;employee@victim.com&gt;</span>
<span class="sc">250 Ok</span>
<span class="cc">DATA</span>
<span class="cc">From: CEO Real Name &lt;ceo@real-company.com&gt;</span> <span class="si">← Message header — identical to envelope</span>
<span class="cc">Subject: Urgent wire transfer needed</span>
<span class="cc">.</span>
 
<span class="cm">/* Without SPF/DKIM/DMARC the receiving server has no way to detect this */</span>
<span class="cm">/* Employee sees ceo@real-company.com — looks completely legitimate */</span></pre></div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>SPF, DKIM, and DMARC — The Email Authentication Trinity</h3><span class="tag tag-purple">AUTHENTICATION</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Mechanism</th><th>What It Checks</th><th>Where Stored</th><th>Verifies</th><th>Fails When</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>SPF</strong><br><span style="font-size:.75rem;color:var(--light-text,#666)">Sender Policy Framework</span></td>
          <td>Envelope sender IP vs authorised sender list</td>
          <td>DNS TXT record of sender domain</td>
          <td>"Did this email come from an authorised server?"</td>
          <td>Legitimate email forwarded through a relay not in SPF record. SPF fails on indirect mail flow.</td>
        </tr>
        <tr>
          <td><strong>DKIM</strong><br><span style="font-size:.75rem;color:var(--light-text,#666)">DomainKeys Identified Mail</span></td>
          <td>Cryptographic signature over message headers and body</td>
          <td>DNS TXT at <code>selector._domainkey.domain</code></td>
          <td>"Was this message signed by the domain it claims to be from? Was it altered in transit?"</td>
          <td>Message modified after signing. Signature mismatch = tampering detected.</td>
        </tr>
        <tr>
          <td><strong>DMARC</strong><br><span style="font-size:.75rem;color:var(--light-text,#666)">Domain-based Msg Auth, Reporting and Conformance</span></td>
          <td>SPF or DKIM alignment with From: header domain</td>
          <td>DNS TXT at <code>_dmarc.domain</code></td>
          <td>"If SPF/DKIM fail, what should the receiver do? Quarantine? Reject? Report?"</td>
          <td>SPF and DKIM both fail, or pass for a different domain than the From: header domain.</td>
        </tr>
      </tbody>
    </table>

<div class="cb"><pre><span class="cm">/* SMTP receiving server checks — in order */</span>
 
1. Connect from IP 1.2.3.4, MAIL FROM:&lt;ajay@jio.com&gt;
 
2. SPF check: DNS lookup TXT jio.com → "v=spf1 include:_spf.jio.com -all"
   Is 1.2.3.4 in _spf.jio.com? If yes: SPF PASS. If no: SPF FAIL.
 
3. DKIM check: Find DKIM-Signature header in message DATA.
   Lookup DNS TXT selector._domainkey.jio.com → get public key.
   Verify signature over specified headers + body. Match? DKIM PASS.
 
4. DMARC check: DNS TXT _dmarc.jio.com → "v=DMARC1; p=reject; rua=mailto:..."
   Does SPF domain or DKIM d= tag align with From: header domain?
   If p=reject and both fail → REJECT the message (return 5xx).
   If p=quarantine → deliver to spam folder.
   If p=none → deliver but send report.
 
<span class="cm">/* Verify SMTP auth headers in received email */</span>
<span class="cm"># In Gmail: "Show original" → look for:</span>
Authentication-Results: mx.google.com;
   dkim=pass header.i=@jio.com header.s=selector1;
   spf=pass smtp.mailfrom=jio.com;
   dmarc=pass (p=REJECT) header.from=jio.com</pre></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>NGFW Email Inspection Capabilities</h3><span class="tag tag-orange">NGFW</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>SMTP proxy</strong> — NGFW terminates the SMTP connection, inspects the entire message, then re-originates to the real server. Full visibility into all commands, headers, and body</li>
      <li><strong>Attachment scanning</strong> — decompress ZIP/RAR, decode Base64 MIME attachments, scan for malware signatures. Block password-protected archives (common malware evasion)</li>
      <li><strong>Content filtering</strong> — scan email body for DLP keywords (credit card numbers, NIN/PAN numbers, confidential), block messages matching patterns</li>
      <li><strong>SPF/DKIM/DMARC enforcement</strong> — reject or quarantine emails that fail authentication regardless of recipient server's policy. Add header stamping with verification results</li>
      <li><strong>Anti-spam scoring</strong> — combine: SPF fail, DKIM fail, blacklisted sending IP (RBL/DNSBL), suspicious subject line patterns, URL reputation in body</li>
      <li><strong>Greylisting</strong> — temporary reject (4xx) on first delivery attempt. Legitimate servers retry, spam bots usually don't. Cheap and effective anti-spam with 10–15 minute delivery delay</li>
      <li><strong>URL reputation</strong> — scan URLs in email body against threat intelligence feeds. Rewrite URLs to pass through a proxy that checks at click-time (time-of-click protection)</li>
    </ul>
  </div>
</div>
</div>


<!-- ════════════ TAB 3 — FTP INTERNALS ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">FTP — FILE TRANSFER PROTOCOL (RFC 959)</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📁</span><h3>FTP's Two-Connection Architecture</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>FTP is unique among common protocols in using <strong>two separate TCP connections</strong>: one for commands (control channel) and one for actual data transfer (data channel). This separation was designed for efficiency but creates significant headaches for firewalls and NAT.</p>
    <ul>
      <li><strong>Control channel</strong> — TCP connection to server port 21. Carries all commands (USER, PASS, LIST, RETR, STOR) and replies. Stays open for the entire FTP session.</li>
      <li><strong>Data channel</strong> — a separate TCP connection opened for each data transfer (directory listing, file upload, file download). The port used depends on whether FTP is in Active or Passive mode.</li>
    </ul>
    <p>The critical insight for NGFW: the data channel port number is negotiated <em>inside the control channel payload</em>. A firewall must inspect L7 content to know which port to permit for the data channel.</p>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Active FTP vs Passive FTP</h3><span class="tag tag-teal">ACTIVE VS PASSIVE</span></div>
  <div class="cp-body">
    <div class="two-col">
      <div>
        <h4>Active FTP (PORT command)</h4>
<div class="cb"><pre><span class="cc">CLIENT                SERVER</span>
 
<span class="cm">/* Control channel */</span>
  → TCP connect to :21
  ← 220 FTP Ready
  → USER ajay
  ← 331 Password:
  → PASS secret
  ← 230 Logged in
 
<span class="cm">/* Client tells server where to call back */</span>
  → PORT 10,0,0,5,196,160
  <span class="si">← IP: 10.0.0.5</span>
  <span class="si">  Port: 196*256+160 = 50336</span>
  ← 200 PORT command OK
 
  → LIST
  ← 150 Opening data connection
<span class="cm">/* Data channel — server initiates! */</span>
  ← TCP connect from :20 to client :50336
  <span class="cm">/* directory listing transferred */</span>
  ← 226 Transfer complete</pre></div>
        <p style="font-size:.82rem;color:var(--text-color,#444)"><strong>Problem:</strong> Server connects back to client on a high port. Client-side firewall must allow INBOUND connections from server. Behind NAT, the embedded IP in PORT is a private address — server cannot reach the client. Active FTP is <strong>incompatible with client-side NAT</strong> without ALG.</p>
      </div>
      <div>
        <h4>Passive FTP (PASV command)</h4>
<div class="cb"><pre><span class="cc">CLIENT                SERVER</span>
 
<span class="cm">/* Control channel */</span>
  → TCP connect to :21
  ← 220 FTP Ready
  → USER ajay
  ← 331 Password:
  → PASS secret
  ← 230 Logged in
 
<span class="cm">/* Client asks server to listen */</span>
  → PASV
  ← 227 Entering Passive Mode
  <span class="si">  (192,168,1,100,200,45)</span>
  <span class="si">  IP: 192.168.1.100</span>
  <span class="si">  Port: 200*256+45 = 51245</span>
 
  → LIST
  ← 150 Opening data connection
<span class="cm">/* Data channel — CLIENT initiates */</span>
  → TCP connect to server :51245
  <span class="cm">/* directory listing transferred */</span>
  ← 226 Transfer complete</pre></div>
        <p style="font-size:.82rem;color:var(--text-color,#444)"><strong>Why passive is better:</strong> Client always initiates. Works through client-side NAT and firewalls (outbound TCP is usually allowed). Standard for modern FTP clients. <strong>Problem:</strong> Server's embedded IP in PASV response may be a private address if server is behind NAT — client cannot connect to 192.168.x.x from the internet. Server-side ALG needed.</p>
      </div>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">💬</span><h3>FTP Commands and Reply Codes</h3><span class="tag tag-amber">REFERENCE</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Command</th><th>Meaning</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td><code>USER</code></td><td>Username</td><td><code>USER ajay</code></td></tr>
        <tr><td><code>PASS</code></td><td>Password (sent in plaintext!)</td><td><code>PASS mysecret</code></td></tr>
        <tr><td><code>PORT</code></td><td>Active mode — specify data channel address</td><td><code>PORT 10,0,0,5,196,160</code></td></tr>
        <tr><td><code>PASV</code></td><td>Enter passive mode</td><td><code>PASV</code> → server replies with IP,port</td></tr>
        <tr><td><code>EPSV</code></td><td>Extended passive mode (IPv6-compatible)</td><td><code>EPSV</code> → <code>229 Entering Extended Passive Mode (|||51245|)</code></td></tr>
        <tr><td><code>LIST</code></td><td>Directory listing (opens data channel)</td><td><code>LIST /home/ajay</code></td></tr>
        <tr><td><code>RETR</code></td><td>Download a file</td><td><code>RETR report.pdf</code></td></tr>
        <tr><td><code>STOR</code></td><td>Upload a file</td><td><code>STOR backup.tar.gz</code></td></tr>
        <tr><td><code>DELE</code></td><td>Delete a file</td><td><code>DELE oldfile.txt</code></td></tr>
        <tr><td><code>MKD</code></td><td>Create directory</td><td><code>MKD newdir</code></td></tr>
        <tr><td><code>CWD</code></td><td>Change working directory</td><td><code>CWD /pub/software</code></td></tr>
        <tr><td><code>PWD</code></td><td>Print working directory</td><td>Reply: <code>257 "/home/ajay"</code></td></tr>
        <tr><td><code>TYPE</code></td><td>Set transfer type</td><td><code>TYPE I</code> = binary, <code>TYPE A</code> = ASCII</td></tr>
        <tr><td><code>QUIT</code></td><td>End session</td><td><code>QUIT</code></td></tr>
      </tbody>
    </table>
    <p>FTP reply codes follow the same 2xx/4xx/5xx pattern as SMTP: <code>125</code>=data connection open, <code>150</code>=opening data connection, <code>200</code>=command ok, <code>226</code>=transfer complete, <code>227</code>=entering passive mode, <code>230</code>=logged in, <code>331</code>=username ok send password, <code>425</code>=can't open data connection, <code>530</code>=login incorrect.</p>
  </div>
</div>
</div>


<!-- ════════════ TAB 4 — FTP AND NAT/ALG ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">FTP ALG — HOW FIREWALLS HANDLE FTP THROUGH NAT</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>The ALG Problem — Why FTP Breaks Through NAT</h3><span class="tag tag-purple">ALG CONCEPT</span></div>
  <div class="cp-body">
    <p>FTP embeds IP addresses and port numbers inside the application payload — in PORT and PASV command responses. When a NAT device rewrites the IP header (changing private IP 10.0.0.5 to public IP 203.x.x.x), the embedded address inside the FTP data remains 10.0.0.5. The remote server tries to connect to the private address — which fails.</p>
    <p>An <strong>Application Layer Gateway (ALG)</strong> solves this by inspecting the FTP control channel payload and rewriting embedded addresses to match the NAT-translated address. This requires the firewall to:</p>
    <ol>
      <li>Identify the FTP control connection (TCP dst port 21)</li>
      <li>Maintain state for the FTP session</li>
      <li>Parse PORT/PASV commands in the control channel payload</li>
      <li>Rewrite the embedded IP/port in the payload to the post-NAT address</li>
      <li>Dynamically add a firewall rule to permit the data channel connection</li>
      <li>Remove the firewall rule when the data channel closes</li>
    </ol>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">💻</span><h3>FTP ALG in Action — Passive FTP Through NAT</h3><span class="tag tag-blue">ALG WALKTHROUGH</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Passive FTP through NAT — without ALG (broken) */</span>
 
Client private IP:  10.0.0.5
Client public IP:   203.0.113.5 (NAT)
FTP server:         198.51.100.10
 
Client → NAT → Server: PASV
Server → NAT → Client: 227 Entering Passive Mode (198,51,100,10,200,45)
                         <span class="si">← Server's real IP + port (this part is fine)</span>
Client → NAT → Server: TCP connect to 198.51.100.10:51245
                         Works! Client always initiates in passive mode.
 
<span class="cm">/* Now the problem: Active FTP through NAT (broken) */</span>
Client → NAT → Server: PORT 10,0,0,5,196,160
                         <span class="si">← Client sends its PRIVATE IP!</span>
Server tries to connect to 10.0.0.5:50336 <span class="se">← private, unreachable!</span>
<span class="se">Connection fails.</span>
 
<span class="cm">/* Active FTP through NAT — with FTP ALG */</span>
Client → NAT (ALG sees PORT command):
  Original: PORT 10,0,0,5,196,160
  ALG rewrites to: PORT 203,0,113,5,196,160   <span class="si">← replaces private IP with public IP</span>
  ALG adds dynamic firewall rule:
    PERMIT TCP from 198.51.100.10:20 to 203.0.113.5:50336
 
Client → NAT (ALG-rewritten) → Server: PORT 203,0,113,5,196,160
Server → NAT → Client: TCP connect from :20 to 203.0.113.5:50336
                        NAT translates to 10.0.0.5:50336  Works!
ALG removes dynamic rule when data channel closes.
 
<span class="cm">/* PASV through NAT with server behind NAT (also needs ALG) */</span>
Server is at private 192.168.1.100, public 203.0.113.10
Server responds: 227 Entering Passive Mode (192,168,1,100,200,45)
                 <span class="si">← server's private IP in response — client can't reach it</span>
ALG on server-side NAT rewrites to: (203,0,113,10,200,45)
                 <span class="si">← public IP — client can now connect</span></pre></div>

    <div class="warn"><p>⚠️ <strong>FTPS (FTP over TLS) breaks the ALG.</strong> When FTP uses TLS (FTPS), the control channel is encrypted — the ALG can no longer read PORT/PASV commands to rewrite them. This is why FTPS is often problematic through NAT firewalls. Solutions: use SFTP instead (SSH file transfer — completely different protocol, single connection), use FTPS with explicit passive mode and restrict the passive port range to something the firewall can statically permit.</p></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>FTP Security and NGFW Policy</h3><span class="tag tag-green">SECURITY</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>FTP sends credentials in plaintext</strong> — USER and PASS commands are ASCII text. Anyone sniffing the network sees the username and password. Block plain FTP at the internet perimeter; require SFTP (SSH-based, always encrypted) or FTPS.</li>
      <li><strong>Anonymous FTP</strong> — servers that allow <code>USER anonymous</code> with any password are a data exfiltration risk. Block outbound connections to anonymous FTP servers.</li>
      <li><strong>FTP bounce attack</strong> — an attacker uses the PORT command to make the FTP server connect to an arbitrary third-party host/port (port scanning via proxy). Mitigated by requiring PORT destination to match the client IP.</li>
      <li><strong>NGFW FTP policy</strong> — enable FTP ALG for internal users accessing external FTP, disable it at internet perimeter (block plain FTP), require SFTP or FTPS for all external transfers, scan uploaded/downloaded files for malware using the ALG inspection capability.</li>
    </ul>
<div class="cb"><pre><span class="cm"># Linux FTP client usage</span>
ftp ftp.example.com          <span class="cm"># plain FTP (avoid)</span>
sftp user@sftp.example.com   <span class="cm"># SFTP over SSH (recommended)</span>
 
<span class="cm"># Check FTP ALG status in Linux conntrack</span>
sudo modprobe nf_conntrack_ftp
sudo cat /proc/net/nf_conntrack | grep ftp
 
<span class="cm"># VPP FTP ALG (conceptual)</span>
<span class="cm"># vppctl: set ftp alg enable  — loads ftp-alg plugin</span>
<span class="cm"># Plugin inspects TCP port 21 streams, rewrites PORT/PASV payloads</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 5 — DHCP INTERNALS ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">DHCP — DYNAMIC HOST CONFIGURATION PROTOCOL (RFC 2131)</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🖥️</span><h3>What DHCP Does — And Why It's Critical</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
    <p>DHCP (RFC 2131) automatically assigns IP configuration to hosts joining a network: IP address, subnet mask, default gateway, DNS servers, lease duration, and optional parameters. Without DHCP, every device would need manual static IP configuration — impractical at any scale.</p>
    <p>DHCP also gives your NGFW crucial identity information: by snooping DHCP exchanges, the firewall learns the mapping between IP address, MAC address, and hostname — enabling meaningful per-host logging and policy. "IP 10.0.0.5 visited malware-c2.com" becomes "Ajay's laptop visited malware-c2.com".</p>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>The DORA Exchange — Discover, Offer, Request, Acknowledge</h3><span class="tag tag-teal">DORA</span></div>
  <div class="cp-body">
    <div class="flow-list">
      <div class="fl-step" data-n="D" style="--sc:#1e6b3c">
        <div>
          <div class="fl-title">DISCOVER — Client broadcasts "I need an IP"</div>
          <div class="fl-detail">Client has no IP yet. Sends DHCP Discover as a broadcast (src=0.0.0.0, dst=255.255.255.255, UDP sport=68, dport=67). Packet contains the client's MAC address (chaddr field) and optionally a hostname (Option 12) and requested parameters list (Option 55).</div>
          <div class="fl-code">0.0.0.0:68 → 255.255.255.255:67  DHCP DISCOVER  xid=0x12345678</div>
        </div>
      </div>
      <div class="fl-step" data-n="O" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">OFFER — Server responds with an available IP</div>
          <div class="fl-detail">DHCP server receives Discover (via broadcast or DHCP relay agent for remote subnets). Selects an available IP from its pool, reserves it temporarily. Replies with DHCP Offer (broadcast or unicast to MAC, src=server IP). Contains: offered IP (yiaddr), lease time, subnet mask, gateway, DNS servers as options.</div>
          <div class="fl-code">192.168.1.1:67 → 255.255.255.255:68  DHCP OFFER  IP=192.168.1.50 lease=86400s</div>
        </div>
      </div>
      <div class="fl-step" data-n="R" style="--sc:#1e6b3c">
        <div>
          <div class="fl-title">REQUEST — Client claims the offered IP</div>
          <div class="fl-detail">Client receives one or more Offers (multiple DHCP servers may respond). Client selects one and broadcasts DHCP Request — announcing its choice to all servers. Includes: requested IP (Option 50), server ID (Option 54) of chosen server. Other servers see this and release their reserved offers.</div>
          <div class="fl-code">0.0.0.0:68 → 255.255.255.255:67  DHCP REQUEST  IP=192.168.1.50 server=192.168.1.1</div>
        </div>
      </div>
      <div class="fl-step" data-n="A" style="--sc:#1a5a8c">
        <div>
          <div class="fl-title">ACKNOWLEDGE — Server confirms assignment</div>
          <div class="fl-detail">Server confirms the lease. Client can now use the IP address. ACK contains the full configuration: IP, mask, gateway, DNS (options 1, 3, 6), lease time (option 51), renewal time T1 (50% of lease), rebind time T2 (87.5% of lease). Client configures its interface.</div>
          <div class="fl-code">192.168.1.1:67 → 255.255.255.255:68  DHCP ACK  IP=192.168.1.50 lease=86400s GW=192.168.1.1 DNS=8.8.8.8</div>
        </div>
      </div>
    </div>

<div class="cb"><pre><span class="cm">/* After lease assignment — lease lifecycle */</span>
T1 (renewal time = lease/2 = 43200s):
  Client unicasts DHCP Request to same server → DHCP ACK → lease renewed
 
T2 (rebind time = lease × 0.875 = 75600s):
  If T1 renewal failed: client broadcasts DHCP Request to any server
  Any server can renew the lease at this point
 
Lease expiry:
  If rebind failed: client must release IP, restart DORA from scratch
  Client cannot use the IP after lease expires
 
<span class="cm">/* DHCP Release — client relinquishing IP */</span>
<span class="cm"># When client disconnects gracefully, sends DHCP Release</span>
<span class="cm"># Server returns IP to available pool immediately</span>
<span class="cm"># Many mobile clients DON'T send Release on WiFi disconnect (battery saving)</span>
 
<span class="cm">/* Check DHCP on Linux */</span>
dhclient eth0                              <span class="cm"># request DHCP lease</span>
dhclient -r eth0                           <span class="cm"># release lease</span>
journalctl -u systemd-networkd | grep DHCP <span class="cm"># view DHCP events</span>
cat /var/lib/dhcp/dhclient.leases          <span class="cm"># lease file</span></pre></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📦</span><h3>DHCP Packet Format</h3><span class="tag tag-green">PACKET FORMAT</span></div>
  <div class="cp-body">
    <p>DHCP packets have a fixed 236-byte base header (inherited from BOOTP) plus a variable-length options field. All four DORA messages use the same packet format — the message type is distinguished by DHCP Option 53.</p>
    <div class="dhcp-fields">
      <div class="dhcp-field"><div class="dhcp-field-name">op</div><div class="dhcp-field-size">1 byte</div><div class="dhcp-field-desc">Message type: 1=BOOTREQUEST (client→server), 2=BOOTREPLY (server→client)</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">htype / hlen</div><div class="dhcp-field-size">1 + 1 bytes</div><div class="dhcp-field-desc">Hardware type (1=Ethernet) and length (6 for MAC). Identifies address format.</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">xid</div><div class="dhcp-field-size">4 bytes</div><div class="dhcp-field-desc">Transaction ID — random number client sets. Server copies into reply. Client matches replies to requests.</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">secs</div><div class="dhcp-field-size">2 bytes</div><div class="dhcp-field-desc">Seconds elapsed since client started DHCP process. Used by relay agents for load balancing.</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">ciaddr</div><div class="dhcp-field-size">4 bytes</div><div class="dhcp-field-desc">Client's current IP address (only in RENEW/REBIND — 0 in initial Discover)</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">yiaddr</div><div class="dhcp-field-size">4 bytes</div><div class="dhcp-field-desc">"Your IP" — the IP address the server is offering to the client</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">siaddr</div><div class="dhcp-field-size">4 bytes</div><div class="dhcp-field-desc">Server IP. Set in Offer and ACK to identify the DHCP server.</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">chaddr</div><div class="dhcp-field-size">16 bytes</div><div class="dhcp-field-desc">Client hardware address (MAC address). First 6 bytes for Ethernet. This is how the server identifies the client before it has an IP.</div></div>
      <div class="dhcp-field"><div class="dhcp-field-name">options</div><div class="dhcp-field-size">variable</div><div class="dhcp-field-desc">Tag-Length-Value (TLV) encoded options. Magic cookie (4 bytes: 99.130.83.99) marks start. Option 53=DHCP message type, 51=lease time, 1=subnet mask, 3=gateway, 6=DNS, 12=hostname, 55=parameter request list</div></div>
    </div>
  </div>
</div>
</div>


<!-- ════════════ TAB 6 — DHCP SECURITY ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">DHCP SECURITY — ATTACKS AND DEFENCES</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>DHCP Attack Taxonomy</h3><span class="tag tag-red">ATTACKS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attack</th><th>How It Works</th><th>Impact</th><th>Defence</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>Rogue DHCP Server</strong></td>
          <td>Attacker runs an unauthorised DHCP server. Responds to Discover messages faster than the legitimate server. Assigns itself as the gateway or DNS server.</td>
          <td>MITM — all client traffic routed through attacker. DNS spoofing — attacker controls name resolution.</td>
          <td><strong>DHCP Snooping</strong> — switch port-level protection: only permit DHCP server responses on trusted ports (uplink to real server). All other ports are untrusted — DHCP server packets from untrusted ports are dropped.</td>
        </tr>
        <tr>
          <td><strong>DHCP Starvation</strong></td>
          <td>Attacker sends thousands of DHCP Discover requests with spoofed MAC addresses (chaddr field). Server allocates all available IPs to fake clients. Pool exhausted.</td>
          <td>Denial of Service — legitimate clients cannot get IP addresses.</td>
          <td>DHCP Snooping rate limiting: limit DHCP requests per physical switch port per second. Source MAC validation — verify chaddr matches the Ethernet frame's source MAC.</td>
        </tr>
        <tr>
          <td><strong>DHCP Relay Agent Spoofing</strong></td>
          <td>Attacker spoofs DHCP Relay Agent messages (Option 82) to claim a client is on a different subnet, getting an IP from a different pool.</td>
          <td>IP address spoofing, policy bypass.</td>
          <td>Validate relay agent IP. Drop Option 82 from untrusted sources. Configure relay on managed switches only.</td>
        </tr>
        <tr>
          <td><strong>IP Conflict Attack</strong></td>
          <td>Attacker sends gratuitous ARP claiming the IP that a victim just received from DHCP. Victim gets conflicting ARP responses, may lose connectivity.</td>
          <td>Denial of service, IP address conflict.</td>
          <td>Dynamic ARP Inspection (DAI) — validates ARP packets against DHCP snooping binding table.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>DHCP Snooping — The Core Defence</h3><span class="tag tag-purple">DHCP SNOOPING</span></div>
  <div class="cp-body">
    <p>DHCP Snooping is a switch-level security feature that builds a binding table of verified IP-to-MAC-to-port mappings. This table is used by both DHCP Snooping itself and by Dynamic ARP Inspection (DAI) and IP Source Guard (IPSG).</p>
<div class="cb"><pre><span class="cm">/* DHCP Snooping binding table */</span>
MAC Address        IP Address      Lease     VLAN  Interface
─────────────────  ──────────────  ────────  ────  ─────────
aa:bb:cc:dd:ee:ff  192.168.1.50   86400s    10    GigE0/1
11:22:33:44:55:66  192.168.1.51   86400s    10    GigE0/2
<span class="cm"># Built by snooping DHCP ACK messages on trusted ports</span>
<span class="cm"># Only the real DHCP server (trusted port) should send ACKs</span>
 
<span class="cm">/* NGFW uses this for identity-based logging */</span>
<span class="cm"># DNS query from 192.168.1.50 → look up in DHCP snooping table</span>
<span class="cm"># → hostname "ajay-laptop" (from Option 12 in Discover)</span>
<span class="cm"># → MAC aa:bb:cc:dd:ee:ff</span>
<span class="cm"># Log: "ajay-laptop (aa:bb:cc:dd:ee:ff / 192.168.1.50) queried malware.com"</span>
 
<span class="cm">/* Dynamic ARP Inspection uses the binding table */</span>
<span class="cm"># ARP from GigE0/1: "aa:bb:cc:dd:ee:ff owns 192.168.1.50"</span>
<span class="cm"># Match binding table → VALID, forward</span>
<span class="cm"># ARP from GigE0/1: "aa:bb:cc:dd:ee:ff owns 192.168.1.1" (gateway!)</span>
<span class="cm"># Not in binding table → DROP → ARP poisoning attack blocked</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 7 — NGFW POLICY ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">NGFW POLICY — SMTP, FTP, AND DHCP TOGETHER</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>Complete NGFW Policy Reference for These Protocols</h3><span class="tag tag-teal">POLICY</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Protocol</th><th>Direction</th><th>Ports</th><th>NGFW Action</th><th>Why</th></tr></thead>
      <tbody>
        <tr style="background:#e8f5e8"><td>SMTP (server relay)</td><td>Outbound</td><td>TCP 25</td><td>Allow from mail server IP only. Block from all other internal hosts.</td><td>Prevent spam from compromised internal hosts (only your MTA should send port 25)</td></tr>
        <tr style="background:#e8f5e8"><td>SMTP Submission</td><td>Outbound</td><td>TCP 587</td><td>Allow with SSL inspection</td><td>Employee mail clients. SSL inspection enables credential theft detection</td></tr>
        <tr style="background:#faeaea"><td>SMTP inbound</td><td>Inbound</td><td>TCP 25</td><td>Proxy mode — SMTP ALG. Full inspection: SPF/DKIM/DMARC, antivirus, anti-spam, attachment policy</td><td>Primary malware and phishing delivery channel</td></tr>
        <tr style="background:#faeaea"><td>Plain FTP</td><td>Both</td><td>TCP 21</td><td>Block at internet perimeter. Allow internally with ALG and file scanning.</td><td>Plaintext credentials. Use SFTP externally.</td></tr>
        <tr style="background:#e8f1f9"><td>SFTP</td><td>Both</td><td>TCP 22</td><td>Allow with DPI for known-good destinations. Log all file transfers.</td><td>Secure replacement for FTP. Still log for DLP.</td></tr>
        <tr style="background:#e8f5e8"><td>DHCP client</td><td>Inbound/Outbound</td><td>UDP 67/68</td><td>Allow on internal interfaces. Enable DHCP snooping on switch ports.</td><td>Required for IP assignment. Snooping prevents rogue servers.</td></tr>
        <tr style="background:#faeaea"><td>DHCP server from external</td><td>Inbound</td><td>UDP 67</td><td>Block at internet perimeter</td><td>External DHCP servers have no business sending to internal networks</td></tr>
        <tr style="background:#e8f1f9"><td>SMTP AUTH brute force</td><td>Inbound</td><td>TCP 587</td><td>Rate-limit per source IP. Block after 5 AUTH failures in 60 seconds.</td><td>Credential stuffing against email accounts</td></tr>
        <tr style="background:#faeaea"><td>Open SMTP relay</td><td>Inbound</td><td>TCP 25</td><td>Block RCPT TO for domains not hosted on your server (relay blocking)</td><td>Open relays used by spammers to abuse your server's reputation</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Protocol-Specific NGFW Inspection Architecture</h3><span class="tag tag-orange">ARCHITECTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* SMTP inspection pipeline in NGFW */</span>
 
Inbound SMTP:
  1. TCP accept on :25 (SMTP proxy mode)
  2. Banner response: "220 ngfw.example.com ESMTP"
  3. Parse EHLO → log sender hostname
  4. Parse MAIL FROM → SPF check (DNS lookup)
  5. Parse RCPT TO → check recipient against policy
  6. Greylisting check (first time from this IP+from+to?)
  7. Receive DATA → buffer entire message (DKIM verify requires full message)
  8. Run antivirus on attachments (decode MIME, decompress, scan)
  9. Run content/DLP scan on body
  10. DKIM verify → check DNS signature
  11. DMARC policy enforcement
  12. Apply spam score (RBL check, heuristics, ML model)
  13. If allowed: forward to internal mail server
  14. Log result: allowed/blocked/quarantined + scores
 
<span class="cm">/* FTP ALG pipeline */</span>
 
Outbound FTP:
  1. Track TCP connections to :21 as FTP control sessions
  2. Parse commands in control stream
  3. On PASV response: rewrite server IP if needed
  4. On PORT command: rewrite client private IP → public IP
  5. Add dynamic conntrack entry for data channel
  6. On data channel connection: apply file inspection policy
  7. On data channel close: remove dynamic entry
  8. Log: client, server, files transferred (via CWD/RETR/STOR tracking)
 
<span class="cm">/* DHCP identity tracking */</span>
 
On DHCP ACK intercept:
  Extract: client MAC (chaddr), offered IP (yiaddr), hostname (option 12)
  Update identity table: IP → MAC → hostname → lease_expiry
  Notify NGFW policy engine: "10.0.0.50 is now ajay-laptop (aa:bb:cc:dd:ee:ff)"
  Policy can now reference "ajay-laptop" in rules, not just IP</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 8 — LABS ════════════ -->
<div id="t8" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>SMTP Session Analysis and SPF/DKIM Verification</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Send a real SMTP session manually using telnet/openssl, capture and decode the exchange, and verify email authentication headers.</p>
    <div class="lab-step"><div class="sn">1</div><div>Interact with a local SMTP server manually using netcat: <code>nc -v localhost 25</code>. If you have postfix installed (<code>sudo apt install postfix</code>, choose "Local only"), type the full SMTP sequence: EHLO, MAIL FROM, RCPT TO, DATA with headers and body, ending with a single dot. Watch the reply codes at each step.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Capture the session: <code>sudo tcpdump -i lo -A 'port 25'</code> in parallel. Observe the plaintext commands and responses in the capture. Identify: MAIL FROM envelope address, DATA section start/end (354 → single dot), reply codes.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>SPF checking: write a Python script that takes a domain and sending IP, fetches the SPF TXT record (using <code>dnspython</code>: <code>pip install dnspython</code>), and evaluates whether the IP is permitted. Test: <code>check_spf("google.com", "209.85.220.41")</code> should return PASS. Test with a random IP — should return SOFTFAIL or FAIL.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>DKIM verification: take a real email from your inbox (in a desktop client, "Show Source" or "View Headers"). Find the DKIM-Signature header. Extract the selector and domain (s= and d= fields). Fetch the public key: <code>dig TXT {selector}._domainkey.{domain}</code>. Verify the signature using Python's <code>dkimpy</code> library or just understand the components.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>DMARC policy lookup: write a script that fetches and parses _dmarc.{domain} TXT records for 5 domains (google.com, amazon.com, github.com, a small company, your own domain if you have one). Display: policy (none/quarantine/reject), rua report address, pct (percentage), and interpret what would happen to a spoofed email from each domain.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus — STARTTLS upgrade:</strong> Connect to an SMTP server that supports TLS: <code>openssl s_client -starttls smtp -connect smtp.gmail.com:587</code>. After the TLS handshake, you're at an SMTP prompt over encrypted connection. Type EHLO and verify the capabilities. Note the certificate presented.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>FTP ALG Analysis and DHCP Dissection</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Set up a local FTP server, observe the two-channel architecture and PORT/PASV commands in Wireshark. Then capture and decode a complete DHCP DORA exchange.</p>
    <div class="lab-step"><div class="sn">1</div><div><strong>FTP setup:</strong> Install vsftpd: <code>sudo apt install vsftpd</code>. Configure for local user access. Start: <code>sudo systemctl start vsftpd</code>. Connect: <code>ftp localhost</code>. Run <code>ls</code> and <code>get /etc/hostname</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Capture with Wireshark: filter <code>ftp or ftp-data</code>. In the FTP stream, find the PASV or PORT command. For PASV: decode the 6 numbers in the response (IP = first 4 numbers as octets, Port = 5th×256 + 6th). Verify that Wireshark shows a separate TCP stream for the data channel on the calculated port.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compare active vs passive: configure your FTP client to use active mode: <code>ftp -A localhost</code>. Capture the PORT command — find your IP and ephemeral port encoded in it. Compare the data channel initiation direction: in active mode the server connects to the client; in passive the client connects to the server.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>DHCP capture:</strong> Start a Wireshark capture on a VM's interface with filter <code>bootp or dhcp</code>. Force a DHCP renewal: <code>sudo dhclient -r eth0 && sudo dhclient eth0</code>. You should see all four DORA packets. For each: identify the message type (Option 53), the transaction ID (xid), and the offered IP (yiaddr in Offer/ACK).</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Decode DHCP options: in Wireshark, expand the "Bootstrap Protocol" section in the DHCP ACK packet. Find and record: Option 1 (subnet mask), Option 3 (router/gateway), Option 6 (DNS servers), Option 12 (hostname), Option 51 (lease time in seconds), Option 53 (DHCP message type). Convert the lease time from seconds to hours.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus — DHCP starvation simulation (safe, on your own VM only):</strong> Use scapy to send multiple DHCP Discovers with random MAC addresses: <code>from scapy.all import *; [sendp(Ether(src=RandMAC())/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(6))/DHCP(options=[("message-type","discover"),"end"])) for _ in range(20)]</code>. Observe: does your DHCP server's lease pool shrink? How many genuine IPs can still be assigned?</div></div>
  </div>
</div>

</div>


<!-- ════════════ TAB 9 — CHECKLIST ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">M09 MASTERY CHECKLIST</p>

<ul class="cl">
  <li>Know the email protocol stack: MUA → port 587 → MSA → port 25 → MTA → IMAP/POP3 → MUA</li>
  <li>Know the three SMTP ports and their purposes: 25=server-to-server relay, 587=client submission (AUTH), 465=SMTPS (TLS from connect)</li>
  <li>Know why ISPs block outbound TCP 25: prevent spam from compromised machines</li>
  <li>Can walk through a complete SMTP session: EHLO → STARTTLS → AUTH → MAIL FROM → RCPT TO → DATA → dot → QUIT</li>
  <li>Know SMTP reply code categories: 2xx=success, 4xx=temporary (retry), 5xx=permanent (don't retry)</li>
  <li>Know 8 specific SMTP reply codes: 220, 221, 235, 250, 354, 421, 535, 550</li>
  <li>Understand envelope vs message headers: MAIL FROM/RCPT TO (routing) vs From:/To: (display) — these can differ enabling spoofing</li>
  <li>Know SPF: DNS TXT record listing authorised sending IPs; checked against MAIL FROM envelope sender</li>
  <li>Know DKIM: cryptographic signature over message headers+body; public key in DNS at selector._domainkey.domain</li>
  <li>Know DMARC: policy (none/quarantine/reject) applied when SPF and DKIM both fail; stored in _dmarc.domain TXT</li>
  <li>Know 7 NGFW email inspection capabilities: SMTP proxy, attachment AV, content/DLP, SPF/DKIM/DMARC enforce, anti-spam, greylisting, URL reputation</li>
  <li>Know FTP's two-connection architecture: control channel (TCP 21 — persistent) + data channel (dynamic port — per-transfer)</li>
  <li>Know Active FTP: client sends PORT command with its IP:port; server connects back to client (breaks client NAT)</li>
  <li>Know Passive FTP: client sends PASV; server provides its IP:port; client connects to server (works through client NAT)</li>
  <li>Know why EPSV was added: IPv6-compatible passive mode that only returns port number, not IP</li>
  <li>Understand the ALG problem: FTP embeds IP:port in payload; NAT changes outer IP but not payload; ALG must rewrite payload</li>
  <li>Know 6 steps of FTP ALG operation: identify control connection, parse PORT/PASV, rewrite IP, add dynamic firewall rule, scan data, remove rule on close</li>
  <li>Know why FTPS breaks ALG: encrypted control channel — ALG cannot read PORT/PASV; solution: use SFTP instead</li>
  <li>Know FTP security issues: plaintext credentials, anonymous FTP abuse, FTP bounce attack, ALG requirement</li>
  <li>Know DHCP DORA: Discover (broadcast, no IP yet) → Offer (server reserves IP) → Request (client claims IP) → ACK (server confirms)</li>
  <li>Know DHCP uses UDP 68 (client) → UDP 67 (server) with broadcast addressing (0.0.0.0 → 255.255.255.255)</li>
  <li>Know the xid field: transaction ID matching Discover to Offer/ACK</li>
  <li>Know key DHCP option numbers: 1=subnet mask, 3=gateway, 6=DNS, 12=hostname, 51=lease time, 53=message type</li>
  <li>Know DHCP lease lifecycle: T1 (50% of lease) = unicast renewal, T2 (87.5%) = broadcast rebind, expiry = restart DORA</li>
  <li>Know 4 DHCP attacks: rogue DHCP server, DHCP starvation, relay agent spoofing, IP conflict</li>
  <li>Know DHCP snooping: switch blocks DHCP server responses from untrusted ports; builds IP-MAC-port binding table</li>
  <li>Know how DHCP snooping enables DAI and identity-based logging: IP → MAC → hostname correlation</li>
  <li>Completed Lab 1: sent manual SMTP session via netcat, wrote SPF checker in Python, decoded DKIM header fields</li>
  <li>Completed Lab 2: captured FTP active/passive sessions, decoded PORT/PASV port calculation, captured full DHCP DORA, decoded all DHCP options</li>
</ul>

<!-- Phase 2 Complete Banner -->
<div class="phase-complete">
  <h3>🎉 Phase 2 Complete — Transport and Application Protocols</h3>
  <p>You have completed all 5 modules of Phase 2: TCP (M05), UDP and ICMP (M06), DNS (M07), HTTP/1.1–3 and QUIC (M08), and SMTP, FTP, DHCP (M09). You now understand every major protocol that an NGFW must inspect, filter, and protect. Move to <strong>Phase 3 — Routing and Forwarding</strong>, starting with <strong>M10 - Routing Fundamentals and FIB</strong>.</p>
</div>
</div>


<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m08-http/">← M08 HTTP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m10-routing-fundamentals/">Next: M10 - Routing and FIB →</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
