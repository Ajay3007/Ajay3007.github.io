---
layout: learning
title: "M21 - IPsec and IKEv2"
permalink: /learning/networking-mastery/m21-ipsec/
---
<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a2a0a 40%,#3a4a0a 70%,#2a3800 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c8d860;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#e0f080;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#f0ffa8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#c8d860;border-bottom-color:#c8d860}
.tab-pane{display:none}.tab-pane.active{display:block}
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
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #5a6800}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#d8e880;white-space:pre}
.cm{color:#607820}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f8fce8;border:1.5px solid #6a7a10;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#141e00;border-color:#8a9a20}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3a4800}[data-theme=dark] .ins strong{color:#c8d860}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#3a4800;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#5a6800}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #6a7a10;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#6a7a10;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#6a7a10;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#6a7a10;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 5 · MODULE 21 · WEEK 19</div>
  <div class="mod-title">🛡️ IPsec and IKEv2</div>
  <div class="mod-subtitle">ESP/AH protocols · SA and SPD · IKEv2 exchange · Transport vs tunnel mode · NAT traversal · StrongSwan</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M19 Cryptography</span>
    <span class="mod-pill">RFC 7296 · RFC 4303</span>
    <span class="mod-pill">VPN and NGFW Core</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">IPsec Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">ESP Protocol</button>
  <button class="tab-btn" onclick="vt(event,'t2')">SA and SPD</button>
  <button class="tab-btn" onclick="vt(event,'t3')">IKEv2 Exchange</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Transport vs Tunnel</button>
  <button class="tab-btn" onclick="vt(event,'t5')">NAT Traversal</button>
  <button class="tab-btn" onclick="vt(event,'t6')">IPsec in Linux</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>

<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">IPsec — INTERNET PROTOCOL SECURITY</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>IPsec Architecture</h3><span class="tag tag-green">OVERVIEW</span></div>
  <div class="cp-body">
    <p>IPsec is a suite of protocols for securing IP communications at the network layer — below TCP/UDP, meaning all applications benefit without modification. Unlike TLS (application layer), IPsec is transparent to applications. It is the standard for site-to-site VPNs, remote access VPNs, and is used between NGFW gateways.</p>
    <p>IPsec has two distinct planes:</p>
    <ul>
      <li><strong>Data plane</strong> — ESP (Encapsulating Security Payload, RFC 4303) encrypts and authenticates actual traffic. AH (Authentication Header, RFC 4302) authenticates only — rarely used today.</li>
      <li><strong>Control plane</strong> — IKEv2 (Internet Key Exchange v2, RFC 7296) negotiates SAs (Security Associations) — the parameters (algorithms, keys, lifetimes) that ESP uses. Runs over UDP 500 (and UDP 4500 for NAT traversal).</li>
    </ul>
  </div>
</div>
</div>

<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">ESP — ENCAPSULATING SECURITY PAYLOAD</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>ESP Packet Format and AEAD</h3><span class="tag tag-blue">ESP</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* ESP packet format (tunnel mode — wraps entire IP packet) */</span>
[Outer IP: src=GW1, dst=GW2, proto=50 (ESP)]
[ESP Header: SPI(4B) + Sequence Number(4B)]
[IV/Nonce: 8-16 bytes (algorithm-dependent)]
[Encrypted Payload:
  [Inner IP: src=10.1.0.5, dst=10.2.0.5]
  [TCP/UDP/ICMP payload]
  [Padding: 0-255 bytes]
  [Pad Length: 1B]
  [Next Header: 4=IPv4, 41=IPv6, 6=TCP, 17=UDP]
]
[Auth Tag / ICV: 12-16 bytes]

<span class="cm">/* SPI — Security Parameters Index */</span>
32-bit value that identifies which SA to use for decryption
Receiver uses (SPI, dst_IP, protocol=ESP) to look up the SA
SA contains: decryption key, algorithm, anti-replay window

<span class="cm">/* Sequence Number */</span>
32-bit (or 64-bit ESN) counter, starts at 1, never wraps
Anti-replay: receiver maintains a sliding window of acceptable SN
Duplicate or out-of-window SN → packet dropped

<span class="cm">/* Modern ESP cipher suites (RFC 8221) */</span>
AES-256-GCM-16:     AES-256 GCM with 16-byte ICV (recommended)
AES-128-GCM-16:     AES-128 GCM with 16-byte ICV
ChaCha20-Poly1305:  For devices without AES-NI

<span class="cm">/* Combined mode AEAD (GCM): */</span>
Authenticated:  ESP header + IV (as AAD)
Encrypted:      payload + padding + next_header
ICV:            16-byte authentication tag

<span class="cm">/* AH vs ESP */</span>
AH (proto 51):  authenticates IP header + payload (no encryption)
                Problem: AH covers IP header fields that NAT changes → NAT breaks AH
ESP (proto 50): encrypts payload + authenticates ESP header
                Does NOT authenticate outer IP header → NAT compatible
Recommendation: always use ESP with authentication (GCM or AES-CBC + HMAC)</pre></div>
  </div>
</div>
</div>

<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">SA, SPD, AND SAD — THE IPsec POLICY AND STATE DATABASES</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🗄️</span><h3>Security Policy Database and Security Association Database</h3><span class="tag tag-purple">SA DATABASES</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* SPD — Security Policy Database */</span>
<span class="cm">/* Defines what to do with each traffic flow */</span>

Policy selector (matches on):
  Source IP/prefix, Destination IP/prefix
  Source port range, Destination port range
  Protocol (TCP, UDP, ICMP, any)

Policy action:
  BYPASS:  send without IPsec (for IKE traffic, local management)
  PROTECT: encrypt with IPsec (most traffic)
  DISCARD: drop (block)

Example SPD:
  10.1.0.0/24 → 10.2.0.0/24  any   PROTECT (tunnel to remote site)
  0.0.0.0/0   → 0.0.0.0/0    UDP:500 BYPASS  (allow IKE to negotiate)
  0.0.0.0/0   → 0.0.0.0/0    any   DISCARD (block unprotected traffic)

<span class="cm">/* SAD — Security Association Database */</span>
<span class="cm">/* Each SA contains the actual keys and parameters for one direction */</span>

SA = {
  SPI:             32-bit identifier (receiver chooses, sender uses)
  Protocol:        ESP (50) or AH (51)
  Mode:            tunnel or transport
  Encryption alg:  AES-256-GCM
  Encryption key:  256-bit key (derived by IKEv2)
  Auth alg:        (not needed for GCM — AEAD provides both)
  Lifetime:        3600 seconds or 4GB bytes (whichever first)
  Sequence number: current counter
  Anti-replay window: 64-bit bitmap
}

<span class="cm">/* SAs are unidirectional — one pair per IPsec connection */</span>
Inbound SA:  (SPI=0x12345678) → decrypt packets FROM remote
Outbound SA: (SPI=0xabcdef01) → encrypt packets TO remote

<span class="cm">/* Linux kernel IPsec state */</span>
ip xfrm state          <span class="cm"># show SA database (SAD)</span>
ip xfrm policy         <span class="cm"># show policy database (SPD)</span>
ip xfrm state add src 10.0.0.1 dst 10.0.0.2 proto esp spi 0x12345678 \
    mode tunnel enc "aes-gcm-esp" 0x... aead-icv-len 128</pre></div>
  </div>
</div>
</div>

<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">IKEv2 — THE KEY EXCHANGE AND NEGOTIATION PROTOCOL</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>IKEv2 Exchange Flow</h3><span class="tag tag-teal">IKEv2</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* IKEv2 establishes the IPsec SA parameters via two exchanges */</span>
<span class="cm">/* All IKE runs over UDP 500 (or 4500 for NAT-T) */</span>

INITIATOR                              RESPONDER
    │                                      │
    │── IKE_SA_INIT ─────────────────────→ │
    │   SA: proposed IKE algorithms         │
    │     (enc: AES-256-CBC/GCM,            │
    │      prf: HMAC-SHA256/SHA384,         │
    │      integ: HMAC-SHA256,              │
    │      dh: ECP-256/384, DH-2048)       │
    │   KE: Diffie-Hellman public value     │
    │   Ni: Nonce (random bytes)            │
    │                                      │
    │←── IKE_SA_INIT ───────────────────── │
    │   SA: selected IKE algorithms         │
    │   KE: Responder DH public value       │
    │   Nr: Responder nonce                 │
    │                                      │
    │ [Both compute SKEYSEED = PRF(Ni|Nr, DH_shared)]
    │ [Derive 7 IKE SA keys via PRF+ ]      │
    │ [All subsequent messages ENCRYPTED]   │
    │                                      │
    │── IKE_AUTH ─────────────────────────→│
    │   IDi: Initiator identity (FQDN or IP)│
    │   CERT: optional certificate          │
    │   AUTH: signature or PSK HMAC        │
    │   SAi: proposed Child SA (ESP) params │
    │   TSi: Traffic selector (initiator)   │
    │   TSr: Traffic selector (responder)   │
    │                                      │
    │←── IKE_AUTH ────────────────────────  │
    │   IDr: Responder identity             │
    │   CERT: certificate                   │
    │   AUTH: signature/PSK                 │
    │   SAr: selected Child SA params       │
    │   TSi/TSr: confirmed traffic selectors│
    │                                      │
    │ [Child SA (ESP) established]          │
    │ [Keys derived from IKE SA keys]       │

<span class="cm">/* Authentication methods */</span>
RSA signatures:    certificate-based (common for site-to-site)
ECDSA:             modern certificate auth
Pre-Shared Key:    shared secret (PSK) — simpler but less scalable
EAP:               for remote access users (EAP-TLS, EAP-MSCHAPv2)

<span class="cm">/* IKEv2 additional exchanges */</span>
CREATE_CHILD_SA:   create additional SAs (multiple tunnels, rekey)
INFORMATIONAL:     SA deletion, liveness check (dead peer detection)

<span class="cm">/* Key material derivation */</span>
SKEYSEED = PRF(Ni | Nr, g^ir)           <span class="cm">/* g^ir = DH shared secret */</span>
{SK_d | SK_ai | SK_ar | SK_ei | SK_er | SK_pi | SK_pr} =
    PRF+(SKEYSEED, Ni | Nr | SPIi | SPIr)
<span class="cm">/* SK_d: used to derive Child SA keys */</span>
<span class="cm">/* SK_e: encryption keys for IKE SA */</span>
<span class="cm">/* SK_a: integrity keys for IKE SA */</span>
<span class="cm">/* SK_p: authentication (PRF input) */</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">TRANSPORT VS TUNNEL MODE</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>Mode Comparison</h3><span class="tag tag-orange">MODES</span></div>
  <div class="cp-body">
    <div class="two-col">
      <div>
        <h4>Transport Mode</h4>
        <p>ESP header inserted between IP header and the transport (TCP/UDP) payload. The original IP header is preserved and visible. Only the transport layer and above are encrypted.</p>
<div class="cb"><pre><span class="cm">/* Transport mode packet */</span>
[IP: src=A dst=B]
[ESP Header]
[Encrypted: TCP + data]
[ESP Auth]

<span class="cm">/* Use: host-to-host encryption */</span>
<span class="cm">/* Both endpoints must have IPsec */</span>
<span class="cm">/* Lower overhead (no extra IP hdr) */</span>
<span class="cm">/* Used with GRE: GRE+IPsec transport */</span></pre></div>
      </div>
      <div>
        <h4>Tunnel Mode</h4>
        <p>The entire original IP packet is encrypted and encapsulated inside a new IP packet with gateway addresses as src/dst. Inner IP (with real endpoint addresses) is hidden from network observers.</p>
<div class="cb"><pre><span class="cm">/* Tunnel mode packet */</span>
[Outer IP: GW1→GW2]
[ESP Header]
[Encrypted:
  [Inner IP: A→B]
  [TCP + data]]
[ESP Auth]

<span class="cm">/* Use: site-to-site VPN */</span>
<span class="cm">/* Gateways encrypt/decrypt */</span>
<span class="cm">/* Endpoints unaware of IPsec */</span>
<span class="cm">/* Standard for NGFW VPN */</span></pre></div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">NAT TRAVERSAL — IPsec THROUGH NAT</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>UDP Encapsulation for NAT Traversal</h3><span class="tag tag-red">NAT-T</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Problem: ESP is IP protocol 50 (not TCP/UDP) */</span>
<span class="cm">/* NAT translates TCP/UDP port numbers — has no concept of ESP SPI */</span>
<span class="cm">/* Multiple ESP sessions through same NAT → ambiguity (which client?) */</span>

<span class="cm">/* NAT-T (NAT Traversal) — RFC 3948 */</span>
<span class="cm">/* Encapsulate ESP inside UDP to allow NAT translation */</span>

IKEv2 NAT detection:
  IKE_SA_INIT includes NAT_DETECTION_SOURCE_IP and NAT_DETECTION_DESTINATION_IP
  payloads (hashes of IP:port). If hash mismatch → NAT detected.

If NAT detected:
  IKE switches to UDP 4500 (instead of 500)
  ESP packets wrapped in UDP 4500 header
  NAT translates the UDP port → multiple clients possible

<span class="cm">/* NAT-T packet structure */</span>
[Outer IP: src=client_public_IP, dst=VPN_GW]
[UDP: sport=4500 dport=4500]
[Non-ESP Marker: 0x00000000 (4 bytes, distinguishes from IKE)]
[ESP header + encrypted payload]

<span class="cm">/* Keepalive for NAT mappings */</span>
<span class="cm">/* NAT state tables expire idle UDP sessions (often 30-120s) */</span>
<span class="cm">/* IKEv2 NAT-T keepalive: single 0xFF byte every 20s on UDP 4500 */</span>
dpd-timeout 30         <span class="cm"># StrongSwan: dead peer detection</span>
nat-keepalive 20       <span class="cm"># keepalive interval</span>

<span class="cm">/* AH cannot work through NAT */</span>
<span class="cm">/* AH authenticates the outer IP header including src IP */</span>
<span class="cm">/* NAT changes src IP → AH authentication fails → AH is dead */</span>
<span class="cm">/* Always use ESP for NAT-compatible IPsec */</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">IPsec IN LINUX — XFRM AND STRONGSWAN</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🐧</span><h3>Linux IPsec Configuration</h3><span class="tag tag-blue">LINUX</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Linux IPsec: kernel handles ESP (via xfrm), StrongSwan handles IKEv2 */</span>

<span class="cm">/* /etc/swanctl/swanctl.conf — StrongSwan IKEv2 config */</span>
connections {
  site-to-site {
    local_addrs  = 203.0.113.1      <span class="cm"># our gateway IP</span>
    remote_addrs = 198.51.100.1     <span class="cm"># peer gateway IP</span>

    local {
      auth  = pubkey                <span class="cm"># certificate authentication</span>
      certs = gw1-cert.pem
      id    = "gw1.example.com"
    }
    remote {
      auth  = pubkey
      id    = "gw2.example.com"
    }

    children {
      tunnel {
        local_ts   = 10.1.0.0/24   <span class="cm"># traffic selectors</span>
        remote_ts  = 10.2.0.0/24
        esp_proposals = aes256gcm128-prfsha384-ecp384  <span class="cm"># cipher suite</span>
        mode      = tunnel
        dpd_action = restart       <span class="cm"># restart tunnel on DPD failure</span>
      }
    }
    ike_proposals = aes256gcm16-prfsha384-ecp384
    version = 2
    dpd_delay = 30s
  }
}

<span class="cm"># Start IKEv2 negotiation</span>
swanctl --load-all
swanctl --initiate --child tunnel

<span class="cm"># Monitor</span>
swanctl --list-sas        <span class="cm"># show active IKE and Child SAs</span>
ip xfrm state             <span class="cm"># kernel ESP SAs (keys, algorithms, byte counts)</span>
ip xfrm policy            <span class="cm"># kernel SPD (traffic selectors, actions)</span>
ip xfrm monitor           <span class="cm"># real-time SA events</span>

<span class="cm"># Check tunnel traffic</span>
tcpdump -i eth0 esp       <span class="cm"># ESP packets</span>
tcpdump -i eth0 udp port 500 or udp port 4500  <span class="cm"># IKE packets</span>

<span class="cm">/* XFRM offload to hardware (Intel QAT, Mellanox IPsec offload) */</span>
<span class="cm"># For your Mellanox ConnectX cards:</span>
<span class="cm"># ip xfrm state add ... offload dev eth0 dir in</span>
<span class="cm"># Pushes ESP encryption/decryption to NIC — reduces CPU overhead significantly</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Site-to-Site IPsec VPN with StrongSwan</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Configure a complete IKEv2/IPsec tunnel between two Linux VMs using StrongSwan. Capture and analyse IKEv2 and ESP traffic.</p>
    <div class="lab-step"><div class="sn">1</div><div>Set up two VMs: GW1 (10.0.0.1, serves 192.168.1.0/24) and GW2 (10.0.0.2, serves 192.168.2.0/24). Install StrongSwan: <code>sudo apt install strongswan strongswan-swanctl</code>. Generate certificates with StrongSwan's PKI: <code>pki --gen --type ecdsa --size 256 > ca.der; pki --self --ca --in ca.der --dn "C=IN, O=Test, CN=Test CA" > ca.crt</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Create gateway certificates signed by the test CA. Configure swanctl.conf on both gateways as shown in Tab 6. Start StrongSwan: <code>sudo systemctl start strongswan</code>. Initiate the tunnel: <code>sudo swanctl --initiate --child tunnel</code>. Verify: <code>sudo swanctl --list-sas</code> shows ESTABLISHED.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Capture IKEv2: <code>sudo tcpdump -i eth0 -w /tmp/ike.pcap udp port 500</code> while initiating the tunnel. Open in Wireshark — decode as IKEv2. Identify: IKE_SA_INIT (two messages), IKE_AUTH (two messages). Note which packets are plaintext (IKE_SA_INIT) vs encrypted (IKE_AUTH).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Test the tunnel: ping from 192.168.1.5 (behind GW1) to 192.168.2.5 (behind GW2). Capture ESP packets: <code>tcpdump -i eth0 esp</code>. Verify: IP protocol is 50 (ESP). Check the kernel SA byte counters: <code>ip xfrm state | grep bytes</code> — should increase as traffic flows. Try pinging an address outside the traffic selector — verify it's NOT tunnelled.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Manual XFRM SA — IPsec Without IKE</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Configure IPsec manually using ip xfrm commands (no IKEv2). This shows exactly what IKEv2 does automatically and deepens understanding of the SA/SPD model.</p>
    <div class="lab-step"><div class="sn">1</div><div>On both VMs, manually add SAs using <code>ip xfrm state add</code>. Choose a random 256-bit key: <code>openssl rand -hex 32</code>. Create the inbound and outbound SAs on each machine with matching SPIs and the same key. Use AES-256-GCM: <code>aead "rfc4106(gcm(aes))" 0xKEY 128</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add security policies: <code>ip xfrm policy add src 192.168.1.0/24 dst 192.168.2.0/24 dir out tmpl src GW1 dst GW2 proto esp mode tunnel</code>. Add the reverse policy. Verify: <code>ip xfrm state</code> shows 2 SAs; <code>ip xfrm policy</code> shows 2 policies.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Ping across the tunnel. Capture and verify ESP packets appear. Check <code>ip xfrm state | grep -A5 "bytes"</code> — counters should increment. Now intentionally set a wrong key on one side. Verify pings fail (authentication error) and find the error counter in <code>ip xfrm state</code>.</div></div>
  </div>
</div>
</div>

<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M21 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know IPsec two planes: data plane (ESP encrypts traffic) and control plane (IKEv2 negotiates keys)</li>
  <li>Know ESP packet format: outer IP + ESP header (SPI + SN) + IV + encrypted payload + auth tag</li>
  <li>Know SPI: 32-bit identifier in ESP header tells receiver which SA (and key) to use for decryption</li>
  <li>Know anti-replay: sequence number + sliding window; duplicate or out-of-window SN → drop</li>
  <li>Know modern ESP cipher: AES-256-GCM-16 (AEAD — no separate auth needed)</li>
  <li>Know why AH is rarely used: covers outer IP header → incompatible with NAT</li>
  <li>Know SPD (Security Policy Database): selector (src/dst IP, port) → action (PROTECT/BYPASS/DISCARD)</li>
  <li>Know SAD (Security Association Database): one SA per direction; contains SPI, keys, algorithm, lifetime, anti-replay state</li>
  <li>Know SAs are unidirectional: one pair (inbound + outbound) per IPsec connection</li>
  <li>Know IKEv2 exchange: IKE_SA_INIT (DH key exchange, algorithm negotiation) → IKE_AUTH (authentication, Child SA creation)</li>
  <li>Know IKEv2 key derivation: SKEYSEED = PRF(Ni|Nr, DH_shared) → 7 IKE SA keys via PRF+</li>
  <li>Know IKEv2 authentication methods: RSA/ECDSA certificates, PSK, EAP</li>
  <li>Know transport mode: protects IP payload, preserves IP header — for host-to-host</li>
  <li>Know tunnel mode: encapsulates entire IP packet in new IP — for site-to-site VPN (gateway-to-gateway)</li>
  <li>Know why NAT breaks ESP: NAT changes IP headers, but ESP SPI is not a port number NAT can track</li>
  <li>Know NAT-T: encapsulate ESP inside UDP 4500; IKE detects NAT via NAT_DETECTION payloads</li>
  <li>Know Linux IPsec: kernel xfrm handles ESP; StrongSwan handles IKEv2; ip xfrm state/policy commands</li>
  <li>Know XFRM offload: push ESP encrypt/decrypt to NIC (Mellanox ConnectX) — saves CPU cycles</li>
  <li>Completed Lab 1: configured site-to-site IKEv2 with StrongSwan; captured and decoded IKEv2/ESP traffic</li>
  <li>Completed Lab 2: manually configured XFRM SAs; verified encryption, tested wrong-key failure</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M22 - SSL/TLS Inspection and PKI Operations</strong> — the final Phase 5 module, bringing together TLS and PKI knowledge into operational NGFW inspection workflows.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/networking-mastery/m20-tls/' | relative_url }}">← M20 TLS</a>
  <a href="{{ '/learning/networking-mastery/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m22-ssl-inspection/' | relative_url }}">Next: M22 - SSL Inspection →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
