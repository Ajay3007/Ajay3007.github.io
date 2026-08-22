---
title: "Module C2: Geo-Distribution & Multi-Region — Study Notes"
description: "Module C2 · Week 26 · Track C — Advanced Topics Prerequisites: B1–B14, C1 Goal: Multi-region replication, active-active, latency-based routing, disaster recovery ⚡ Interactive…"
domain: system-design
track: system-design-hld
order: 205
url: /learning/system-design/hld/module-c2-notes/
---

<div style="margin-bottom:24px;padding:14px 20px;background:#e0fafb;border-left:4px solid #00b8c8;border-radius:0 4px 4px 0;font-family:'JetBrains Mono',monospace;font-size:13px;">
  <strong>Module C2 · Week 26 · Track C — Advanced Topics</strong><br>
  <span style="color:#666;">Prerequisites: B1–B14, C1 &nbsp;|&nbsp; Goal: Multi-region replication, active-active, latency-based routing, disaster recovery</span>
</div>

<a href="/learning/system-design/hld/module-c2-geo-distribution/" style="display:inline-block;margin-bottom:32px;padding:10px 20px;background:#00b8c8;color:#fff;border-radius:4px;text-decoration:none;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;">⚡ Interactive Visual Version</a>

# Module C2 — Geo-Distribution & Multi-Region Architecture
## System Design Mastery Course | Track C: Advanced Topics | Week 26

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** C — Advanced Topics
**Prerequisites:** B1–B12, C1
**Goal:** Single-region systems fail entirely when a cloud region goes down. Multi-region systems are fundamentally harder — you're trading local consistency for global availability. This module covers the full spectrum: active-passive failover, active-active with conflict resolution, CRDTs, data residency (GDPR), and the real latency math that drives every multi-region design decision.

---

## 1. Why Go Multi-Region?

```
Three distinct motivations (different solutions for each):

1. AVAILABILITY — survive a full region outage
   AWS us-east-1 goes down (has happened: 2017, 2021, 2023)
   Solution: active-passive or active-active failover

2. LATENCY — serve users from nearby geography
   Tokyo user hitting us-east-1: ~140ms RTT
   Tokyo user hitting ap-northeast-1: ~5ms RTT
   Solution: read replicas or active-active in nearest region

3. COMPLIANCE — data residency regulations
   GDPR (EU): EU user data must remain within EU borders
   India PDPB: Indian personal data must stay in India
   Solution: regional data partitioning + geo-routing

Clarifying question in interviews:
  "Which of these three are we solving? Availability, latency, or compliance?"
  Each leads to a significantly different architecture.
```

---

## 2. Speed of Light — The Unavoidable Constraint

```
Network round-trip times between major regions (approximate, real-world):

Within a single AZ:          ~0.5 ms
Cross-AZ (same region):      ~1–2 ms
US East → US West:           ~70 ms
US East → EU West:           ~85 ms
US East → Asia Pacific:      ~140 ms
EU → Asia Pacific:           ~130 ms
EU West → EU Central:        ~20 ms
Within Asia Pacific:         ~50–80 ms

Implications for distributed systems:
  Synchronous replication US→EU: adds 85ms to every write
  Raft consensus US+EU+APAC: quorum needs 2 of 3 regions
    → write latency = max(US→EU, US→APAC) = ~140ms
    → unacceptable for interactive workloads

  Rule of thumb: synchronous cross-region consensus ≈ 1 RTT to furthest node
  Asynchronous replication: near-zero write latency, seconds of replication lag
```

---

## 3. Active-Passive (Primary-Secondary)

```
One region is PRIMARY (serves all reads and writes).
Other region(s) are STANDBY (replicate from primary, serve nothing normally).

Replication:
  Synchronous: primary waits for standby ACK before committing
    → RPO = 0 (zero data loss)
    → Higher write latency (must wait for cross-region ACK)
    → Standby unavailability blocks primary writes

  Asynchronous: primary commits immediately, replication happens in background
    → RPO = seconds (may lose last few seconds of writes on failover)
    → No write latency penalty
    → Standard choice for most active-passive setups

Failover:
  Manual:    Ops team detects outage, manually promotes standby → RTO = minutes-hours
  Automatic: Health checks detect primary failure, auto-promote standby → RTO = 30–120s
    Challenge: detecting true failure vs transient network issue (false positive failover)
    Risk: split-brain if primary recovers while standby is already promoted

RTO and RPO:
  RPO (Recovery Point Objective): max acceptable data loss
    → synchronous replication: RPO=0
    → asynchronous replication: RPO=seconds
  RTO (Recovery Time Objective): max acceptable downtime
    → automatic failover: RTO=30–120s
    → manual failover: RTO=minutes–hours

Use cases:
  Most databases (MySQL with async replicas, PostgreSQL streaming replication)
  Single-master datastores when consistency is paramount
  Simple systems that rarely fail and can tolerate brief downtime
```

---

## 4. Active-Active

```
Multiple regions all serve reads AND writes simultaneously.
No primary — all regions are peers.

Requirement: writes in different regions must eventually converge to the same state.

Approaches to convergence:

1. Last-Write-Wins (LWW)
   Each write carries a timestamp. On conflict: highest timestamp wins.
   Simple but lossy — concurrent writes to same key: one silently lost.
   Used by: Cassandra (default), DynamoDB (in some configurations)
   Acceptable for: sessions, caches, non-financial counters

2. Multi-Version Concurrency (vector clocks)
   Each write carries a vector clock tracking causality.
   Concurrent writes detected and surfaced to application.
   Application must resolve conflicts explicitly.
   Used by: Riak, Dynamo (original Amazon)
   Complex for applications to handle correctly.

3. CRDTs (Conflict-free Replicated Data Types)
   Data structures that merge automatically — no conflicts possible.
   Mathematical guarantee: any two replicas, merged in any order, produce same result.
   (Covered in depth in Section 5)

4. Operational Transformation (OT)
   Used for collaborative editing (Google Docs).
   Operations transformed against concurrent operations before applying.
   Complex to implement correctly; largely superseded by CRDTs.
```

---

## 5. CRDTs — Conflict-Free Replicated Data Types

```
Key insight: design data structures where concurrent updates ALWAYS merge correctly,
             regardless of order or number of replicas.

Mathematical property: Commutative, Associative, Idempotent merge operation.
  merge(A, B) == merge(B, A)          ← commutative: order doesn't matter
  merge(merge(A,B), C) == merge(A, merge(B,C))  ← associative: grouping doesn't matter
  merge(A, A) == A                    ← idempotent: duplicate merge = same result

--- G-Counter (Grow-only Counter) ---
State: vector of counts, one per node. Node i only increments slot i.
  Node A: [3, 0, 0]  (incremented 3 times)
  Node B: [0, 5, 0]  (incremented 5 times)
  Node C: [0, 0, 2]  (incremented 2 times)
Merge: take max of each slot → [3, 5, 2]
Value: sum all slots → 10
Concurrent increments on different nodes → always merge correctly.
Real use: view counters, like counts, event counts

--- PN-Counter (Positive-Negative Counter) ---
Two G-Counters: P (positive/increments) and N (negative/decrements)
Value = sum(P) - sum(N)
Allows decrement while remaining CRDT.
Real use: shopping cart item count, inventory approximation

--- G-Set (Grow-only Set) ---
Elements can only be added, never removed.
Merge: union of both sets.
Real use: tag sets, feature flags, immutable membership lists

--- 2P-Set (Two-Phase Set) ---
Two G-Sets: Add-set (A) and Remove-set (R).
Element present if: in A and NOT in R.
Once removed, cannot be re-added (remove is permanent).
Merge: union both A-sets, union both R-sets.

--- OR-Set (Observed-Remove Set) ---
Each element tagged with unique ID on add.
Remove only removes elements with specific tag (not all copies).
Allows add-remove-add correctly.
Real use: collaborative editing, presence systems

--- LWW-Register (Last-Write-Wins Register) ---
Stores single value with timestamp.
Merge: take value with highest timestamp.
Simple but: timestamp must be monotonic, concurrent writes = data loss.
Real use: configuration values, user preferences (where loss is acceptable)

--- MV-Register (Multi-Value Register) ---
On conflict: keeps BOTH values (concurrent writes become a set).
Application must resolve the set to one value.
Used by: Riak.

--- RGA / LSEQ (Sequence CRDTs for text) ---
For collaborative text editing: assign unique identifiers to positions.
Insertions/deletions can be merged from any source in any order.
Apple's Notes, Figma, and Notion use sequence CRDTs internally.
```

---

## 6. DynamoDB Global Tables

```
AWS's managed active-active multi-region solution.

Architecture:
  Table replicated across N regions (e.g., us-east-1, eu-west-1, ap-southeast-1)
  Each region can accept reads and writes
  DynamoDB replicates changes between all regions asynchronously

Conflict resolution: Last-Write-Wins based on timestamps
  Concurrent writes to same item from different regions: highest timestamp wins
  This is a business decision: suitable for sessions, user preferences, carts
  Not suitable for: financial balances, inventory counts (use application-level locks)

Replication lag: typically ~1s between regions (can spike during high load)
Read consistency options:
  Eventually consistent reads: any region, may be slightly stale
  Strongly consistent reads: only from local region (fresh, but if region is down → unavailable)

Cost: ~2× the storage and throughput costs for each additional region

Use cases: user session storage, shopping carts, user preferences, configuration

Limitations:
  No cross-region transactions
  LWW conflicts = silent data loss for concurrent writes
  No support for counters (concurrent increments → lost updates)
  → For counters: use DynamoDB Streams + Lambda to consolidate, or use a CRDT-based service
```

---

## 7. CockroachDB Multi-Region

```
CockroachDB is designed for multi-region from the ground up.

Key concepts:

1. Survival Goals:
  ZONE survival:    survive loss of one AZ within a region
  REGION survival:  survive loss of an entire region
  → Region survival requires majority of replicas in each region

2. Table Locality:
  REGIONAL BY ROW:  Each row pinned to a region (closest to the user)
    → Reads/writes for that row go to the row's home region
    → EU users' rows in EU region → ~5ms latency
  REGIONAL BY TABLE: Entire table pinned to one region
    → Good for tables that are only accessed from one region
  GLOBAL:           Table replicated to all regions, optimized for reads everywhere
    → Reads from any region are fast, but writes need global consensus

3. Non-Voting Replicas:
  Standard Raft: 3 replicas in one region → loses region survival
  Non-voting replicas: additional replicas in other regions
    → Participate in reads but NOT in write quorum
    → US-East has 2 voting replicas + EU has 1 non-voting
    → Write quorum only in US-East (fast), EU can serve reads

4. Follower Reads:
  Read from a replica that may be slightly stale (bounded staleness ~4.8s)
  Near-instant reads from any region
  Use when: analytics, dashboards, non-critical reads where slight staleness OK
```

---

## 8. GDPR & Data Residency

```
GDPR (EU): Personal data of EU residents must:
  - Be stored within EU/EEA, OR
  - Be transferred to a country with adequate protections
  - Not be accessible to non-EU entities without proper safeguards

Practical architecture implications:
  1. Data classification: which data is "personal" under GDPR?
     → Name, email, IP address, location, device identifiers, etc.
     → Must be identified before designing storage

  2. Data residency partitioning:
     EU users → EU region (Frankfurt, Ireland)
     US users → US region (us-east-1, us-west-2)
     APAC users → APAC region (ap-southeast-1, ap-northeast-1)

  3. Geo-routing:
     DNS-based: Route 53 geolocation routing → EU request → eu-west-1
     Application-level: JWT contains region, service routes accordingly

  4. Cross-region data access:
     EU user's data must NOT be replicated to US region (even for backups)
     Exception: user explicitly consents, or data is anonymized/pseudonymized

  5. Right to erasure ("right to be forgotten"):
     Must delete user's personal data from ALL replicas, ALL regions, ALL backups
     Design implication: cryptographic erasure (encrypt data, delete the key)
       → Data becomes unreadable even in backups without re-encryption

  6. Data Processing Agreements (DPA):
     Third-party services (analytics, monitoring) that receive personal data
     must have DPAs in place. Log aggregation (Datadog, Splunk) must not
     contain EU personal data unless EU data residency is configured.

Interview pattern:
  "How would you make the Twitter Feed design GDPR-compliant?"
  → Partition tweet storage by user's region
  → EU users' tweets stored only in eu-west-1
  → Geo-routing at DNS layer (Route 53 geolocation)
  → Non-EU users' timeline cannot include EU users' data without consent
  → Encryption at rest with per-region KMS keys
  → Right-to-erasure: delete KMS key for user → all their data cryptographically erased
```

---

## 9. Multi-Region Design Patterns

### Pattern 1: Read Replicas (Read-Mostly Systems)
```
Write region: us-east-1 (primary, all writes)
Read replicas: eu-west-1, ap-southeast-1 (async replication, serve reads)

Replication lag: ~1–5 seconds
Read routing: latency-based DNS → user hits nearest read replica
Write routing: all writes go to us-east-1 (adds latency for EU/APAC users)

Good for: content platforms, social media feeds, catalog data
Bad for: financial transactions, inventory management
```

### Pattern 2: Regional Writes + Global Reads
```
Write to local region only → replicate to all regions asynchronously
Read from any region (eventually consistent)

Implementation: each user's "home region" determined at registration
  EU user → writes always go to eu-west-1
  US user → writes always go to us-east-1
  Global leaderboard: aggregated asynchronously across regions

Good for: user-centric data (profiles, preferences, timelines)
Bad for: global shared state (global inventory, global balance)
```

### Pattern 3: Active-Active with CRDT State
```
Each region accepts writes → CRDT ensures convergence
No conflicts possible (by CRDT design)

Good for: counters, sets, collaborative editing
Bad for: anything requiring strict global ordering
```

### Pattern 4: Tiered Consistency
```
Critical path (financial, inventory): strong consistency via single-region consensus
Non-critical path (analytics, feeds, notifications): eventual consistency, any region

Separate services:
  Payment service: active-passive, synchronous replication, RPO=0
  Feed service: active-active with LWW, RPO=seconds
  Analytics: fire-and-forget, eventual consistency acceptable
```

---

## 10. RPO/RTO Design

```
RPO (Recovery Point Objective): How much data loss is acceptable?
  RPO = 0:       Synchronous replication (zero data loss, higher latency)
  RPO = seconds: Asynchronous replication (small data loss, no write overhead)
  RPO = minutes: Periodic backups (significant data loss, cheapest)

RTO (Recovery Time Objective): How fast must the system recover?
  RTO = seconds:  Automatic failover, hot standby, pre-warmed (expensive)
  RTO = minutes:  Automatic failover with warm standby
  RTO = hours:    Manual failover process
  RTO = days:     Cold backup restore (disaster recovery only)

Cost vs. RPO/RTO:
  99.99% availability (52 min/year) → hot standby, automatic failover
  99.9% availability (8.7 hrs/year) → warm standby, semi-automatic failover
  99% availability (87 hrs/year)    → cold backup, manual restore

Interview formula:
  SLA → required RTO/RPO → replication strategy → standby type
  "99.99% SLA means < 52 min/year downtime. With an incident taking 15 min
   to detect and 30 min to resolve, we have no margin — we need automatic
   failover (RTO < 30s) and synchronous replication (RPO = 0) for the
   primary data store."
```

---

## 📝 Tasks

### Task 1 — Latency Math
Calculate the minimum achievable write latency for:
1. Active-active cluster with regions in US-East, EU-West, and AP-Southeast. Raft consensus (quorum = 2 of 3). Client writes from US-East.
2. Same cluster but AP-Southeast uses non-voting replicas (CockroachDB style). Now what's the write latency from US-East?
3. You add a 4th region (SA-East, ~90ms from US-East). Does adding SA-East change write latency? Why or why not?
4. A user in Tokyo is using an active-passive system where US-East is primary. What is the round-trip time for a write? For a read from the Tokyo replica?

### Task 2 — CRDT Implementation
Implement a PN-Counter CRDT in Java or Python:
1. `increment(nodeId)` and `decrement(nodeId)` operations
2. `merge(other)` — merge another replica's state into this one
3. `value()` — return current count
4. Simulate: Node A increments 3×, Node B increments 5×, Node B decrements 2×. Merge A into B and B into A. Verify both replicas show value=6.
5. Why can't a regular integer counter be a CRDT? What property does it violate?

### Task 3 — GDPR Architecture
Re-design the Twitter feed from B6 to be GDPR-compliant:
1. Which data fields are "personal data" under GDPR?
2. Design the regional partitioning — where is EU user data stored? Can EU users' tweets be in the US region's cache?
3. A user exercises "right to erasure" — delete all their data. How do you handle data in Cassandra replicas, Redis caches, CDN edge caches, and Kafka message logs?
4. Your analytics pipeline (ClickHouse) aggregates tweet metrics across all regions. Is this GDPR-compliant if it contains EU user data?
5. Design cryptographic erasure for user data — how does deleting a KMS key make all copies of the data unreadable?

### ⭐ Task 4 — Design a Multi-Region E-Commerce Platform
Design an e-commerce platform (like Flipkart/Amazon) with users in India and EU:
1. Users: 50M India (writes in India), 20M EU (writes in EU). GDPR applies to EU users.
2. Product catalog: read-heavy, can be global. What replication strategy?
3. Inventory: globally shared (1 item in Bangalore warehouse, both India and EU users can buy it). How do you prevent overselling without global locking?
4. Orders and payments: GDPR means EU orders must stay in EU. How do you handle the India user buying a product in an EU warehouse?
5. RPO/RTO requirements: inventory = RPO 0, RTO 30s; catalog = RPO minutes, RTO hours; orders = RPO 0, RTO 60s. Design the replication strategy for each.

---

## ✅ Completion Checklist

- [ ] Three reasons to go multi-region: availability, latency, compliance
- [ ] Speed of light RTTs: US↔EU ~85ms, US↔APAC ~140ms, cross-AZ ~1ms
- [ ] Active-passive: RPO (sync=0, async=seconds), RTO (auto=30–120s, manual=minutes)
- [ ] Active-active: LWW, vector clocks, CRDTs, OT — four conflict approaches
- [ ] G-Counter CRDT: vector per node, merge=max per slot, value=sum
- [ ] PN-Counter: two G-Counters, value = P - N
- [ ] G-Set, 2P-Set, OR-Set — add/remove semantics and merge rules
- [ ] LWW-Register vs MV-Register — data loss vs conflict surfacing
- [ ] Sequence CRDTs (RGA/LSEQ) — used in collaborative editing
- [ ] DynamoDB Global Tables: LWW active-active, ~1s replication lag
- [ ] CockroachDB multi-region: REGIONAL BY ROW, non-voting replicas, follower reads
- [ ] GDPR: data residency, right to erasure, cryptographic erasure with KMS
- [ ] Geo-routing: DNS geolocation (Route 53) for regional partitioning
- [ ] Read replicas pattern: good for reads, all writes still go to primary
- [ ] Regional writes + global reads: home region per user
- [ ] RPO/RTO: sync=RPO0, async=RPO seconds; auto failover=RTO 30s
- [ ] Completed Task 1 — latency math across region topologies
- [ ] Completed Task 2 — PN-Counter CRDT implementation
- [ ] Completed Task 3 — GDPR architecture for Twitter feed
- [ ] Completed Task 4 — multi-region e-commerce capstone

**→ Next: Module C3 — ML Systems Design (Feature Stores, Training Pipelines, Model Serving)**

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'JetBrains Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-c1-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← C1 Consensus Notes</a>
  <a href="/learning/system-design/hld/module-c2-geo-distribution/" style="padding:12px 24px;border:1px solid #00b8c8;color:#00b8c8;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b13-notes/" style="padding:12px 24px;background:#00b8c8;color:#fff;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: C3 ML Systems →</a>
</div>
