---
title: "Module B3 — Caching | Full Notes"
description: "System Design Roadmap › HLD Hub › Module B3 › Full Notes ⚡ Interactive Visual Version ← Recommended for learning."
domain: system-design
track: system-design-hld
order: 107
url: /learning/system-design/hld/module-b3-notes/
---

<div style="margin-bottom:1.5rem;">
  <a href="/learning/system-design/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">System Design Roadmap</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">HLD Hub</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/module-b3-caching/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">Module B3</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <span style="color:var(--text-color);font-size:0.85rem;font-weight:600;">Full Notes</span>
</div>

<div style="margin-bottom:2rem;">
  <a href="/learning/system-design/hld/module-b3-caching/" style="display:inline-block;padding:0.5rem 1.1rem;background:rgba(0,212,170,0.1);color:#00d4aa;border:1px solid rgba(0,212,170,0.3);border-radius:6px;font-size:0.85rem;font-weight:600;text-decoration:none;">⚡ Interactive Visual Version</a>
  <span style="margin-left:0.8rem;font-size:0.82rem;color:var(--light-text);">← Recommended for learning. This page is the printable reference.</span>
</div>

# Module B3 — Caching
## System Design Mastery Course | Track B: HLD | Week 13

---

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** B — High-Level Design (HLD)  
**Prerequisites:** B1 (HLD Fundamentals), B2 (Databases at Scale)  
**Goal:** Caching is the most common tool for scaling read-heavy systems. Used correctly, it turns database disasters into non-events. Used incorrectly, it causes subtle data corruption and thundering herds. Master it.

### Module B3 Topics

| Topic | Core Insight |
|-------|-------------|
| Why Cache | Memory is 1000× faster than disk; cache = trading space for time |
| Cache-Aside | Most common pattern; application controls cache |
| Write-Through | Write DB and cache together; strong consistency |
| Write-Back | Write cache first, DB asynchronously; risk of loss |
| Read-Through | Cache sits in front; transparently fetches from DB |
| Cache Eviction | LRU, LFU, TTL — when to expire stale data |
| Cache Invalidation | Hardest problem in CS; several strategies |
| Cache Stampede | Thundering herd on cold cache; prevention |
| Redis Data Structures | Strings, Hashes, Sets, Sorted Sets, Lists |
| CDN | Geographic caching for static + dynamic content |

---

## 1. Why Cache?

### The Speed Gap
```
RAM access:      ~100 ns      (in-process cache, HashMap)
Redis access:    ~0.5 ms      (network roundtrip to Redis)
SSD DB read:     ~1–5 ms      (cold query, disk I/O)
HDD DB read:     ~10–50 ms    (spinning disk + query execution)
Cross-region:    ~100–300 ms

→ Redis is 10–100× faster than a DB query.
→ In-process cache (HashMap) is 100,000× faster than disk.
```

### When to Cache
```
✅ Read-heavy workloads (reads >> writes)
✅ Data that changes infrequently (user profiles, product catalog)
✅ Expensive computation results (aggregations, ML predictions)
✅ Session storage (replaces sticky sessions)
✅ Rate limiting counters
✅ Leaderboards, ranked lists

❌ Write-heavy data that changes on every request
❌ Data that must always be fresh (real-time stock prices)
❌ Data that is user-specific and rarely re-read (long tail)
❌ When cache hit rate is low (<50%) — overhead not worth it
```

### Cache Hit Rate
```
Hit Rate = Cache Hits / (Cache Hits + Cache Misses)

Target: > 80% for caching to be worthwhile
Excellent: > 99% (e.g., Twitter's timeline cache)

If hit rate is low:
  - Cache size is too small (not enough entries fit)
  - TTL is too short (items expire before re-read)
  - Data is too diverse / long-tail (Pareto 80/20 doesn't apply)
  - Wrong data is being cached
```

---

## 2. Cache-Aside (Lazy Loading) — Most Common

### Pattern
```
READ path:
  1. Check cache: cache.get(key)
  2. If HIT: return cached value
  3. If MISS:
       a. Fetch from DB: db.get(key)
       b. Write to cache: cache.set(key, value, TTL)
       c. Return value

WRITE path:
  1. Write to DB: db.set(key, value)
  2. Invalidate (or update) cache: cache.delete(key)
     (Delete is safer than update — avoids stale-write race)
```

### Implementation
```java
class UserService {
    private final Cache  cache;
    private final UserDB db;

    public User getUser(long userId) {
        String cacheKey = "user:" + userId;

        // 1. Try cache
        User cached = cache.get(cacheKey);
        if (cached != null) return cached;     // CACHE HIT

        // 2. Cache miss — fetch DB
        User user = db.findById(userId);

        // 3. Populate cache with TTL
        cache.set(cacheKey, user, Duration.ofMinutes(30));
        return user;                           // CACHE MISS
    }

    public void updateUser(long userId, UserUpdate update) {
        db.update(userId, update);
        cache.delete("user:" + userId);        // INVALIDATE on write
    }
}
```

### Pros & Cons
```
✅ Only caches data that is actually requested (no wasted memory)
✅ DB failures degrade gracefully (cache still serves stale data)
✅ Simple to implement; application has full control

❌ First request after miss (or after TTL expiry) is slow
❌ Cache can hold stale data between write and next read
❌ Potential race condition: two concurrent misses both query DB
```

---

## 3. Write-Through Cache

### Pattern
```
WRITE path:
  1. Write to cache
  2. Synchronously write to DB
  3. Confirm to client only after BOTH succeed

READ path:
  Same as cache-aside (cache has the data after write)
```

### Implementation
```java
public void updateUser(long userId, User user) {
    // Write cache and DB atomically (or with retry on failure)
    db.update(userId, user);               // 1. Write DB first
    cache.set("user:" + userId, user);     // 2. Update cache
    // Client confirms after both succeed
}
```

### When to Use
```
✅ Read-after-write consistency required (user immediately sees their update)
✅ Cache is the primary data store (Memcached as write-through in front of DB)
✅ Write patterns are predictable

❌ Adds latency to writes (two writes per operation)
❌ Writes cache data that may never be re-read (wasted memory)
   → Combine with TTL to evict cold data
```

---

## 4. Write-Back (Write-Behind) Cache

### Pattern
```
WRITE path:
  1. Write to cache immediately (fast ACK to client)
  2. Asynchronously flush to DB in background

READ path:
  1. Read from cache (always has latest data)
```

### When to Use
```
✅ Write-heavy workloads (counters, view counts, real-time metrics)
✅ Writes can be batched (more efficient DB writes)
✅ Temporary data loss is acceptable

❌ If cache crashes before flush → recent writes lost
❌ DB may be temporarily inconsistent with cache
❌ More complex to implement correctly

Example: Like counter — write to Redis immediately, flush to DB every 30 seconds.
         If Redis crashes, you lose the last 30 seconds of likes. Acceptable trade-off.
```

---

## 5. Read-Through Cache

### Pattern
```
READ path:
  1. Application asks cache for key
  2. If HIT: cache returns value
  3. If MISS: cache (not application) fetches from DB, stores, returns

Application code never talks to DB directly — cache is the abstraction layer.

Difference from cache-aside:
  Cache-aside: APPLICATION fetches DB on miss and populates cache
  Read-through: CACHE fetches DB on miss and populates itself
```

### When to Use
```
✅ Simplifies application code (single data access point)
✅ Cache library handles miss logic
✅ Good for read-heavy access patterns

❌ Cold start: all first reads are slow until cache warms up
❌ Less control over what gets cached vs cache-aside
❌ DB connection from cache layer (adds coupling)

Used by: JCache (JSR-107), Spring Cache abstraction, Hibernate 2nd-level cache
```

---

## 6. Cache Eviction Policies

### LRU — Least Recently Used
```
Evict the entry that hasn't been accessed for the longest time.

Implementation: Doubly-linked list + HashMap
  HashMap: O(1) lookup by key
  List:    Most-recently-used at head, least-recently at tail
  On access: move entry to head
  On evict:  remove tail entry

Best for: General-purpose caching — recently accessed data likely re-accessed.
Used by: Redis (allkeys-lru policy), most systems
```

### LFU — Least Frequently Used
```
Evict the entry with the fewest total accesses.

Implementation: HashMap + frequency heap
  On access: increment access count
  On evict:  remove entry with minimum count

Best for: Data where some items are popular long-term (not just recently).
          Avoids cache pollution from one-time large scans.
Used by: Redis (allkeys-lfu policy, available since Redis 4.0)
```

### TTL — Time-To-Live
```
Each entry has an expiration timestamp.
After TTL expires, entry is invalid and will be re-fetched on next access.

Best for: Data that goes stale after a known time interval.
  cache.set("session:abc", sessionData, 3600);  // 1 hour TTL

Pitfall: Thundering herd — many keys with the same TTL expire simultaneously
         → All misses hit DB at the same time
Solution: TTL jitter — add random ±0..10% to TTL to spread expirations
```

---

## 7. Cache Invalidation

> "There are only two hard things in Computer Science: cache invalidation and naming things." — Phil Karlton

### Strategies

#### Delete on Write (Most Common)
```java
void updateProduct(long id, Product p) {
    db.update(id, p);
    cache.delete("product:" + id);          // Invalidate
    cache.delete("products:category:" + p.getCategoryId()); // Invalidate list too!
}

// Next read will miss → fetch fresh from DB → repopulate
```

#### Version-Based Keys
```
Instead of invalidating, embed a version in the key.
When data changes, bump the version.

"product:42:v8"  →  "product:42:v9"

Old key naturally expires via TTL.
No explicit invalidation needed.
Useful for: config data, feature flags, rarely-changing reference data.
```

#### Event-Based Invalidation
```
Subscribe to DB change events (CDC — Change Data Capture).
When DB row changes, publish event → cache consumers invalidate.

DB → Debezium/CDC → Kafka topic → Cache invalidation service → Redis.delete(key)

Pros: Decoupled, real-time, works for distributed caches
Cons: More infrastructure, event delivery latency, ordering guarantees needed
```

### The Invalidation Race Condition
```
Thread A: UPDATE product WHERE id=42
Thread B: SELECT product WHERE id=42 → MISS → read DB (before A commits)
Thread A: DELETE cache key "product:42"
Thread B: SET cache "product:42" = stale value (old DB read)

Result: Cache holds stale data indefinitely (until TTL expires)!

Prevention:
  1. Use "delete on write" not "update on write" (always safer)
  2. Use cache.set only if cache.get is still null (double-check)
  3. Use database transactions to ensure delete happens after write
  4. Accept small stale window (set short TTL as safety net)
```

---

## 8. Cache Stampede (Thundering Herd)

### The Problem
```
Scenario:
  - Popular cache key (e.g., homepage data) expires at T=0
  - 10,000 requests arrive per second
  - All 10,000 miss the cache simultaneously
  - All 10,000 query the DB simultaneously
  - DB is overwhelmed → latency spikes → system degraded

This is "thundering herd" or "cache stampede"
```

### Solutions

#### Probabilistic Early Expiration (PER)
```
Before TTL expires, probabilistically start refreshing based on remaining TTL.
The closer to expiration, the higher the probability of early refresh.

// Each request checks:
if (remainingTTL < randomExpiry()) { refresh(); }

Only ONE request triggers the refresh at a time.
Others continue serving (slightly stale) cached value.
```

#### Mutex / Lock on Miss
```java
String get(String key) {
    String val = cache.get(key);
    if (val != null) return val;                 // HIT

    // MISS — try to acquire lock
    boolean locked = cache.setnx("lock:" + key, "1", 10_seconds);
    if (locked) {
        try {
            val = db.get(key);
            cache.set(key, val, TTL);
            return val;
        } finally {
            cache.delete("lock:" + key);
        }
    } else {
        // Another thread is refreshing — wait briefly and retry
        Thread.sleep(50);
        return get(key);                         // Retry
    }
}
// Only ONE thread queries DB; others wait and get cached value.
```

#### Background Refresh
```
Cache entry stores both value AND last_refresh_time.
Background job constantly refreshes popular keys before they expire.

pros: Zero miss latency for hot keys
cons: Wasted refreshes for cold keys; need popularity tracking
Used by: CDNs (stale-while-revalidate header)
```

---

## 9. Redis Data Structures

### String — Most Basic
```
SET user:42:name "Ajay Sharma"
GET user:42:name

INCR view_count:post:123      → atomic increment (perfect for counters)
SETEX session:abc 3600 data   → set with TTL

Use for: Counters, feature flags, session data, rate limiting tokens
```

### Hash — Object Storage
```
HSET user:42 name "Ajay" email "a@b.com" tier "pro"
HGET user:42 name            → "Ajay"
HMGET user:42 name tier      → ["Ajay", "pro"]
HINCRBY user:42 login_count 1

Use for: User profiles, configuration objects, shopping carts
Benefit: Fetch individual fields without deserializing entire object
```

### List — Queue / Stack
```
RPUSH queue:email email1 email2  → push to tail
LPOP  queue:email                → pop from head (FIFO queue)
LRANGE queue:email 0 9           → peek at first 10

Use for: Job queues, activity feeds, recent items, notifications
```

### Set — Unique Members
```
SADD  active_users 42 88 123
SISMEMBER active_users 42    → 1 (true)
SUNION  set1 set2            → union
SINTER  followers:A followers:B  → mutual followers

Use for: Tagging, unique visitor tracking, friend recommendations
```

### Sorted Set (ZSet) — Ranked Data
```
ZADD  leaderboard 9800 "player:alice"
ZADD  leaderboard 9500 "player:bob"
ZRANGE leaderboard 0 9 WITHSCORES REV  → top 10 players

ZADD  rate_limit:user:42 <timestamp> <request_id>  → sliding window
ZRANGEBYSCORE rate_limit:user:42 (now-60s) now     → requests in last minute

Use for: Leaderboards, rate limiting (sliding window), priority queues,
         proximity search (GEOADD uses sorted sets internally)
```

---

## 10. CDN (Content Delivery Network)

### What CDN Does
```
Distributes content to edge nodes geographically close to users.
Serves cached content from nearest edge instead of origin server.

Without CDN:
  User (Mumbai) → Origin Server (US-East) = ~200ms

With CDN:
  User (Mumbai) → CDN Edge (Singapore) = ~15ms → cache hit
  User (Mumbai) → CDN Edge (Singapore) → Origin (US-East) = ~200ms (miss, first time only)
```

### Static vs Dynamic Caching
```
STATIC content (images, CSS, JS, fonts):
  Cache-Control: max-age=31536000, immutable
  CDN caches for 1 year → hash-based filenames for cache busting
  Netflix: 90% of traffic is CDN-served video chunks

DYNAMIC content (API responses, personalised pages):
  Cache-Control: max-age=60  → cache for 60 seconds
  Vary: Accept-Encoding      → separate cache per compression type
  ESI (Edge Side Includes)   → cache page fragments individually

PRIVATE content (user-specific):
  Cache-Control: private, no-store  → CDN does NOT cache
  Goes directly to origin
```

### Cache Busting
```
Problem: You deploy new JS but users get cached old version.

Solution 1: Hash-based filenames
  app.js → app.8f3d92ab.js   (content hash in filename)
  New deploy → new hash → new URL → CDN fetches fresh copy

Solution 2: Query parameters (less reliable)
  app.js?v=2024-01-15        (CDN may ignore query params)

Solution 3: CDN Purge API
  Call CDN's purge endpoint after deploy.
  Instantaneous but requires coordination with deploy pipeline.
```

---

## 📝 Tasks

### Task 1 — Cache Strategy Selection
For each system/feature, choose: cache-aside, write-through, write-back, or no cache. Justify your choice including the consistency trade-off.

1. E-commerce product page (price + inventory)
2. Social media post like count (500M likes/day)
3. Bank account balance before a debit
4. User authentication session (JWT + server-side session)
5. Trending hashtags computed every 5 minutes
6. Real-time stock price feed

### Task 2 — LRU Cache Implementation
Implement a thread-safe LRU cache with O(1) get and put.

```
API:
  int get(int key)              → -1 if absent
  void put(int key, int value)  → evict LRU if at capacity

Constraints:
  - Thread-safe (ConcurrentHashMap + ReentrantLock or synchronized)
  - O(1) get and put
  - Correct eviction order under concurrent access
  - Bonus: extend to support TTL per entry
```

### Task 3 — Cache Stampede Prevention
Design a cache layer for a news website homepage:
- 1M concurrent users
- Homepage data computed from 50 DB queries (takes 500ms)
- Currently: cache TTL = 60 seconds
- Problem: Every 60 seconds, a stampede hits the DB

Design a solution that:
1. Eliminates the stampede completely
2. Keeps homepage latency < 50ms for 99% of requests
3. Handles cache server failure gracefully
4. Explain the consistency trade-off of your approach

### Task 4 — Design a Rate Limiter with Redis
Implement a distributed rate limiter using Redis:

```
Requirements:
  - Per-user limit: 100 requests per 60-second window
  - Sliding window algorithm (not fixed window)
  - Multi-server deployment (Redis is shared)
  - Return: allow/deny + requests remaining + reset time

Algorithms to implement and compare:
  A) Fixed Window Counter (INCR + EXPIRE)
  B) Sliding Window Log (Sorted Set by timestamp)
  C) Sliding Window Counter (hybrid of A+B)

For each: show Redis commands, time complexity, memory usage, and trade-offs.
```

---

## 💡 Interview Tips — Caching

| Question | Strong Answer |
|----------|--------------|
| "How does cache-aside work?" | Application checks cache first; on miss, queries DB and populates cache. On write, invalidates cache key. Simple, resilient, most common pattern. |
| "What is thundering herd?" | When a popular cache key expires, thousands of concurrent requests all miss and hammer the DB simultaneously. Prevent with: mutex lock on miss, probabilistic early expiration, or background refresh. |
| "How to handle cache invalidation?" | Delete-on-write is safest (avoids write race). Can use TTL as safety net. For complex dependencies, use event-based invalidation via CDC + Kafka. |
| "Write-through vs write-back?" | Write-through: strong consistency, slow writes. Write-back: fast writes, risk of data loss if cache crashes before flush. Write-back for non-critical high-frequency writes (view counts). |
| "What Redis structure for rate limiting?" | Sorted Set (ZSet) for sliding window: score = timestamp, member = request_id. Count members in (now - window) to (now). ZRANGEBYSCORE + ZCARD = atomic with pipeline. |
| "Cache hit rate is 40% — what do you do?" | Investigate: Is the cache too small? Is TTL too short? Is it a long-tail data pattern? Add monitoring, increase size, adjust TTL, or reconsider whether caching is the right tool. |

---

## ✅ Module B3 Completion Checklist

- [ ] Understand why cache works: latency numbers, memory vs disk speed gap
- [ ] Can implement cache-aside (read + write paths) from memory
- [ ] Know write-through vs write-back trade-offs and when to use each
- [ ] Understand cache stampede and can explain 3 prevention strategies
- [ ] Know LRU vs LFU vs TTL eviction policies
- [ ] Understand the invalidation race condition and how to prevent it
- [ ] Know all 5 Redis data structures and their use cases
- [ ] Can design a sliding window rate limiter with Redis Sorted Sets
- [ ] Know CDN: static vs dynamic caching, cache busting strategies
- [ ] Completed Task 1 — cache strategy selection (6 scenarios)
- [ ] Completed Task 2 — thread-safe LRU cache with TTL bonus
- [ ] Completed Task 3 — cache stampede prevention design
- [ ] Completed Task 4 — distributed rate limiter (3 algorithms)

**→ Next: Module B4 — Message Queues (Kafka, RabbitMQ, async patterns)**
