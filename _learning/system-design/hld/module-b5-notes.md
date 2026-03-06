---
layout: default
title: "Module B5 — URL Shortener Notes"
permalink: /learning/system-design/hld/module-b5-notes/
---

# Module B5 — URL Shortener (End-to-End HLD Case Study)
## System Design Mastery Course | Track B: HLD | Week 15

---

## 🎯 Module Overview

**Duration:** 1 Week
**Track:** B — HLD Case Studies
**Prerequisites:** B1–B4 (all fundamentals)
**Goal:** Apply every HLD concept in a complete end-to-end design. URL shortener is the most common FAANG warm-up question. Master it so well you can teach it.

### Why URL Shortener?
- Small enough to design fully in 45 minutes
- Touches every core HLD topic: DB, cache, hashing, scale, availability
- Read-heavy (100:1 read:write) — demonstrates caching mastery
- Redirect latency SLA (<10ms p99) — forces cache-first thinking
- Unique ID generation is a classic distributed systems problem

---

## 1. Requirements Clarification

### Functional Requirements
```
Core features:
  1. POST /shorten          — Given a long URL, return a short code (e.g. "abc1234")
  2. GET /{shortCode}       — Redirect to original long URL (HTTP 301/302)
  3. Custom aliases         — User can specify their own short code
  4. TTL / expiry           — URLs can have an optional expiration date
  5. Analytics              — Click count, referrer, geo, device (optional)

Out of scope (for this design):
  - User accounts / auth
  - Dashboard UI
  - Link editing after creation
```

### Non-Functional Requirements
```
Scale:
  - 300 million URLs stored
  - Write: 100 new URLs/second (peak: 500/sec)
  - Read:  10,000 redirects/second (peak: 50,000/sec)
  - Read:write ratio = 100:1

Performance:
  - Redirect latency: p99 < 10ms
  - Shorten latency:  p99 < 100ms

Durability & Availability:
  - 99.99% availability
  - URLs must never be lost (durable writes)
  - Short codes must be globally unique

Storage:
  - Short code: 7 chars → 56 billion unique codes (62^7)
  - URL record: ~500 bytes (short code + long URL + metadata)
  - Total: 300M × 500 bytes = 150 GB (fits on one DB node with room to grow)
```

---

## 2. Capacity Estimation

```
WRITE QPS:
  100 URLs/sec average → peak 500/sec
  Storage/day: 100 × 86,400 × 500 bytes = ~4.3 GB/day
  Storage/5 years: 4.3 GB × 365 × 5 = ~7.8 TB

READ QPS:
  10,000 redirects/sec average → peak 50,000/sec
  Bandwidth: 50,000 × 500 bytes = ~25 MB/sec (response)

CACHE:
  Assuming 80/20 rule: top 20% URLs get 80% of traffic
  Hot set: 300M × 0.20 × 500 bytes = ~30 GB → fits in Redis cluster
  Target: 99%+ cache hit rate for redirects

SERVERS:
  Each app server handles ~10K req/sec
  Read path: 50K req/sec → 5 servers minimum (use 10–20 with LB)
  Write path: 500 req/sec → 1 server (use 3 for HA)
```

---

## 3. High-Level Architecture

```
                    ┌─────────────────────────────────────────┐
                    │                                         │
[Browser/App] ──→ [DNS] ──→ [Load Balancer (L7 / HTTPS)]     │
                                      │                       │
                    ┌─────────────────┼───────────────────┐   │
                    │                 │                   │   │
                    ↓                 ↓                   ↓   │
             [API Server 1]   [API Server 2]   [API Server N] │
                    │                                         │
          ┌─────────┼─────────────────────────────────┐       │
          │         │                                 │       │
          ↓         ↓                                 ↓       │
    [Redis Cache] [ID Generator]              [MySQL Primary] │
    (hot URLs)    (Snowflake/                 (source of truth)│
                   base62)                         │           │
                                            [MySQL Replicas]  │
                                            (read replicas)   │
                    │                                         │
                    ↓                                         │
             [Kafka: click-events]                            │
                    │                                         │
                    ↓                                         │
           [Analytics Consumer]                              │
           (ClickHouse/BigQuery)                             │
                    └─────────────────────────────────────────┘
```

### Read Path (Redirect — must be <10ms)
```
1. GET /abc1234
2. Check Redis cache: GET url:abc1234
   → HIT (99% of cases): return 302 redirect immediately (~0.5ms)
   → MISS (1%): read from MySQL replica (~5ms)
3. On cache miss: populate Redis (TTL 24h), return redirect
4. Async: publish click event to Kafka (fire-and-forget, doesn't block redirect)
```

### Write Path (Shorten URL)
```
1. POST /shorten { longUrl, customAlias?, expiresAt? }
2. Validate URL (parseable, not already in blocklist)
3. Generate short code (see Section 4)
4. Write to MySQL primary (durable)
5. Optionally pre-warm Redis cache
6. Return { shortUrl: "https://sho.rt/abc1234" }
```

---

## 4. Short Code Generation

### Option A: MD5 Hash + Truncation
```java
String shortCode = Base62.encode(MD5.hash(longUrl)).substring(0, 7);

Pros:
  ✅ Deterministic — same URL always gets same short code (natural dedup)
  ✅ No ID generator dependency
  ✅ Stateless — any server can generate independently

Cons:
  ❌ Hash collision: two different URLs can produce same 7-char prefix
     Collision probability: 1/(62^7) = 1 in 3.5 trillion — but at 300M URLs it matters
  ❌ Resolution: detect collision, append counter, rehash
  ❌ Custom aliases not supported
```

### Option B: Auto-Increment ID + Base62 Encoding (Recommended)
```java
// DB generates auto-increment ID
long id = db.insertAndGetId(longUrl);  // e.g., id = 123456789

// Encode to base62
String shortCode = base62Encode(id);   // "8M0kX" (5 chars for this ID)

Base62 alphabet: 0-9, a-z, A-Z (62 characters)
7 characters → 62^7 = 3.5 trillion unique codes

base62Encode(123456789):
  123456789 % 62 = 41 → 'p'
  123456789 / 62 = 1991238 → recurse
  Result: "8M0kX" (variable length, pad to 7 if needed)

Pros:
  ✅ Guaranteed unique (monotonically increasing ID)
  ✅ Simple, fast
  ✅ Short — lower IDs = shorter codes

Cons:
  ❌ Predictable — attackers can enumerate URLs (ID 1, 2, 3...)
  ❌ Single point of failure if using one DB for ID generation
```

### Option C: Distributed ID (Snowflake-style)
```
64-bit ID structure:
  [41 bits: timestamp ms] [10 bits: machine ID] [12 bits: sequence]

Generates ~4096 IDs/ms per machine. Globally unique. No DB dependency.
Encode result in base62 → 7-char code.

Use when: extremely high write throughput, multi-region deployment.
```

### Option D: Pre-generated Code Pool
```
Background job pre-generates random 7-char base62 codes.
Stores in a "codes" table with status: available/used.
API server fetches next available code atomically (SELECT FOR UPDATE).

Pros:
  ✅ No collision risk
  ✅ Random → not enumerable
Cons:
  ❌ More complex, pre-generation overhead
```

**Recommendation:** Option B (auto-increment + base62) for simplicity. Add random salt to prevent enumeration if needed.

---

## 5. Database Schema

```sql
CREATE TABLE urls (
    id           BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code   VARCHAR(10) NOT NULL UNIQUE,
    long_url     TEXT NOT NULL,
    user_id      BIGINT,              -- NULL if anonymous
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at   TIMESTAMP,           -- NULL = never expires
    click_count  BIGINT DEFAULT 0,    -- approximate, updated async
    is_active    BOOLEAN DEFAULT TRUE
);

CREATE UNIQUE INDEX idx_short_code ON urls(short_code);
CREATE INDEX idx_user_id ON urls(user_id);  -- "my URLs" page
CREATE INDEX idx_expires_at ON urls(expires_at) WHERE expires_at IS NOT NULL;
-- Partial index only on rows with expiry → smaller, faster for cleanup job
```

### DB Choice: MySQL (or PostgreSQL)
```
Justification:
  - 150 GB total storage → fits comfortably on single node
  - Access pattern: primary key lookup (short_code) → perfect for SQL B-tree index
  - ACID required: prevent duplicate short codes under concurrent inserts
  - Complex queries not needed → NoSQL would work too, but SQL is simpler

Read replicas: 3 replicas for 10K+ redirects/sec read load
Sharding: not needed at 150 GB — if URLs reach 10 TB, shard by hash(short_code)
```

---

## 6. Caching Strategy

```
Layer 1: In-process cache (Caffeine)
  - Size: top 10,000 most accessed URLs per server
  - TTL: 5 minutes
  - Hit rate: ~60% of traffic (power-law distribution)

Layer 2: Redis
  - Key: "url:{shortCode}"
  - Value: long_url string
  - TTL: 24 hours (most URLs accessed within 24h of creation)
  - Hit rate: ~99% of remaining traffic
  - Eviction: allkeys-lru (hot URLs stay, cold ones evicted)

Cache miss path:
  → Query MySQL read replica (~5ms)
  → Populate Redis (TTL 24h)
  → Populate in-process cache (TTL 5min)

Cache invalidation:
  - URL deleted: delete from Redis immediately
  - URL expired: TTL-based expiry or background job deletes + Redis key deleted
  - Click count: NOT cached — updated async via Kafka consumer to MySQL
```

---

## 7. Redirect: 301 vs 302

```
HTTP 301 Moved Permanently:
  ✅ Browser caches the redirect → subsequent visits bypass your server
  ✅ Reduces server load
  ❌ Can't track repeat visits from same browser
  ❌ If long URL changes, browsers serve old cached redirect
  Use when: link never changes, analytics not critical

HTTP 302 Found (Temporary):
  ✅ Browser does NOT cache → every visit hits your server
  ✅ Full analytics on every click
  ✅ Can update long URL at any time
  ❌ Higher server load (every click hits you)
  Use when: analytics required, URLs may change (RECOMMENDED for TinyURL)
```

---

## 8. Analytics Pipeline

```
Async — does NOT block the redirect:

[Redirect handler] ──fire-and-forget──→ [Kafka topic: click-events]
                                                │
                    ┌───────────────────────────┤
                    │                           │
                    ↓                           ↓
          [Click Count Consumer]     [Analytics Consumer]
          (UPDATE urls SET           (stream to ClickHouse
           click_count += 1)         for dashboard queries:
                                     geo, device, referrer,
                                     hourly/daily aggregates)

Click event schema:
{
  shortCode: "abc1234",
  timestamp: 1700000000,
  ipAddress: "1.2.3.4",      // → geo lookup
  userAgent: "Chrome/120",   // → device type
  referrer:  "twitter.com"
}
```

---

## 9. Edge Cases & Deep Dives

### Expiry Handling
```
Option A: Lazy expiry
  On redirect, check expires_at. If expired, return 404. Let Redis TTL handle cache.
  Simple — no background job needed.

Option B: Background cleanup job
  Scheduled daily: DELETE FROM urls WHERE expires_at < NOW()
  Prevents DB from filling with dead rows.
  Combined approach: lazy check + periodic cleanup.
```

### Custom Aliases
```
POST /shorten { longUrl: "...", alias: "my-campaign" }

Validation:
  - Must be unique (UNIQUE index on short_code handles this)
  - Alphanumeric + hyphens only (prevent injection, reserved words)
  - Max length 50 chars
  - Reserve system words: "api", "health", "admin" → blocklist

On conflict: return HTTP 409 Conflict
```

### Rate Limiting
```
Prevent abuse (URL bombing, scraping):
  - 100 shorten requests per IP per hour
  - 1000 redirect requests per IP per minute
  Implementation: Redis counter with TTL
    INCR rate:shorten:{ip}:{hour}
    EXPIRE rate:shorten:{ip}:{hour} 3600
    If count > 100 → return HTTP 429
```

### URL Validation
```
Before storing:
  1. Parse URL (valid scheme: http/https)
  2. Check against blocklist (malware domains, phishing lists)
  3. Check for redirect loops (short URL pointing to another short URL)
  4. Max long URL length: 2048 chars
```

### High Traffic URLs (Hotkeys)
```
Problem: A viral tweet links to abc1234 → 100K requests/second

Solutions:
  1. In-process cache per server handles burst (no Redis roundtrip at all)
  2. If still insufficient: replicate hot key across N Redis instances
     GET url:abc1234:0, :1, :2 → round-robin reads
  3. CDN: cache the redirect response at CDN edge
     (only works for 301, not 302 — tradeoff with analytics)
```

---

## 10. Interview Framework Applied

```
Step 1 — Requirements (5 min): [See Section 1]
Step 2 — Estimation (5 min):   300M URLs, 100:1 read:write, 150GB total
Step 3 — HLD (10 min):         [See architecture diagram, Section 3]
Step 4 — Deep dive (15 min):   Short code generation + caching strategy
Step 5 — Bottlenecks (5 min):  Cache hit rate, hot URLs, write bottleneck (ID gen)
Step 6 — Failures (2 min):     Redis down → fallback to DB; DB down → serve cached
Step 7 — Scale (3 min):        >1 TB → shard by hash(short_code), multi-region

Key numbers to say out loud:
  "150 GB fits on one DB — no sharding needed initially"
  "99% cache hit rate — nearly all redirects never touch MySQL"
  "7-char base62 = 3.5 trillion codes — won't run out for centuries"
  "302 for analytics, 301 for CDN offload — explicit trade-off"
```

---

## 📝 Tasks

### Task 1 — Implement Short Code Generator
Write base62 encode/decode in Java. Handle: encode(0), encode(1), encode(62), encode(62^7 - 1). Verify: decode(encode(n)) == n. Handle collision strategy for MD5 approach.

### Task 2 — Schema Design
Extend the schema to support:
- User accounts owning URLs
- URL groups / campaigns
- Per-URL click analytics (hourly buckets)
- A/B testing (one short code → two long URLs, split traffic)

### Task 3 — Failure Scenarios
Design the failure handling for:
1. Redis cluster completely down
2. MySQL primary goes down mid-write
3. ID generator service is unavailable
4. Analytics Kafka topic has 5-minute lag (consumer backlog)
5. A single URL receives 1M req/sec (DDoS via viral link)

### ⭐ Task 4 — Full Redesign: Multi-Region
Redesign for global deployment (US + EU + APAC):
- Users in each region should get <5ms redirect latency
- URLs created in US should be accessible from EU immediately
- Analytics should be unified across regions
- No user data should leave EU (GDPR)

Design: DNS routing strategy, data replication approach, consistency model for cross-region writes, analytics aggregation.

---

## ✅ Module B5 Completion Checklist

- [ ] Can state all functional + non-functional requirements from memory
- [ ] Can do capacity estimation in <5 minutes (300M URLs, 100:1 ratio, 150GB)
- [ ] Can draw the full architecture diagram with all components
- [ ] Know all 4 short code generation approaches and trade-offs
- [ ] Can implement base62 encode/decode from scratch
- [ ] Know the DB schema with correct indexes
- [ ] Can explain the 2-layer cache strategy (in-process + Redis)
- [ ] Know 301 vs 302 trade-off with analytics implications
- [ ] Can describe the async analytics pipeline (Kafka + ClickHouse)
- [ ] Know all edge cases: expiry, custom aliases, rate limiting, hot URLs
- [ ] Can apply the 7-step HLD framework to URL shortener in 45 minutes
- [ ] Completed Task 1 — base62 encode/decode implementation
- [ ] Completed Task 2 — extended schema design
- [ ] Completed Task 3 — failure scenarios
- [ ] Completed Task 4 — multi-region redesign

<br>

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
  <a href="/learning/system-design/hld/module-b5-url-shortener/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; background: rgba(230, 80, 50, 0.1); color: #e65032; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.9rem; transition: background 0.2s;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    BACK TO VISUAL PAGE
  </a>
  <a href="/learning/system-design/hld/module-b6-twitter-feed/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; background: rgba(255, 255, 255, 0.05); color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.9rem; transition: background 0.2s;">
    NEXT: MODULE B6
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>
