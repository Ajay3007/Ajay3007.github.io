---
layout: default
title: System Design Mastery — Complete Roadmap
custom_css: system-design-roadmap
custom_js: system-design-roadmap
permalink: /learning/system-design/system-design-roadmap/
---
<header>
  <div class="header-tag">// system design mastery course</div>
  <h1>Complete System Design<br>Roadmap & Course</h1>
  <div class="header-meta">
    <div class="meta-pill">Duration: <span>24 Weeks</span></div>
    <div class="meta-pill">Track: <span>LLD + HLD + ML Systems + K8s</span></div>
    <div class="meta-pill">Style: <span>Balanced · Interview + Concepts</span></div>
    <div class="meta-pill">Audience: <span>Beginners → FAANG-Ready</span></div>
  </div>
</header>

<div class="tabs">
  <div class="tab active" onclick="switchTab('gantt', this)">① Week-by-Week Gantt</div>
  <div class="tab" onclick="switchTab('dep', this)">② Topic Dependency Graph</div>
  <div class="tab" onclick="switchTab('milestone', this)">③ Milestone Progression</div>
</div>

<!-- ==================== VIEW 1: GANTT ==================== -->
<div class="view active" id="view-gantt">
  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:#ffa94d"></div> Phase 0 · Foundation</div>
    <div class="legend-item"><div class="legend-dot" style="background:#7c6fff"></div> Track A · LLD</div>
    <div class="legend-item"><div class="legend-dot" style="background:#00d4aa"></div> Track B · HLD</div>
    <div class="legend-item"><div class="legend-dot" style="background:#ff6b9d"></div> Phase 2 · Convergence</div>
    <div class="legend-item"><div class="legend-dot" style="background:#e879f9"></div> Phase 3 · Advanced</div>
    <div class="legend-item"><div class="legend-dot" style="background:#38bdf8"></div> Phase 4 · Mock + Capstone</div>
    <div class="legend-item"><div class="legend-dot" style="background:#ffa94d;border-radius:2px"></div> Task/Project</div>
  </div>

  <div class="gantt-container">
    <div id="gantt-root"></div>
  </div>
</div>

<!-- ==================== VIEW 2: DEPENDENCY ==================== -->
<div class="view" id="view-dep">
  <div class="dep-view">

    <div class="dep-phase">
      <a href="/learning/system-design/foundation/phase0-foundation/" class="dep-phase-title" style="background:rgba(255,169,77,0.1);color:#ffa94d;border:1px solid rgba(255,169,77,0.2);display:block;text-decoration:none;">
        ⬡ PHASE 0 — Foundation (Weeks 1–2) · Prerequisites for everything below
      </a>
      <div class="dep-nodes">
        <div class="dep-node" style="border-color:rgba(255,169,77,0.4);color:#ffa94d">
          Networking Basics<span class="node-tag">TCP/IP · HTTP · DNS</span>
        </div>
        <div class="dep-node" style="border-color:rgba(255,169,77,0.4);color:#ffa94d">
          OS Fundamentals<span class="node-tag">Threads · I/O · Memory</span>
        </div>
        <div class="dep-node" style="border-color:rgba(255,169,77,0.4);color:#ffa94d">
          Database Basics<span class="node-tag">ACID · Index · Tx</span>
        </div>
        <div class="dep-node" style="border-color:rgba(255,169,77,0.4);color:#ffa94d">
          SD Interview Framework<span class="node-tag">Req → Est → HLD → Tradeoffs</span>
        </div>
        <div class="dep-node" style="border-color:rgba(255,169,77,0.4);color:#ffa94d">
          Back-of-Envelope Estimation<span class="node-tag">QPS · Storage · Bandwidth</span>
        </div>
      </div>
    </div>

    <div class="dep-connector">⬇ unlocks both tracks</div>

    <div class="dep-tracks">
      <!-- LLD Track -->
      <div class="dep-track" style="border-color:rgba(124,111,255,0.3)">
        <div class="dep-track-title" style="color:#7c6fff">
          <span>Track A · LLD</span>
          <span class="track-badge" style="background:rgba(124,111,255,0.1);color:#7c6fff">Weeks 3–10</span>
        </div>

        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A1 · SOLID + OOP + UML</span><span class="week-tag">W3</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A2 · Creational Patterns (5)</span><span class="week-tag">W4</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A3 · Structural Patterns (7)</span><span class="week-tag">W5</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A4 · Behavioral Patterns (12)</span><span class="week-tag">W6–7</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A5 · Concurrency in LLD</span><span class="week-tag">W8</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#7c6fff">
          <span>A6 · Advanced LLD Systems</span><span class="week-tag">W9–10</span>
        </div>
      </div>

      <!-- HLD Track -->
      <div class="dep-track" style="border-color:rgba(0,212,170,0.3)">
        <div class="dep-track-title" style="color:#00d4aa">
          <span>Track B · HLD</span>
          <span class="track-badge" style="background:rgba(0,212,170,0.1);color:#00d4aa">Weeks 3–16</span>
        </div>

        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B1 · System Requirements</span><span class="week-tag">W3</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B2 · Networking + Protocols</span><span class="week-tag">W4</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B3 · Hardware + Infrastructure</span><span class="week-tag">W5</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B4 · Caching</span><span class="week-tag">W6</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B5 · Data Store Internals</span><span class="week-tag">W7</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B6 · Databases at Scale</span><span class="week-tag">W8</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B7 · Queues + Kafka</span><span class="week-tag">W9</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B8 · Distributed Sys Concepts</span><span class="week-tag">W10</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B9 · Scalability Patterns</span><span class="week-tag">W11</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B10 · Reliability + Fault Tolerance</span><span class="week-tag">W12</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B11 · Storage Systems</span><span class="week-tag">W13</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B12 · Special Topics</span><span class="week-tag">W14</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B13 · ML Systems Design</span><span class="week-tag">W15</span>
        </div>
        <div class="dep-arrow">↓</div>
        <div class="dep-module" style="border-left-color:#00d4aa">
          <span>B14 · Kubernetes + Containers</span><span class="week-tag">W16</span>
        </div>
      </div>
    </div>

    <div class="dep-connector">⬇ both tracks converge</div>

    <div class="dep-phase">
      <div class="dep-phase-title" style="background:rgba(255,107,157,0.1);color:#ff6b9d;border:1px solid rgba(255,107,157,0.2)">
        ⬡ PHASE 2 — Convergence: Full System Designs (Weeks 17–20)
      </div>
      <div class="dep-nodes">
        <div class="dep-node" style="border-color:rgba(255,107,157,0.4);color:#ff6b9d">URL Shortener · Pastebin<span class="node-tag">W17</span></div>
        <div class="dep-node" style="border-color:rgba(255,107,157,0.4);color:#ff6b9d">WhatsApp · Notification System<span class="node-tag">W17</span></div>
        <div class="dep-node" style="border-color:rgba(255,107,157,0.4);color:#ff6b9d">Instagram · Twitter · News Feed<span class="node-tag">W18</span></div>
        <div class="dep-node" style="border-color:rgba(255,107,157,0.4);color:#ff6b9d">YouTube · Dropbox · Google Drive<span class="node-tag">W19</span></div>
        <div class="dep-node" style="border-color:rgba(255,107,157,0.4);color:#ff6b9d">Ticket Master · Web Crawler<span class="node-tag">W20</span></div>
      </div>
    </div>

    <div class="dep-connector">↓</div>

    <div class="dep-phase">
      <div class="dep-phase-title" style="background:rgba(232,121,249,0.1);color:#e879f9;border:1px solid rgba(232,121,249,0.2)">
        ⬡ PHASE 3 — Advanced Production Topics (Weeks 21–22)
      </div>
      <div class="dep-nodes">
        <div class="dep-node" style="border-color:rgba(232,121,249,0.4);color:#e879f9">Maintainability<span class="node-tag">Observability · SLOs</span></div>
        <div class="dep-node" style="border-color:rgba(232,121,249,0.4);color:#e879f9">Security Patterns<span class="node-tag">AuthN · AuthZ · mTLS</span></div>
        <div class="dep-node" style="border-color:rgba(232,121,249,0.4);color:#e879f9">Cost Optimization<span class="node-tag">Spot · Reserved · Tiering</span></div>
        <div class="dep-node" style="border-color:rgba(232,121,249,0.4);color:#e879f9">Fraud Detection System<span class="node-tag">Mini Project</span></div>
        <div class="dep-node" style="border-color:rgba(232,121,249,0.4);color:#e879f9">Auth + Monitoring System<span class="node-tag">Mini Project</span></div>
      </div>
    </div>

    <div class="dep-connector">↓</div>

    <div class="dep-phase">
      <div class="dep-phase-title" style="background:rgba(56,189,248,0.1);color:#38bdf8;border:1px solid rgba(56,189,248,0.2)">
        ⬡ PHASE 4 — Mock Interviews + Capstone (Weeks 23–24)
      </div>
      <div class="dep-nodes">
        <div class="dep-node" style="border-color:rgba(56,189,248,0.4);color:#38bdf8">20 Mock Problems<span class="node-tag">With rubric</span></div>
        <div class="dep-node" style="border-color:rgba(56,189,248,0.4);color:#38bdf8">Capstone: Uber E2E<span class="node-tag">LLD + HLD</span></div>
        <div class="dep-node" style="border-color:rgba(56,189,248,0.4);color:#38bdf8">Capstone: YouTube E2E<span class="node-tag">LLD + HLD + CDN</span></div>
        <div class="dep-node" style="border-color:rgba(56,189,248,0.4);color:#38bdf8">Capstone: BookMyShow<span class="node-tag">Concurrency + Scale</span></div>
      </div>
    </div>

  </div>
</div>

<!-- ==================== VIEW 3: MILESTONE ==================== -->
<div class="view" id="view-milestone">
  <div class="milestone-view">

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-number" style="color:#7c6fff">24</div>
        <div class="stat-label">Total Weeks</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color:#00d4aa">14</div>
        <div class="stat-label">HLD Modules</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color:#7c6fff">6</div>
        <div class="stat-label">LLD Modules</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color:#ffa94d">23</div>
        <div class="stat-label">Design Patterns</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color:#ff6b9d">20+</div>
        <div class="stat-label">System Designs</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color:#38bdf8">3</div>
        <div class="stat-label">Capstone Projects</div>
      </div>
    </div>

    <div class="milestone-track">

      <!-- M0 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#ffa94d"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <a href="/learning/system-design/foundation/phase0-foundation/" class="milestone-title" style="color:#ffa94d;text-decoration:none;">🚀 Phase 0 — Foundation Primer</a>
            <div class="milestone-week">Weeks 1–2</div>
          </div>
          <div class="milestone-desc">Build the non-negotiable baseline. Networking, OS, DB basics, and the SD Interview Framework. Learn Back-of-Envelope estimation as a repeatable skill. Everyone starts here.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Estimate Instagram / WhatsApp / YouTube</div>
            <div class="deliverable task">Task: Write requirements doc for 3 systems</div>
            <div class="deliverable">5 Topics</div>
            <div class="deliverable">2 Weeks</div>
          </div>
        </div>
      </div>

      <!-- M1 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">🧱 LLD A1 — SOLID + OOP + UML</div>
            <div class="milestone-week">Week 3</div>
          </div>
          <div class="milestone-desc">Master SOLID principles with real violations and fixes. Learn UML Class and Sequence diagrams. Build the design instinct before patterns.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Refactor badly designed Parking Lot</div>
            <div class="deliverable">Unlock: All Design Patterns</div>
          </div>
        </div>
      </div>

      <!-- M2 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">🏗️ LLD A2 — Creational Patterns</div>
            <div class="milestone-week">Week 4</div>
          </div>
          <div class="milestone-desc">Singleton, Factory, Abstract Factory, Builder, Prototype — each mapped to a real system (Logging, Parking Lot, Snake & Ladder, Chess, File System).</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: ATM System</div>
            <div class="deliverable task">5 Pattern Implementations</div>
          </div>
        </div>
      </div>

      <!-- M3 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">🔗 LLD A3 — Structural Patterns</div>
            <div class="milestone-week">Week 5</div>
          </div>
          <div class="milestone-desc">Adapter, Decorator, Proxy, Composite, Facade, Bridge, Flyweight — mapped to Vending Machine, Pizza Billing, Car Rental, Splitwise, CricBuzz, TrueCaller.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: Splitwise + Simplify Algorithm</div>
            <div class="deliverable task">7 Pattern Implementations</div>
          </div>
        </div>
      </div>

      <!-- M4 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">⚙️ LLD A4 — Behavioral Patterns</div>
            <div class="milestone-week">Weeks 6–7</div>
          </div>
          <div class="milestone-desc">12 behavioral patterns: Strategy, Observer, Chain of Responsibility, State, Command, Iterator, Mediator, Memento, Template Method, Visitor, Null Object, Interpreter.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: BookMyShow + Concurrency</div>
            <div class="deliverable task">12 Pattern Implementations</div>
          </div>
        </div>
      </div>

      <!-- M5 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">🔄 LLD A5 — Concurrency in LLD</div>
            <div class="milestone-week">Week 8</div>
          </div>
          <div class="milestone-desc">Threads, Locks, Semaphores, Monitors. Producer-Consumer, Thread Pool, Deadlock prevention. The bridge between OOP design and systems programming.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Thread-safe BookMyShow booking engine</div>
            <div class="deliverable">Unlock: Advanced LLD Systems</div>
          </div>
        </div>
      </div>

      <!-- M6 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#7c6fff"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#7c6fff">🏢 LLD A6 — Advanced LLD Systems</div>
            <div class="milestone-week">Weeks 9–10</div>
          </div>
          <div class="milestone-desc">LinkedIn, Amazon, Uber/Ola, Hotel Booking, Online Voting, Cache Mechanism, Rate Limiter, Food Delivery, Chat System, Restaurant Management, Bowling Alley.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Major Project: Uber LLD end-to-end</div>
            <div class="deliverable task">10+ System Designs</div>
            <div class="deliverable">✅ LLD Track Complete</div>
          </div>
        </div>
      </div>

      <!-- HLD START -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">📋 HLD B1–B3 — Requirements, Networking, Infrastructure</div>
            <div class="milestone-week">Weeks 3–5</div>
          </div>
          <div class="milestone-desc">System qualities (availability, scalability, durability, consistency). Network protocols deep dive. Hardware topology: servers → VMs → containers → serverless. CDN, Proxy, API Gateway.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Protocol comparison for 5 real systems</div>
            <div class="deliverable task">Task: Global infra layout design</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">💾 HLD B4–B5 — Caching + Data Store Internals</div>
            <div class="milestone-week">Weeks 6–7</div>
          </div>
          <div class="milestone-desc">Cache eviction, invalidation, distributed caching. Then the course differentiator: LSM-tree vs B-tree, RocksDB, Page Cache, Log-structured storage, build a key-value store.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: Build a minimal Key-Value Store</div>
            <div class="deliverable task">Task: Caching layer for Twitter feed</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">🗄️ HLD B6–B7 — Databases at Scale + Queues</div>
            <div class="milestone-week">Weeks 8–9</div>
          </div>
          <div class="milestone-desc">SQL vs NoSQL decision framework. Sharding, Partitioning, Replication, Leader Election, Indexing. Then Kafka deep dive: consumer offsets, delivery guarantees, async patterns.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: DB design for Instagram</div>
            <div class="deliverable task">Task: Notification pipeline with Kafka</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">⚖️ HLD B8–B9 — Distributed Concepts + Scalability</div>
            <div class="milestone-week">Weeks 10–11</div>
          </div>
          <div class="milestone-desc">CAP Theorem, Consistency models, Consistent Hashing, Bloom Filter, Merkle Tree, Gossip Protocol. Then: 0-to-million scaling, Load Balancing, Autoscaling, Microservices patterns.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Consistent hashing ring implementation</div>
            <div class="deliverable task">Task: Monolith → microservices evolution</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">🛡️ HLD B10–B11 — Reliability + Storage Systems</div>
            <div class="milestone-week">Weeks 12–13</div>
          </div>
          <div class="milestone-desc">Circuit Breaker, Bulkhead, Shuffle Sharding, Timeouts, Retries, Fail-fast. Then Block/File/Object storage, RAID, GFS, HDFS for large-scale file systems.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Resilience patterns for payment system</div>
            <div class="deliverable task">Task: Storage layer for Dropbox</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">🔍 HLD B12 — Special Topics</div>
            <div class="milestone-week">Week 14</div>
          </div>
          <div class="milestone-desc">Search Autocomplete/Typeahead internals, Web Crawler architecture, News Feed ranking, Geospatial systems (NearbyFriends, Yelp).</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: Design Typeahead search system</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">🤖 HLD B13 — ML Systems Design</div>
            <div class="milestone-week">Week 15</div>
          </div>
          <div class="milestone-desc">Feature stores, training pipelines, model serving, A/B testing infrastructure, recommendation systems, real-time ML inference at scale. MLOps fundamentals.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: Design a Recommendation System</div>
            <div class="deliverable task">Task: Design Feature Store</div>
          </div>
        </div>
      </div>

      <div class="milestone">
        <div class="milestone-dot" style="background:#00d4aa"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#00d4aa">☸️ HLD B14 — Kubernetes + Container Orchestration</div>
            <div class="milestone-week">Week 16</div>
          </div>
          <div class="milestone-desc">Containers → Pods → Services → Ingress. Deployments, StatefulSets, HPA, resource management. Service mesh basics (Istio). K8s in system design interviews.</div>
          <div class="milestone-deliverables">
            <div class="deliverable task">Task: K8s architecture for a microservices system</div>
            <div class="deliverable">✅ HLD Track Complete</div>
          </div>
        </div>
      </div>

      <!-- PHASE 2 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#ff6b9d"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#ff6b9d">🔀 Phase 2 — Convergence: Full System Designs</div>
            <div class="milestone-week">Weeks 17–20</div>
          </div>
          <div class="milestone-desc">Both tracks merge. Apply LLD + HLD together. Each system: Requirements → Estimation → HLD diagram → Deep dive 2 components → Trade-offs. 10+ complete system designs.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">URL Shortener · Pastebin</div>
            <div class="deliverable project">WhatsApp · Notification System</div>
            <div class="deliverable project">Instagram · Twitter · News Feed</div>
            <div class="deliverable project">YouTube · Dropbox · Google Drive</div>
            <div class="deliverable project">Ticket Master · Web Crawler · NearbyFriends</div>
          </div>
        </div>
      </div>

      <!-- PHASE 3 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#e879f9"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#e879f9">⚡ Phase 3 — Advanced Production Topics</div>
            <div class="milestone-week">Weeks 21–22</div>
          </div>
          <div class="milestone-desc">Maintainability, Observability, SLOs. Security patterns (AuthN, AuthZ, mTLS, Zero Trust). Cost optimization (Spot instances, tiered storage). Fraud detection + Auth+Monitoring system designs.</div>
          <div class="milestone-deliverables">
            <div class="deliverable project">Mini Project: Fraud Detection System</div>
            <div class="deliverable project">Mini Project: Auth + Monitoring System</div>
          </div>
        </div>
      </div>

      <!-- PHASE 4 -->
      <div class="milestone">
        <div class="milestone-dot" style="background:#38bdf8"></div>
        <div class="milestone-card">
          <div class="milestone-header">
            <div class="milestone-title" style="color:#38bdf8">🏆 Phase 4 — Mock Interviews + Capstone</div>
            <div class="milestone-week">Weeks 23–24</div>
          </div>
          <div class="milestone-desc">20 timed mock problems with evaluation rubric. Then the final capstone: choose one end-to-end project that combines everything — LLD entities, HLD architecture, storage, reliability, and trade-off analysis.</div>
          <div class="milestone-deliverables">
            <div class="deliverable mock">20 Mock Interview Problems</div>
            <div class="deliverable capstone">Capstone: Uber E2E (LLD + HLD)</div>
            <div class="deliverable capstone">Capstone: YouTube E2E (+ CDN + Storage)</div>
            <div class="deliverable capstone">Capstone: BookMyShow (Concurrency + Scale)</div>
            <div class="deliverable">✅ Course Complete · FAANG Ready</div>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>

<div class="tooltip" id="tooltip">
  <div class="tooltip-title" id="tt-title"></div>
  <div class="tooltip-body" id="tt-body"></div>
</div>
