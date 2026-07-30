---
layout: learning
title: "Module B11: ACID, Distributed Transactions & Saga"
permalink: /learning/system-design/hld/module-b11-distributed-tx/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-b11.css" | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Crimson+Pro:wght@300;400;600&display=swap" rel="stylesheet">

<div class="sd-module-b11">
<header>
  <div class="hdr-rule"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B11 · WEEK 21</span>
    <span>ACID · 2PC · SAGA · OUTBOX · IDEMPOTENCY</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">Distributed Systems Consistency · Saga Pattern · Compensation</div>
      <h1><span class="acc">ACID</span>,<br>Distributed<br>Transactions<br>& <span class="acc">Saga</span></h1>
      <div class="hdr-sub">ISOLATION LEVELS · 2-PHASE COMMIT · SAGA PATTERN<br>CHOREOGRAPHY vs ORCHESTRATION · OUTBOX · IDEMPOTENCY</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">4</div><div class="hs-l">ACID PROPERTIES</div></div>
      <div class="hs"><div class="hs-v">2PC</div><div class="hs-l">CLASSIC SOLUTION</div></div>
      <div class="hs"><div class="hs-v">Saga</div><div class="hs-l">MODERN SOLUTION</div></div>
      <div class="hs"><div class="hs-v">B11</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--gold)">ACID</div>
    <div class="tg" style="color:var(--bri)">Isolation Levels</div>
    <div class="tg" style="color:var(--red)">2PC Problems</div>
    <div class="tg" style="color:var(--grn)">Saga Pattern</div>
    <div class="tg" style="color:var(--cya)">Choreography</div>
    <div class="tg" style="color:var(--pur)">Orchestration</div>
    <div class="tg" style="color:var(--gold)">Outbox Pattern</div>
    <div class="tg" style="color:var(--bri)">Idempotency</div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="mb11_show('acid',this)">ACID</div>
  <div class="nt" onclick="mb11_show('isolation',this)">Isolation Levels</div>
  <div class="nt" onclick="mb11_show('problem',this)">The Problem</div>
  <div class="nt" onclick="mb11_show('twopc',this)">2-Phase Commit</div>
  <div class="nt" onclick="mb11_show('saga',this)">Saga Pattern</div>
  <div class="nt" onclick="mb11_show('choreorch',this)">Choreo vs Orch</div>
  <div class="nt" onclick="mb11_show('compensation',this)">Compensation</div>
  <div class="nt" onclick="mb11_show('outbox',this)">Outbox Pattern</div>
  <div class="nt" onclick="mb11_show('idempotency',this)">Idempotency</div>
  <div class="nt" onclick="mb11_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb11_show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- ACID -->
<div class="view active" id="view-acid">
  <div class="sh">ACID Properties</div>
  <div class="sr">The four guarantees of a reliable database transaction</div>
  <div class="acid-grid">
    <div class="ac">
      <div class="ac-letter">A</div>
      <div class="ac-name">ATOMICITY</div>
      <div class="ac-body">All operations succeed together, or all fail together. Money cannot leave account A without arriving at account B.</div>
      <div class="ac-impl">Mechanism:<br>Write-ahead log (WAL)<br>Rollback on failure</div>
    </div>
    <div class="ac">
      <div class="ac-letter">C</div>
      <div class="ac-name">CONSISTENCY</div>
      <div class="ac-body">Every transaction takes the DB from one valid state to another. Constraints and rules are never violated during a transaction.</div>
      <div class="ac-impl">Mechanism:<br>CHECK constraints<br>Foreign key rules<br>Application logic</div>
    </div>
    <div class="ac">
      <div class="ac-letter">I</div>
      <div class="ac-name">ISOLATION</div>
      <div class="ac-body">Concurrent transactions don't see each other's in-flight changes. Each transaction sees a consistent snapshot.</div>
      <div class="ac-impl">Mechanism:<br>MVCC (Postgres)<br>Locking (MySQL)<br>See: isolation levels</div>
    </div>
    <div class="ac">
      <div class="ac-letter">D</div>
      <div class="ac-name">DURABILITY</div>
      <div class="ac-body">Committed data survives crashes. Once COMMIT returns, it's on disk. Server crash immediately after cannot lose the commit.</div>
      <div class="ac-impl">Mechanism:<br>fsync to WAL<br>Battery-backed cache<br>Replication</div>
    </div>
  </div>
  <div class="al gld"><em>The one that matters most in interviews:</em> Isolation — specifically the trade-offs between isolation levels. Most bugs in distributed systems come from incorrect assumptions about isolation, not from atomicity or durability failures.</div>
</div>

<!-- ISOLATION -->
<div class="view" id="view-isolation">
  <div class="sh">Isolation Levels</div>
  <div class="sr">Four anomalies, four levels — each level prevents a subset of anomalies</div>
  <div class="cb"><div class="cb-top">Four isolation anomalies — know these cold<span class="cb-l">CONCURRENCY BUGS</span></div>
<pre class="c"><span class="cm">// 1. DIRTY READ: read uncommitted data that later rolls back</span>
T1: UPDATE balance = 50 WHERE user='alice'  <span class="cm">(not yet committed)</span>
T2: SELECT balance FROM users WHERE user='alice'  → <span class="er">50</span>  <span class="cm">(dirty!)</span>
T1: ROLLBACK  → balance never changed to 50
T2 read data that never existed.

<span class="cm">// 2. NON-REPEATABLE READ: same row returns different values in same transaction</span>
T1: SELECT balance FROM users WHERE user='alice'  → <span class="go">100</span>
T2: UPDATE balance = 200 WHERE user='alice'; COMMIT
T1: SELECT balance FROM users WHERE user='alice'  → <span class="er">200</span>  <span class="cm">(changed!)</span>

<span class="cm">// 3. PHANTOM READ: new rows appear in a repeated range query</span>
T1: SELECT COUNT(*) FROM orders WHERE status='pending'  → <span class="go">5</span>
T2: INSERT INTO orders (status) VALUES ('pending'); COMMIT
T1: SELECT COUNT(*) FROM orders WHERE status='pending'  → <span class="er">6</span>  <span class="cm">(phantom!)</span>

<span class="cm">// 4. LOST UPDATE: two transactions overwrite each other's changes</span>
T1: READ balance = 100
T2: READ balance = 100
T1: WRITE balance = 110  <span class="cm">(+10)</span>
T2: WRITE balance = 120  <span class="cm">(+20, but only saw original 100 — lost T1's update!)</span>
<span class="er">// Should be 130. T2 overwrote T1. 10 dollars vanished.</span></pre>
  </div>
  <table class="iso-table">
    <thead><tr><th>ISOLATION LEVEL</th><th>DIRTY READ</th><th>NON-REPEAT READ</th><th>PHANTOM</th><th>LOST UPDATE</th><th>DEFAULT FOR</th></tr></thead>
    <tbody>
      <tr><td>Read Uncommitted</td><td class="er-cell">✗ allowed</td><td class="er-cell">✗ allowed</td><td class="er-cell">✗ allowed</td><td class="er-cell">✗ allowed</td><td>Rarely used</td></tr>
      <tr><td>Read Committed</td><td class="ok-cell">✓ prevented</td><td class="er-cell">✗ allowed</td><td class="er-cell">✗ allowed</td><td class="er-cell">✗ allowed</td><td>PostgreSQL</td></tr>
      <tr><td>Repeatable Read</td><td class="ok-cell">✓ prevented</td><td class="ok-cell">✓ prevented</td><td class="er-cell">✗ allowed</td><td class="ok-cell">✓ prevented</td><td>MySQL InnoDB</td></tr>
      <tr><td>Serializable</td><td class="ok-cell">✓ prevented</td><td class="ok-cell">✓ prevented</td><td class="ok-cell">✓ prevented</td><td class="ok-cell">✓ prevented</td><td>Max consistency</td></tr>
    </tbody>
  </table>
</div>

<!-- PROBLEM -->
<div class="view" id="view-problem">
  <div class="sh">The Distributed Transaction Problem</div>
  <div class="sr">A single business operation spans multiple databases — no ACID across them</div>
  <div class="cb"><div class="cb-top">Order placement: 4 services, 4 databases, 1 business operation<span class="cb-l">THE PROBLEM</span></div>
<pre class="c"><span class="cm">// A customer places an order. This requires:</span>
<span class="cm">// 1. Order Service     → INSERT order  INTO orders_db</span>
<span class="cm">// 2. Payment Service   → UPDATE balance IN payment_db</span>
<span class="cm">// 3. Inventory Service → UPDATE stock   IN inventory_db</span>
<span class="cm">// 4. Notification      → send email     via external SMTP</span>

<span class="cm">// These are FOUR SEPARATE DATABASES. There is NO single transaction spanning them.</span>
<span class="cm">// What happens if Step 3 fails after Steps 1 and 2 succeed?</span>

BEGIN TRANSACTION on orders_db:
  INSERT INTO orders ...    <span class="ok">✓ committed</span>
  
BEGIN TRANSACTION on payment_db:
  UPDATE balance - $100 ... <span class="ok">✓ committed</span>  <span class="cm">← alice is charged</span>
  
BEGIN TRANSACTION on inventory_db:
  UPDATE stock - 1 ...      <span class="er">✗ FAILS</span>  <span class="cm">← item out of stock!</span>

<span class="er">// Alice was charged $100 but cannot receive her item.</span>
<span class="er">// Order DB shows order created. Payment DB shows deduction. Inventory unchanged.</span>
<span class="er">// System is in an INCONSISTENT state across services.</span></pre>
  </div>
  <div class="al red"><em>The fundamental issue:</em> You cannot have a single ACID transaction that spans two separate database servers. Network partitions make it impossible to guarantee atomicity across DBs. Every distributed system must choose: 2-Phase Commit (consistency, but blocks), or Saga (eventual consistency, but available).</div>
</div>

<!-- 2PC -->
<div class="view" id="view-twopc">
  <div class="sh">Two-Phase Commit (2PC)</div>
  <div class="sr">Classic distributed transaction — correct but fragile</div>
  <div class="twopc">
    <div class="tp-label">// 2PC HAPPY PATH</div>
    <div class="tp-phase">
      <div class="tp-ph"><span style="color:var(--gold)">Phase 1 — PREPARE</span></div>
      <div class="tp-row"><div class="tp-actor">Coordinator</div><div class="tp-arrow">──PREPARE──→</div><div class="tp-msg">Order Service, Payment Service, Inventory Service</div></div>
      <div class="tp-row"><div class="tp-actor">Each Participant</div><div class="tp-arrow"></div><div class="tp-msg">Executes transaction locally (does NOT commit). Writes PREPARE to WAL. Replies READY.</div></div>
      <div class="tp-row"><div class="tp-actor">Coordinator</div><div class="tp-arrow">←──READY───</div><div class="tp-msg">All 3 reply READY → proceed to Phase 2</div></div>
    </div>
    <div class="tp-phase">
      <div class="tp-ph"><span style="color:var(--grn)">Phase 2 — COMMIT</span></div>
      <div class="tp-row"><div class="tp-actor">Coordinator</div><div class="tp-arrow">──COMMIT──→</div><div class="tp-msg">All participants</div></div>
      <div class="tp-row"><div class="tp-actor">Each Participant</div><div class="tp-arrow"></div><div class="tp-msg">Commits local transaction. Releases locks. Replies DONE.</div></div>
    </div>
  </div>
  <div class="twopc">
    <div class="tp-label" style="color:var(--red)">// 2PC FAILURE — COORDINATOR CRASHES AFTER PREPARE</div>
    <div class="tp-row"><div class="tp-actor">Coordinator</div><div class="tp-arrow">──PREPARE──→</div><div class="tp-msg">All participants reply READY. Coordinator writes COMMIT decision to log.</div></div>
    <div class="tp-row"><div class="tp-actor"></div><div class="tp-arrow"></div><div class="tp-msg tp-note">💥 COORDINATOR CRASHES before sending COMMIT</div></div>
    <div class="tp-row"><div class="tp-actor">Participants</div><div class="tp-arrow"></div><div class="tp-msg tp-note">Stuck in PREPARED state — holding locks, cannot commit OR rollback.</div></div>
    <div class="tp-row"><div class="tp-actor">System</div><div class="tp-arrow"></div><div class="tp-msg tp-note">FROZEN until coordinator recovers. All participants block indefinitely.</div></div>
  </div>
  <div class="al red"><em>2PC's fatal flaw:</em> It is a blocking protocol. If the coordinator crashes after sending PREPARE but before sending COMMIT, all participants are in an "uncertain" state — they hold locks and cannot proceed without hearing from the coordinator. Recovery requires coordinator restart, which may take minutes. During that time, the system is frozen.</div>
</div>

<!-- SAGA -->
<div class="view" id="view-saga">
  <div class="sh">The Saga Pattern</div>
  <div class="sr">Local transactions + compensating transactions — no distributed locks</div>
  <div class="saga-flow">
    <div class="sf-label" style="color:var(--grn)">// SAGA HAPPY PATH — Order placement</div>
    <div class="sf-step">
      <div class="sf-num" style="color:var(--grn)">1</div>
      <div class="sf-svc" style="color:var(--gold)">Order Service</div>
      <div class="sf-action">Create order (status: PENDING)<div class="sf-event" style="color:var(--grn)">→ publishes "OrderCreated"</div></div>
    </div>
    <div class="sf-step">
      <div class="sf-num" style="color:var(--grn)">2</div>
      <div class="sf-svc" style="color:var(--gold)">Payment Service</div>
      <div class="sf-action">Deduct $100 from alice<div class="sf-event" style="color:var(--grn)">→ publishes "PaymentProcessed"</div></div>
    </div>
    <div class="sf-step">
      <div class="sf-num" style="color:var(--grn)">3</div>
      <div class="sf-svc" style="color:var(--gold)">Inventory Service</div>
      <div class="sf-action">Reserve item (stock - 1)<div class="sf-event" style="color:var(--grn)">→ publishes "InventoryReserved"</div></div>
    </div>
    <div class="sf-step">
      <div class="sf-num" style="color:var(--grn)">4</div>
      <div class="sf-svc" style="color:var(--gold)">Order Service</div>
      <div class="sf-action">Update order (status: CONFIRMED)<div class="sf-event" style="color:var(--grn)">→ publishes "OrderConfirmed"</div></div>
    </div>
    <div class="sf-step">
      <div class="sf-num" style="color:var(--grn)">5</div>
      <div class="sf-svc" style="color:var(--gold)">Notification</div>
      <div class="sf-action">Send confirmation email<div class="sf-event" style="color:var(--grn)">→ done (pivot transaction)</div></div>
    </div>
  </div>
  <div class="saga-flow">
    <div class="sf-label" style="color:var(--red)">// SAGA COMPENSATION PATH — Inventory fails at step 3</div>
    <div class="sf-step"><div class="sf-num" style="color:var(--muted)">1✓</div><div class="sf-svc" style="color:var(--muted)">Order Service</div><div class="sf-action" style="color:var(--muted)">Order created — done</div></div>
    <div class="sf-step"><div class="sf-num" style="color:var(--muted)">2✓</div><div class="sf-svc" style="color:var(--muted)">Payment Service</div><div class="sf-action" style="color:var(--muted)">Payment deducted — done</div></div>
    <div class="sf-step"><div class="sf-num" style="color:var(--red)">3✗</div><div class="sf-svc" style="color:var(--red)">Inventory Service</div><div class="sf-action"><span style="color:var(--red)">FAILS — item out of stock</span><div class="sf-event" style="color:var(--red)">→ publishes "InventoryFailed"</div></div></div>
    <div class="sf-step comp-marker"><div class="sf-num" style="color:var(--red)">C2</div><div class="sf-svc" style="color:var(--red)">Payment Service</div><div class="sf-action"><span style="color:var(--red)">COMPENSATE: refund $100 to alice</span><div class="sf-event" style="color:var(--red)">→ publishes "PaymentRefunded"</div></div></div>
    <div class="sf-step comp-marker"><div class="sf-num" style="color:var(--red)">C1</div><div class="sf-svc" style="color:var(--red)">Order Service</div><div class="sf-action"><span style="color:var(--red)">COMPENSATE: cancel order (status: CANCELLED)</span><div class="sf-event" style="color:var(--red)">→ publishes "OrderCancelled"</div></div></div>
  </div>
</div>

<!-- CHOREO vs ORCH -->
<div class="view" id="view-choreorch">
  <div class="sh">Choreography vs Orchestration</div>
  <div class="sr">Two ways to coordinate a Saga — choose based on complexity and observability needs</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--cya);padding:14px">
      <div style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:700;color:var(--white);margin-bottom:6px">Choreography</div>
      <div style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted);letter-spacing:1px;margin-bottom:10px">EVENT-DRIVEN · NO COORDINATOR</div>
      <div style="font-size:12px;color:var(--text);line-height:1.7;margin-bottom:8px">Services react to events independently. Each service subscribes to relevant events, performs its action, publishes the next event. No central conductor.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9px;line-height:1.8">
        <span style="color:var(--grn)">✓ Loose coupling — services don't know each other</span><br>
        <span style="color:var(--grn)">✓ No SPOF coordinator service</span><br>
        <span style="color:var(--grn)">✓ Easy to add new steps</span><br>
        <span style="color:var(--red)">✗ No single view of saga state</span><br>
        <span style="color:var(--red)">✗ Hard to debug distributed event chains</span><br>
        <span style="color:var(--red)">✗ Cyclic dependencies can emerge</span>
      </div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--pur);padding:14px">
      <div style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:700;color:var(--white);margin-bottom:6px">Orchestration ★</div>
      <div style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted);letter-spacing:1px;margin-bottom:10px">CENTRAL COORDINATOR · COMMAND-DRIVEN</div>
      <div style="font-size:12px;color:var(--text);line-height:1.7;margin-bottom:8px">A dedicated Saga Orchestrator commands each service step-by-step. Orchestrator tracks state, handles failures, issues compensations. One service to reason about.</div>
      <div style="font-family:'Courier Prime',monospace;font-size:9px;line-height:1.8">
        <span style="color:var(--grn)">✓ Clear saga state in one place</span><br>
        <span style="color:var(--grn)">✓ Easy to debug and add observability</span><br>
        <span style="color:var(--grn)">✓ Handles complex conditional flows</span><br>
        <span style="color:var(--red)">✗ Orchestrator is potential SPOF</span><br>
        <span style="color:var(--red)">✗ More coupling to orchestrator</span><br>
        <span style="color:var(--red)">✗ Can become a God service</span>
      </div>
    </div>
  </div>
  <div class="al gld"><em>Interview recommendation:</em> "For simple linear flows with few services, choreography is elegant. For complex conditional flows or anything requiring strong observability (e.g., payment processing), I'd use orchestration — the ability to answer 'what state is this saga in?' is invaluable in production."</div>
</div>

<!-- COMPENSATION -->
<div class="view" id="view-compensation">
  <div class="sh">Compensating Transactions</div>
  <div class="sr">Forward-moving corrections — not rollbacks</div>
  <div class="al gld"><em>Key insight:</em> Compensating transactions are NOT rollbacks. You cannot un-send an email or un-charge a credit card. Compensation is a new, forward-moving transaction that corrects the previous one (refund, cancel, unreserve).</div>
  <div class="cb"><div class="cb-top">Compensation design — every step must have a compensating step<span class="cb-l">DESIGN</span></div>
<pre class="c"><span class="cm">// For every Saga step, design its compensation BEFORE building the step:</span>

Step 1: <span class="go">Create Order</span>        → Compensation: <span class="er">Cancel Order</span>
Step 2: <span class="go">Deduct Payment</span>     → Compensation: <span class="er">Issue Refund</span>
Step 3: <span class="go">Reserve Inventory</span>  → Compensation: <span class="er">Release Reservation</span>
Step 4: <span class="go">Book Shipping Slot</span> → Compensation: <span class="er">Cancel Booking</span>
Step 5: <span class="go">Send Email</span>         → Compensation: <span class="er">Send Cancellation Email</span>
<span class="cm">// (cannot un-send; notify user of cancellation instead)</span>

<span class="cm">// Pivot transaction: the step after which compensation is impossible/impractical</span>
<span class="cm">// Design: put pivot transaction AS LATE AS POSSIBLE in the saga</span>
<span class="cm">// Notifications, external API calls = typically pivot transactions</span>

<span class="cm">// Idempotency requirement:</span>
<span class="cm">// Compensation may run multiple times (network retry, at-least-once delivery)</span>
<span class="cm">// REFUND must be idempotent: cannot refund twice for one order</span>
<span class="cm">// Check: INSERT INTO refunds (order_id, amount) ON CONFLICT DO NOTHING</span>
<span class="cm">// Or: idempotency key = order_id → check before processing</span></pre>
  </div>
</div>

<!-- OUTBOX -->
<div class="view" id="view-outbox">
  <div class="sh">The Outbox Pattern</div>
  <div class="sr">Atomic DB update + event publication — without distributed transactions</div>
  <div class="cb"><div class="cb-top">The bug without outbox — dual write problem<span class="cb-l">BUG</span></div>
<pre class="c"><span class="cm">// Payment Service receives "ProcessPayment" command</span>

<span class="cm">// Step 1: update DB</span>
UPDATE accounts SET balance = balance - 100 WHERE user='alice';
COMMIT;  <span class="ok">← succeeds</span>

<span class="cm">// 💥 SERVER CRASHES HERE</span>

<span class="cm">// Step 2: publish event</span>
kafka.publish("PaymentProcessed", {...});  <span class="er">← NEVER RUNS</span>

<span class="cm">// Result: alice's balance is deducted, but no "PaymentProcessed" event was published.</span>
<span class="cm">// The saga is stuck. Alice pays but gets nothing.</span>
<span class="cm">// Dual write problem: two separate systems (DB + Kafka) cannot be updated atomically.</span></pre>
  </div>
  <div class="cb"><div class="cb-top">Outbox pattern — atomic DB + event in single local transaction<span class="cb-l">SOLUTION</span></div>
<pre class="c"><span class="cm">// Within a SINGLE LOCAL DB TRANSACTION:</span>
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 100 WHERE user='alice';
  INSERT INTO outbox (id, event_type, payload, sent, created_at)
  VALUES (uuid(), <span class="str">'PaymentProcessed'</span>, <span class="str">'{"order":"123","amount":100}'</span>, false, NOW());
COMMIT;  <span class="cm">← both update AND outbox row are atomic</span>

<span class="cm">// Separate "Outbox Relay" process (runs continuously):</span>
<span class="kw">while</span> (true) {
  rows = db.<span class="fn">query</span>(<span class="str">"SELECT * FROM outbox WHERE sent = false ORDER BY created_at LIMIT 100"</span>)
  <span class="kw">for</span> (row of rows) {
    kafka.<span class="fn">publish</span>(row.event_type, row.payload)  <span class="cm">// at-least-once</span>
    db.<span class="fn">update</span>(<span class="str">"UPDATE outbox SET sent=true WHERE id=?"</span>, row.id)
  }
  sleep(100ms)
}

<span class="cm">// Guarantee: if DB committed → event row exists → relay will publish it</span>
<span class="cm">// Relay may publish twice (retry on crash) → consumer must be idempotent</span>
<span class="cm">// Alternative: CDC (Debezium) watches DB transaction log → publishes to Kafka</span></pre>
  </div>
  <div class="outbox-box">
    <div class="ob-hdr"><span>TABLE: outbox</span><span style="color:var(--gold)">per-service, same DB as business tables</span></div>
    <div class="ob-body">
      <div class="ob-row" style="border-bottom:1px solid var(--bord2);padding-bottom:4px;margin-bottom:4px">
        <span style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted)">COLUMN</span>
        <span style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted)">TYPE</span>
        <span style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted)">PURPOSE</span>
      </div>
      <div class="ob-row"><div class="ob-col">id</div><div class="ob-type">UUID</div><div class="ob-note">Unique event ID — used for idempotency on consumer side</div></div>
      <div class="ob-row"><div class="ob-col">event_type</div><div class="ob-type">VARCHAR</div><div class="ob-note">'PaymentProcessed', 'OrderCreated', etc.</div></div>
      <div class="ob-row"><div class="ob-col">payload</div><div class="ob-type">JSONB</div><div class="ob-note">Full event data to publish to Kafka</div></div>
      <div class="ob-row"><div class="ob-col">sent</div><div class="ob-type">BOOLEAN</div><div class="ob-note">false = pending publication, true = published</div></div>
      <div class="ob-row"><div class="ob-col">created_at</div><div class="ob-type">TIMESTAMP</div><div class="ob-note">Ordering — relay publishes in creation order</div></div>
      <div class="ob-row"><div class="ob-col">sent_at</div><div class="ob-type">TIMESTAMP</div><div class="ob-note">NULL until published — monitoring lag</div></div>
    </div>
  </div>
</div>

<!-- IDEMPOTENCY -->
<div class="view" id="view-idempotency">
  <div class="sh">Idempotency</div>
  <div class="sr">Performing an operation multiple times = same result as once</div>
  <div class="cb"><div class="cb-top">Idempotency key pattern — Stripe's approach<span class="cb-l">PATTERN</span></div>
<pre class="c"><span class="cm">// Client sends payment with idempotency key</span>
POST /payments
Headers: Idempotency-Key: <span class="str">"order-123-payment-attempt-1"</span>
Body:    <span class="str">{"amount": 100, "currency": "USD", "user": "alice"}</span>

<span class="cm">// Server logic:</span>
<span class="kw">function</span> <span class="fn">processPayment</span>(idempotencyKey, amount, user) {
  <span class="cm">// Check if already processed</span>
  existing = db.<span class="fn">query</span>(<span class="str">"SELECT result FROM idempotency_cache WHERE key = ?"</span>, idempotencyKey)
  <span class="kw">if</span> (existing) <span class="kw">return</span> existing.result  <span class="cm">// return same result, don't charge again</span>

  <span class="cm">// Process payment</span>
  result = stripe.<span class="fn">charge</span>(amount, user)

  <span class="cm">// Store result with key (within same transaction as the charge)</span>
  db.<span class="fn">insert</span>(<span class="str">"INSERT INTO idempotency_cache (key, result, expires_at) VALUES (?,?,?)"</span>,
    idempotencyKey, result, now + 24h)

  <span class="kw">return</span> result
}

<span class="cm">// If client retries (network timeout, didn't receive response):</span>
<span class="cm">// POST /payments with same Idempotency-Key → returns cached result, no double charge</span>

<span class="cm">// Idempotency key design:</span>
<span class="cm">// order_id + step_name = "order-123-payment"  (scoped to specific operation)</span>
<span class="cm">// UUID per attempt = allows retry after timeout, prevents replay after success</span>
<span class="cm">// TTL: 24 hours (after which key expires; client should create new order)</span></pre>
  </div>
  <div class="al gld"><em>Why idempotency is non-negotiable in Sagas:</em> Kafka delivers at-least-once. Your outbox relay may publish the same event twice. Network retries happen. Every step in a Saga must be idempotent — running it twice must produce the same outcome as running it once. This is not optional.</div>
</div>

<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="mb11_tt(this)"><div class="t-num">I</div><div class="t-lbl">Isolation Level Analysis</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>For each scenario: name the isolation anomaly and the minimum isolation level to prevent it.</p>
        <ol>
          <li>Banking app: user checks balance while an incoming transfer is in-flight (UPDATE not yet committed)</li>
          <li>Ticket booking: two users simultaneously book the last seat — both see 1 seat available</li>
          <li>Report: SELECT SUM(revenue) while revenue rows are being inserted by other transactions</li>
          <li>Two users both read a stock price, both decide to buy, both increment a counter — final count is wrong</li>
        </ol>
        <p style="margin-top:8px">For each: explain whether you'd use MVCC (snapshot) isolation or pessimistic locking, and why.</p>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb11_tt(this)"><div class="t-num">II</div><div class="t-lbl">Design a Payment Saga</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>E-commerce checkout: Order → Payment (Stripe) → Inventory → Shipping → Notification</p>
        <ol>
          <li>Draw the happy path event/command sequence</li>
          <li>Draw the compensation path when Inventory fails at step 3</li>
          <li>Choose choreography or orchestration for this scenario — justify your choice</li>
          <li>Design the outbox table schema for the Payment Service</li>
          <li>Design the idempotency key for the "DeductPayment" step. What makes a good key?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb11_tt(this)"><div class="t-num">III</div><div class="t-lbl">2PC vs Saga: Money Transfer</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Design a bank transfer ($100 from Alice to Bob) using 2PC. What are the 4 network roundtrips?</li>
          <li>What happens if the coordinator crashes after sending PREPARE but before COMMIT? Walk through exactly.</li>
          <li>Design the same transfer as a Saga. What is the compensating transaction for "debit Alice"?</li>
          <li>During the Saga, there's a brief window where Alice has been debited but Bob hasn't been credited. How do you handle this in the UI?</li>
          <li>For money transfer specifically — do you recommend 2PC or Saga? Justify for this exact use case.</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--gold)">
      <div class="task-hd" onclick="mb11_tt(this)"><div class="t-num" style="color:var(--gold)">★</div><div class="t-lbl">Full "Place Order" Saga Design</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Design the complete "Place Order" saga for an e-commerce platform. 5 services: Order, Payment, Inventory, Shipping, Notification.</p>
        <ol>
          <li>Choose orchestration or choreography. Draw the full state machine for the order entity.</li>
          <li>Design the Saga Orchestrator's state table schema (how does it track saga progress?)</li>
          <li>Outbox + Kafka: show how Payment Service publishes events atomically with DB updates.</li>
          <li>Idempotency throughout: design keys for each step. What happens if PaymentService receives the same "ProcessPayment" command twice?</li>
          <li>Failure scenarios: <br>
            a) Payment network timeout (client doesn't know if charge succeeded)<br>
            b) InventoryService crashes mid-reservation<br>
            c) Orchestrator itself crashes with order in step 3
          </li>
          <li>How do you make the Orchestrator itself highly available?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 18 completed</span><span style="font-family:'Courier Prime',monospace">MODULE B11 · ACID & SAGA</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">ACID: all 4 properties with concrete examples</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">4 isolation anomalies: dirty read, non-repeatable, phantom, lost update</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Isolation levels: Read Committed (PG default), Repeatable Read (MySQL default)</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Distributed transaction problem: no single ACID transaction across DBs</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">2PC: prepare phase + commit phase — correct but blocking</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">2PC fatal flaw: coordinator crash after PREPARE = participants frozen</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Saga pattern: local transactions + events/commands + compensation</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Saga happy path and compensation path — can draw both</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Choreography: event-driven, no coordinator, loose coupling</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Orchestration: central coordinator, clear state, conditional logic</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Compensation: forward-moving (refund), not rollback — always idempotent</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Pivot transaction: point of no return — place notifications last</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Outbox pattern: DB update + event in same local transaction</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Outbox relay: polls outbox, publishes to Kafka, marks sent — at-least-once</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Idempotency key: check before processing, store result, TTL 24h</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">BASE vs ACID: "ACID within services, BASE between services"</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks I–III: isolation analysis, payment saga, 2PC vs Saga</div></div>
    <div class="chk" onclick="mb11_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task IV (capstone): full Place Order saga design</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--gold)">
    <div style="font-family:'Courier Prime',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">§ NEXT MODULE</div>
    <div style="font-family:'Cormorant Garamond',serif;font-size:26px;font-weight:700;font-style:italic;color:var(--white);margin-bottom:6px">B12 — System Design Interview Framework & Mock Interviews</div>
    <div style="font-family:'Courier Prime',monospace;font-size:9px;color:var(--muted);line-height:2">
      The 7-step framework in detail · Time allocation (45 min)<br>
      Back-of-envelope estimation practice · 6 full mock interviews<br>
      Common mistakes · What interviewers actually look for
    </div>
  </div>
</div>

</div>

<!-- Bottom Navigation -->
<div class="mb11-bottom-nav">
  <a href="/learning/system-design/hld/module-b10-consistent-hashing/" class="mb11-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb11-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    PREVIOUS: B10
  </a>
  <a href="/learning/system-design/hld/module-b11-notes/" class="mb11-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb11-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb11-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb11-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b12-interview-framework/" class="mb11-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    NEXT: B12
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb11-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>

</div>
<script src="{{ "/assets/js/sd-module-b11.js" | relative_url }}"></script>
