---
title: "M22 - SSL Inspection and PKI Operations"
description: "NETWORKING MASTERY · PHASE 5 · MODULE 22 · WEEK 20 · PHASE 5 FINAL 🔍 SSL Inspection and PKI Operations TLS MITM architecture · Certificate generation · CA management · Bypass…"
domain: networking
track: networking-mastery
order: 22
url: /learning/networking-mastery/m22-ssl-inspection/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a0a28 40%,#3a0a1a 70%,#280010 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f080a0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ffc0d0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ffe0e8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f080a0;border-bottom-color:#f080a0}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #901030}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ffc0d0;white-space:pre}
.cm{color:#804050}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#fff0f4;border:1.5px solid #901030;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#280010;border-color:#b04060}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#600020}[data-theme=dark] .ins strong{color:#f080a0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#600020;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#901030}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #901030;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#901030;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#901030;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#901030;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
.phase-complete{background:linear-gradient(135deg,#280010,#700030);border-radius:10px;padding:1.4rem 1.6rem;margin:2rem 0;border:1.5px solid #a04060;color:#fff}
.phase-complete h3{margin:0 0 .5rem;font-size:1.1rem;font-weight:800;color:#fff;border:none}
.phase-complete p{margin:0;font-size:.88rem;line-height:1.65;color:#ffd0d8}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 5 · MODULE 22 · WEEK 20 · PHASE 5 FINAL</div>
  <div class="mod-title">🔍 SSL Inspection and PKI Operations</div>
  <div class="mod-subtitle">TLS MITM architecture · Certificate generation · CA management · Bypass policy · Certificate pinning · ECH</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M20 TLS</span>
    <span class="mod-pill">NGFW Core Capability</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">SSL Inspection Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">MITM Proxy Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Certificate Generation</button>
  <button class="tab-btn" onclick="vt(event,'t3')">CA Management</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Bypass Policy</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Certificate Pinning</button>
  <button class="tab-btn" onclick="vt(event,'t6')">ECH and Future Challenges</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>

<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">SSL INSPECTION — THE NGFW'S WINDOW INTO ENCRYPTED TRAFFIC</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Why SSL Inspection Is Essential for NGFW</h3><span class="tag tag-red">OVERVIEW</span></div>
  <div class="cp-body">
    <p>Over 95% of internet traffic is now HTTPS. Without SSL inspection, an NGFW is essentially blind to the majority of traffic — it can see destination IPs and SNI hostnames, but cannot inspect URLs, request/response content, or file transfers. Malware increasingly uses HTTPS for C2 communication precisely because simple firewalls cannot inspect it.</p>
    <p>SSL inspection (also called TLS inspection, SSL/TLS deep inspection, SSL bump) allows the NGFW to decrypt, inspect, and re-encrypt HTTPS traffic in real time. It is the single capability that separates a modern NGFW from a basic firewall.</p>
    <table class="t-table">
      <thead><tr><th>Without SSL Inspection</th><th>With SSL Inspection</th></tr></thead>
      <tbody>
        <tr><td>See: destination IP, SNI hostname</td><td>See: full URL, all headers, request/response body</td></tr>
        <tr><td>URL filtering: by hostname only</td><td>URL filtering: exact path and query string</td></tr>
        <tr><td>Malware scanning: impossible</td><td>Malware scanning: scan file downloads in real time</td></tr>
        <tr><td>DLP: impossible for HTTPS data</td><td>DLP: inspect POST bodies, detect sensitive data exfiltration</td></tr>
        <tr><td>App identification: by certificate only</td><td>App identification: by HTTP headers, content, API patterns</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>

<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">MITM PROXY ARCHITECTURE — HOW SSL INSPECTION WORKS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Full SSL Inspection Flow</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* SSL Inspection — two separate TLS sessions */</span>

STEP 1: Client initiates connection
  Client → NGFW: TCP SYN to server IP
  NGFW intercepts (transparent proxy mode — no client config needed)

STEP 2: NGFW connects to real server
  NGFW → Real Server: TCP connect, TLS ClientHello
  NGFW validates server certificate (chain, expiry, revocation)
  NGFW completes TLS handshake with real server
  NGFW now has session keys → can decrypt all server responses

STEP 3: NGFW generates certificate for client
  NGFW reads SNI from client's ClientHello (or from server cert)
  NGFW dynamically generates a certificate:
    Subject: CN=&lt;target domain&gt; (e.g., CN=accounts.google.com)
    SAN: original server's SAN list (preserved for correctness)
    Issuer: NGFW's internal CA certificate
    Validity: short (24–72 hours, not original cert lifetime)
    Key: new ephemeral key (never the real server's key)
  NGFW signs cert with its private CA key

STEP 4: NGFW completes TLS with client
  NGFW → Client: TLS ServerHello with generated certificate
  Client validates: checks chain → NGFW cert → NGFW CA → trust store
  Client trusts because NGFW CA was deployed to device trust store
  Client completes TLS handshake with NGFW

STEP 5: Inspection
  Every HTTP request from client → NGFW decrypts → inspects → forwards to server
  Every HTTP response from server → NGFW decrypts → inspects → forwards to client
  Inspection can: scan for malware, check URLs, apply DLP, log everything

<span class="cm">/* Transparency — is the client aware? */</span>
Technical: YES — the certificate presented is signed by NGFW CA, not real CA.
         The certificate serial/key differ from the real server's cert.
         A careful user or security-aware app CAN detect this.
User-visible: Usually NOT — URL bar still shows padlock, correct hostname.
Legal: Must inform users that inspection is occurring (employee policy, consent).

<span class="cm">/* Performance considerations */</span>
Each SSL inspection = 2× TLS sessions: NGFW-client + NGFW-server
CPU cost: 2× TLS handshakes per connection
Latency: +5-20ms per new connection (TLS handshake cost)
Session resumption: NGFW must manage its own session cache client-side
                    AND use session resumption server-side</pre></div>
  </div>
</div>
</div>

<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">CERTIFICATE GENERATION — CREATING CERTIFICATES ON THE FLY</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📜</span><h3>Dynamic Certificate Generation with OpenSSL</h3><span class="tag tag-teal">CERT GEN</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Dynamic certificate generation — runs for every new HTTPS connection */</span>

<span class="ck">int</span> generate_inspection_cert(
        const char *hostname,        <span class="cm">/* from SNI or server cert CN */</span>
        X509 *real_server_cert,      <span class="cm">/* for SAN list preservation */</span>
        X509 *ca_cert,               <span class="cm">/* NGFW CA certificate */</span>
        EVP_PKEY *ca_key,            <span class="cm">/* NGFW CA private key */</span>
        X509 **out_cert,
        EVP_PKEY **out_key)
{
    <span class="cm">/* 1. Generate ephemeral key (EC P-256 for speed) */</span>
    EVP_PKEY *pkey = EVP_EC_gen(<span class="cs">"P-256"</span>);

    <span class="cm">/* 2. Create certificate */</span>
    X509 *cert = X509_new();
    X509_set_version(cert, 2);      <span class="cm">/* version 3 */</span>
    
    <span class="cm">/* Random serial number (each cert needs unique serial) */</span>
    BIGNUM *serial = BN_new();
    BN_rand(serial, 64, 0, 0);
    BN_to_ASN1_INTEGER(serial, X509_get_serialNumber(cert));
    
    <span class="cm">/* Short validity — 24 hours */</span>
    X509_gmtime_adj(X509_getm_notBefore(cert), 0);
    X509_gmtime_adj(X509_getm_notAfter(cert), 86400);
    
    <span class="cm">/* Subject: CN = hostname */</span>
    X509_NAME *name = X509_NAME_new();
    X509_NAME_add_entry_by_txt(name, <span class="cs">"CN"</span>, MBSTRING_ASC,
        (unsigned char *)hostname, -1, -1, 0);
    X509_set_subject_name(cert, name);
    
    <span class="cm">/* Issuer: our CA */</span>
    X509_set_issuer_name(cert, X509_get_subject_name(ca_cert));
    
    <span class="cm">/* Subject Alt Names — copy from real server cert */</span>
    copy_san_extension(cert, real_server_cert);
    
    <span class="cm">/* Key usage */</span>
    add_key_usage(cert, KU_DIGITAL_SIGNATURE | KU_KEY_ENCIPHERMENT);
    add_ext_key_usage(cert, NID_server_auth);
    
    <span class="cm">/* Attach public key */</span>
    X509_set_pubkey(cert, pkey);
    
    <span class="cm">/* Sign with CA key */</span>
    X509_sign(cert, ca_key, EVP_sha256());
    
    *out_cert = cert;
    *out_key  = pkey;
    return 0;
}

<span class="cm">/* Performance optimisation: certificate caching */</span>
<span class="cm">/* Generating a new cert takes ~1ms (EC key gen + sign) */</span>
<span class="cm">/* Cache by hostname: hash(SNI) → (cert, key) */</span>
<span class="cm">/* Cache lifetime: 1 hour (shorter than real cert validity) */</span>
<span class="cm">/* Cache size: 10,000 entries covers most enterprise browsing patterns */</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">CA MANAGEMENT — BUILDING AND OPERATING AN INSPECTION CA</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏛️</span><h3>NGFW CA Lifecycle and Deployment</h3><span class="tag tag-purple">CA MANAGEMENT</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Creating the NGFW inspection CA */</span>

<span class="cm"># Generate 4096-bit RSA CA key (CA key compromise = all inspection certs compromised)</span>
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out ngfw-ca.key

<span class="cm"># Create self-signed CA certificate (10 year validity)</span>
openssl req -new -x509 -key ngfw-ca.key -out ngfw-ca.crt -days 3650 \
  -subj "/C=IN/O=Jio Platforms/OU=Network Security/CN=Jio NGFW Inspection CA" \
  -extensions v3_ca

<span class="cm"># Verify CA cert</span>
openssl x509 -in ngfw-ca.crt -text -noout | grep -A5 "Basic Constraints"
<span class="cm"># Must show: CA:TRUE</span>

<span class="cm">/* Security hardening of CA key */</span>
<span class="cm"># Store CA private key in HSM (Hardware Security Module) if possible</span>
<span class="cm"># If software: encrypt with strong passphrase, restrict file permissions</span>
chmod 400 ngfw-ca.key
<span class="cm"># Or use PKCS#11 engine to access HSM from OpenSSL:</span>
<span class="cm"># openssl engine pkcs11 -pre MODULE_PATH:/usr/lib/softhsm/libsofthsm2.so</span>

<span class="cm">/* CA distribution — push to all managed endpoints */</span>

Windows (Group Policy):
  Computer Configuration → Policies → Windows Settings → Public Key Policies
  → Trusted Root Certification Authorities → Import ngfw-ca.crt

Linux (system-wide):
  sudo cp ngfw-ca.crt /usr/local/share/ca-certificates/ngfw-ca.crt
  sudo update-ca-certificates

macOS (MDM):
  Deploy via MDM profile → Certificate payload → Always Trust

Android/iOS (MDM):
  Deploy via MDM → Certificate profile → Install as trusted CA

<span class="cm">/* CA rotation — periodic key replacement */</span>
<span class="cm"># CA key should be rotated every 2-3 years</span>
<span class="cm"># Process: generate new CA key → deploy new CA cert → phase out old</span>
<span class="cm"># Overlap period: both CAs active simultaneously during rollout</span>
<span class="cm"># Use sub-CA: root CA signs a sub-CA cert used for signing; rotate sub-CA annually</span>

<span class="cm">/* Sub-CA architecture (recommended for enterprise) */</span>
Offline Root CA (air-gapped, 4096-bit RSA, 20-year cert)
  └── Online Sub-CA (HSM-backed, ECDSA P-384, 5-year cert)
        └── NGFW dynamically signs per-hostname certs</pre></div>
  </div>
</div>
</div>

<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">BYPASS POLICY — WHEN NOT TO INSPECT</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🚦</span><h3>SSL Inspection Bypass Categories and Rules</h3><span class="tag tag-amber">BYPASS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Category</th><th>Why Bypass</th><th>How to Identify</th><th>Risk of Inspecting</th></tr></thead>
      <tbody>
        <tr><td>Banking and finance</td><td>Privacy regulations (GDPR, RBI guidelines); credentials in transit</td><td>URL category: financial; TLD: .bank</td><td>Legal liability; user trust erosion</td></tr>
        <tr><td>Healthcare portals</td><td>Protected health information (PHI); HIPAA equivalent</td><td>URL category: health; hospital domains</td><td>Regulatory violation</td></tr>
        <tr><td>HR and payroll</td><td>Employee personal data; company confidentiality</td><td>URL category: HR; known HR SaaS domains</td><td>Privacy regulations</td></tr>
        <tr><td>Personal email</td><td>Employee personal communications; legal considerations</td><td>URL: gmail.com, outlook.com personal access</td><td>Privacy expectations</td></tr>
        <tr><td>Certificate-pinned apps</td><td>App will fail — cannot accept NGFW CA cert</td><td>Known list: Twitter app, many banking apps, Signal</td><td>App breakage</td></tr>
        <tr><td>Internal PKI services</td><td>Use private CA already trusted; NGFW CA not in chain</td><td>Internal domains, RFC 1918 destinations</td><td>Certificate chain errors</td></tr>
        <tr><td>Update servers</td><td>Signed packages — inspection adds latency; code signing</td><td>URL: windowsupdate.com, apt.canonical.com</td><td>Update failures possible</td></tr>
        <tr><td>Legal counsel / IR tools</td><td>Attorney-client privilege</td><td>Known legal SaaS, law firm domains</td><td>Privileged communication exposure</td></tr>
      </tbody>
    </table>

<div class="cb"><pre><span class="cm">/* Bypass decision flowchart in NGFW */</span>
For each new TLS connection:

1. Is destination in bypass-by-IP list? → BYPASS
2. Is destination in bypass-by-domain list? → BYPASS
3. Is URL category in bypass-category list? → BYPASS
4. Does server cert have a CT SCT? (all trusted certs should) → if missing: BLOCK
5. Is server cert EV (Extended Validation)? → optional bypass
6. Does server cert use domain-validated DV from known CA? → INSPECT
7. Is client in inspection-exempt group? → BYPASS
8. Default: INSPECT

<span class="cm">/* Squeezing more visibility without full inspection */</span>
<span class="cm">/* Even without decryption, TLS metadata reveals a lot: */</span>

JA3/JA3S fingerprint:
  Hash of TLS ClientHello parameters (cipher suites, extensions, curves)
  Identifies the TLS client library (Chrome, Firefox, curl, Python, malware)
  Malware often has distinctive JA3 hashes
  JA3 = MD5(SSLVersion, Ciphers, Extensions, EllipticCurves, EllipticCurveFormats)

Certificate analysis:
  Self-signed cert for common domains → likely malware C2
  Cert issued <1 hour ago → suspicious (malware uses short-lived Let's Encrypt certs)
  Cert from unknown CA → block or alert

QUIC/HTTP3 detection:
  Alt-Svc header in HTTP response suggests QUIC support
  NGFW must block UDP 443 to force HTTP/2 (for inspection)
  Or deploy QUIC-capable inspection proxy</pre></div>
  </div>
</div>
</div>

<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">CERTIFICATE PINNING — THE INSPECTION ADVERSARY</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">📌</span><h3>How Certificate Pinning Works and Breaks Inspection</h3><span class="tag tag-red">PINNING</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Certificate pinning */</span>
App embeds expected certificate or public key directly in its binary.
On each TLS connection: compares server cert to pinned value.
If mismatch → connection refused (even if chain validates correctly).

Types:
  Leaf pinning:   pin the exact leaf certificate
  Public key pin: pin the subject public key (survives cert renewal)
  CA pin:         pin a specific CA — accepts any cert from that CA only
  SPKI pin:       Subject Public Key Info hash (RFC 7469 HPKP — now deprecated)

Result with SSL inspection:
  NGFW presents forged cert signed by NGFW CA, with different key.
  Pinned app: "Expected key X, got key Y" → TLS abort.
  App logs: "Certificate validation failed" / "SSL error" / silent failure.

<span class="cm">/* Detection: how to identify pinned apps */</span>
<span class="cm"># Symptom: app works without SSL inspection, fails with inspection</span>
<span class="cm"># Test: enable inspection → app fails; disable → app works</span>
<span class="cm"># Tool: mitmproxy bypass detection log</span>
<span class="cm"># Android: frida-based SSLUnpinning script (for testing/research)</span>

<span class="cm">/* NGFW handling strategies */</span>

Option 1: Bypass list (most practical)
  Add known-pinning apps/domains to bypass list.
  Risk: bypass allows uninspected traffic.
  Examples: Twitter app, Facebook app, many banking apps, Signal, WhatsApp.

Option 2: MDM enforcement
  Deploy MDM policy that disables cert pinning override.
  Only works for MDM-managed devices — not personal devices.

Option 3: Application block
  If app uses pinning and you can't inspect it → block the app entirely.
  Heavy-handed but used for high-security environments.

Option 4: Zero-trust network access (ZTNA)
  Replace SSL inspection with ZTNA agent on endpoint.
  Agent inspects traffic before it leaves the device (no MITM needed).
  Increasingly the modern alternative to network-based SSL inspection.

<span class="cm">/* Known apps using certificate pinning (partial list) */</span>
Strong pinning: WhatsApp, Signal, most banking apps, Twitter native app
Partial pinning: Chrome (HSTS preload), Firefox (for mozilla.org)
Historical: Google Chrome (Chrome pins Symantec certs — removed 2018)</pre></div>
  </div>
</div>
</div>

<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">ECH AND FUTURE CHALLENGES TO SSL INSPECTION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔮</span><h3>Encrypted ClientHello — The Coming Inspection Challenge</h3><span class="tag tag-purple">ECH</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Current TLS: SNI is cleartext */</span>
ClientHello contains:
  server_name (SNI) extension: "accounts.google.com"  ← VISIBLE TO NGFW

This allows:
  - NGFW URL filtering by hostname
  - ISP traffic monitoring
  - Country-level censorship
  - Passive TLS fingerprinting

<span class="cm">/* ECH — Encrypted ClientHello (TLS 1.3 extension, draft RFC) */</span>
New model:
  Outer ClientHello: SNI = "cloudflare.com" (the CDN/front)  ← visible
  Inner ClientHello: SNI = "accounts.google.com"              ← ENCRYPTED

How:
  Server publishes an ECH public key in DNS (HTTPS record type 65)
  Client fetches ECH key via DoH (bypassing ISP DNS)
  Client encrypts inner ClientHello with ECH public key
  Only the target server (with ECH private key) can decrypt inner ClientHello

<span class="cm">/* ECH impact on NGFW */</span>
Without SSL inspection: NGFW sees only outer SNI (CDN domain, not real destination)
                        URL filtering by hostname becomes impossible for ECH sites
                        Malware can hide its C2 domain behind Cloudflare/CDN with ECH

With SSL inspection: NGFW terminates TLS before ECH → can still decrypt everything
                     But NGFW must now connect to CDN as outer client,
                     then somehow route to real backend — complex for transparent proxy

<span class="cm">/* Current status (2025) */</span>
ECH is in RFC draft stage (draft-ietf-tls-esni)
Cloudflare, Fastly deploying ECH for their customers
Firefox and Chrome have ECH support behind flags or partial rollout
Major browser adoption + CDN deployment = ECH becomes common by 2026-2027

<span class="cm">/* NGFW strategic responses to ECH */</span>
1. DNS-based filtering:
   Block DNS HTTPS records (type 65) → ECH key not available → fallback to plain SNI
   Risk: browsers may treat as network error and retry with DoH

2. TLS fingerprint-based detection:
   JA4+ fingerprints identify TLS libraries even without SNI
   Combine with IP reputation, QUIC fingerprinting

3. Endpoint-based inspection (ZTNA agent):
   Agent on endpoint can inspect before encryption
   Avoids the network MITM problem entirely

4. DNS-over-HTTPS interception:
   Intercept all DoH queries (force internal resolver)
   Prevents ECH key retrieval for controlled environments

<span class="cm">/* Takeaway for NGFW engineers */</span>
<span class="cm"># The long-term trend is toward more encryption, not less</span>
<span class="cm"># ECH + QUIC + DoH create a world where network-based inspection weakens</span>
<span class="cm"># Future NGFW: endpoint agent + cloud policy + AI-based behavioural detection</span>
<span class="cm"># Network inspection remains viable for on-premise managed environments</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Build a Working SSL Inspection Proxy</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a working TLS MITM proxy using mitmproxy and your own CA. Observe inspection capabilities and test bypass scenarios.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install mitmproxy: <code>pip install mitmproxy</code>. Run in transparent mode: <code>mitmproxy --mode transparent --showhost</code>. Configure iptables to redirect traffic: <code>iptables -t nat -A OUTPUT -p tcp --dport 443 -j REDIRECT --to-port 8080</code>. Browse to HTTPS sites and observe mitmproxy decrypting all traffic.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Install mitmproxy's CA certificate: it auto-generates at <code>~/.mitmproxy/mitmproxy-ca.pem</code>. Import to your browser: Settings → Certificates → Import. Verify HTTPS sites now show the mitmproxy CA in the certificate chain instead of the real CA. Find a site and compare the real cert vs the generated cert.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test certificate pinning: try accessing an app or site that uses pinning (Twitter's web app, some banking sites). Observe the error. Document which applications fail. Use curl as a test: <code>curl --proxy http://127.0.0.1:8080 https://github.com</code> (should work) vs <code>curl --pinnedpubkey sha256//... https://github.com</code> (should fail if key changes).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Write a mitmproxy addon (Python script) that: logs the full URL, request headers, and response status for every request, saves POST body content to a file (DLP simulation), and blocks any response body containing the string "password" (test with a custom HTTP server). This demonstrates what real NGFW SSL inspection engines do.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Enterprise CA Setup and Certificate Management</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a two-tier CA hierarchy (root CA + sub-CA) using OpenSSL. Generate inspection certificates dynamically and verify the chain.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create an offline root CA: generate a 4096-bit RSA key, create a self-signed certificate with CA:TRUE and pathlen:1 (allows one sub-CA). Mark this as the root — in production it would be kept offline. <code>openssl req -x509 -newkey rsa:4096 -keyout root-ca.key -out root-ca.crt -days 7300 -nodes -extensions v3_ca -subj "/CN=Test Root CA"</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Create the NGFW sub-CA: generate an EC P-384 key, create a CSR, sign it with the root CA. The sub-CA gets: CA:TRUE, pathlen:0 (no further sub-CAs), shorter validity (5 years). This is what the NGFW uses for daily signing operations.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write a Python script that generates an inspection certificate for a given hostname in under 1ms (target). The cert must: copy SANs from the real server cert (fetch real cert with socket+ssl), use the sub-CA for signing, cache results by hostname. Benchmark: time 1000 certificate generations.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify the chain: <code>openssl verify -CAfile root-ca.crt -untrusted sub-ca.crt generated-cert.crt</code>. Should show "OK". Also verify with a browser: import root-ca.crt as trusted root, then use nginx with the generated cert. Browser should show a padlock with the custom CA chain.</div></div>
  </div>
</div>
</div>

<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M22 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know why SSL inspection is essential: 95%+ traffic is HTTPS; without it NGFW is blind to URLs, content, malware in downloads</li>
  <li>Know SSL inspection reveals vs not: reveals full URL/headers/body; does NOT reveal source code or keys of real server</li>
  <li>Know the MITM proxy architecture: two separate TLS sessions (NGFW↔client and NGFW↔server)</li>
  <li>Know the 5-step inspection flow: intercept → connect to real server → validate real cert → generate forged cert → serve to client → inspect bidirectionally</li>
  <li>Know why clients trust forged certs: corporate CA is pre-deployed to managed device trust stores</li>
  <li>Know what generated certs must contain: hostname in CN/SAN, CA:FALSE, short validity, copied SAN list, signed by NGFW sub-CA</li>
  <li>Know certificate caching: generate once per hostname, cache 1 hour — ~1ms/cert without cache, sub-µs with cache</li>
  <li>Know two-tier CA hierarchy: offline root CA + online NGFW sub-CA (root CA signs sub-CA; sub-CA signs inspection certs)</li>
  <li>Know CA distribution methods: Windows GPO, Linux update-ca-certificates, MDM for mobile</li>
  <li>Know SSL inspection bypass categories: banking, healthcare, HR/payroll, personal email, cert-pinned apps, internal PKI, update servers</li>
  <li>Know TLS metadata visible without decryption: SNI, JA3/JA3S fingerprint, certificate subject/issuer, cipher suites, ALPN</li>
  <li>Know JA3: hash of TLS ClientHello parameters; identifies TLS client library; malware has distinctive JA3</li>
  <li>Know certificate pinning: app embeds expected cert/key; NGFW forged cert → mismatch → connection refused</li>
  <li>Know three pinning types: leaf cert pin, public key pin, CA pin</li>
  <li>Know NGFW strategies for pinning: bypass list (practical), MDM disable, block app, ZTNA agent</li>
  <li>Know ECH (Encrypted ClientHello): encrypts SNI in ClientHello; only CDN/server can decrypt; blinds NGFW to real destination</li>
  <li>Know ECH NGFW responses: block DNS HTTPS records, TLS fingerprinting, ZTNA endpoint agent, DoH interception</li>
  <li>Completed Lab 1: ran mitmproxy SSL inspection proxy; tested cert pinning failure; wrote DLP addon</li>
  <li>Completed Lab 2: built two-tier CA hierarchy; generated inspection certs programmatically; benchmarked cert generation</li>
</ul>

<div class="phase-complete">
  <h3>🎉 Phase 5 Complete — Security Protocols</h3>
  <p>You have completed all 4 modules of Phase 5: Cryptography Foundations (M19), TLS Internals (M20), IPsec and IKEv2 (M21), and SSL Inspection and PKI Operations (M22). You now have a thorough understanding of the cryptographic protocols underpinning modern network security — the same protocols your NGFW must implement, inspect, and in some cases circumvent. Move to <strong>Phase 6 — NGFW Development</strong>, the capstone phase.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m21-ipsec/">← M21 IPsec</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m23-conntrack-nat/">Next: M23 - Conntrack and NAT →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
