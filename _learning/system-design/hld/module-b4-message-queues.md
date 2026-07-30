---
layout: default
title: "Module B4 — Message Queues"
permalink: /learning/system-design/hld/module-b4-message-queues/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-b4.css" | relative_url }}">

<div class="mb4-page">
  <header class="mb4-header">
    <div class="mb4-hdr-top">
      <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B4 · WEEK 14</span>
      <span>HIGH-LEVEL DESIGN · MESSAGE QUEUES</span>
    </div>
    <div class="mb4-hdr-body">
      <div>
        <div class="mb4-hdr-kicker">// ASYNC MESSAGING · EVENT STREAMING · DECOUPLING</div>
        <h1>MSG<br><span class="mb4-acc">QUEUES</span></h1>
        <div class="mb4-hdr-sub">KAFKA · RABBITMQ · DELIVERY SEMANTICS<br>CONSUMER GROUPS · PARTITIONS · EXACTLY-ONCE</div>
      </div>
      <div class="mb4-hdr-stats">
        <div class="mb4-hs"><div class="mb4-hs-v">3</div><div class="mb4-hs-l">SEMANTICS</div></div>
        <div class="mb4-hs"><div class="mb4-hs-v">∞</div><div class="mb4-hs-l">REPLAY</div></div>
        <div class="mb4-hs"><div class="mb4-hs-v">16K</div><div class="mb4-hs-l">PARTITIONS MAX</div></div>
        <div class="mb4-hs"><div class="mb4-hs-v">B4</div><div class="mb4-hs-l">MODULE</div></div>
      </div>
    </div>
    <div class="mb4-topic-row">
      <div class="mb4-tp" style="color:var(--mag)">Kafka Arch</div>
      <div class="mb4-tp" style="color:var(--grn)">Consumer Groups</div>
      <div class="mb4-tp" style="color:var(--yel)">Delivery Semantics</div>
      <div class="mb4-tp" style="color:var(--blu)">Exactly-Once</div>
      <div class="mb4-tp" style="color:var(--orange)">Kafka vs Rabbit</div>
      <div class="mb4-tp" style="color:var(--mag)">Patterns</div>
      <div class="mb4-tp" style="color:var(--grn)">Config</div>
    </div>
  </header>

  <nav class="mb4-nav">
    <div class="mb4-nt active" onclick="mb4Show('why',this)">Why MQ</div>
    <div class="mb4-nt" onclick="mb4Show('kafka',this)">Kafka Arch</div>
    <div class="mb4-nt" onclick="mb4Show('semantics',this)">Delivery Semantics</div>
    <div class="mb4-nt" onclick="mb4Show('compare',this)">Kafka vs RabbitMQ</div>
    <div class="mb4-nt" onclick="mb4Show('patterns',this)">Patterns</div>
    <div class="mb4-nt" onclick="mb4Show('config',this)">Config Cheatsheet</div>
    <div class="mb4-nt" onclick="mb4Show('tasks',this)">Tasks</div>
    <div class="mb4-nt" onclick="mb4Show('checklist',this)">Checklist</div>
  </nav>

  <div class="mb4-content">
    
    <!-- WHY -->
    <div class="mb4-view active" id="view-why">
      <div class="mb4-sh">Why Message Queues?</div>
      <div class="mb4-sr">The six problems a message queue solves — in every distributed system</div>
      <div class="mb4-cb"><div class="mb4-cb-top">Core value proposition<span class="mb4-cb-l">CONCEPT</span></div>
<pre class="mb4-c"><span class="mb4-cm">// WITHOUT message queue: tight coupling, brittle</span>
[Order Service] <span class="mb4-er">──sync──→</span> [Inventory Service]  <span class="mb4-cm">// What if inventory is down?</span>
[Order Service] <span class="mb4-er">──sync──→</span> [Email Service]      <span class="mb4-cm">// What if email is slow (2s)?</span>
[Order Service] <span class="mb4-er">──sync──→</span> [Analytics Service]  <span class="mb4-cm">// User waits for all 3!</span>

<span class="mb4-cm">// WITH message queue: decoupled, resilient, fast</span>
[Order Service] <span class="mb4-ok">──→ [Topic: order-placed] ──→</span> [Inventory]  <span class="mb4-cm">← independent</span>
                                               <span class="mb4-ok">──→</span> [Email]      <span class="mb4-cm">← independent</span>
                                               <span class="mb4-ok">──→</span> [Analytics]  <span class="mb4-cm">← independent</span>

<span class="mb4-hl">Order Service returns in &lt;1ms.</span> <span class="mb4-cm">Downstream services process asynchronously.</span>
<span class="mb4-cm">If email is down → messages queue up → processed when it recovers.</span>
<span class="mb4-cm">Each consumer processes at its own rate. No cascading failures.</span></pre>
      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0;">
        <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--mag);padding:14px">
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:15px;font-weight:900;color:var(--white);margin-bottom:6px">DECOUPLING</div>
          <div style="font-size:11px;color:var(--text);line-height:1.6">Producer doesn't know consumers exist. Add/remove consumers without touching producer. Services evolve independently.</div>
        </div>
        <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--mag);padding:14px">
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:15px;font-weight:900;color:var(--white);margin-bottom:6px">BUFFERING</div>
          <div style="font-size:11px;color:var(--text);line-height:1.6">Black Friday spike: 100K orders/sec hits queue. Consumer processes at steady 10K/sec. Queue absorbs the burst — no DB overload.</div>
        </div>
        <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--mag);padding:14px">
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:15px;font-weight:900;color:var(--white);margin-bottom:6px">REPLAY</div>
          <div style="font-size:11px;color:var(--text);line-height:1.6">Kafka retains messages for days/years. New service deployed? Read from offset 0 — replay all historical events. Invaluable for debugging.</div>
        </div>
      </div>
    </div>

    <!-- KAFKA -->
    <div class="mb4-view" id="view-kafka">
      <div class="mb4-sh">Kafka Architecture</div>
      <div class="mb4-sr">Topic → Partitions → Offsets → Consumer Groups — the mental model</div>

      <div class="mb4-kaf-box">
        <div class="mb4-kaf-label">// TOPIC: "order-placed" — 3 PARTITIONS, REPLICATION FACTOR 3</div>
        <div class="mb4-kaf-partitions">
          <div class="mb4-kaf-part">
            <div class="mb4-kp-title">PARTITION 0 — Broker 1 (leader)</div>
            <div class="mb4-kp-msgs">
              <div class="mb4-kp-msg">off:0 order#101</div>
              <div class="mb4-kp-msg">off:1 order#104</div>
              <div class="mb4-kp-msg">off:2 order#107</div>
            </div>
          </div>
          <div class="mb4-kaf-part">
            <div class="mb4-kp-title">PARTITION 1 — Broker 2 (leader)</div>
            <div class="mb4-kp-msgs">
              <div class="mb4-kp-msg">off:0 order#102</div>
              <div class="mb4-kp-msg">off:1 order#105</div>
              <div class="mb4-kp-msg">off:2 order#108</div>
            </div>
          </div>
          <div class="mb4-kaf-part">
            <div class="mb4-kp-title">PARTITION 2 — Broker 3 (leader)</div>
            <div class="mb4-kp-msgs">
              <div class="mb4-kp-msg">off:0 order#103</div>
              <div class="mb4-kp-msg">off:1 order#106</div>
              <div class="mb4-kp-msg">off:2 order#109</div>
            </div>
          </div>
        </div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:8px;color:var(--muted);margin-bottom:12px;letter-spacing:1px">// THREE INDEPENDENT CONSUMER GROUPS — all receive all messages</div>
        <div class="mb4-kaf-groups">
          <div class="mb4-kaf-grp">
            <div class="mb4-kg-name">GROUP A: inventory-service</div>
            <div class="mb4-kg-body">Consumer A1 → P0<br>Consumer A2 → P1<br>Consumer A3 → P2<br><span style="color:var(--mag);font-family:'IBM Plex Mono',monospace;font-size:9px">3 consumers = 3 partitions ✓</span></div>
          </div>
          <div class="mb4-kaf-grp">
            <div class="mb4-kg-name">GROUP B: email-service</div>
            <div class="mb4-kg-body">Consumer B1 → P0, P1, P2<br><br><span style="color:var(--yel);font-family:'IBM Plex Mono',monospace;font-size:9px">1 consumer handles all — slower, but independent</span></div>
          </div>
          <div class="mb4-kaf-grp">
            <div class="mb4-kg-name">GROUP C: analytics-service</div>
            <div class="mb4-kg-body">Consumer C1 → P0<br>Consumer C2 → P1<br>Consumer C3 → P2<br><span style="color:var(--mag);font-family:'IBM Plex Mono',monospace;font-size:9px">fully parallel ✓</span></div>
          </div>
        </div>
      </div>

      <div class="mb4-al mag"><em>The key insight:</em> Each consumer group maintains its own offset per partition. Group A being at offset 50 has zero effect on Group B at offset 12. They're completely independent readers of the same durable log.</div>

      <div class="mb4-sh">Replication & Durability</div>
      <div class="mb4-cb"><div class="mb4-cb-top">ISR and acks configuration<span class="mb4-cb-l">KAFKA CONFIG</span></div>
<pre class="mb4-c"><span class="mb4-cm">// replication.factor=3 → 1 leader + 2 ISR replicas per partition</span>
<span class="mb4-cm">// ISR = In-Sync Replicas (have replicated all leader messages)</span>

<span class="mb4-hl">acks=0:</span>  <span class="mb4-cm">Producer doesn't wait for ACK. Fastest, no durability guarantee.</span>
<span class="mb4-hl">acks=1:</span>  <span class="mb4-cm">Leader ACKs after writing. Fast, but replica may not have it yet.</span>
<span class="mb4-hl">acks=all:</span><span class="mb4-cm">All ISR ACKs before producer gets confirmation. Strongest guarantee.</span>

<span class="mb4-cm">// With acks=all + min.insync.replicas=2 + replication.factor=3:</span>
<span class="mb4-cm">// → Can lose 1 broker with ZERO data loss</span>
<span class="mb4-cm">// → Brokers 1 (leader) + Broker 2 (replica) both have message before ACK</span>
<span class="mb4-cm">// → Broker 1 dies → Broker 2 becomes leader → no data lost</span>

<span class="mb4-cm">// Partition key routing:</span>
<span class="mb4-fn">producer.send</span>(<span class="mb4-str">"order-placed"</span>, userId, orderEvent);
<span class="mb4-cm">// hash(userId) % numPartitions → same userId → same partition → ordered</span></pre>
      </div>
    </div>

    <!-- SEMANTICS -->
    <div class="mb4-view" id="view-semantics">
      <div class="mb4-sh">Delivery Semantics</div>
      <div class="mb4-sr">What happens when things go wrong — the three guarantees</div>

      <div class="mb4-sem-grid">
        <div class="mb4-sem-card" style="border-top:2px solid var(--yel)">
          <div class="mb4-sc-name" style="color:var(--yel)">AT-MOST-ONCE</div>
          <div class="mb4-sc-sub">FIRE AND FORGET</div>
          <div class="mb4-sc-body">Producer sends, no retry. Consumer auto-commits offset BEFORE processing.<br><br>Failure: consumer crashes after commit, before processing → <span style="color:var(--red)">message LOST</span>.</div>
          <div class="mb4-sc-use" style="color:var(--yel)">Use: analytics, metrics, logs<br>(loss is acceptable)</div>
        </div>
        <div class="mb4-sem-card" style="border-top:2px solid var(--mag)">
          <div class="mb4-sc-name" style="color:var(--mag)">AT-LEAST-ONCE</div>
          <div class="mb4-sc-sub">DEFAULT — MOST COMMON</div>
          <div class="mb4-sc-body">Producer retries on failure. Consumer commits AFTER processing.<br><br>Failure: consumer crashes after processing, before commit → <span style="color:var(--orange)">message DUPLICATED</span>.</div>
          <div class="mb4-sc-use" style="color:var(--mag)">Use: most systems — combine with<br>idempotent consumer pattern</div>
        </div>
        <div class="mb4-sem-card" style="border-top:2px solid var(--grn)">
          <div class="mb4-sc-name" style="color:var(--grn)">EXACTLY-ONCE</div>
          <div class="mb4-sc-sub">HARDEST — ~20% COST</div>
          <div class="mb4-sc-body">Idempotent producer (seq dedup) + Kafka transactions (atomic write + commit).<br><br>No loss, no duplicates. Requires <span style="color:var(--grn)">enable.idempotence=true</span> + <span style="color:var(--grn)">transactional.id</span>.</div>
          <div class="mb4-sc-use" style="color:var(--grn)">Use: financial transactions,<br>inventory — real harm from duplication</div>
        </div>
      </div>

      <div class="mb4-sh">Idempotent Consumer — Making At-Least-Once Safe</div>
      <div class="mb4-cb"><div class="mb4-cb-top">Processing the same message twice must be safe<span class="mb4-cb-l">JAVA</span></div>
<pre class="mb4-c"><span class="mb4-kw">public void</span> <span class="mb4-fn">processPayment</span>(PaymentEvent e) {
    <span class="mb4-cm">// Check idempotency key — has this message been processed before?</span>
    <span class="mb4-kw">if</span> (db.<span class="mb4-fn">exists</span>(<span class="mb4-str">"processed:"</span> + e.idempotencyKey)) {
        log.<span class="mb4-fn">info</span>(<span class="mb4-str">"Duplicate — skipping: {}"</span>, e.idempotencyKey);
        <span class="mb4-kw">return</span>;  <span class="mb4-cm">// Silently no-op on duplicate</span>
    }

    <span class="mb4-cm">// Atomic: process + mark as processed in same DB transaction</span>
    db.<span class="mb4-fn">transaction</span>(() -> {
        db.<span class="mb4-fn">debitAccount</span>(e.accountId, e.amount);
        db.<span class="mb4-fn">markProcessed</span>(<span class="mb4-str">"processed:"</span> + e.idempotencyKey);
    });
    <span class="mb4-cm">// Now commit Kafka offset — at-least-once is effectively exactly-once</span>
    consumer.<span class="mb4-fn">commitSync</span>();
}

<span class="mb4-cm">// Key: idempotencyKey must uniquely identify the business operation</span>
<span class="mb4-cm">// Options: UUID in message, (userId + orderId + action), event sequence number</span></pre>
      </div>

      <div class="mb4-al grn"><em>Interview insight:</em> Exactly-once in Kafka is real but expensive (~20% throughput cost). In practice, most teams use at-least-once + idempotent consumers. The idempotency key is the secret weapon — if processing the same event twice produces the same DB state, you've achieved the effect of exactly-once without the overhead.</div>
    </div>

    <!-- COMPARE -->
    <div class="mb4-view" id="view-compare">
      <div class="mb4-sh">Kafka vs RabbitMQ</div>
      <div class="mb4-sr">Not competing — different tools for different jobs</div>

      <table class="mb4-ct">
        <thead><tr><th>ASPECT</th><th>KAFKA</th><th>RABBITMQ</th></tr></thead>
        <tbody>
          <tr><td>Delivery model</td><td>Pull (consumers fetch at own pace)</td><td>Push (broker delivers to consumer)</td></tr>
          <tr><td>Message retention</td><td>Durable log — days to years after delivery</td><td>Deleted on ACK — ephemeral</td></tr>
          <tr><td>Throughput</td><td>Millions of messages/second</td><td>Hundreds of thousands/sec</td></tr>
          <tr><td>Ordering guarantee</td><td>Within a partition (by key)</td><td>Within a queue (single consumer)</td></tr>
          <tr><td>Replay history</td><td class="mb4-yes">Yes — seek to any offset</td><td class="mb4-no">No — deleted after consume</td></tr>
          <tr><td>Multiple consumers</td><td>N independent consumer groups</td><td>Competing consumers (one gets each msg)</td></tr>
          <tr><td>Routing logic</td><td>Topic/partition key only</td><td>Exchanges: direct, topic, fanout, headers</td></tr>
          <tr><td>Message TTL</td><td>Topic-level retention only</td><td>Per-message TTL, priority queues</td></tr>
        </tbody>
      </table>

      <div class="mb4-al mag"><em>Decision heuristic:</em> "Do I need replay, multiple independent consumers, or millions of events/sec?" → Kafka. "Do I need complex routing, per-message TTL, or a simple work queue?" → RabbitMQ. In practice: use Kafka for event streaming backbone, RabbitMQ for task queues with routing logic.</div>

      <div class="mb4-sh" style="margin-top:22px">When to Use Each — Concrete Scenarios</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0">
        <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--mag);padding:14px">
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:16px;font-weight:900;color:var(--mag);margin-bottom:8px">CHOOSE KAFKA</div>
          <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--text);line-height:2">
            ✓ Order lifecycle events (multiple services react)<br>
            ✓ User activity stream (audit log needed)<br>
            ✓ CDC: DB changes → Elasticsearch<br>
            ✓ Real-time analytics pipeline<br>
            ✓ Microservice event backbone<br>
            ✓ New service needs historical data (replay)
          </div>
        </div>
        <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--grn);padding:14px">
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:16px;font-weight:900;color:var(--grn);margin-bottom:8px">CHOOSE RABBITMQ</div>
          <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--text);line-height:2">
            ✓ Background email/SMS sending workers<br>
            ✓ Task distribution to N worker processes<br>
            ✓ Routing by message type to different queues<br>
            ✓ Per-job TTL (expire unprocessed jobs)<br>
            ✓ Priority queue (high-priority tasks first)<br>
            ✓ Simple job scheduler without replay needs
          </div>
        </div>
      </div>
    </div>

    <!-- PATTERNS -->
    <div class="mb4-view" id="view-patterns">
      <div class="mb4-sh">Key Kafka Patterns</div>
      <div class="mb4-sr">Fan-out · DLQ · Back-pressure · Ordering · Log compaction</div>

      <div class="mb4-pat-grid">
        <div class="mb4-pc" style="border-left-color:var(--mag)">
          <div class="mb4-pc-n">Fan-Out via Consumer Groups</div>
          <div class="mb4-pc-b">One topic → N consumer groups, all receiving all messages independently. The canonical Kafka pattern for microservices.</div>
          <div class="mb4-pc-eg" style="color:var(--mag)">Topic "order-placed" →<br>Group inventory-svc, Group email-svc,<br>Group analytics-svc, Group fraud-svc</div>
        </div>
        <div class="mb4-pc" style="border-left-color:var(--red)">
          <div class="mb4-pc-n">Dead Letter Queue (DLQ)</div>
          <div class="mb4-pc-b">After N failed retries, route to DLQ topic. Prevents one bad message from blocking the queue. Inspect/replay after fix.</div>
          <div class="mb4-pc-eg" style="color:var(--red)">topic → consumer → fail ×3<br>→ send to topic.dlq<br>→ alert on-call → fix → replay</div>
        </div>
        <div class="mb4-pc" style="border-left-color:var(--yel)">
          <div class="mb4-pc-n">Back-Pressure Monitoring</div>
          <div class="mb4-pc-b">Consumer lag = latest_offset − committed_offset. High lag = consumer falling behind. Scale consumers (up to numPartitions) or optimize logic.</div>
          <div class="mb4-pc-eg" style="color:var(--yel)">Alert: consumer_lag > 10,000<br>Action: scale consumer group<br>Ceiling: max_consumers = num_partitions</div>
        </div>
        <div class="mb4-pc" style="border-left-color:var(--grn)">
          <div class="mb4-pc-n">Per-Entity Ordering</div>
          <div class="mb4-pc-b">Partition by user_id or order_id → all events for same entity → same partition → strictly ordered. Different entities process in parallel.</div>
          <div class="mb4-pc-eg" style="color:var(--grn)">producer.send(topic, userId, event)<br>→ hash(userId) % numPartitions<br>→ same partition = in-order</div>
        </div>
        <div class="mb4-pc" style="border-left-color:var(--blu)">
          <div class="mb4-pc-n">Log Compaction</div>
          <div class="mb4-pc-b">Retain only the LATEST message per key. New consumers rebuild current state without full history. Like a change-data-capture snapshot.</div>
          <div class="mb4-pc-eg" style="color:var(--blu)">Before: [u1:v1][u2:v1][u1:v2][u1:v3]<br>After:  [u2:v1][u1:v3] (latest per key)<br>Use: user profiles, config, inventory</div>
        </div>
        <div class="mb4-pc" style="border-left-color:var(--orange)">
          <div class="mb4-pc-n">Outbox Pattern</div>
          <div class="mb4-pc-b">Write to DB outbox table and publish to Kafka atomically (same transaction). Prevents dual-write inconsistency between DB and queue.</div>
          <div class="mb4-pc-eg" style="color:var(--orange)">BEGIN TRANSACTION<br>  INSERT INTO orders ...<br>  INSERT INTO outbox (event, payload)<br>COMMIT → CDC picks up → Kafka</div>
        </div>
      </div>
    </div>

    <!-- CONFIG -->
    <div class="mb4-view" id="view-config">
      <div class="mb4-sh">Configuration Cheatsheet</div>
      <div class="mb4-sr">Producer · Consumer · Topic — the settings that matter in interviews</div>

      <div class="mb4-cfg-grid">
        <div class="mb4-cfg-card">
          <div class="mb4-cfg-title">Producer</div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">acks</span><span class="mb4-cfg-v">all</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">enable.idempotence</span><span class="mb4-cfg-v">true</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">retries</span><span class="mb4-cfg-v">MAX_INT</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">linger.ms</span><span class="mb4-cfg-v">5</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">batch.size</span><span class="mb4-cfg-v">16384</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">compression.type</span><span class="mb4-cfg-v">snappy</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">transactional.id</span><span class="mb4-cfg-v">unique-id</span></div>
        </div>
        <div class="mb4-cfg-card">
          <div class="mb4-cfg-title">Consumer</div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">enable.auto.commit</span><span class="mb4-cfg-v">false</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">auto.offset.reset</span><span class="mb4-cfg-v">earliest</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">max.poll.records</span><span class="mb4-cfg-v">500</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">session.timeout.ms</span><span class="mb4-cfg-v">30000</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">isolation.level</span><span class="mb4-cfg-v">read_committed</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">fetch.min.bytes</span><span class="mb4-cfg-v">1</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">heartbeat.interval</span><span class="mb4-cfg-v">3000</span></div>
        </div>
        <div class="mb4-cfg-card">
          <div class="mb4-cfg-title">Topic</div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">num.partitions</span><span class="mb4-cfg-v">12</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">replication.factor</span><span class="mb4-cfg-v">3</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">min.insync.replicas</span><span class="mb4-cfg-v">2</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">retention.ms</span><span class="mb4-cfg-v">604800000</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">cleanup.policy</span><span class="mb4-cfg-v">delete</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">cleanup.policy</span><span class="mb4-cfg-v">compact</span></div>
          <div class="mb4-cfg-row"><span class="mb4-cfg-k">max.message.bytes</span><span class="mb4-cfg-v">1048576</span></div>
        </div>
      </div>

      <div class="mb4-sh" style="margin-top:22px">Scale Estimation</div>
      <div class="mb4-cb"><div class="mb4-cb-top">How many partitions do I need?<span class="mb4-cb-l">MATH</span></div>
<pre class="mb4-c"><span class="mb4-cm">// Example: order event stream</span>
<span class="mb4-cm">// 1M orders/day, peak 50× average</span>

Peak events/sec  = 1M orders/day ÷ 86,400 × 50 = <span class="mb4-mg">~580 events/sec</span>
Event size       = <span class="mb4-or">1 KB</span>
Peak throughput  = 580 × 1KB = <span class="mb4-mg">~0.6 MB/sec</span>

<span class="mb4-cm">// Single partition max throughput: ~100 MB/sec write</span>
Partitions needed = 0.6 MB/sec ÷ 100 MB/sec = <span class="mb4-ok">1 partition</span> <span class="mb4-cm">(use 12 for growth headroom)</span>

<span class="mb4-cm">// Storage (7-day retention, 3 replicas):</span>
Daily = 580 events/sec × 86,400 × 1 KB = <span class="mb4-mg">~50 GB/day</span>
Total = 50 GB × 7 days × 3 replicas   = <span class="mb4-mg">~1.05 TB</span>

<span class="mb4-cm">// General rules:</span>
<span class="mb4-cm">//   num_partitions ≥ max_consumers_in_any_group</span>
<span class="mb4-cm">//   num_partitions = target_throughput_MB_s ÷ throughput_per_partition_MB_s</span>
<span class="mb4-cm">//   Start with 12–24, easier to add partitions than subtract</span></pre>
      </div>
    </div>

    <!-- TASKS -->
    <div class="mb4-view" id="view-tasks">
      <div class="mb4-task-list">
        <div class="mb4-task-card">
          <div class="mb4-task-hd" onclick="mb4ToggleTask(this)"><div class="mb4-t-num">01</div><div class="mb4-t-lbl">Delivery Semantics — 5 Systems</div><div class="mb4-t-meta">~1 hr</div><div class="mb4-t-arr">›</div></div>
          <div class="mb4-task-bd">
            <p>For each, choose at-most-once / at-least-once / exactly-once. State the failure scenario and idempotency strategy:</p>
            <ol>
              <li><strong>Real-time page view counter</strong> for analytics dashboard</li>
              <li><strong>Bank transfer</strong> between two accounts triggered by Kafka event</li>
              <li><strong>Email notification:</strong> "Your order has shipped" (user receives one email)</li>
              <li><strong>Inventory decrement</strong> when an order is placed (oversell = bad)</li>
              <li><strong>User activity feed update</strong> — showing what friends liked</li>
            </ol>
            <p style="margin-top:8px">For each: what is the <strong>exact failure scenario</strong> if you choose wrong?</p>
          </div>
        </div>

        <div class="mb4-task-card">
          <div class="mb4-task-hd" onclick="mb4ToggleTask(this)"><div class="mb4-t-num">02</div><div class="mb4-t-lbl">Partition Key Design — 5 Scenarios</div><div class="mb4-t-meta">~1 hr</div><div class="mb4-t-arr">›</div></div>
          <div class="mb4-task-bd">
            <p>For each: choose the partition key, state the ordering guarantee provided, and identify any potential hotkey risk:</p>
            <ol>
              <li><strong>E-commerce order events:</strong> created → paid → shipped → delivered (must be in order)</li>
              <li><strong>WhatsApp group chat</strong> messages (order within a conversation matters)</li>
              <li><strong>Real-time stock prices</strong> for 10,000 tickers (Apple trades 1000× more than a small cap)</li>
              <li><strong>IoT sensor readings</strong> from 100K devices</li>
              <li><strong>User login/logout events</strong> (session coherence required)</li>
            </ol>
          </div>
        </div>

        <div class="mb4-task-card">
          <div class="mb4-task-hd" onclick="mb4ToggleTask(this)"><div class="mb4-t-num">03</div><div class="mb4-t-lbl">Kafka vs RabbitMQ — 5 Decisions</div><div class="mb4-t-meta">~45 min</div><div class="mb4-t-arr">›</div></div>
          <div class="mb4-task-bd">
            <ol>
              <li>8 microservices all need to react to every new user signup — each does something different</li>
              <li>Background job system that sends weekly digest emails to 10M users</li>
              <li>Fraud detection pipeline that must audit every financial transaction for 5 years</li>
              <li>Real-time bidding system where each ad impression must be handled by exactly ONE bidder</li>
              <li>CDC pipeline streaming database row changes to Elasticsearch for search indexing</li>
            </ol>
          </div>
        </div>

        <div class="mb4-task-card" style="border-top:2px solid var(--mag)">
          <div class="mb4-task-hd" onclick="mb4ToggleTask(this)"><div class="mb4-t-num" style="color:var(--mag)">★</div><div class="mb4-t-lbl">Uber Event Streaming Architecture</div><div class="mb4-t-meta">~3 hrs · full design</div><div class="mb4-t-arr">›</div></div>
          <div class="mb4-task-bd">
            <p><strong>Context:</strong> 5M active drivers sending GPS every 4 seconds. Ride lifecycle events (requested, matched, started, completed, rated). Surge pricing recalculated per zone per minute. Real-time analytics + historical audit.</p>
            <p style="margin-top:8px">Design complete Kafka architecture. For each topic:</p>
            <ul>
              <li>Topic name and purpose</li>
              <li>Partition key choice and ordering guarantee</li>
              <li>Delivery semantic (with justification)</li>
              <li>Retention policy (with justification)</li>
              <li>Which consumer groups consume it and what they do</li>
            </ul>
            <p style="margin-top:8px">Calculate: peak events/sec total, storage/day total, minimum partitions needed.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- CHECKLIST -->
    <div class="mb4-view" id="view-checklist">
      <div class="mb4-prog-row"><span id="prog-lbl">0 / 15 completed</span><span style="font-family:'IBM Plex Mono',monospace">MODULE B4 · MESSAGE QUEUES</span></div>
      <div class="mb4-prog-track"><div class="mb4-prog-fill" id="prog-fill"></div></div>

      <div class="mb4-chk-grid">
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">3 messaging models: queue, pub-sub, event stream — and when to use each</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Kafka: topic → partition → offset → consumer group mental model</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Consumer groups: how N groups read the same topic independently</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Partition key: ordering guarantee, hotkey risk, hash(key) % N routing</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">At-most-once: auto-commit before processing — message loss scenario</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">At-least-once: commit after processing — duplication scenario</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Exactly-once: idempotent producer + transactions — ~20% cost</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Idempotent consumer pattern implementation in code</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Kafka vs RabbitMQ: pull vs push, retention, replay, routing</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Fan-out pattern: N consumer groups each getting all messages</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Dead letter queue: purpose, after-N-retries flow, manual replay</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Consumer lag = latest_offset − committed_offset; how to fix high lag</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">Key configs: acks=all, enable.idempotence, replication.factor, min.insync.replicas</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">✏️ Tasks 1–3: semantics, partition keys, Kafka vs Rabbit decisions</div></div>
        <div class="mb4-chk" onclick="mb4Tick(this)"><div class="mb4-chk-box"></div><div class="mb4-chk-lbl">✏️ Capstone: Uber streaming architecture — full Kafka design with estimates</div></div>
      </div>

      <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--mag)">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
        <div style="font-family:'Barlow Condensed',sans-serif;font-size:30px;font-weight:900;color:var(--white);margin-bottom:6px">B5 — URL SHORTENER</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
          First end-to-end HLD case study · 300M URLs · 100:1 read:write ratio<br>
          Short code generation (base62, MD5) · Redirect latency &lt;10ms · Hot URL caching<br>
          Analytics pipeline · Rate limiting · Custom aliases · TTL expiry
        </div>
      </div>
    </div>

  </div>
  
  <div class="mb4-bottom-nav">
    <a href="/learning/system-design/hld/module-b3-caching/" class="mb4-nav-footer-btn">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
      B3: Caching
    </a>
    <a href="/learning/system-design/hld/module-b4-notes/" class="mb4-nav-footer-btn">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
      READ STUDY NOTES
    </a>
    <a href="/learning/system-design/system-design-roadmap/" class="mb4-nav-footer-btn">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
      ROADMAP
    </a>
    <a href="/learning/system-design/hld/module-b5-url-shortener/" class="mb4-nav-footer-btn">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      B5: URL Shortener
    </a>
  </div>
</div>
<script src="{{ "/assets/js/sd-module-b4.js" | relative_url }}"></script>
