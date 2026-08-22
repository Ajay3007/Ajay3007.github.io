---
title: "Module B9 Notes: Rate Limiter"
description: "Module B9 — Design a Rate Limiter System Design Mastery Course Track B: HLD Week 19 --- 🎯 Module Overview Duration: 1 Week Track: B — HLD Fundamentals Deep Dive Prerequisites:…"
domain: system-design
track: system-design-hld
order: 119
ownHeader: true
url: /learning/system-design/hld/module-b9-notes/
---

# Module B9 — Design a Rate Limiter
## System Design Mastery Course | Track B: HLD | Week 19

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Fundamentals Deep Dive  
**Prerequisites:** B1–B8  
**Goal:** Rate limiting is the most commonly asked infrastructure component in system design interviews. It appears as a standalone question ("design a rate limiter") and as part of every API design question. This module covers all 5 algorithms with exact memory/accuracy trade-offs, Redis Lua implementation, and distributed coordination strategies.

---

## 1. Why Rate Limit?

```
Three primary motivations:

1. DDoS / Abuse Prevention
   Attacker sends 100K requests/sec to API
   Per-IP rate limit at CDN edge: attacker gets 429, backend sees zero traffic
   
2. Noisy Neighbour
   One API tenant bug: tight loop, 10K req/sec
   Per-API-key limits: buggy tenant throttled, others unaffected
   
3. Cost Control
   External API costs money per call (OpenAI, Google Maps)
   Bug sends 1M calls/min = $50K cloud bill overnight
   Outbound rate limiter: max 1,000 external calls/minute
```

---

## 2. Algorithm Comparison

| Algorithm | Memory | Accuracy | Burst? | Best Use Case |
|---|---|---|---|---|
| Fixed Window | O(1) | ~Low | 2× at boundary | Internal services |
| Sliding Window Log | O(requests) | Exact | No | Financial APIs |
| **Sliding Window Counter ★** | **O(1)** | **~99.7%** | **No boundary** | **Production default** |
| Token Bucket | O(1) | Exact | Yes (up to B) | Burst-ok APIs |
| Leaky Bucket | O(queue) | Exact | No | Payment processors |

---

## 3. Fixed Window Counter

```
Key: "rl:fixed:{userId}:{current_minute}"
Ops: INCR key → if count==1: EXPIRE key 60

Problem: Boundary attack
  00:59 — 100 requests (allowed, window ends)
  01:00 — 100 requests (allowed, new window)
  Total: 200 requests in 2 seconds ← 2× your intended rate

Use when: internal services, rough protection only
Avoid: any external-facing high-value API
```

---

## 4. Sliding Window Log

```
Data structure: Redis Sorted Set (score = timestamp)
Ops:
  ZADD key {now_ms} {now_ms}
  ZREMRANGEBYSCORE key 0 {now - window_ms}  ← remove old entries
  count = ZCARD key
  
Properties:
  Memory: O(requests in window) — 100 req/user × 1M users = 100M entries in Redis
  Accuracy: Exact — no boundary problem
  
When to use: financial APIs, operations where exact count is regulatory requirement
When not: high-volume consumer APIs (memory prohibitive)
```

---

## 5. Sliding Window Counter ★ (Production Default)

```
Key insight: approximate sliding count from 2 fixed windows

Keys: "rl:{userId}:{prev_minute}", "rl:{userId}:{curr_minute}"

Formula:
  elapsed_fraction = seconds_into_current_minute / 60.0
  effective_count = prev × (1 - elapsed_fraction) + curr
  
  if effective_count >= limit → reject
  else → INCR curr_key, allow

Example (at 30 seconds into minute):
  prev = 80, curr = 30, limit = 100
  effective = 80 × 0.5 + 30 = 70 → allowed

Boundary attack fails:
  00:59: 100 requests → prev = 100
  01:30: 60 requests cumulative → effective = 100×0.5 + 60 = 110 → BLOCKED ✓

Memory: O(2 keys per user) — same as fixed window!
Accuracy: Max error bounded by ~0.003% in practice
```

---

## 6. Token Bucket

```
Concept:
  Bucket capacity: B tokens (max burst)
  Refill rate: R tokens per second
  Each request consumes 1 token
  No tokens → reject request

Behaviour:
  Idle period → bucket fills to B tokens
  Burst arrives → can serve up to B requests instantly
  After burst → restores to steady R req/sec rate

Use when:
  Upload API: allow burst of 10 uploads then 1/minute
  Chat API: allow typing burst then throttle
  
Implementation: MUST use Redis Lua script for atomicity
  Without Lua: GET tokens, compute new tokens, SET tokens
  Race condition: two concurrent requests both read 1 token, both decrement to 0
  Both get allowed, but you actually had only 1 token → count wrong
```

---

## 7. Redis Lua Script (Critical Concept)

```lua
-- Sliding Window Counter — Lua for atomicity
local prev = tonumber(redis.call('get', KEYS[1])) or 0
local curr = tonumber(redis.call('get', KEYS[2])) or 0
local limit = tonumber(ARGV[1])
local fraction = tonumber(ARGV[2])

local count = math.floor(prev * (1.0 - fraction)) + curr

if count >= limit then
    return {0, count}  -- blocked
end

local new_count = redis.call('incr', KEYS[2])
if new_count == 1 then
    redis.call('expire', KEYS[2], ARGV[3])
end

return {1, count + 1}  -- allowed
```

```
WHY LUA? Redis Lua scripts execute atomically.
No concurrent execution during script run.
No race conditions possible.
Alternative (wrong): GET → compute → INCR in separate commands
  Two concurrent requests: both GET count=99, both allowed, count reaches 101
```

---

## 8. Distributed Rate Limiting

```
Problem: 10 gateway nodes, where does the counter live?

Option 1: Local counter per gateway
  Fast (no network), but:
  Effective limit = N × limit (N = gateway count)
  10 gateways × 100/min = 1000/min actual
  
Option 2: Centralised Redis ★ (production default)
  All gateways → one Redis cluster
  Latency: ~1ms per request (Redis round-trip)
  Accuracy: exact global count
  Sharding: consistent hashing on API key → each key on one shard
  Failure: fail open (allow) + circuit breaker
  
Option 3: Synchronised local counters
  Each gateway syncs to peers every 100ms
  Max overshoot: sync_interval × rate
  Use: non-critical limits, Redis unavailable scenario
  
Production choice: Centralised Redis with consistent hashing
  3–5 Redis cluster nodes
  Single Redis call per API request
  If shard fails → fail open (not fail closed)
```

---

## 9. HTTP 429 Response Standard

```
Always include these headers:

HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 100            ← the limit
X-RateLimit-Remaining: 0          ← how many left
X-RateLimit-Reset: 1705334460     ← Unix timestamp of window reset
Retry-After: 47                   ← seconds until retry (REQUIRED)

Body: {"error": {"code": "RATE_LIMIT_EXCEEDED", "retryAfter": 47}}

On every successful request too:
X-RateLimit-Remaining: 73         ← lets clients self-throttle proactively

Why Retry-After matters:
  Without it: clients retry immediately → make overload WORSE
  With it: good clients wait → thundering herd problem self-resolves
```

---

## 10. Multi-Tier Architecture

```
Layer 1: CDN / Edge (per IP, ~10,000 req/min)
  → Catches DDoS before it reaches your infra
  → Cloudflare, AWS WAF, Akamai handle this
  
Layer 2: API Gateway (per API key, varies by tier)
  → Free: 100 req/min, Pro: 10,000 req/min  
  → Centralised Redis backing
  → This is what most "rate limiter" interview questions are about

Layer 3: Application Layer (per endpoint)
  → POST /search: 10 req/sec (expensive DB query)
  → POST /payment: 5 req/min (fraud prevention)
  → GET /profile: 1,000 req/min (cheap)

Layer 4: Database / External API (outbound limits)
  → Max 50 req/sec to Google Maps API
  → Circuit breaker: trips at 50% error rate
```

---

## 📝 Tasks

### Task 1 — Algorithm Selection
1. Twitter "post tweet": 300 per 3 hours. Which algorithm?
2. Payment API: must NEVER exceed 5/min (regulatory). Which algorithm?
3. File upload: burst of 10 then 1/minute. Which algorithm? What are B and R?
4. Demonstrate fixed window boundary attack with numbers
5. Prove sliding window counter max error is bounded

### Task 2 — Redis Implementation
1. Implement Fixed Window Counter. Write exact Redis commands.
2. Implement Sliding Window Log. What data structure? Memory for 1M users × 100/min?
3. Show the race condition in Token Bucket without Lua. Concrete 2-request example.
4. Redis experiences 50ms latency spike — impact on API p99? How to handle?
5. Redis crashes — fail open (allow all) or fail closed (block all)? Justify.

### Task 3 — Distributed Design
Design rate limiter for 10 gateway nodes, 100M API calls/day, per-key limits.
Questions: Redis calls per request? Latency budget? Shard failure handling?

### ⭐ Task 4 — URL Shortener Rate Limiting
Add rate limiting to B5 URL shortener:
  POST /shorten: 10/min anonymous, 1,000/min authenticated
  GET /{code}: 1,000/min per IP
  DELETE /links/{id}: 5/min
  Global: 50,000 req/sec total

---

## ✅ Completion Checklist

- [ ] Why rate limit: DDoS, noisy neighbour, cost control
- [ ] Fixed window: O(1) memory, boundary burst = 2× limit
- [ ] Sliding window log: exact, sorted set, O(requests) memory
- [ ] Sliding window counter: O(1) memory, 99.7% accurate, formula
- [ ] Token bucket: B tokens capacity, R tokens/sec refill, burst ok
- [ ] Leaky bucket: uniform output, no burst, queue-based
- [ ] Algorithm selection matrix: know when to pick each
- [ ] Redis Lua: why required (atomicity), race condition without it
- [ ] Distributed centralised Redis: consistent hashing, fail open
- [ ] 429 response: all 4 headers, why Retry-After is critical
- [ ] Multi-tier: CDN → Gateway → App → DB/external
- [ ] Completed Task 1 — algorithm selection scenarios
- [ ] Completed Task 2 — Redis implementation + failure modes
- [ ] Completed Task 3 — distributed design
- [ ] Completed Task 4 — URL shortener rate limiting

**→ Next: Module B10 — Consistent Hashing &amp; Service Discovery**

<br>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b8-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B8 YouTube Notes</a>
  <a href="/learning/system-design/hld/module-b9-rate-limiter/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b10-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B10 Consistent Hashing →</a>
</div>
