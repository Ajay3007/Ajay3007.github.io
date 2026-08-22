---
title: "Low-Level Design (LLD)"
description: "⚙️ Low-Level Design (LLD) Design classes, components, and interactions at the code level — SOLID principles, all 23 GoF design patterns, concurrency, and real interview case…"
domain: system-design
track: system-design-lld
order: 0
ownHeader: true
url: /learning/system-design/lld/
---

# ⚙️ Low-Level Design (LLD)

Design classes, components, and interactions at the code level — SOLID principles, all 23 GoF design patterns, concurrency, and real interview case studies.

<div style="display:flex;gap:1rem;flex-wrap:wrap;margin:1rem 0 2rem;">
  <span style="background:rgba(124,111,255,0.1);color:#7c6fff;border:1px solid rgba(124,111,255,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">Track A · Weeks 3–10</span>
  <span style="background:rgba(16,185,129,0.1);color:#10b981;border:1px solid rgba(16,185,129,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">6 of 6 modules complete</span>
  <span style="background:rgba(245,158,11,0.1);color:#f59e0b;border:1px solid rgba(245,158,11,0.3);border-radius:20px;padding:0.3rem 0.85rem;font-size:0.85rem;font-weight:600;">23 Design Patterns</span>
</div>

---

## Track A — Module Map

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.25rem;margin:1.5rem 0;">

  <!-- A1 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A1 · Week 3</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;"><a href="/learning/system-design/lld/module-a1-solid/">SOLID + OOP + UML</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">5 SOLID principles, OOP pillars (Abstraction, Encapsulation, Inheritance, Polymorphism), UML class & sequence diagrams.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a1-solid/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a1-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <!-- A2 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A2 · Week 4</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;"><a href="/learning/system-design/lld/module-a2-creational/">Creational Patterns</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">5 patterns: Singleton, Factory Method, Abstract Factory, Builder, Prototype — when to use each, pitfalls, real-world examples.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a2-creational/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a2-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <!-- A3 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A3 · Week 5</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;"><a href="/learning/system-design/lld/module-a3-structural/">Structural Patterns</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">7 patterns: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy — structural composition and interface shaping.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a3-structural/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a3-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <!-- A4 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A4 · Weeks 6–7</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;"><a href="/learning/system-design/lld/module-a4-behavioral/">Behavioral Patterns</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">11 patterns: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor, Interpreter.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a4-behavioral/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a4-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <!-- A5 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A5 · Week 8</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);"><a href="/learning/system-design/lld/module-a5-concurrency/">Concurrency in LLD</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">Thread safety, synchronization primitives, Producer-Consumer, Reader-Writer, Thread Pool, deadlock detection and prevention.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a5-concurrency/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a5-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

  <!-- A6 -->
  <div class="project-card" style="border-left:4px solid #7c6fff;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
      <span style="font-size:0.78rem;font-weight:700;color:#7c6fff;text-transform:uppercase;letter-spacing:0.05em;">A6 · Weeks 9–10</span>
      <span style="background:#10b981;color:white;border-radius:12px;padding:0.2rem 0.6rem;font-size:0.72rem;font-weight:700;">✓ Complete</span>
    </div>
    <h3 style="margin:0 0 0.4rem;color:var(--text-color);"><a href="/learning/system-design/lld/module-a6-case-studies/">LLD Case Studies</a></h3>
    <p style="margin:0 0 0.75rem;font-size:0.9rem;color:var(--light-text);">6 full systems: Chess Game, Elevator, Library Management, Food Ordering, Parking Lot, Hotel Booking — applying all patterns end-to-end.</p>
    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
      <a href="/learning/system-design/lld/module-a6-case-studies/" style="font-size:0.8rem;color:#7c6fff;font-weight:600;">📖 Module →</a>
      <a href="/learning/system-design/lld/module-a6-notes/" style="font-size:0.8rem;color:var(--light-text);font-weight:600;">📝 Notes →</a>
    </div>
  </div>

</div>

---

## Pattern Coverage Summary

| Category | Patterns | Module | Status |
|----------|----------|--------|--------|
| **Creational** (5) | Singleton, Factory Method, Abstract Factory, Builder, Prototype | A2 | ✅ Complete |
| **Structural** (7) | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy | A3 | ✅ Complete |
| **Behavioral** (11) | CoR, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template, Visitor, Interpreter | A4 | ✅ Complete |
| **SOLID + OOP** | SRP, OCP, LSP, ISP, DIP + 4 OOP pillars + UML | A1 | ✅ Complete |
| **Concurrency** | Thread safety, locks, semaphores, concurrent patterns | A5 | ✅ Complete |
| **LLD Systems** | Chess, Elevator, Library, Food Ordering, Parking Lot, Hotel | A6 | ✅ Complete |

---

<div class="topic-crosslinks">
  <a href="/learning/system-design/" class="topic-hub-link">← Back to System Design</a>
  <a href="/learning/system-design/system-design-roadmap/" class="topic-hub-link">🗺️ Full Roadmap</a>
</div>
