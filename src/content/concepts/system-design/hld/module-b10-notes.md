---
title: "Module B10 Notes: Consistent Hashing"
description: "Module B10 — Consistent Hashing & Service Discovery System Design Mastery Track B: HLD Week 20 --- 🎯 Module Overview Duration: 1 Week Prerequisites: B1–B9 Goal: Consistent…"
domain: system-design
track: system-design-hld
order: 121
url: /learning/system-design/hld/module-b10-notes/
---

# Module B10 — Consistent Hashing & Service Discovery
## System Design Mastery | Track B: HLD | Week 20

---

## 🎯 Module Overview

**Duration:** 1 Week | **Prerequisites:** B1–B9  
**Goal:** Consistent hashing appears as a component question in every distributed systems interview (sharded caches, distributed DBs, CDN routing). Service discovery is required for any microservices design. Both are foundational.

---

## 1. The Modulo Hashing Problem

```
Naive: shard = hash(key) % N   (N = number of nodes)

Problem: Add a 4th node (N=3 → N=4):
  ~75% of all keys now map to different nodes
  Cache: 75% miss rate instantly (thundering herd)
  Sharded DB: 75% queries hit wrong shard (data missing)

Consistent hashing solves this:
  Adding/removing 1 node remaps only ~1/N keys
  For 12-node cluster + 13th node: only 7.7% move
  With modulo: 92.3% would move
```

---

## 2. The Hash Ring

```
Concept: map both nodes AND keys to a circular ring [0, 2^32)

Setup:
  Node A → hash("NodeA#0") = pos 12, hash("NodeA#1") = pos 67, ...
  Node B → hash("NodeB#0") = pos 45, ...
  Node C → hash("NodeC#0") = pos 78, ...

Key assignment:
  Hash the key → position on ring
  Walk CLOCKWISE to find next node
  That node owns the key

Example (no vnodes):
  "user:123" → pos 20 → next node clockwise at 45 = Node B
  "user:456" → pos 60 → next node clockwise at 78 = Node C
  "user:789" → pos 90 → wraps to 12 = Node A

Adding Node D at position 55:
  Before: keys 45–78 belonged to Node C
  After:  keys 45–55 → Node D, keys 55–78 still Node C
  Only keys in (45, 55] remapped → ~1/N of all keys ✓
```

---

## 3. Virtual Nodes (Vnodes)

```
Problem with basic ring: unequal arc sizes → unequal load
  Node placement is random → some nodes get 5× more keys than others

Solution: K virtual node positions per physical node
  Node A → 150 positions spread randomly around the ring
  Node B → 150 positions spread randomly
  Each virtual node maps to the physical node

Benefits:
  1. Load balancing: with K=150, each node's share ≈ 1/N ± <5%
  2. New node: 150 vnodes spread everywhere → steals from ALL nodes equally
  3. Heterogeneous capacity:
       Powerful node (32 cores): 300 vnodes → 2× data
       Standard node (16 cores): 150 vnodes → 1× data
       Weak node (8 cores):       75 vnodes → 0.5× data
       No special logic — just different vnode counts

Production standards:
  Cassandra: 256 vnodes per physical node (default)
  Redis Cluster: 16,384 hash slots (fine-grained = many vnodes)
```

---

## 4. Java Implementation

```java
public class ConsistentHashRing {
    private final TreeMap<Integer, String> ring = new TreeMap<>();
    private final int VNODES = 150;

    private int hash(String key) {
        // MurmurHash — fast, non-crypto, consistent
        return Hashing.murmur3_32().hashString(key, UTF_8).asInt();
    }

    public void addNode(String node) {
        for (int v = 0; v < VNODES; v++)
            ring.put(hash(node + "#" + v), node);
    }

    public void removeNode(String node) {
        for (int v = 0; v < VNODES; v++)
            ring.remove(hash(node + "#" + v));
    }

    public String getNode(String key) {
        if (ring.isEmpty()) throw new IllegalStateException("No nodes");
        // ceilingEntry = first node at or after key's position (clockwise)
        Map.Entry<Integer, String> e = ring.ceilingEntry(hash(key));
        return (e != null ? e : ring.firstEntry()).getValue(); // wrap if at end
    }
}
```

```
Key insight: TreeMap.ceilingEntry() = O(log N) clockwise walk
  firstEntry() handles the ring wrap-around case
  addNode/removeNode: O(VNODES × log N)
  getNode: O(log N) — fast even with 100K vnodes on ring
```

---

## 5. Real-World Use

```
Redis Cluster:
  16,384 hash slots (not modulo — consistent hashing variant)
  CRC16(key) % 16384 → slot → assigned node
  Hash tags: {user_id} forces related keys to same slot

Apache Cassandra:
  256 vnodes per node by default
  Replication Factor 3: 3 consecutive ring nodes own each key
  Snitch routes reads to nearest replica

Amazon DynamoDB:
  Consistent hashing for partition routing
  Auto-scaling splits hot partitions → minimal key remapping

CDN (Akamai, Cloudflare):
  Same URL → same cache server within PoP → higher hit rate
  Adding cache server: only ~1/N URLs get cache misses

Sticky Load Balancing:
  Same user → same backend server (in-memory session cache works)
  Server failure: only that server's users remapped (not all)
```

---

## 6. Service Discovery

```
Problem: How does Service A find Service B in a dynamic cluster?

Old way: hardcode IPs
  service_b = "192.168.1.45:8080"
  Problem: IP changes on restart / scale / deployment

New way: Service Registry
  Service B registers: {name, host, port, health-check URL}
  Service A queries: "where is payment-service?" → current IPs
  Registry removes dead instances via health checks
```

### Discovery Patterns

```
Pattern 1: Client-Side Discovery
  Client → Registry (get instances) → Client picks one → Client → Service
  Pro: no extra hop, client controls LB strategy
  Con: LB logic in every client, multiple language SDKs needed

Pattern 2: Server-Side Discovery ★ (production default)
  Client → Gateway → Registry (get instances) → Gateway → Service
  Pro: clients are simple, central LB policy, language-agnostic
  Con: extra hop through gateway, gateway is critical path

Pattern 3: DNS-Based (Kubernetes default)
  Registry publishes IPs as DNS A records
  payment-service.default.svc.cluster.local → current pod IPs
  Pro: standard protocol, k8s native, no client library
  Con: DNS TTL caching can serve stale IPs
```

---

## 7. Consul & ZooKeeper

### Consul (HashiCorp)
```
Features: service registration, health checks, KV store, service mesh, multi-DC

Registration:
  PUT /v1/agent/service/register
  {"Name": "payment-service", "Address": "10.0.1.23", "Port": 8080,
   "Check": {"HTTP": "http://10.0.1.23:8080/health", "Interval": "10s"}}

Discovery (healthy only):
  GET /v1/health/service/payment-service?passing=true

Watch for changes (long-poll):
  GET /v1/health/service/payment-service?passing=true&index=50&wait=30s
  → Blocks until change or timeout → client auto-refreshes instance list
```

### ZooKeeper
```
Distributed coordination (Apache). Beyond service discovery:
  Leader election, distributed locks, configuration management

Service discovery via ephemeral znodes:
  Service registers: create /services/payment/instance-1 [EPHEMERAL]
  Ephemeral = auto-deleted when service disconnects (session expires)
  Clients watch /services/payment → notified on create/delete
  Session timeout (default 30s) → ephemeral znodes deleted → watchers fire
```

| Feature | Consul | ZooKeeper | etcd (k8s) |
|---|---|---|---|
| Consistency | Raft | ZAB | Raft |
| Health checks | Built-in (HTTP/TCP) | Session timeout only | TTL leases |
| Primary use | Service mesh | Locks, leader election | K8s control plane |

---

## 8. Health Checks

```
Types:
  TCP check:    Can we connect to port 8080? (basic liveness)
  HTTP check:   GET /health → 200 OK? (application-level)
  Script check: custom script returns 0 for healthy
  gRPC check:   gRPC health protocol

/health endpoint should return:
  HTTP 200 {"status":"healthy", "checks": {"database":"connected", "redis":"connected"}}
  HTTP 503 {"status":"unhealthy", "checks": {"database": "connection refused"}}

Thresholds:
  Consul: 2 consecutive failures → mark critical → deregister
  Check interval 10s → failure detected within 20–30s

Kubernetes Liveness vs Readiness:
  Liveness: is the process alive? → kubelet restarts if failing
  Readiness: is the service ready for traffic? → removed from LB if failing
  A service can be alive but not ready (warming up cache, migrations running)
  Only readiness affects service discovery routing
```

---

## 9. Gossip Protocol

```
Used by: Consul (SWIM), Cassandra, Riak for cluster membership

How it works:
  Each node randomly selects K neighbors every T seconds and shares state
  "Node X joined" → spreads to K nodes → each shares to K more → ...
  Propagation time: O(log N) rounds → all N nodes informed quickly

Properties:
  Eventually consistent: all nodes converge to same view (not instant)
  Fault tolerant: no single point of failure, no central coordinator
  Scalable: O(log N) communication per dissemination round

Gossip vs Raft:
  Gossip: eventually consistent, no leader, scales to thousands of nodes
           → use for: membership, failure detection
  Raft:   strongly consistent, leader-based, ~5-7 nodes practical
           → use for: config, leader election, distributed locks

Consul uses BOTH:
  Gossip (SWIM protocol) for membership + failure detection
  Raft for KV store + service catalog (needs consistency)
```

---

## 📝 Tasks

### Task 1 — Hash Ring Implementation
1. Implement `ConsistentHashRing` in Java with TreeMap
2. Test: 3 nodes, 1000 keys → ~33% per node (±10%)
3. Add 4th node → verify ~25% keys remapped (not 75%)
4. Remove node → verify only that node's keys remapped
5. Handle hash collision: two nodes at same ring position

### Task 2 — Virtual Node Analysis
1. Simulate 3 nodes with 1, 10, 50, 150, 300 vnodes
2. Hash 10,000 keys in each configuration
3. Measure std deviation across nodes — at what vnode count is it &lt;5%?
4. Compare: 4th node added with K=150 vs modulo hashing

### Task 3 — Service Discovery Design
50 microservices, 3–10 instances each:
1. Client-side vs server-side — pick and justify
2. Pod start: step-by-step until first request
3. Pod crash (no SIGTERM): when do clients stop seeing errors?
4. Consul partition: 2 servers can't reach other 3 — what happens?
5. /health design: what checks, what thresholds?

### ⭐ Task 4 — URL Shortener + Consistent Hashing
5 Redis cache nodes, use consistent hashing:
1. Vnodes per node — justify choice
2. Node 3 fails — miss rate vs modulo
3. Add node 6 — % cache misses needed to reload from DB
4. Modulo comparison
5. Zero-downtime migration from modulo to consistent hashing

---

## ✅ Completion Checklist

- [ ] Modulo flaw: N→N+1 remaps ~N/(N+1) of all keys
- [ ] Hash ring: nodes and keys on [0, 2^32), clockwise walk to find owner
- [ ] Virtual nodes: K positions per physical node, ~150 is production standard
- [ ] Heterogeneous capacity via weighted vnode counts
- [ ] TreeMap implementation: ceilingEntry O(log N), firstEntry for wrap
- [ ] 1/N keys remapped on add/remove
- [ ] Use cases: Redis Cluster, Cassandra, CDN, sticky LB
- [ ] Service discovery: registry, register, query, health check
- [ ] Client-side vs server-side trade-offs
- [ ] DNS-based (Kubernetes CoreDNS)
- [ ] Consul HTTP API: register, passing=true, long-poll watch
- [ ] ZooKeeper: ephemeral znodes, auto-delete on session expire
- [ ] Health checks: TCP/HTTP/gRPC, 2-failure threshold, 10s interval
- [ ] Liveness vs readiness — different kubelet actions
- [ ] Gossip: O(log N) propagation, eventual consistency, no leader
- [ ] Gossip vs Raft — when to use each
- [ ] Completed Task 1 — hash ring implementation
- [ ] Completed Task 2 — vnode distribution analysis
- [ ] Completed Task 3 — service discovery design
- [ ] Completed Task 4 — URL shortener with consistent hashing

**→ Next: Module B11 — ACID, Distributed Transactions &amp; Saga**

<br>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b9-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B9 Rate Limiter Notes</a>
  <a href="/learning/system-design/hld/module-b10-consistent-hashing/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b11-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B11 Distributed Tx →</a>
</div>
