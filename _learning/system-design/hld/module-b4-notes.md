---
layout: default
title: "Module B4 Notes — Message Queues"
permalink: /learning/system-design/hld/module-b4-notes/
---

# Module B4 — Message Queues
## System Design Mastery Course | Track B: HLD | Week 14

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD | **Prerequisites:** B1, B2, B3

Message queues decouple services, absorb traffic bursts, and enable async processing. Kafka appears in nearly every FAANG design question.

### Why Message Queues?
- **Decoupling:** A doesn't need to know B's location or count
- **Buffering:** Queue absorbs bursts; B processes at its own rate
- **Reliability:** If B is down, messages wait (not lost)
- **Fanout:** One message → many consumers (Kafka consumer groups)
- **Ordering:** Messages in partition are strictly ordered
- **Replay:** Consumers can re-read past messages (Kafka retention)

---

## 1. Core Concepts

### Three Messaging Models

| Model | Delivery | Retention | Best For |
|-------|----------|-----------|---------|
| Message Queue (RabbitMQ, SQS) | One consumer | Delete on ACK | Task distribution, work queues |
| Pub-Sub (Redis Pub/Sub) | All subscribers | Not persistent | Real-time notifications |
| Event Stream (Kafka, Kinesis) | All consumer groups | Durable log (days-years) | Event sourcing, data pipelines, audit logs |

---

## 2. Kafka Architecture

### Topic → Partition → Offset
```
Topic: "user-events" (3 partitions)
  Partition 0: [msg0 offset=0] [msg3 offset=1] [msg6 offset=2] ...
  Partition 1: [msg1 offset=0] [msg4 offset=1] [msg7 offset=2] ...
  Partition 2: [msg2 offset=0] [msg5 offset=1] [msg8 offset=2] ...

Ordering: guaranteed WITHIN a partition, NOT across partitions
Partition key: hash(key) % numPartitions → same key → same partition
```

### Consumer Groups
```
Topic: "order-placed" (6 partitions)

Consumer Group A (inventory-service): [C1→P0,P1] [C2→P2,P3] [C3→P4,P5]
Consumer Group B (email-service):     [C1→P0,P1,P2,P3,P4,P5]  (single consumer)
Consumer Group C (analytics-service): [C1→P0] [C2→P1] ... [C6→P5]

Each group gets ALL messages. Groups are fully independent.
Rule: partitions >= consumers per group for full utilization.
```

### Replication
```
replication.factor=3 → 1 leader + 2 ISR (In-Sync Replicas)
min.insync.replicas=2 → at least 2 replicas ACK before producer gets ACK
acks=all → strongest durability (combine with above)

Tolerate: 1 broker failure with no data loss (ISR has 2 copies)
Failover: ZooKeeper/KRaft elects new leader from ISR in ~30s
```

---

## 3. Delivery Semantics

### At-Most-Once
- Producer fires and forgets. Consumer auto-commits before processing.
- Risk: crash after commit, before processing → **message lost**
- Use: analytics, metrics, non-critical logs (loss acceptable)

### At-Least-Once (Default)
- Producer retries on failure. Consumer commits AFTER processing.
- Risk: crash after processing, before commit → **message processed twice**
- Use: most systems — handle with idempotent consumers

### Exactly-Once
- Idempotent producer (seq number per message, broker deduplicates) + Transactions (atomic multi-partition write + offset commit)
- Config: `enable.idempotence=true`, `acks=all`, `transactional.id=unique`
- Cost: ~20% throughput reduction
- Use: financial transactions, inventory — when duplicates cause real harm

### Idempotent Consumer Pattern
```java
public void processPayment(PaymentEvent e) {
    if (db.exists("processed:" + e.idempotencyKey)) return; // Already done
    db.debitAccount(e.accountId, e.amount);
    db.markProcessed("processed:" + e.idempotencyKey);
    // Safe to run twice — second run is no-op
}
```

---

## 4. Kafka vs RabbitMQ

| Aspect | Kafka | RabbitMQ |
|--------|-------|----------|
| Model | Pull (consumers fetch) | Push (broker delivers) |
| Retention | Durable log (days–years) | Delete on ACK |
| Throughput | Millions msg/sec | Hundreds of thousands |
| Ordering | Within partition | Within queue |
| Replay | Yes (any offset) | No |
| Consumer groups | Multiple independent | Competing consumers |
| Use case | Event streaming, pipelines | Task queues, routing |

**Choose Kafka:** High throughput, replay needed, multiple consumer groups, event sourcing, CDC pipelines.

**Choose RabbitMQ:** Complex routing (topic/header exchanges), per-message TTL, priority queues, work queue pattern, simpler setup.

---

## 5. Key Patterns

### Fan-Out
One topic → N consumer groups, each processing independently.
Order placed → inventory, email, analytics, fraud — all get every event.

### Dead Letter Queue (DLQ)
After N failed retries → route to DLQ topic for inspection/manual replay. Prevents stuck messages blocking the queue.

### Back-Pressure
`consumer_lag = latest_offset - committed_offset`
High lag → add consumers (up to numPartitions) or optimize consumer logic.

### Partition Key for Ordering
Partition by `user_id` or `order_id` → all events for same entity → same partition → ordered. Trade: no global order, but per-entity order + cross-entity parallelism.

### Log Compaction
Retain only latest message per key. Consumers rebuild current state without full history. Use for: user profiles, config changes, inventory levels.

---

## 6. Producer/Consumer Config Cheat Sheet

```
# Producer
acks=all                    # Strongest durability
enable.idempotence=true     # Safe retries
retries=MAX_INT             # Keep retrying
linger.ms=5                 # Batch for 5ms → throughput
compression.type=snappy     # 4× compression

# Consumer
enable.auto.commit=false    # Manual commit → at-least-once
auto.offset.reset=earliest  # New group reads from beginning
max.poll.records=500        # Batch size per poll()

# Topic
num.partitions=12           # Parallelism ceiling
replication.factor=3        # Durability
min.insync.replicas=2       # Minimum ACKs
retention.ms=604800000      # 7 days
```

---

## 📝 Tasks

### Task 1 — Delivery Semantics Analysis
Choose at-most-once / at-least-once / exactly-once for each. Explain failure scenario and idempotency strategy:
1. Real-time page view counter for analytics
2. Bank transfer triggered by Kafka event
3. Email: "Your order has shipped"
4. Inventory decrement when order placed
5. User activity feed update (friends' likes)

### Task 2 — Partition Key Design
Choose partition key, explain ordering guarantee and hotkey risk:
1. E-commerce order events (created, paid, shipped, delivered)
2. WhatsApp group chat messages
3. Real-time stock prices for 10,000 tickers
4. IoT sensor readings from 100K devices
5. User login/logout events

### Task 3 — Kafka vs RabbitMQ Decision
1. 8 services all react to every new user signup
2. Background job: weekly digest emails to 10M users
3. Fraud detection: audit every transaction for 5 years
4. Real-time bidding: each impression handled by exactly one bidder
5. CDC: stream DB changes to Elasticsearch for search indexing

### ⭐ Task 4 — Uber Event Streaming Architecture
5M active drivers sending location every 4 seconds. Ride lifecycle events. Surge pricing per zone per minute. Analytics.

Design: topic layout, partition keys, consumer groups, delivery semantics, retention policies, and estimate events/sec + storage/day.

---

## ✅ Completion Checklist

- [ ] Know 3 messaging models: queue, pub-sub, event stream
- [ ] Kafka: topic, partition, consumer group, offset, ISR
- [ ] Partition key selection and ordering implications
- [ ] All 3 delivery semantics with failure scenarios
- [ ] Idempotent consumer implementation
- [ ] Kafka vs RabbitMQ decision criteria
- [ ] Fan-out pattern via consumer groups
- [ ] Dead letter queue purpose and flow
- [ ] Back-pressure and consumer lag monitoring
- [ ] Key Kafka configs (acks, retries, replication.factor)
- [ ] Can estimate Kafka scale: events/sec → partitions → storage
- [ ] Tasks 1–3 completed
- [ ] Task 4: Uber streaming architecture completed

<br>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b3-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B3 Caching Notes</a>
  <a href="/learning/system-design/hld/module-b4-message-queues/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b5-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B5 URL Shortener →</a>
</div>
