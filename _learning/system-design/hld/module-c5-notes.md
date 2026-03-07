---
layout: default
title: "Module C5: Security Architecture — Study Notes"
permalink: /learning/system-design/hld/module-c5-notes/
custom_css: dsa-chapter
---

<div style="margin-bottom:24px;padding:14px 20px;background:#fde8ea;border-left:4px solid #e03040;border-radius:0 4px 4px 0;font-family:'IBM Plex Mono',monospace;font-size:13px;">
  <strong>Module C5 · Week 29 · Track C — Advanced Topics</strong><br>
  <span style="color:#666;">Prerequisites: B1–B14, C1–C4 &nbsp;|&nbsp; Goal: AuthN/AuthZ, mTLS, Zero Trust, API security, secret management</span>
</div>

<a href="/learning/system-design/hld/module-c5-security/" style="display:inline-block;margin-bottom:32px;padding:10px 20px;background:#e03040;color:#fff;border-radius:4px;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;">⚡ Interactive Visual Version</a>

# Module C5 — Security Architecture
## System Design Mastery Course | Track C: Advanced Topics | Week 29

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** C — Advanced Topics
**Prerequisites:** B1–B12, C1–C4
**Goal:** Security is not an afterthought — it's a system design constraint. Every FAANG interview expects you to mention auth, rate limiting, and data protection unprompted. This module covers the full security stack: OAuth2/OIDC, JWT internals, mTLS, Zero-Trust, secrets management, OWASP Top 10, and DDoS mitigation.

---

## 1. Authentication vs Authorization

```
Authentication (AuthN): WHO are you? Prove your identity.
  → Passwords, biometrics, OAuth tokens, certificates

Authorization (AuthZ): WHAT can you do? What resources may you access?
  → RBAC, ABAC, ACLs, scopes

Common mistake: conflating the two.
  "The user is logged in" = authentication complete.
  "The user can delete this resource" = authorization check.
  A logged-in user can still be unauthorized for specific actions.

Identity providers (IdPs): Google, GitHub, Okta, Auth0
  → Handle authentication on your behalf via OAuth2/OIDC.
  → Your app never sees the user's password.
```

---

## 2. OAuth2 — The Authorization Framework

```
OAuth2 is NOT an authentication protocol. It's an authorization delegation framework.
  "Allow this app to access my Google Drive on my behalf."
  The app gets an access token, not the user's password.

Four roles:
  Resource Owner:    The user. Owns the data.
  Client:            The application requesting access.
  Authorization Server: Issues tokens. (Google, GitHub, Okta)
  Resource Server:   Hosts the protected resources (Google Drive API).

Four grant types (flows):

1. AUTHORIZATION CODE (with PKCE) — standard for web and mobile apps:
   a. Client redirects user to authorization server with:
      - client_id, redirect_uri, scope, state, code_challenge (PKCE)
   b. User authenticates and consents at authorization server.
   c. Auth server redirects to client with authorization code.
   d. Client exchanges code + code_verifier for tokens (server-side).
   e. Auth server returns: access_token + refresh_token + id_token.
   Why PKCE: prevents authorization code interception attacks on mobile.

2. CLIENT CREDENTIALS — for machine-to-machine (no user involved):
   Service A → POST /token {client_id, client_secret, grant_type=client_credentials}
   → Auth server returns access_token.
   Used for: microservice-to-microservice auth, cron jobs, background workers.

3. IMPLICIT FLOW — deprecated. Tokens in URL fragment = leakage risk.
   Replaced by Authorization Code + PKCE everywhere.

4. RESOURCE OWNER PASSWORD CREDENTIALS — deprecated.
   User gives password directly to client. Defeats the purpose of OAuth.

Token types:
  Access token:  short-lived (15 min – 1 hr). Used to call APIs.
                 Opaque (random string) OR JWT (self-contained).
  Refresh token: long-lived (days – weeks). Used to get new access tokens.
                 Stored securely. Never sent to resource servers.
  ID token:      JWT containing user identity claims. OIDC extension.
```

---

## 3. OIDC — OpenID Connect

```
OIDC = OAuth2 + Identity Layer.
  OAuth2 gives you: "this token allows access to these resources."
  OIDC adds: "this is WHO the token belongs to."

OIDC introduces:
  ID token: a JWT containing claims about the user.
    {
      "iss": "https://accounts.google.com",
      "sub": "1234567890",         ← unique user identifier
      "aud": "your-client-id",     ← must verify this matches your app
      "exp": 1700000000,           ← expiry — must verify
      "iat": 1699996400,
      "email": "user@example.com",
      "name": "Alice Smith"
    }

  UserInfo endpoint: GET /userinfo with access_token → more user attributes.

  Discovery document: /.well-known/openid-configuration
    → lists authorization_endpoint, token_endpoint, jwks_uri, etc.

OIDC verification steps (CRITICAL — must do all):
  1. Verify signature using public key from JWKS endpoint.
  2. Verify iss matches expected issuer.
  3. Verify aud matches your client_id.
  4. Verify exp is in the future (not expired).
  5. Verify iat is recent (clock skew tolerance: 5 min).
  6. Verify nonce if you sent one (replay attack prevention).
```

---

## 4. JWT — JSON Web Tokens

```
Structure: header.payload.signature (Base64URL encoded, dot-separated)

Header:
  {
    "alg": "RS256",    ← signing algorithm (RS256 = RSA + SHA-256)
    "typ": "JWT",
    "kid": "key-id-1"  ← which public key to use for verification
  }

Payload (claims):
  {
    "sub": "user_123",          ← subject (user ID)
    "iss": "auth.company.com",  ← issuer
    "aud": "api.company.com",   ← audience (who should accept this)
    "exp": 1700000000,          ← expiry (Unix timestamp)
    "iat": 1699996400,          ← issued at
    "jti": "unique-token-id",   ← JWT ID (for revocation tracking)
    "roles": ["user", "admin"], ← custom claims
    "scope": "read:data write:data"
  }

Signature: RSA_SHA256(base64url(header) + "." + base64url(payload), private_key)
  → Verification uses the PUBLIC key.
  → Only the auth server with the private key can issue valid JWTs.
  → Anyone with the public key can verify — no auth server call needed.

Key algorithms:
  HS256: HMAC-SHA256. Symmetric key — same key signs and verifies.
         Problem: every service that verifies must have the secret key.
         Risk: key compromise → forge any token.
         Avoid in distributed systems.
  RS256: RSA-SHA256. Asymmetric — private key signs, public key verifies.
         Auth server keeps private key secret.
         All services get the public key (can be published at JWKS endpoint).
         Preferred for distributed systems.

JWT vulnerabilities:
  1. alg:none attack: attacker changes header to {"alg":"none"}, removes signature.
     Server accepts if it doesn't enforce algorithm. Fix: whitelist algorithms.
  2. HS256 key confusion: attacker uses server's public key as HS256 secret.
     Server verifies HS256 with its own public key. Fix: validate alg strictly.
  3. Missing claims validation: if exp not checked, expired tokens work forever.
  4. Sensitive data in payload: payload is Base64 encoded, NOT encrypted.
     Anyone can decode it. Never put passwords, PII, secrets in JWT payload.

JWT revocation problem:
  JWTs are stateless. You cannot revoke them without a server-side check.
  Solutions:
  1. Short expiry (15 min) + refresh tokens. Refresh token is revocable.
  2. Revocation list (blocklist): store revoked jti values in Redis. Check on each request.
     Downside: adds a Redis lookup to every API call.
  3. Token versioning: store user's current token version in DB.
     JWT carries version claim. Bump version to invalidate all tokens.
```

---

## 5. mTLS — Mutual TLS

```
Regular TLS: client verifies server's certificate. Server doesn't verify client.
mTLS:        both parties verify each other's certificates.

Use case: microservice-to-microservice authentication.
  "You're not just connecting to a valid payment service —
   you're proving you ARE the order service."

How it works:
  1. Both services have certificates issued by a shared CA (Certificate Authority).
  2. TLS handshake: both present and verify each other's certificates.
  3. If either cert is invalid/expired/untrusted: connection refused.

Certificate lifecycle:
  Issue: CA signs a certificate for the service (contains service name, expiry).
  Rotate: certificates have short TTL (24–72 hours in modern systems).
  Revoke: CRL (Certificate Revocation List) or OCSP stapling.
  Automate: cert-manager (k8s), SPIRE/SPIFFE, Istio service mesh handles rotation.

SPIFFE/SPIRE:
  SPIFFE: standard for workload identity (a service's certificate).
  SPIRE: implementation. Automatically issues and rotates certs for k8s pods.
  SVID: SPIFFE Verifiable Identity Document — the cert/JWT workload identity.

Service mesh (Istio, Linkerd):
  Injects a sidecar proxy (Envoy) into every pod.
  Sidecar handles mTLS automatically — application code doesn't change.
  Policy: "only order-service may call payment-service" — enforced by the mesh.
```

---

## 6. Zero-Trust Architecture

```
Traditional security model: "trust everything inside the perimeter."
  → VPN access = trusted = can reach any internal resource.
  → Problem: one compromised endpoint = attacker has free rein inside.

Zero-Trust model: "never trust, always verify."
  → No implicit trust based on network location.
  → Every request authenticated and authorized, regardless of origin.
  → Assume breach: design as if the attacker is already inside.

Zero-Trust principles:
  1. Verify explicitly: authenticate and authorize every request.
     Identity-based access, not network-based.
  2. Use least privilege: users and services get only the permissions they need.
     No standing admin access. Just-in-time (JIT) privilege escalation.
  3. Assume breach: minimize blast radius. Segment everything.
     Log all access. Alert on anomalies. Practice response.

Pillars of Zero-Trust:
  Identity: strong auth (MFA) for users. mTLS for services.
  Device:   device posture checks (is the device patched, encrypted, enrolled?).
  Network:  microsegmentation. Services can only talk to explicitly allowed peers.
  Application: RBAC at app layer. Fine-grained authorization.
  Data:     encrypt at rest and in transit. Data classification and access policies.

Implementation:
  Service mesh: mTLS between all services. Policy: "A → B allowed, A → C denied."
  API gateway: OAuth2/OIDC for user-facing APIs. JWT validation at the edge.
  BeyondCorp (Google's Zero-Trust): employee access based on device + identity,
    not VPN. The office network and the internet are treated the same.

Microsegmentation:
  Traditional: flat network — all services can talk to all services.
  Microsegmented: network policies (k8s NetworkPolicy, AWS Security Groups).
    payment-service: only accepts connections from order-service.
    DB: only accepts connections from app servers, not from web tier.
```

---

## 7. Secrets Management

```
Secret: any sensitive value — API keys, DB passwords, private keys, tokens.

Anti-patterns (what NOT to do):
  ❌ Hardcode secrets in source code (git history = permanent exposure)
  ❌ Store secrets in environment variables in Dockerfiles or k8s YAML
  ❌ Email or Slack secrets to teammates
  ❌ Use the same secret across all environments (dev/staging/prod)
  ❌ Never rotate secrets ("it's been working for 3 years")

Secret management tools:
  HashiCorp Vault:
    Centralized secret store. Audit log for every access.
    Dynamic secrets: Vault generates a DB password for each request, with TTL.
      App gets: username=vault-app-20250307, password=abc123, TTL=1hr.
      After 1 hour, credential automatically revoked. No long-lived passwords.
    Secret lease + renewal: apps renew leases before expiry.

  AWS Secrets Manager:
    Managed service. Auto-rotation for RDS, ElastiCache, etc.
    Versioning: new secret version staged, apps migrated, old version deleted.
    Cost: $0.40/secret/month + $0.05 per 10K API calls.

  Kubernetes Secrets:
    Base64 encoded (NOT encrypted by default!).
    Enable encryption at rest with KMS provider.
    Use external-secrets-operator: syncs secrets from Vault/AWS SM into k8s.

Secret rotation strategy:
  1. Rotation trigger: scheduled (every 30 days) or on breach.
  2. New secret created in secrets manager.
  3. New secret version deployed to apps (zero-downtime: support both old + new).
  4. Old secret deprecated → revoked after grace period.

Principle of least privilege for secrets:
  App A: needs DB read access → gets read-only DB credential.
  App B: needs S3 write access → gets s3:PutObject on specific bucket only.
  Service accounts: one per service, not shared across services.
```

---

## 8. OWASP Top 10 (2021)

```
1. Broken Access Control (#1 most common):
   Vertical privilege escalation: user accesses admin endpoints.
   Horizontal: user accesses another user's data (IDOR — Insecure Direct Object Reference).
   Fix: enforce authorization at every endpoint. Don't trust client-supplied IDs.
   Example: GET /users/123 → check that 123 is the requesting user's ID or admin.

2. Cryptographic Failures:
   Weak algorithms (MD5, SHA1 for passwords — broken, preimage attacks).
   Passwords stored in plaintext or with reversible encryption.
   HTTP instead of HTTPS for sensitive data.
   Fix: bcrypt/Argon2 for passwords. AES-256 for data at rest. TLS 1.2+ everywhere.

3. Injection (SQL, NoSQL, LDAP, OS commands):
   User input inserted directly into queries: "SELECT * FROM users WHERE id = " + userId
   Fix: parameterized queries / prepared statements. Never concatenate user input.
   Example: SQLi — input "1 OR 1=1 --" → returns all users.

4. Insecure Design:
   No threat modeling during design phase.
   Business logic flaws: buy item for $0 by sending negative quantity.
   Fix: threat model during design. Test business logic adversarially.

5. Security Misconfiguration:
   Default credentials, unnecessary features enabled, verbose error messages.
   S3 bucket public by default, debug endpoints exposed in production.
   Fix: security-hardened configs, IaC security scanning (tfsec, checkov).

6. Vulnerable and Outdated Components:
   Using libraries with known CVEs. Log4Shell was in log4j (a common dependency).
   Fix: SCA (Software Composition Analysis) tools — Snyk, Dependabot, OWASP Dependency-Check.

7. Identification and Authentication Failures:
   Weak passwords accepted, no MFA, predictable session IDs, session not invalidated on logout.
   Fix: strong password policy, MFA, cryptographically random session IDs, proper logout.

8. Software and Data Integrity Failures:
   Unsigned software updates, CI/CD pipeline attacks (SolarWinds).
   Fix: sign releases, verify checksums, secure the CI/CD pipeline.

9. Security Logging and Monitoring Failures:
   No logging of auth failures, no alerting on brute force, logs not reviewed.
   Fix: log auth events, alert on anomalies (10 failed logins in 60s), SIEM.

10. Server-Side Request Forgery (SSRF):
    App fetches a URL from user input → attacker supplies http://169.254.169.254/latest/meta-data/
    AWS metadata endpoint → gets IAM credentials.
    Fix: whitelist allowed domains, block internal IP ranges, use metadata service v2 (IMDSv2).
```

---

## 9. Rate Limiting for Security

```
Beyond throughput control — rate limiting prevents abuse:

Authentication endpoints:
  Brute force: attacker tries 10M passwords per second.
  Fix: rate limit POST /login to 5 attempts per IP per 15 minutes.
  Lockout after 10 failures (with CAPTCHA or exponential backoff).

API abuse:
  Credential stuffing: attacker uses breached credentials list.
  Fix: rate limit per IP, per user, per API key.
  Distributed: multiple IPs → rate limit on user_id not just IP.

Strategies:
  IP-based: good for unauthenticated endpoints.
  User-based: good for authenticated endpoints.
  Global: protect specific expensive endpoints regardless of who's calling.

Implementation:
  Redis: INCR counter per (user_id, endpoint, time_window).
         EXPIRE key at window boundary.
  Token bucket algorithm: allows burst, then smooths out traffic.

DDoS mitigation:
  Layer 3/4 (volumetric): ISP-level filtering, BGP blackholing.
                           Cloudflare/AWS Shield for scrubbing.
  Layer 7 (application): WAF (Web Application Firewall) — block bad patterns.
                          Rate limiting. CAPTCHA for suspected bots.
                          Cloudflare, AWS WAF, Akamai.
  Anycast: Cloudflare's network absorbs DDoS at the edge, not your origin.
```

---

## 📝 Tasks

### Task 1 — OAuth2 Flow Design
Design the authentication flow for a web app that lets users log in with Google:
1. Draw the Authorization Code + PKCE flow step by step (8 steps).
2. Where do you store the access token and refresh token in the browser? Why not localStorage?
3. The access token expires. Walk through the silent refresh flow.
4. User logs out. What must you invalidate on client and server?
5. Your API needs to call Google Drive on behalf of the user. How does the token flow differ?

### Task 2 — JWT Security Review
Review this JWT implementation and find all security vulnerabilities:
```
// server code
token = jwt.decode(request.headers["Authorization"], algorithms=["HS256", "RS256", "none"])
if token["user_id"] == requested_user_id:
    return data
```
1. Identify every vulnerability in this code snippet (at least 4).
2. Write the correct implementation with all validations.
3. A user's account is compromised. How do you invalidate their JWT immediately? Two approaches.
4. Should the JWT payload contain: user's email, user's role, user's SSN, user's account balance? Justify each.

### Task 3 — Zero-Trust for Microservices
Apply Zero-Trust to the YouTube system from B8 (video upload, transcoding, CDN):
1. Map all service-to-service calls. Which ones currently use shared credentials?
2. Design the mTLS policy: which services may call which?
3. The transcoding service needs S3 read/write. Design the least-privilege IAM policy.
4. A transcoding pod is compromised. With Zero-Trust in place, what can the attacker access? Without it?
5. Design the secret rotation procedure for the S3 credentials.

### ⭐ Task 4 — Secure a Fintech API
Design the complete security architecture for a payments API (like Stripe):
1. Authentication: how do API keys work? How does OAuth2 work for user-authorized payments?
2. Authorization: a merchant can only access their own data. Design the RBAC model.
3. Secrets: merchant API keys must be stored. Hash them or encrypt them? Why?
4. OWASP: identify the top 3 OWASP risks for a payments API and their mitigations.
5. Rate limiting: design limits for: unauthenticated endpoints, authenticated API calls, charge endpoint specifically.
6. Audit log: design the audit log schema. What events must be logged? What's the retention policy?

---

## ✅ Completion Checklist

- [ ] AuthN vs AuthZ — identity vs permissions, two distinct checks
- [ ] OAuth2 four grant types: auth code+PKCE, client credentials, implicit (deprecated), ROPC (deprecated)
- [ ] OAuth2 four roles: resource owner, client, auth server, resource server
- [ ] PKCE: prevents auth code interception on mobile/SPA
- [ ] OIDC = OAuth2 + identity layer, ID token is a JWT with user claims
- [ ] OIDC verification: signature, iss, aud, exp, iat, nonce — all six
- [ ] JWT structure: header.payload.signature (Base64URL, NOT encrypted)
- [ ] RS256 vs HS256: asymmetric (preferred for distributed) vs symmetric
- [ ] JWT vulnerabilities: alg:none, HS256 key confusion, missing exp check, sensitive data in payload
- [ ] JWT revocation: short expiry + refresh token OR jti blocklist in Redis
- [ ] mTLS: both sides present certs, used for service-to-service auth
- [ ] SPIFFE/SPIRE: workload identity standard for k8s
- [ ] Zero-Trust: never trust, always verify — identity-based not network-based
- [ ] Zero-Trust principles: verify explicitly, least privilege, assume breach
- [ ] Microsegmentation: NetworkPolicy, security groups — explicit allow rules
- [ ] Secrets anti-patterns: hardcoded, env vars in Dockerfile, no rotation
- [ ] HashiCorp Vault dynamic secrets: TTL-scoped credentials per request
- [ ] Secret rotation: new version → deploy → deprecate → revoke
- [ ] OWASP #1 Broken Access Control: IDOR, vertical privilege escalation
- [ ] OWASP #3 Injection: parameterized queries always
- [ ] OWASP #10 SSRF: block internal IPs, whitelist allowed domains
- [ ] Rate limiting for security: brute force, credential stuffing prevention
- [ ] DDoS: L3/4 BGP blackholing + L7 WAF + Anycast (Cloudflare)
- [ ] Completed Tasks 1–4

**→ Module C5 completes Track C. Full course complete: Tracks A (LLD) + B (HLD) + C (Advanced).**
**→ Suggested next steps: mock interview sessions, LeetCode system design problems, real interview preparation.**

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-c4-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← C4 Observability Notes</a>
  <a href="/learning/system-design/hld/module-c5-security/" style="padding:12px 24px;border:1px solid #e03040;color:#e03040;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;background:#e03040;color:#fff;border-radius:4px;text-decoration:none;font-weight:600;">✅ Track C Complete</a>
</div>
