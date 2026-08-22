---
title: "Module A1 — SOLID + OOP + UML | LLD Track"
description: "TRACK A · LLD · MODULE A1 · WEEK 3 S O L I D Principles + OOP + UML Prereq Phase 0 Unlocks All 23 Design Patterns Task Parking Lot Refactoring Duration 1 Week Track A —…"
domain: system-design
track: system-design-lld
order: 2
url: /learning/system-design/lld/module-a1-solid/
---

<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Fira+Code:wght@300;400;500&display=swap" rel="stylesheet">

<div class="m1-page">

<!-- ── HEADER ────────────────────────────────────────────────── -->
<div class="m1-header">
  <div class="m1-header-glow"></div>
  <div class="m1-module-badge">TRACK A · LLD · MODULE A1 · WEEK 3</div>
  <div class="m1-solid-letters">
    <span class="m1-solid-letter s">S</span><span class="m1-solid-letter o">O</span><span class="m1-solid-letter l">L</span><span class="m1-solid-letter i">I</span><span class="m1-solid-letter d">D</span>
  </div>
  <h1>Principles + OOP + UML</h1>
  <div class="m1-pills">
    <div class="m1-pill">Prereq <span>Phase 0</span></div>
    <div class="m1-pill">Unlocks <span>All 23 Design Patterns</span></div>
    <div class="m1-pill">Task <span>Parking Lot Refactoring</span></div>
    <div class="m1-pill">Duration <span>1 Week</span></div>
    <div class="m1-pill">Track <span>A — Low-Level Design</span></div>
  </div>
</div>

<!-- ── NAV ───────────────────────────────────────────────────── -->
<nav class="m1-nav">
  <div class="m1-nav-tab active" onclick="m1Show('oop',this)">OOP Pillars</div>
  <div class="m1-nav-tab" onclick="m1Show('solid',this)">SOLID Deep Dive</div>
  <div class="m1-nav-tab" onclick="m1Show('violations',this)">Violation Patterns</div>
  <div class="m1-nav-tab" onclick="m1Show('uml',this)">UML Reference</div>
  <div class="m1-nav-tab" onclick="m1Show('parking',this)">Parking Lot</div>
  <div class="m1-nav-tab" onclick="m1Show('tasks',this)">Tasks</div>
  <div class="m1-nav-tab" onclick="m1Show('checklist',this)">Checklist</div>
</nav>

<div class="m1-content">

<!-- ===== VIEW 1: OOP PILLARS ===== -->
<div class="m1-view active" id="m1-view-oop">
  <div class="m1-pillars-grid">
    <div class="m1-pillar-card">
      <div class="m1-pillar-icon">🔒</div>
      <div class="m1-pillar-name">Encapsulation</div>
      <div class="m1-pillar-tagline">bundle + hide + expose only what's needed</div>
      <div class="m1-pillar-body">Bundle data and behaviour. Hide internal state behind methods. Expose only a stable public interface. When internals change, callers don't break.</div>
    </div>
    <div class="m1-pillar-card">
      <div class="m1-pillar-icon">🎭</div>
      <div class="m1-pillar-name">Abstraction</div>
      <div class="m1-pillar-tagline">expose WHAT, hide HOW</div>
      <div class="m1-pillar-body">Program to interfaces, not implementations. Callers know what a thing does, not how. Foundation of Strategy, Factory, Bridge patterns.</div>
    </div>
    <div class="m1-pillar-card">
      <div class="m1-pillar-icon">🧬</div>
      <div class="m1-pillar-name">Inheritance</div>
      <div class="m1-pillar-tagline">IS-A relationships only — prefer composition</div>
      <div class="m1-pillar-body">Child inherits parent's state + behaviour. Valid only for true IS-A relationships (Dog IS-A Animal). For HAS-A use composition. Inheritance = tight coupling.</div>
    </div>
    <div class="m1-pillar-card">
      <div class="m1-pillar-icon">🔀</div>
      <div class="m1-pillar-name">Polymorphism</div>
      <div class="m1-pillar-tagline">same interface, different behaviour</div>
      <div class="m1-pillar-body">One method call, many implementations. Runtime polymorphism via overriding. Compile-time via overloading. Core to OCP and all design patterns that use substitution.</div>
    </div>
  </div>

  <div class="m1-rule-box">
    <div class="m1-rule-label">⚠️ CRITICAL RULE</div>
    <div class="m1-rule-title">Favour Composition Over Inheritance</div>
    <div class="m1-rule-body">Inheritance creates tight coupling — when the parent changes, all children may break. Use inheritance only when the IS-A relationship is semantically true and stable. Use composition (HAS-A) when behaviour needs to be flexible or swappable at runtime. Most design patterns exploit composition, not inheritance.</div>
    <div class="m1-rule-examples">
      <div class="m1-rule-example"><span style="color:var(--m1-bad)">✗ Inheritance:</span><span style="color:var(--m1-muted)"> Duck extends Bird (breaks for robots)</span></div>
      <div class="m1-rule-example"><span style="color:var(--m1-good)">✓ Composition:</span><span style="color:var(--m1-muted)"> Duck has FlyBehaviour (swappable)</span></div>
    </div>
  </div>
</div>

<!-- ===== VIEW 2: SOLID DEEP DIVE ===== -->
<div class="m1-view" id="m1-view-solid">
  <div class="m1-solid-nav">
    <div class="m1-solid-btn s active" onclick="m1SelectSolid('s',this)">S — Single Responsibility</div>
    <div class="m1-solid-btn o" onclick="m1SelectSolid('o',this)">O — Open/Closed</div>
    <div class="m1-solid-btn l" onclick="m1SelectSolid('l',this)">L — Liskov Substitution</div>
    <div class="m1-solid-btn i" onclick="m1SelectSolid('i',this)">I — Interface Segregation</div>
    <div class="m1-solid-btn d" onclick="m1SelectSolid('d',this)">D — Dependency Inversion</div>
  </div>

  <!-- S -->
  <div class="m1-solid-panel active" id="m1-solid-s">
    <div class="m1-principle-header">
      <div class="m1-principle-letter s">S</div>
      <div>
        <div class="m1-principle-name">Single Responsibility Principle</div>
        <div class="m1-principle-full">SRP · Robert C. Martin</div>
        <div class="m1-principle-quote" style="border-left-color:var(--m1-s)">"A class should have only one reason to change."</div>
      </div>
    </div>
    <div class="m1-code-compare">
      <div class="m1-code-box">
        <div class="m1-code-box-hd bad">✗ VIOLATION — 4 reasons to change</div>
        <div class="m1-code-content"><span class="kw">class</span> <span class="cls">Invoice</span> {
  <span class="hl">// Reason 1: business logic changes</span>
  <span class="kw">double</span> <span class="fn">calculateTotal</span>() { ... }

  <span class="hl">// Reason 2: DB schema changes</span>
  <span class="kw">void</span> <span class="fn">saveToDatabase</span>() { ... }

  <span class="hl">// Reason 3: report format changes</span>
  <span class="kw">void</span> <span class="fn">printInvoice</span>() { ... }

  <span class="hl">// Reason 4: email provider changes</span>
  <span class="kw">void</span> <span class="fn">sendEmail</span>() { ... }
}</div>
      </div>
      <div class="m1-code-box">
        <div class="m1-code-box-hd good">✓ FIX — one responsibility each</div>
        <div class="m1-code-content"><span class="kw">class</span> <span class="cls">Invoice</span> {
  <span class="fix">// Only: business logic</span>
  <span class="kw">double</span> <span class="fn">calculateTotal</span>() { ... }
}
<span class="kw">class</span> <span class="cls">InvoiceRepository</span> {
  <span class="fix">// Only: persistence</span>
  <span class="kw">void</span> <span class="fn">save</span>(<span class="cls">Invoice</span> inv) { ... }
}
<span class="kw">class</span> <span class="cls">InvoicePrinter</span> {
  <span class="fix">// Only: printing</span>
  <span class="kw">void</span> <span class="fn">print</span>(<span class="cls">Invoice</span> inv) { ... }
}
<span class="kw">class</span> <span class="cls">InvoiceEmailer</span> {
  <span class="fix">// Only: email</span>
  <span class="kw">void</span> <span class="fn">send</span>(<span class="cls">Invoice</span> inv) { ... }
}</div>
      </div>
    </div>
    <div class="m1-interview-tip">SRP violations are the #1 reason codebases become unmaintainable. In interviews, when asked "what's wrong with this design?", look for classes doing too many things. Count the "reasons to change" — should always be 1.</div>
  </div>

  <!-- O -->
  <div class="m1-solid-panel" id="m1-solid-o">
    <div class="m1-principle-header">
      <div class="m1-principle-letter o">O</div>
      <div>
        <div class="m1-principle-name">Open/Closed Principle</div>
        <div class="m1-principle-full">OCP · Bertrand Meyer, popularised by Martin</div>
        <div class="m1-principle-quote" style="border-left-color:var(--m1-o)">"Open for extension, closed for modification."</div>
      </div>
    </div>
    <div class="m1-code-compare">
      <div class="m1-code-box">
        <div class="m1-code-box-hd bad">✗ VIOLATION — modify for every new type</div>
        <div class="m1-code-content"><span class="kw">class</span> <span class="cls">DiscountCalc</span> {
  <span class="kw">double</span> <span class="fn">calculate</span>(<span class="cls">String</span> type, <span class="kw">double</span> p) {
    <span class="hl">if</span> (type.equals(<span class="str">"REGULAR"</span>)) <span class="kw">return</span> p * 0.95;
    <span class="hl">if</span> (type.equals(<span class="str">"PREMIUM"</span>))  <span class="kw">return</span> p * 0.85;
    <span class="hl">if</span> (type.equals(<span class="str">"EMPLOYEE"</span>)) <span class="kw">return</span> p * 0.70;
    <span class="cm">// Every new type = modify this class!</span>
    <span class="kw">return</span> p;
  }
}</div>
      </div>
      <div class="m1-code-box">
        <div class="m1-code-box-hd good">✓ FIX — extend without modifying</div>
        <div class="m1-code-content"><span class="kw">interface</span> <span class="cls">DiscountStrategy</span> {
  <span class="kw">double</span> <span class="fn">apply</span>(<span class="kw">double</span> price);
}
<span class="kw">class</span> <span class="cls">RegularDiscount</span> <span class="kw">implements</span> <span class="cls">DiscountStrategy</span> {
  <span class="kw">public double</span> <span class="fn">apply</span>(<span class="kw">double</span> p) { <span class="kw">return</span> p*0.95; }
}
<span class="cm">// New type = new class, touch NOTHING else:</span>
<span class="fix">class</span> <span class="cls">VIPDiscount</span> <span class="kw">implements</span> <span class="cls">DiscountStrategy</span> {
  <span class="kw">public double</span> <span class="fn">apply</span>(<span class="kw">double</span> p) { <span class="kw">return</span> p*0.60; }
}</div>
      </div>
    </div>
    <div class="m1-interview-tip">OCP is directly embodied by the Strategy Pattern (A2) and Template Method (A4). When you see an if/else chain branching on type — that's OCP violation territory. The fix is almost always a Strategy or polymorphism.</div>
  </div>

  <!-- L -->
  <div class="m1-solid-panel" id="m1-solid-l">
    <div class="m1-principle-header">
      <div class="m1-principle-letter l">L</div>
      <div>
        <div class="m1-principle-name">Liskov Substitution Principle</div>
        <div class="m1-principle-full">LSP · Barbara Liskov, 1987</div>
        <div class="m1-principle-quote" style="border-left-color:var(--m1-l)">"Subtypes must be substitutable for their base types without altering program correctness."</div>
      </div>
    </div>
    <div class="m1-code-compare">
      <div class="m1-code-box">
        <div class="m1-code-box-hd bad">✗ VIOLATION — Square breaks Rectangle contract</div>
        <div class="m1-code-content"><span class="kw">class</span> <span class="cls">Rectangle</span> {
  <span class="kw">void</span> <span class="fn">setWidth</span>(<span class="kw">int</span> w)  { <span class="kw">this</span>.width = w; }
  <span class="kw">void</span> <span class="fn">setHeight</span>(<span class="kw">int</span> h) { <span class="kw">this</span>.height = h; }
}
<span class="kw">class</span> <span class="cls">Square</span> <span class="kw">extends</span> <span class="cls">Rectangle</span> {
  <span class="hl">void</span> <span class="fn">setWidth</span>(<span class="kw">int</span> w)  { width=w; height=w; }
  <span class="hl">void</span> <span class="fn">setHeight</span>(<span class="kw">int</span> h) { width=h; height=h; }
}
<span class="cm">// testArea(r): r.setWidth(5); r.setHeight(4);</span>
<span class="cm">// Passes for Rectangle, FAILS for Square!</span></div>
      </div>
      <div class="m1-code-box">
        <div class="m1-code-box-hd good">✓ FIX — use abstraction instead</div>
        <div class="m1-code-content"><span class="kw">interface</span> <span class="cls">Shape</span> {
  <span class="fix">int</span> <span class="fn">area</span>();
}

<span class="kw">class</span> <span class="cls">Rectangle</span> <span class="kw">implements</span> <span class="cls">Shape</span> {
  <span class="kw">int</span> <span class="fn">area</span>() { <span class="kw">return</span> width * height; }
}

<span class="kw">class</span> <span class="cls">Square</span> <span class="kw">implements</span> <span class="cls">Shape</span> {
  <span class="kw">int</span> <span class="fn">area</span>() { <span class="kw">return</span> side * side; }
}
<span class="cm">// Both honour the Shape contract ✓</span></div>
      </div>
    </div>
    <div class="m1-interview-tip">LSP violations show up as <code>instanceof</code> checks or <code>UnsupportedOperationException</code> throws. These scream "inheritance hierarchy is wrong." Common trap: Penguin extends Bird (fly() throws!).</div>
  </div>

  <!-- I -->
  <div class="m1-solid-panel" id="m1-solid-i">
    <div class="m1-principle-header">
      <div class="m1-principle-letter i">I</div>
      <div>
        <div class="m1-principle-name">Interface Segregation Principle</div>
        <div class="m1-principle-full">ISP · Robert C. Martin</div>
        <div class="m1-principle-quote" style="border-left-color:var(--m1-i)">"Clients should not be forced to depend on interfaces they do not use."</div>
      </div>
    </div>
    <div class="m1-code-compare">
      <div class="m1-code-box">
        <div class="m1-code-box-hd bad">✗ VIOLATION — fat interface forces stubs</div>
        <div class="m1-code-content"><span class="kw">interface</span> <span class="cls">Worker</span> {
  <span class="kw">void</span> <span class="fn">work</span>();
  <span class="hl">void</span> <span class="fn">eat</span>();    <span class="cm">// robots don't eat</span>
  <span class="hl">void</span> <span class="fn">sleep</span>();   <span class="cm">// robots don't sleep</span>
}
<span class="kw">class</span> <span class="cls">RobotWorker</span> <span class="kw">implements</span> <span class="cls">Worker</span> {
  <span class="kw">void</span> <span class="fn">work</span>()  { ... }
  <span class="hl">void</span> <span class="fn">eat</span>()   { <span class="kw">throw new</span> <span class="cls">UnsupportedOperationException</span>(); }
  <span class="hl">void</span> <span class="fn">sleep</span>() { <span class="kw">throw new</span> <span class="cls">UnsupportedOperationException</span>(); }
}</div>
      </div>
      <div class="m1-code-box">
        <div class="m1-code-box-hd good">✓ FIX — focused role interfaces</div>
        <div class="m1-code-content"><span class="kw">interface</span> <span class="cls">Workable</span>  { <span class="fix">void</span> <span class="fn">work</span>(); }
<span class="kw">interface</span> <span class="cls">Feedable</span>   { <span class="fix">void</span> <span class="fn">eat</span>(); }
<span class="kw">interface</span> <span class="cls">Restable</span>   { <span class="fix">void</span> <span class="fn">sleep</span>(); }

<span class="kw">class</span> <span class="cls">HumanWorker</span> <span class="kw">implements</span>
    <span class="cls">Workable</span>, <span class="cls">Feedable</span>, <span class="cls">Restable</span> { ... }

<span class="kw">class</span> <span class="cls">RobotWorker</span> <span class="kw">implements</span>
    <span class="cls">Workable</span> { ... }
<span class="cm">// Only what it needs — no stubs!</span></div>
      </div>
    </div>
    <div class="m1-interview-tip">ISP violations are common in legacy codebases. Look for: interfaces with 10+ methods, classes implementing interface methods that throw UnsupportedOperationException, or clients importing an interface but only using 2 of its 12 methods.</div>
  </div>

  <!-- D -->
  <div class="m1-solid-panel" id="m1-solid-d">
    <div class="m1-principle-header">
      <div class="m1-principle-letter d">D</div>
      <div>
        <div class="m1-principle-name">Dependency Inversion Principle</div>
        <div class="m1-principle-full">DIP · Robert C. Martin</div>
        <div class="m1-principle-quote" style="border-left-color:var(--m1-d)">"High-level modules should not depend on low-level modules. Both should depend on abstractions."</div>
      </div>
    </div>
    <div class="m1-code-compare">
      <div class="m1-code-box">
        <div class="m1-code-box-hd bad">✗ VIOLATION — hard-coded concrete deps</div>
        <div class="m1-code-content"><span class="kw">class</span> <span class="cls">OrderService</span> {
  <span class="kw">private</span> <span class="cls">MySQLDatabase</span> <span class="hl">database</span>;
  <span class="kw">private</span> <span class="cls">EmailService</span>   <span class="hl">emailer</span>;

  <span class="kw">public</span> <span class="cls">OrderService</span>() {
    <span class="kw">this</span>.database = <span class="hl">new</span> <span class="cls">MySQLDatabase</span>(); <span class="cm">// ✗</span>
    <span class="kw">this</span>.emailer  = <span class="hl">new</span> <span class="cls">EmailService</span>();   <span class="cm">// ✗</span>
  }
}
<span class="cm">// To switch to PostgreSQL — must change OrderService!</span></div>
      </div>
      <div class="m1-code-box">
        <div class="m1-code-box-hd good">✓ FIX — inject abstractions</div>
        <div class="m1-code-content"><span class="kw">interface</span> <span class="cls">OrderRepository</span>    { <span class="fix">void</span> <span class="fn">save</span>(<span class="cls">Order</span> o); }
<span class="kw">interface</span> <span class="cls">NotificationService</span> { <span class="fix">void</span> <span class="fn">notify</span>(<span class="cls">Order</span> o); }

<span class="kw">class</span> <span class="cls">OrderService</span> {
  <span class="kw">private final</span> <span class="cls">OrderRepository</span>    repo;
  <span class="kw">private final</span> <span class="cls">NotificationService</span> notif;

  <span class="kw">public</span> <span class="cls">OrderService</span>(<span class="cls">OrderRepository</span> r,
                       <span class="cls">NotificationService</span> n) {
    <span class="kw">this</span>.repo = r; <span class="kw">this</span>.notif = n;
  }
}
<span class="cm">// Wiring: new OrderService(new PostgreSQL(), new SMS());</span></div>
      </div>
    </div>
    <div class="m1-interview-tip">DIP is the principle that makes unit testing possible. Without it, you can't mock dependencies. In LLD interviews, always inject dependencies via constructor — never instantiate them inside the class.</div>
  </div>
</div>

<!-- ===== VIEW 3: VIOLATION PATTERNS ===== -->
<div class="m1-view" id="m1-view-violations">
  <div class="m1-scanner">
    <div class="m1-scanner-title">🔍 Quick-Reference: SOLID Violation Scanner</div>
    <div class="m1-violation-list">
      <div class="m1-violation-item">
        <div class="m1-v-principle s">S</div>
        <div class="m1-v-text"><strong>Class with 5+ unrelated methods</strong>Split into focused classes with one responsibility each. Count "reasons to change."</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle o">O</div>
        <div class="m1-v-text"><strong>if/else or switch on type/string</strong>Replace with polymorphism. New types = new classes. Strategy Pattern is the canonical fix.</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle l">L</div>
        <div class="m1-v-text"><strong>Subclass throws UnsupportedOperationException</strong>Redesign inheritance hierarchy. Use abstraction or composition instead.</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle l">L</div>
        <div class="m1-v-text"><strong>instanceof checks in polymorphic code</strong>Fix the inheritance hierarchy. Use proper polymorphism — callers should never check the type.</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle i">I</div>
        <div class="m1-v-text"><strong>Fat interface with 10+ methods</strong>Split into role-specific interfaces. Each client depends only on what it uses.</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle d">D</div>
        <div class="m1-v-text"><strong>new ConcreteClass() inside service/class</strong>Introduce an interface. Inject the dependency via constructor (or DI framework).</div>
      </div>
      <div class="m1-violation-item">
        <div class="m1-v-principle d">D</div>
        <div class="m1-v-text"><strong>Hard to unit test — can't mock dependencies</strong>Classic DIP violation. Introduce interface, inject dependency, mock in tests.</div>
      </div>
    </div>
  </div>

  <div class="m1-uml-container">
    <div class="m1-uml-title">📋 Interview One-Liners — Say These Verbatim</div>
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="display:flex;gap:16px;align-items:flex-start;padding:14px 16px;background:var(--m1-surf2);border-radius:8px;border-left:3px solid var(--m1-s);">
        <div style="font-family:'Fira Code',monospace;font-size:13px;font-weight:700;color:var(--m1-s);width:24px;flex-shrink:0;">S</div>
        <div style="font-size:13px;color:var(--m1-muted);">— <strong style="color:var(--m1-text)">"Each class has one reason to change"</strong> → enables Strategy, Template Method</div>
      </div>
      <div style="display:flex;gap:16px;align-items:flex-start;padding:14px 16px;background:var(--m1-surf2);border-radius:8px;border-left:3px solid var(--m1-o);">
        <div style="font-family:'Fira Code',monospace;font-size:13px;font-weight:700;color:var(--m1-o);width:24px;flex-shrink:0;">O</div>
        <div style="font-size:13px;color:var(--m1-muted);">— <strong style="color:var(--m1-text)">"Open for extension, closed for modification"</strong> → Strategy, Template Method</div>
      </div>
      <div style="display:flex;gap:16px;align-items:flex-start;padding:14px 16px;background:var(--m1-surf2);border-radius:8px;border-left:3px solid var(--m1-l);">
        <div style="font-family:'Fira Code',monospace;font-size:13px;font-weight:700;color:var(--m1-l);width:24px;flex-shrink:0;">L</div>
        <div style="font-size:13px;color:var(--m1-muted);">— <strong style="color:var(--m1-text)">"Subtypes must honour the parent's contract"</strong> → prevents bad inheritance</div>
      </div>
      <div style="display:flex;gap:16px;align-items:flex-start;padding:14px 16px;background:var(--m1-surf2);border-radius:8px;border-left:3px solid var(--m1-i);">
        <div style="font-family:'Fira Code',monospace;font-size:13px;font-weight:700;color:var(--m1-i);width:24px;flex-shrink:0;">I</div>
        <div style="font-size:13px;color:var(--m1-muted);">— <strong style="color:var(--m1-text)">"Many focused interfaces &gt; one fat interface"</strong> → enables clean composition</div>
      </div>
      <div style="display:flex;gap:16px;align-items:flex-start;padding:14px 16px;background:var(--m1-surf2);border-radius:8px;border-left:3px solid var(--m1-d);">
        <div style="font-family:'Fira Code',monospace;font-size:13px;font-weight:700;color:var(--m1-d);width:24px;flex-shrink:0;">D</div>
        <div style="font-size:13px;color:var(--m1-muted);">— <strong style="color:var(--m1-text)">"Depend on abstractions, not concretions"</strong> → Factory, DI containers</div>
      </div>
    </div>
  </div>
</div>

<!-- ===== VIEW 4: UML REFERENCE ===== -->
<div class="m1-view" id="m1-view-uml">
  <div class="m1-uml-container">
    <div class="m1-uml-title">CLASS DIAGRAM — Relationship Symbols</div>
    <div class="m1-rel-legend">
      <div class="m1-rel-item"><div class="m1-rel-symbol">A ────── B</div><div class="m1-rel-info"><div class="m1-rel-name">Association</div><div class="m1-rel-desc">A uses/knows B</div></div></div>
      <div class="m1-rel-item"><div class="m1-rel-symbol">A ◇──── B</div><div class="m1-rel-info"><div class="m1-rel-name">Aggregation</div><div class="m1-rel-desc">HAS-A (weak): B can exist without A</div></div></div>
      <div class="m1-rel-item"><div class="m1-rel-symbol">A ◆──── B</div><div class="m1-rel-info"><div class="m1-rel-name">Composition</div><div class="m1-rel-desc">HAS-A (strong): B cannot exist without A</div></div></div>
      <div class="m1-rel-item"><div class="m1-rel-symbol">A ────▷ B</div><div class="m1-rel-info"><div class="m1-rel-name">Inheritance</div><div class="m1-rel-desc">IS-A: A extends B (solid line)</div></div></div>
      <div class="m1-rel-item"><div class="m1-rel-symbol">A - - -▷ B</div><div class="m1-rel-info"><div class="m1-rel-name">Implementation</div><div class="m1-rel-desc">A implements interface B (dashed)</div></div></div>
      <div class="m1-rel-item"><div class="m1-rel-symbol">A - - -> B</div><div class="m1-rel-info"><div class="m1-rel-name">Dependency</div><div class="m1-rel-desc">A depends on B transitively</div></div></div>
    </div>
  </div>

  <div class="m1-uml-container">
    <div class="m1-uml-title">CLASS BOX NOTATION</div>
    <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">
      <div class="m1-uml-class">
        <div class="m1-uml-class-name">ClassName</div>
        <div class="m1-uml-class-section">
          <div class="m1-uml-attr"><span class="private">-</span>privateField: Type</div>
          <div class="m1-uml-attr"><span class="protected">#</span>protectedField: Type</div>
          <div class="m1-uml-attr"><span class="public">+</span>publicField: Type</div>
        </div>
        <div class="m1-uml-class-section">
          <div class="m1-uml-method">+ publicMethod(): Type</div>
          <div class="m1-uml-attr">- privateMethod(): void</div>
        </div>
      </div>
      <div class="m1-uml-class">
        <div class="m1-uml-class-name abstract">AbstractClass</div>
        <div class="m1-uml-class-section">
          <div class="m1-uml-attr"><span class="protected">#</span>state: int</div>
        </div>
        <div class="m1-uml-class-section">
          <div class="m1-uml-method">+ concreteMethod(): void</div>
          <div class="m1-uml-attr">+ abstractMethod(): void</div>
        </div>
      </div>
      <div class="m1-uml-class">
        <div class="m1-uml-class-name interface">&lt;&lt;interface&gt;&gt;<br>Printable</div>
        <div class="m1-uml-class-section">
          <div class="m1-uml-method">+ print(): void</div>
          <div class="m1-uml-method">+ scan(): void</div>
        </div>
      </div>
      <div style="font-size:12px;color:var(--m1-muted);font-family:'Fira Code',monospace;line-height:2;padding-top:8px;">
        <div><span style="color:var(--m1-bad)">-</span> = private</div>
        <div><span style="color:var(--m1-warn)">#</span> = protected</div>
        <div><span style="color:var(--m1-good)">+</span> = public</div>
        <div style="margin-top:8px;color:var(--m1-muted)">Multiplicities:</div>
        <div>1 &nbsp;&nbsp; exactly one</div>
        <div>0..1  zero or one</div>
        <div>* &nbsp;&nbsp; zero or more</div>
        <div>1..* one or more</div>
      </div>
    </div>
  </div>

  <div class="m1-uml-container">
    <div class="m1-uml-title">SEQUENCE DIAGRAM NOTATION</div>
    <div style="background:#141c2e;padding:20px 16px 16px;border-radius:8px;overflow-x:auto;">
      <svg viewBox="0 0 660 295" style="width:100%;min-width:500px;font-family:'Fira Code',monospace;" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="a1-arr-sync" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#00e5ff"/>
          </marker>
          <marker id="a1-arr-ret" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#69ff47"/>
          </marker>
        </defs>

        <!-- ── Actor boxes ─────────────────────────────────── -->
        <!-- Customer x=80 -->
        <rect x="35" y="8" width="90" height="26" rx="4" fill="#1e2a40" stroke="#263450"/>
        <text x="80" y="25" text-anchor="middle" fill="#d4deff" font-size="11">Customer</text>

        <!-- OrderSvc x=240 -->
        <rect x="195" y="8" width="90" height="26" rx="4" fill="#001e2e" stroke="#00e5ff" stroke-width="1.5"/>
        <text x="240" y="25" text-anchor="middle" fill="#00e5ff" font-size="11">OrderSvc</text>

        <!-- PaymentSvc x=400 -->
        <rect x="352" y="8" width="96" height="26" rx="4" fill="#1e2a40" stroke="#263450"/>
        <text x="400" y="25" text-anchor="middle" fill="#d4deff" font-size="11">PaymentSvc</text>

        <!-- EmailSvc x=570 -->
        <rect x="525" y="8" width="90" height="26" rx="4" fill="#1e2a40" stroke="#263450"/>
        <text x="570" y="25" text-anchor="middle" fill="#d4deff" font-size="11">EmailSvc</text>

        <!-- ── Lifelines ────────────────────────────────────── -->
        <line x1="80"  y1="34" x2="80"  y2="260" stroke="#263450" stroke-dasharray="4,3"/>
        <line x1="240" y1="34" x2="240" y2="260" stroke="#00e5ff" stroke-dasharray="4,3" opacity="0.35"/>
        <line x1="400" y1="34" x2="400" y2="260" stroke="#263450" stroke-dasharray="4,3"/>
        <line x1="570" y1="34" x2="570" y2="260" stroke="#263450" stroke-dasharray="4,3"/>

        <!-- ── Messages ──────────────────────────────────────── -->
        <!-- 1. Customer → OrderSvc : placeOrder(cart) -->
        <line x1="82" y1="65" x2="233" y2="65" stroke="#00e5ff" stroke-width="1.5" marker-end="url(#a1-arr-sync)"/>
        <text x="157" y="60" text-anchor="middle" fill="#00e5ff" font-size="10">placeOrder(cart)</text>

        <!-- 2. OrderSvc → PaymentSvc : validatePayment(card) -->
        <line x1="242" y1="98" x2="393" y2="98" stroke="#00e5ff" stroke-width="1.5" marker-end="url(#a1-arr-sync)"/>
        <text x="317" y="93" text-anchor="middle" fill="#00e5ff" font-size="10">validatePayment(card)</text>

        <!-- 3. PaymentSvc → OrderSvc : paymentConfirmed  [return] -->
        <line x1="398" y1="131" x2="247" y2="131" stroke="#69ff47" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#a1-arr-ret)"/>
        <text x="322" y="126" text-anchor="middle" fill="#69ff47" font-size="10">paymentConfirmed</text>

        <!-- 4. OrderSvc → EmailSvc : sendEmail(email) -->
        <line x1="242" y1="164" x2="563" y2="164" stroke="#00e5ff" stroke-width="1.5" marker-end="url(#a1-arr-sync)"/>
        <text x="403" y="159" text-anchor="middle" fill="#00e5ff" font-size="10">sendEmail(email)</text>

        <!-- 5. EmailSvc → OrderSvc : sent  [return] -->
        <line x1="568" y1="197" x2="247" y2="197" stroke="#69ff47" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#a1-arr-ret)"/>
        <text x="406" y="192" text-anchor="middle" fill="#69ff47" font-size="10">sent</text>

        <!-- 6. OrderSvc → Customer : orderId  [return] -->
        <line x1="238" y1="230" x2="87" y2="230" stroke="#69ff47" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#a1-arr-ret)"/>
        <text x="160" y="225" text-anchor="middle" fill="#69ff47" font-size="10">orderId</text>

        <!-- ── Legend ──────────────────────────────────────────── -->
        <line x1="36" y1="273" x2="66" y2="273" stroke="#00e5ff" stroke-width="1.5" marker-end="url(#a1-arr-sync)"/>
        <text x="73" y="277" fill="#7888b8" font-size="10">synchronous call</text>
        <line x1="210" y1="273" x2="240" y2="273" stroke="#69ff47" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#a1-arr-ret)"/>
        <text x="247" y="277" fill="#7888b8" font-size="10">return / async</text>
        <rect x="380" y="265" width="88" height="16" rx="3" fill="none" stroke="rgba(255,184,0,0.4)"/>
        <text x="424" y="277" text-anchor="middle" fill="#ffb800" font-size="10">alt [condition]</text>
        <text x="476" y="277" fill="#7888b8" font-size="10">= conditional block</text>
      </svg>
    </div>
  </div>
</div>

<!-- ===== VIEW 5: PARKING LOT ===== -->
<div class="m1-view" id="m1-view-parking">
  <div class="m1-uml-container">
    <div class="m1-uml-title">REFACTORED PARKING LOT — UML Class Diagram (SOLID-compliant)</div>
    <div class="m1-parking-diagram">

      <!-- ParkingLot -->
      <div class="m1-parking-row">
        <div class="m1-uml-class" style="min-width:200px;">
          <div class="m1-uml-class-name">ParkingLot</div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-attr"><span class="private">-</span>name: String</div>
            <div class="m1-uml-attr"><span class="private">-</span>capacity: int</div>
          </div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-method">+ park(vehicle): Ticket</div>
            <div class="m1-uml-method">+ unpark(ticket): Bill</div>
          </div>
        </div>
      </div>

      <div class="m1-parking-connector">
        <div class="m1-connector-diamond"></div>
        <div class="m1-connector-line"></div>
        <div style="font-size:10px">1..*</div>
      </div>

      <!-- Floor -->
      <div class="m1-parking-row">
        <div class="m1-uml-class" style="min-width:200px;">
          <div class="m1-uml-class-name">ParkingFloor</div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-attr"><span class="private">-</span>floorNum: int</div>
          </div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-method">+ getAvailableSpot(): ParkingSpot</div>
          </div>
        </div>
      </div>

      <div class="m1-parking-connector">
        <div class="m1-connector-diamond"></div>
        <div class="m1-connector-line"></div>
        <div style="font-size:10px">1..*</div>
      </div>

      <!-- Spots row -->
      <div class="m1-parking-row">
        <div class="m1-uml-class" style="min-width:180px;">
          <div class="m1-uml-class-name abstract">ParkingSpot</div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-attr"><span class="private">-</span>spotNum: int</div>
            <div class="m1-uml-attr"><span class="private">-</span>occupied: bool</div>
          </div>
          <div class="m1-uml-class-section">
            <div class="m1-uml-method">+ canFit(v): bool</div>
            <div class="m1-uml-method">+ isAvailable(): bool</div>
          </div>
        </div>
        <div style="width:48px;display:flex;align-items:center;justify-content:center;font-family:'Fira Code',monospace;font-size:14px;color:var(--m1-muted)">◁</div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div class="m1-uml-class"><div class="m1-uml-class-name">CarSpot</div><div class="m1-uml-class-section"><div class="m1-uml-method">+canFit(v): bool</div></div></div>
          <div class="m1-uml-class"><div class="m1-uml-class-name">BikeSpot</div><div class="m1-uml-class-section"><div class="m1-uml-method">+canFit(v): bool</div></div></div>
          <div class="m1-uml-class"><div class="m1-uml-class-name">TruckSpot</div><div class="m1-uml-class-section"><div class="m1-uml-method">+canFit(v): bool</div></div></div>
        </div>
        <div style="width:48px;"></div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div class="m1-uml-class"><div class="m1-uml-class-name interface">&lt;&lt;interface&gt;&gt;<br>PricingStrategy</div><div class="m1-uml-class-section"><div class="m1-uml-method">+ calculateFee(h): double</div></div></div>
          <div class="m1-uml-class"><div class="m1-uml-class-name">HourlyPricing</div><div class="m1-uml-class-section"><div class="m1-uml-method">+ calculateFee(h): double</div></div></div>
          <div class="m1-uml-class"><div class="m1-uml-class-name">FlatRatePricing</div><div class="m1-uml-class-section"><div class="m1-uml-method">+ calculateFee(h): double</div></div></div>
        </div>
      </div>

      <div class="m1-parking-row">
        <div style="background:rgba(255,184,0,0.06);border:1px solid rgba(255,184,0,0.2);border-radius:8px;padding:16px 20px;font-size:12px;color:var(--m1-l);font-family:'Fira Code',monospace;max-width:560px;text-align:center;line-height:1.7;">
          SRP: ParkingLot, Floor, Spot, Ticket, Bill, PricingStrategy all separate<br>
          OCP: New vehicle type = new Spot subclass, zero modifications to existing<br>
          DIP: PricingStrategy injected — swap hourly/flat without changing Spot<br>
          LSP: All Spot subtypes honour canFit() contract — no UnsupportedOperation
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ===== VIEW 6: TASKS ===== -->
<div class="m1-view" id="m1-view-tasks">
  <div class="m1-task-grid">

    <div class="m1-task-card">
      <div class="m1-task-head" onclick="m1ToggleTask(this)">
        <div class="m1-task-num">TASK 01</div>
        <div class="m1-task-label">SOLID Violation Hunt — 4 Snippets</div>
        <div class="m1-task-meta">~2 hrs · identify + fix</div>
        <div class="m1-task-chevron">›</div>
      </div>
      <div class="m1-task-body">
        <p>For each snippet: name the principle violated, explain why, and write the fixed version.</p>
        <pre>// Snippet A — which principle?
class Report {
  String generateHTML() { ... }
  String generatePDF() { ... }
  void saveToFile(String path) { ... }
  void uploadToS3() { ... }
  void emailReport(String to) { ... }
}

// Snippet B — which principle?
class Square extends Rectangle {
  void setWidth(int w)  { this.width=w; this.height=w; }
  void setHeight(int h) { this.width=h; this.height=h; }
}

// Snippet C — which principle?
interface Printable {
  void print(); void scan(); void fax(); void copy();
}
class BasicPrinter implements Printable {
  void print() { ... }
  void scan()  { throw new UnsupportedOperationException(); }
  void fax()   { throw new UnsupportedOperationException(); }
  void copy()  { throw new UnsupportedOperationException(); }
}

// Snippet D — which principle?
class NotificationService {
  void notify(String type, String message) {
    if (type.equals("EMAIL")) sendEmail(message);
    else if (type.equals("SMS")) sendSMS(message);
    else if (type.equals("PUSH")) sendPush(message);
  }
}</pre>
      </div>
    </div>

    <div class="m1-task-card">
      <div class="m1-task-head" onclick="m1ToggleTask(this)">
        <div class="m1-task-num">TASK 02</div>
        <div class="m1-task-label">UML Class Diagram — Library Management System</div>
        <div class="m1-task-meta">~1.5 hrs · diagram</div>
        <div class="m1-task-chevron">›</div>
      </div>
      <div class="m1-task-body">
        <p>Draw the UML class diagram with these entities. Include all attributes, methods, relationships with correct symbols, and multiplicities.</p>
        <pre>Entities: Library, Member, Book, BookCopy, Loan, Librarian

Requirements:
- A Library has many Members and many BookCopies
- A Book can have multiple BookCopies
- A Loan connects a Member to a BookCopy (with dates)
- A Librarian manages loans
- Members have a borrowing limit (max 3 books)
- BookCopy has status: AVAILABLE, BORROWED, RESERVED

Include: composition vs aggregation distinction
         inheritance if Librarian IS-A Member
         all multiplicities on every relationship</pre>
      </div>
    </div>

    <div class="m1-task-card">
      <div class="m1-task-head" onclick="m1ToggleTask(this)">
        <div class="m1-task-num">TASK 03</div>
        <div class="m1-task-label">Sequence Diagram — E-Commerce Order Flow</div>
        <div class="m1-task-meta">~1 hr · diagram</div>
        <div class="m1-task-chevron">›</div>
      </div>
      <div class="m1-task-body">
        <p>Draw a sequence diagram for the complete order placement flow including the failure path.</p>
        <pre>Actors: Customer, OrderService, PaymentService,
        InventoryService, EmailService

Happy path:
1. Customer → OrderService: placeOrder(cart)
2. OrderService → PaymentService: validatePayment(card)
3. PaymentService → OrderService: paymentConfirmed
4. OrderService → InventoryService: reserveItems(cart)
5. InventoryService → OrderService: reservationId
6. OrderService → EmailService: sendConfirmation(email)
7. OrderService → Customer: orderId

Also model: what happens when payment fails?
            Show the failure path as an alt block</pre>
      </div>
    </div>

    <div class="m1-task-card">
      <div class="m1-task-head" onclick="m1ToggleTask(this)">
        <div class="m1-task-num star">⭐ PROJECT</div>
        <div class="m1-task-label">Parking Lot Refactoring — Full LLD Exercise</div>
        <div class="m1-task-meta">~4 hrs · code + diagram</div>
        <div class="m1-task-chevron">›</div>
      </div>
      <div class="m1-task-body">
        <p>The violating code below has multiple SOLID violations. List every violation with line references, produce refactored Java code, and draw the UML class diagram of your solution.</p>
        <pre>class ParkingLot {
  private int totalSpots = 100;
  private int occupiedSpots = 0;
  private List&lt;String[]&gt; parkedVehicles = new ArrayList&lt;&gt;();

  public String parkVehicle(String vehicleType, String plate) {
    if (occupiedSpots &gt;= totalSpots) return "Lot is full";

    // ← VIOLATION: what principle? why?
    double rate;
    if (vehicleType.equals("CAR"))   rate = 20.0;
    else if (vehicleType.equals("BIKE"))  rate = 10.0;
    else if (vehicleType.equals("TRUCK")) rate = 40.0;
    else return "Unknown vehicle type";

    // ← VIOLATION: what principle? why?
    String ticketId = "T" + System.currentTimeMillis();
    parkedVehicles.add(new String[]{ticketId, plate,
      vehicleType, String.valueOf(System.currentTimeMillis()),
      String.valueOf(rate)});
    occupiedSpots++;

    // ← VIOLATION: what principle? why?
    System.out.println("Parked " + vehicleType);

    // ← VIOLATION: what principle? why?
    saveToDatabase(ticketId, plate);
    return ticketId;
  }

  private void saveToDatabase(String id, String plate) {
    System.out.println("Saving to MySQL: " + id);  // hardcoded!
  }

  public double calculateBill(String ticketId) {
    // billing logic crammed here ← VIOLATION: what principle?
    for (String[] v : parkedVehicles) {
      if (v[0].equals(ticketId)) {
        long entry = Long.parseLong(v[3]);
        double hours = (System.currentTimeMillis()-entry)/3600000.0;
        double rate  = Double.parseDouble(v[4]);
        return Math.ceil(hours) * rate;
      }
    }
    return 0;
  }
}

Deliverable:
1. List each violation (principle + explanation)
2. Refactored Java code (multiple classes)
3. UML class diagram of the refactored design</pre>
      </div>
    </div>

  </div>
</div>

<!-- ===== VIEW 7: CHECKLIST ===== -->
<div class="m1-view" id="m1-view-checklist">
  <div class="m1-progress-wrap">
    <div class="m1-progress-info">
      <span id="m1-prog-label">0 / 9 completed</span>
      <span style="color:var(--m1-s)">A1 → SOLID + OOP + UML</span>
    </div>
    <div class="m1-progress-track"><div class="m1-progress-fill" id="m1-prog-fill"></div></div>
  </div>

  <div class="m1-checklist">
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Can explain all 5 SOLID principles from memory without notes</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Can identify SOLID violations in code and name the exact principle</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Know all 4 OOP pillars and can give a concrete example of each</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Can draw UML class diagrams with correct notation: ◆ ◇ ▷ dashed</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Understand composition vs aggregation vs association distinction</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">Can draw sequence diagrams with lifelines, messages, and alt blocks</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">✏️ Task 1: All 4 SOLID violation snippets fixed with principle named</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">✏️ Task 2 + 3: Library UML + E-Commerce sequence diagram drawn</div></div>
    <div class="m1-chk" onclick="m1Toggle(this)"><div class="m1-chk-box"></div><div class="m1-chk-label">✏️ Mini Project: Parking Lot violations listed + refactored code + UML</div></div>
  </div>

  <div style="margin-top:28px;padding:20px 24px;background:var(--m1-surface);border:1px solid var(--m1-border);border-radius:10px;border-top:2px solid var(--m1-o);">
    <div style="font-family:'Fira Code',monospace;font-size:11px;color:var(--m1-muted);letter-spacing:1px;margin-bottom:8px;">NEXT MODULE</div>
    <div style="font-size:15px;font-weight:700;color:var(--m1-bright);margin-bottom:6px;">A2 — Creational Design Patterns</div>
    <div style="font-size:13px;color:var(--m1-muted);line-height:1.6;">Singleton, Factory, Abstract Factory, Builder, Prototype — each mapped to a real system. Mini Project: ATM System design using Creational patterns.</div>
  </div>
</div>

</div><!-- end .m1-content -->

<!-- ── BOTTOM NAV ─────────────────────────────────────────────── -->
<div class="m1-bottom-nav" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--m1-border);padding-top:20px;">
  <a href="/learning/system-design/foundation/phase0-foundation/" class="m1-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--m1-border);border-radius:4px;color:var(--m1-muted);text-decoration:none;">← PREVIOUS: PHASE 0</a>
  <a href="/learning/system-design/lld/module-a1-notes/" class="m1-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--m1-s);color:var(--m1-s);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" class="m1-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--m1-border);border-radius:4px;color:var(--m1-muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a2-creational/" class="m1-nav-footer-btn" style="padding:12px 24px;background:var(--m1-s);color:var(--m1-bg);border-radius:4px;text-decoration:none;font-weight:600;">NEXT: LLD A2 →</a>
</div>

</div><!-- end .m1-page -->
