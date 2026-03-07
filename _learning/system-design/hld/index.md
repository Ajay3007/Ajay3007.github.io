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

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B1 · Week 11</span>
      <span style="background:#00d4aa;color:#030810;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">HLD Fundamentals</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Scalability, CAP Theorem, Consistency Models, Availability Patterns, Load Balancing, Latency vs Throughput. Back-of-envelope estimation and the SD Interview Framework.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b1-hld-fundamentals/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b1-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B2 · Week 12</span>
      <span style="background:#00d4aa;color:#030810;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Databases at Scale</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Indexing (B-Tree, Hash, Composite, Covering), ACID vs BASE, SQL vs NoSQL decision framework, Replication, Sharding strategies, and a practical DB Selection Guide.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b2-databases-at-scale/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b2-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B3 · Week 13</span>
      <span style="background:#00d4aa;color:#030810;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Caching</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Cache-Aside, Write-Through, Write-Back, Read-Through. LRU/LFU eviction, cache invalidation, stampede prevention. Redis data structures (Strings, Hashes, Sets, Sorted Sets) and CDN caching.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b3-caching/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b3-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B4 · Week 14</span>
      <span style="background:#00d4aa;color:#030810;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Message Queues & Kafka</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Async messaging patterns, Kafka architecture (partitions, offsets, consumer groups), at-least-once vs exactly-once, backpressure.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b4-message-queues/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b4-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B5 · Week 15</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Coming Soon</h3>
    <p style="margin:0;font-size:0.88rem;color:var(--light-text);">Next HLD module — to be announced.</p>
  </div>

</div>

---

## Phase B-II — Distributed Systems (Weeks 8–12)

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B6 · Week 16</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Design Twitter/X Feed</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Fan-out on write vs read, hybrid timeline generation, graph DBs, custom cache.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b6-twitter-feed/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b6-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B7 · Week 17</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Design WhatsApp</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">WebSockets, Cassandra, session store, delivery receipts, presence system.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b7-whatsapp/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b7-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B8 · Week 18</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Design YouTube</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Chunked upload, transcoding (temporal parallelism), HLS adaptive streaming, 3-tier CDN, sharded view counter, Elasticsearch search.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b8-youtube/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b8-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B9 · Week 19</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Design a Rate Limiter</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">5 algorithms (fixed/sliding window, token/leaky bucket), Redis Lua scripts, distributed limiting, HTTP 429 headers, multi-tier architecture.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b9-rate-limiter/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b9-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B10 · Week 20</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Consistent Hashing &amp; Service Discovery</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Hash ring, virtual nodes, Consul, ZooKeeper, client vs server-side discovery, health checks, gossip protocol, Raft consensus.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b10-consistent-hashing/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b10-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
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

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B13 · Week 15</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">ML Systems Design</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Feature stores, model serving infrastructure, A/B testing at scale, recommendation system design, stream processing for ML pipelines.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b13-ml-systems/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b13-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B14 · Week 16</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Kubernetes & Containers</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Docker fundamentals, Kubernetes architecture (pods, services, ingress), horizontal pod autoscaling, rolling deployments, Helm.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b14-kubernetes/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b14-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
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
