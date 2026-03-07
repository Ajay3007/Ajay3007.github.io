# Module B11 — ACID, Distributed Transactions & Saga Pattern
## System Design Mastery Course | Track B: HLD | Week 21

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Fundamentals Deep Dive
**Prerequisites:** B1–B10
**Goal:** Every distributed system faces the problem of multi-service consistency. This module covers the full spectrum from single-DB ACID transactions to distributed Sagas. Appears in every interview involving payments, order processing, or any multi-step operation spanning services.

---

## 1. ACID — The Foundation

```
ACID properties guarantee reliable database transactions:

A — Atomicity
  All operations in a transaction succeed, or all fail together.
  No partial state. Money can't leave account A without arriving at account B.
  Implementation: write-ahead log (WAL), rollback on failure

C — Consistency
  Every transaction takes the DB from one valid state to another valid state.
  Constraints, triggers, and rules are never violated.
  Example: balance cannot go negative if there's a constraint preventing it

I — Isolation
  Concurrent transactions don't interfere with each other.
  Each transaction sees a consistent snapshot of the database.
  Levels: Read Uncommitted → Read Committed → Repeatable Read → Serializable

D — Durability
  Committed transactions survive crashes.
  Once "commit" returns, data is on disk (WAL flushed, fsync called).
  Even if server crashes immediately after, the commit survives
```

### Isolation Levels (The Detail That Separates Good Answers)
```
Problem: 4 phenomena that can occur without proper isolation

1. Dirty Read:    Transaction A reads data written by uncommitted Transaction B.
                  B then rolls back → A read data that never existed.

2. Non-Repeatable Read: A reads row X. B updates row X and commits. A reads X again → different value.
                        Same SELECT returns different results within one transaction.

3. Phantom Read:  A queries "all users with age > 18" → 5 rows.
                  B inserts a new user age 25 and commits.
                  A re-queries → 6 rows. A "phantom" row appeared.

4. Lost Update:   A reads balance=100. B reads balance=100. A writes 110. B writes 120.
                  A's update is lost. Should be 130 (both +10 and +20 applied).

Isolation levels (weakest → strongest):
  Read Uncommitted: dirty reads allowed. Fastest. Almost never used.
  Read Committed:   no dirty reads. PostgreSQL default. Most common.
  Repeatable Read:  no dirty reads, no non-repeatable reads. MySQL InnoDB default.
  Serializable:     no dirty reads, no phantoms, no lost updates. Slowest. Strongest.

Trade-off: stronger isolation = more locking = lower concurrency = lower throughput
```

---

## 2. The Distributed Transaction Problem

```
In a microservices world, a single business operation spans multiple services/DBs:

Order placement example:
  1. Order Service:   create order record in orders_db
  2. Payment Service: deduct payment from payment_db
  3. Inventory Service: reserve item in inventory_db
  4. Notification Service: send confirmation email

Problem: these are 4 separate databases. There is no single transaction that spans them.
  - Order created, payment deducted, then inventory reservation fails →
    customer charged for an item they can't receive!

CAP Theorem reminder:
  Distributed systems can only guarantee 2 of: Consistency, Availability, Partition tolerance
  In practice: choose AP (available, eventually consistent) or CP (consistent, may be unavailable)
  Distributed transactions attempt CP — they sacrifice availability for consistency
```

---

## 3. Two-Phase Commit (2PC)

```
Classic solution: coordinate a distributed transaction across multiple services.

Phase 1 — Prepare:
  Coordinator sends PREPARE to all participants
  Each participant:
    - Executes the transaction locally (but does NOT commit)
    - Writes a prepare record to its WAL
    - Responds READY (if success) or ABORT (if failure)

Phase 2 — Commit or Abort:
  If ALL participants respond READY:
    Coordinator sends COMMIT to all → participants commit → respond DONE
  If ANY participant responds ABORT:
    Coordinator sends ABORT to all → participants rollback → respond DONE

Guarantees:
  ✓ Atomicity across services — either all commit or none do
  ✓ Consistency — no partial state

PROBLEMS with 2PC:
  1. Blocking:  If coordinator crashes after PREPARE but before COMMIT, participants
                are stuck in "uncertain" state holding locks. Cannot proceed or rollback.
                Recovery requires coordinator to restart (minutes → system frozen)

  2. Availability: Coordinator = SPOF. Coordinator down → all transactions blocked.
                  2PC violates CAP Availability for the duration of uncertainty.

  3. Performance: Multiple network roundtrips (prepare + commit) per transaction.
                  ~2–5× slower than local transaction. Unacceptable for high-throughput.

  4. Lock contention: Participants hold locks between phases.
                      Slow participant = locks held longer = more contention.

Where 2PC is still used:
  - Single-vendor databases (MySQL XA transactions within one cluster)
  - Low-throughput, high-consistency needs (banking batch jobs)
  - Tightly coupled systems where coordinator crash is recoverable quickly
```

---

## 4. Saga Pattern — The Modern Solution

```
Instead of a distributed transaction, break the operation into a sequence of
LOCAL transactions, each of which publishes an event or message to trigger the next.

If any step fails: run compensating transactions to undo the completed steps.

Key properties:
  ✓ No distributed locks (each step is a local transaction)
  ✓ High availability (each service independently available)
  ✓ Scales to many services
  ✗ Eventually consistent (not immediately consistent)
  ✗ Requires compensating transactions (rollback is explicit, not automatic)

Order placement as a Saga:
  Step 1: Order Service → creates order (status: PENDING) → publishes "OrderCreated"
  Step 2: Payment Service → deducts payment → publishes "PaymentProcessed"
  Step 3: Inventory Service → reserves item → publishes "InventoryReserved"
  Step 4: Order Service → updates order (status: CONFIRMED) → publishes "OrderConfirmed"
  Step 5: Notification Service → sends confirmation email

If Step 3 fails (inventory unavailable):
  Compensating Step 3: (none needed — reservation failed, nothing to undo)
  Compensating Step 2: Payment Service → refunds payment
  Compensating Step 1: Order Service → cancels order (status: CANCELLED)
```

---

## 5. Saga: Choreography vs Orchestration

### Choreography (Event-Driven)
```
Each service listens for events and reacts independently.
No central coordinator — services talk through a message bus (Kafka/RabbitMQ).

Order Saga (choreography):
  [Order Service] → publishes "OrderCreated" to Kafka
  [Payment Service] listens → processes payment → publishes "PaymentProcessed"
  [Inventory Service] listens → reserves item → publishes "InventoryReserved"
  [Order Service] listens → marks order CONFIRMED → publishes "OrderConfirmed"
  [Notification] listens → sends email

On failure (payment fails):
  [Payment Service] → publishes "PaymentFailed"
  [Order Service] listens for "PaymentFailed" → cancels order

Pros:
  ✓ Loose coupling — services don't know about each other directly
  ✓ Easy to add new steps (just subscribe to events)
  ✓ No SPOF coordinator

Cons:
  ✗ Hard to track overall saga state ("what step is this order on?")
  ✗ Cyclic dependencies can emerge
  ✗ Difficult to debug distributed event chains
  ✗ No single place to view saga progress
```

### Orchestration (Central Coordinator)
```
A dedicated Saga Orchestrator service manages the entire workflow.
Orchestrator tells each service what to do via commands.
Orchestrator tracks state, handles failures, issues compensations.

Order Saga (orchestration):
  [Order Orchestrator] receives "place order" request
  [Order Orchestrator] → sends command "CreateOrder" to Order Service → waits
  [Order Orchestrator] → sends command "ProcessPayment" to Payment Service → waits
  [Order Orchestrator] → sends command "ReserveInventory" to Inventory Service → waits
  If success: [Order Orchestrator] → sends command "ConfirmOrder" to Order Service
  If Step 3 fails: [Order Orchestrator] → sends "RefundPayment" to Payment Service
                                        → sends "CancelOrder" to Order Service

Pros:
  ✓ Clear visibility — orchestrator has full saga state
  ✓ Easy to reason about flow and add compensation logic
  ✓ Easier to debug, monitor, and add observability
  ✓ Handles complex conditional flows (if X, then Y, else Z)

Cons:
  ✗ Orchestrator = additional service + potential SPOF
  ✗ Services more coupled to orchestrator
  ✗ Orchestrator can become a "God service" with too much business logic

When to use:
  Choreography: simple linear flows, many services, loose coupling priority
  Orchestration: complex flows, conditional logic, observability priority
  In practice: large orgs prefer orchestration (easier to operate and debug)
```

---

## 6. Compensating Transactions

```
Key principle: compensating transactions are NOT rollbacks.
               They are forward-moving corrections.

Example: Payment of $100 was made. Saga then fails.
  Wrong (can't do): time-travel rollback the payment
  Right (compensating): issue a $100 refund — a new, forward transaction

Properties of compensating transactions:
  1. Idempotent: safe to run multiple times without double-refunding
  2. Forward-moving: they create new state, not undo old state
  3. Always possible: the system must be designed so compensation is always possible
                      (you can always refund; you can always cancel an order)

Design principle: make every step in a Saga compensatable.
  Reserve inventory:  compensation = unreserve inventory
  Deduct payment:     compensation = issue refund
  Create order:       compensation = cancel order
  Send email:         ??? compensation = "send cancellation email" (notification only)
  
  Notification services are typically "pivot transactions" — once sent, can't un-send.
  Design: notifications happen LAST in the saga (after all risky steps complete).
```

---

## 7. The Outbox Pattern

```
Critical problem: publishing an event AND updating a DB must be atomic.
Without this: system crashes after DB update but before event published →
              saga stuck, downstream never triggered.

Example of the bug:
  Payment Service receives command "ProcessPayment"
  DB: UPDATE balance = balance - 100 WHERE user=alice   ← succeeds
  Kafka: publish "PaymentProcessed" event                ← CRASH HERE
  → alice's balance is deducted but no one knows payment succeeded
  → order never progresses, alice pays but gets nothing

Outbox Pattern solution:
  Within the SAME LOCAL DB TRANSACTION:
    1. UPDATE balance = balance - 100 WHERE user=alice
    2. INSERT INTO outbox (event_type, payload, created_at, sent=false)
         VALUES ('PaymentProcessed', '{...}', NOW(), false)
  Commit atomically.

  Separate "outbox relay" process:
    Poll outbox WHERE sent=false
    Publish each event to Kafka
    Mark as sent=true

Guarantee: if DB transaction commits → event row exists → will be published
           if DB transaction fails → neither update nor event row exist
           "At least once" publishing (may publish twice on retry, but never lost)

Combined with idempotent consumers → exactly-once semantics end-to-end.
```

---

## 8. Idempotency

```
Definition: an operation is idempotent if performing it multiple times
            produces the same result as performing it once.

Why needed in Sagas:
  Network is unreliable → messages may be delivered more than once.
  Kafka at-least-once delivery → consumer may process same event twice.
  Compensating transactions must not double-refund if replayed.

Idempotency key pattern:
  Client sends: { amount: 100, idempotency_key: "order-123-payment" }
  Server checks: SELECT * FROM payments WHERE idempotency_key = 'order-123-payment'
  If exists: return previous result (don't process again)
  If not: process payment, store with idempotency_key

Storage: idempotency key → result, TTL 24 hours (after which client must re-order)
Implementation: idempotency table, or check UNIQUE constraint on idempotency_key column

Stripe's pattern: every write API call includes an Idempotency-Key header.
                  Replaying the same key always returns the same response.
```

---

## 9. BASE vs ACID

```
ACID: Atomic, Consistent, Isolated, Durable
  → Single-node or tightly-coupled distributed transactions
  → Prioritises correctness over availability
  → Examples: PostgreSQL, MySQL, Oracle

BASE: Basically Available, Soft state, Eventually consistent
  → Distributed systems with multiple services
  → Prioritises availability over immediate consistency
  → Examples: DynamoDB, Cassandra, Elasticsearch

The trade-off:
  ACID: "balance is always exactly right, but may be unavailable under failure"
  BASE: "system always accepts writes, balance eventually becomes correct"

Saga pattern implements BASE:
  After payment deducted, order may briefly show "pending" inventory
  Eventually (ms to seconds later) inventory reserved and order confirmed
  User sees eventual consistency — brief window of "soft state"

When ACID is still needed within microservices:
  Each service's local DB should still use ACID transactions
  The cross-service coordination uses Saga (BASE)
  "ACID within, BASE between" — a common and sound architecture
```

---

## 10. Real-World Example: Ride-Hailing Order Saga

```
Saga for "User requests a ride" (Uber-style):

Step 1: Trip Service → create trip (status: REQUESTED) → publish "TripRequested"
Step 2: Driver Service → find + assign nearest driver → publish "DriverAssigned"
Step 3: Payment Service → authorize payment method → publish "PaymentAuthorized"
Step 4: Trip Service → update trip (status: CONFIRMED) → publish "TripConfirmed"
Step 5: Notification Service → notify driver and rider

Compensation scenarios:
  No drivers available (Step 2 fails):
    Compensate Step 1: cancel trip
    Publish "TripCancelled"

  Payment authorization fails (Step 3 fails):
    Compensate Step 2: unassign driver (driver becomes available again)
    Compensate Step 1: cancel trip

  Driver cancels after Step 4:
    New forward saga begins: find replacement driver (Compensate Step 2, then retry Step 2)

Orchestrator tracks: {tripId, currentStep, retries, compensation_stack}
```

---

## 📝 Tasks

### Task 1 — Isolation Level Analysis
For each scenario, identify the isolation problem and the minimum isolation level needed:
1. Banking app: user checks balance while a transfer is in-flight (not yet committed)
2. Ticket booking: two users book the last seat simultaneously
3. Report generation: aggregate over table while rows are being inserted
4. Shopping cart: user sees item count while another user's add-to-cart is processing

### Task 2 — Design a Payment Saga
Design a complete Saga for an e-commerce checkout:
Services: Order, Payment (Stripe), Inventory, Shipping, Notification
1. Draw the happy path — all steps succeed
2. Draw the compensation path — inventory unavailable at step 3
3. Which approach: choreography or orchestration? Justify.
4. Design the outbox table schema for the Payment Service
5. Make the "DeductPayment" step idempotent — what's the idempotency key?

### Task 3 — 2PC vs Saga Trade-offs
A bank needs to transfer money between two accounts in different microservices:
1. Design using 2PC — what happens if coordinator crashes after PREPARE?
2. Design using Saga — what's the compensation for "debit account A"?
3. For this specific use case (money transfer), which do you recommend and why?
4. How does the Outbox pattern prevent double-debit in the Saga approach?

### ⭐ Task 4 — Design "Place Order" for an E-Commerce System
Full system design covering:
- 5-service saga: Order, Payment, Inventory, Shipping, Notification
- Choose orchestration or choreography
- Complete state machine for the order
- Outbox + Kafka for reliable event publishing
- Idempotency keys throughout
- Failure scenarios: network partition, service crash mid-saga, duplicate events
- How does the orchestrator itself achieve high availability?

---

## ✅ Completion Checklist

- [ ] ACID: all 4 properties with concrete examples
- [ ] 4 isolation anomalies: dirty read, non-repeatable read, phantom, lost update
- [ ] 4 isolation levels: Read Uncommitted → Serializable, which prevents which
- [ ] Distributed transaction problem: no single transaction spans multiple DBs
- [ ] 2PC: prepare phase + commit phase, and the blocking failure mode
- [ ] 2PC problems: coordinator SPOF, locks held between phases, network overhead
- [ ] Saga pattern: local transactions + compensating transactions
- [ ] Choreography: event-driven, no coordinator, loose coupling
- [ ] Orchestration: central coordinator, clearer state, conditional logic
- [ ] When to use choreography vs orchestration
- [ ] Compensating transactions: forward-moving, idempotent, always possible
- [ ] Outbox pattern: DB + event in single local transaction, relay publishes
- [ ] Idempotency key pattern: check before processing, store result
- [ ] BASE vs ACID: "ACID within, BASE between" for microservices
- [ ] Completed Task 1 — isolation level analysis
- [ ] Completed Task 2 — payment saga design
- [ ] Completed Task 3 — 2PC vs Saga trade-offs
- [ ] Completed Task 4 — full "place order" saga design

**→ Next: Module B12 — System Design Interview Framework & Mock Interviews**
