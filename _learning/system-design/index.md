---
layout: default
title: System Design
permalink: /learning/system-design/
---

# 🛠️ System Design Learning Hub

A structured 24-week course covering Low-Level Design (all 23 GoF patterns), High-Level Design (14 modules), full system design case studies, and production-grade advanced topics.

<div style="display:flex;gap:1rem;flex-wrap:wrap;margin:1rem 0 2rem;">
  <span style="background:rgba(0,212,255,0.1);color:#00d4ff;border:1px solid rgba(0,212,255,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">24-Week Roadmap</span>
  <span style="background:rgba(16,185,129,0.1);color:#10b981;border:1px solid rgba(16,185,129,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">LLD Track A — 6/6 modules done</span>
  <span style="background:rgba(245,158,11,0.1);color:#f59e0b;border:1px solid rgba(245,158,11,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">HLD Track B — 3/14 modules done</span>
</div>

<div style="margin-bottom:2rem;">
  <a href="{{ '/learning/system-design/system-design-roadmap/' | relative_url }}" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.5rem;background:linear-gradient(135deg,#7c6fff,#00d4aa);color:white;border-radius:8px;font-weight:700;text-decoration:none;font-size:0.95rem;">🗺️ View Full 24-Week Roadmap →</a>
</div>

---

## Phase 0 — Foundation

<div class="project-card" style="border-left:4px solid #ffa94d;margin-bottom:2rem;">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
    <span style="font-size:0.78rem;font-weight:700;color:#ffa94d;text-transform:uppercase;letter-spacing:0.05em;">Weeks 1–2 · Prerequisites</span>
    <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
  </div>
  <h3 style="margin:0 0 0.4rem;"><a href="{{ '/learning/system-design/foundation/phase0-foundation/' | relative_url }}">Foundation — Networking, OS, Databases &amp; Estimation</a></h3>
  <p style="margin:0;font-size:0.9rem;color:var(--light-text);">TCP/IP, HTTP, DNS, OS threads &amp; I/O, ACID, database indexing, SD interview framework, back-of-envelope estimation (QPS, storage, bandwidth).</p>
</div>

---

## Track A — Low-Level Design (LLD)

Object-oriented design, all 23 GoF design patterns, concurrency, and end-to-end LLD case studies.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A1 · Week 3</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a1-solid/' | relative_url }}">SOLID + OOP + UML</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">5 SOLID principles, 4 OOP pillars, UML class &amp; sequence diagrams.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A2 · Week 4</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a2-creational/' | relative_url }}">Creational Patterns</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Singleton, Factory Method, Abstract Factory, Builder, Prototype.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A3 · Week 5</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a3-structural/' | relative_url }}">Structural Patterns</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A4 · Weeks 6–7</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a4-behavioral/' | relative_url }}">Behavioral Patterns</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">11 patterns: CoR, Command, Observer, State, Strategy, Iterator &amp; more.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A5 · Week 8</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a5-concurrency/' | relative_url }}">Concurrency in LLD</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Thread safety, locks, semaphores, Producer-Consumer, Thread Pool.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#7c6fff;font-weight:700;">A6 · Weeks 9–10</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/lld/module-a6-case-studies/' | relative_url }}">LLD Case Studies</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Chess, Elevator, Library, Food Ordering, Parking Lot, Hotel Booking.</p>
  </div>

</div>

<a href="{{ '/learning/system-design/lld/' | relative_url }}" style="font-size:0.9rem;color:#7c6fff;font-weight:600;">See full LLD module map →</a>

---

## Track B — High-Level Design (HLD)

Scalability, distributed systems, databases, caching, queues, reliability, and real system designs.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;margin:1.5rem 0 2rem;">

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B1–B3 · Weeks 11–13</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/hld/' | relative_url }}">Foundations of Scale</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">HLD Fundamentals, Databases at Scale, Caching.</p>
  </div>

  <div class="project-card b-track" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#00d4aa;text-transform:uppercase;letter-spacing:0.05em;">B4 · Week 14</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);">Message Queues & Kafka</h3>
    <p style="margin:0 0 0.6rem;font-size:0.88rem;color:var(--light-text);">Async messaging patterns, Kafka architecture (partitions, offsets, consumer groups), at-least-once vs exactly-once, backpressure.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;">
      <a href="{{ '/learning/system-design/hld/module-b4-message-queues/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b4-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B5 · Week 15</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/hld/module-b5-url-shortener/' | relative_url }}">URL Shortener (TinyURL)</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Base62 encoding, caching, 301/302.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;margin-top:0.6rem;">
      <a href="{{ '/learning/system-design/hld/module-b5-url-shortener/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b5-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B6 · Week 16</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/hld/module-b6-twitter-feed/' | relative_url }}">Design Twitter/X Feed</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Fan-out on write vs read, hybrid timeline.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;margin-top:0.6rem;">
      <a href="{{ '/learning/system-design/hld/module-b6-twitter-feed/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b6-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B7 · Week 17</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">✓ Done</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;"><a href="{{ '/learning/system-design/hld/module-b7-whatsapp/' | relative_url }}">Design WhatsApp</a></h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">WebSockets, Cassandra, Presence, Group Messaging.</p>
    <div style="display:flex;gap:0.8rem;flex-wrap:wrap;margin-top:0.6rem;">
      <a href="{{ '/learning/system-design/hld/module-b7-whatsapp/' | relative_url }}" style="font-size:0.8rem;color:#00d4aa;font-weight:600;">📖 Module →</a>
      <a href="{{ '/learning/system-design/hld/module-b7-notes/' | relative_url }}" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B8–B10 · Weeks 8–12</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;color:var(--text-color);">Distributed Systems</h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Databases at Scale, Kafka, Distributed Systems, Scalability Patterns, Reliability.</p>
  </div>

  <div class="project-card" style="border-left:4px solid #00d4aa;opacity:0.75;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
      <span style="font-size:0.75rem;color:#00d4aa;font-weight:700;">B11–B14 · Weeks 13–16</span>
      <span style="background:#94a3b8;color:white;border-radius:12px;padding:0.15rem 0.55rem;font-size:0.7rem;font-weight:700;">🔜 Soon</span>
    </div>
    <h3 style="margin:0 0 0.3rem;font-size:1rem;color:var(--text-color);">Advanced Systems</h3>
    <p style="margin:0;font-size:0.85rem;color:var(--light-text);">Storage Systems, Special Topics, ML Systems Design, Kubernetes &amp; Containers.</p>
  </div>

</div>

<a href="{{ '/learning/system-design/hld/' | relative_url }}" style="font-size:0.9rem;color:#00d4aa;font-weight:600;">See HLD module plan →</a>

---

## Phase 2–4 — Case Studies, Advanced Topics &amp; Mocks

| Phase | Weeks | Content | Status |
|-------|-------|---------|--------|
| **Phase 2** | 17–20 | Full system designs: URL Shortener, WhatsApp, YouTube, Instagram, Dropbox, Twitter... | 🔜 Coming |
| **Phase 3** | 21–22 | Observability, Security, Cost Optimization, mini-projects | 🔜 Coming |
| **Phase 4** | 23–24 | 20 mock interview problems, Capstones: Uber, YouTube, BookMyShow | 🔜 Coming |

---

<div class="topic-crosslinks">
  <a href="{{ '/learning/system-design/system-design-roadmap/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">🗺️ Full Roadmap</a>
  <a href="{{ '/learning/' | relative_url }}" class="topic-hub-link">← Learning Hub</a>
</div>
