---
title: "Module C1: Consensus Algorithms — Study Notes"
description: "Module C1 · Week 25 · Track C — Advanced Topics Prerequisites: B1–B14 Goal: Raft consensus, Paxos, leader election, distributed coordination ⚡ Interactive Visual Version Module…"
domain: system-design
track: system-design-hld
order: 203
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-c1-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div style="margin-bottom:24px;padding:14px 20px;background:#e8f0ff;border-left:4px solid #2060e0;border-radius:0 4px 4px 0;font-family:'JetBrains Mono',monospace;font-size:13px;">
  <strong>Module C1 · Week 25 · Track C — Advanced Topics</strong><br>
  <span style="color:#666;">Prerequisites: B1–B14 &nbsp;|&nbsp; Goal: Raft consensus, Paxos, leader election, distributed coordination</span>
</div>
<a href="/learning/system-design/hld/module-c1-consensus/" style="display:inline-block;margin-bottom:32px;padding:10px 20px;background:#2060e0;color:#fff;border-radius:4px;text-decoration:none;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;">⚡ Interactive Visual Version</a>

# Module C1 — Consensus Algorithms: Raft & Paxos
## System Design Mastery Course | Track C: Advanced Topics | Week 25

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** C — Advanced Topics
**Prerequisites:** B1–B12
**Goal:** Consensus is the bedrock of every strongly-consistent distributed system — etcd, ZooKeeper, CockroachDB, Kafka's KRaft mode, and more. Most engineers use these systems without understanding why they work. This module gives you that understanding, making you dangerous in deep-dive interviews and in production when things go wrong.

---

## 1. The Consensus Problem

```
Definition: Get a set of N nodes to agree on a single value, even when
            some nodes crash or messages are delayed.

Why is this hard?
  - Nodes can crash at any moment
  - Messages can be delayed, reordered, or lost (asynchronous network)
  - You can't distinguish a crashed node from a very slow one
  - You need to make progress despite failures

FLP Impossibility Theorem (Fischer, Lynch, Paterson — 1985):
  "In an asynchronous distributed system, no consensus algorithm can
   guarantee both safety AND liveness if even one node may crash."

  Safety:  Never return incorrect result (no two nodes decide differently)
  Liveness: Always eventually return a result (system makes progress)

  Practical implication:
    Paxos and Raft choose safety over liveness.
    They may stall (no progress) during certain failure scenarios,
    but they will NEVER return incorrect results.
    This is the right trade-off for databases and coordination services.
```

---

## 2. Paxos — The Original Consensus Algorithm

### Core Roles
```
Proposer:  Proposes a value to be agreed upon
Acceptor:  Votes on proposed values (stores the agreed value)
Learner:   Learns the final agreed value (receives notifications)

In practice: a single node plays all three roles simultaneously.
```

### Single-Decree Paxos (Agree on ONE value)
```
Phase 1a — PREPARE:
  Proposer chooses a proposal number N (must be unique and higher than any seen).
  Proposer sends PREPARE(N) to a majority of Acceptors.

Phase 1b — PROMISE:
  Each Acceptor receiving PREPARE(N):
    If N > any previously promised proposal number:
      Responds PROMISE(N, accepted_value, accepted_number)
      (accepted_value = the value it previously accepted, if any)
      Promises to never accept proposals < N again.
    Else: ignores (or sends NACK).

Phase 2a — ACCEPT:
  If Proposer receives PROMISE from majority:
    If any PROMISE included an already-accepted value:
      Proposer MUST use that value (not its own)
    Else: Proposer uses its own value
    Proposer sends ACCEPT(N, value) to majority.

Phase 2b — ACCEPTED:
  Each Acceptor receiving ACCEPT(N, value):
    If N >= its promised number: accepts, sends ACCEPTED(N, value) to Learners
    Else: ignores.

Completion:
  Learner sees ACCEPTED from majority → value is chosen (consensus reached).
```

### Why Paxos is Hard to Implement
```
Problems with basic Paxos:
  1. Multi-Paxos needed for log replication (not single value)
  2. Leader election not specified — any node can propose (livelock possible)
  3. Gap handling: what if slot 5 in the log is missing?
  4. Reconfiguration: how do you add/remove nodes safely?
  5. State machine replication on top of Paxos = lots of additional engineering
  6. The paper deliberately left implementation details vague

"Paxos is famously difficult to understand and even harder to implement correctly."
— Diego Ongaro (Raft paper author)

Real implementations: Chubby (Google), Zab (ZooKeeper's variant), Viewstamped Replication
```

---

## 3. Raft — Designed for Understandability

### Core Insight
```
Raft decomposes consensus into three sub-problems:
  1. Leader Election:    Elect one leader; leader has full authority
  2. Log Replication:   Leader accepts log entries, replicates to followers
  3. Safety:            Committed entries are never lost or overwritten

Key simplification vs Paxos:
  Raft has a strong leader — all reads and writes go through leader.
  No concurrent proposals — only leader proposes.
  This eliminates most of the complexity of Paxos.
```

### Node States
```
Every Raft node is in exactly one of three states:

FOLLOWER:
  Passive — responds to requests from Leader and Candidates.
  Starts an election if it doesn't hear from Leader within election timeout (150–300ms).

CANDIDATE:
  Trying to become Leader — sends RequestVote RPCs to all nodes.
  Becomes Leader if it gets votes from majority.
  Returns to Follower if it hears from a valid Leader.

LEADER:
  Handles all client requests.
  Sends heartbeats to all Followers to prevent elections.
  Replicates log entries to Followers.
  Steps down if it discovers a higher term.
```

### Terms — Raft's Logical Clock
```
Term: a monotonically increasing integer. Each election starts a new term.
  Term 1: Node A elected leader
  Term 2: A crashes, B starts election, B elected leader
  Term 3: B crashes, C and D split vote, no leader elected
  Term 4: C wins election

Rules:
  Every RPC includes the sender's current term.
  If node receives RPC with higher term → update term, revert to Follower.
  If node receives RPC with lower term → reject (stale message).
  Terms detect stale leaders — an old leader that reconnects immediately steps down.
```

### Leader Election
```
Trigger: Follower receives no heartbeat within election timeout (150–300ms, random).
  Randomized timeout is KEY — prevents all nodes from starting elections simultaneously.

Election process:
  1. Follower increments its term, transitions to Candidate.
  2. Votes for itself.
  3. Sends RequestVote(term, candidateId, lastLogIndex, lastLogTerm) to all nodes.
  4. Node grants vote IF:
     a. term >= voter's current term
     b. voter hasn't voted this term yet
     c. Candidate's log is at least as up-to-date as voter's log
        (lastLogTerm > voter's lastLogTerm, OR
         lastLogTerm == voter's lastLogTerm AND lastLogIndex >= voter's lastLogIndex)

  5. Candidate receives majority votes → becomes Leader, sends heartbeats.
  6. Two candidates split the vote → both time out, start new election (new term).
     Randomized timeouts ensure they don't split again immediately.

Safety: "Log completeness" — a Candidate can only win if its log is as complete
        as a majority of nodes. This guarantees the winner has all committed entries.
```

### Log Replication
```
Client write flow:
  1. Client sends write request to Leader.
  2. Leader appends entry to its log: {term: 3, index: 47, command: "SET x=5"}
  3. Leader sends AppendEntries(term, leaderId, prevLogIndex, prevLogTerm,
                                entries[], leaderCommit) to all Followers in parallel.
  4. Followers append entry to their log (not yet committed).
  5. Follower responds SUCCESS.
  6. Leader receives SUCCESS from majority → entry is COMMITTED.
  7. Leader applies entry to state machine → responds to client.
  8. Next AppendEntries (or heartbeat) includes updated commitIndex.
  9. Followers apply committed entries to their own state machines.

Consistency check (prevLogIndex + prevLogTerm):
  AppendEntries includes the index and term of the entry BEFORE the new one.
  Follower rejects if its log doesn't match at prevLogIndex/prevLogTerm.
  Leader then sends older entries to bring Follower up to date (log healing).

Log healing:
  Leader maintains nextIndex[i] for each Follower (next entry to send).
  On rejection: decrement nextIndex[i], retry with older entries.
  Follower overwrites any conflicting entries.
  Eventually: Follower's log matches Leader's log up to the committed point.
```

### Commitment and Durability
```
Entry is COMMITTED when:
  It has been replicated to a majority of nodes (quorum = ⌊N/2⌋ + 1).
  For 3 nodes: committed when 2 nodes have it.
  For 5 nodes: committed when 3 nodes have it.

IMPORTANT: Leader only commits entries from its OWN term.
  (Entries from previous terms are committed indirectly when a current-term
   entry commits — they were already replicated, just not yet official.)

Durability:
  Committed entry → at least ⌊N/2⌋ + 1 nodes have it.
  Any future leader must win majority vote.
  Winner's log must be as up-to-date as majority.
  → Future leader guaranteed to have all committed entries.
  → Committed entries are NEVER lost.
```

---

## 4. Raft vs Paxos — The Key Differences

```
┌─────────────────────┬──────────────────────┬─────────────────────┐
│ Property            │ Paxos                │ Raft                │
├─────────────────────┼──────────────────────┼─────────────────────┤
│ Leadership          │ Any node can propose │ Strong single leader│
│ Log ordering        │ Complex (gaps OK)    │ Simple sequential   │
│ Understandability   │ Hard                 │ Designed to be easy │
│ Reconfiguration     │ Not specified        │ Joint consensus     │
│ Leader election     │ Not specified        │ Built-in, specified │
│ Real implementations│ Chubby, Zab, ViewRep │ etcd, CockroachDB   │
│ Livelock possible   │ Yes (two proposers)  │ No (randomized TO)  │
└─────────────────────┴──────────────────────┴─────────────────────┘
```

---

## 5. Raft in the Real World

### etcd (Kubernetes control plane)
```
etcd uses Raft for all writes. Every Kubernetes object (Pod, Service, Deployment)
is stored in etcd. When you run `kubectl apply`, it goes through Raft consensus.

Typical cluster: 3 or 5 etcd nodes.
  3 nodes: tolerates 1 failure (quorum = 2)
  5 nodes: tolerates 2 failures (quorum = 3)
  7 nodes: rarely used — write latency increases with more nodes

Write path:
  kubectl → API Server → etcd leader → replicated to followers → committed → response

Read path:
  etcd default: linearizable reads (go through leader — always fresh)
  etcd option:  serializable reads (any node — may be slightly stale)

Why 5 nodes for production:
  Rolling upgrades: take 1 node down → still have quorum (4 of 5 available)
  Zone failure:     lose 1 AZ (1 node) → still have quorum
  Two simultaneous failures tolerated → much safer for HA
```

### CockroachDB
```
CockroachDB uses Raft per range (default 64 MB ranges).
Each key range has its own Raft group.

Structure:
  Table data is split into ranges.
  Each range has 3 replicas (by default).
  Each range's replicas form a Raft group.
  Writes to a range go through that range's Raft leader.

Consequence: a 3-node CockroachDB cluster runs THOUSANDS of Raft groups simultaneously.
  Each node is simultaneously Leader for some ranges, Follower for others.
  Load is naturally distributed.

Range splits: when a range grows beyond 64 MB, it splits → two Raft groups.
Lease holder: the Raft leader for a range — handles reads for that range.
```

### Kafka KRaft (replacing ZooKeeper)
```
Pre-Kafka 3.x: Kafka used ZooKeeper (ZAB protocol, Paxos variant) for:
  - Broker metadata (who is leader for which partition)
  - Controller election (which broker is the controller)

Kafka 3.x+ KRaft mode: Kafka implements its own Raft variant (KRaft).
  - Controller quorum (3 or 5 controller nodes) uses Raft for metadata log
  - Eliminates ZooKeeper dependency
  - Faster controller failover (~30s → milliseconds)
  - Metadata stored in a Kafka topic (the __cluster_metadata topic)

Benefits: No separate ZooKeeper cluster to manage. Simpler ops.
```

### ZooKeeper / ZAB
```
ZAB (ZooKeeper Atomic Broadcast) = Paxos variant, similar to Raft.
Key difference from Raft:
  ZAB uses epoch numbers (≈ Raft terms) but recovery is different.
  In ZAB, new leader must re-propose all uncommitted proposals from previous epoch.
  In Raft, new leader simply commits new entries; old entries commit implicitly.

ZooKeeper use cases (even post-Kafka KRaft):
  Leader election for non-Kafka systems
  Distributed locks (ephemeral znodes)
  Config management
  Service discovery (still widely used despite Consul being newer)
```

---

## 6. Quorum Math & Failure Tolerance

```
Cluster size N, quorum Q = ⌊N/2⌋ + 1 (simple majority)

N=3: Q=2, tolerates 1 failure  (F=1)
N=5: Q=3, tolerates 2 failures (F=2)
N=7: Q=4, tolerates 3 failures (F=3)

Formula: F = ⌊(N-1)/2⌋

Why odd numbers?
  Even N doesn't give more fault tolerance:
  N=4: Q=3, F=1 (same as N=3, but more nodes to manage)
  N=6: Q=4, F=2 (same as N=5, but more nodes to manage)
  → Always use odd-sized clusters

Write latency vs fault tolerance:
  More nodes = more replicas to wait for = higher write latency
  5-node cluster: must wait for 3 acknowledgements
  3-node cluster: must wait for 2 acknowledgements
  Practical: 3 nodes (dev/small prod), 5 nodes (production HA)

Split-brain prevention:
  Network partition splits 5-node cluster into [3] and [2].
  [3] has quorum → can elect leader, process writes.
  [2] cannot reach quorum → cannot elect leader, rejects writes.
  Result: [3] becomes the active partition, [2] is read-only/unavailable.
  No split-brain — only one partition can ever have quorum at a time.
```

---

## 7. Common Interview Questions on Consensus

```
Q: "How does Raft prevent split-brain?"
A: "Quorum requirement — a leader can only be elected and can only commit
    entries with votes/acknowledgements from a majority of nodes (⌊N/2⌋+1).
    In a network partition, only one partition can have a majority. The other
    partition cannot elect a leader or commit writes. Two active leaders
    simultaneously is impossible — they'd need two separate majorities,
    which requires more than N total nodes."

Q: "What happens if the Raft leader crashes mid-write?"
A: "If the entry was not yet committed (not replicated to majority), the new
    leader won't have it — it's simply lost from the client's perspective
    (client gets a timeout, must retry). If the entry WAS committed (majority
    had it), the new leader's log completeness check guarantees it will be
    elected only if it has all committed entries — so the entry survives."

Q: "Why use 5 nodes instead of 3?"
A: "3 nodes tolerates 1 failure. 5 nodes tolerates 2 simultaneous failures.
    In a cloud environment running on 3 AZs, a 5-node cluster can lose an
    entire AZ (1-2 nodes) plus a second node in another AZ and still maintain
    quorum. For rolling upgrades: take 1 node offline for maintenance → 4/5
    still available, quorum maintained. The write latency cost (waiting for
    3 vs 2 acks) is typically acceptable for coordination services."

Q: "What is the difference between Raft and Paxos?"
A: "Both solve consensus. Paxos allows any node to propose values, making it
    flexible but complex — especially for log replication. Raft enforces a
    strong leader who is the only proposer; all writes go through the leader.
    This simplifies reasoning: the leader's log is always the authoritative
    one. Raft was explicitly designed to be understandable and specifies
    leader election and reconfiguration — areas Paxos leaves to the implementer."
```

---

## 📝 Tasks

### Task 1 — Raft Election Simulation
Simulate a 5-node Raft cluster (on paper or code):
1. All nodes start as Followers in term 1. Node A is the leader.
2. A crashes. Show the election: which node starts first (why?), what messages are exchanged, who wins.
3. During the election, a network partition isolates Node E. Show what happens to E during and after.
4. A comes back online (now stale, term=1). What does it do when it receives a heartbeat from the new leader (term=2)?

### Task 2 — Log Replication & Healing
5-node cluster (leader L, followers F1–F4). Log state after some entries:
```
L:  [1:SET a=1] [1:SET b=2] [2:SET c=3] [2:SET d=4]  ← leader (term 2)
F1: [1:SET a=1] [1:SET b=2] [2:SET c=3] [2:SET d=4]  ← up to date
F2: [1:SET a=1] [1:SET b=2] [2:SET c=3]               ← missing one entry
F3: [1:SET a=1] [1:SET b=2]                            ← missing two entries
F4: [1:SET a=1] [1:SET b=2] [1:SET x=9]               ← conflicting entry!
```
1. Which entries are committed? (quorum = 3)
2. How does L heal F2, F3, and F4?
3. F4's `[1:SET x=9]` — where did it come from? What happens to it?

### Task 3 — Quorum Failure Scenarios
For a 5-node etcd cluster across 3 AZs (AZ1: nodes 1,2 | AZ2: nodes 3,4 | AZ3: node 5):
1. AZ2 goes down entirely (nodes 3+4 fail). Can the cluster elect a leader? Process writes?
2. Nodes 1, 3, 5 partition away from 2 and 4. What happens in each partition?
3. You want to do a rolling upgrade (restart one node at a time). How many nodes can be down simultaneously while maintaining quorum?
4. You want to expand from 3 to 5 nodes. What is the risk during the expansion? (hint: joint consensus)

### ⭐ Task 4 — Design etcd-Backed Leader Election
Design a leader election service for your microservices:
1. Use etcd leases (TTL keys) to implement leader election — describe the protocol
2. What happens if the leader's network connection to etcd is slow (but not broken)?
3. What happens if the leader process crashes without releasing the lease?
4. How do you prevent two nodes from both thinking they are leader (split-brain at the application layer)?
5. Compare to ZooKeeper ephemeral nodes — same pattern, different guarantees?

---

## ✅ Completion Checklist

- [ ] FLP impossibility: safety vs liveness, why it matters for Raft/Paxos
- [ ] Paxos: Prepare → Promise → Accept → Accepted — all four phases
- [ ] Paxos: why proposer must use already-accepted value (safety invariant)
- [ ] Paxos: why it's hard to implement (multi-Paxos, gaps, reconfiguration)
- [ ] Raft: three sub-problems (election, log replication, safety)
- [ ] Raft: three node states (Follower, Candidate, Leader) and transitions
- [ ] Raft: terms as logical clock — stale leaders immediately step down
- [ ] Leader election: randomized timeouts, log completeness check, majority vote
- [ ] Log replication: AppendEntries, prevLogIndex/prevLogTerm consistency check
- [ ] Commitment: entry committed when majority has it
- [ ] Log healing: nextIndex, decrement on rejection, follower overwrites conflicts
- [ ] Split-brain prevention: quorum math — only one partition can have majority
- [ ] Quorum math: N=3→F=1, N=5→F=2, N=7→F=3; always odd clusters
- [ ] etcd: Raft for Kubernetes control plane, 3 vs 5 node trade-offs
- [ ] CockroachDB: Raft per range, thousands of Raft groups simultaneously
- [ ] Kafka KRaft: Raft replacing ZooKeeper for metadata
- [ ] ZAB vs Raft: key differences
- [ ] Completed Task 1 — Raft election simulation
- [ ] Completed Task 2 — log replication + healing
- [ ] Completed Task 3 — quorum failure scenarios
- [ ] Completed Task 4 — etcd-backed leader election design

**→ Next: Module C2 — Geo-Distribution & Multi-Region Architecture**

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'JetBrains Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b14-kubernetes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B14 Kubernetes</a>
  <a href="/learning/system-design/hld/module-c1-consensus/" style="padding:12px 24px;border:1px solid #2060e0;color:#2060e0;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-c2-notes/" style="padding:12px 24px;background:#2060e0;color:#fff;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: C2 Geo-Distribution →</a>
</div>
