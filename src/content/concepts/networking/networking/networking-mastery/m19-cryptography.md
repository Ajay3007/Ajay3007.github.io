---
title: "M19 - Cryptography Foundations"
description: "NETWORKING MASTERY · PHASE 5 · MODULE 19 · WEEK 17 🔐 Cryptography Foundations Symmetric encryption · Asymmetric crypto · Hash functions · MACs · Key exchange · PKI · Random…"
domain: networking
track: networking-mastery
order: 19
url: /learning/networking-mastery/m19-cryptography/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a1a3a 40%,#3a1a5a 70%,#2a0a48 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#d0a0f8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#e8d0ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#f0e0ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#d0a0f8;border-bottom-color:#d0a0f8}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #6030a0}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#e0c8ff;white-space:pre}
.cm{color:#705890}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f4eeff;border:1.5px solid #6030a0;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1a0830;border-color:#8050c0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3a1070}[data-theme=dark] .ins strong{color:#d0a0f8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#3a1070;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#5020a0}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #6030a0;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#6030a0;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#6030a0;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#6030a0;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 5 · MODULE 19 · WEEK 17</div>
  <div class="mod-title">🔐 Cryptography Foundations</div>
  <div class="mod-subtitle">Symmetric encryption · Asymmetric crypto · Hash functions · MACs · Key exchange · PKI · Random numbers</div>
  <div class="mod-pills">
    <span class="mod-pill">Intermediate → Advanced</span>
    <span class="mod-pill">Prerequisite: M05 TCP</span>
    <span class="mod-pill">Essential for TLS and IPsec</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Why Crypto</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Symmetric Encryption</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Asymmetric Crypto</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Hash Functions and MACs</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Key Exchange</button>
  <button class="tab-btn" onclick="vt(event,'t5')">PKI and Certificates</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Algorithms Reference</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>

<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">THREE SECURITY PROPERTIES CRYPTOGRAPHY PROVIDES</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>Confidentiality, Integrity, and Authentication</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
    <p>Every cryptographic protocol in networking — TLS, IPsec, SSH, WireGuard — provides some combination of three fundamental properties. Understanding what each primitive provides (and what it doesn't) is how you reason about security protocols.</p>
    <ul>
      <li><strong>Confidentiality</strong> — only the intended recipient can read the data. Provided by encryption (AES, ChaCha20). Does NOT guarantee the data wasn't modified.</li>
      <li><strong>Integrity</strong> — the data was not modified in transit. Provided by MACs (HMAC-SHA256) or AEAD ciphers (AES-GCM). Does NOT tell you who sent it.</li>
      <li><strong>Authentication</strong> — you are communicating with who you think you are. Provided by digital signatures (RSA, ECDSA) + PKI. Does NOT keep data confidential.</li>
    </ul>
    <p>Most protocols combine all three: TLS uses asymmetric crypto for authentication + key exchange, then symmetric AEAD for confidentiality + integrity of the data stream. IPsec uses IKE for authentication + key exchange, then ESP for confidentiality + integrity.</p>
  </div>
</div>
</div>

<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">SYMMETRIC ENCRYPTION — FAST, SHARED-KEY CIPHERS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔑</span><h3>AES and ChaCha20 — Modern Symmetric Ciphers</h3><span class="tag tag-blue">SYMMETRIC</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Symmetric encryption: same key encrypts and decrypts */</span>
<span class="cm">/* Problem: how do two parties share the key securely? → Key Exchange (Tab 4) */</span>

<span class="cm">/* AES (Advanced Encryption Standard) */</span>
Block cipher: processes 128-bit (16-byte) blocks
Key sizes:    128, 192, or 256 bits (AES-128, AES-192, AES-256)
Structure:    10/12/14 rounds of SubBytes + ShiftRows + MixColumns + AddRoundKey
Hardware:     AES-NI CPU instructions (x86 since 2010) — ~1 cycle/byte on modern CPUs

<span class="cm">/* Block cipher modes — how to encrypt more than 16 bytes */</span>
ECB (Electronic Codebook):  Same plaintext → same ciphertext. NEVER USE.
CBC (Cipher Block Chaining): XOR with previous ciphertext block. Needs IV. Padding required.
CTR (Counter):              Turns AES into a stream cipher. Parallelisable. No padding.
GCM (Galois/Counter Mode):  CTR + GHASH authentication tag. AEAD. Standard for TLS 1.3.

<span class="cm">/* AEAD — Authenticated Encryption with Associated Data */</span>
<span class="cm">/* Single primitive providing both confidentiality AND integrity */</span>
AES-128-GCM:  AES-CTR encryption + GHASH-128 authentication tag (16 bytes)
AES-256-GCM:  Same with 256-bit key
ChaCha20-Poly1305: ChaCha20 stream cipher + Poly1305 MAC
              No AES-NI needed — fast on mobile/ARM/embedded

<span class="cm">/* AEAD inputs and outputs */</span>
Encrypt:
  Input:  key, nonce (12 bytes), plaintext, AAD (additional auth data)
  Output: ciphertext (same length as plaintext) + auth_tag (16 bytes)

Decrypt:
  Input:  key, nonce, ciphertext, auth_tag, AAD
  Output: plaintext (if tag verifies) OR reject (if tag fails)

<span class="cm">/* Critical: nonce MUST be unique per (key, message) */</span>
<span class="cm">/* Nonce reuse with AES-GCM → catastrophic key recovery possible */</span>
<span class="cm">/* TLS 1.3 uses XOR of static IV with sequence number as nonce */</span>

<span class="cm">/* OpenSSL AEAD in C */</span>
EVP_AEAD_CTX *ctx = EVP_AEAD_CTX_new(EVP_aead_aes_128_gcm(),
    key, 16, EVP_AEAD_DEFAULT_TAG_LENGTH);
EVP_AEAD_CTX_seal(ctx, ciphertext, &clen, max_out,
    nonce, 12, plaintext, plen, aad, aad_len);
EVP_AEAD_CTX_open(ctx, plaintext, &plen, max_out,
    nonce, 12, ciphertext, clen, aad, aad_len);</pre></div>
  </div>
</div>
</div>

<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">ASYMMETRIC CRYPTOGRAPHY — PUBLIC KEY SYSTEMS</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>RSA and Elliptic Curve Cryptography</h3><span class="tag tag-purple">ASYMMETRIC</span></div>
  <div class="cp-body">
    <p>Asymmetric (public-key) cryptography uses a mathematically linked key pair: the public key is freely distributed, the private key is secret. Operations with one key can only be verified/reversed with the other. This solves the key distribution problem — you can publish your public key to the world without compromising security.</p>
<div class="cb"><pre><span class="cm">/* RSA — Rivest-Shamir-Adleman */</span>
Based on: hardness of factoring large integers (n = p × q)
Key sizes: 2048 bits minimum (currently safe), 4096 for long-term
Use cases: digital signatures, key encapsulation (encrypting a small key)
NOT used for: bulk data encryption (too slow — 1000× slower than AES)
Performance: ~1ms per RSA-2048 sign, ~0.1ms verify on modern CPU

<span class="cm">/* RSA signature */</span>
Sign:   sig = m^d mod n    (private key d)
Verify: m   = sig^e mod n  (public key e)
<span class="cm">/* In practice: sign H(message) not message itself */</span>
<span class="cm">/* Padding: PKCS#1 v1.5 (legacy) or PSS (modern, recommended) */</span>

<span class="cm">/* Elliptic Curve Cryptography (ECC) */</span>
Based on:  hardness of ECDLP (Elliptic Curve Discrete Logarithm Problem)
Key sizes: 256-bit ECC ≈ 3072-bit RSA security
           384-bit ECC ≈ 7680-bit RSA security
Performance: 10-20× faster than equivalent RSA
Curves:
  P-256 (secp256r1/prime256v1): NIST standard, TLS/HTTPS default
  P-384 (secp384r1):             Higher security, government use
  X25519 (Curve25519):           Bernstein curve, fastest, used in TLS 1.3 + WireGuard
  Ed25519:                        EdDSA signatures — fast, no random nonce needed

<span class="cm">/* ECDSA — Elliptic Curve Digital Signature Algorithm */</span>
<span class="cm">/* Standard for TLS certificates (alongside RSA) */</span>
<span class="cm">/* WARNING: ECDSA requires a unique random nonce per signature */</span>
<span class="cm">/* Nonce reuse → private key recovery (PS3 hack, Bitcoin theft) */</span>
<span class="cm">/* Solution: use Ed25519 (EdDSA) which derives nonce deterministically */</span>

<span class="cm">/* Key generation with OpenSSL */</span>
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out ec_key.pem
openssl pkey -in ec_key.pem -pubout -out ec_pub.pem
openssl genpkey -algorithm Ed25519 -out ed_key.pem</pre></div>
  </div>
</div>
</div>

<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">HASH FUNCTIONS AND MACs — INTEGRITY PRIMITIVES</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>Cryptographic Hash Functions</h3><span class="tag tag-teal">HASH</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Cryptographic hash function properties */</span>
1. Deterministic:     same input → always same output
2. One-way:           given H(x), computationally infeasible to find x
3. Collision resistant: hard to find x≠y such that H(x) = H(y)
4. Avalanche effect:  one bit change in input → ~50% output bits change

<span class="cm">/* Hash algorithms — current recommendations */</span>
SHA-256:   256-bit output, 64 rounds. Standard for most uses.
SHA-384:   384-bit output, truncated SHA-512. Faster on 64-bit.
SHA-512:   512-bit output, 80 rounds. Higher collision resistance.
SHA-3:     Different construction (Keccak sponge). Backup if SHA-2 broken.
BLAKE3:    Modern, faster than SHA-256, used in WireGuard, Bao.

MD5, SHA-1: BROKEN — do not use for security. Still used for checksums.

<span class="cm">/* HMAC — Hash-based Message Authentication Code */</span>
HMAC-K(m) = H( (K ⊕ opad) || H( (K ⊕ ipad) || m ) )
<span class="cm">/* Provides: integrity + authentication (proves sender has key K) */</span>
<span class="cm">/* Does NOT provide: confidentiality */</span>

HMAC-SHA256: 256-bit authentication tag
HMAC-SHA384: 384-bit tag (used in IPsec/IKEv2 PRF)

<span class="cm">/* HKDF — HMAC-based Key Derivation Function (RFC 5869) */</span>
<span class="cm">/* Extract-then-Expand: derive multiple keys from one master secret */</span>

<span class="cm">/* Extract phase */</span>
prk = HMAC-SHA256(salt, ikm)    <span class="cm">/* input keying material → pseudorandom key */</span>

<span class="cm">/* Expand phase */</span>
OKM = T(1) || T(2) || ... where T(i) = HMAC-SHA256(prk, T(i-1) || info || i)

<span class="cm">/* TLS 1.3 uses HKDF to derive all session keys from the master secret */</span>
<span class="cm">/* IPsec uses PRF (usually HMAC-SHA256 or AES-XCBC) similarly */</span>

<span class="cm">/* OpenSSL hash in C */</span>
unsigned char digest[SHA256_DIGEST_LENGTH];
SHA256((unsigned char *)msg, msg_len, digest);

<span class="cm">/* HMAC in C */</span>
unsigned char hmac[32];
unsigned int hlen;
HMAC(EVP_sha256(), key, key_len, data, data_len, hmac, &hlen);</pre></div>
  </div>
</div>
</div>

<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">KEY EXCHANGE — SECURE SHARED SECRET OVER PUBLIC CHANNEL</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Diffie-Hellman and ECDH</h3><span class="tag tag-green">KEY EXCHANGE</span></div>
  <div class="cp-body">
    <p>Key exchange protocols allow two parties to derive the same shared secret over a completely public, observable channel — without ever transmitting the secret. This solves the fundamental problem of symmetric cryptography: how to agree on a key when you have no pre-shared secret.</p>
<div class="cb"><pre><span class="cm">/* Diffie-Hellman Key Exchange — conceptual */</span>
Public parameters: prime p, generator g (both public, known to attacker)

Alice chooses secret a, sends A = g^a mod p  (public)
Bob   chooses secret b, sends B = g^b mod p  (public)

Alice computes: S = B^a mod p = (g^b)^a mod p = g^(ab) mod p
Bob   computes: S = A^b mod p = (g^a)^b mod p = g^(ab) mod p

Both arrive at S = g^(ab) mod p without ever transmitting a or b.
Attacker sees: g, p, A, B — but computing a from A = g^a mod p is the
discrete logarithm problem — computationally infeasible for large p.

<span class="cm">/* ECDH — Elliptic Curve Diffie-Hellman */</span>
Same concept on elliptic curves. X25519 is the modern standard:
  - Curve25519 points, 255-bit coordinates
  - Used in TLS 1.3, WireGuard, Signal Protocol
  - 32-byte keys, ~100µs per key exchange on modern CPU
  - Immune to timing attacks (constant-time implementation)

<span class="cm">/* Forward Secrecy (Perfect Forward Secrecy) */</span>
Key property: even if long-term private key is compromised later,
past session keys cannot be recovered.

Achieved by: ephemeral key exchange (generate new DH keypair per session)
TLS 1.3: ECDHE (Ephemeral) — mandatory forward secrecy
TLS 1.2: may use static RSA key exchange — no forward secrecy!
          "RSA key exchange": client encrypts premaster secret with server cert public key
          If server private key leaked → all past recorded sessions decryptable.

<span class="cm">/* ECDH in OpenSSL C */</span>
EVP_PKEY_CTX *ctx = EVP_PKEY_CTX_new_id(EVP_PKEY_X25519, NULL);
EVP_PKEY_keygen_init(ctx);
EVP_PKEY *pkey = NULL;
EVP_PKEY_keygen(ctx, &pkey);   <span class="cm">/* generate ephemeral keypair */</span>

<span class="cm">/* After receiving peer's public key: */</span>
EVP_PKEY_CTX *dctx = EVP_PKEY_CTX_new(pkey, NULL);
EVP_PKEY_derive_init(dctx);
EVP_PKEY_derive_set_peer(dctx, peer_pubkey);
size_t slen;
EVP_PKEY_derive(dctx, shared_secret, &slen);  <span class="cm">/* 32-byte X25519 secret */</span></pre></div>
    <div class="ins"><p>💡 <strong>Forward secrecy is non-negotiable for modern security.</strong> Without it, an adversary who records encrypted traffic today and later compromises your server's private key can decrypt everything retroactively. This is why TLS 1.3 mandates ECDHE and removed static RSA key exchange. IPsec IKEv2 also uses ephemeral DH for the same reason.</p></div>
  </div>
</div>
</div>

<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">PKI — PUBLIC KEY INFRASTRUCTURE</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🏛️</span><h3>X.509 Certificates and the CA Trust Chain</h3><span class="tag tag-orange">PKI</span></div>
  <div class="cp-body">
    <p>A public key alone doesn't tell you who it belongs to. PKI binds a public key to an identity (domain name, organisation) via a digitally signed certificate. Trust is established through a chain of signatures from a trusted root CA.</p>
<div class="cb"><pre><span class="cm">/* X.509 certificate key fields */</span>
Version:          3 (current standard)
Serial Number:    unique per CA (used for revocation)
Issuer:           who signed this cert (CA name)
Subject:          who this cert is for ("CN=www.google.com, O=Google LLC")
Validity:         NotBefore and NotAfter (expiry)
Subject Public Key: the public key (RSA or EC) + algorithm
Extensions:
  Subject Alt Names (SAN): all domain names cert is valid for
  Key Usage:        what the key can do (digitalSignature, keyEncipherment)
  Extended Key Usage: TLS server auth, TLS client auth, code signing
  Basic Constraints: is this a CA cert? (isCA=true/false, path length)
Signature:        CA's signature over everything above

<span class="cm">/* Chain of trust */</span>
Root CA (self-signed, in browser/OS trust store)
  → Intermediate CA (signed by Root CA)
      → Leaf certificate (signed by Intermediate CA, has your domain)

<span class="cm">/* Certificate validation */</span>
1. Verify leaf cert signature using intermediate CA's public key
2. Verify intermediate CA signature using root CA's public key
3. Root CA is self-signed — trust must come from trust store
4. Check validity period (not expired)
5. Check Subject Alt Names — does CN/SAN match the domain?
6. Check revocation (CRL or OCSP)

<span class="cm">/* OpenSSL certificate inspection */</span>
openssl x509 -in cert.pem -text -noout   <span class="cm"># full cert details</span>
openssl x509 -in cert.pem -dates         <span class="cm"># validity period</span>
openssl s_client -connect google.com:443 -showcerts  <span class="cm"># live cert chain</span>
openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt cert.pem

<span class="cm">/* Certificate transparency (CT) */</span>
<span class="cm"># All public TLS certs must be logged to CT logs</span>
<span class="cm"># Browsers require SCT (Signed Certificate Timestamp) in TLS handshake</span>
<span class="cm"># Enables detection of mis-issued certs (NGFW relevance: detect rogue CAs)</span>

<span class="cm">/* OCSP Stapling */</span>
<span class="cm"># Server fetches OCSP response (revocation status) from CA</span>
<span class="cm"># Staples it to TLS handshake — client doesn't need to query CA separately</span>
<span class="cm"># NGFW: inspect OCSP status of presented certificates</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">ALGORITHM SELECTION REFERENCE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Current Best-Practice Algorithm Choices</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Purpose</th><th>Recommended (2024+)</th><th>Acceptable</th><th>Avoid</th></tr></thead>
      <tbody>
        <tr><td>Symmetric encryption</td><td>AES-256-GCM, ChaCha20-Poly1305</td><td>AES-128-GCM</td><td>AES-CBC, AES-ECB, 3DES, RC4</td></tr>
        <tr><td>Hash / digest</td><td>SHA-256, SHA-384, BLAKE3</td><td>SHA-512</td><td>MD5, SHA-1 (security), SHA-224</td></tr>
        <tr><td>MAC / HMAC</td><td>HMAC-SHA256, Poly1305</td><td>HMAC-SHA384</td><td>HMAC-MD5, HMAC-SHA1</td></tr>
        <tr><td>Key exchange</td><td>X25519, ECDH P-256</td><td>FFDHE-3072</td><td>Static RSA, DH-1024/2048, ECDH P-192</td></tr>
        <tr><td>Digital signatures</td><td>Ed25519, ECDSA P-256</td><td>RSA-PSS-2048</td><td>ECDSA with bad RNG, RSA-PKCS1-1.5, DSA</td></tr>
        <tr><td>Password hashing</td><td>Argon2id, bcrypt(cost≥12)</td><td>scrypt</td><td>SHA-256(password), MD5(password)</td></tr>
        <tr><td>Random numbers</td><td>getrandom(), /dev/urandom</td><td>CSPRNG from OpenSSL</td><td>rand(), srand(time()), /dev/random blocking</td></tr>
        <tr><td>Post-quantum (future)</td><td>CRYSTALS-Kyber (KEM), CRYSTALS-Dilithium (sig)</td><td>Hybrid classical+PQ</td><td>Pure classical for PQ-sensitive data</td></tr>
      </tbody>
    </table>

    <h4>Key Sizes — Security Level Reference</h4>
    <table class="t-table">
      <thead><tr><th>Security Level</th><th>Symmetric</th><th>RSA/DH</th><th>ECC</th><th>Good Until</th></tr></thead>
      <tbody>
        <tr><td>128-bit</td><td>AES-128</td><td>3072 bits</td><td>P-256 / X25519</td><td>2030+</td></tr>
        <tr><td>192-bit</td><td>AES-192</td><td>7680 bits</td><td>P-384</td><td>2040+</td></tr>
        <tr><td>256-bit</td><td>AES-256</td><td>15360 bits</td><td>P-521</td><td>2050+</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>

<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Hands-On Cryptographic Primitives with OpenSSL</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement and test each primitive: AEAD encrypt/decrypt, HMAC, HKDF, ECDH key exchange, and certificate parsing.</p>
    <div class="lab-step"><div class="sn">1</div><div>AEAD: Write a C program that AES-128-GCM encrypts a test message. Verify: (a) decryption recovers plaintext, (b) flipping one byte of ciphertext causes authentication failure, (c) changing the nonce causes failure. Document what "authentication tag" bytes look like in the output.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>HMAC: Compute HMAC-SHA256 of "Hello, World" with key "secret". Verify with: <code>echo -n "Hello, World" | openssl dgst -sha256 -hmac "secret"</code>. Then implement HKDF extract+expand in Python using the hmac module. Derive 3 separate 32-byte keys from one 32-byte master secret.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>ECDH: Generate two X25519 keypairs (Alice and Bob). Compute Alice's shared secret using Bob's public key and vice versa. Verify they produce the same 32 bytes. This is exactly what TLS 1.3 does during the handshake. Time the operation — how many key exchanges per second can your CPU do?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Certificate parsing: fetch a live TLS certificate: <code>openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -text -noout</code>. Identify: issuer, subject, SANs, key type and size, validity period, CT SCT extension. Verify the certificate chain: does github.com use RSA or EC? What intermediate CA signed it?</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build a Secure Channel from Primitives</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a minimal secure channel over a TCP socket using ECDH + HKDF + AES-GCM — demonstrating how TLS-like security can be constructed from primitives.</p>
    <div class="lab-step"><div class="sn">1</div><div>Client and server each generate an X25519 ephemeral keypair. Exchange public keys over the TCP connection (cleartext — this simulates the TLS ClientHello/ServerHello key share exchange). Compute the shared ECDH secret on both sides.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run HKDF over the ECDH shared secret (with a fixed salt and "our-protocol-v1" as the info string). Extract two 32-byte keys: one for client→server encryption, one for server→client encryption. This is the key schedule step.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Use AES-256-GCM with the derived keys to encrypt/decrypt messages. Use a 64-bit sequence number as the nonce (zero-padded to 12 bytes). Send 5 encrypted messages each direction. Verify: each message has a unique nonce, decryption succeeds, and a tampered ciphertext is rejected.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Identify what your channel is missing compared to real TLS: (a) server authentication — no certificate, MITM possible; (b) client authentication — no mutual TLS; (c) protocol negotiation — no cipher suite selection. Document what TLS adds on top of these primitives.</div></div>
  </div>
</div>
</div>

<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M19 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know the 3 cryptographic properties: confidentiality (encryption), integrity (MAC/AEAD), authentication (signatures + PKI)</li>
  <li>Know AES modes: ECB (broken), CBC (needs padding/IV), CTR (stream, parallelisable), GCM (AEAD — standard)</li>
  <li>Know AEAD inputs: key + nonce + plaintext + AAD → ciphertext + auth_tag</li>
  <li>Know why nonce must be unique: nonce reuse with AES-GCM → key recovery attack</li>
  <li>Know ChaCha20-Poly1305: AEAD alternative to AES-GCM, no AES-NI required, used in TLS 1.3 and WireGuard</li>
  <li>Know RSA: based on integer factoring; 2048+ bits; slow; used for signatures and key encapsulation, not bulk encryption</li>
  <li>Know ECC: based on ECDLP; 256-bit ECC ≈ 3072-bit RSA; 10-20× faster; standard curves: P-256, P-384, X25519, Ed25519</li>
  <li>Know ECDSA nonce reuse danger: same nonce twice → private key recovery (PS3, Bitcoin)</li>
  <li>Know Ed25519 advantage over ECDSA: deterministic nonce derivation — immune to bad RNG</li>
  <li>Know hash function properties: one-way, collision resistant, avalanche effect</li>
  <li>Know SHA-256 output size (256 bits) and current status (unbroken); know MD5/SHA-1 are broken</li>
  <li>Know HMAC: provides integrity + authentication (not confidentiality); HMAC-SHA256 = 256-bit tag</li>
  <li>Know HKDF: extract (IKM → PRK) then expand (PRK → multiple derived keys); used in TLS 1.3, IPsec</li>
  <li>Know Diffie-Hellman: shared secret from public values, g^(ab) mod p; DLP hardness</li>
  <li>Know X25519: modern ECDH curve; 32-byte keys; ~100µs per exchange; used in TLS 1.3 and WireGuard</li>
  <li>Know forward secrecy: ephemeral key exchange means past sessions safe even if long-term key compromised</li>
  <li>Know why TLS 1.3 removed static RSA key exchange: no forward secrecy</li>
  <li>Know X.509 certificate fields: Subject, Issuer, SAN, validity, key type, Basic Constraints, Key Usage</li>
  <li>Know certificate chain validation: leaf → intermediate → root; root must be in trust store</li>
  <li>Know OCSP stapling: server pre-fetches revocation proof, attaches to TLS handshake</li>
  <li>Know current best-practice choices: AES-256-GCM, SHA-256, HMAC-SHA256, X25519, Ed25519</li>
  <li>Completed Lab 1: implemented AES-GCM, HMAC, HKDF, ECDH; parsed live TLS certificate</li>
  <li>Completed Lab 2: built ECDH + HKDF + AES-GCM secure channel; identified what TLS adds</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M20 - TLS Internals</strong> — now that you understand the primitives, the TLS protocol will make complete sense as the composition of exactly these building blocks.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m18-vpp/">← M18 VPP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m20-tls/">Next: M20 - TLS →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
