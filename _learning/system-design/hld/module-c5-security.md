---
layout: default
title: "Module C5: Security Architecture"
permalink: /learning/system-design/hld/module-c5-security/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-c5.css" | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:ital,wght@0,300;0,400;0,600;1,400&display=swap" rel="stylesheet">

<header>
  <div class="hdr-bar"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK C · MODULE C5 · WEEK 29</span>
    <span>OAUTH2 · JWT · MTLS · ZERO-TRUST · SECRETS · OWASP · DDOS</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">// TRACK C · ADVANCED TOPICS · FINAL MODULE</div>
      <h1>Security<br><span class="acc">Architecture</span></h1>
      <div class="hdr-sub">OAUTH2 / OIDC · JWT INTERNALS · MTLS · ZERO-TRUST<br>SECRETS MANAGEMENT · OWASP TOP 10 · DDOS MITIGATION</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">OAuth2</div><div class="hs-l">AUTH STANDARD</div></div>
      <div class="hs"><div class="hs-v">10</div><div class="hs-l">OWASP RISKS</div></div>
      <div class="hs"><div class="hs-v">Zero</div><div class="hs-l">IMPLICIT TRUST</div></div>
      <div class="hs"><div class="hs-v">C5</div><div class="hs-l">FINAL MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--red)">OAuth2 / OIDC</div>
    <div class="tg" style="color:var(--gold)">JWT</div>
    <div class="tg" style="color:var(--cya)">mTLS</div>
    <div class="tg" style="color:var(--grn)">Zero-Trust</div>
    <div class="tg" style="color:var(--pur)">Secrets Mgmt</div>
    <div class="tg" style="color:var(--ora)">OWASP Top 10</div>
    <div class="tg" style="color:var(--blu)">DDoS / Rate Limit</div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="show('authn',this)">AuthN vs AuthZ</div>
  <div class="nt" onclick="show('oauth',this)">OAuth2 / OIDC</div>
  <div class="nt" onclick="show('jwt',this)">JWT Deep Dive</div>
  <div class="nt" onclick="show('mtls',this)">mTLS</div>
  <div class="nt" onclick="show('zerotrust',this)">Zero-Trust</div>
  <div class="nt" onclick="show('secrets',this)">Secrets Mgmt</div>
  <div class="nt" onclick="show('owasp',this)">OWASP Top 10</div>
  <div class="nt" onclick="show('ratelimit',this)">Rate Limit / DDoS</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- AUTHN -->
<div class="view active" id="view-authn">
  <div class="sh">Authentication vs Authorization</div>
  <div class="sr">Two separate checks — conflating them is the root cause of access control bugs</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:14px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--red);padding:16px">
      <div style="font-family:'Cinzel',serif;font-size:17px;font-weight:700;color:var(--red);margin-bottom:4px">Authentication</div>
      <div style="font-family:'Courier Prime',monospace;font-size:8px;letter-spacing:2px;color:var(--muted);margin-bottom:10px">WHO ARE YOU? PROVE YOUR IDENTITY.</div>
      <div style="font-size:13px;color:var(--text);line-height:1.65;margin-bottom:8px">Validates that the caller is who they claim to be. Happens once per session or token issuance.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9.5px;color:var(--sub);line-height:1.85">→ Passwords + MFA<br>→ OAuth2 tokens<br>→ mTLS certificates<br>→ "The user is logged in"</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--gold);padding:16px">
      <div style="font-family:'Cinzel',serif;font-size:17px;font-weight:700;color:var(--gold);margin-bottom:4px">Authorization</div>
      <div style="font-family:'Courier Prime',monospace;font-size:8px;letter-spacing:2px;color:var(--muted);margin-bottom:10px">WHAT CAN YOU DO? CHECK PERMISSIONS.</div>
      <div style="font-size:13px;color:var(--text);line-height:1.65;margin-bottom:8px">Validates that the authenticated caller has permission for this specific action on this specific resource. Happens on every request.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9.5px;color:var(--sub);line-height:1.85">→ RBAC / ABAC / ACLs<br>→ OAuth2 scopes<br>→ "User can delete order #123"<br>→ Must check on EVERY endpoint</div>
    </div>
  </div>
  <div class="al red"><em>Common mistake:</em> checking authentication but not authorization. A user who is logged in can call any endpoint — even ones that belong to other users. Always check: (1) is this request authenticated? (2) does this principal have permission for THIS specific resource? Missing step 2 = IDOR (Insecure Direct Object Reference) = OWASP #1.</div>
</div>

<!-- OAUTH -->
<div class="view" id="view-oauth">
  <div class="sh">OAuth2 & OpenID Connect</div>
  <div class="sr">OAuth2 delegates authorization — OIDC adds identity on top</div>
  <div class="oauth-flow">
    <div class="of-label">// AUTHORIZATION CODE + PKCE FLOW — the correct flow for web & mobile</div>
    <div class="of-step"><div class="of-num">1</div><div class="of-body">User clicks "Login with Google." App generates <span>code_verifier</span> (random 43–128 chars) and <span>code_challenge</span> = BASE64URL(SHA256(code_verifier)).</div></div>
    <div class="of-step"><div class="of-num">2</div><div class="of-body">App redirects browser to Google: <span>/authorize?client_id=...&redirect_uri=...&scope=openid+email&state=xyz&code_challenge=...&code_challenge_method=S256</span></div></div>
    <div class="of-step"><div class="of-num">3</div><div class="of-body">User authenticates at Google (password + MFA). User consents to requested scopes. Google redirects back to app's <span>redirect_uri</span> with a short-lived <span>authorization_code</span> and the original <span>state</span>.</div></div>
    <div class="of-step"><div class="of-num">4</div><div class="of-body">App verifies <span>state</span> matches (CSRF protection). App POSTs to <span>/token</span>: <em>{ code, code_verifier, client_id, redirect_uri, grant_type=authorization_code }</em></div></div>
    <div class="of-step"><div class="of-num">5</div><div class="of-body">Google verifies code_verifier matches code_challenge. Returns: <span>access_token</span> (15min), <span>refresh_token</span> (14 days), <span>id_token</span> (JWT with user claims).</div></div>
    <div class="of-step"><div class="of-num">6</div><div class="of-body">App validates <span>id_token</span> signature + claims (iss, aud, exp, nonce). Stores refresh_token in httpOnly cookie. Keeps access_token in memory only (not localStorage).</div></div>
    <div class="of-step"><div class="of-num">7</div><div class="of-body">App calls APIs with <span>Authorization: Bearer &lt;access_token&gt;</span>. API verifies token signature using Google's public JWKS keys — no round-trip to Google needed.</div></div>
    <div class="of-step"><div class="of-num">8</div><div class="of-body">Access token expires. App uses <span>refresh_token</span> to silently get a new access token via POST /token with grant_type=refresh_token. User never sees this.</div></div>
  </div>
  <div class="al gold"><em>Why PKCE?</em> On mobile, the OS can intercept redirects from any app. Without PKCE, a malicious app could steal the authorization code from the redirect and exchange it for tokens. PKCE binds the code to a verifier that only the legitimate app knows — stolen codes are useless without code_verifier.</div>
</div>

<!-- JWT -->
<div class="view" id="view-jwt">
  <div class="sh">JWT Deep Dive</div>
  <div class="sr">Base64URL encoded, NOT encrypted — never put secrets in the payload</div>
  <div class="jwt-parts">
    <div class="jp" style="background:rgba(80,144,232,.04)">
      <div class="jp-name" style="color:var(--blu)">Header</div>
      <div class="jp-sub" style="color:var(--blu)">ALGORITHM + KEY ID</div>
      <div class="jp-body">{<br>  "alg": "RS256",<br>  "typ": "JWT",<br>  "kid": "key-id-1"<br>}<br><br><span style="color:var(--sub)">kid → selects which public key<br>to use from JWKS endpoint</span></div>
    </div>
    <div class="jp" style="background:rgba(200,160,64,.04)">
      <div class="jp-name" style="color:var(--gold)">Payload</div>
      <div class="jp-sub" style="color:var(--gold)">CLAIMS — VERIFY ALL</div>
      <div class="jp-body">{<br>  "sub": "user_123",<br>  "iss": "auth.co.com",<br>  "aud": "api.co.com",<br>  "exp": 1700000000,<br>  "jti": "uuid-abc",<br>  "roles": ["admin"]<br>}</div>
    </div>
    <div class="jp" style="background:rgba(64,216,120,.04)">
      <div class="jp-name" style="color:var(--grn)">Signature</div>
      <div class="jp-sub" style="color:var(--grn)">RSA-SHA256 SIGNED</div>
      <div class="jp-body">RSA_SHA256(<br>  base64url(header)<br>  + "."<br>  + base64url(payload),<br>  private_key<br>)<br><br><span style="color:var(--sub)">Verify with public key.<br>Only auth server can mint.</span></div>
    </div>
  </div>
  <div class="vuln-grid">
    <div class="vul">
      <div class="vul-name">alg:none Attack</div>
      <div class="vul-body">Attacker changes header to <code style="font-family:'Courier Prime',monospace;color:var(--yel)">"alg":"none"</code>, strips the signature. Server accepts if it doesn't enforce algorithm whitelist.</div>
      <div class="vul-fix">Fix: whitelist allowed algorithms.<br>Reject any token with alg=none.<br>Never trust the header's alg claim blindly.</div>
    </div>
    <div class="vul">
      <div class="vul-name">HS256 Key Confusion</div>
      <div class="vul-body">If server accepts both RS256 and HS256, attacker signs a token using HS256 with the server's public key as the HMAC secret. Server verifies it using its own public key.</div>
      <div class="vul-fix">Fix: validate algorithm strictly.<br>Never allow algorithm negotiation.<br>Use RS256 only in distributed systems.</div>
    </div>
    <div class="vul">
      <div class="vul-name">Missing exp Validation</div>
      <div class="vul-body">If expiry is not checked, tokens work forever. A token issued 2 years ago for a deleted account still grants access.</div>
      <div class="vul-fix">Fix: always check exp &gt; now().<br>Allow 5-min clock skew tolerance.<br>Keep access tokens short (15 min).</div>
    </div>
    <div class="vul">
      <div class="vul-name">Sensitive Data in Payload</div>
      <div class="vul-body">JWT payload is Base64URL encoded — it is NOT encrypted. Anyone who intercepts the token can read the payload. Passwords, SSNs, PII stored there are exposed.</div>
      <div class="vul-fix">Fix: put only non-sensitive claims.<br>Use JWE (encrypted JWT) if confidentiality needed.<br>Never put passwords, PII, or secrets.</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">RS256 vs HS256 — why RS256 wins in distributed systems<span class="cb-l">ALGORITHM CHOICE</span></div>
<pre class="c"><span class="cm">// HS256 (HMAC-SHA256) — SYMMETRIC</span>
<span class="cm">// Same key used to sign AND verify.</span>
<span class="cm">// Problem: every service that verifies must have the secret key.</span>
<span class="cm">// If any service is compromised → attacker can forge any token.</span>
token = jwt.<span class="fn">sign</span>(payload, <span class="str">"shared-secret-key"</span>, { algorithm: <span class="str">"HS256"</span> })
jwt.<span class="fn">verify</span>(token, <span class="str">"shared-secret-key"</span>)   <span class="cm">← every service needs this key</span>

<span class="cm">// RS256 (RSA-SHA256) — ASYMMETRIC ← PREFERRED</span>
<span class="cm">// Auth server signs with PRIVATE key (kept secret, only auth server has it).</span>
<span class="cm">// All services verify with PUBLIC key (published at JWKS endpoint).</span>
<span class="cm">// Compromise of any service → cannot forge tokens (no private key).</span>
token = jwt.<span class="fn">sign</span>(payload, private_key, { algorithm: <span class="str">"RS256"</span>, keyid: <span class="str">"key-1"</span> })
public_key = <span class="fn">fetch</span>(<span class="str">"https://auth.co.com/.well-known/jwks.json"</span>)
jwt.<span class="fn">verify</span>(token, public_key, {
  algorithms: [<span class="str">"RS256"</span>],     <span class="cm">← whitelist ONLY RS256</span>
  audience: <span class="str">"api.co.com"</span>,   <span class="cm">← verify aud claim</span>
  issuer: <span class="str">"auth.co.com"</span>    <span class="cm">← verify iss claim</span>
})</pre>
  </div>
</div>

<!-- MTLS -->
<div class="view" id="view-mtls">
  <div class="sh">mTLS — Mutual TLS</div>
  <div class="sr">Service-to-service authentication — both sides prove identity via certificates</div>
  <div class="cb"><div class="cb-top">mTLS handshake — what happens under the hood<span class="cb-l">TLS HANDSHAKE</span></div>
<pre class="c"><span class="cm">// Regular TLS: only CLIENT verifies server certificate.</span>
<span class="cm">// mTLS: BOTH sides verify each other. Used for service-to-service auth.</span>

Client (order-service)            Server (payment-service)
    |                                    |
    |--- ClientHello ------------------>|
    |<-- ServerHello + ServerCert ------|  <span class="cm">← server sends its cert</span>
    |    (CN=payment-service,           |
    |     issued by internal-CA)        |
    |                                   |
    |--- ClientCert ------------------->|  <span class="cm">← client sends its cert</span>
    |    (CN=order-service,             |
    |     issued by internal-CA)        |
    |                                   |
    <span class="cm">// Both sides verify:</span>
    <span class="cm">// 1. Certificate signed by trusted internal CA?</span>
    <span class="cm">// 2. Certificate not expired?</span>
    <span class="cm">// 3. Certificate not in CRL (revoked)?</span>
    <span class="cm">// 4. Subject (CN) matches expected service name?</span>
    |                                   |
    |=== Encrypted channel established ==|
    |--- GET /charge (HTTP/1.1) ------->|  <span class="cm">← now authorized</span>

<span class="cm">// Service mesh (Istio) automates all of this:</span>
<span class="cm">// Envoy sidecar handles mTLS transparently.</span>
<span class="cm">// Policy: "order-service → payment-service: ALLOW"</span>
<span class="cm">//         "frontend → payment-service: DENY"</span>
<span class="cm">// Your application code calls http://payment-service/charge</span>
<span class="cm">// Envoy sidecar upgrades to mTLS automatically.</span>

<span class="cm">// Cert rotation (SPIRE):</span>
<span class="cm">// SPIRE issues short-lived SVIDs (24–72 hrs) to every workload.</span>
<span class="cm">// Automatic rotation before expiry — zero manual cert management.</span></pre>
  </div>
  <div class="al grn"><em>Why mTLS over API keys for service-to-service?</em> API keys are static strings — once compromised they're valid until manually rotated. mTLS certificates are short-lived (24–72 hours), automatically rotated, cryptographically bound to a specific workload, and revocable via CRL. A compromised cert is useless after its short TTL. A compromised API key may go undetected for months.</div>
</div>

<!-- ZERO TRUST -->
<div class="view" id="view-zerotrust">
  <div class="sh">Zero-Trust Architecture</div>
  <div class="sr">Never trust, always verify — treat every request as if the attacker is already inside</div>
  <div class="zt-grid">
    <div class="zt" style="border-top-color:var(--red)">
      <div class="zt-icon">🪪</div>
      <div class="zt-name" style="color:var(--red)">Identity</div>
      <div class="zt-body">MFA for users. mTLS + SPIFFE for services. Every principal verified.</div>
    </div>
    <div class="zt" style="border-top-color:var(--ora)">
      <div class="zt-icon">💻</div>
      <div class="zt-name" style="color:var(--ora)">Device</div>
      <div class="zt-body">Posture checks: patched, encrypted, MDM-enrolled before access.</div>
    </div>
    <div class="zt" style="border-top-color:var(--yel)">
      <div class="zt-icon">🌐</div>
      <div class="zt-name" style="color:var(--yel)">Network</div>
      <div class="zt-body">Microsegmentation. Explicit allow rules. No flat network trust.</div>
    </div>
    <div class="zt" style="border-top-color:var(--grn)">
      <div class="zt-icon">⚙️</div>
      <div class="zt-name" style="color:var(--grn)">Application</div>
      <div class="zt-body">RBAC at app layer. Fine-grained AuthZ. Scoped tokens per action.</div>
    </div>
    <div class="zt" style="border-top-color:var(--blu)">
      <div class="zt-icon">🔐</div>
      <div class="zt-name" style="color:var(--blu)">Data</div>
      <div class="zt-body">Encrypted at rest + in transit. Classification. Per-user KMS keys.</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Microsegmentation — explicit allow vs flat network<span class="cb-l">K8S NETWORK POLICY</span></div>
<pre class="c"><span class="cm">// Flat network (DEFAULT, DANGEROUS):</span>
<span class="cm">// Any pod can call any pod. Compromised frontend → calls payment DB directly.</span>

<span class="cm">// Microsegmented (ZERO-TRUST):</span>
<span class="cm">// All traffic denied by default. Explicit allows only.</span>

<span class="kw">apiVersion</span>: networking.k8s.io/v1
<span class="kw">kind</span>: NetworkPolicy
<span class="kw">metadata</span>:
  <span class="kw">name</span>: payment-service-policy
<span class="kw">spec</span>:
  <span class="kw">podSelector</span>:
    <span class="kw">matchLabels</span>: { app: payment-service }
  <span class="kw">policyTypes</span>: [Ingress, Egress]
  <span class="kw">ingress</span>:
  - <span class="kw">from</span>:
    - <span class="kw">podSelector</span>:
        <span class="kw">matchLabels</span>: { app: order-service }  <span class="cm">← ONLY order-service may call payment</span>
    <span class="kw">ports</span>: [{ port: 8080 }]
  <span class="kw">egress</span>:
  - <span class="kw">to</span>:
    - <span class="kw">podSelector</span>:
        <span class="kw">matchLabels</span>: { app: payment-db }     <span class="cm">← ONLY payment-db may be called</span>

<span class="cm">// Blast radius comparison:</span>
<span class="cm">// Without Zero-Trust: compromised transcoding pod → access to payment DB, user DB, secrets</span>
<span class="cm">// With Zero-Trust: compromised transcoding pod → can only reach video-storage S3 bucket</span>
<span class="cm">//                  (its only explicit allow). Attacker is contained.</span></pre>
  </div>
</div>

<!-- SECRETS -->
<div class="view" id="view-secrets">
  <div class="sh">Secrets Management</div>
  <div class="sr">Static long-lived secrets are a liability — dynamic short-lived credentials are the goal</div>
  <div class="anti-list">
    <div class="anti"><div class="anti-icon" style="color:var(--red)">✗</div><div class="anti-body"><strong>Hardcoded in source code</strong> — git history is permanent. Even if you delete the file, the secret is in every clone, fork, and CI log. Secret scanners (GitGuardian, truffleHog) find these instantly.</div></div>
    <div class="anti"><div class="anti-icon" style="color:var(--red)">✗</div><div class="anti-body"><strong>In environment variables in Dockerfile / k8s YAML</strong> — anyone who can read the pod spec can read the secret. These files get committed, shared, and logged.</div></div>
    <div class="anti"><div class="anti-icon" style="color:var(--red)">✗</div><div class="anti-body"><strong>Never rotated</strong> — "it's been working for 3 years." Long-lived static secrets accumulate risk. Rotate all secrets at fixed intervals and immediately on any suspected breach.</div></div>
    <div class="anti"><div class="anti-icon" style="color:var(--red)">✗</div><div class="anti-body"><strong>Same secret across environments</strong> — a dev breach should never compromise production. Separate secrets per environment, separate KMS keys, separate rotation schedules.</div></div>
  </div>
  <div class="cb"><div class="cb-top">HashiCorp Vault dynamic secrets — no long-lived credentials<span class="cb-l">VAULT</span></div>
<pre class="c"><span class="cm">// STATIC secret (dangerous): long-lived DB password stored as a secret</span>
<span class="cm">// If the secret leaks: valid forever until manually rotated.</span>

<span class="cm">// DYNAMIC secret (Vault): Vault generates credentials per-request, with TTL</span>

<span class="cm">// App startup: request DB credentials from Vault</span>
response = vault.<span class="fn">read</span>(<span class="str">"database/creds/my-role"</span>)
<span class="cm">// Vault generates: { username: "v-app-20250307-abc", password: "xyz", lease_ttl: "1h" }</span>
<span class="cm">// Vault creates this user in the DB with read permissions</span>
<span class="cm">// After 1 hour: Vault AUTOMATICALLY revokes the DB user</span>

db.<span class="fn">connect</span>(
  host=<span class="str">"db.internal"</span>,
  user=response.username,     <span class="cm">← temporary, unique to this app instance</span>
  password=response.password  <span class="cm">← expires in 1 hour</span>
)

<span class="cm">// App renews lease before expiry:</span>
vault.<span class="fn">renew</span>(response.lease_id)  <span class="cm">← extend by another hour</span>

<span class="cm">// Benefits:</span>
<span class="cm">// • No long-lived credentials → breach window is at most 1 hour</span>
<span class="cm">// • Full audit log: who requested what credential, when</span>
<span class="cm">// • Automatic cleanup: no orphaned credentials accumulate</span>
<span class="cm">// • Unique per instance: compromise of one pod ≠ compromise of all pods</span></pre>
  </div>
</div>

<!-- OWASP -->
<div class="view" id="view-owasp">
  <div class="sh">OWASP Top 10 (2021)</div>
  <div class="sr">Know these cold — they appear in every security-conscious system design interview</div>
  <div class="owasp-list">
    <div class="ow">
      <div class="ow-num" style="color:var(--red)">1</div>
      <div class="ow-body"><div class="ow-name">BROKEN ACCESS CONTROL</div><div class="ow-desc">IDOR: user accesses another user's data by changing an ID in the URL. Vertical escalation: user calls admin endpoints. Most common vuln in modern apps.</div><div class="ow-fix">Fix: check authorization on every request. Never trust client-supplied resource IDs without verifying ownership.</div></div>
    </div>
    <div class="ow">
      <div class="ow-num" style="color:var(--ora)">2</div>
      <div class="ow-body"><div class="ow-name">CRYPTOGRAPHIC FAILURES</div><div class="ow-desc">Passwords stored in plaintext or with MD5/SHA1 (broken). HTTP for sensitive data. Weak random number generation for tokens.</div><div class="ow-fix">Fix: bcrypt/Argon2 for passwords. AES-256 for data at rest. TLS 1.2+ everywhere. CSPRNG for tokens.</div></div>
    </div>
    <div class="ow">
      <div class="ow-num" style="color:var(--yel)">3</div>
      <div class="ow-body"><div class="ow-name">INJECTION (SQL, NoSQL, OS Commands)</div><div class="ow-desc">User input concatenated into queries. Input "1 OR 1=1 --" returns all users. Can lead to full DB dump, data deletion, or OS command execution.</div><div class="ow-fix">Fix: parameterized queries / prepared statements. NEVER concatenate user input into SQL strings.</div></div>
    </div>
    <div class="ow">
      <div class="ow-num" style="color:var(--grn)">5</div>
      <div class="ow-body"><div class="ow-name">SECURITY MISCONFIGURATION</div><div class="ow-desc">Default credentials, public S3 buckets, verbose error messages with stack traces, debug endpoints in production, unnecessary ports open.</div><div class="ow-fix">Fix: IaC security scanning (tfsec, checkov). Hardened default configs. Regular misconfiguration audits.</div></div>
    </div>
    <div class="ow">
      <div class="ow-num" style="color:var(--blu)">6</div>
      <div class="ow-body"><div class="ow-name">VULNERABLE COMPONENTS</div><div class="ow-desc">Log4Shell was in log4j — a transitive dependency. Attackers scan for known CVEs in common libraries. Your app is only as secure as its weakest dependency.</div><div class="ow-fix">Fix: Snyk, Dependabot, OWASP Dependency-Check in CI. Auto-PRs for security patches. SBOM (Software Bill of Materials).</div></div>
    </div>
    <div class="ow">
      <div class="ow-num" style="color:var(--pur)">10</div>
      <div class="ow-body"><div class="ow-name">SERVER-SIDE REQUEST FORGERY (SSRF)</div><div class="ow-desc">App fetches a URL from user input. Attacker supplies http://169.254.169.254/latest/meta-data/ → AWS metadata endpoint → IAM credentials → full cloud account access.</div><div class="ow-fix">Fix: whitelist allowed domains. Block internal IP ranges (169.254.x.x, 10.x.x.x). Use AWS IMDSv2 (requires session token, blocks simple SSRF).</div></div>
    </div>
  </div>
</div>

<!-- RATE LIMIT / DDOS -->
<div class="view" id="view-ratelimit">
  <div class="sh">Rate Limiting for Security & DDoS Mitigation</div>
  <div class="sr">Rate limiting prevents abuse — DDoS mitigation absorbs volumetric attacks</div>
  <div class="cb"><div class="cb-top">Security-focused rate limiting — brute force and credential stuffing prevention<span class="cb-l">REDIS</span></div>
<pre class="c"><span class="cm">// BRUTE FORCE on login endpoint:</span>
<span class="cm">// Without protection: attacker tries 10M passwords/second.</span>
<span class="kw">def</span> <span class="fn">check_login_rate_limit</span>(ip, user_id):
    <span class="cm"># Per-IP: 5 attempts per 15 minutes (stops distributed single-user attack)</span>
    ip_key = <span class="str">f"login:ip:{ip}"</span>
    ip_count = redis.<span class="fn">incr</span>(ip_key)
    <span class="kw">if</span> ip_count == <span class="hl">1</span>: redis.<span class="fn">expire</span>(ip_key, <span class="hl">900</span>)   <span class="cm"># 15 min window</span>
    <span class="kw">if</span> ip_count > <span class="hl">5</span>: <span class="kw">raise</span> TooManyRequests

    <span class="cm"># Per-user: 10 attempts per hour (stops distributed multi-IP attack)</span>
    user_key = <span class="str">f"login:user:{user_id}"</span>
    user_count = redis.<span class="fn">incr</span>(user_key)
    <span class="kw">if</span> user_count == <span class="hl">1</span>: redis.<span class="fn">expire</span>(user_key, <span class="hl">3600</span>)  <span class="cm"># 1 hour window</span>
    <span class="kw">if</span> user_count > <span class="hl">10</span>:
        <span class="fn">send_suspicious_activity_alert</span>(user_id)
        <span class="kw">raise</span> TooManyRequests

<span class="cm">// CREDENTIAL STUFFING (breached credentials list from other sites):</span>
<span class="cm">// Attacker uses many different IPs → per-IP limits ineffective.</span>
<span class="cm">// Fix: rate limit per user_id (not just IP). CAPTCHA after 3 failures.</span>
<span class="cm">// HIBP (Have I Been Pwned) check: reject passwords in known breach datasets.</span>
<span class="cm">// Device fingerprinting: flag new device + failed login → MFA challenge.</span>

<span class="cm">// DDoS mitigation layers:</span>
<span class="cm">// L3/4 volumetric (millions of packets): ISP BGP blackholing, AWS Shield Standard</span>
<span class="cm">// L7 application (HTTP flood): Cloudflare WAF, AWS WAF, rate limiting, CAPTCHA</span>
<span class="cm">// Anycast: Cloudflare has 200+ PoPs — attack absorbed at edge, never reaches origin</span></pre>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:12px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--red);padding:12px">
      <div style="font-family:'Courier Prime',monospace;font-size:9px;letter-spacing:1px;color:var(--red);margin-bottom:6px">L3/L4 VOLUMETRIC</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">Millions of packets/sec. Saturates bandwidth. BGP blackholing at ISP level. AWS Shield Standard (free) handles basic L3/4.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9px;color:var(--sub);line-height:1.7">Tools: AWS Shield,<br>Cloudflare Magic Transit,<br>Arbor/NETSCOUT</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--ora);padding:12px">
      <div style="font-family:'Courier Prime',monospace;font-size:9px;letter-spacing:1px;color:var(--ora);margin-bottom:6px">L7 APPLICATION</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">HTTP flood, slowloris, GET flood. WAF blocks known attack patterns. Rate limiting + CAPTCHA + bot detection.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9px;color:var(--sub);line-height:1.7">Tools: Cloudflare WAF,<br>AWS WAF, Akamai,<br>rate limiting</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--gold);padding:12px">
      <div style="font-family:'Courier Prime',monospace;font-size:9px;letter-spacing:1px;color:var(--gold);margin-bottom:6px">ANYCAST ABSORPTION</div>
      <div style="font-size:12px;color:var(--text);line-height:1.6;margin-bottom:6px">Cloudflare's 200+ PoPs share the same IP via anycast. Attack traffic is routed to nearest PoP and absorbed — never reaching your origin server.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9px;color:var(--sub);line-height:1.7">Tools: Cloudflare,<br>Akamai, Fastly,<br>AWS CloudFront</div>
    </div>
  </div>
</div>

<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">1</div><div class="t-lbl">OAuth2 Flow Design — Login with Google</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Draw the full Authorization Code + PKCE flow, step by step (8 steps). Label every HTTP request and response.</li>
          <li>Where do you store the access token and refresh token in the browser? Why not <code>localStorage</code>? What attack does <code>httpOnly</code> cookie prevent?</li>
          <li>The access token expires after 15 minutes. Walk through the silent refresh flow — what happens without the user noticing?</li>
          <li>User clicks "Logout." What must you invalidate on the client side and on the server side? What happens if you only clear the cookie?</li>
          <li>Your API server needs to call Google Drive on behalf of the user. How does the token flow differ from a user logging in? What scope do you request?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">2</div><div class="t-lbl">JWT Security Review — Find the Vulnerabilities</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Review this code and find all security issues:</p>
        <pre style="background:var(--surf);padding:10px;font-family:'Courier Prime',monospace;font-size:11px;color:var(--text);margin:8px 0;line-height:1.7">token = jwt.decode(request.headers["Authorization"],
                  algorithms=["HS256", "RS256", "none"])
if token["user_id"] == requested_user_id:
    return data</pre>
        <ol>
          <li>Identify every vulnerability (at least 4). Explain why each is dangerous.</li>
          <li>Write the corrected implementation with all required validations.</li>
          <li>A user's account is compromised at 2pm. Their JWT expires at 6pm. How do you invalidate it immediately? Give two approaches and their trade-offs.</li>
          <li>Should the JWT payload contain each of these? Justify: user's email, user's role, user's SSN, user's account balance.</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">3</div><div class="t-lbl">Zero-Trust for YouTube Microservices (B8)</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Map all service-to-service calls in the YouTube system. Which currently use shared long-lived credentials?</li>
          <li>Design the mTLS policy matrix: which services are allowed to call which? Express as explicit allow rules.</li>
          <li>The transcoding service needs read/write access to S3. Write the least-privilege IAM policy — which specific S3 actions on which specific bucket prefix?</li>
          <li>A transcoding pod is compromised. With Zero-Trust microsegmentation in place: what can the attacker reach? Without it: what can they reach?</li>
          <li>Design the secret rotation procedure for the S3 credentials: trigger, new version creation, zero-downtime migration, old version revocation.</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--red)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--red)">★</div><div class="t-lbl">Secure a Fintech Payments API (Stripe-like)</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Design complete security architecture for a payments API used by merchants to charge customers.</p>
        <ol>
          <li>Authentication: how do merchant API keys work mechanically (creation, hashing, lookup)? How does OAuth2 work for user-authorized payments (like Stripe Connect)?</li>
          <li>Authorization RBAC: a merchant can only access their own charges, customers, and refunds. Design the RBAC model — what roles, what resources, what permissions?</li>
          <li>Storing API keys: should you hash them (like passwords) or encrypt them? What's the difference? What does Stripe actually do (sk_live_ keys)?</li>
          <li>Top 3 OWASP risks for a payments API and their specific mitigations.</li>
          <li>Rate limiting design: limits for unauthenticated endpoints (API key lookup), authenticated API calls (general), and the charge endpoint specifically. Include the Redis data structure.</li>
          <li>Audit log schema: what events must be logged (at minimum)? What fields per event? What retention policy for PCI-DSS compliance?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 24 completed</span><span style="font-family:'Courier Prime',monospace">MODULE C5 · SECURITY ARCHITECTURE</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">AuthN vs AuthZ — identity vs permissions, separate checks on every request</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OAuth2 four grant types: auth code+PKCE, client credentials, implicit (deprecated), ROPC (deprecated)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OAuth2 four roles: resource owner, client, auth server, resource server</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">PKCE: code_verifier + code_challenge — prevents auth code interception</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OIDC = OAuth2 + identity, ID token is a JWT with user claims</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OIDC verification: signature, iss, aud, exp, iat, nonce — all six checks</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">JWT: header.payload.signature — Base64URL encoded, NOT encrypted</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">RS256 (asymmetric, preferred) vs HS256 (symmetric, avoid in distributed)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">JWT vulnerabilities: alg:none, HS256 key confusion, missing exp, sensitive data</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">JWT revocation: short expiry + refresh token OR jti blocklist in Redis</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">mTLS: both sides verify certificates — used for service-to-service auth</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">SPIFFE/SPIRE: workload identity — short-lived SVIDs, auto-rotated</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Zero-Trust: never trust, always verify — identity-based not network-based</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Three Zero-Trust principles: verify explicitly, least privilege, assume breach</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Microsegmentation: explicit allow rules — compromised pod is contained</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Secrets anti-patterns: hardcoded, in Dockerfiles, never rotated, shared across envs</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Vault dynamic secrets: TTL-scoped per-request credentials, audit log</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OWASP #1 Broken Access Control: IDOR, vertical privilege escalation</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OWASP #3 Injection: parameterized queries always — never concatenate user input</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OWASP #10 SSRF: block internal IPs, whitelist allowed domains, IMDSv2</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Rate limiting for security: per-IP + per-user for brute force prevention</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Credential stuffing: rate limit by user_id + CAPTCHA + HIBP check</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">DDoS: L3/4 Shield, L7 WAF + rate limit, Anycast absorption at edge</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–4 completed (OAuth2, JWT review, Zero-Trust, Stripe security)</div></div>
  </div>

  <div class="complete-banner">
    <div class="cb-title">🎓 COURSE COMPLETE</div>
    <div style="font-family:'Cinzel',serif;font-size:16px;color:var(--white);margin-bottom:12px;letter-spacing:1px">System Design Mastery — All Three Tracks</div>
    <div class="cb-sub">
      TRACK A · LOW-LEVEL DESIGN · 6 MODULES (A1–A6)<br>
      TRACK B · HIGH-LEVEL DESIGN · 12 MODULES (B1–B12)<br>
      TRACK C · ADVANCED TOPICS · 5 MODULES (C1–C5)<br><br>
      TOPICS MASTERED: OOP · SOLID · DESIGN PATTERNS · DATABASES · CACHING<br>
      MESSAGE QUEUES · URL SHORTENER · TWITTER · WHATSAPP · YOUTUBE<br>
      RATE LIMITER · CONSISTENT HASHING · ACID · SAGA · INTERVIEW FRAMEWORK<br>
      CONSENSUS / RAFT · GEO-DISTRIBUTION · CRDTS · ML SYSTEMS<br>
      OBSERVABILITY · SRE · OAUTH2 · JWT · ZERO-TRUST · SECURITY<br><br>
      RECOMMENDED NEXT STEPS:<br>
      MOCK INTERVIEWS · LEETCODE SYSTEM DESIGN · PRAMP · INTERVIEWING.IO
    </div>
  </div>
</div>
</div>


<div class="mb-nav">
  <a href="/learning/system-design/hld/module-c4-observability/">← C4 Observability</a>
  <a href="/learning/system-design/hld/module-c5-notes/">📄 Study Notes</a>
  <a href="/learning/system-design/system-design-roadmap/">↑ Roadmap</a>
  <a href="/learning/system-design/system-design-roadmap/" class="primary">✅ Track Complete</a>
</div>

<script src="{{ "/assets/js/sd-module-c5.js" | relative_url }}"></script>
