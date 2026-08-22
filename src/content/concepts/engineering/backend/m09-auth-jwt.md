---
title: "M09 — Authentication & Authorization"
description: "M09 — Authentication Authorization Phase 3 · Auth Authz · Sessions · JWT · OAuth2 · RBAC · Argon2 Phase 3 Requires M03 (REST) C / OpenSSL / libsodium Overview Sessions Cookies…"
domain: engineering
track: backend
order: 9
ownHeader: true
url: /learning/backend/m09-auth-jwt/
---

<style>
/* ── Base ── */
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:#f7fafc;color:#1a202c}
a{color:#ef4444;text-decoration:none}
a:hover{text-decoration:underline}
code{font-family:'Cascadia Code','Fira Code',monospace;font-size:.85em;
     background:#f1f5f9;padding:1px 5px;border-radius:3px;color:#be123c}

/* ── Module header ── */
.mod-header{background:linear-gradient(135deg,#1a1f36 0%,#2d1b3d 100%);
  color:#fff;padding:2.5rem 2rem 2rem;border-radius:12px;margin-bottom:1.5rem;
  border-left:5px solid #ef4444}
.mod-header h1{font-size:1.9rem;margin-bottom:.4rem}
.mod-header .sub{color:#fca5a5;font-size:1rem;margin-bottom:1rem}
.badges{display:flex;flex-wrap:wrap;gap:.5rem}
.badge{padding:.25rem .75rem;border-radius:20px;font-size:.75rem;font-weight:600}
.b-phase{background:rgba(239,68,68,.25);color:#fca5a5;border:1px solid rgba(239,68,68,.4)}
.b-prereq{background:rgba(249,115,22,.2);color:#fdba74;border:1px solid rgba(249,115,22,.35)}
.b-lang{background:rgba(148,163,184,.15);color:#cbd5e1;border:1px solid rgba(148,163,184,.25)}

/* ── Tabs ── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.5rem}
.tab-btn{padding:.5rem 1.1rem;border:none;border-radius:8px;cursor:pointer;
  font-size:.85rem;font-weight:600;background:#e2e8f0;color:#475569;transition:.2s}
.tab-btn:hover{background:#fecaca;color:#991b1b}
.tab-btn.active{background:linear-gradient(135deg,#ef4444,#f97316);color:#fff}
.tab-pane{display:none}.tab-pane.active{display:block}

/* ── Content panels ── */
.cp{border-radius:10px;margin-bottom:1.2rem;overflow:hidden}
.cp-hdr{padding:.75rem 1rem;font-weight:700;font-size:.9rem;letter-spacing:.03em}
.cp-body{padding:1rem 1.2rem;font-size:.9rem;line-height:1.7}
.p-red .cp-hdr{background:#fef2f2;color:#991b1b;border-left:4px solid #ef4444}
.p-red .cp-body{background:#fff5f5;border-left:4px solid #fecaca}
.p-orange .cp-hdr{background:#fff7ed;color:#9a3412;border-left:4px solid #f97316}
.p-orange .cp-body{background:#fffbf5;border-left:4px solid #fed7aa}
.p-amber .cp-hdr{background:#fffbeb;color:#92400e;border-left:4px solid #f59e0b}
.p-amber .cp-body{background:#fefce8;border-left:4px solid #fde68a}
.p-blue .cp-hdr{background:#eff6ff;color:#1e40af;border-left:4px solid #3b82f6}
.p-blue .cp-body{background:#f8faff;border-left:4px solid #bfdbfe}
.p-teal .cp-hdr{background:#f0fdfa;color:#115e59;border-left:4px solid #14b8a6}
.p-teal .cp-body{background:#f7fffe;border-left:4px solid #99f6e4}
.p-violet .cp-hdr{background:#f5f3ff;color:#5b21b6;border-left:4px solid #8b5cf6}
.p-violet .cp-body{background:#faf9ff;border-left:4px solid #ddd6fe}
.p-green .cp-hdr{background:#f0fdf4;color:#14532d;border-left:4px solid #22c55e}
.p-green .cp-body{background:#f7fef9;border-left:4px solid #bbf7d0}
.p-indigo .cp-hdr{background:#eef2ff;color:#312e81;border-left:4px solid #6366f1}
.p-indigo .cp-body{background:#f8f9ff;border-left:4px solid #c7d2fe}

/* ── Callouts ── */
.ins,.warn,.note,.analogy{padding:.75rem 1rem;border-radius:8px;
  margin:.8rem 0;font-size:.88rem;line-height:1.6}
.ins{background:#fef2f2;border-left:4px solid #ef4444;color:#7f1d1d}
.warn{background:#fffbeb;border-left:4px solid #f59e0b;color:#78350f}
.note{background:#eff6ff;border-left:4px solid #3b82f6;color:#1e3a5f}
.analogy{background:#f5f3ff;border-left:4px solid #8b5cf6;color:#3b0764}

/* ── Code blocks ── */
.cb{background:#0f172a;border-radius:8px;padding:1.2rem;margin:.8rem 0;
  overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.82rem;line-height:1.65}
.cm{color:#64748b}   /* comment  */
.ck{color:#f472b6}   /* keyword  */
.cv{color:#86efac}   /* variable */
.cs{color:#fbbf24}   /* string   */
.cn{color:#67e8f9}   /* number/type */
.cf{color:#a5b4fc}   /* function */

/* ── Flow list ── */
.flow-list{list-style:none;padding:0}
.flow-list li{display:flex;align-items:flex-start;gap:.75rem;padding:.6rem 0;
  border-bottom:1px solid #f1f5f9;font-size:.9rem}
.flow-list li:last-child{border-bottom:none}
.fl-step{background:linear-gradient(135deg,#ef4444,#f97316);color:#fff;
  min-width:28px;height:28px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;font-weight:700;font-size:.8rem;flex-shrink:0}

/* ── Tables ── */
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#1a1f36;color:#f8fafc;padding:.6rem .9rem;text-align:left;font-size:.8rem}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#fef2f2}
.good{color:#15803d;font-weight:600}
.bad{color:#dc2626;font-weight:600}
.ok{color:#d97706;font-weight:600}

/* ── Two-col ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:680px){.two-col{grid-template-columns:1fr}}

/* ── Lab box ── */
.lab-box{background:#fff;border:1px solid #fecaca;border-radius:10px;
  margin-bottom:1.2rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#ef4444,#f97316);color:#fff;
  padding:.7rem 1rem;font-weight:700;font-size:.9rem}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.7}
.lab-step{display:flex;gap:.7rem;margin:.4rem 0;align-items:flex-start}
.sn{background:#ef4444;color:#fff;min-width:22px;height:22px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-size:.72rem;
  font-weight:700;flex-shrink:0;margin-top:.15rem}

/* ── Checklist ── */
.cl{list-style:none;padding:0}
.cl li{padding:.45rem .6rem;margin:.3rem 0;border-radius:6px;font-size:.88rem;
  background:#fff;border:1px solid #e2e8f0;display:flex;align-items:flex-start;gap:.5rem}
.cl li::before{content:"☐";color:#ef4444;font-size:1rem;flex-shrink:0}

/* ── Separator ── */
.sep{border:none;border-top:1px solid #e2e8f0;margin:1.2rem 0}

/* ── Navigation ── */
.mod-nav{display:flex;justify-content:space-between;align-items:center;
  margin-top:2rem;padding-top:1rem;border-top:2px solid #e2e8f0;flex-wrap:wrap;gap:.5rem}
.nb{display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.1rem;
  border-radius:8px;font-size:.85rem;font-weight:600;transition:.2s;
  background:#f1f5f9;color:#475569;border:1px solid #e2e8f0}
.nb:hover{background:linear-gradient(135deg,#ef4444,#f97316);color:#fff;
  border-color:transparent;text-decoration:none}

/* ── Security callout ── */
.sec-box{background:#fef2f2;border:1px solid #fecaca;border-left:4px solid #ef4444;
  border-radius:8px;padding:.9rem 1rem;margin:.8rem 0;font-size:.87rem}
.sec-box strong{color:#991b1b;display:block;margin-bottom:.3rem}

/* ── Sequence diagram ── */
.seq{background:#0f172a;border-radius:8px;padding:1.2rem;margin:.8rem 0;
  font-family:'Cascadia Code','Fira Code',monospace;font-size:.8rem;
  color:#e2e8f0;line-height:1.8;overflow-x:auto}
.seq .actor{color:#f472b6;font-weight:700}
.seq .msg{color:#86efac}
.seq .note{color:#fbbf24;background:transparent;border:none;padding:0}
</style>

<div class="mod-header">
  <h1>M09 — Authentication &amp; Authorization</h1>
  <div class="sub">Phase 3 · Auth &amp; Authz · Sessions · JWT · OAuth2 · RBAC · Argon2</div>
  <div class="badges">
    <span class="badge b-phase">Phase 3</span>
    <span class="badge b-prereq">Requires M03 (REST)</span>
    <span class="badge b-lang">C / OpenSSL / libsodium</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('sessions',this)">Sessions &amp; Cookies</button>
  <button class="tab-btn" onclick="vt('jwt',this)">JWT Deep Dive</button>
  <button class="tab-btn" onclick="vt('oauth',this)">OAuth2 &amp; API Keys</button>
  <button class="tab-btn" onclick="vt('authz',this)">Authorization</button>
  <button class="tab-btn" onclick="vt('passwords',this)">Password Security</button>
  <button class="tab-btn" onclick="vt('impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('labs',this)">Labs</button>
  <button class="tab-btn" onclick="vt('checklist',this)">Checklist</button>
</div>

<!-- ═══════════════════════ OVERVIEW ═══════════════════════ -->
<div class="tab-pane active" id="tab-overview">

<div class="cp p-red">
  <div class="cp-hdr">What this module covers</div>
  <div class="cp-body">
    Authentication (AuthN) answers <em>"Who are you?"</em>; Authorization (AuthZ) answers <em>"What are you allowed to do?"</em>
    Both are security-critical and surprisingly nuanced. This module builds from first principles — cookies and sessions —
    through stateless JWT tokens, to OAuth2 delegation, RBAC/ABAC access control, and cryptographically-correct password storage.
    All code examples use <strong>C with OpenSSL</strong> and <strong>libsodium</strong>.
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">Why get this right</div>
  <div class="cp-body">
    <ul style="padding-left:1.2rem;line-height:1.9">
      <li>Broken authentication is #1 on OWASP's list of critical web security risks</li>
      <li>A single mistake — MD5 passwords, weak JWT secret, missing <code>HttpOnly</code> flag — can expose every user account</li>
      <li>Auth bugs are often invisible: the system <em>works</em> but is trivially bypassable</li>
      <li>Security-in-depth requires both correct concepts and correct implementation</li>
    </ul>
  </div>
</div>

<hr class="sep">

<div class="cp p-blue">
  <div class="cp-hdr">The authentication landscape</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Mechanism</th><th>State</th><th>Best for</th><th>Main risk</th></tr></thead>
      <tbody>
        <tr><td><strong>Session cookies</strong></td><td>Server-side</td><td>Traditional web apps, SSR</td><td>CSRF, session fixation</td></tr>
        <tr><td><strong>JWT (Bearer)</strong></td><td>Stateless</td><td>APIs, SPA, mobile</td><td>Token theft, alg=none, weak secret</td></tr>
        <tr><td><strong>OAuth2 / OIDC</strong></td><td>Delegated</td><td>Third-party login, SSO</td><td>Open redirect, CSRF on callback</td></tr>
        <tr><td><strong>API Keys</strong></td><td>Stateless</td><td>M2M, developer APIs</td><td>Key exposure, no expiry</td></tr>
        <tr><td><strong>mTLS</strong></td><td>Cert-based</td><td>Service-to-service</td><td>Cert rotation complexity</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">Phase 3 concept map</div>
  <div class="cp-body">
    <ul class="flow-list">
      <li><span class="fl-step">1</span><div><strong>Sessions &amp; Cookies</strong> — server-side state, <code>HttpOnly</code>+<code>Secure</code>+<code>SameSite</code>, Redis storage, session fixation, CSRF tokens</div></li>
      <li><span class="fl-step">2</span><div><strong>JWT</strong> — header.payload.signature, signing algorithms (HS256/RS256/ES256), claims, verification, pitfalls (<code>alg:none</code>, weak secrets)</div></li>
      <li><span class="fl-step">3</span><div><strong>Access + Refresh tokens</strong> — short-lived access, long-lived refresh, rotation, revocation in DB</div></li>
      <li><span class="fl-step">4</span><div><strong>OAuth2</strong> — Authorization Code + PKCE, Client Credentials, Device Code; OIDC layer for identity</div></li>
      <li><span class="fl-step">5</span><div><strong>API Keys</strong> — CSPRNG generation, SHA-256 hashing at rest, prefix-based lookup, scoping, rotation</div></li>
      <li><span class="fl-step">6</span><div><strong>RBAC / ABAC</strong> — role hierarchy, permission matrices, policy evaluation, OPA integration</div></li>
      <li><span class="fl-step">7</span><div><strong>Password security</strong> — bcrypt, Argon2id parameters, timing-safe comparison, pepper strategy</div></li>
    </ul>
  </div>
</div>

<div class="note">
  <strong>Module path:</strong> This is M09 in Phase 3 (of 8 phases). Prerequisites: M01 (TCP/TLS), M03 (REST APIs), M06 (SQL/PostgreSQL).
  Concepts build on each other within this module — read tabs in order on your first pass.
</div>

</div><!-- /overview -->

<!-- ═══════════════════════ SESSIONS & COOKIES ═══════════════════════ -->
<div class="tab-pane" id="tab-sessions">

<div class="cp p-red">
  <div class="cp-hdr">How session-based authentication works</div>
  <div class="cp-body">
    <ol class="flow-list">
      <li><span class="fl-step">1</span><div>User submits credentials (username + password) over HTTPS</div></li>
      <li><span class="fl-step">2</span><div>Server verifies password hash, then calls <code>session_create()</code> → generates cryptographically random session ID</div></li>
      <li><span class="fl-step">3</span><div>Server stores session data (user_id, role, created_at, expires_at) in Redis/DB keyed by session ID</div></li>
      <li><span class="fl-step">4</span><div>Server sends: <code>Set-Cookie: sid=&lt;random_id&gt;; HttpOnly; Secure; SameSite=Strict; Max-Age=3600</code></div></li>
      <li><span class="fl-step">5</span><div>Browser automatically includes cookie on every subsequent same-origin request</div></li>
      <li><span class="fl-step">6</span><div>Server looks up session ID in Redis → retrieves user context → authorizes request</div></li>
      <li><span class="fl-step">7</span><div>On logout: delete the session record from Redis (server-side invalidation) + clear cookie</div></li>
    </ol>
  </div>
</div>

<div class="two-col">
  <div class="cp p-orange">
    <div class="cp-hdr">Cookie attributes — every one matters</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Attribute</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td><code>HttpOnly</code></td><td>JS cannot read cookie → blocks XSS token theft</td></tr>
          <tr><td><code>Secure</code></td><td>Only sent over HTTPS → no cleartext leakage</td></tr>
          <tr><td><code>SameSite=Strict</code></td><td>Cookie not sent cross-site → blocks CSRF</td></tr>
          <tr><td><code>SameSite=Lax</code></td><td>Sent on top-level GET nav; blocks form-based CSRF</td></tr>
          <tr><td><code>Max-Age</code></td><td>Seconds until expiry (prefer over <code>Expires</code>)</td></tr>
          <tr><td><code>Path=/</code></td><td>Scope to whole domain (usually what you want)</td></tr>
          <tr><td><code>Domain</code></td><td>Omit to restrict to exact domain (more secure)</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="cp p-blue">
    <div class="cp-hdr">Redis session storage layout</div>
    <div class="cp-body">
<div class="cb">
<span class="cm"># Key: "session:{id}" — TTL = session duration</span>
<span class="cm"># Value: hash with user context</span>
HSET session:a3f9b2c1...
  user_id    42
  email      alice@example.com
  role       admin
  created_at 1711000000
  ip         203.0.113.5

EXPIRE session:a3f9b2c1... 3600

<span class="cm"># Lookup on every request (sub-millisecond)</span>
HGETALL session:a3f9b2c1...
</div>
      <div class="note" style="margin-top:.5rem">Use a dedicated Redis DB (index 1+) for sessions, separate from cache, so a cache flush doesn't log everyone out.</div>
    </div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">Session fixation attack &amp; defence</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Attack scenario:</strong> Attacker visits site, gets session ID <code>sid=ATTACKER_KNOWN_ID</code>.
      Tricks victim into using that same ID (e.g., via URL parameter <code>?sid=...</code>).
      Victim logs in. Server associates victim's identity with attacker's known session ID.
      Attacker is now authenticated as victim.
    </div>
    <div class="sec-box">
      <strong>Defence: Always regenerate session ID on privilege elevation</strong>
      On login (or any privilege change): delete old session record, create new session ID, set new cookie.
      Never reuse a pre-authentication session ID after authentication.
    </div>
<div class="cb">
<span class="cm">/* Pseudocode for safe login flow */</span>
<span class="ck">void</span> <span class="cf">handle_login</span>(Request *req, Response *res) {
    <span class="cm">// 1. Verify credentials</span>
    User *user = verify_credentials(req->body.username, req->body.password);
    <span class="ck">if</span> (!user) { send_401(res); <span class="ck">return</span>; }

    <span class="cm">// 2. CRITICAL: destroy old session (session fixation defence)</span>
    <span class="ck">const char</span> *old_sid = get_cookie(req, <span class="cs">"sid"</span>);
    <span class="ck">if</span> (old_sid) redis_del(old_sid);

    <span class="cm">// 3. Generate new session ID (128-bit random)</span>
    <span class="cn">uint8_t</span> raw[<span class="cn">16</span>];
    RAND_bytes(raw, <span class="ck">sizeof</span>(raw));  <span class="cm">/* OpenSSL CSPRNG */</span>
    <span class="ck">char</span> sid[<span class="cn">33</span>]; bin2hex(raw, sid, <span class="cn">16</span>);

    <span class="cm">// 4. Store in Redis with TTL</span>
    redis_hset(<span class="cs">"session:"</span>, sid, <span class="cs">"user_id"</span>, user->id);
    redis_expire(<span class="cs">"session:"</span>, sid, <span class="cn">3600</span>);

    <span class="cm">// 5. Set HttpOnly Secure SameSite=Strict cookie</span>
    set_cookie(res, <span class="cs">"sid"</span>, sid,
        <span class="cs">"HttpOnly; Secure; SameSite=Strict; Max-Age=3600"</span>);
}
</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">CSRF — Cross-Site Request Forgery</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Why cookies are vulnerable to CSRF:</strong> The browser attaches cookies automatically to ANY request to the target origin — including requests initiated from a malicious third-party site via hidden forms or image tags.
    </div>
    <table class="t-table">
      <thead><tr><th>CSRF Defence</th><th>How it works</th><th>When to use</th></tr></thead>
      <tbody>
        <tr><td><code>SameSite=Strict</code></td><td>Cookie never sent cross-site</td><td>Best — use for auth cookies</td></tr>
        <tr><td><code>SameSite=Lax</code></td><td>Sent on top-level GET nav only</td><td>Good fallback, allows OAuth redirects</td></tr>
        <tr><td>CSRF token (synchronizer)</td><td>Server issues random token, validates on POST</td><td>Needed when SameSite not supported</td></tr>
        <tr><td>Double-submit cookie</td><td>Cookie + header must match</td><td>Stateless CSRF protection</td></tr>
        <tr><td>Origin/Referer check</td><td>Validate request origin header</td><td>Defense-in-depth only</td></tr>
      </tbody>
    </table>
    <div class="warn">SameSite=Lax still allows CSRF via cross-site top-level navigation (e.g., clicking a link). Use Strict for login flows. If you use both SameSite and CSRF tokens, you get defense-in-depth.</div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">Session security checklist</div>
  <div class="cp-body">
    <ul class="cl">
      <li>Session ID is ≥128 bits from CSPRNG (OpenSSL <code>RAND_bytes</code>, not <code>rand()</code>)</li>
      <li>Session ID regenerated on every login (session fixation defence)</li>
      <li>Cookie: <code>HttpOnly</code> + <code>Secure</code> + <code>SameSite=Strict</code></li>
      <li>Session TTL enforced server-side (Redis EXPIRE), not just client-side cookie</li>
      <li>Logout deletes session from Redis (not just clears cookie)</li>
      <li>Concurrent session limit enforced (revoke old sessions on new login, or cap at N)</li>
      <li>Session ID not in URL (prevents log leakage)</li>
    </ul>
  </div>
</div>

</div><!-- /sessions -->

<!-- ═══════════════════════ JWT DEEP DIVE ═══════════════════════ -->
<div class="tab-pane" id="tab-jwt">

<div class="cp p-red">
  <div class="cp-hdr">JWT anatomy — every byte matters</div>
  <div class="cp-body">
    A JWT is three Base64url-encoded JSON objects joined by dots:
<div class="cb">
<span class="cm">// Full JWT (line-wrapped for readability):</span>
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJzdWIiOiI0MiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcxMTAwMDAwMCwiZXhwIjoxNzExMDAzNjAwfQ
.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

<span class="cm">// Header (decoded):</span>
{ <span class="cs">"alg"</span>: <span class="cs">"HS256"</span>, <span class="cs">"typ"</span>: <span class="cs">"JWT"</span> }

<span class="cm">// Payload (decoded):</span>
{
  <span class="cs">"sub"</span>: <span class="cs">"42"</span>,       <span class="cm">// subject — user ID</span>
  <span class="cs">"iss"</span>: <span class="cs">"api.example.com"</span>,  <span class="cm">// issuer</span>
  <span class="cs">"aud"</span>: <span class="cs">"frontend"</span>, <span class="cm">// audience — who can use this token</span>
  <span class="cs">"role"</span>: <span class="cs">"admin"</span>,   <span class="cm">// custom claim</span>
  <span class="cs">"iat"</span>: 1711000000, <span class="cm">// issued at (Unix timestamp)</span>
  <span class="cs">"exp"</span>: 1711003600, <span class="cm">// expiry — 1 hour later</span>
  <span class="cs">"jti"</span>: <span class="cs">"a3f9b2c1-..."</span> <span class="cm">// JWT ID — for revocation</span>
}

<span class="cm">// Signature = HMAC-SHA256(base64url(header) + "." + base64url(payload), secret)</span>
</div>
    <div class="warn">The payload is <strong>not encrypted</strong> — only signed. Anyone with the token can base64-decode and read the claims. Never put secrets, PII, or sensitive data in JWT payload unless using JWE (JSON Web Encryption).</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">Signing algorithms: HS256 vs RS256 vs ES256</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Algorithm</th><th>Type</th><th>Key material</th><th>Verify cost</th><th>Best for</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>HS256</strong></td><td>Symmetric HMAC-SHA256</td>
          <td>One shared secret — all services that verify must have it</td>
          <td>Very fast</td>
          <td>Monolith or single-service systems</td>
        </tr>
        <tr>
          <td><strong>RS256</strong></td><td>Asymmetric RSA-PKCS1v15</td>
          <td>Private key signs, public key verifies — distributable JWKS endpoint</td>
          <td>Slow (RSA)</td>
          <td>Multi-service; public key can be published</td>
        </tr>
        <tr>
          <td><strong>ES256</strong></td><td>Asymmetric ECDSA P-256</td>
          <td>Same as RS256 but smaller keys (256-bit vs 2048-bit)</td>
          <td>Moderate</td>
          <td>Modern APIs, mobile, IoT</td>
        </tr>
      </tbody>
    </table>
    <div class="sec-box">
      <strong>HS256 secret requirements:</strong> Must be ≥256 bits (32 bytes) of entropy from CSPRNG.
      A weak secret (e.g., "secret", "password") can be brute-forced offline — attacker just needs any valid JWT.
      For RS256/ES256, use a proper key pair generated with OpenSSL.
    </div>
  </div>
</div>

<div class="cp p-violet">
  <div class="cp-hdr">Access + Refresh token pattern</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Problem:</strong> If you make access tokens long-lived (24h+), a stolen token is valid for a long time.
      If you make them short-lived (15min), users must re-login constantly. The solution is two tokens with different lifetimes.
    </div>

<div class="seq">
<span class="actor">Client</span>          <span class="actor">Auth Server</span>                      <span class="actor">Resource Server</span>
  │                    │                                   │
  │──POST /login──────►│                                   │
  │                    │ verify password                   │
  │◄──access(15m)──────│                                   │
  │   refresh(30d)     │ store refresh in DB               │
  │                    │                                   │
  │──GET /api ─────────────────────────────────────────────►
  │  Authorization: Bearer &lt;access_token&gt;                  │
  │                    │  verify signature (no DB lookup)  │
  │◄────────────────────────────────────── 200 OK ─────────│
  │                    │                                   │
  │ ... 15 min later, access_token expired ...            │
  │──POST /refresh────►│                                   │
  │   {refresh_token}  │ lookup in DB, validate            │
  │                    │ rotate: delete old, issue new     │
  │◄──new access(15m)──│                                   │
  │   new refresh(30d) │                                   │
</div>

    <table class="t-table" style="margin-top:.8rem">
      <thead><tr><th>Property</th><th>Access Token</th><th>Refresh Token</th></tr></thead>
      <tbody>
        <tr><td>Lifetime</td><td>15 min – 1 hour</td><td>7 – 30 days</td></tr>
        <tr><td>Storage (client)</td><td>Memory (SPA) or HttpOnly cookie</td><td>HttpOnly Secure cookie</td></tr>
        <tr><td>Validation</td><td>Signature only — no DB lookup</td><td>DB lookup — can be revoked</td></tr>
        <tr><td>Rotation</td><td>Not rotated</td><td>Single-use: new token on each use</td></tr>
        <tr><td>On theft detection</td><td>Wait for expiry</td><td>Revoke entire refresh token family</td></tr>
      </tbody>
    </table>
    <div class="ins">Refresh token rotation: if server receives a previously-used (already-rotated) refresh token, assume token theft → revoke all tokens for that user/session immediately (refresh token reuse detection).</div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">Critical JWT vulnerabilities</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attack</th><th>How it works</th><th>Defence</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="bad">alg:none</span></td>
          <td>Attacker sets <code>"alg":"none"</code> in header and removes signature. Some libraries accept unsigned tokens.</td>
          <td>Hardcode expected algorithm — never trust the header's <code>alg</code> field. Reject <code>none</code>.</td>
        </tr>
        <tr>
          <td><span class="bad">Algorithm confusion</span></td>
          <td>RS256 server given token with <code>alg:HS256</code>; HMAC key = public key (which attacker knows). Library uses public key as HMAC secret.</td>
          <td>Always specify algorithm explicitly in verification call, never pass <code>allowed_algs=all</code>.</td>
        </tr>
        <tr>
          <td><span class="bad">Weak HS256 secret</span></td>
          <td>Offline brute-force with hashcat using any valid JWT.</td>
          <td>Use ≥256 bits from CSPRNG. Rotate regularly.</td>
        </tr>
        <tr>
          <td><span class="bad">Missing exp validation</span></td>
          <td>Expired tokens accepted indefinitely.</td>
          <td>Always validate <code>exp</code>, <code>nbf</code>, <code>iss</code>, <code>aud</code>.</td>
        </tr>
        <tr>
          <td><span class="bad">JWT stored in localStorage</span></td>
          <td>XSS can read <code>localStorage</code> and exfiltrate the token.</td>
          <td>Store in memory (SPA) or HttpOnly cookie. Never <code>localStorage</code>.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">JWT revocation strategies</div>
  <div class="cp-body">
    JWTs are stateless — once issued, they're valid until <code>exp</code> unless you implement revocation:
    <table class="t-table" style="margin-top:.6rem">
      <thead><tr><th>Strategy</th><th>How</th><th>Cost</th><th>Scale</th></tr></thead>
      <tbody>
        <tr><td><strong>Short expiry</strong></td><td>15-min access tokens; only refresh revocable</td><td>None</td><td>Excellent</td></tr>
        <tr><td><strong>jti denylist</strong></td><td>Store revoked <code>jti</code> values in Redis; check on every request</td><td>1 Redis lookup/req</td><td>Good</td></tr>
        <tr><td><strong>Token family in DB</strong></td><td>Store token generation counter per user; reject if stale</td><td>1 DB lookup/req</td><td>Moderate</td></tr>
        <tr><td><strong>JWKS key rotation</strong></td><td>Rotate signing key; old tokens signed with revoked key rejected</td><td>None per-req</td><td>Excellent (bulk revoke)</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /jwt -->

<!-- ═══════════════════════ OAUTH2 & API KEYS ═══════════════════════ -->
<div class="tab-pane" id="tab-oauth">

<div class="cp p-orange">
  <div class="cp-hdr">OAuth2 — delegation, not authentication</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>OAuth2 is an authorization framework, not an authentication protocol.</strong>
      It lets a user delegate limited access to their resources (e.g., their GitHub repos) to a third-party app,
      without giving the app their password. OpenID Connect (OIDC) adds an identity layer on top of OAuth2.
    </div>
    <table class="t-table" style="margin-top:.6rem">
      <thead><tr><th>Role</th><th>Who they are</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td><strong>Resource Owner</strong></td><td>The user</td><td>Alice</td></tr>
        <tr><td><strong>Client</strong></td><td>App requesting access</td><td>Your app</td></tr>
        <tr><td><strong>Authorization Server</strong></td><td>Issues tokens after user consent</td><td>GitHub, Google, Auth0</td></tr>
        <tr><td><strong>Resource Server</strong></td><td>API that accepts tokens</td><td>GitHub API</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">Authorization Code + PKCE flow (recommended for SPAs &amp; mobile)</div>
  <div class="cp-body">
<div class="seq">
<span class="actor">User</span>       <span class="actor">Your App (Client)</span>           <span class="actor">Auth Server</span>
  │                  │                              │
  │─click "Login"───►│                              │
  │                  │ generate code_verifier (random 32 bytes)
  │                  │ code_challenge = BASE64URL(SHA-256(verifier))
  │                  │──redirect /authorize?──────►│
  │                  │  client_id=...               │
  │                  │  redirect_uri=...            │
  │                  │  response_type=code          │
  │                  │  code_challenge=...          │
  │                  │  code_challenge_method=S256  │
  │◄─────────────────│  (user sees consent screen)  │
  │─approve──────────────────────────────────────►│
  │◄──redirect ?code=AUTH_CODE─────────────────────│
  │                  │                              │
  │──code────────────►│                              │
  │                  │──POST /token ───────────────►│
  │                  │  code=AUTH_CODE              │
  │                  │  code_verifier=VERIFIER      │
  │                  │◄───── access_token + id_token│
  │◄──logged in──────│                              │
</div>
    <div class="note">PKCE (Proof Key for Code Exchange) prevents authorization code interception attacks. Even if the code is stolen in transit, the attacker doesn't have the code_verifier needed to exchange it for a token.</div>
  </div>
</div>

<div class="cp p-violet">
  <div class="cp-hdr">Client Credentials flow (machine-to-machine)</div>
  <div class="cp-body">
    Used when there's no user involved — a service authenticating to another service:
<div class="cb">
<span class="cm">// POST /oauth/token</span>
{
  <span class="cs">"grant_type"</span>: <span class="cs">"client_credentials"</span>,
  <span class="cs">"client_id"</span>: <span class="cs">"my-service"</span>,
  <span class="cs">"client_secret"</span>: <span class="cs">"s3cr3t"</span>,
  <span class="cs">"scope"</span>: <span class="cs">"payments:read inventory:write"</span>
}

<span class="cm">// Response:</span>
{
  <span class="cs">"access_token"</span>: <span class="cs">"eyJ..."</span>,
  <span class="cs">"token_type"</span>: <span class="cs">"Bearer"</span>,
  <span class="cs">"expires_in"</span>: 3600,
  <span class="cs">"scope"</span>: <span class="cs">"payments:read inventory:write"</span>
}
</div>
    <div class="warn">Client secrets are like passwords — store in environment variables or a secrets manager (Vault, AWS Secrets Manager), never in code or git.</div>
  </div>
</div>

<hr class="sep">

<div class="cp p-red">
  <div class="cp-hdr">API Keys — design for security</div>
  <div class="cp-body">
    <ul class="flow-list">
      <li><span class="fl-step">1</span><div><strong>Generation:</strong> 32 bytes from CSPRNG → base62 or hex encode → prefix with identifier (e.g., <code>sk_live_</code> for lookup without full hash scan)</div></li>
      <li><span class="fl-step">2</span><div><strong>Storage:</strong> Never store plaintext. Store <code>SHA-256(key)</code> in DB. Show full key to user exactly once on creation.</div></li>
      <li><span class="fl-step">3</span><div><strong>Lookup:</strong> <code>prefix</code> column (first 8 chars) for fast DB lookup + constant-time comparison of hash</div></li>
      <li><span class="fl-step">4</span><div><strong>Scoping:</strong> Attach permissions to key (e.g., <code>read:payments</code>, <code>write:orders</code>)</div></li>
      <li><span class="fl-step">5</span><div><strong>Rotation:</strong> Allow multiple active keys; deactivate old key after grace period</div></li>
      <li><span class="fl-step">6</span><div><strong>Rate limiting:</strong> Limit by key, not just IP — prevents key sharing abuse</div></li>
    </ul>

<div class="cb">
<span class="cm">-- API key DB schema</span>
<span class="ck">CREATE TABLE</span> api_keys (
    id         UUID         <span class="ck">PRIMARY KEY DEFAULT</span> gen_random_uuid(),
    user_id    BIGINT       <span class="ck">REFERENCES</span> users(id),
    prefix     <span class="cn">VARCHAR(8)</span>   <span class="ck">NOT NULL</span>,              <span class="cm">-- first 8 chars, for lookup</span>
    key_hash   <span class="cn">CHAR(64)</span>     <span class="ck">NOT NULL UNIQUE</span>,       <span class="cm">-- SHA-256 hex</span>
    name       <span class="cn">TEXT</span>         <span class="ck">NOT NULL</span>,              <span class="cm">-- e.g., "Production App"</span>
    scopes     <span class="cn">TEXT[]</span>       <span class="ck">NOT NULL DEFAULT</span> <span class="cs">'{}'</span>,
    last_used  TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    revoked_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ  <span class="ck">NOT NULL DEFAULT</span> now()
);
<span class="ck">CREATE INDEX</span> ON api_keys (prefix) <span class="ck">WHERE</span> revoked_at <span class="ck">IS NULL</span>;
</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">OAuth2 security pitfalls</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Vulnerability</th><th>Description</th><th>Defence</th></tr></thead>
      <tbody>
        <tr><td><span class="bad">Open redirect</span></td><td><code>redirect_uri</code> not validated → tokens sent to attacker</td><td>Exact match against allowlist of registered URIs</td></tr>
        <tr><td><span class="bad">CSRF on callback</span></td><td>Attacker initiates OAuth flow, tricks user's browser to complete it</td><td>Use <code>state</code> parameter (random nonce, validated on callback)</td></tr>
        <tr><td><span class="bad">Token leakage in logs</span></td><td>Access tokens appear in access logs via URL params</td><td>Always use Authorization header, never URL params</td></tr>
        <tr><td><span class="bad">Implicit flow</span></td><td>Token returned in URL fragment (deprecated) → history/referrer leakage</td><td>Use Authorization Code + PKCE instead of Implicit flow</td></tr>
        <tr><td><span class="bad">aud not validated</span></td><td>Token issued for service A accepted by service B</td><td>Always validate <code>aud</code> claim matches expected audience</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /oauth -->

<!-- ═══════════════════════ AUTHORIZATION ═══════════════════════ -->
<div class="tab-pane" id="tab-authz">

<div class="cp p-indigo">
  <div class="cp-hdr">RBAC — Role-Based Access Control</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Concept:</strong> Users are assigned roles; roles are granted permissions.
      The user never holds permissions directly — only via roles. Simple, auditable, scales well for most apps.
    </div>
<div class="cb">
<span class="cm">-- Classic RBAC schema</span>
<span class="ck">CREATE TABLE</span> roles (id BIGINT <span class="ck">PRIMARY KEY</span>, name <span class="cn">TEXT UNIQUE</span>);
<span class="ck">CREATE TABLE</span> permissions (id BIGINT <span class="ck">PRIMARY KEY</span>, name <span class="cn">TEXT UNIQUE</span>);
<span class="ck">CREATE TABLE</span> role_permissions (role_id BIGINT, permission_id BIGINT, <span class="ck">PRIMARY KEY</span>(role_id, permission_id));
<span class="ck">CREATE TABLE</span> user_roles (user_id BIGINT, role_id BIGINT, <span class="ck">PRIMARY KEY</span>(user_id, role_id));

<span class="cm">-- Check: can user 42 read invoices?</span>
<span class="ck">SELECT</span> 1 <span class="ck">FROM</span> user_roles ur
  <span class="ck">JOIN</span> role_permissions rp <span class="ck">ON</span> ur.role_id = rp.role_id
  <span class="ck">JOIN</span> permissions p      <span class="ck">ON</span> rp.permission_id = p.id
<span class="ck">WHERE</span> ur.user_id = 42
  <span class="ck">AND</span> p.name = <span class="cs">'invoices:read'</span>
<span class="ck">LIMIT</span> 1;
</div>
    <table class="t-table" style="margin-top:.7rem">
      <thead><tr><th>Role</th><th>Permissions</th></tr></thead>
      <tbody>
        <tr><td>viewer</td><td>invoices:read, orders:read</td></tr>
        <tr><td>editor</td><td>+ invoices:write, orders:write</td></tr>
        <tr><td>admin</td><td>+ users:manage, settings:write</td></tr>
        <tr><td>billing</td><td>invoices:*, payments:*</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-violet">
  <div class="cp-hdr">ABAC — Attribute-Based Access Control</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Concept:</strong> Policies evaluate attributes of subject (user), resource, action, and environment.
      More expressive than RBAC — supports fine-grained, context-aware rules.
    </div>
<div class="cb">
<span class="cm">// OPA (Open Policy Agent) Rego policy example</span>
<span class="ck">package</span> authz

<span class="cm">// Allow read if user is in same org as document</span>
allow {
    input.action == <span class="cs">"read"</span>
    input.subject.org_id == input.resource.org_id
}

<span class="cm">// Allow write only for managers in same org</span>
allow {
    input.action == <span class="cs">"write"</span>
    input.subject.role == <span class="cs">"manager"</span>
    input.subject.org_id == input.resource.org_id
}

<span class="cm">// Deny after business hours (environment attribute)</span>
deny {
    input.action == <span class="cs">"export"</span>
    hour := time.clock(time.now_ns())[0]
    hour >= <span class="cn">18</span>
}
</div>
    <table class="t-table" style="margin-top:.7rem">
      <thead><tr><th></th><th>RBAC</th><th>ABAC</th></tr></thead>
      <tbody>
        <tr><td>Granularity</td><td>Coarse (role-level)</td><td>Fine (any attribute)</td></tr>
        <tr><td>Complexity</td><td>Simple</td><td>Complex (policy management)</td></tr>
        <tr><td>Context-awareness</td><td>None</td><td>Time, IP, device, location</td></tr>
        <tr><td>Auditing</td><td>Easy</td><td>Harder (policy explosion)</td></tr>
        <tr><td>Use when</td><td>Clear role hierarchy</td><td>Multi-tenant, fine-grained rules</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">Authorization enforcement patterns</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Pattern</th><th>How</th><th>Problem it solves</th></tr></thead>
      <tbody>
        <tr><td><strong>Middleware check</strong></td><td>Auth middleware runs before route handler; rejects if insufficient role</td><td>Coarse-grained: route-level protection</td></tr>
        <tr><td><strong>Resource ownership</strong></td><td><code>WHERE user_id = current_user_id</code> in every query</td><td>Prevents horizontal privilege escalation (user A reading user B's data)</td></tr>
        <tr><td><strong>Policy as code</strong></td><td>OPA sidecar or in-process evaluation</td><td>Complex/dynamic rules; audit trail</td></tr>
        <tr><td><strong>Field-level authz</strong></td><td>Strip sensitive fields from response if requester lacks permission</td><td>Fine-grained: same resource, different views</td></tr>
      </tbody>
    </table>
    <div class="ins">
      <strong>Horizontal privilege escalation (IDOR)</strong> — the most common authz bug:<br>
      <code>GET /invoices/9999</code> — always check that invoice 9999 belongs to the authenticated user.
      Never rely only on "authenticated" — always check ownership.
    </div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">JWT claims as lightweight RBAC</div>
  <div class="cp-body">
    Embed permissions or roles in the JWT to avoid a DB lookup on every request:
<div class="cb">
{
  <span class="cs">"sub"</span>: <span class="cs">"42"</span>,
  <span class="cs">"role"</span>: <span class="cs">"admin"</span>,
  <span class="cs">"perms"</span>: [<span class="cs">"invoices:read"</span>, <span class="cs">"invoices:write"</span>, <span class="cs">"users:manage"</span>],
  <span class="cs">"org_id"</span>: <span class="cs">"acme"</span>,
  <span class="cs">"exp"</span>: 1711003600
}
</div>
    <div class="warn">
      Claims in JWT are stale as soon as they're issued. If you revoke a user's role, they retain the old claims until token expiry.
      Short access token lifetime (15min) limits the stale-data window. For immediate revocation, use a token denylist.
    </div>
  </div>
</div>

</div><!-- /authz -->

<!-- ═══════════════════════ PASSWORD SECURITY ═══════════════════════ -->
<div class="tab-pane" id="tab-passwords">

<div class="cp p-red">
  <div class="cp-hdr">Why fast hashes are catastrophically wrong</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Hash</th><th>Speed on GPU</th><th>Time to crack 8-char password</th></tr></thead>
      <tbody>
        <tr><td>MD5</td><td class="bad">~200 billion/sec</td><td class="bad">Seconds</td></tr>
        <tr><td>SHA-256</td><td class="bad">~20 billion/sec</td><td class="bad">Minutes to hours</td></tr>
        <tr><td>bcrypt (cost=10)</td><td class="ok">~10,000/sec</td><td class="ok">Months to years</td></tr>
        <tr><td>Argon2id (recommended)</td><td class="good">~1,000/sec</td><td class="good">Years to decades</td></tr>
      </tbody>
    </table>
    <div class="analogy">
      <strong>Why password hashing needs to be slow:</strong> A DB breach exposes all hashed passwords.
      With a fast hash, a GPU cluster can try billions of common passwords per second.
      A deliberately slow hash (bcrypt, Argon2) forces brute-force to take impractically long, even if the hash is stolen.
    </div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">bcrypt — the reliable default</div>
  <div class="cp-body">
<div class="cb">
<span class="cm">/* bcrypt: cost factor controls iteration count (2^cost rounds) */</span>
<span class="cm">/* Target: ~100ms hash time on your server hardware */</span>
<span class="cm">/* Start at cost=12; benchmark; increase as hardware improves */</span>

<span class="cm">/* Format: $2b$12$&lt;22-char salt&gt;&lt;31-char hash&gt; */</span>
$2b$<span class="cn">12</span>$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/leHD7dNzT0pLcOHo.

<span class="cm">/* Key properties: */</span>
<span class="cm">/* - Salt is embedded in the hash string (no separate salt column needed) */</span>
<span class="cm">/* - Output always 60 chars — use VARCHAR(60) or CHAR(60) */</span>
<span class="cm">/* - Cost factor should be re-evaluated every 2 years */</span>
<span class="cm">/* - Max input 72 bytes (silently truncates longer passwords) */</span>
</div>
    <div class="warn">bcrypt truncates inputs longer than 72 bytes. If users might have longer passwords, pre-hash with SHA-256 (to compress to 32 bytes) before bcrypt — but use a constant encoding, not just SHA-256 alone.</div>
  </div>
</div>

<div class="cp p-violet">
  <div class="cp-hdr">Argon2id — OWASP recommended</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Why Argon2id over bcrypt?</strong> Argon2 is memory-hard — it requires large amounts of RAM per hash,
      which makes GPU/ASIC attacks expensive (GPUs have less RAM per core than CPUs).
      Argon2id combines Argon2i (side-channel resistance) and Argon2d (GPU resistance).
    </div>
<div class="cb">
<span class="cm">/* Argon2id parameters (OWASP recommendations for interactive login): */</span>
<span class="cm">/* - m = 19456 KB (19 MiB) memory                                    */</span>
<span class="cm">/* - t = 2       iterations                                          */</span>
<span class="cm">/* - p = 1       parallelism                                         */</span>
<span class="cm">/* - tag_len = 32 bytes output                                       */</span>

<span class="cm">/* For high-security (allow >500ms): m=65536, t=3, p=4              */</span>

<span class="cm">/* libsodium (C library) — preferred over rolling your own: */</span>
<span class="ck">#include</span> <span class="cs">&lt;sodium.h&gt;</span>

<span class="ck">char</span> hashed_password[crypto_pwhash_STRBYTES];  <span class="cm">/* 128 bytes */</span>

<span class="ck">if</span> (crypto_pwhash_str(
        hashed_password,
        password, strlen(password),
        crypto_pwhash_OPSLIMIT_INTERACTIVE,   <span class="cm">/* 2 ops   */</span>
        crypto_pwhash_MEMLIMIT_INTERACTIVE    <span class="cm">/* 64 MiB  */</span>
    ) != <span class="cn">0</span>) {
    <span class="cm">/* out of memory — return 500 */</span>
}
<span class="cm">/* Store hashed_password in DB */</span>

<span class="cm">/* Verification: */</span>
<span class="ck">if</span> (crypto_pwhash_str_verify(
        hashed_password,
        password, strlen(password)
    ) != <span class="cn">0</span>) {
    <span class="cm">/* Wrong password */</span>
}
</div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">Timing-safe comparison — critical for security</div>
  <div class="cp-body">
    <div class="analogy">
      <strong>Timing attack:</strong> A naive <code>strcmp()</code> returns early on the first differing byte.
      An attacker can measure how long the comparison takes to deduce how many bytes of their guess match.
      With enough measurements, they can recover a secret byte-by-byte.
    </div>
<div class="cb">
<span class="cm">/* WRONG — leaks timing information */</span>
<span class="ck">int</span> verify = strcmp(submitted_hash, stored_hash) == <span class="cn">0</span>;

<span class="cm">/* CORRECT — constant-time comparison (OpenSSL) */</span>
<span class="ck">#include</span> <span class="cs">&lt;openssl/crypto.h&gt;</span>
<span class="ck">int</span> result = CRYPTO_memcmp(computed_hmac, stored_hmac, HMAC_LEN);
<span class="cm">/* result == 0 means equal — no early exit */</span>

<span class="cm">/* Also safe: libsodium's constant-time equal */</span>
<span class="ck">#include</span> <span class="cs">&lt;sodium.h&gt;</span>
<span class="ck">int</span> ok = sodium_memcmp(a, b, len);  <span class="cm">/* 0 = equal */</span>

<span class="cm">/* Use constant-time comparison for: */</span>
<span class="cm">/* - HMAC verification (JWT, CSRF tokens, webhook signatures) */</span>
<span class="cm">/* - API key comparison (though hash-then-compare is better) */</span>
<span class="cm">/* Note: For passwords, use crypto_pwhash_str_verify() — which
         handles timing internally */</span>
</div>
    <div class="ins">When comparing API keys: hash both submitted and stored values with SHA-256, then compare the hashes with a constant-time function. This is safer than comparing raw keys.</div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">Pepper — defense in depth for password hashing</div>
  <div class="cp-body">
    A <strong>pepper</strong> is a secret value mixed into the password hash, stored separately from the DB (e.g., in an env var or secrets manager):
<div class="cb">
<span class="cm">/* Pepper strategy: HMAC password with pepper, then Argon2 */</span>
<span class="ck">void</span> <span class="cf">hash_password_with_pepper</span>(<span class="ck">const char</span> *password, <span class="ck">char</span> *out) {
    <span class="cn">uint8_t</span> pepper[<span class="cn">32</span>];
    get_pepper_from_env(pepper);  <span class="cm">/* load from secrets manager */</span>

    <span class="cm">/* HMAC-SHA256(pepper, password) → 32 bytes */</span>
    <span class="cn">uint8_t</span> peppered[<span class="cn">32</span>];
    HMAC(EVP_sha256(), pepper, <span class="cn">32</span>,
         (<span class="ck">const unsigned char</span> *)password, strlen(password),
         peppered, <span class="ck">NULL</span>);

    <span class="cm">/* Then Argon2id the peppered value */</span>
    crypto_pwhash_str(out, (<span class="ck">const char</span> *)peppered, <span class="cn">32</span>,
        crypto_pwhash_OPSLIMIT_INTERACTIVE,
        crypto_pwhash_MEMLIMIT_INTERACTIVE);
}
<span class="cm">/* Benefit: even if DB is stolen, attacker also needs the pepper
   to crack passwords. Pepper rotation requires rehashing all users. */</span>
</div>
  </div>
</div>

</div><!-- /passwords -->

<!-- ═══════════════════════ C IMPLEMENTATION ═══════════════════════ -->
<div class="tab-pane" id="tab-impl">

<div class="cp p-red">
  <div class="cp-hdr">JWT HS256 sign and verify in C (OpenSSL)</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">#include</span> <span class="cs">&lt;openssl/hmac.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;openssl/evp.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;openssl/rand.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdint.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;time.h&gt;</span>

<span class="cm">/* Base64url encoding (no padding) */</span>
<span class="ck">static const char</span> b64url_chars[] =
    <span class="cs">"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"</span>;

<span class="ck">void</span> <span class="cf">base64url_encode</span>(<span class="ck">const uint8_t</span> *data, <span class="cn">size_t</span> len, <span class="ck">char</span> *out) {
    <span class="cn">size_t</span> i = <span class="cn">0</span>, j = <span class="cn">0</span>;
    <span class="ck">for</span> (; i + <span class="cn">2</span> < len; i += <span class="cn">3</span>) {
        out[j++] = b64url_chars[(data[i] >> <span class="cn">2</span>) & <span class="cn">0x3F</span>];
        out[j++] = b64url_chars[((data[i] & <span class="cn">3</span>) << <span class="cn">4</span>) | (data[i+<span class="cn">1</span>] >> <span class="cn">4</span>)];
        out[j++] = b64url_chars[((data[i+<span class="cn">1</span>] & <span class="cn">0xF</span>) << <span class="cn">2</span>) | (data[i+<span class="cn">2</span>] >> <span class="cn">6</span>)];
        out[j++] = b64url_chars[data[i+<span class="cn">2</span>] & <span class="cn">0x3F</span>];
    }
    <span class="ck">if</span> (i < len) {
        out[j++] = b64url_chars[(data[i] >> <span class="cn">2</span>) & <span class="cn">0x3F</span>];
        <span class="ck">if</span> (i + <span class="cn">1</span> == len) {
            out[j++] = b64url_chars[(data[i] & <span class="cn">3</span>) << <span class="cn">4</span>];
        } <span class="ck">else</span> {
            out[j++] = b64url_chars[((data[i] & <span class="cn">3</span>) << <span class="cn">4</span>) | (data[i+<span class="cn">1</span>] >> <span class="cn">4</span>)];
            out[j++] = b64url_chars[(data[i+<span class="cn">1</span>] & <span class="cn">0xF</span>) << <span class="cn">2</span>];
        }
    }
    out[j] = <span class="cs">'\0'</span>;
}

<span class="cm">/* Create JWT: header.payload — returns malloc'd string */</span>
<span class="ck">char</span> *<span class="cf">jwt_create_hs256</span>(<span class="ck">const char</span> *payload_json,
                        <span class="ck">const uint8_t</span> *secret, <span class="cn">size_t</span> secret_len)
{
    <span class="cm">/* Fixed header: {"alg":"HS256","typ":"JWT"} */</span>
    <span class="ck">const char</span> *hdr_json = <span class="cs">"{\"alg\":\"HS256\",\"typ\":\"JWT\"}"</span>;
    <span class="ck">char</span> hdr_b64[<span class="cn">64</span>], pay_b64[<span class="cn">512</span>], sig_b64[<span class="cn">64</span>];

    base64url_encode((<span class="ck">const uint8_t</span> *)hdr_json, strlen(hdr_json), hdr_b64);
    base64url_encode((<span class="ck">const uint8_t</span> *)payload_json, strlen(payload_json), pay_b64);

    <span class="cm">/* Signing input: base64url(header) + "." + base64url(payload) */</span>
    <span class="ck">char</span> signing_input[<span class="cn">600</span>];
    snprintf(signing_input, <span class="ck">sizeof</span>(signing_input), <span class="cs">"%s.%s"</span>, hdr_b64, pay_b64);

    <span class="cm">/* HMAC-SHA256 */</span>
    <span class="cn">uint8_t</span> sig[<span class="cn">32</span>]; <span class="cn">uint32_t</span> sig_len;
    HMAC(EVP_sha256(), secret, (<span class="ck">int</span>)secret_len,
         (<span class="ck">const uint8_t</span> *)signing_input, strlen(signing_input),
         sig, &sig_len);

    base64url_encode(sig, sig_len, sig_b64);

    <span class="ck">char</span> *token = malloc(<span class="cn">700</span>);
    snprintf(token, <span class="cn">700</span>, <span class="cs">"%s.%s"</span>, signing_input, sig_b64);
    <span class="ck">return</span> token;
}

<span class="cm">/* Constant-time comparison */</span>
<span class="ck">static int</span> <span class="cf">const_time_eq</span>(<span class="ck">const uint8_t</span> *a, <span class="ck">const uint8_t</span> *b, <span class="cn">size_t</span> n) {
    <span class="cn">uint8_t</span> diff = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="cn">size_t</span> i = <span class="cn">0</span>; i < n; i++) diff |= a[i] ^ b[i];
    <span class="ck">return</span> diff == <span class="cn">0</span>;
}

<span class="cm">/* Verify JWT signature — returns 1 on success, 0 on failure */</span>
<span class="ck">int</span> <span class="cf">jwt_verify_hs256</span>(<span class="ck">const char</span> *token,
                      <span class="ck">const uint8_t</span> *secret, <span class="cn">size_t</span> secret_len,
                      <span class="ck">char</span> **payload_out)
{
    <span class="cm">/* Split: find the two dots */</span>
    <span class="ck">const char</span> *dot1 = strchr(token, <span class="cs">'.'</span>);
    <span class="ck">if</span> (!dot1) <span class="ck">return</span> <span class="cn">0</span>;
    <span class="ck">const char</span> *dot2 = strchr(dot1 + <span class="cn">1</span>, <span class="cs">'.'</span>);
    <span class="ck">if</span> (!dot2) <span class="ck">return</span> <span class="cn">0</span>;

    <span class="cm">/* signing_input = everything before last dot */</span>
    <span class="cn">size_t</span> si_len = dot2 - token;
    <span class="ck">char</span> signing_input[<span class="cn">600</span>];
    <span class="ck">if</span> (si_len >= <span class="ck">sizeof</span>(signing_input)) <span class="ck">return</span> <span class="cn">0</span>;
    memcpy(signing_input, token, si_len);
    signing_input[si_len] = <span class="cs">'\0'</span>;

    <span class="cm">/* Recompute HMAC */</span>
    <span class="cn">uint8_t</span> computed[<span class="cn">32</span>]; <span class="cn">uint32_t</span> clen;
    HMAC(EVP_sha256(), secret, (<span class="ck">int</span>)secret_len,
         (<span class="ck">const uint8_t</span> *)signing_input, si_len,
         computed, &clen);

    <span class="cm">/* TODO: base64url-decode the signature portion (dot2+1) and compare */</span>
    <span class="cm">/* Omitted for brevity — see labs for complete implementation */</span>

    *payload_out = (<span class="ck">char</span> *)(dot1 + <span class="cn">1</span>);  <span class="cm">/* base64url(payload) */</span>
    <span class="ck">return</span> <span class="cn">1</span>;  <span class="cm">/* simplified: full impl decodes and constant-time compares */</span>
}
</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">API key generation and verification in C</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">#include</span> <span class="cs">&lt;openssl/rand.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;openssl/sha.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;openssl/crypto.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>

<span class="cm">/* Generate API key: "sk_live_" + 32 random bytes as hex = 72 chars total */</span>
<span class="ck">void</span> <span class="cf">generate_api_key</span>(<span class="ck">char</span> *out_key, <span class="cn">size_t</span> key_len,
                       <span class="ck">char</span> *out_prefix, <span class="ck">char</span> *out_hash_hex)
{
    <span class="cn">uint8_t</span> raw[<span class="cn">32</span>];
    <span class="ck">if</span> (RAND_bytes(raw, <span class="cn">32</span>) != <span class="cn">1</span>) {
        fprintf(stderr, <span class="cs">"RAND_bytes failed\n"</span>); <span class="ck">return</span>;
    }

    <span class="cm">/* Build key string */</span>
    <span class="ck">char</span> hex[<span class="cn">65</span>];
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i < <span class="cn">32</span>; i++)
        sprintf(hex + i*<span class="cn">2</span>, <span class="cs">"%02x"</span>, raw[i]);
    snprintf(out_key, key_len, <span class="cs">"sk_live_%s"</span>, hex);

    <span class="cm">/* First 8 chars after prefix = prefix for DB lookup */</span>
    strncpy(out_prefix, hex, <span class="cn">8</span>);
    out_prefix[<span class="cn">8</span>] = <span class="cs">'\0'</span>;

    <span class="cm">/* SHA-256 hash for DB storage */</span>
    <span class="cn">uint8_t</span> hash[<span class="cn">32</span>];
    SHA256((<span class="ck">const uint8_t</span> *)out_key, strlen(out_key), hash);
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i < <span class="cn">32</span>; i++)
        sprintf(out_hash_hex + i*<span class="cn">2</span>, <span class="cs">"%02x"</span>, hash[i]);
    out_hash_hex[<span class="cn">64</span>] = <span class="cs">'\0'</span>;
}

<span class="cm">/* Verify submitted key against stored hash */</span>
<span class="ck">int</span> <span class="cf">verify_api_key</span>(<span class="ck">const char</span> *submitted_key, <span class="ck">const char</span> *stored_hash_hex)
{
    <span class="cn">uint8_t</span> computed_hash[<span class="cn">32</span>];
    SHA256((<span class="ck">const uint8_t</span> *)submitted_key, strlen(submitted_key), computed_hash);

    <span class="ck">char</span> computed_hex[<span class="cn">65</span>];
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i < <span class="cn">32</span>; i++)
        sprintf(computed_hex + i*<span class="cn">2</span>, <span class="cs">"%02x"</span>, computed_hash[i]);
    computed_hex[<span class="cn">64</span>] = <span class="cs">'\0'</span>;

    <span class="cm">/* Constant-time comparison — prevent timing attacks */</span>
    <span class="ck">return</span> CRYPTO_memcmp(computed_hex, stored_hash_hex, <span class="cn">64</span>) == <span class="cn">0</span>;
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="ck">char</span> key[<span class="cn">80</span>], prefix[<span class="cn">9</span>], hash_hex[<span class="cn">65</span>];
    generate_api_key(key, <span class="ck">sizeof</span>(key), prefix, hash_hex);

    printf(<span class="cs">"API Key (show user ONCE): %s\n"</span>, key);
    printf(<span class="cs">"Store in DB - prefix: %s\n"</span>, prefix);
    printf(<span class="cs">"Store in DB - hash:   %s\n"</span>, hash_hex);

    printf(<span class="cs">"Verify: %s\n"</span>, verify_api_key(key, hash_hex) ? <span class="cs">"OK"</span> : <span class="cs">"FAIL"</span>);
    printf(<span class="cs">"Verify (wrong): %s\n"</span>, verify_api_key(<span class="cs">"sk_live_wrong"</span>, hash_hex) ? <span class="cs">"OK"</span> : <span class="cs">"FAIL"</span>);
    <span class="ck">return</span> <span class="cn">0</span>;
}
<span class="cm">/* gcc api_key.c -o api_key -lssl -lcrypto */</span>
</div>
  </div>
</div>

<div class="cp p-violet">
  <div class="cp-hdr">Argon2id password hashing with libsodium</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">#include</span> <span class="cs">&lt;sodium.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>

<span class="cm">/* Hash a password for storage */</span>
<span class="ck">int</span> <span class="cf">hash_password</span>(<span class="ck">const char</span> *password, <span class="ck">char</span> *hash_out)
{
    <span class="cm">/* hash_out must be crypto_pwhash_STRBYTES (128) bytes */</span>
    <span class="ck">if</span> (crypto_pwhash_str(
            hash_out,
            password, strlen(password),
            crypto_pwhash_OPSLIMIT_INTERACTIVE,   <span class="cm">/* 2 ops */</span>
            crypto_pwhash_MEMLIMIT_INTERACTIVE    <span class="cm">/* 64 MiB */</span>
        ) != <span class="cn">0</span>) {
        fprintf(stderr, <span class="cs">"hash failed: out of memory\n"</span>);
        <span class="ck">return</span> -<span class="cn">1</span>;
    }
    <span class="ck">return</span> <span class="cn">0</span>;
}

<span class="cm">/* Verify a password against stored hash */</span>
<span class="ck">int</span> <span class="cf">verify_password</span>(<span class="ck">const char</span> *stored_hash, <span class="ck">const char</span> *password)
{
    <span class="ck">int</span> ret = crypto_pwhash_str_verify(
        stored_hash,
        password, strlen(password)
    );
    <span class="ck">return</span> ret == <span class="cn">0</span>;  <span class="cm">/* 0 = match */</span>
}

<span class="cm">/* Check if hash needs re-hash (cost factor upgraded) */</span>
<span class="ck">int</span> <span class="cf">needs_rehash</span>(<span class="ck">const char</span> *stored_hash)
{
    <span class="ck">return</span> crypto_pwhash_str_needs_rehash(
        stored_hash,
        crypto_pwhash_OPSLIMIT_INTERACTIVE,
        crypto_pwhash_MEMLIMIT_INTERACTIVE
    );
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="ck">if</span> (sodium_init() < <span class="cn">0</span>) { fprintf(stderr, <span class="cs">"sodium init failed\n"</span>); <span class="ck">return</span> <span class="cn">1</span>; }

    <span class="ck">char</span> stored_hash[crypto_pwhash_STRBYTES];
    <span class="ck">const char</span> *password = <span class="cs">"correct-horse-battery-staple"</span>;

    hash_password(password, stored_hash);
    printf(<span class="cs">"Stored: %.50s...\n"</span>, stored_hash);

    printf(<span class="cs">"Verify correct:  %s\n"</span>, verify_password(stored_hash, password) ? <span class="cs">"OK"</span> : <span class="cs">"FAIL"</span>);
    printf(<span class="cs">"Verify wrong:    %s\n"</span>, verify_password(stored_hash, <span class="cs">"wrongpassword"</span>) ? <span class="cs">"OK"</span> : <span class="cs">"FAIL"</span>);
    printf(<span class="cs">"Needs rehash:    %s\n"</span>, needs_rehash(stored_hash) ? <span class="cs">"yes"</span> : <span class="cs">"no"</span>);
    <span class="ck">return</span> <span class="cn">0</span>;
}
<span class="cm">/* gcc argon2_demo.c -o argon2_demo -lsodium */</span>
</div>
    <div class="note">After a successful login, call <code>needs_rehash()</code> — if true, transparently re-hash the plaintext password (which you have in memory at login time only) and update the DB. This handles algorithm upgrades without forcing password resets.</div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">Session ID generation — CSPRNG in C</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">#include</span> <span class="cs">&lt;openssl/rand.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>

<span class="cm">/* Generate 128-bit session ID as 32-char hex string */</span>
<span class="ck">int</span> <span class="cf">generate_session_id</span>(<span class="ck">char</span> *out)  <span class="cm">/* out: 33+ bytes */</span>
{
    <span class="cn">uint8_t</span> raw[<span class="cn">16</span>];
    <span class="ck">if</span> (RAND_bytes(raw, <span class="ck">sizeof</span>(raw)) != <span class="cn">1</span>) <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* CSPRNG failure */</span>

    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i < <span class="cn">16</span>; i++)
        sprintf(out + i*<span class="cn">2</span>, <span class="cs">"%02x"</span>, raw[i]);
    out[<span class="cn">32</span>] = <span class="cs">'\0'</span>;
    <span class="ck">return</span> <span class="cn">0</span>;
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="ck">char</span> sid[<span class="cn">33</span>];
    generate_session_id(sid);
    printf(<span class="cs">"Session ID: %s\n"</span>, sid);
    <span class="ck">return</span> <span class="cn">0</span>;
}
<span class="cm">/* gcc session_id.c -o session_id -lssl -lcrypto */</span>
</div>
    <div class="warn">Never use <code>rand()</code>, <code>srand(time(NULL))</code>, or sequential counters for session IDs. These are predictable. Only use a CSPRNG: <code>RAND_bytes()</code> (OpenSSL), <code>randombytes_buf()</code> (libsodium), or <code>/dev/urandom</code> directly.</div>
  </div>
</div>

</div><!-- /impl -->

<!-- ═══════════════════════ LABS ═══════════════════════ -->
<div class="tab-pane" id="tab-labs">

<div class="lab-box">
  <div class="lab-hdr">Lab 1 — JWT from scratch in C</div>
  <div class="lab-body">
    <strong>Goal:</strong> Implement JWT sign, verify, and claim extraction entirely in C using OpenSSL. No external JWT library.
    <div class="lab-step"><span class="sn">1</span><div>Create a file <code>jwt.c</code>. Implement <code>base64url_encode()</code> and <code>base64url_decode()</code>.</div></div>
    <div class="lab-step"><span class="sn">2</span><div>Implement <code>jwt_sign_hs256(payload_json, secret) → token_string</code>. The header is fixed as <code>{"alg":"HS256","typ":"JWT"}</code>.</div></div>
    <div class="lab-step"><span class="sn">3</span><div>Implement <code>jwt_verify_hs256(token, secret, payload_out)</code> — splits on dots, recomputes HMAC, constant-time compares, extracts payload.</div></div>
    <div class="lab-step"><span class="sn">4</span><div>Implement basic JSON claim extraction: <code>jwt_get_claim(payload, "exp") → string</code> using simple string parsing (no JSON library).</div></div>
    <div class="lab-step"><span class="sn">5</span><div>Test: sign a token with <code>exp = now + 60</code>. Verify it passes. Modify one byte of the token. Verify it fails. Advance time past expiry. Verify expiry check fails.</div></div>
    <div class="lab-step"><span class="sn">6</span><div><strong>Security test:</strong> craft a token with <code>"alg":"none"</code> and no signature. Ensure your verifier rejects it.</div></div>
    <strong>Build:</strong>
<div class="cb">gcc -Wall -Wextra jwt.c -o jwt -lssl -lcrypto
./jwt</div>
    <div class="note">Decode any token at jwt.io to verify your base64url encoding is correct.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">Lab 2 — Password hashing benchmark and upgrade path</div>
  <div class="lab-body">
    <strong>Goal:</strong> Understand real-world performance of bcrypt vs Argon2id; implement transparent rehash-on-login.
    <div class="lab-step"><span class="sn">1</span><div>Install libsodium: <code>sudo apt install libsodium-dev</code></div></div>
    <div class="lab-step"><span class="sn">2</span><div>Write a benchmark that hashes "password123" 10 times each with:
      <ul style="margin-top:.3rem;padding-left:1.2rem">
        <li>SHA-256 (baseline — show why it's wrong)</li>
        <li>Argon2id INTERACTIVE params</li>
        <li>Argon2id MODERATE params</li>
        <li>Argon2id SENSITIVE params</li>
      </ul>
      Print average time per hash.
    </div></div>
    <div class="lab-step"><span class="sn">3</span><div>Simulate a "DB" (array of structs) with 5 users. Hash their passwords with Argon2id INTERACTIVE params and store.</div></div>
    <div class="lab-step"><span class="sn">4</span><div>Simulate login: given username + plaintext password, verify and check <code>needs_rehash()</code>.</div></div>
    <div class="lab-step"><span class="sn">5</span><div>Upgrade: change the params to MODERATE. Re-run login loop — show that users whose hashes used old params get transparently re-hashed on next login.</div></div>
    <strong>Build:</strong>
<div class="cb">gcc -Wall pwhash_bench.c -o pwhash_bench -lsodium
./pwhash_bench</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">Lab 3 — API key system with PostgreSQL</div>
  <div class="lab-body">
    <strong>Goal:</strong> Build a complete API key issuance and verification system backed by PostgreSQL and libpq.
    <div class="lab-step"><span class="sn">1</span><div>Create the schema from the OAuth2 tab (api_keys table). Run migrations with psql.</div></div>
    <div class="lab-step"><span class="sn">2</span><div>Write <code>apikey_issue(user_id, name, scopes[]) → key_string</code>:
      <ul style="margin-top:.3rem;padding-left:1.2rem">
        <li>Generate key: <code>sk_test_</code> + 32 random bytes hex</li>
        <li>Compute SHA-256 hash</li>
        <li>Insert (prefix, hash, user_id, name, scopes) into api_keys</li>
        <li>Return the full key string (only time it's visible)</li>
      </ul>
    </div></div>
    <div class="lab-step"><span class="sn">3</span><div>Write <code>apikey_verify(submitted_key) → {user_id, scopes} or NULL</code>:
      <ul style="margin-top:.3rem;padding-left:1.2rem">
        <li>Extract prefix (first 8 chars after <code>sk_test_</code>)</li>
        <li>Query: <code>SELECT ... FROM api_keys WHERE prefix=$1 AND revoked_at IS NULL</code></li>
        <li>Compute hash of submitted key, constant-time compare with stored hash</li>
        <li>Update last_used timestamp</li>
        <li>Return user context on match</li>
      </ul>
    </div></div>
    <div class="lab-step"><span class="sn">4</span><div>Write <code>apikey_revoke(key_id)</code> — sets revoked_at = now().</div></div>
    <div class="lab-step"><span class="sn">5</span><div>Test: issue key, verify it works, verify a wrong key fails, revoke key, verify it's rejected.</div></div>
    <strong>Build:</strong>
<div class="cb">gcc apikey.c -o apikey -lssl -lcrypto -lpq
./apikey</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">Lab 4 — RBAC middleware in a minimal HTTP server</div>
  <div class="lab-body">
    <strong>Goal:</strong> Add JWT authentication and RBAC authorization middleware to a minimal HTTP server.
    <div class="lab-step"><span class="sn">1</span><div>Start with a minimal C HTTP server (see M03 reference) with routes: <code>POST /login</code>, <code>GET /api/invoices</code>, <code>DELETE /api/invoices/:id</code>, <code>GET /api/admin/users</code>.</div></div>
    <div class="lab-step"><span class="sn">2</span><div>Implement <code>POST /login</code>: accepts JSON <code>{username, password}</code>. Verifies against hardcoded users (Argon2id hashes). Returns JWT with <code>sub</code>, <code>role</code>, <code>exp=now+900</code> (15 min).</div></div>
    <div class="lab-step"><span class="sn">3</span><div>Implement JWT middleware: extracts <code>Authorization: Bearer &lt;token&gt;</code> header, verifies signature, checks <code>exp</code>, populates request context with <code>user_id</code> and <code>role</code>. Returns 401 if missing/invalid.</div></div>
    <div class="lab-step"><span class="sn">4</span><div>Add RBAC checks:
      <ul style="margin-top:.3rem;padding-left:1.2rem">
        <li><code>GET /api/invoices</code> — roles: viewer, editor, admin</li>
        <li><code>DELETE /api/invoices/:id</code> — roles: editor, admin only</li>
        <li><code>GET /api/admin/users</code> — role: admin only → returns 403 for others</li>
      </ul>
    </div></div>
    <div class="lab-step"><span class="sn">5</span><div>Test with curl:
<div class="cb">TOKEN=$(curl -s -X POST localhost:8080/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"alice","password":"hunter2"}' | jq -r .token)

curl -H "Authorization: Bearer $TOKEN" localhost:8080/api/invoices
curl -X DELETE -H "Authorization: Bearer $TOKEN" localhost:8080/api/invoices/1
curl -H "Authorization: Bearer $TOKEN" localhost:8080/api/admin/users  # expect 403</div>
    </div></div>
    <div class="lab-step"><span class="sn">6</span><div><strong>Bonus:</strong> Add <code>POST /refresh</code> with a refresh token (store in Redis-like in-memory map), implement rotation and reuse detection.</div></div>
  </div>
</div>

</div><!-- /labs -->

<!-- ═══════════════════════ CHECKLIST ═══════════════════════ -->
<div class="tab-pane" id="tab-checklist">

<div class="cp p-red">
  <div class="cp-hdr">Phase 3 concept checklist</div>
  <div class="cp-body">
    <p style="margin-bottom:.8rem;font-size:.88rem;color:#64748b">Check each item after you can explain it clearly and implement it without referencing notes.</p>

    <div class="ch-section-label" style="font-size:.8rem;font-weight:700;color:#ef4444;margin-bottom:.4rem">Sessions &amp; Cookies</div>
    <ul class="cl">
      <li>Session ID is ≥128-bit CSPRNG output, hex or base64url encoded, never predictable</li>
      <li>Session ID regenerated on login — prevents session fixation attacks</li>
      <li>Session stored server-side (Redis) with TTL; client only holds the ID</li>
      <li>Cookie attributes: <code>HttpOnly</code> (no JS access), <code>Secure</code> (HTTPS only), <code>SameSite=Strict</code> (no CSRF)</li>
      <li>Logout deletes session from Redis, doesn't just expire the cookie</li>
      <li>CSRF: SameSite=Strict prevents cross-site request forgery for modern browsers</li>
    </ul>

    <div class="ch-section-label" style="font-size:.8rem;font-weight:700;color:#ef4444;margin:.8rem 0 .4rem">JWT</div>
    <ul class="cl">
      <li>JWT = base64url(header) + "." + base64url(payload) + "." + base64url(signature)</li>
      <li>Payload is NOT encrypted — only signed. Never store secrets in payload.</li>
      <li>Standard claims: <code>iss</code>, <code>sub</code>, <code>aud</code>, <code>exp</code>, <code>nbf</code>, <code>iat</code>, <code>jti</code></li>
      <li>HS256 = symmetric HMAC; RS256/ES256 = asymmetric; hardcode algorithm in verifier</li>
      <li>Always verify: signature, <code>exp</code>, <code>nbf</code>, <code>iss</code>, <code>aud</code></li>
      <li>Never accept <code>alg:none</code> — explicitly reject it in your verifier</li>
      <li>Access token: 15min, stateless. Refresh token: 7-30d, stored in DB for revocation</li>
      <li>Refresh token rotation: each use issues a new token; reuse detection revokes family</li>
    </ul>

    <div class="ch-section-label" style="font-size:.8rem;font-weight:700;color:#ef4444;margin:.8rem 0 .4rem">OAuth2 &amp; API Keys</div>
    <ul class="cl">
      <li>OAuth2 = authorization framework (delegation), not authentication</li>
      <li>PKCE: code_verifier → SHA-256 → code_challenge; prevents authorization code interception</li>
      <li>State parameter on OAuth callback prevents CSRF</li>
      <li>redirect_uri must exactly match registered URI (open redirect prevention)</li>
      <li>API keys: generate with CSPRNG, store SHA-256 hash in DB, show plaintext once</li>
      <li>API key lookup: prefix column (fast) + constant-time hash comparison</li>
    </ul>

    <div class="ch-section-label" style="font-size:.8rem;font-weight:700;color:#ef4444;margin:.8rem 0 .4rem">Authorization</div>
    <ul class="cl">
      <li>RBAC: users → roles → permissions; simple, auditable, works for most systems</li>
      <li>ABAC: policy evaluates subject + resource + action + environment attributes</li>
      <li>Always check resource ownership (IDOR prevention): <code>WHERE user_id = $current</code></li>
      <li>JWT role/permission claims go stale — short access token TTL limits the window</li>
    </ul>

    <div class="ch-section-label" style="font-size:.8rem;font-weight:700;color:#ef4444;margin:.8rem 0 .4rem">Password Security</div>
    <ul class="cl">
      <li>Never use MD5/SHA-256 for passwords — they're too fast (&gt;billion/sec on GPU)</li>
      <li>Argon2id (OWASP recommended): memory-hard + time-hard + side-channel resistant</li>
      <li>bcrypt: cost factor 12+, ~100ms target; max 72 bytes input</li>
      <li>Use constant-time comparison for all security tokens (CRYPTO_memcmp / sodium_memcmp)</li>
      <li>Implement transparent rehash-on-login for cost factor upgrades</li>
      <li>Pepper = secret mixed in before hashing; stored in secrets manager, not DB</li>
    </ul>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">Common mistakes to avoid</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Mistake</th><th>Consequence</th><th>Correct approach</th></tr></thead>
      <tbody>
        <tr><td>JWT in localStorage</td><td>XSS can steal token → full account takeover</td><td>Memory (SPA) or HttpOnly cookie</td></tr>
        <tr><td>Missing <code>exp</code> check</td><td>Expired tokens valid forever</td><td>Always validate all standard claims</td></tr>
        <tr><td>Trusting <code>alg</code> header</td><td>alg:none bypass, algorithm confusion</td><td>Hardcode expected algorithm</td></tr>
        <tr><td>Weak HS256 secret</td><td>Offline brute-force from any valid token</td><td>32+ bytes from CSPRNG</td></tr>
        <tr><td>MD5/SHA-256 for passwords</td><td>Full crack in hours after DB breach</td><td>Argon2id or bcrypt</td></tr>
        <tr><td>Non-constant-time compare</td><td>Timing oracle reveals token byte-by-byte</td><td>CRYPTO_memcmp / sodium_memcmp</td></tr>
        <tr><td>No session fixation protection</td><td>Attacker elevates pre-auth session</td><td>Regenerate session ID on login</td></tr>
        <tr><td>Missing IDOR check</td><td>User A reads/writes user B's data</td><td>Always scope queries to current user</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /checklist -->

<div class="mod-nav">
  <a href="/learning/backend/m06-sql-indexing/" class="nb">← M06 SQL &amp; Indexing</a>
  <a href="/learning/backend/backend-roadmap/" class="nb">↑ Back to Roadmap</a>
  <a href="/learning/backend/m11-concurrency/" class="nb">M11 Concurrency →</a>
</div>

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}
</script>
