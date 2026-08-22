---
title: "Module B1 — HLD Fundamentals | Full Notes"
description: "System Design Roadmap › HLD Hub › Module B1 › Full Notes ⚡ Interactive Visual Version ← Recommended for learning."
domain: system-design
track: system-design-hld
order: 103
url: /learning/system-design/hld/module-b1-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div style="margin-bottom:1.5rem;">
  <a href="/learning/system-design/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">System Design Roadmap</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">HLD Hub</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <a href="/learning/system-design/hld/module-b1-hld-fundamentals/" style="color:var(--light-text);text-decoration:none;font-size:0.85rem;">Module B1</a>
  <span style="color:var(--light-text);margin:0 0.4rem;">›</span>
  <span style="color:var(--text-color);font-size:0.85rem;font-weight:600;">Full Notes</span>
</div>

<div style="margin-bottom:2rem;">
  <a href="/learning/system-design/hld/module-b1-hld-fundamentals/" style="display:inline-block;padding:0.5rem 1.1rem;background:rgba(0,212,170,0.1);color:#00d4aa;border:1px solid rgba(0,212,170,0.3);border-radius:6px;font-size:0.85rem;font-weight:600;text-decoration:none;">⚡ Interactive Visual Version</a>
  <span style="margin-left:0.8rem;font-size:0.82rem;color:var(--light-text);">← Recommended for learning. This page is the printable reference.</span>
</div>

# Module B1 — HLD Fundamentals
## System Design Mastery Course | Track B: HLD | Week 11

---

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** B — High-Level Design (HLD)  
**Prerequisites:** Track A (LLD complete)  
**Goal:** Build the conceptual foundation for all HLD interviews. Every system design question you'll encounter depends on mastering these fundamentals. Learn them deeply — not as buzzwords, but as tools you can reason with.

### What Changes in HLD vs LLD

| Dimension | LLD (Track A) | HLD (Track B) |
|-----------|--------------|---------------|
| Focus | Single machine, classes, patterns | Distributed system, services, infrastructure |
| Scale | Thousands of requests | Millions to billions |
| Failures | Code-level exceptions | Node crashes, network partitions |
| Language | Java classes, interfaces | Services, databases, queues, caches |
| Time horizon | Code changes in hours | Architecture evolves over months |

### Module B1 Topics

| Topic | Core Insight |
|-------|-------------|
| Scalability | Vertical vs Horizontal; stateless design |
| CAP Theorem | You can't have all three — choose a trade-off |
| Consistency Models | Strong, eventual, causal — what they mean in practice |
| Availability Patterns | Active-passive, active-active, fault tolerance |
| Load Balancing | Algorithms, L4 vs L7, sticky sessions |
| Latency vs Throughput | Why they trade off; Little's Law |
| Back-of-envelope Math | Estimation without a calculator |
| System Design Framework | How to structure any HLD interview answer |

---

## 1. Scalability

### Vertical Scaling (Scale Up)
Add more resources to a single machine (more CPU, RAM, SSD).

```
Pros:
  ✅ Simple — no code changes needed
  ✅ No distributed coordination overhead
  ✅ Strong consistency trivially

Cons:
  ❌ Hard limit — biggest machine available
  ❌ Single point of failure
  ❌ Expensive beyond a point
  ❌ Downtime required to upgrade

Example: Upgrading a PostgreSQL server from 16 core to 64 core
```

### Horizontal Scaling (Scale Out)
Add more machines; distribute load across them.

```
Pros:
  ✅ Theoretically unlimited scale
  ✅ No single point of failure
  ✅ Commodity hardware (cost-effective at scale)

Cons:
  ❌ Application must be stateless (or state must be externalised)
  ❌ Distributed coordination complexity
  ❌ Network latency between nodes
  ❌ Harder to debug

Example: Adding more backend servers behind a load balancer
```

### The Stateless Mandate
For horizontal scaling to work, each server must be stateless — it must not store session state locally. State is externalised:

```
User sessions       → Redis / Memcached
User data           → Database (relational / NoSQL)
Uploaded files      → S3 / Object storage
Long-running tasks  → Message queue (Kafka, RabbitMQ)

Stateless rule: any server can handle any request.
If server-A crashes, server-B picks up with no data loss.
```

---

## 2. CAP Theorem

### The Theorem
In a distributed system, you can guarantee at most **2 of 3** properties:

```
C — Consistency:    Every read sees the most recent write
A — Availability:   Every request gets a response (not an error)
P — Partition Tolerance: System continues operating despite network partition

KEY INSIGHT: Network partitions WILL happen. P is not optional.
Therefore: real choice is between C and A when a partition occurs.

CA systems:  Traditional single-node RDBMS (but these aren't distributed)
CP systems:  HBase, Zookeeper, MongoDB (w/ majority write concern)
AP systems:  Cassandra, DynamoDB, CouchDB, DNS
```

### What a Network Partition Looks Like
```
Normal:
  [Node A] ←→ [Node B] ←→ [Node C]  (all connected)

Partition:
  [Node A] | [Node B] ←→ [Node C]   (A isolated)

When user writes to Node A:
  CP system: Reject the write (preserve consistency, sacrifice availability)
  AP system: Accept the write (stay available, risk inconsistency)
```

### CP vs AP — Real Examples

| Scenario | Choose CP | Choose AP |
|----------|-----------|-----------|
| Bank transfer | ✅ Never show wrong balance | — |
| Social media likes | — | ✅ Approximate count OK |
| Inventory reservation | ✅ Never oversell | — |
| User profile | — | ✅ Slightly stale is fine |
| Payment processing | ✅ | — |
| DNS lookups | — | ✅ Stale record > no record |

### PACELC — The Extension
CAP only describes behavior during partitions. PACELC extends it:

```
P: During Partition → choose A or C (CAP)
E: Else (no partition) → choose Latency or Consistency

PACELC(P: A/C; E: L/C)

Cassandra:   PA/EL — available during partition; low latency normally
DynamoDB:    PA/EL — same
Zookeeper:   PC/EC — consistent during partition; consistent normally
MySQL:       PC/EC — consistent always
```

---

## 3. Consistency Models

From strongest to weakest:

### Strong Consistency
Every read returns the latest write. Feels like a single machine.

```
Implementation: 2-Phase Commit (2PC), Paxos, Raft consensus
Cost: High latency (must coordinate across all replicas before returning)
Examples: Google Spanner (TrueTime), Zookeeper, etcd

When you need it: Banking, inventory, booking systems
                  (anything where stale data causes real harm)
```

### Linearizability
Strongest form of consistency. Operations appear atomic and in real-time order.

```
Every operation appears to take effect instantaneously at some point
between its start and end. External observers see a consistent history.

Stronger than strong consistency — guarantees wall-clock ordering.
Used in: distributed locks, leader election (etcd, Zookeeper)
```

### Sequential Consistency
All nodes see operations in the same order, but not necessarily real-time order.

```
Weaker than linearizability — order preserved, but clock may lag.
Used in: Some multi-processor memory models
```

### Causal Consistency
Causally related operations are seen in correct order. Concurrent operations may be seen in different orders.

```
If A → B (A causes B), all nodes see A before B.
But unrelated operations can appear in any order.

Example: Reply always appears after the original post.
         But two unrelated posts can appear in any order.

Used in: Distributed databases with vector clocks (DynamoDB streams)
```

### Eventual Consistency
Given no new updates, all replicas eventually converge to the same state.

```
No guarantees on WHEN convergence happens.
Reads may return stale data.
Writes are never rejected.

Example: DNS propagation — new record eventually spreads to all resolvers.
         Shopping cart in Amazon — may briefly show stale items.

Used in: Cassandra, DynamoDB, S3, most AP systems
```

### Read-Your-Own-Writes (Session Consistency)
A user always sees their own writes, even if others don't yet.

```
Implementation: Route user's reads to the replica they wrote to.
                Or use sticky sessions to always route same user to same node.

Example: After you post a tweet, you always see your own tweet.
         Others might not see it immediately.

Common pattern in: Social networks, user profile updates
```

---

## 4. Availability Patterns

### Measuring Availability (The Nines)

```
Availability = Uptime / (Uptime + Downtime)

99%     = 87.6 hours downtime/year    (2 nines)
99.9%   = 8.7 hours downtime/year     (3 nines)
99.99%  = 52.6 minutes downtime/year  (4 nines — typical SLA)
99.999% = 5.3 minutes downtime/year   (5 nines — telecom grade)

Combined availability of N services in sequence:
  Total = A1 × A2 × A3
  If each service is 99.9%: 0.999 × 0.999 × 0.999 = 99.7%
  → MORE services in a request path → LOWER total availability
```

### Active-Passive (Failover)
One active node serves traffic; one passive node is on standby.

```
Normal:    [Client] → [Active]     [Passive] (standby)
Failover:  [Client] → [Passive]    [Active] (dead/recovering)

Variants:
  Hot standby:  Passive is running, synced, can take over in seconds
  Warm standby: Passive needs startup time (minutes)
  Cold standby: Passive needs to be provisioned (minutes to hours)

Used in: Traditional databases (MySQL primary-replica), RDBMS HA
```

### Active-Active (Load Sharing)
Multiple nodes actively serve traffic simultaneously.

```
Normal: [Client] → [LB] → [Node A]
                        → [Node B]
                        → [Node C]

All nodes handle reads and writes.
Conflict resolution required (last-write-wins, CRDTs, application-level merge).

Used in: Cassandra, DynamoDB, Akamai CDN, most NoSQL systems at scale
```

### Failover Challenges
```
Split-brain: Network partition causes BOTH nodes to think they're the active primary.
             Both accept writes → divergent state.
Prevention:  Quorum (must have majority agree before accepting writes)
             Fencing tokens (revoke old primary's ability to write to storage)

Data loss window: In async replication, recent writes may not reach passive.
                  Addressed with: sync replication (slower) or WAL shipping
```

---

## 5. Load Balancing

### What a Load Balancer Does
Distributes incoming requests across a fleet of backend servers.

```
Client → [Load Balancer] → Server A
                        → Server B
                        → Server C

Functions:
  1. Traffic distribution (main job)
  2. Health checking (remove unhealthy servers)
  3. SSL termination (decrypt HTTPS once, forward as HTTP)
  4. Session stickiness (route same user to same server)
  5. Rate limiting (per client or per endpoint)
```

### L4 vs L7 Load Balancing

| Feature | L4 (Transport Layer) | L7 (Application Layer) |
|---------|---------------------|----------------------|
| Works on | TCP/UDP packets | HTTP/HTTPS requests |
| Routing basis | IP + Port | URL path, headers, cookies |
| Speed | Very fast (no content inspection) | Slower (parses content) |
| SSL termination | No | Yes |
| Smart routing | No | Yes (route /api → API servers) |
| Examples | AWS NLB, HAProxy L4 | AWS ALB, NGINX, Envoy |

### Load Balancing Algorithms

```
Round Robin:
  Requests distributed evenly in rotation: A → B → C → A → B → C
  Simple, equal distribution. Ignores server capacity.

Weighted Round Robin:
  Servers with higher weight get more requests.
  Server A (weight 3): A → A → A → B → B → C → repeat
  Use when: heterogeneous server fleet (some servers are bigger)

Least Connections:
  New request goes to server with fewest active connections.
  Best when: requests vary significantly in processing time.

Least Response Time:
  Route to server with lowest latency + fewest connections.
  Adds health check latency monitoring.

IP Hash (Sticky Sessions):
  Hash(client IP) % N servers → always same server.
  Use when: server-side session state (avoid by using Redis instead).

Consistent Hashing:
  Map servers and requests to same hash ring.
  Adding/removing servers only remaps O(1/N) of requests.
  Best for: distributed caches, CDN, databases.
```

---

## 6. Latency vs Throughput

### Definitions

```
Latency:    Time for ONE request to complete (milliseconds)
            "How fast is a single request?"

Throughput: Number of requests completed per unit time (req/sec)
            "How many requests can the system handle?"

They trade off:
  - Processing more requests in parallel → higher throughput
  - But more parallel work means more queuing → higher latency
  - Optimizing for one often hurts the other
```

### Little's Law

```
L = λ × W

L = average number of items in the system (queue depth)
λ = average arrival rate (throughput, requests/sec)
W = average time in system (latency, seconds)

Example: 
  A service handles 100 req/sec (λ=100)
  Average latency is 50ms (W=0.05s)
  Average items in system: L = 100 × 0.05 = 5 concurrent requests

Insight: If latency increases (W↑) and arrival rate stays same (λ=const),
         queue depth (L) increases → eventually overload
```

### Latency Numbers to Memorize

```
L1 cache reference:              0.5 ns
L2 cache reference:              7   ns
RAM access:                    100   ns
SSD random read:             100,000 ns = 0.1 ms
Network within datacenter:   500,000 ns = 0.5 ms
HDD random read:          10,000,000 ns = 10  ms
Network cross-region:    150,000,000 ns = 150 ms

Rules of thumb:
  Memory read:   ~100 ns
  SSD read:      ~0.1 ms (1000x slower than RAM)
  HDD read:      ~10 ms  (100x slower than SSD)
  Same DC:       ~0.5 ms
  Cross-region:  ~50–150 ms
```

---

## 7. Back-of-Envelope Estimation

### Estimation Framework
```
Step 1: Clarify scale — DAU, requests/user/day
Step 2: Calculate peak QPS = (DAU × req/day) / 86400 × 2–3 (peak factor)
Step 3: Calculate storage = items × item_size × retention_period
Step 4: Calculate bandwidth = QPS × payload_size
Step 5: Calculate servers = peak_QPS / (capacity_per_server)
```

### Example — Twitter-scale Estimation

```
Assumptions:
  300M DAU
  Each user reads 100 tweets/day, writes 2 tweets/day
  Average tweet: 280 chars ≈ 300 bytes + metadata ≈ 1 KB

READ QPS:
  300M × 100 / 86,400 ≈ 347,000 reads/sec
  Peak (3×): ~1M reads/sec

WRITE QPS:
  300M × 2 / 86,400 ≈ 7,000 writes/sec
  Peak (3×): ~21,000 writes/sec

STORAGE (tweets, 5 years):
  300M users × 2 tweets/day × 365 × 5 years × 1 KB
  = 300M × 2 × 365 × 5 × 1000 bytes
  ≈ 1 KB × 1.1 × 10^12 ≈ 1.1 PB

BANDWIDTH:
  Read: 1M reads/sec × 1 KB = 1 GB/sec
  Write: 21K writes/sec × 1 KB ≈ 21 MB/sec

SERVERS (assuming 50K req/sec/server):
  Read servers: 1M / 50K = 20 servers (minimum, before replication)
```

### Storage Estimation Cheat Sheet
```
Character:         1 byte (ASCII) / 4 bytes (UTF-8 max)
Integer (int):     4 bytes
Long:              8 bytes
UUID:             16 bytes
Unix timestamp:    4 bytes
Image (compressed): 100 KB – 5 MB
HD video (1 min):  60 MB (compressed H.264)
4K video (1 min):  375 MB

1 KB = 10³ bytes
1 MB = 10⁶ bytes
1 GB = 10⁹ bytes
1 TB = 10¹² bytes
1 PB = 10¹⁵ bytes
```

---

## 8. System Design Interview Framework

### The 7-Step Template

```
Step 1: REQUIREMENTS CLARIFICATION (5 min)
  Functional requirements: What does the system do?
    - Core features (write, read, search?)
    - Users, use cases, flows
  Non-functional requirements: How does it perform?
    - Scale (DAU, QPS, storage)
    - Latency targets (<200ms for reads?)
    - Availability target (99.99%?)
    - Consistency requirements (strong or eventual?)
    - Geographic distribution?

Step 2: CAPACITY ESTIMATION (5 min)
  - DAU, peak QPS, storage per year
  - Bandwidth (read + write)
  - Number of servers needed
  Show your math. Round aggressively.

Step 3: HIGH-LEVEL DESIGN (10 min)
  - Draw the big boxes: clients, API layer, services, databases, caches
  - Identify read vs write path
  - Show data flows between components
  - Don't go deep yet — breadth first

Step 4: DEEP DIVE (15 min)
  - Pick 1–2 most interesting/complex components
  - Database schema or data model
  - Critical API design
  - Specific algorithm or data structure
  - The part you're being tested on

Step 5: BOTTLENECKS + TRADE-OFFS (5 min)
  - Where are the hotspots?
  - What would break first at 10× scale?
  - What trade-offs did you make and why?
  - How would you handle a specific failure scenario?

Step 6: FAILURE SCENARIOS (2 min)
  - What happens if the database goes down?
  - What if the cache is cold?
  - What happens during a DC failover?

Step 7: SCALE EVOLUTION (optional, if time permits)
  - What would you add for 10× more scale?
  - Sharding strategy for the database?
  - CDN for static content?
```

### Common Components and When to Use Them

```
CDN:                   Static content (images, JS, CSS) or globally read-heavy content
Load Balancer:         Multiple backend instances; traffic distribution
Cache (Redis):         Hot reads, session storage, rate limiting counters
Message Queue (Kafka): Async processing, event streaming, decoupling services
SQL Database:          Structured data, ACID transactions, complex queries
NoSQL Database:        High throughput, flexible schema, horizontal scale
Object Storage (S3):   Large files (images, videos, backups)
Search Engine:         Full-text search, faceted filtering
Data Warehouse:        Analytics, aggregations over historical data
```

---

## 📝 Tasks

### Task 1 — CAP Theorem Application (8 Scenarios)
For each, identify: CP or AP? Why? What trade-off are you making?

1. Online banking — check account balance before debit
2. Facebook Like counter on a viral post
3. Uber driver location updates (driver moves every 4 seconds)
4. Hotel room reservation system (last room available)
5. Amazon product review display
6. Stock trading platform — order placement
7. WhatsApp message delivery status (sent/delivered/read)
8. E-commerce shopping cart (items added by user)

### Task 2 — Estimation Practice
Do full back-of-envelope for each:

**System A — WhatsApp**
- 2 billion users, 100M active daily
- 100 messages/user/day, avg message = 100 bytes
- Calculate: QPS (peak), storage/year, bandwidth

**System B — YouTube**
- 2 billion users, 500 hours of video uploaded per minute
- 1 billion video views/day, avg view = 10 minutes at 1 Mbps
- Calculate: storage per year (uploads), bandwidth (views), CDN cost approximation

### Task 3 — Consistency Model Selection
For each scenario, pick the correct consistency model and justify:

1. Bank ledger — transfer between two accounts
2. User profile picture update
3. Social media comments — replies must appear after parent
4. Shopping cart — items added/removed
5. Distributed lock (exactly one service acquires the lock)
6. Netflix "continue watching" progress

### Task 4 — HLD Framework Practice
Apply the full 7-step framework to design a URL shortener (TinyURL):
- No code — just the framework output
- 300M URLs, 100:1 read:write ratio, 5-year retention
- Identify where CAP applies, which consistency model, availability target

---

## 💡 Interview Tips — HLD Fundamentals

| Mistake | Correction |
|---------|-----------|
| "CAP says choose 2 of 3" | CAP says choose C or A *when a partition occurs*. P is always required. |
| "Eventual consistency is always bad" | It's a deliberate trade-off. Facebook likes don't need strong consistency. |
| "More servers = better availability" | Only if they're stateless and behind a LB. Stateful servers need careful HA design. |
| "Just use a cache" | Cache invalidation is one of the hardest problems. When do you invalidate? |
| Jumping to DB choice first | Start with requirements. DB choice follows from consistency/scale/query needs. |
| Not estimating scale | Every HLD starts with numbers. Scale determines architecture. |

### The CAP One-liner for Interviews
> "During a network partition, you can either reject requests to guarantee consistency (CP), or serve potentially stale data to maintain availability (AP). Since partitions are inevitable in distributed systems, the real design question is: for this use case, which is more acceptable — serving stale data or refusing to serve?"

---

## ✅ Module B1 Completion Checklist

- [ ] Can explain CAP theorem without the buzzwords
- [ ] Know the difference between strong, causal, and eventual consistency
- [ ] Can calculate availability given N services in sequence
- [ ] Know all load balancing algorithms and when to use each
- [ ] Memorized the key latency numbers table
- [ ] Can do back-of-envelope for any system in 5 minutes
- [ ] Know the 7-step HLD interview framework by heart
- [ ] Know when to use: CDN, LB, Cache, Queue, SQL, NoSQL, S3
- [ ] Completed Task 1 — CAP scenarios (8 systems)
- [ ] Completed Task 2 — Estimations (WhatsApp + YouTube)
- [ ] Completed Task 3 — Consistency model selection (6 scenarios)
- [ ] Completed Task 4 — URL Shortener full framework walkthrough

**→ Next: Module B2 — Databases at Scale (sharding, replication, SQL vs NoSQL)**
