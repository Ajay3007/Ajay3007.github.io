---
layout: default
title: High-Level Design (HLD)
permalink: /learning/system-design/hld/
---

# 🏗️ High-Level Design (HLD)

Scale systems to millions of users — networking, databases, caching, message queues, distributed systems, reliability, and full case studies.

<div style="display:flex;gap:1rem;flex-wrap:wrap;margin:1rem 0 2rem;">
  <span style="background:rgba(0,212,170,0.1);color:#00d4aa;border:1px solid rgba(0,212,170,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">Track B · Weeks 3–16</span>
  <span style="background:rgba(245,158,11,0.1);color:#f59e0b;border:1px solid rgba(245,158,11,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">14 Modules · Coming Soon</span>
  <span style="background:rgba(148,163,184,0.1);color:#94a3b8;border:1px solid rgba(148,163,184,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">3 Phases</span>
</div>

---

## Phase B-I — Foundations of Scale (Weeks 3–7)

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B1 · Week 3</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Requirements & API Design</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Functional vs non-functional requirements, capacity estimation, SLIs/SLOs, REST vs gRPC, API versioning and idempotency.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B2 · Week 4</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Networking & Edge</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">DNS, CDN, Load Balancers (L4 vs L7), reverse proxies, WebSockets, long polling, and connection pooling.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B3 · Week 5</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Hardware & Infrastructure</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">CPU, memory, disk I/O trade-offs, vertical vs horizontal scaling, data centers, cloud regions and availability zones.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B4 · Week 6</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Caching Strategies</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Cache-aside, write-through, write-behind; Redis vs Memcached; eviction policies (LRU, LFU); cache stampede prevention.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B5 · Week 7</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Data Store Internals</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">SQL vs NoSQL trade-offs, B-Tree & LSM indexing, WAL, ACID vs BASE, row vs column stores, polyglot persistence.</p>
  </div>

</div>

---

## Phase B-II — Distributed Systems (Weeks 8–12)

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B6 · Week 8</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Databases at Scale</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Replication (leader-follower, multi-leader), sharding strategies (range, hash, directory), consistent hashing, cross-shard queries.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B7 · Week 9</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Message Queues & Kafka</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Async messaging patterns, Kafka architecture (partitions, offsets, consumer groups), at-least-once vs exactly-once, backpressure.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B8 · Week 10</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Distributed Systems Concepts</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">CAP theorem, PACELC, consistency models, Paxos & Raft consensus, vector clocks, distributed transactions (2PC, Saga).</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B9 · Week 11</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Scalability Patterns</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Microservices, API gateway, service mesh, rate limiting (token bucket, leaky bucket), circuit breakers, bulkhead pattern.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B10 · Week 12</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Reliability & Fault Tolerance</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Availability (nines), SLIs/SLOs/SLAs, health checks, retries with exponential backoff, chaos engineering, disaster recovery.</p>
  </div>

</div>

---

## Phase B-III — Advanced Systems (Weeks 13–16)

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B11 · Week 13</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Storage Systems</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Object storage (S3), blob storage, HDFS, time-series DBs, search engines (Elasticsearch), columnar analytics (BigQuery, Redshift).</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B12 · Week 14</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Special Topics</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Full-text search, notification systems (push/pull), geospatial systems, unique ID generation (UUID, Snowflake), top-K / trending.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B13 · Week 15</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">ML Systems Design</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Feature stores, model serving infrastructure, A/B testing at scale, recommendation system design, stream processing for ML pipelines.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B14 · Week 16</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Kubernetes & Containers</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Docker fundamentals, Kubernetes architecture (pods, services, ingress), horizontal pod autoscaling, rolling deployments, Helm.</p>
  </div>

</div>

---

## Module Coverage Summary

| Phase | Modules | Weeks | Topics |
|-------|---------|-------|--------|
| **B-I: Foundations** | B1–B5 | 3–7 | Requirements, Networking, Hardware, Caching, Data Stores |
| **B-II: Distributed** | B6–B10 | 8–12 | DB Scale, Kafka, CAP/Raft, Scalability, Reliability |
| **B-III: Advanced** | B11–B14 | 13–16 | Storage, Special Topics, ML Systems, Kubernetes |

---

<div class="topic-crosslinks">
  <a href="{{ '/learning/system-design/' | relative_url }}" class="topic-hub-link">← Back to System Design</a>
  <a href="{{ '/learning/system-design/system-design-roadmap/' | relative_url }}" class="topic-hub-link">🗺️ Full Roadmap</a>
</div>
