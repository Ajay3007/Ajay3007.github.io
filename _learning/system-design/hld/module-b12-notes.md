---
layout: learning
title: "Module B12 Notes: System Design Interview Framework"
permalink: /learning/system-design/hld/module-b12-notes/
---

# Module B12 — System Design Interview Framework & Mock Interviews
## System Design Mastery Course | Track B: HLD | Week 22

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Capstone
**Prerequisites:** B1–B11 (all HLD modules)
**Goal:** All the knowledge from B1–B11 means nothing if you can't communicate it under interview pressure. This module teaches the structured framework, time management, communication patterns, and gives 6 full mock interview problems — one per day — to practice before any real interview.

---

## 1. The 7-Step Framework (45-Minute Interview)

```
STEP 1 — REQUIREMENTS CLARIFICATION (5 min)
  Functional requirements:  What must the system DO?
  Non-functional requirements: How must it perform? (scale, latency, availability)
  Out of scope: What are you explicitly NOT designing?

  Questions to always ask:
  "How many daily active users?"
  "What is the read:write ratio?"
  "Is this globally distributed or single-region?"
  "What is the acceptable latency for the hot path?"
  "Do we need strong consistency, or is eventual consistency OK?"
  "What is the expected data retention period?"

STEP 2 — CAPACITY ESTIMATION (5 min)
  Storage:   daily_writes × avg_object_size × retention_years
  Throughput: peak_qps = (daily_requests × peak_factor) / 86400
  Bandwidth:  peak_qps × avg_response_size
  Cache:      hot_set = total_data × 0.2 (80/20 rule)

  Key numbers to memorize:
  1 million users × 1 req/day = 12 QPS sustained
  1 billion req/day = ~11,600 QPS = ~12K QPS
  1 KB × 1M rows = 1 GB
  86,400 seconds/day (approx as 100K for rough math)

STEP 3 — HIGH-LEVEL DESIGN (10 min)
  Draw the major components: clients, LB, services, caches, DBs, queues
  Don't over-detail yet — stay at the box-and-arrow level
  Cover: data flow for the primary use case (write path + read path)

STEP 4 — DATA MODEL & API DESIGN (5 min)
  Core tables/documents: fields, primary keys, indexes
  Critical API endpoints: method, URL, request, response
  Don't design ALL tables — only the ones that matter for discussion

STEP 5 — DEEP DIVE (15 min)
  Pick 2–3 components the interviewer cares about most
  Typically: the read hot path, the write bottleneck, or the consistency challenge
  This is where B1–B11 knowledge is applied
  Go deep on trade-offs — show you've thought about alternatives

STEP 6 — BOTTLENECKS & SCALING (4 min)
  Where does your design break as scale increases 10×?
  How would you address each bottleneck?
  Show awareness of: single points of failure, hot spots, thundering herd

STEP 7 — SUMMARY (1 min)
  Restate the key decisions and why
  Mention what you'd do differently with more time
```

---

## 2. Requirements Framework — What to Always Cover

### Functional Requirements Template
```
Write: What does the user CREATE/UPDATE/DELETE?
Read:  What does the user VIEW/SEARCH/QUERY?
The non-obvious ones that impress interviewers:
  - "Should deletes be soft deletes? (data retention compliance)"
  - "Do we need audit logging for GDPR/SOX?"
  - "Should reads be eventually consistent (cheaper) or strongly consistent (expensive)?"
```

### Non-Functional Requirements Template
```
Scale:        DAU, MAU, writes/sec, reads/sec
Latency:      p50, p99 targets for hot paths
Availability: 99.9% (8.7 hrs/yr downtime) vs 99.99% (52 min/yr)
Durability:   can we lose data? RPO (recovery point objective)
Consistency:  strong vs eventual — and for which operations?
Geo:          single region or multi-region? GDPR constraints?
```

---

## 3. Capacity Estimation Cheat Sheet

```
Memory units:
  1 char = 1 byte
  UUID = 16 bytes
  int32 = 4 bytes, int64 = 8 bytes
  timestamp = 8 bytes
  average tweet/message = 140 bytes–1 KB
  average photo = 1 MB (thumbnail: 10–50 KB)
  average video = 50–500 MB

Time units:
  1 day = 86,400 seconds ≈ 100K (for estimates)
  1 month ≈ 2.5M seconds
  1 year ≈ 31.5M seconds ≈ 30M

Traffic conversions:
  1M req/day = 12 QPS sustained, 36 QPS peak (3× peak factor)
  10M req/day = 120 QPS sustained, 360 QPS peak
  1B req/day = 12,000 QPS sustained, 36,000 QPS peak

Storage math shortcut:
  1M users × 1 KB/user = 1 GB
  1B users × 1 KB/user = 1 TB
  1B users × 1 MB/user = 1 PB

Server capacity rules of thumb (for estimation):
  1 commodity server: ~10K–20K QPS (simple reads from cache)
  1 commodity server: ~1K–5K QPS (DB reads with disk I/O)
  1 commodity server: ~100–500 QPS (writes with replication)
  1 Redis node: ~100K–500K simple ops/sec
  1 Kafka broker: ~1M messages/sec (1 KB messages)
```

---

## 4. Communication Patterns (What Interviewers Actually Listen For)

### State your reasoning before your answer
```
❌ Bad: "I'll use Cassandra."
✓ Good: "For the write-heavy timeline feed with 50K writes/sec and TTL-based
         expiry, I'd use Cassandra. Its LSM tree handles write throughput well,
         and I can model the timeline as a wide row partitioned by user_id."
```

### Acknowledge trade-offs proactively
```
❌ Bad: "Redis is the best cache."
✓ Good: "Redis solves the hot-read problem well here, but it adds operational
         complexity — we'll need a cache invalidation strategy and we need to
         size it carefully. The alternative is read replicas, which are simpler
         but higher latency. Given the 10ms SLA, Redis is worth the complexity."
```

### Drive the conversation, don't wait to be asked
```
❌ Passive: [waits for interviewer to ask about failures]
✓ Active: "Now let me think about failure modes. The notification service is
           non-critical, so I'll make it async. The payment service is critical
           — I need to think about what happens if it's slow or unavailable..."
```

---

## 5. Common Mistakes (and How to Avoid Them)

```
MISTAKE 1: Jumping to solutions before clarifying requirements
  Fix: Spend 5 minutes on requirements. Interviewer may reveal constraints
       that completely change the design.

MISTAKE 2: Designing a perfect single-machine system
  Fix: Always think distributed. Ask about scale first.

MISTAKE 3: Avoiding trade-offs
  Fix: Every choice has a cost. Acknowledge trade-offs before being asked.

MISTAKE 4: Not knowing your numbers
  Fix: Do the math. "1B req/day = 12K QPS × 3 peak = 36K peak QPS."

MISTAKE 5: Designing in a vacuum, not collaborating
  Fix: Check in every few minutes. "Does this direction make sense?"

MISTAKE 6: Spending too long on the "obvious" parts
  Fix: Cover basics quickly. Save time for distributed systems problems.

MISTAKE 7: Not handling failures
  Fix: Proactively cover: circuit breakers, retries, dead letter queues.
```

---

## 6. Six Mock Interview Problems

### Mock 1 — Design Pastebin / URL Shortener (Warmup)
```
Scale: 1M pastes/day, 100M reads/day, max paste size 10 MB
Key decisions: ID generation (base62), text in S3 vs DB, expiry, CDN, async analytics
Deep dive: cache tier, ID collision, lazy vs background expiry cleanup
Time: 45 minutes
```

### Mock 2 — Design a Notification System
```
Scale: 10M notifications/day across 3 channels, delivery within 30 seconds
Key decisions: channel routing, priority, user preferences, retry/fallback, deduplication
Deep dive: retry/fallback strategy, deduplication, delivery receipts
Time: 45 minutes
```

### Mock 3 — Design a Distributed Job Scheduler (Medium-Hard)
```
Scale: 1M jobs, 1K jobs/sec triggering at peak, at-most-once execution
Key decisions: storage, polling vs time-wheel, leader election, exactly-once, crash recovery
Deep dive: exactly-once execution, partition assignment, failure recovery
Time: 45 minutes
```

### Mock 4 — Design Google Drive / Dropbox (Hard)
```
Scale: 50M DAU, 100M uploads/day, avg file 500KB, total storage 10 PB
Key decisions: chunked upload (4MB + SHA-256 dedup), delta sync, metadata DB + S3, conflict resolution
Deep dive: chunk deduplication, delta sync algorithm, last-write-wins vs OT
Time: 45 minutes
```

### Mock 5 — Design a Live Streaming Platform (Hard)
```
Scale: 1K concurrent streamers, 10M viewers, peak 100K viewers per stream, <10s latency
Key decisions: RTMP ingest → HLS transcode, CDN fan-out, WebSocket chat, HyperLogLog viewer count
Deep dive: transcoding pipeline, chat fan-out at 100K viewers, approximate viewer count
Time: 45 minutes
```

### Mock 6 — Design a Search Autocomplete System (Medium)
```
Scale: 10K QPS autocomplete, 100M unique queries/day in logs
Key decisions: trie vs inverted index, precompute top-N, daily batch update, shard by prefix
Deep dive: trie sharding, pre-computation pipeline, unicode handling
Time: 45 minutes
```

---

## 7. Quick Answers Cheat Sheet

```
Q: "How do you handle hot partitions?"
A: "Add suffix (0–9) to partition key to spread across 10× more partitions.
    Or: consistent hashing with virtual nodes. Or: cache hot keys in Redis."

Q: "How do you handle thundering herd on cache miss?"
A: "Probabilistic early expiration, or mutex/semaphore on cache miss —
    only one thread refreshes, others wait. Redis: SETNX as a lock."

Q: "How do you achieve exactly-once processing?"
A: "Kafka at-least-once + idempotent consumer. Check idempotency key
    before processing. Transactional Kafka (EOS) for stronger guarantees."

Q: "How do you handle cascading failures?"
A: "Circuit breaker: open after N failures, fail fast, half-open probe after timeout.
    Bulkhead: isolate thread pools per downstream service."

Q: "How would you design for multi-region?"
A: "Active-active with eventual consistency (DynamoDB global tables).
    Or active-passive with failover. Latency-based routing (Route 53)."

Q: "How do you do schema migrations on a live table?"
A: "Expand-contract: add new column (nullable), dual-write to both,
    backfill old rows, switch reads to new column, drop old column.
    Never ALTER TABLE on a large live table — takes a lock."
```

---

## ✅ Completion Checklist

- [ ] 7-step framework memorized — can recite step names + times
- [ ] Capacity estimation: storage, throughput, bandwidth formulas
- [ ] Key numbers: 1B req/day = 12K QPS, 1M users × 1KB = 1 GB
- [ ] Requirements questions: 6 functional + 6 non-functional to always ask
- [ ] Communication: state reasoning before answer, proactive trade-offs
- [ ] Common mistakes: 7 mistakes identified and internalized
- [ ] Quick answers: hot partitions, thundering herd, exactly-once, circuit breakers
- [ ] Mock 1: Pastebin — completed timed 45-min session
- [ ] Mock 2: Notifications — completed timed 45-min session
- [ ] Mock 3: Job Scheduler — completed timed 45-min session
- [ ] Mock 4: Google Drive — completed timed 45-min session
- [ ] Mock 5: Live Streaming — completed timed 45-min session
- [ ] Mock 6: Autocomplete — completed timed 45-min session

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b11-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B11 Distributed TX Notes</a>
  <a href="/learning/system-design/hld/module-b12-interview-framework/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b13-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B13 ML Systems →</a>
</div>
