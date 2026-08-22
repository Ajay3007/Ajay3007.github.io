---
title: "M20 - TLS Internals"
description: "NETWORKING MASTERY · PHASE 5 · MODULE 20 · WEEK 18 🔒 TLS Internals TLS 1.3 handshake · Record protocol · Cipher suites · Certificate validation · 0-RTT · mTLS · SSL inspection…"
domain: networking
track: networking-mastery
order: 20
url: /learning/networking-mastery/m20-tls/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#0a2a3a 40%,#0a4a6a 70%,#0a2a5a 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#80d0f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#b0e8ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d0f0ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#80d0f0;border-bottom-color:#80d0f0}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a6a9c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#b0e0f8;white-space:pre}
.cm{color:#406880}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f4ff;border:1.5px solid #1a6a9c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2038;border-color:#2a8ac0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0a3a5c}[data-theme=dark] .ins strong{color:#80d0f0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#0a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5a8c}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a6a9c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a6a9c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a6a9c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a6a9c;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 5 · MODULE 20 · WEEK 18</div>
  <div class="mod-title">🔒 TLS Internals</div>
  <div class="mod-subtitle">TLS 1.3 handshake · Record protocol · Cipher suites · Certificate validation · 0-RTT · mTLS · SSL inspection</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M19 Cryptography</span>
    <span class="mod-pill">RFC 8446</span>
    <span class="mod-pill">Ubiquitous — Every HTTPS Connection</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">TLS Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">TLS 1.3 Handshake</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Key Schedule</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Record Protocol</button>
  <button class="tab-btn" onclick="vt(event,'t4')">TLS 1.2 vs 1.3</button>
  <button class="tab-btn" onclick="vt(event,'t5')">0-RTT and Session Resumption</button>
  <button class="tab-btn" onclick="vt(event,'t6')">mTLS and Client Auth</button>
  <button class="tab-btn" onclick="vt(event,'t7')">SSL Inspection</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>

<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">TLS — TRANSPORT LAYER SECURITY</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>TLS in the Protocol Stack</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
    <p>TLS (Transport Layer Security) is the protocol that makes HTTPS, SMTPS, IMAPS, FTPS, and many other "S" protocols secure. It sits between TCP and the application layer, providing: server authentication (via certificates), optional client authentication (mTLS), forward-secret key exchange (ECDHE), and authenticated encryption of all application data.</p>
    <p>TLS 1.3 (RFC 8446, 2018) is the current standard. It eliminated all deprecated algorithms, reduced handshake latency from 2 RTTs to 1 RTT (0 RTT for resumption), and simplified the protocol significantly. Understanding TLS 1.3 is essential for NGFW because HTTPS carries the majority of internet traffic — and inspecting it requires understanding or terminating the TLS session.</p>
  </div>
</div>
</div>

<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">TLS 1.3 HANDSHAKE — 1 RTT TO ENCRYPTED DATA</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>TLS 1.3 Full Handshake</h3><span class="tag tag-blue">HANDSHAKE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* TLS 1.3 Handshake — message flow */</span>

CLIENT                                           SERVER
  │                                                │
  │─── ClientHello ────────────────────────────→  │
  │    • client_random (32 bytes)                  │
  │    • supported_versions: [TLS 1.3, TLS 1.2]   │
  │    • supported_groups: [X25519, P-256, P-384]  │
  │    • key_share: X25519 ephemeral pubkey        │
  │    • signature_algs: [Ed25519, ECDSA P-256,    │
  │                        RSA-PSS-SHA256]         │
  │    • server_name (SNI): "example.com"          │
  │    • psk_ke_modes (if resuming)                │
  │                                                │
  │←── ServerHello ────────────────────────────── │
  │    • server_random (32 bytes)                  │
  │    • selected cipher: TLS_AES_256_GCM_SHA384   │
  │    • key_share: X25519 server ephemeral pubkey │
  │    • selected TLS version: 1.3                 │
  │                                                │
  │ [ECDH shared secret computed by both sides]    │
  │ [Handshake keys derived via HKDF]              │
  │ [All subsequent messages are ENCRYPTED]        │
  │                                                │
  │←── {EncryptedExtensions} ─────────────────── │
  │    • ALPN: "h2" (HTTP/2 negotiated)            │
  │    • max_fragment_length, server_cert_type      │
  │                                                │
  │←── {Certificate} ──────────────────────────── │
  │    • Server's X.509 certificate chain          │
  │                                                │
  │←── {CertificateVerify} ────────────────────── │
  │    • Signature over transcript hash            │
  │      (proves server has private key)           │
  │                                                │
  │←── {Finished} ─────────────────────────────── │
  │    • HMAC over entire handshake transcript     │
  │      (proves handshake integrity)              │
  │                                                │
  │─── {Finished} ──────────────────────────────→ │
  │    • Client's HMAC over transcript             │
  │                                                │
  │←→  {Application Data (AEAD encrypted)} ←────→ │

RTT count: 1 full RTT before application data can flow
           (ClientHello → ServerHello+Cert+Finished → ClientFinished+AppData)</pre></div>
    <div class="ins"><p>💡 <strong>Key insight:</strong> In TLS 1.3, the server can send encrypted extensions, its certificate, and its Finished message all in one flight — before receiving anything from the client beyond ClientHello. This is possible because ECDHE allows the server to derive encryption keys immediately after seeing the client's key share. The client verifies the server's Finished HMAC to confirm the handshake wasn't tampered with.</p></div>
  </div>
</div>
</div>

<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">TLS 1.3 KEY SCHEDULE — HOW KEYS ARE DERIVED</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🗝️</span><h3>HKDF-Based Key Schedule</h3><span class="tag tag-purple">KEY SCHEDULE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* TLS 1.3 Key Schedule (RFC 8446 §7.1) */</span>
<span class="cm">/* All derivations use HKDF with the negotiated hash (SHA-256 or SHA-384) */</span>

0 (Early Secret)
  ├─ Early Traffic Keys (for 0-RTT data, if resuming with PSK)
  │
  ↓ HKDF-Extract(PSK or 0-bytes, Early Secret)
Handshake Secret
  ├─ client_handshake_traffic_secret
  │   → client_handshake_key (AES key for client→server during handshake)
  │   → client_handshake_iv  (nonce base)
  ├─ server_handshake_traffic_secret
  │   → server_handshake_key (AES key for server→client during handshake)
  │   → server_handshake_iv
  │
  ↓ HKDF-Extract(ECDHE shared secret, Handshake Secret)
Master Secret
  ├─ client_application_traffic_secret_0
  │   → client_write_key (AES key for client→server application data)
  │   → client_write_iv
  ├─ server_application_traffic_secret_0
  │   → server_write_key (AES key for server→client application data)
  │   → server_write_iv
  ├─ exporter_master_secret (for channel binding)
  └─ resumption_master_secret (for session tickets / PSK resumption)

<span class="cm">/* Nonce construction — prevents nonce reuse */</span>
<span class="cm">/* For each record: nonce = write_iv XOR sequence_number (64-bit, left-padded) */</span>
<span class="cm">/* Sequence number increments with each record → unique nonce per record */</span>

<span class="cm">/* Key update (post-handshake) */</span>
<span class="cm">/* Either side can send KeyUpdate message → derive new traffic keys */</span>
new_secret = HKDF-Expand-Label(current_secret, "traffic upd", "", hash_len)
<span class="cm">/* Forward secrecy within a session: old keys deleted, new keys derived */</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">TLS RECORD PROTOCOL — WIRE FORMAT</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📦</span><h3>TLS Record Structure</h3><span class="tag tag-teal">RECORD FORMAT</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* TLS Record format (all TLS versions) */</span>
+------------------+------------------+------------------+
| Content Type (1B)| Version (2B)     | Length (2B)      |
+------------------+------------------+------------------+
| Payload (up to 16384 bytes)                            |
+--------------------------------------------------------+

Content Types:
  20 = change_cipher_spec (legacy, sent for TLS 1.2 compat)
  21 = alert             (error notification)
  22 = handshake         (ClientHello, ServerHello, Certificate, etc.)
  23 = application_data  (encrypted payload)

Version field in TLS 1.3:
  Outer record: 0x0303 (TLS 1.2) — for middlebox compatibility
  Inner content_type (inside AEAD ciphertext): real type

<span class="cm">/* TLS 1.3 Application Data record layout */</span>
+------+--------+--------+----------------------------------+----------+
| 0x17 | 0x0303 | length | Encrypted(application_data +     | auth_tag |
|  23  | TLS1.2 | 2B     | inner_content_type) — AEAD       | 16B      |
+------+--------+--------+----------------------------------+----------+

<span class="cm">/* AEAD inputs for encrypting a record */</span>
Plaintext:  application_data bytes + inner_content_type (1 byte at end)
AAD:        TLS record header (5 bytes: type + version + length)
Key:        write_key (from key schedule)
Nonce:      write_iv XOR (seq_number as 12-byte big-endian)

<span class="cm">/* Maximum record size */</span>
16384 bytes (2^14) of plaintext per record
+ 256 bytes of padding (optional, hides true record size)
+ 16 bytes auth tag
= up to 16657 bytes per record

<span class="cm">/* Alert record format (2 bytes inside TLS record) */</span>
Level:       1=warning, 2=fatal
Description: 0=close_notify, 10=unexpected_message, 20=bad_record_mac,
             42=bad_certificate, 48=unknown_ca, 70=protocol_version,
             80=internal_error, 100=no_renegotiation, 112=unrecognized_name (SNI)

<span class="cm">/* Wireshark TLS decryption */</span>
SSLKEYLOGFILE=/tmp/keys.log curl https://example.com
<span class="cm"># In Wireshark: Edit → Preferences → TLS → Master-Secret log file → /tmp/keys.log</span>
<span class="cm"># Wireshark will decrypt all TLS records and show plaintext handshake + data</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">TLS 1.2 vs TLS 1.3 — KEY DIFFERENCES</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📊</span><h3>What Changed from TLS 1.2 to 1.3</h3><span class="tag tag-orange">COMPARISON</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Feature</th><th>TLS 1.2</th><th>TLS 1.3</th></tr></thead>
      <tbody>
        <tr><td>Handshake RTTs</td><td>2 RTTs minimum</td><td>1 RTT (0 RTT for resumption)</td></tr>
        <tr><td>Forward secrecy</td><td>Optional (ECDHE or static RSA)</td><td>Mandatory (ECDHE always)</td></tr>
        <tr><td>Cipher suites</td><td>Hundreds incl. RC4, 3DES, NULL, anon</td><td>5 only, all AEAD</td></tr>
        <tr><td>Key exchange</td><td>RSA, ECDHE, DHE, ECDH (static)</td><td>ECDHE, DHE (finite field) only</td></tr>
        <tr><td>Certificate encryption</td><td>Plaintext in handshake (visible to network)</td><td>Encrypted (after server key derived)</td></tr>
        <tr><td>Renegotiation</td><td>Allowed (caused vulnerabilities)</td><td>Removed entirely</td></tr>
        <tr><td>Compression</td><td>Optional (CRIME attack)</td><td>Removed</td></tr>
        <tr><td>MAC-then-Encrypt</td><td>Used in CBC mode (BEAST, POODLE)</td><td>Removed — AEAD only</td></tr>
        <tr><td>Session IDs</td><td>Server stores session state</td><td>Stateless session tickets only</td></tr>
        <tr><td>SNI encryption</td><td>No (SNI in cleartext ClientHello)</td><td>ECH (Encrypted ClientHello) — draft</td></tr>
        <tr><td>Removed from TLS 1.3</td><td>—</td><td>RSA key exchange, CBC, RC4, 3DES, MD5, SHA-1, renegotiation, compression, DSA</td></tr>
      </tbody>
    </table>

    <h4>TLS 1.3 Cipher Suites — Only 5</h4>
<div class="cb"><pre>TLS_AES_128_GCM_SHA256          (most common, high performance)
TLS_AES_256_GCM_SHA384          (higher security)
TLS_CHACHA20_POLY1305_SHA256    (mobile/ARM performance)
TLS_AES_128_CCM_SHA256          (constrained IoT)
TLS_AES_128_CCM_8_SHA256        (constrained IoT, shorter tag)

<span class="cm"># Note: no key exchange or auth in TLS 1.3 cipher suites</span>
<span class="cm"># Key exchange is always ECDHE (negotiated separately in supported_groups)</span>
<span class="cm"># Authentication is always certificate-based (negotiated in signature_algs)</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">0-RTT AND SESSION RESUMPTION</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>PSK and 0-RTT Early Data</h3><span class="tag tag-green">0-RTT</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* TLS 1.3 session resumption via PSK (Pre-Shared Key) */</span>

After a successful TLS 1.3 handshake, the server sends a NewSessionTicket:
  - Contains a PSK (pre-shared key) encrypted with a server-only ticket key
  - Includes a ticket_lifetime (e.g., 7 days)
  - Client stores this opaque blob

On reconnect, client includes the PSK in ClientHello:
  - pre_shared_key extension: ticket blob
  - psk_key_exchange_modes: psk_dhe_ke (PSK + ephemeral DH — recommended)
                            or psk_ke (PSK only — no forward secrecy!)
  - early_data extension: client wants to send 0-RTT data

<span class="cm">/* 0-RTT early data — zero round-trip cost */</span>

Standard 1-RTT:     ClientHello → ServerHello+Cert+Finished → {AppData}
0-RTT resumption:   ClientHello + {EarlyData} → ServerHello → {AppData}
                    ↑ Application data piggybacks on ClientHello!

<span class="cm">/* 0-RTT security limitations */</span>
Replay attack risk:
  Attacker captures ClientHello+EarlyData, replays it to server.
  Server has no way to distinguish replay from original!
  
  Mitigations:
  1. Only use 0-RTT for idempotent requests (GET, not POST)
  2. Server-side replay detection (store nonces, use anti-replay window)
  3. Accept risk for non-sensitive use (performance vs security tradeoff)

0-RTT does NOT provide forward secrecy for early data:
  If PSK ticket key is compromised → early data decryptable
  Post-handshake application data DOES have forward secrecy (ECDHE)

<span class="cm">/* NGFW considerations for 0-RTT */</span>
<span class="cm"># 0-RTT early data is encrypted with the early_traffic_key</span>
<span class="cm"># Without the PSK or TLS session keys, NGFW cannot decrypt 0-RTT</span>
<span class="cm"># SSL inspection proxy must handle 0-RTT specially</span>
<span class="cm"># Many NGFW products simply reject 0-RTT by not returning early_data in EncryptedExtensions</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">mTLS — MUTUAL AUTHENTICATION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Client Certificate Authentication</h3><span class="tag tag-purple">mTLS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Standard TLS: only server is authenticated */</span>
<span class="cm">/* mTLS (mutual TLS): both server AND client present certificates */</span>

<span class="cm">/* mTLS handshake additions */</span>
After sending Certificate + CertificateVerify + Finished, server sends:
  CertificateRequest: list of acceptable CA DNs for client certificates

Client responds with:
  Certificate: client's X.509 certificate (or empty if none available)
  CertificateVerify: signature over handshake transcript with client private key
  Finished: as normal

<span class="cm">/* Use cases for mTLS */</span>
Service mesh (Istio, Linkerd): all microservices authenticate each other
Zero-trust networks: every connection requires client cert (device identity)
API security: client apps authenticate with cert instead of API keys
IoT devices: device certificates for mutual auth to backend
NGFW policy: require client cert for access to sensitive internal resources

<span class="cm">/* Configure nginx for mTLS */</span>
ssl_client_certificate /etc/ssl/ca.pem;  # CA that signed client certs
ssl_verify_client on;                     # require client cert
ssl_verify_depth 2;                       # allow one intermediate CA

<span class="cm">/* OpenSSL mTLS server in C */</span>
SSL_CTX *ctx = SSL_CTX_new(TLS_server_method());
SSL_CTX_load_verify_locations(ctx, <span class="cs">"ca.pem"</span>, NULL);
SSL_CTX_use_certificate_file(ctx, <span class="cs">"server.pem"</span>, SSL_FILETYPE_PEM);
SSL_CTX_use_PrivateKey_file(ctx, <span class="cs">"server.key"</span>, SSL_FILETYPE_PEM);
SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER | SSL_VERIFY_FAIL_IF_NO_PEER_CERT, NULL);

<span class="cm">/* After SSL_accept(): inspect client certificate */</span>
X509 *client_cert = SSL_get_peer_certificate(ssl);
X509_NAME *subj = X509_get_subject_name(client_cert);
char cn[256];
X509_NAME_get_text_by_NID(subj, NID_commonName, cn, sizeof(cn));
printf(<span class="cs">"Client cert CN: %s\n"</span>, cn);
X509_free(client_cert);</pre></div>
  </div>
</div>
</div>

<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<p class="sep">SSL INSPECTION — NGFW TLS INTERCEPTION</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>How SSL/TLS Inspection Works</h3><span class="tag tag-red">SSL INSPECTION</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* SSL inspection (TLS MITM proxy) — the NGFW's view */</span>

Normal TLS:
  Client ←── TLS ──→ Server
  Client trusts server's cert from a real CA
  NGFW sees: encrypted bytes → cannot inspect content

SSL inspection:
  Client ←── TLS ──→ NGFW ←── TLS ──→ Server
  
  NGFW-Server leg:
    NGFW establishes TLS to the real server
    Validates server's real certificate
    NGFW has the session keys → can decrypt/inspect server responses
  
  Client-NGFW leg:
    NGFW generates a certificate for the domain
    Signs it with the corporate CA (deployed to all managed devices)
    Client validates against corporate CA → succeeds
    NGFW has these session keys too → can decrypt/inspect client requests

<span class="cm">/* What SSL inspection reveals */</span>
Full HTTP URL path (not just hostname)
All HTTP request/response headers
Request bodies (POST data, form submissions)
Response bodies (file downloads → malware scanning)
WebSocket data
gRPC payloads

<span class="cm">/* What SSL inspection breaks */</span>
Certificate pinning: apps that pin to specific certs (Twitter app, many banking apps)
HPKP (deprecated): HTTP Public Key Pinning
Client certificates (mTLS): NGFW must handle client cert forwarding
QUIC/HTTP3: QUIC encrypts more aggressively, harder to intercept

<span class="cm">/* NGFW SSL inspection bypass list (do NOT inspect) */</span>
Banking domains (privacy regulation)
Healthcare portals (HIPAA)
Legal/HR applications (attorney-client privilege)
Apps known to use certificate pinning
Internal PKI-protected services (use different trust chain)

<span class="cm">/* Implementing basic TLS termination in C with OpenSSL */</span>
SSL_CTX *server_ctx = SSL_CTX_new(TLS_server_method());
<span class="cm">/* Load your generated cert for the target domain */</span>
SSL_CTX_use_certificate(server_ctx, generated_cert);
SSL_CTX_use_PrivateKey(server_ctx, generated_key);

SSL_CTX *client_ctx = SSL_CTX_new(TLS_client_method());
<span class="cm">/* Connect to real server */</span>
SSL *client_ssl = SSL_new(client_ctx);
SSL_set_fd(client_ssl, server_socket_fd);
SSL_connect(client_ssl);
<span class="cm">/* Verify real server cert */</span>
X509 *real_cert = SSL_get_peer_certificate(client_ssl);
<span class="cm">/* Extract domain, generate matching cert for client, serve it */</span></pre></div>

    <div class="warn"><p>⚠️ <strong>ECH (Encrypted ClientHello)</strong> — in development for TLS 1.3 — will encrypt the SNI extension and other ClientHello fields, preventing NGFW from seeing the destination hostname without decrypting the entire TLS session. This fundamentally challenges SNI-based filtering and makes SSL inspection the only way to identify destinations. Watch RFC drafts for ECH deployment timeline.</p></div>
  </div>
</div>
</div>

<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>TLS 1.3 Handshake Dissection</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Capture and fully decode a TLS 1.3 handshake using Wireshark with TLS key logging.</p>
    <div class="lab-step"><div class="sn">1</div><div>Set up key logging: <code>export SSLKEYLOGFILE=/tmp/tls_keys.log</code>. Make a TLS 1.3 connection: <code>curl --tlsv1.3 -v https://cloudflare.com 2>&1 | head -40</code>. Capture simultaneously: <code>sudo tcpdump -i eth0 -w /tmp/tls.pcap host cloudflare.com</code>. Open pcap in Wireshark with key log configured.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>In Wireshark, examine the ClientHello: find and record — the supported_versions extension (should include 0x0304 = TLS 1.3), the key_share extension (X25519 public key bytes), the server_name extension (SNI), the signature_algorithms extension. Note that all these are in the clear.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Examine the ServerHello: verify TLS 1.3 is selected (version extension 0x0304), find the server's X25519 key share. After the ServerHello, all subsequent messages should show as "Encrypted Handshake Message" without the key log, but decryptable with the key log. Verify the Certificate record shows the real cert chain.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify the cipher suite negotiated (should be TLS_AES_256_GCM_SHA384 or TLS_AES_128_GCM_SHA256). Find the application data records — without key log they're opaque; with key log Wireshark shows the HTTP/2 frames inside. Count the total number of TLS records in the handshake and confirm the 1-RTT timing.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build a TLS Client and Server with OpenSSL</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement a TLS 1.3 echo server and client in C using OpenSSL. Extend with mTLS client authentication.</p>
    <div class="lab-step"><div class="sn">1</div><div>Generate test certificates: <code>openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-256 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"</code>. Write a minimal TLS server: socket → SSL_CTX_new(TLS_server_method()) → SSL_CTX_use_certificate/PrivateKey → accept loop → SSL_accept → SSL_read/write.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Force TLS 1.3 only: <code>SSL_CTX_set_min_proto_version(ctx, TLS1_3_VERSION)</code>. Verify with: <code>openssl s_client -connect localhost:8443 -tls1_3</code>. Confirm the cipher suite selected. Check the certificate presented: <code>openssl s_client -connect localhost:8443 2>/dev/null | openssl x509 -noout -text</code>.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Add mTLS: generate a client CA and client certificate. Configure the server to request a client cert (SSL_VERIFY_PEER). Test with: <code>openssl s_client -connect localhost:8443 -cert client.crt -key client.key</code>. Verify the server prints the client cert's CN. Try without a cert — verify the server rejects with "alert handshake failure".</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Enable session tickets and test resumption: after a successful connection, store the session: <code>SSL_get1_session(ssl)</code>. On the next connection, restore it: <code>SSL_set_session(ssl, session)</code>. Capture both connections in Wireshark and verify the second one is shorter (no Certificate/CertificateVerify).</div></div>
  </div>
</div>
</div>

<!-- TAB 9 -->
<div id="t9" class="tab-pane">
<p class="sep">M20 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know TLS provides: server auth (cert), optional client auth (mTLS), forward-secret key exchange, AEAD encryption</li>
  <li>Know TLS 1.3 handshake messages in order: ClientHello → ServerHello → {EncryptedExtensions, Certificate, CertificateVerify, Finished} → {Finished} → application data</li>
  <li>Know ClientHello key fields: client_random, supported_versions, key_share (X25519 pubkey), signature_algorithms, SNI, ALPN</li>
  <li>Know that TLS 1.3 takes 1 RTT (server sends cert + finished in same flight as ServerHello)</li>
  <li>Know TLS 1.3 key schedule: ECDHE shared secret + HKDF → handshake keys → master secret → application keys</li>
  <li>Know TLS record format: 5-byte header (content_type + version + length) + AEAD ciphertext + auth_tag</li>
  <li>Know TLS 1.3 nonce: write_iv XOR sequence_number (64-bit, prevents nonce reuse)</li>
  <li>Know the 5 TLS 1.3 cipher suites (all AEAD); know that key exchange and auth are negotiated separately</li>
  <li>Know what TLS 1.3 removed vs 1.2: static RSA, CBC, RC4, 3DES, compression, renegotiation, session IDs</li>
  <li>Know forward secrecy difference: TLS 1.3 always ECDHE (FS); TLS 1.2 could use static RSA (no FS)</li>
  <li>Know 0-RTT: PSK session ticket, early data sent with ClientHello, replay attack risk, only for idempotent requests</li>
  <li>Know 0-RTT does NOT have forward secrecy for early data</li>
  <li>Know mTLS: server sends CertificateRequest; client responds with Certificate + CertificateVerify; both sides authenticated</li>
  <li>Know mTLS use cases: service mesh, zero-trust, IoT device auth, API security</li>
  <li>Know SSL inspection architecture: NGFW as MITM; two separate TLS sessions; corporate CA signed cert for client</li>
  <li>Know what SSL inspection reveals: full URL, headers, request/response bodies, file downloads</li>
  <li>Know SSL inspection exclusions: banking, healthcare, apps with certificate pinning</li>
  <li>Know ECH (Encrypted ClientHello) as the upcoming challenge to SNI-based NGFW filtering</li>
  <li>Completed Lab 1: dissected TLS 1.3 handshake in Wireshark with key log; identified all extensions and messages</li>
  <li>Completed Lab 2: built TLS 1.3 server+client in C; implemented mTLS; verified session resumption</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M21 - IPsec and IKEv2</strong> — the VPN protocol stack used for site-to-site and remote access in enterprise networks, and the encryption layer for many NGFW deployments.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m19-cryptography/">← M19 Cryptography</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m21-ipsec/">Next: M21 - IPsec →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
