---
layout: learning
title: "M13 — Event-Driven Architecture"
description: "Kafka internals, RabbitMQ patterns, Saga, Outbox, CQRS, Event Sourcing, idempotent consumers — with C/librdkafka implementations"
---

<style>
/* ── Module shell ── */
.mod-wrap{max-width:960px;margin:0 auto;padding:0 1rem 4rem;font-family:'Segoe UI',system-ui,sans-serif;color:#1e293b}
.mod-header{background:#fff;border-left:5px solid #06b6d4;border-radius:10px;padding:1.6rem 2rem;margin-bottom:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;color:#0f172a}
.mod-header .sub{color:#64748b;font-size:.95rem}
.phase-tag{display:inline-block;background:linear-gradient(90deg,#06b6d4,#0ea5e9);color:#fff;font-size:.75rem;font-weight:700;padding:.25rem .75rem;border-radius:20px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.05em}

/* ── Tabs ── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.25rem}
.tab-btn{padding:.45rem 1rem;border:2px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.82rem;font-weight:600;cursor:pointer;color:#64748b;transition:all .2s}
.tab-btn:hover{border-color:#06b6d4;color:#06b6d4}
.tab-btn.active{background:linear-gradient(135deg,#06b6d4,#0ea5e9);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(6,182,212,.35)}
.tab-pane{display:none}.tab-pane.active{display:block}

/* ── Cards / panels ── */
.cp{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.cp-hdr{padding:.65rem 1.1rem;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.5rem}
.cp-body{padding:1rem 1.2rem;background:#fff;font-size:.9rem;line-height:1.75}
.p-cyan  .cp-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);color:#0e7490;border-left:4px solid #06b6d4}
.p-blue  .cp-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);color:#1d4ed8;border-left:4px solid #3b82f6}
.p-teal  .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #22c55e}
.p-orange.cp-hdr,.p-orange>.cp-hdr{background:linear-gradient(90deg,#fff7ed,#ffedd5);color:#c2410c;border-left:4px solid #f97316}
.p-purple.cp-hdr,.p-purple>.cp-hdr{background:linear-gradient(90deg,#faf5ff,#f3e8ff);color:#7e22ce;border-left:4px solid #a855f7}
.p-green .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #16a34a}
.p-red   .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#be123c;border-left:4px solid #f43f5e}
.p-amber .cp-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);color:#92400e;border-left:4px solid #f59e0b}
.p-indigo.cp-hdr{background:linear-gradient(90deg,#eef2ff,#e0e7ff);color:#3730a3;border-left:4px solid #6366f1}
.p-violet.cp-hdr{background:linear-gradient(90deg,#f5f3ff,#ede9fe);color:#5b21b6;border-left:4px solid #7c3aed}
.p-orange{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-purple{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}

/* ── Callouts ── */
.ins,.warn,.note,.analogy{border-radius:8px;padding:.75rem 1rem;margin:.75rem 0;font-size:.87rem;line-height:1.7}
.ins  {background:#ecfeff;border-left:4px solid #06b6d4;color:#164e63}
.warn {background:#fff7ed;border-left:4px solid #f97316;color:#7c2d12}
.note {background:#f0f9ff;border-left:4px solid #0ea5e9;color:#0c4a6e}
.analogy{background:#faf5ff;border-left:4px solid #a855f7;color:#581c87}

/* ── Code blocks ── */
.cb{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-size:.82rem;line-height:1.75;font-family:'Cascadia Code','Fira Code',monospace}
.cm{color:#94a3b8}.ck{color:#7dd3fc}.cv{color:#86efac}.cs{color:#fca5a5}
.cn{color:#fdba74}.cf{color:#c4b5fd}.co{color:#fde68a}.cg{color:#6ee7b7}

/* ── Flow list ── */
.flow-list{list-style:none;padding:0;margin:.5rem 0}
.fl-step{display:flex;align-items:flex-start;gap:.85rem;padding:.65rem .85rem;margin-bottom:.5rem;border-radius:8px;background:#f8fafc;border-left:3px solid #06b6d4;font-size:.88rem;line-height:1.65}
.fl-num{background:linear-gradient(135deg,#06b6d4,#0ea5e9);color:#fff;border-radius:50%;width:1.6rem;height:1.6rem;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0}

/* ── Tables ── */
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0}
.t-table th{background:linear-gradient(90deg,#06b6d4,#0ea5e9);color:#fff;padding:.6rem .9rem;text-align:left}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#ecfeff}

/* ── Two-col ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.75rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* ── Lab box ── */
.lab-box{border:2px solid #06b6d4;border-radius:10px;margin-bottom:1.25rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);padding:.7rem 1.1rem;display:flex;align-items:center;gap:.6rem;font-weight:700;font-size:.9rem;color:#0e7490}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.75}
.lab-step{padding:.4rem 0;padding-left:1.1rem;border-left:2px solid #06b6d4;margin-bottom:.4rem}
.sn{display:inline-block;background:#06b6d4;color:#fff;border-radius:50%;width:1.3rem;height:1.3rem;font-size:.7rem;font-weight:700;text-align:center;line-height:1.3rem;margin-right:.4rem}

/* ── Checklist ── */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.35rem .5rem;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem}
.cl li::before{content:"☐";color:#06b6d4;font-size:1rem;flex-shrink:0}

/* ── Diagram ── */
.diagram-box{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.78rem;line-height:1.8;color:#94a3b8}
.dg-cyan{color:#67e8f9}.dg-blue{color:#93c5fd}.dg-green{color:#86efac}.dg-red{color:#fca5a5}.dg-amber{color:#fde68a}.dg-gray{color:#64748b}.dg-purple{color:#c4b5fd}

/* ── Navigation ── */
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding:1rem 0;border-top:2px solid #e2e8f0;font-size:.88rem}
.nb{padding:.5rem 1.1rem;border:2px solid #06b6d4;border-radius:20px;color:#06b6d4;text-decoration:none;font-weight:600;transition:all .2s}
.nb:hover{background:#06b6d4;color:#fff}
.sep{text-align:center;color:#94a3b8;font-size:.8rem;letter-spacing:.1em;margin:1.5rem 0;text-transform:uppercase}
</style>

<div class="mod-wrap">

<div class="mod-header">
  <h1>M13 — Event-Driven Architecture</h1>
  <div class="sub">
    <span class="phase-tag">Phase 5</span>
    Kafka internals &amp; delivery semantics · RabbitMQ exchange patterns · Saga &amp; Outbox · CQRS &amp; Event Sourcing · Idempotent consumers · C/librdkafka implementations
  </div>
</div>

<!-- Tab bar -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-kafka',this)">Kafka Core</button>
  <button class="tab-btn" onclick="vt('t-delivery',this)">Delivery Semantics</button>
  <button class="tab-btn" onclick="vt('t-rabbit',this)">RabbitMQ</button>
  <button class="tab-btn" onclick="vt('t-saga',this)">Saga &amp; Outbox</button>
  <button class="tab-btn" onclick="vt('t-cqrs',this)">CQRS &amp; Event Sourcing</button>
  <button class="tab-btn" onclick="vt('t-idempotency',this)">Idempotency</button>
  <button class="tab-btn" onclick="vt('t-impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 1 — Overview
     ══════════════════════════════════════════════════════════ -->
<div id="t-overview" class="tab-pane active">

<div class="cp p-cyan">
  <div class="cp-hdr">🎯 Why Event-Driven Architecture?</div>
  <div class="cp-body">
    Synchronous request/response creates <strong>temporal coupling</strong> — the caller blocks until the callee responds, and a slow callee cascades latency. Event-driven architecture severs this coupling: producers emit events without knowing who consumes them, and consumers process at their own pace.
    <br><br>
    <strong>Key motivations:</strong>
    <ul>
      <li><strong>Temporal decoupling:</strong> producer and consumer run independently — if the consumer is down, events buffer in the broker</li>
      <li><strong>Fanout:</strong> one event reaches multiple consumers simultaneously (notifications, analytics, search indexing — all from one order-placed event)</li>
      <li><strong>Audit log / replay:</strong> full event history is replayable — rebuild any read model from scratch, debug production issues with real data</li>
      <li><strong>Reduces synchronous blocking chains:</strong> checkout doesn't wait for email service; email service consumes the event asynchronously</li>
      <li><strong>Enables eventual consistency:</strong> services converge on consistent state over time, trading strong consistency for availability and partition tolerance</li>
    </ul>
  </div>
</div>

<div class="analogy">
  <strong>Analogy — Event streaming vs work queue:</strong><br>
  A <em>work queue</em> (RabbitMQ) is like a restaurant ticket system — a ticket is torn off by one chef, cooked, and discarded. A <em>log-based stream</em> (Kafka) is like a newspaper printing press — each edition is stamped with a page number (offset), archived forever, and any subscriber can re-read any past edition at any time.
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">📦 Message Queue Model (RabbitMQ)</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Message consumed → <strong>deleted</strong> from queue</li>
        <li>Push-based delivery to consumers</li>
        <li>Competing consumers share load</li>
        <li>At-most-once or at-least-once via ACK</li>
        <li>Dead-letter exchange handles failures</li>
        <li>Complex routing via exchanges</li>
        <li>Great for: task queues, RPC, work distribution</li>
      </ul>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">📜 Event Stream Model (Kafka)</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Messages <strong>retained</strong> for configurable period</li>
        <li>Pull-based: consumers control their pace</li>
        <li>Consumer groups: each partition → one consumer</li>
        <li>Exactly-once via idempotent producer + transactions</li>
        <li>Any consumer can replay from any offset</li>
        <li>Ordered within partition</li>
        <li>Great for: event sourcing, audit log, stream processing</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📐 Pattern Landscape</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Pattern</th><th>Problem Solved</th><th>Trade-off</th></tr></thead>
      <tbody>
        <tr><td><strong>Outbox</strong></td><td>Atomic: DB write + event publish in one transaction</td><td>Extra table + relay process</td></tr>
        <tr><td><strong>Saga (Orchestration)</strong></td><td>Multi-service transactions without 2PC</td><td>Central coordinator = SPOF risk</td></tr>
        <tr><td><strong>Saga (Choreography)</strong></td><td>Distributed coordination via events</td><td>Hard to trace overall flow</td></tr>
        <tr><td><strong>CQRS</strong></td><td>Separate write model from read model</td><td>Eventual consistency on reads</td></tr>
        <tr><td><strong>Event Sourcing</strong></td><td>State as immutable event log</td><td>Complex queries, snapshot management</td></tr>
        <tr><td><strong>Idempotent Consumer</strong></td><td>Handle at-least-once delivery safely</td><td>Dedup table storage + lookup cost</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🗺️ Phase 5 Module Map</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Module</th><th>Topic</th><th>Key Concepts</th></tr></thead>
      <tbody>
        <tr><td><strong>M13 (this)</strong></td><td>Event-Driven Architecture</td><td>Kafka, RabbitMQ, Saga, Outbox, CQRS, Event Sourcing</td></tr>
        <tr><td>M14</td><td>Stream Processing</td><td>Kafka Streams, Flink windowing, stateful operators, exactly-once</td></tr>
      </tbody>
    </table>
    <div class="note" style="margin-top:.75rem">Prerequisites: Ph2 (databases — you need to understand transactions for Outbox), Ph4 (concurrency — consumer thread pools, back-pressure)</div>
  </div>
</div>

</div><!-- /t-overview -->

<!-- ══════════════════════════════════════════════════════════
     TAB 2 — Kafka Core
     ══════════════════════════════════════════════════════════ -->
<div id="t-kafka" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">⚙️ Kafka Architecture — Internals</div>
  <div class="cp-body">
    Kafka's fundamental unit is the <strong>topic</strong> — a logical feed of records. Topics are split into <strong>partitions</strong>, each an ordered, immutable append-only log on disk.
  </div>
</div>

<div class="diagram-box">
<span class="dg-cyan">Topic: orders</span>
<span class="dg-gray">  (3 partitions, replication-factor=2)</span>

<span class="dg-blue">Partition 0</span>  [<span class="dg-amber">offset 0</span>][<span class="dg-amber">offset 1</span>][<span class="dg-amber">offset 2</span>]...[<span class="dg-green">offset 847</span>]  ← append-only
<span class="dg-blue">Partition 1</span>  [<span class="dg-amber">offset 0</span>][<span class="dg-amber">offset 1</span>]...[<span class="dg-green">offset 391</span>]
<span class="dg-blue">Partition 2</span>  [<span class="dg-amber">offset 0</span>]...[<span class="dg-green">offset 1203</span>]

<span class="dg-gray">          ┌─── Broker 1 (leader P0, follower P1) ───┐</span>
<span class="dg-gray">          │    Broker 2 (leader P1, follower P2)    │</span>
<span class="dg-gray">          │    Broker 3 (leader P2, follower P0)    │</span>
<span class="dg-gray">          └─────────────────────────────────────────┘</span>

<span class="dg-purple">Producer</span> → assigns partition by: <span class="dg-cyan">hash(key) % num_partitions</span> (key set)
                              or: <span class="dg-cyan">round-robin</span> (key=null)

<span class="dg-green">Consumer Group A</span>: consumer-A1 reads P0, consumer-A2 reads P1, consumer-A3 reads P2
<span class="dg-red">Consumer Group B</span>: consumer-B1 reads P0+P1, consumer-B2 reads P2  (independent read positions)
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🔑 Partition Key Assignment</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Key set:</strong> <code>partition = murmur2(key) % num_partitions</code> — all events for the same key go to the same partition → ordering guaranteed per key</li>
        <li><strong>Key null:</strong> sticky partitioner (batch to one partition, rotate after batch) — maximizes throughput</li>
        <li><strong>Custom partitioner:</strong> implement <code>Partitioner</code> interface for business logic (e.g., tenant-based routing)</li>
      </ul>
      <div class="warn" style="margin-top:.5rem">Hot partition: if 10% of keys account for 80% of traffic, their partition becomes a bottleneck. Spread hot keys with a suffix: <code>order_id + "_" + random(0,N)</code></div>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">🔄 Consumer Group Rebalancing</div>
    <div class="cp-body">
      When a consumer joins or leaves, the group coordinator (a broker) triggers a <strong>rebalance</strong>:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Eager rebalance (stop-the-world):</strong> all consumers stop, revoke all partitions, reassign — processing pauses</li>
        <li><strong>Cooperative rebalance (incremental):</strong> only affected partitions are moved; others keep processing — reduces pause</li>
        <li><code>partition.assignment.strategy = CooperativeStickyAssignor</code> for incremental</li>
        <li><code>session.timeout.ms</code>: consumer must send heartbeat within this window or be considered dead → rebalance</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-cyan">
  <div class="cp-hdr">📊 ISR — In-Sync Replicas</div>
  <div class="cp-body">
    Each partition has one <strong>leader</strong> (handles all reads/writes) and N <strong>follower replicas</strong> that pull from the leader. The <strong>ISR set</strong> tracks which replicas are caught up within <code>replica.lag.time.max.ms</code>.
    <br><br>
    <table class="t-table">
      <thead><tr><th>Setting</th><th>Meaning</th><th>Trade-off</th></tr></thead>
      <tbody>
        <tr><td><code>acks=0</code></td><td>Producer doesn't wait for any ack</td><td>Fastest, may lose messages</td></tr>
        <tr><td><code>acks=1</code></td><td>Leader acknowledges write</td><td>Lost if leader fails before replication</td></tr>
        <tr><td><code>acks=all</code> (-1)</td><td>All ISR members acknowledge</td><td>Slowest, strongest durability</td></tr>
        <tr><td><code>min.insync.replicas=2</code></td><td>Minimum ISR for acks=all to succeed</td><td>Prevents silent data loss with small ISR</td></tr>
      </tbody>
    </table>
    <div class="ins">Production recommendation: <code>acks=all</code> + <code>min.insync.replicas=2</code> + <code>replication.factor=3</code> — survives one broker failure without data loss.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">📍 Offset Management</div>
  <div class="cp-body">
    Each consumer group tracks its position (offset) per partition in the <code>__consumer_offsets</code> internal topic.
    <br><br>
    <strong>Commit strategies:</strong>
    <ul>
      <li><strong>Auto-commit</strong> (<code>enable.auto.commit=true</code>): commits periodically. Risk: commit before processing → data loss on crash; or process but not commit → reprocess on restart</li>
      <li><strong>Manual sync commit</strong> (<code>commitSync()</code>): blocks until broker confirms. Safe but slower</li>
      <li><strong>Manual async commit</strong> (<code>commitAsync()</code>): fire-and-forget. Higher throughput, retry on failure is tricky (stale offset may overwrite newer commit)</li>
      <li><strong>Best practice:</strong> manual sync commit after batch processing, async for throughput-critical paths with idempotent processing</li>
    </ul>
    <div class="note"><strong>Log compaction:</strong> Kafka can compact topics (<code>cleanup.policy=compact</code>) — keeps only the latest value per key, discards older records. Used for changelogs (KTable in Kafka Streams).</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📐 Kafka Producer Batching &amp; Compression</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Config</th><th>Effect</th><th>Tuning Guidance</th></tr></thead>
      <tbody>
        <tr><td><code>batch.size</code></td><td>Max bytes per batch per partition</td><td>Increase (e.g. 64KB) for throughput</td></tr>
        <tr><td><code>linger.ms</code></td><td>Wait up to N ms to fill a batch</td><td>5–50ms trades latency for throughput</td></tr>
        <tr><td><code>compression.type</code></td><td>snappy/lz4/zstd per batch</td><td>zstd for best ratio, lz4 for speed</td></tr>
        <tr><td><code>buffer.memory</code></td><td>Total producer buffer bytes</td><td>Increase if producers block frequently</td></tr>
        <tr><td><code>max.in.flight.requests.per.connection</code></td><td>Concurrent unacked requests</td><td>Set to 1 for strict ordering (without idempotence)</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-kafka -->

<!-- ══════════════════════════════════════════════════════════
     TAB 3 — Delivery Semantics
     ══════════════════════════════════════════════════════════ -->
<div id="t-delivery" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">📬 The Three Delivery Guarantees</div>
  <div class="cp-body">
    Message delivery semantics describe what happens when things go wrong (network timeout, broker restart, producer crash mid-send).
    <table class="t-table" style="margin-top:.75rem">
      <thead><tr><th>Guarantee</th><th>How</th><th>Risk</th><th>Use When</th></tr></thead>
      <tbody>
        <tr><td><strong>At-most-once</strong></td><td><code>acks=0</code>, no retry</td><td>Messages lost if broker is down</td><td>Metrics where loss is acceptable</td></tr>
        <tr><td><strong>At-least-once</strong></td><td><code>acks=all</code> + retries</td><td>Duplicates on retry after timeout</td><td>Most use-cases with idempotent consumers</td></tr>
        <tr><td><strong>Exactly-once</strong></td><td>Idempotent producer + transactions</td><td>Higher latency, more complex</td><td>Financial transfers, order processing</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔑 At-Least-Once: The Duplicate Problem</div>
  <div class="cp-body">
    With retries enabled, a producer sends a message. The broker receives it, writes it, but the network fails before sending the ACK. The producer retries — the broker receives a duplicate.
    <div class="diagram-box" style="margin:.75rem 0">
<span class="dg-cyan">Producer</span>  ──[msg #1]──►  <span class="dg-blue">Broker</span>  (writes to log)
                             │
              network blip ──┘  <span class="dg-red">(ACK lost)</span>

<span class="dg-cyan">Producer</span>  ──[msg #1 retry]──►  <span class="dg-blue">Broker</span>  (writes duplicate!)
                                  offset 5: msg#1
                                  offset 6: msg#1  ← <span class="dg-red">duplicate!</span>
    </div>
    <strong>Solution:</strong> idempotent producer assigns each message a <strong>sequence number + producer ID (PID)</strong>. The broker deduplicates within a 5-message window per <code>(PID, partition)</code>.
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">✅ Exactly-Once: Idempotent Producer + Transactions</div>
  <div class="cp-body">
    <strong>Idempotent producer</strong> (single-partition, single-session):
<div class="cb"><span class="cm">// Producer config for idempotence</span>
<span class="ck">rd_kafka_conf_set</span>(conf, <span class="cv">"enable.idempotence"</span>, <span class="cv">"true"</span>, errstr, sz);
<span class="cm">// Automatically sets: acks=all, retries=INT_MAX, max.in.flight=5</span></div>
    <strong>Transactional producer</strong> (multi-partition, multi-message atomic write):
<div class="cb"><span class="cm">// Transactional config</span>
<span class="ck">rd_kafka_conf_set</span>(conf, <span class="cv">"enable.idempotence"</span>, <span class="cv">"true"</span>, errstr, sz);
<span class="ck">rd_kafka_conf_set</span>(conf, <span class="cv">"transactional.id"</span>, <span class="cv">"my-txn-producer-1"</span>, errstr, sz);

<span class="cm">// Usage pattern</span>
<span class="ck">rd_kafka_init_transactions</span>(rk, <span class="cn">10000</span>);   <span class="cm">// once at startup</span>
<span class="ck">rd_kafka_begin_transaction</span>(rk);
<span class="cm">// ... produce messages ...</span>
err = <span class="ck">rd_kafka_commit_transaction</span>(rk, <span class="cn">10000</span>);
<span class="cm">// on error:</span>
<span class="ck">rd_kafka_abort_transaction</span>(rk, <span class="cn">10000</span>);</div>
    <div class="note">Transactions guarantee atomicity across partitions: all messages commit or none do. Consumers must set <code>isolation.level=read_committed</code> to skip uncommitted messages (aborted transaction leftovers).</div>
    <div class="warn"><strong>EOS (Exactly-Once Semantics) end-to-end</strong> requires: idempotent producer + transactions + <code>read_committed</code> isolation + atomic offset commit within the transaction. This is what Kafka Streams provides out-of-the-box with <code>processing.guarantee=exactly_once_v2</code>.</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">⚡ Consumer-Side Delivery Semantics</div>
  <div class="cp-body">
    Delivery guarantees apply to both producer→broker and broker→consumer:
    <ul>
      <li><strong>At-most-once consumer:</strong> commit offset <em>before</em> processing. If processing fails, message is lost (offset already moved forward)</li>
      <li><strong>At-least-once consumer:</strong> commit offset <em>after</em> processing. If crash after process but before commit, message is reprocessed on restart → make consumers idempotent</li>
      <li><strong>Exactly-once consumer:</strong> atomic commit — use Kafka transactions to write processing result AND commit offset in one transaction</li>
    </ul>
    <div class="ins">
      <strong>Practical guidance:</strong> for most systems, at-least-once delivery + idempotent consumers is the right balance. Pure exactly-once adds significant complexity — use only when duplicates cause real business harm (billing, double-shipping).
    </div>
  </div>
</div>

</div><!-- /t-delivery -->

<!-- ══════════════════════════════════════════════════════════
     TAB 4 — RabbitMQ
     ══════════════════════════════════════════════════════════ -->
<div id="t-rabbit" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">🐰 RabbitMQ — AMQP Model</div>
  <div class="cp-body">
    RabbitMQ implements the AMQP 0-9-1 protocol. Messages are published to <strong>exchanges</strong>, which route to <strong>queues</strong> via <strong>bindings</strong>. Consumers subscribe to queues.
  </div>
</div>

<div class="diagram-box">
<span class="dg-purple">Publisher</span>  ──[msg + routing_key]──►  <span class="dg-cyan">Exchange</span>
                                           │
                                           ├──[binding: routing_key=*.error]──► <span class="dg-blue">Queue: errors</span>
                                           ├──[binding: routing_key=orders.*]──► <span class="dg-green">Queue: orders</span>
                                           └──[binding: fanout]──────────────► <span class="dg-amber">Queue: analytics</span>
                                                                               <span class="dg-amber">Queue: audit-log</span>

<span class="dg-blue">Queue: errors</span>   ──►  <span class="dg-red">Consumer A</span>  (ACK → message deleted)
                 └──►  <span class="dg-gray">DLX → dead-letter-queue</span>  (NACK/TTL expired)
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🔀 Exchange Types</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Type</th><th>Routing Logic</th></tr></thead>
        <tbody>
          <tr><td><strong>direct</strong></td><td>Exact routing key match — one queue per key</td></tr>
          <tr><td><strong>topic</strong></td><td>Pattern match: <code>*</code> (one word) / <code>#</code> (zero+). e.g. <code>order.*.created</code></td></tr>
          <tr><td><strong>fanout</strong></td><td>Ignores routing key — copies to ALL bound queues</td></tr>
          <tr><td><strong>headers</strong></td><td>Match on message headers (key-value), ignores routing key</td></tr>
          <tr><td><strong>default</strong></td><td>Built-in direct exchange — routes to queue named = routing key</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="cp p-red">
    <div class="cp-hdr">💀 Dead Letter Exchange (DLX)</div>
    <div class="cp-body">
      Messages are dead-lettered when:
      <ul style="margin:0;padding-left:1.2rem">
        <li>Consumer sends <strong>NACK</strong> with <code>requeue=false</code></li>
        <li>Message <strong>TTL</strong> expires in queue</li>
        <li>Queue length <strong>overflow</strong> (x-max-length)</li>
      </ul>
      Dead-lettered messages go to the DLX (if configured), enabling:
      <ul style="margin:0;padding-left:1.2rem;margin-top:.4rem">
        <li>Retry queues with exponential backoff (TTL + DLX chain)</li>
        <li>Poison message parking for inspection</li>
        <li>Alerting on repeated failures</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🔁 Retry with Exponential Backoff via DLX Chain</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* Declare retry queue with TTL + DLX pointing back to main exchange */</span>
<span class="cm">/* main queue */</span>
amqp_queue_declare(ch, <span class="cn">1</span>, amqp_cstring_bytes(<span class="cv">"orders"</span>), ...);

<span class="cm">/* retry-30s: TTL=30000ms, dead-letter back to "orders-exchange" */</span>
amqp_table_entry_t args[<span class="cn">2</span>] = {
  { amqp_cstring_bytes(<span class="cv">"x-message-ttl"</span>),
    { .kind = AMQP_FIELD_KIND_I32, .value.i32 = <span class="cn">30000</span> } },
  { amqp_cstring_bytes(<span class="cv">"x-dead-letter-exchange"</span>),
    { .kind = AMQP_FIELD_KIND_BYTES,
      .value.bytes = amqp_cstring_bytes(<span class="cv">"orders-exchange"</span>) } }
};
amqp_table_t tbl = { .num_entries = <span class="cn">2</span>, .entries = args };
amqp_queue_declare(ch, <span class="cn">1</span>,
    amqp_cstring_bytes(<span class="cv">"orders.retry.30s"</span>),
    <span class="cn">0</span>, <span class="cn">1</span>, <span class="cn">0</span>, <span class="cn">0</span>, tbl);</div>
    <div class="note">Pattern: main queue → failure → NACK → DLX(retry-5s) → TTL expires → DLX(retry-30s) → DLX(retry-5m) → DLX(dead-letter-final). Each level doubles the delay — classic exponential backoff without consumer sleep loops.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">⚖️ Consumer ACK Modes</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Mode</th><th>Behavior</th><th>Risk</th></tr></thead>
      <tbody>
        <tr><td><code>autoAck=true</code></td><td>Broker removes message as soon as delivered (at-most-once)</td><td>Lost if consumer crashes before processing</td></tr>
        <tr><td>Manual <strong>ACK</strong></td><td>Consumer confirms success; broker removes message</td><td>None — correct at-least-once</td></tr>
        <tr><td>Manual <strong>NACK</strong> requeue=true</td><td>Message returned to front of queue</td><td>Infinite loop on poison messages</td></tr>
        <tr><td>Manual <strong>NACK</strong> requeue=false</td><td>Message sent to DLX (if configured) or dropped</td><td>Dropped if no DLX</td></tr>
        <tr><td><strong>Reject</strong></td><td>Same as NACK for single message</td><td>—</td></tr>
      </tbody>
    </table>
    <div class="ins"><strong>prefetch count</strong> (<code>basicQos</code>): limits unacked messages per consumer. Set to 1 for strict round-robin fairness; increase (e.g. 20–100) for throughput when processing is fast.</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🆚 Kafka vs RabbitMQ — When to Use Which</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Criterion</th><th>Use Kafka</th><th>Use RabbitMQ</th></tr></thead>
      <tbody>
        <tr><td>Message retention</td><td>Need replay / audit log</td><td>Process-and-forget</td></tr>
        <tr><td>Multiple consumers</td><td>Independent consumer groups reading same events</td><td>One consumer per message (competing consumers)</td></tr>
        <tr><td>Ordering</td><td>Strict ordering per key (partition)</td><td>Best-effort (priority queues)</td></tr>
        <tr><td>Throughput</td><td>Millions of msg/sec (sequential disk I/O)</td><td>Tens of thousands/sec</td></tr>
        <tr><td>Routing complexity</td><td>Simple (partition key)</td><td>Rich (exchange types, header matching)</td></tr>
        <tr><td>RPC / request-reply</td><td>Awkward</td><td>Built-in (correlation ID + reply-to)</td></tr>
        <tr><td>Stream processing</td><td>Kafka Streams, ksqlDB native</td><td>Needs external framework</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-rabbit -->

<!-- ══════════════════════════════════════════════════════════
     TAB 5 — Saga & Outbox
     ══════════════════════════════════════════════════════════ -->
<div id="t-saga" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">🔄 Distributed Transactions: Why Not 2PC?</div>
  <div class="cp-body">
    Two-Phase Commit (2PC) coordinates distributed transactions but has critical problems: the coordinator is a <strong>single point of failure</strong>, participants hold locks during phase 1 (blocking), and the protocol is <strong>blocking</strong> — a coordinator crash leaves participants in limbo. In a microservices system spanning multiple databases and services, 2PC is impractical.
    <br><br>
    The <strong>Saga pattern</strong> replaces distributed ACID transactions with a sequence of local transactions, each publishing an event. If a step fails, <strong>compensating transactions</strong> undo the completed steps.
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🎭 Orchestration Saga</div>
    <div class="cp-body">
      A central <strong>Saga Orchestrator</strong> sends commands and receives events, maintaining the state machine.
      <div class="diagram-box" style="margin:.5rem 0;font-size:.7rem">
<span class="dg-cyan">Orchestrator</span>
     │─[ReserveInventory]──► <span class="dg-blue">Inventory Svc</span>
     │◄─[InventoryReserved]──┘
     │─[ChargePayment]──────► <span class="dg-green">Payment Svc</span>
     │◄─[PaymentFailed]──────┘  <span class="dg-red">← failure!</span>
     │─[ReleaseInventory]───► <span class="dg-blue">Inventory Svc</span>  <span class="dg-gray">compensation</span>
      </div>
      <strong>Pros:</strong> easy to trace, centralized state, clear compensations<br>
      <strong>Cons:</strong> orchestrator = potential SPOF; logic centralized may become god object
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">💃 Choreography Saga</div>
    <div class="cp-body">
      No central coordinator — each service listens for events and emits new events.
      <div class="diagram-box" style="margin:.5rem 0;font-size:.7rem">
<span class="dg-cyan">Order Svc</span> emits [OrderCreated]
     ▼
<span class="dg-blue">Inventory Svc</span> listens → reserves → emits [InventoryReserved]
     ▼
<span class="dg-green">Payment Svc</span> listens → charges → emits [PaymentFailed]
     ▼
<span class="dg-blue">Inventory Svc</span> listens → releases → emits [InventoryReleased]
<span class="dg-cyan">Order Svc</span> listens → marks order failed
      </div>
      <strong>Pros:</strong> decentralized, services fully independent<br>
      <strong>Cons:</strong> hard to understand overall flow; compensations scattered across services
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📤 Outbox Pattern — Atomic DB Write + Event Publish</div>
  <div class="cp-body">
    <strong>Problem:</strong> you write to the database and then publish to Kafka. What if the process crashes between the two operations? The DB write committed but the event never published → downstream services miss the event → <strong>distributed inconsistency</strong>.
    <br><br>
    <strong>Solution:</strong> write to an <code>outbox</code> table in the <strong>same local transaction</strong> as the business data. A separate relay process publishes outbox records to the broker and marks them as sent.
  </div>
</div>

<div class="diagram-box">
<span class="dg-cyan">Business Transaction</span>  (atomic, single DB)
  ┌─────────────────────────────────────────────┐
  │  INSERT INTO orders (id, …)                 │
  │  INSERT INTO outbox (event_type, payload,   │
  │                      status='PENDING')      │  ← same txn!
  └─────────────────────────────────────────────┘

<span class="dg-blue">Relay Process</span>  (separate, runs continuously)
  SELECT * FROM outbox WHERE status='PENDING' LIMIT 100
  FOR EACH row:
    publish to Kafka/RabbitMQ
    UPDATE outbox SET status='SENT', sent_at=NOW() WHERE id=row.id

<span class="dg-gray">Alternatives to polling relay:</span>
  <span class="dg-green">CDC (Change Data Capture)</span> via Debezium — reads DB WAL log directly,
  zero-latency, no polling overhead, works with Postgres/MySQL logical replication
</div>

<div class="cp p-red">
  <div class="cp-hdr">⚠️ Outbox: Failure Modes and Guarantees</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Failure</th><th>Outcome</th><th>Why Safe</th></tr></thead>
      <tbody>
        <tr><td>Process crashes after DB write, before relay runs</td><td>Relay picks up PENDING row on restart</td><td>Row persists in outbox</td></tr>
        <tr><td>Relay publishes to Kafka but crashes before marking SENT</td><td>Relay re-publishes on restart → duplicate</td><td>Consumer must be idempotent</td></tr>
        <tr><td>DB transaction rolled back</td><td>Outbox row never created → no event</td><td>Atomicity maintained</td></tr>
        <tr><td>Kafka broker down during relay</td><td>Relay retries; PENDING rows accumulate</td><td>Broker recovery unblocks relay</td></tr>
      </tbody>
    </table>
    <div class="note">The Outbox pattern provides <strong>at-least-once</strong> delivery. To prevent business harm from duplicates, combine with idempotent consumers (Tab 7).</div>
  </div>
</div>

</div><!-- /t-saga -->

<!-- ══════════════════════════════════════════════════════════
     TAB 6 — CQRS & Event Sourcing
     ══════════════════════════════════════════════════════════ -->
<div id="t-cqrs" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">✂️ CQRS — Command Query Responsibility Segregation</div>
  <div class="cp-body">
    Traditional CRUD uses one model for reads and writes. As systems scale, reads and writes have very different access patterns: writes need normalized data for integrity; reads need denormalized projections for performance.
    <br><br>
    CQRS separates them into two explicit models:
    <ul>
      <li><strong>Command side:</strong> mutates state, normalized DB optimized for writes and integrity (e.g., PostgreSQL with foreign keys)</li>
      <li><strong>Query side:</strong> returns projections, denormalized read model optimized for queries (e.g., Elasticsearch, Redis, materialized views)</li>
    </ul>
  </div>
</div>

<div class="diagram-box">
<span class="dg-purple">Client</span>
  │
  ├──[Command: PlaceOrder(items)]──► <span class="dg-cyan">Command Handler</span>
  │                                        │
  │                                        ▼
  │                               <span class="dg-blue">Write DB (PostgreSQL)</span>
  │                               orders, order_items, inventory
  │                                        │
  │                               [Domain Event: OrderPlaced]
  │                                        │
  │                          ┌─────────────┼───────────────┐
  │                          ▼             ▼               ▼
  │                   <span class="dg-green">Read DB</span>     <span class="dg-amber">Search Index</span>  <span class="dg-red">Analytics DB</span>
  │                (denormalized   (Elasticsearch)  (ClickHouse)
  │                 order view)
  │
  └──[Query: GetOrderSummary(userId)]──► <span class="dg-green">Query Handler</span>
                                               │
                                               ▼
                                       <span class="dg-green">Read DB (fast!)</span>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">✅ CQRS Benefits</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Read model can be independently scaled (horizontal replicas)</li>
        <li>Read model optimized for each query pattern (denormalized)</li>
        <li>Write model optimized for correctness (normalized, transactions)</li>
        <li>Multiple specialized read models from the same events</li>
        <li>Replay events to rebuild read models after bugs</li>
      </ul>
    </div>
  </div>
  <div class="cp p-red">
    <div class="cp-hdr">⚠️ CQRS Trade-offs</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Eventual consistency:</strong> read model lags behind writes (typically milliseconds)</li>
        <li>Additional infrastructure (separate read store)</li>
        <li>Synchronization complexity (events must be reliably published)</li>
        <li>Read-your-own-writes: a user who just placed an order may see stale data on immediate reload → handle with version tokens or direct write-model reads for the write's own session</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">📜 Event Sourcing — State as Event Log</div>
  <div class="cp-body">
    Instead of storing the <em>current state</em>, store the <em>sequence of events</em> that led to the current state. Current state is derived by replaying events.
    <br><br>
    <strong>Normal CRUD:</strong> <code>accounts: {id:1, balance:850}</code><br>
    <strong>Event Sourced:</strong>
<div class="cb"><span class="cm">event_log (account_id=1):</span>
<span class="cv">AccountOpened</span>   { amount: <span class="cn">1000</span> }   <span class="cm">// balance → 1000</span>
<span class="cv">MoneyWithdrawn</span>  { amount: <span class="cn">200</span> }   <span class="cm">// balance → 800</span>
<span class="cv">InterestEarned</span>  { amount: <span class="cn">50</span> }    <span class="cm">// balance → 850</span>
<span class="cm">// replay → current balance = 850</span></div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-amber">
    <div class="cp-hdr">📸 Snapshots</div>
    <div class="cp-body">
      Replaying 10 years of events on every read is slow. <strong>Snapshots</strong> periodically capture current state:
      <ul style="margin:0;padding-left:1.2rem">
        <li>Every N events, save a snapshot: <code>{account_id:1, balance:850, version:3}</code></li>
        <li>On read: load latest snapshot, replay events since that snapshot version</li>
        <li>Typical threshold: every 100–1000 events</li>
      </ul>
    </div>
  </div>
  <div class="cp p-violet">
    <div class="cp-hdr">🔄 Schema Evolution</div>
    <div class="cp-body">
      Events are immutable — you can't change past events. Handling schema changes:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Upcasting:</strong> transform old event format to new format at read time</li>
        <li><strong>Versioned events:</strong> <code>MoneyWithdrawn_v1</code> vs <code>MoneyWithdrawn_v2</code></li>
        <li><strong>Additive changes only:</strong> add fields, never remove or rename</li>
        <li>Use Avro/Protobuf with Schema Registry for versioned schemas</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📐 When to Use Event Sourcing (vs When Not To)</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Use Event Sourcing When…</th><th>Avoid When…</th></tr></thead>
      <tbody>
        <tr><td>Complete audit log is required by regulation</td><td>Simple CRUD with no history requirement</td></tr>
        <tr><td>State reconstruction / time-travel debugging needed</td><td>Team unfamiliar with the pattern — steep learning curve</td></tr>
        <tr><td>Multiple read models from the same data</td><td>Queries span multiple aggregates (event sourcing is aggregate-scoped)</td></tr>
        <tr><td>Business domain is naturally event-oriented (banking, order management)</td><td>Simple content management, settings, static data</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-cqrs -->

<!-- ══════════════════════════════════════════════════════════
     TAB 7 — Idempotency
     ══════════════════════════════════════════════════════════ -->
<div id="t-idempotency" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">🔑 Idempotent Consumers: Handling At-Least-Once Delivery</div>
  <div class="cp-body">
    In any reliable messaging system (Kafka with retries, RabbitMQ with NACK+requeue, Outbox relay), messages may be delivered <strong>more than once</strong>. An <strong>idempotent consumer</strong> produces the same result regardless of how many times it processes the same message.
    <br><br>
    Two approaches:
    <ul>
      <li><strong>Natural idempotency:</strong> the operation is inherently idempotent — e.g., <code>SET balance=850</code> vs <code>balance = balance - 200</code>. If the operation can be expressed as an absolute state (upsert), duplicates are safe.</li>
      <li><strong>Deduplication table:</strong> track processed message IDs; reject re-processed messages.</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🗃️ Deduplication Table Pattern</div>
  <div class="cp-body">
    Each message carries a unique <strong>idempotency key</strong> (message ID, event ID, or a business key). The consumer records processed keys in a <code>processed_events</code> table.
<div class="cb"><span class="cm">-- Schema</span>
<span class="ck">CREATE TABLE</span> processed_events (
    event_id   <span class="cv">TEXT</span>        <span class="ck">PRIMARY KEY</span>,
    processed_at <span class="cv">TIMESTAMPTZ</span> <span class="ck">DEFAULT NOW</span>()
);

<span class="cm">-- Atomic check-and-process (PostgreSQL)</span>
<span class="ck">BEGIN</span>;
  <span class="cm">-- Attempt to insert event ID (fails with UNIQUE violation if duplicate)</span>
  <span class="ck">INSERT INTO</span> processed_events (event_id)
  <span class="ck">VALUES</span> ($<span class="cn">1</span>)
  <span class="ck">ON CONFLICT</span> (event_id) <span class="ck">DO NOTHING</span>
  <span class="ck">RETURNING</span> event_id;

  <span class="cm">-- If no row returned: already processed, skip</span>
  <span class="cm">-- If row returned: new event, proceed with business logic</span>
  <span class="ck">UPDATE</span> accounts <span class="ck">SET</span> balance = balance - $<span class="cn">2</span> <span class="ck">WHERE</span> id = $<span class="cn">3</span>;
<span class="ck">COMMIT</span>;</div>
    <div class="note">The <code>INSERT ... ON CONFLICT DO NOTHING</code> + business logic must be in the <strong>same transaction</strong> for atomicity. If the transaction rolls back, the event ID is not recorded and can be safely reprocessed.</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">⚡ Redis-based Deduplication (High Throughput)</div>
  <div class="cp-body">
    For very high throughput, use Redis with a TTL-based dedup set instead of a DB table:
<div class="cb"><span class="cm">/* Check + mark with SETNX (SET if Not eXists) */</span>
<span class="cm">/* Returns 1 if set (new), 0 if already existed (duplicate) */</span>
<span class="cs">int</span> is_new = redis_setnx(r, event_id, <span class="cv">"1"</span>);
<span class="ck">if</span> (is_new) {
    redis_expire(r, event_id, <span class="cn">86400</span>); <span class="cm">/* TTL: 24h — beyond message retention */</span>
    process_event(event);
} <span class="ck">else</span> {
    <span class="cm">/* duplicate: skip */</span>
}</div>
    <div class="warn">Redis dedup is best-effort — Redis can lose data if not persisted (AOF/RDB). For financial events, prefer the database dedup table for durable deduplication.</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">🧠 Designing Idempotency Keys</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Source</th><th>Key Strategy</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td>Kafka messages</td><td><code>topic:partition:offset</code></td><td>Globally unique per message position</td></tr>
        <tr><td>RabbitMQ messages</td><td>Set <code>message-id</code> AMQP property at publish time</td><td>Producer responsibility; use UUID</td></tr>
        <tr><td>Business events</td><td><code>order_id:event_type</code></td><td>Natural key; handles schema-level dedup</td></tr>
        <tr><td>HTTP API calls</td><td>Client-supplied <code>Idempotency-Key</code> header (UUID)</td><td>Store response and return cached result on repeat</td></tr>
      </tbody>
    </table>
    <div class="ins"><strong>TTL management:</strong> set the dedup key TTL longer than your maximum retry window. If retries can span 24h, use 48h TTL. If your Kafka retention is 7 days, set TTL to 8 days.</div>
  </div>
</div>

</div><!-- /t-idempotency -->

<!-- ══════════════════════════════════════════════════════════
     TAB 8 — C Implementation
     ══════════════════════════════════════════════════════════ -->
<div id="t-impl" class="tab-pane">

<div class="cp p-cyan">
  <div class="cp-hdr">🔧 Libraries Used</div>
  <div class="cp-body">
    <ul>
      <li><strong>librdkafka</strong> — official C Kafka client; used by the Python/Go/Ruby clients under the hood</li>
      <li><strong>rabbitmq-c</strong> (amqp.h) — C AMQP 0-9-1 client for RabbitMQ</li>
    </ul>
    <div class="cb"><span class="cm"># Install (Ubuntu)</span>
<span class="ck">apt-get install</span> librdkafka-dev librabbitmq-dev

<span class="cm"># Compile</span>
<span class="ck">gcc</span> -o kafka_producer kafka_producer.c -lrdkafka
<span class="ck">gcc</span> -o amqp_consumer amqp_consumer.c -lrabbitmq</div>
  </div>
</div>

<div class="sep">── Implementation 1 — Kafka Producer with Delivery Reports ──</div>

<div class="cp p-blue">
  <div class="cp-hdr">📤 Kafka Producer (librdkafka) — Full Implementation</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* kafka_producer.c — production-ready Kafka producer */</span>
<span class="cs">#include</span> &lt;librdkafka/rdkafka.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;
<span class="cs">#include</span> &lt;signal.h&gt;

<span class="cs">static volatile</span> <span class="cs">int</span> run = <span class="cn">1</span>;
<span class="ck">static void</span> <span class="cf">sigterm</span>(<span class="cs">int</span> sig) { run = <span class="cn">0</span>; }

<span class="cm">/* Called for every message after produce attempt */</span>
<span class="ck">static void</span> <span class="cf">delivery_report_cb</span>(rd_kafka_t *rk,
                               <span class="cs">const</span> rd_kafka_message_t *msg,
                               <span class="cs">void</span> *opaque) {
    (void)rk; (void)opaque;
    <span class="ck">if</span> (msg-&gt;err) {
        fprintf(stderr, <span class="cv">"[DR] FAILED: topic=%s err=%s key=%.*s\n"</span>,
                rd_kafka_topic_name(msg-&gt;rkt),
                rd_kafka_err2str(msg-&gt;err),
                (<span class="cs">int</span>)msg-&gt;key_len, (<span class="cs">const char</span> *)msg-&gt;key);
    } <span class="ck">else</span> {
        fprintf(stdout, <span class="cv">"[DR] OK: topic=%s partition=%"</span> PRId32
                        <span class="cv">" offset=%"</span> PRId64 <span class="cv">" key=%.*s\n"</span>,
                rd_kafka_topic_name(msg-&gt;rkt),
                msg-&gt;partition, msg-&gt;offset,
                (<span class="cs">int</span>)msg-&gt;key_len, (<span class="cs">const char</span> *)msg-&gt;key);
    }
}

<span class="cs">int</span> <span class="cf">main</span>(<span class="cs">int</span> argc, <span class="cs">char</span> *argv[]) {
    <span class="ck">if</span> (argc &lt; <span class="cn">4</span>) {
        fprintf(stderr, <span class="cv">"Usage: %s &lt;brokers&gt; &lt;topic&gt; &lt;message&gt;\n"</span>, argv[<span class="cn">0</span>]);
        <span class="ck">return</span> <span class="cn">1</span>;
    }

    <span class="cs">char</span> errstr[<span class="cn">512</span>];
    rd_kafka_conf_t *conf = rd_kafka_conf_new();

    <span class="cm">/* Broker list */</span>
    <span class="ck">if</span> (rd_kafka_conf_set(conf, <span class="cv">"bootstrap.servers"</span>, argv[<span class="cn">1</span>],
                          errstr, <span class="ck">sizeof</span>(errstr)) != RD_KAFKA_CONF_OK) {
        fprintf(stderr, <span class="cv">"%s\n"</span>, errstr);
        <span class="ck">return</span> <span class="cn">1</span>;
    }

    <span class="cm">/* Idempotent producer: deduplicates retries automatically */</span>
    rd_kafka_conf_set(conf, <span class="cv">"enable.idempotence"</span>, <span class="cv">"true"</span>, errstr, <span class="ck">sizeof</span>(errstr));

    <span class="cm">/* Delivery callback for per-message success/failure reporting */</span>
    rd_kafka_conf_set_dr_msg_cb(conf, delivery_report_cb);

    rd_kafka_t *rk = rd_kafka_new(RD_KAFKA_PRODUCER, conf,
                                  errstr, <span class="ck">sizeof</span>(errstr));
    <span class="ck">if</span> (!rk) {
        fprintf(stderr, <span class="cv">"Failed to create producer: %s\n"</span>, errstr);
        <span class="ck">return</span> <span class="cn">1</span>;
    }

    <span class="cs">const char</span> *topic = argv[<span class="cn">2</span>];
    <span class="cs">const char</span> *msg   = argv[<span class="cn">3</span>];
    <span class="cs">const char</span> *key   = <span class="cv">"order-key-001"</span>;  <span class="cm">/* determines partition */</span>

    signal(SIGINT, sigterm);
    signal(SIGTERM, sigterm);

retry_produce:
    <span class="cs">rd_kafka_resp_err_t</span> err = rd_kafka_producev(
        rk,
        RD_KAFKA_V_TOPIC(topic),
        RD_KAFKA_V_MSGFLAGS(RD_KAFKA_MSG_F_COPY),
        RD_KAFKA_V_KEY(key, strlen(key)),
        RD_KAFKA_V_VALUE((<span class="cs">void</span> *)msg, strlen(msg)),
        RD_KAFKA_V_OPAQUE(NULL),
        RD_KAFKA_V_END
    );

    <span class="ck">if</span> (err) {
        fprintf(stderr, <span class="cv">"Produce failed: %s\n"</span>, rd_kafka_err2str(err));
        <span class="ck">if</span> (err == RD_KAFKA_RESP_ERR__QUEUE_FULL) {
            rd_kafka_poll(rk, <span class="cn">1000</span>);  <span class="cm">/* drain delivery queue, then retry */</span>
            <span class="ck">goto</span> retry_produce;
        }
    }

    <span class="cm">/* Poll for delivery reports (fires delivery_report_cb) */</span>
    rd_kafka_poll(rk, <span class="cn">0</span>);  <span class="cm">/* non-blocking poll */</span>

    <span class="cm">/* Wait for all outstanding messages to be delivered */</span>
    fprintf(stdout, <span class="cv">"Flushing...\n"</span>);
    rd_kafka_flush(rk, <span class="cn">10</span> * <span class="cn">1000</span>);  <span class="cm">/* wait up to 10s */</span>

    <span class="ck">if</span> (rd_kafka_outq_len(rk) &gt; <span class="cn">0</span>)
        fprintf(stderr, <span class="cv">"%d message(s) not delivered\n"</span>,
                rd_kafka_outq_len(rk));

    rd_kafka_destroy(rk);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="sep">── Implementation 2 — Kafka Consumer with Manual Offset Commit ──</div>

<div class="cp p-teal">
  <div class="cp-hdr">📥 Kafka Consumer (librdkafka) — At-Least-Once with Manual Commit</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* kafka_consumer.c — manual offset commit consumer */</span>
<span class="cs">#include</span> &lt;librdkafka/rdkafka.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;

<span class="cs">static volatile</span> <span class="cs">int</span> run = <span class="cn">1</span>;

<span class="ck">static void</span> <span class="cf">rebalance_cb</span>(rd_kafka_t *rk, rd_kafka_resp_err_t err,
                          rd_kafka_topic_partition_list_t *parts,
                          <span class="cs">void</span> *opaque) {
    <span class="ck">switch</span> (err) {
    <span class="ck">case</span> RD_KAFKA_RESP_ERR__ASSIGN_PARTITIONS:
        fprintf(stdout, <span class="cv">"Rebalance: assigned %d partitions\n"</span>, parts-&gt;cnt);
        rd_kafka_assign(rk, parts);
        <span class="ck">break</span>;
    <span class="ck">case</span> RD_KAFKA_RESP_ERR__REVOKE_PARTITIONS:
        fprintf(stdout, <span class="cv">"Rebalance: revoking partitions, committing offsets\n"</span>);
        rd_kafka_commit(rk, parts, <span class="cn">0</span>);  <span class="cm">/* sync commit before revoke */</span>
        rd_kafka_assign(rk, NULL);
        <span class="ck">break</span>;
    <span class="ck">default</span>:
        rd_kafka_assign(rk, NULL);
        <span class="ck">break</span>;
    }
}

<span class="cs">int</span> <span class="cf">main</span>(<span class="cs">int</span> argc, <span class="cs">char</span> *argv[]) {
    <span class="ck">if</span> (argc &lt; <span class="cn">4</span>) {
        fprintf(stderr, <span class="cv">"Usage: %s &lt;brokers&gt; &lt;group&gt; &lt;topic&gt;\n"</span>, argv[<span class="cn">0</span>]);
        <span class="ck">return</span> <span class="cn">1</span>;
    }

    <span class="cs">char</span> errstr[<span class="cn">512</span>];
    rd_kafka_conf_t *conf = rd_kafka_conf_new();
    rd_kafka_conf_set(conf, <span class="cv">"bootstrap.servers"</span>, argv[<span class="cn">1</span>], errstr, <span class="ck">sizeof</span>(errstr));
    rd_kafka_conf_set(conf, <span class="cv">"group.id"</span>,           argv[<span class="cn">2</span>], errstr, <span class="ck">sizeof</span>(errstr));
    rd_kafka_conf_set(conf, <span class="cv">"auto.offset.reset"</span>,   <span class="cv">"earliest"</span>, errstr, <span class="ck">sizeof</span>(errstr));
    <span class="cm">/* Disable auto-commit: we commit manually after processing */</span>
    rd_kafka_conf_set(conf, <span class="cv">"enable.auto.commit"</span>,  <span class="cv">"false"</span>, errstr, <span class="ck">sizeof</span>(errstr));
    rd_kafka_conf_set_rebalance_cb(conf, rebalance_cb);

    rd_kafka_t *rk = rd_kafka_new(RD_KAFKA_CONSUMER, conf, errstr, <span class="ck">sizeof</span>(errstr));
    rd_kafka_poll_set_consumer(rk);

    <span class="cm">/* Subscribe to topic */</span>
    rd_kafka_topic_partition_list_t *topics =
        rd_kafka_topic_partition_list_new(<span class="cn">1</span>);
    rd_kafka_topic_partition_list_add(topics, argv[<span class="cn">3</span>], RD_KAFKA_PARTITION_UA);
    rd_kafka_subscribe(rk, topics);
    rd_kafka_topic_partition_list_destroy(topics);

    <span class="cs">int</span> msg_count = <span class="cn">0</span>;
    <span class="ck">while</span> (run) {
        rd_kafka_message_t *msg = rd_kafka_consumer_poll(rk, <span class="cn">1000</span>);
        <span class="ck">if</span> (!msg) <span class="ck">continue</span>;

        <span class="ck">if</span> (msg-&gt;err) {
            <span class="ck">if</span> (msg-&gt;err == RD_KAFKA_RESP_ERR__PARTITION_EOF)
                fprintf(stdout, <span class="cv">"Reached end of partition\n"</span>);
            <span class="ck">else</span>
                fprintf(stderr, <span class="cv">"Consumer error: %s\n"</span>, rd_kafka_message_errstr(msg));
        } <span class="ck">else</span> {
            <span class="cm">/* Process message */</span>
            fprintf(stdout, <span class="cv">"Message: partition=%"</span> PRId32
                            <span class="cv">" offset=%"</span> PRId64 <span class="cv">" key=%.*s value=%.*s\n"</span>,
                    msg-&gt;partition, msg-&gt;offset,
                    (<span class="cs">int</span>)msg-&gt;key_len,    (<span class="cs">const char</span> *)msg-&gt;key,
                    (<span class="cs">int</span>)msg-&gt;len,        (<span class="cs">const char</span> *)msg-&gt;payload);

            <span class="cm">/* TODO: process_message(msg->payload, msg->len); */</span>

            <span class="cm">/* Commit offset after successful processing (at-least-once) */</span>
            <span class="ck">if</span> (++msg_count % <span class="cn">100</span> == <span class="cn">0</span>) {
                <span class="cm">/* Sync commit every 100 messages for durability */</span>
                rd_kafka_commit_message(rk, msg, <span class="cm">/*async=*/</span><span class="cn">0</span>);
            }
        }

        rd_kafka_message_destroy(msg);
    }

    <span class="cm">/* Final commit before shutdown */</span>
    rd_kafka_commit(rk, NULL, <span class="cn">0</span>);
    rd_kafka_consumer_close(rk);
    rd_kafka_destroy(rk);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="sep">── Implementation 3 — RabbitMQ Consumer with DLX (rabbitmq-c) ──</div>

<div class="cp p-orange">
  <div class="cp-hdr">🐰 RabbitMQ Consumer with Dead-Letter Exchange (rabbitmq-c)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* amqp_consumer.c — RabbitMQ consumer with manual ACK and DLX */</span>
<span class="cs">#include</span> &lt;amqp.h&gt;
<span class="cs">#include</span> &lt;amqp_tcp_socket.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;

<span class="ck">static void</span> <span class="cf">die_on_amqp_error</span>(amqp_rpc_reply_t x, <span class="cs">const char</span> *context) {
    <span class="ck">if</span> (x.reply_type != AMQP_RESPONSE_NORMAL) {
        fprintf(stderr, <span class="cv">"%s: AMQP error\n"</span>, context);
        exit(<span class="cn">1</span>);
    }
}

<span class="cs">int</span> <span class="cf">main</span>() {
    amqp_connection_state_t conn = amqp_new_connection();
    amqp_socket_t *socket = amqp_tcp_socket_new(conn);
    amqp_tcp_socket_open(socket, <span class="cv">"localhost"</span>, <span class="cn">5672</span>, NULL);
    die_on_amqp_error(
        amqp_login(conn, <span class="cv">"/"</span>, <span class="cn">0</span>, <span class="cn">131072</span>, <span class="cn">0</span>,
                   AMQP_SASL_METHOD_PLAIN, <span class="cv">"guest"</span>, <span class="cv">"guest"</span>),
        <span class="cv">"Login"</span>);

    amqp_channel_open(conn, <span class="cn">1</span>);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Open channel"</span>);

    <span class="cm">/* Declare dead-letter exchange */</span>
    amqp_exchange_declare(conn, <span class="cn">1</span>,
        amqp_cstring_bytes(<span class="cv">"dlx.orders"</span>),
        amqp_cstring_bytes(<span class="cv">"fanout"</span>),
        <span class="cn">0</span>, <span class="cn">1</span>, <span class="cn">0</span>, <span class="cn">0</span>, amqp_empty_table);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Declare DLX"</span>);

    <span class="cm">/* Declare dead-letter queue */</span>
    amqp_queue_declare(conn, <span class="cn">1</span>,
        amqp_cstring_bytes(<span class="cv">"orders.dead-letter"</span>),
        <span class="cn">0</span>, <span class="cn">1</span>, <span class="cn">0</span>, <span class="cn">0</span>, amqp_empty_table);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Declare DLQ"</span>);

    amqp_queue_bind(conn, <span class="cn">1</span>,
        amqp_cstring_bytes(<span class="cv">"orders.dead-letter"</span>),
        amqp_cstring_bytes(<span class="cv">"dlx.orders"</span>),
        amqp_cstring_bytes(<span class="cv">""</span>), amqp_empty_table);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Bind DLQ"</span>);

    <span class="cm">/* Declare main queue with DLX configured */</span>
    amqp_table_entry_t dlx_arg = {
        .key = amqp_cstring_bytes(<span class="cv">"x-dead-letter-exchange"</span>),
        .value = {
            .kind = AMQP_FIELD_KIND_UTF8,
            .value.bytes = amqp_cstring_bytes(<span class="cv">"dlx.orders"</span>)
        }
    };
    amqp_table_t dlx_args = { .num_entries = <span class="cn">1</span>, .entries = &amp;dlx_arg };
    amqp_queue_declare(conn, <span class="cn">1</span>,
        amqp_cstring_bytes(<span class="cv">"orders"</span>),
        <span class="cn">0</span>, <span class="cn">1</span>, <span class="cn">0</span>, <span class="cn">0</span>, dlx_args);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Declare orders queue"</span>);

    <span class="cm">/* Set prefetch count — process 10 at a time */</span>
    amqp_basic_qos(conn, <span class="cn">1</span>, <span class="cn">0</span>, <span class="cn">10</span>, <span class="cn">0</span>);

    <span class="cm">/* Start consuming (no-ack=false: manual ACK mode) */</span>
    amqp_basic_consume(conn, <span class="cn">1</span>,
        amqp_cstring_bytes(<span class="cv">"orders"</span>),
        amqp_empty_bytes,
        <span class="cn">0</span>, <span class="cn">0</span> <span class="cm">/*no_ack=false*/</span>, <span class="cn">0</span>, amqp_empty_table);
    die_on_amqp_error(amqp_get_rpc_reply(conn), <span class="cv">"Consume"</span>);

    <span class="ck">while</span> (<span class="cn">1</span>) {
        amqp_envelope_t envelope;
        amqp_maybe_release_buffers(conn);
        amqp_rpc_reply_t res = amqp_consume_message(conn, &amp;envelope, NULL, <span class="cn">0</span>);
        <span class="ck">if</span> (res.reply_type != AMQP_RESPONSE_NORMAL) <span class="ck">break</span>;

        fprintf(stdout, <span class="cv">"Delivery tag: %"</span> PRIu64 <span class="cv">" body: %.*s\n"</span>,
                envelope.delivery_tag,
                (<span class="cs">int</span>)envelope.message.body.len,
                (<span class="cs">const char</span> *)envelope.message.body.bytes);

        <span class="cs">int</span> success = <span class="cn">1</span>;  <span class="cm">/* TODO: replace with actual processing */</span>
        <span class="ck">if</span> (success) {
            <span class="cm">/* ACK: remove from queue */</span>
            amqp_basic_ack(conn, <span class="cn">1</span>, envelope.delivery_tag, <span class="cn">0</span>);
        } <span class="ck">else</span> {
            <span class="cm">/* NACK + requeue=false: sends to DLX */</span>
            amqp_basic_nack(conn, <span class="cn">1</span>, envelope.delivery_tag, <span class="cn">0</span>, <span class="cn">0</span>);
        }

        amqp_destroy_envelope(&amp;envelope);
    }

    amqp_channel_close(conn, <span class="cn">1</span>, AMQP_REPLY_SUCCESS);
    amqp_connection_close(conn, AMQP_REPLY_SUCCESS);
    amqp_destroy_connection(conn);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="sep">── Implementation 4 — Outbox Relay (libpq) ──</div>

<div class="cp p-purple">
  <div class="cp-hdr">📤 Outbox Relay: PostgreSQL → Kafka (libpq + librdkafka)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* outbox_relay.c — polls outbox table and publishes to Kafka */</span>
<span class="cs">#include</span> &lt;libpq-fe.h&gt;
<span class="cs">#include</span> &lt;librdkafka/rdkafka.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;unistd.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;

<span class="cs">#define</span> BATCH_SIZE <span class="cn">100</span>
<span class="cs">#define</span> POLL_INTERVAL_MS <span class="cn">100</span>

<span class="cs">typedef struct</span> {
    PGconn      *pg;
    rd_kafka_t  *rk;
    rd_kafka_topic_t *rkt;
} relay_ctx_t;

<span class="ck">static void</span> <span class="cf">relay_batch</span>(relay_ctx_t *ctx) {
    <span class="cm">/* Fetch pending outbox rows */</span>
    PGresult *res = PQexec(ctx-&gt;pg,
        <span class="cv">"SELECT id, event_type, payload FROM outbox "</span>
        <span class="cv">"WHERE status = 'PENDING' ORDER BY created_at LIMIT "</span>
        BATCH_SIZE_STR <span class="cv">" FOR UPDATE SKIP LOCKED"</span>);

    <span class="ck">if</span> (PQresultStatus(res) != PGRES_TUPLES_OK) {
        fprintf(stderr, <span class="cv">"Query failed: %s\n"</span>, PQerrorMessage(ctx-&gt;pg));
        PQclear(res);
        <span class="ck">return</span>;
    }

    <span class="cs">int</span> rows = PQntuples(res);
    <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; i &lt; rows; i++) {
        <span class="cs">const char</span> *id         = PQgetvalue(res, i, <span class="cn">0</span>);
        <span class="cs">const char</span> *event_type = PQgetvalue(res, i, <span class="cn">1</span>);
        <span class="cs">const char</span> *payload    = PQgetvalue(res, i, <span class="cn">2</span>);

        <span class="cm">/* Produce to Kafka (fire-and-forget here; use delivery callback for ACK) */</span>
        rd_kafka_produce(ctx-&gt;rkt,
            RD_KAFKA_PARTITION_UA,
            RD_KAFKA_MSG_F_COPY,
            (<span class="cs">void</span> *)payload, strlen(payload),
            event_type, strlen(event_type),
            NULL);

        <span class="cm">/* Mark as sent in same connection (no distributed txn needed: </span>
<span class="cm">           at-least-once — may re-publish if crash here before UPDATE) */</span>
        <span class="cs">const char</span> *params[<span class="cn">1</span>] = { id };
        PQexecParams(ctx-&gt;pg,
            <span class="cv">"UPDATE outbox SET status='SENT', sent_at=NOW() WHERE id=$1"</span>,
            <span class="cn">1</span>, NULL, params, NULL, NULL, <span class="cn">0</span>);
    }

    PQclear(res);
    rd_kafka_flush(ctx-&gt;rk, <span class="cn">5000</span>);
}

<span class="cs">int</span> <span class="cf">main</span>() {
    relay_ctx_t ctx;
    <span class="cs">char</span> errstr[<span class="cn">512</span>];

    ctx.pg = PQconnectdb(<span class="cv">"host=localhost dbname=myapp user=relay_user"</span>);
    <span class="ck">if</span> (PQstatus(ctx.pg) != CONNECTION_OK) {
        fprintf(stderr, <span class="cv">"PG connect failed: %s\n"</span>, PQerrorMessage(ctx.pg));
        <span class="ck">return</span> <span class="cn">1</span>;
    }

    rd_kafka_conf_t *conf = rd_kafka_conf_new();
    rd_kafka_conf_set(conf, <span class="cv">"bootstrap.servers"</span>, <span class="cv">"localhost:9092"</span>,
                      errstr, <span class="ck">sizeof</span>(errstr));
    rd_kafka_conf_set(conf, <span class="cv">"enable.idempotence"</span>, <span class="cv">"true"</span>, errstr, <span class="ck">sizeof</span>(errstr));
    ctx.rk  = rd_kafka_new(RD_KAFKA_PRODUCER, conf, errstr, <span class="ck">sizeof</span>(errstr));
    ctx.rkt = rd_kafka_topic_new(ctx.rk, <span class="cv">"domain-events"</span>, NULL);

    fprintf(stdout, <span class="cv">"Outbox relay started\n"</span>);
    <span class="ck">while</span> (<span class="cn">1</span>) {
        relay_batch(&amp;ctx);
        usleep(POLL_INTERVAL_MS * <span class="cn">1000</span>);
    }
}</div>
    <div class="note"><strong>FOR UPDATE SKIP LOCKED:</strong> if running multiple relay processes for redundancy, this PostgreSQL clause ensures each row is only processed by one relay at a time — no duplicate publications from concurrent relays.</div>
  </div>
</div>

</div><!-- /t-impl -->

<!-- ══════════════════════════════════════════════════════════
     TAB 9 — Labs & Checklist
     ══════════════════════════════════════════════════════════ -->
<div id="t-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 1 — Kafka Producer / Consumer Pipeline with Delivery Guarantees</div>
  <div class="lab-body">
    Build a Kafka pipeline and observe the behavior of different delivery semantics.
    <div class="lab-step"><span class="sn">1</span> Start Kafka locally: <code>docker compose up kafka zookeeper</code>. Create topic <code>events</code> with 3 partitions, replication-factor 1.</div>
    <div class="lab-step"><span class="sn">2</span> Write a producer using librdkafka with <code>enable.idempotence=true</code>. Send 10,000 messages with keys <code>user-{i%100}</code> (100 distinct keys).</div>
    <div class="lab-step"><span class="sn">3</span> Observe partition distribution: messages with the same key always go to the same partition. Verify with <code>kafka-console-consumer --partition</code> output.</div>
    <div class="lab-step"><span class="sn">4</span> Write two consumer processes in the same group. Start both. Observe partition rebalancing in logs when the second consumer joins.</div>
    <div class="lab-step"><span class="sn">5</span> Kill one consumer mid-stream. Observe rebalance and that the surviving consumer picks up all partitions and continues from the committed offset (not the beginning).</div>
    <div class="lab-step"><span class="sn">6</span> <strong>Bonus:</strong> write a transactional producer that sends batches of 10 messages atomically. Verify with <code>isolation.level=read_committed</code> consumer that aborted batches are not visible.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 2 — RabbitMQ Dead-Letter Exchange Chain</div>
  <div class="lab-body">
    Build a retry-with-backoff pipeline using DLX chaining.
    <div class="lab-step"><span class="sn">1</span> Start RabbitMQ: <code>docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management</code>. Open management UI at <code>http://localhost:15672</code>.</div>
    <div class="lab-step"><span class="sn">2</span> Declare the following chain using rabbitmq-c or the management UI:
      <ul>
        <li><code>orders</code> queue → DLX: <code>retry-exchange</code></li>
        <li><code>orders.retry.5s</code> queue → TTL: 5000ms → DLX: <code>orders-exchange</code> (routes back to <code>orders</code>)</li>
        <li><code>orders.dead-final</code> queue for permanently failed messages (retry limit exceeded)</li>
      </ul>
    </div>
    <div class="lab-step"><span class="sn">3</span> Write a consumer that processes messages. Increment a retry count header. After 3 retries, NACK to final dead-letter queue. Otherwise NACK to retry queue.</div>
    <div class="lab-step"><span class="sn">4</span> Publish 10 messages. Fail the first 3 (to trigger retries). Verify in management UI that messages move through the retry chain with 5s delay.</div>
    <div class="lab-step"><span class="sn">5</span> <strong>Bonus:</strong> modify retry delay to be exponential: 5s → 30s → 5m using three distinct retry queues.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 3 — Outbox Pattern with PostgreSQL + Kafka</div>
  <div class="lab-body">
    Demonstrate atomic event publishing using the Outbox pattern.
    <div class="lab-step"><span class="sn">1</span> Create PostgreSQL tables:
<div class="cb"><span class="ck">CREATE TABLE</span> orders (id <span class="cv">SERIAL PRIMARY KEY</span>, customer_id <span class="cv">INT</span>, amount <span class="cv">NUMERIC</span>);
<span class="ck">CREATE TABLE</span> outbox (
    id         <span class="cv">UUID PRIMARY KEY DEFAULT gen_random_uuid()</span>,
    event_type <span class="cv">TEXT NOT NULL</span>,
    payload    <span class="cv">JSONB NOT NULL</span>,
    status     <span class="cv">TEXT NOT NULL DEFAULT 'PENDING'</span>,
    created_at <span class="cv">TIMESTAMPTZ DEFAULT NOW()</span>,
    sent_at    <span class="cv">TIMESTAMPTZ</span>
);</div>
    </div>
    <div class="lab-step"><span class="sn">2</span> Write a transaction in C (libpq) that inserts an order AND an outbox record atomically. Simulate a crash (call abort() after DB commit) — verify the outbox row persists even though Kafka was never published.</div>
    <div class="lab-step"><span class="sn">3</span> Build the Outbox Relay from Tab 8. Run it — observe it picks up the PENDING row and publishes to Kafka. Verify message arrives in Kafka consumer.</div>
    <div class="lab-step"><span class="sn">4</span> Test the duplicate scenario: manually reset a row to PENDING after it was marked SENT. Run relay again — verify Kafka receives a duplicate. Make the Kafka consumer idempotent using a Redis SETNX dedup check.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 4 — CQRS Read Model Projection</div>
  <div class="lab-body">
    Build a minimal CQRS system: write to PostgreSQL, project events to a Redis read model.
    <div class="lab-step"><span class="sn">1</span> Write model: <code>orders</code> table in PostgreSQL with normalized schema. Each INSERT/UPDATE publishes an event to Kafka topic <code>order-events</code>.</div>
    <div class="lab-step"><span class="sn">2</span> Read model consumer: subscribe to <code>order-events</code>. For each event, upsert a denormalized Redis hash: <code>HSET order:{id} customer_name "..." status "..." total "..."</code>.</div>
    <div class="lab-step"><span class="sn">3</span> Query handler: read from Redis hash for single order lookups. Measure latency vs direct PostgreSQL query under load (use Apache Bench or wrk).</div>
    <div class="lab-step"><span class="sn">4</span> Simulate read model rebuild: delete Redis keys, reset consumer offset to earliest, re-run consumer — verify Redis is repopulated from event history.</div>
    <div class="lab-step"><span class="sn">5</span> <strong>Bonus:</strong> add a "leaderboard" read model: top 10 customers by order total, stored as a Redis sorted set (<code>ZADD</code>). Update on every OrderPlaced event.</div>
  </div>
</div>

<div class="sep">── Phase 5 Mastery Checklist ──</div>

<div class="two-col">
  <div>
    <strong style="color:#0e7490">Kafka</strong>
    <ul class="cl">
      <li>Explain topic, partition, offset, consumer group, ISR</li>
      <li>Describe producer partition assignment: key hash vs round-robin</li>
      <li>Explain rebalance: eager vs cooperative, triggers</li>
      <li>Configure <code>acks=all + min.insync.replicas=2</code> for durability</li>
      <li>Implement idempotent producer with librdkafka</li>
      <li>Implement manual offset commit consumer</li>
      <li>Explain log compaction and when to use it</li>
    </ul>
    <strong style="color:#0e7490">RabbitMQ</strong>
    <ul class="cl">
      <li>Explain the 5 exchange types and when to use each</li>
      <li>Configure dead-letter exchange for failed messages</li>
      <li>Build retry chain with TTL + DLX</li>
      <li>Implement manual ACK/NACK consumer</li>
      <li>Set prefetch count for flow control</li>
    </ul>
  </div>
  <div>
    <strong style="color:#0e7490">Delivery Semantics</strong>
    <ul class="cl">
      <li>Explain at-most-once, at-least-once, exactly-once trade-offs</li>
      <li>Configure idempotent + transactional producer for EOS</li>
      <li>Set <code>isolation.level=read_committed</code> for EOS consumers</li>
    </ul>
    <strong style="color:#0e7490">Patterns</strong>
    <ul class="cl">
      <li>Implement Outbox: atomic DB write + relay process</li>
      <li>Explain Saga orchestration vs choreography trade-offs</li>
      <li>Design CQRS write/read model split for a given domain</li>
      <li>Explain Event Sourcing: replay, snapshots, schema versioning</li>
      <li>Implement idempotent consumer with dedup table (PostgreSQL)</li>
      <li>Design idempotency keys for Kafka, RabbitMQ, HTTP APIs</li>
    </ul>
  </div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/backend/m11-concurrency/' | relative_url }}" class="nb">← M11: Concurrency &amp; Performance</a>
  <a href="{{ '/learning/backend/' | relative_url }}" class="nb">↑ Roadmap</a>
  <a href="{{ '/learning/backend/m15-microservices/' | relative_url }}" class="nb">M15: Microservices →</a>
</div>

</div><!-- /t-labs -->

</div><!-- /mod-wrap -->

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
