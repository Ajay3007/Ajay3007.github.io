---
title: "Module B2 — Databases at Scale | Full Notes"
description: "System Design Roadmap › HLD Hub › Module B2 › Full Notes ⚡ Interactive Visual Version ← Recommended for learning."
domain: system-design
track: system-design-hld
order: 105
url: /learning/system-design/hld/module-b2-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div style="margin-bottom:1.5rem;">
  <a href="/learning/system-design/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">System Design Roadmap</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">HLD Hub</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/module-b2-databases-at-scale/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">Module B2</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <span style="color:var(--text-color);font-size:0.85rem;font-weight:600;">Full Notes</span>
</div>

<div style="margin-bottom:2rem;">
  <a href="/learning/system-design/hld/module-b2-databases-at-scale/" style="display:inline-block;padding:0.5rem 1.1rem;background:rgba(0,212,170,0.1);color:#00d4aa;border:1px solid rgba(0,212,170,0.3);border-radius:6px;font-size:0.85rem;font-weight:600;text-decoration:none;">⚡ Interactive Visual Version</a>
  <span style="margin-left:0.8rem;font-size:0.82rem;color:var(--light-text);">← Recommended for learning. This page is the printable reference.</span>
</div>

# Module B2 — Databases at Scale
## System Design Mastery Course | Track B: HLD | Week 12

---

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** B — High-Level Design (HLD)  
**Prerequisites:** B1 (HLD Fundamentals — CAP, consistency, availability)  
**Goal:** Deep understanding of how databases scale — the most critical component in any distributed system. Database decisions are the hardest to change after the fact. Get them right.

### Module B2 Topics

| Topic | Core Problem |
|-------|-------------|
| Indexing | Why queries go from O(n) to O(log n) |
| ACID vs BASE | The consistency guarantee spectrum |
| SQL vs NoSQL | Not a religion — a trade-off based on access patterns |
| Replication | How to survive node failures + serve more reads |
| Sharding | How to store data that doesn't fit on one machine |
| Read Replicas | Scaling reads without touching writes |
| Database Selection Guide | Choosing the right DB for the right job |

---

## 1. Indexing — Why It Matters

Without an index, every query scans every row — O(n). With an index, queries become O(log n) or O(1).

### B-Tree Index (Default in PostgreSQL, MySQL)
```
Structure: Balanced binary search tree of key → row_pointer pairs
Best for:  Equality (=), range queries (<, >, BETWEEN), ORDER BY, JOIN

Example:
  SELECT * FROM users WHERE email = 'a@b.com'
  Without index: scan all 10M rows
  With B-tree index on email: binary search → ~24 comparisons (log₂ 10M)
```

### Hash Index
```
Structure: Hash map of key → row_pointer
Best for:  Equality queries only (=)
Worst for: Range queries (not supported — hash loses ordering)

Example: Memcached, Redis hash maps, MySQL MEMORY engine
```

### Composite Index
```
CREATE INDEX idx_user_date ON orders(user_id, created_at);

Left-most prefix rule:
  ✅ WHERE user_id = 5                        (uses index)
  ✅ WHERE user_id = 5 AND created_at > X     (uses index)
  ❌ WHERE created_at > X                     (does NOT use index — skips user_id)

Most selective column should be first.
```

### Covering Index
```
An index that contains all columns needed by a query:
  SELECT user_id, created_at FROM orders WHERE user_id = 5

If index includes (user_id, created_at), the DB reads only the index,
never touches the row data. Drastically reduces I/O.
```

### Index Costs
```
✅ Speeds up SELECT dramatically
❌ Slows down INSERT, UPDATE, DELETE (must update the index too)
❌ Consumes disk space (can be 10–30% of table size)
❌ Can lead to index bloat over time (periodic REINDEX needed)

Rule: Index columns that appear in WHERE, JOIN ON, ORDER BY.
      Don't index every column — low-cardinality columns (boolean, status enum)
      give poor selectivity; the optimizer may prefer a full scan.
```

---

## 2. ACID vs BASE

### ACID (Relational Databases)
```
A — Atomicity:    Transaction is all-or-nothing. No partial writes.
C — Consistency:  DB transitions from one valid state to another.
                  Constraints (FK, NOT NULL, UNIQUE) always satisfied.
I — Isolation:    Concurrent transactions don't see each other's in-progress writes.
D — Durability:   Committed transactions survive crashes (WAL / fsync).
```

### Isolation Levels (ACID — I in depth)
```
Phenomena (problems):
  Dirty Read:      Transaction A reads uncommitted data from B.
  Non-repeatable:  Transaction A reads same row twice; B commits between → different value.
  Phantom Read:    Transaction A runs same query twice; B inserts matching row → different count.

Isolation levels (weakest → strongest):
  READ UNCOMMITTED:  Allows dirty reads (rarely used)
  READ COMMITTED:    No dirty reads; non-repeatable reads possible (PostgreSQL default)
  REPEATABLE READ:   No dirty/non-repeatable reads; phantoms possible (MySQL default)
  SERIALIZABLE:      Fully isolated; no concurrency anomalies (slowest)

Trade-off: Higher isolation = fewer anomalies = more locking = lower throughput
```

### BASE (NoSQL / Distributed Systems)
```
BA — Basically Available:  System always responds (may be stale/partial)
S  — Soft State:           State can change over time even without input (replication)
E  — Eventually Consistent: Given no new updates, replicas will converge

BASE is not "ACID without guarantees" — it's a deliberate design choice for
availability and performance over strict consistency.
```

---

## 3. SQL vs NoSQL — The Real Trade-off

### When to Choose SQL
```
✅ Complex queries with JOINs across multiple tables
✅ ACID transactions required (financial, booking, inventory)
✅ Schema is well-defined and stable
✅ Rich query patterns (GROUP BY, aggregations, window functions)
✅ Data integrity constraints critical (FK, UNIQUE, CHECK)
✅ Team knows SQL deeply

Examples: PostgreSQL, MySQL, Aurora, SQLite
```

### When to Choose NoSQL
```
✅ Access pattern is simple and known (key lookup, range scan)
✅ Need horizontal scale beyond what vertical + sharding SQL can give
✅ Schema is flexible / evolving rapidly
✅ Extremely high write throughput required
✅ Data is naturally document-shaped (nested JSON), graph, or time-series

Examples: DynamoDB (key-value/document), Cassandra (wide-column),
          MongoDB (document), Neo4j (graph), InfluxDB (time-series)
```

### NoSQL Data Models

```
Key-Value:
  Structure: Key → Value (blob, string, JSON, binary)
  Access:    Get(key), Put(key, value), Delete(key)
  Best for:  Session storage, caching, shopping carts, user preferences
  Examples:  Redis, DynamoDB, Riak

Document:
  Structure: Nested JSON/BSON documents; flexible schema per document
  Access:    Query on any field within document; partial updates
  Best for:  Content management, catalogs, user profiles, event logging
  Examples:  MongoDB, CouchDB, Firestore

Wide-Column (Column Family):
  Structure: Row key → sorted map of column families
  Access:    Efficient range scans on row key; sparse columns
  Best for:  Time-series, IoT telemetry, write-heavy analytics
  Examples:  Cassandra, HBase, Bigtable

Graph:
  Structure: Nodes (entities) + Edges (relationships) + properties on both
  Access:    Traverse relationships; shortest path; neighbor queries
  Best for:  Social networks, recommendation engines, fraud detection
  Examples:  Neo4j, Amazon Neptune, Dgraph

Time-Series:
  Structure: Timestamp + measurement; optimised for time-range queries
  Access:    Last N values, aggregations over time ranges, downsampling
  Best for:  Metrics, monitoring, IoT, financial tick data
  Examples:  InfluxDB, TimescaleDB, Prometheus
```

---

## 4. Replication

### Primary-Replica (Leader-Follower)
```
Architecture:
  Primary: accepts writes
  Replica(s): receive changes asynchronously from primary; serve reads

                     WRITE
[Client W] ──→ [Primary DB] ──async──→ [Replica 1]
                                  ──async──→ [Replica 2]
[Client R] ──→ [Replica 1]  (read traffic distributed)

Pros:
  ✅ Scales reads horizontally (add more replicas)
  ✅ Replicas can be promoted to primary if primary fails
  ✅ Replicas can serve analytics queries (separate read pool)

Cons:
  ❌ Replication lag — reads from replica may be stale
  ❌ Primary is still single write point (vertical scale only for writes)
  ❌ Failover takes time; potential for data loss (async window)
```

### Replication Lag Problem
```
Scenario:
  1. User updates their profile photo (write → primary)
  2. User immediately views their profile (read → replica)
  3. Replica hasn't received update yet → user sees old photo

Solutions:
  a) Read-your-own-writes: route user's reads to primary for their own data
  b) Monotonic reads: always route same user to same replica
  c) Sync replication: write waits for replica acknowledgement (slower)
  d) Synchronous replication for critical paths only
```

### Multi-Primary (Multi-Master)
```
All nodes accept writes. Must handle write conflicts.

Conflict resolution strategies:
  Last-write-wins (LWW): Timestamp-based; risk of data loss
  CRDTs:                 Conflict-free Replicated Data Types (mathematical guarantee)
  Application merge:     Business logic resolves conflicts
  Avoid conflicts:       Partition writes by user/tenant (each user has one home node)

Use case: Multi-datacenter active-active (geo-distributed writes)
Examples: Cassandra, CockroachDB (with consensus), MySQL Group Replication
```

### Synchronous vs Asynchronous Replication
```
Synchronous:
  Primary waits for replica ACK before confirming write to client
  ✅ No data loss on primary failure
  ❌ Write latency increases by one network RTT
  ❌ If replica is slow, primary is slowed

Semi-synchronous:
  Primary waits for ACK from at least ONE replica (not all)
  Balance between durability and latency

Asynchronous (default for most systems):
  Primary confirms write immediately; replication happens in background
  ✅ Lowest write latency
  ❌ Recent writes may be lost if primary crashes before replica catches up
```

---

## 5. Sharding (Horizontal Partitioning)

### What is Sharding?
Distributing rows of a table across multiple database nodes (shards), so each shard holds a subset of the data.

```
Without sharding: All 10B rows on one DB node → single point of scale limit
With sharding:    2.5B rows on Shard 0, 1, 2, 3 each → 4× write throughput
```

### Sharding Strategies

#### Range-Based Sharding
```
Partition by range of shard key value.

Shard 0: user_id 1 – 25,000,000
Shard 1: user_id 25,000,001 – 50,000,000
Shard 2: user_id 50,000,001 – 75,000,000
Shard 3: user_id 75,000,001 – 100,000,000

✅ Range queries efficient (all results on one or few shards)
✅ Easy to add new shards at end of range
❌ Hot spots: if recent users are most active, highest user_id shard is hot
❌ Uneven distribution if data is skewed
```

#### Hash-Based Sharding
```
shard = hash(shard_key) % num_shards

User 12345 → hash(12345) % 4 = 2 → Shard 2

✅ Even distribution (hash distributes randomly)
✅ No hot spots
❌ Range queries require scatter-gather (must ask all shards)
❌ Resharding is painful: changing num_shards remaps all keys
```

#### Consistent Hashing
```
Map servers and keys to same hash ring (0 to 2³² positions).
Each key belongs to the nearest server clockwise on the ring.

Adding/removing a server only remaps K/N keys.
(K = total keys, N = total servers → ~1/N fraction remapped)

Virtual nodes: Each physical server → multiple virtual positions on ring.
               Ensures even distribution even with few servers.

Used by: DynamoDB, Cassandra, Memcached clusters
```

### The Hotkey Problem
```
Problem: A single shard key is accessed overwhelmingly more than others.
  Example: Taylor Swift's user_id during a concert ticket release
           A viral post's post_id with millions of concurrent reads

Solutions:
  1. Key suffixing: post_id_0, post_id_1, ..., post_id_9 → distribute across shards
  2. Caching: Put a Redis cache in front; DB shard only for cache misses
  3. Read replicas per shard: multiple replicas for the hot shard
  4. Application-level fan-out: pre-compute and distribute to many buckets
```

### Cross-Shard Queries
```
Problem: JOINs across shards are expensive (scatter-gather + merge)

Solutions:
  1. Denormalise: embed related data in the same document/row (NoSQL pattern)
  2. Design sharding key to co-locate related data:
       Shard all of a user's orders by user_id → queries for "my orders" stay on one shard
  3. Use a separate analytics DB (data warehouse) for cross-shard aggregations
  4. Accept scatter-gather for rare complex queries; cache results aggressively
```

---

## 6. Read Replicas at Scale

```
Architecture for read-heavy systems (e.g., 95% reads, 5% writes):

[Writes] → [Primary]
                ├──→ [Replica 1] ←── [Read LB]
                ├──→ [Replica 2] ←── /
                └──→ [Replica 3] ←── /
                        ↑
                [Read traffic distributed by read LB]

Scaling further:
  - Add more replicas (reads scale linearly)
  - Use connection pooling (PgBouncer/ProxySQL) to reduce connection overhead
  - Cache hot reads in Redis → avoid DB altogether for most reads
  - Cross-region replicas for geo-distributed read latency reduction
```

---

## 7. Database Selection Guide

```
┌─────────────────────────────────────────────────────────────────┐
│                    DECISION FRAMEWORK                            │
│                                                                 │
│  Need ACID + complex queries?           → PostgreSQL / MySQL    │
│  Need massive write throughput?         → Cassandra / DynamoDB  │
│  Need flexible document schema?         → MongoDB               │
│  Need graph traversals?                 → Neo4j                 │
│  Need time-series + metrics?            → InfluxDB / TimescaleDB│
│  Need full-text search?                 → Elasticsearch         │
│  Need distributed SQL (global)?         → CockroachDB / Spanner │
│  Need in-memory cache?                  → Redis / Memcached     │
│  Need object/file storage?              → S3 / GCS              │
└─────────────────────────────────────────────────────────────────┘
```

### Comparison Table

| DB | Type | Consistency | Scale | Best For |
|----|------|-------------|-------|---------|
| PostgreSQL | Relational | ACID | Vertical + read replicas | Complex queries, transactions |
| MySQL | Relational | ACID | Vertical + read replicas | Web apps, proven reliability |
| MongoDB | Document | Tunable | Horizontal sharding | Flexible schema, catalogs |
| Cassandra | Wide-column | Eventual/Tunable | Horizontal (massive) | High-write IoT, time-series |
| DynamoDB | Key-value/Doc | Eventual/Strong | Horizontal (managed) | Serverless, variable load |
| Redis | Key-value | Strong (single node) | Vertical + cluster | Cache, sessions, pub/sub |
| HBase | Wide-column | Strong (Zookeeper) | Horizontal (Hadoop) | Analytics on Hadoop |
| Neo4j | Graph | ACID | Vertical (limited H) | Relationships, recommendations |
| InfluxDB | Time-series | Eventual | Horizontal | Metrics, monitoring |
| Elasticsearch | Search | Eventual | Horizontal | Full-text search, logs |

---

## 📝 Tasks

### Task 1 — Index Design
Given this schema and query patterns, design the optimal index strategy:

```sql
-- Table: orders (10M rows)
CREATE TABLE orders (
    id          BIGINT PRIMARY KEY,
    user_id     INT,
    restaurant_id INT,
    status      VARCHAR(20),  -- 'pending', 'delivered', 'cancelled'
    total       DECIMAL(10,2),
    created_at  TIMESTAMP
);

-- Query patterns:
-- Q1: Find all orders for a specific user (most frequent)
-- Q2: Find recent orders for a restaurant ordered by time
-- Q3: Find all pending orders (dashboard refresh every 5s)
-- Q4: Find orders by user in a date range

-- For each query: design the index, explain the B-tree traversal,
-- and identify which queries could use a covering index.
```

### Task 2 — Sharding Design
Design a sharding strategy for a multi-tenant SaaS product:
- 10,000 business tenants, each with 10,000–1,000,000 records
- Most queries are scoped to a single tenant
- 3 large tenants generate 60% of the traffic
- Occasional cross-tenant analytics queries needed

Questions to answer:
1. What is the shard key? Why?
2. Which sharding strategy (range, hash, consistent hashing)?
3. How do you handle the 3 hot tenants?
4. How do you handle cross-tenant analytics?

### Task 3 — Replication Lag Scenario
A social media platform has this architecture:
- Primary DB for writes
- 3 read replicas for reads
- Replication lag is typically 100ms but can spike to 2s

For each feature, decide: read from primary or replica, and justify:
1. User views their own profile after updating it
2. User views another user's follower count
3. User's home feed (timeline of posts from people they follow)
4. Payment confirmation page after a purchase
5. Admin dashboard showing total active users (updated every 5 min)

### ⭐ Task 4 — Design Instagram's Storage Layer
Using B1 + B2 concepts, design the complete storage layer for Instagram:

Data to store:
- User accounts (500M users)
- Photos/Videos (100B media files, avg 3 MB each)
- Comments (10B comments)
- Likes (500B likes)
- Follow relationships (graph: avg 500 followers per user)
- Feed (each user sees posts from people they follow)

For each: choose the DB type, justify with CAP + access pattern, estimate storage, and describe sharding strategy.

---

## 💡 Interview Tips — Databases

| Question | Strong Answer |
|----------|--------------|
| "SQL or NoSQL?" | "It depends on access patterns. If I need complex joins and ACID, SQL. If I need horizontal scale and simple key lookups, NoSQL. Tell me the access patterns and I'll choose." |
| "How does indexing work?" | "B-tree keeps keys sorted, enabling O(log n) search and range scans. Trade-off: every write must update the index, so don't index everything." |
| "How do you handle a hotkey?" | "Cache it in Redis, distribute the key with suffixes (key_0...key_N), or use application-level fan-out to spread the load." |
| "Primary vs replica reads?" | "Reads from replica are faster but may be stale. Route to primary only when freshness is critical: after user's own write, or for financial data." |
| "How to shard by user_id?" | "Hash(user_id) % N for even distribution. But then range queries scatter-gather. Alternatively, range shard if temporal locality matters." |
| "ACID vs BASE?" | "ACID: all-or-nothing transactions, strong consistency, works for financial systems. BASE: available, eventually consistent, works for social media likes." |

---

## ✅ Module B2 Completion Checklist

- [ ] Understand B-tree indexing — why O(log n), cost on writes, left-most prefix rule
- [ ] Understand composite and covering indexes
- [ ] Know ACID in depth — all 4 properties + all 4 isolation levels
- [ ] Know BASE — and when it's the right choice
- [ ] Can articulate SQL vs NoSQL decision criteria clearly
- [ ] Know all 5 NoSQL data models (KV, Document, Wide-column, Graph, Time-series)
- [ ] Understand primary-replica replication + replication lag solutions
- [ ] Know all 3 sharding strategies + when to use each
- [ ] Understand the hotkey problem and its solutions
- [ ] Can design sharding for cross-shard query minimisation
- [ ] Completed Task 1 — Index design for orders table
- [ ] Completed Task 2 — Sharding design for multi-tenant SaaS
- [ ] Completed Task 3 — Replication lag decision scenarios
- [ ] Completed Task 4 — Instagram storage layer design

**→ Next: Module B3 — Caching (Redis, CDN, cache strategies, invalidation)**
