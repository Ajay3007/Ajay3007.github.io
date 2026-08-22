---
title: "Module A4 — Behavioral Patterns"
description: "Track A · LLD · Module A4 · Weeks 6–7 Behavioral Patterns 12 patterns · 2 weeks · BookMyShow mini project Strategy Observer Chain of Resp."
domain: system-design
track: system-design-lld
order: 8
url: /learning/system-design/lld/module-a4-behavioral/
---

<div class="m4-page">
<header class="m4-header">
  <div class="m4-eyebrow">Track A · LLD · Module A4 · Weeks 6–7</div>
  <h1>Behavioral<br><em>Patterns</em></h1>
  <div class="m4-h-count">12 patterns · 2 weeks · BookMyShow mini project</div>
  <div class="m4-pill-strip">
    <div class="m4-p-pill" style="color:var(--p1);border-color:rgba(126,200,80,0.2)">Strategy</div>
    <div class="m4-p-pill" style="color:var(--p2);border-color:rgba(80,200,120,0.2)">Observer</div>
    <div class="m4-p-pill" style="color:var(--p3);border-color:rgba(80,200,160,0.2)">Chain of Resp.</div>
    <div class="m4-p-pill" style="color:var(--p4);border-color:rgba(74,184,200,0.2)">State</div>
    <div class="m4-p-pill" style="color:var(--p5);border-color:rgba(96,143,223,0.2)">Command</div>
    <div class="m4-p-pill" style="color:var(--p6);border-color:rgba(144,112,208,0.2)">Template Method</div>
    <div class="m4-p-pill" style="color:var(--p7);border-color:rgba(192,96,176,0.2)">Iterator</div>
    <div class="m4-p-pill" style="color:var(--p8);border-color:rgba(208,80,112,0.2)">Mediator</div>
    <div class="m4-p-pill" style="color:var(--p9);border-color:rgba(208,128,64,0.2)">Memento</div>
    <div class="m4-p-pill" style="color:var(--p10);border-color:rgba(200,184,48,0.2)">Visitor</div>
    <div class="m4-p-pill" style="color:var(--p11);border-color:rgba(128,200,64,0.2)">Null Object</div>
    <div class="m4-p-pill" style="color:var(--p12);border-color:rgba(64,184,160,0.2)">Interpreter</div>
  </div>
</header>

<nav class="m4-nav">
  <div class="m4-nav-tab active" onclick="m4Show('overview',this)">Overview</div>
  <div class="m4-nav-tab" onclick="m4Show('patterns',this)">Deep Dives</div>
  <div class="m4-nav-tab" onclick="m4Show('compare',this)">Distinctions</div>
  <div class="m4-nav-tab" onclick="m4Show('state',this)">State Machine</div>
  <div class="m4-nav-tab" onclick="m4Show('bms',this)">BookMyShow</div>
  <div class="m4-nav-tab" onclick="m4Show('tasks',this)">Tasks</div>
  <div class="m4-nav-tab" onclick="m4Show('checklist',this)">Checklist</div>
</nav>

<div class="m4-content">

<!-- ===== OVERVIEW ===== -->
<div class="m4-view active" id="m4-view-overview">
  <p style="font-size:14px;color:var(--muted);line-height:1.8;max-width:720px;margin-bottom:28px;">
    Behavioral patterns deal with <strong style="color:var(--bright)">algorithms and object communication</strong> — how responsibilities are distributed and how objects interact. Click any card to jump to its deep dive.
  </p>

  <div class="m4-group-label" style="--color:var(--p1)">Week 6 — Core Six</div>
  <div class="m4-ov-grid" style="margin-bottom:16px;">
    <div class="m4-ov-card" onclick="m4GoToPattern(0)" style="">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p1)"></div>
      <div class="m4-ov-num">01</div><div class="m4-ov-name">Strategy</div>
      <div class="m4-ov-sys">→ Payment System</div>
      <div class="m4-ov-gist">Swap algorithms at runtime via interface</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(1)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p2)"></div>
      <div class="m4-ov-num">02</div><div class="m4-ov-name">Observer</div>
      <div class="m4-ov-sys">→ Stock Ticker</div>
      <div class="m4-ov-gist">One-to-many auto notification on state change</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(2)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p3)"></div>
      <div class="m4-ov-num">03</div><div class="m4-ov-name">Chain of Resp.</div>
      <div class="m4-ov-sys">→ ATM Dispenser</div>
      <div class="m4-ov-gist">Pass request along chain until handled</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(3)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p4)"></div>
      <div class="m4-ov-num">04</div><div class="m4-ov-name">State</div>
      <div class="m4-ov-sys">→ Vending Machine</div>
      <div class="m4-ov-gist">Behaviour changes as internal state changes</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(4)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p5)"></div>
      <div class="m4-ov-num">05</div><div class="m4-ov-name">Command</div>
      <div class="m4-ov-sys">→ Smart Home</div>
      <div class="m4-ov-gist">Encapsulate requests as objects. Enables undo.</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(5)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p6)"></div>
      <div class="m4-ov-num">06</div><div class="m4-ov-name">Template Method</div>
      <div class="m4-ov-sys">→ Data Migration</div>
      <div class="m4-ov-gist">Fixed skeleton; defer steps to subclass</div>
    </div>
  </div>

  <div class="m4-group-label">Week 7 — Supporting Six</div>
  <div class="m4-ov-grid">
    <div class="m4-ov-card" onclick="m4GoToPattern(6)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p7)"></div>
      <div class="m4-ov-num">07</div><div class="m4-ov-name">Iterator</div>
      <div class="m4-ov-sys">→ Custom Playlist</div>
      <div class="m4-ov-gist">Traverse collection without exposing internals</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(7)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p8)"></div>
      <div class="m4-ov-num">08</div><div class="m4-ov-name">Mediator</div>
      <div class="m4-ov-sys">→ Air Traffic Control</div>
      <div class="m4-ov-gist">Central hub decouples many-to-many peers</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(8)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p9)"></div>
      <div class="m4-ov-num">09</div><div class="m4-ov-name">Memento</div>
      <div class="m4-ov-sys">→ Text Editor Undo</div>
      <div class="m4-ov-gist">Snapshot state for undo without breaking encapsulation</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(9)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p10)"></div>
      <div class="m4-ov-num">10</div><div class="m4-ov-name">Visitor</div>
      <div class="m4-ov-sys">→ Tax Calculator</div>
      <div class="m4-ov-gist">New operations without modifying element classes</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(10)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p11)"></div>
      <div class="m4-ov-num">11</div><div class="m4-ov-name">Null Object</div>
      <div class="m4-ov-sys">→ Logger</div>
      <div class="m4-ov-gist">Default no-op object eliminates null checks everywhere</div>
    </div>
    <div class="m4-ov-card" onclick="m4GoToPattern(11)">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--p12)"></div>
      <div class="m4-ov-num">12</div><div class="m4-ov-name">Interpreter</div>
      <div class="m4-ov-sys">→ Math Expr. Parser</div>
      <div class="m4-ov-gist">Evaluate grammar-based expressions / DSL rules</div>
    </div>
  </div>

  <table class="m4-cmp-table" style="margin-top:24px;">
    <thead><tr><th>PATTERN</th><th>TRIGGER / SMELL</th><th>KEY MECHANISM</th><th>SOLID PRINCIPLE</th></tr></thead>
    <tbody>
      <tr><td style="color:var(--p1)">Strategy</td><td>if/else branching on algorithm type</td><td>Inject strategy via interface</td><td>OCP, DIP</td></tr>
      <tr><td style="color:var(--p2)">Observer</td><td>One change → notify many dependents</td><td>Register/notify observers</td><td>OCP, SRP</td></tr>
      <tr><td style="color:var(--p3)">Chain of Resp.</td><td>Multiple potential handlers, unknown upfront</td><td>Handlers form a linked chain</td><td>SRP, OCP</td></tr>
      <tr><td style="color:var(--p4)">State</td><td>switch/if on growing state field</td><td>State objects hold behaviour; context delegates</td><td>SRP, OCP</td></tr>
      <tr><td style="color:var(--p5)">Command</td><td>Need undo/redo, queue, or logging of ops</td><td>Command objects with execute() + undo()</td><td>SRP, OCP</td></tr>
      <tr><td style="color:var(--p6)">Template Method</td><td>Same algorithm, different step implementations</td><td>Abstract class; subclasses override steps</td><td>OCP, DRY</td></tr>
      <tr><td style="color:var(--p7)">Iterator</td><td>Need sequential access to collection internals</td><td>Iterator object with hasNext/next</td><td>SRP</td></tr>
      <tr><td style="color:var(--p8)">Mediator</td><td>N objects all talk directly → N² connections</td><td>All communication routes through mediator</td><td>SRP, DIP</td></tr>
      <tr><td style="color:var(--p9)">Memento</td><td>Need save/restore state without exposing internals</td><td>Originator creates opaque Memento; Caretaker stores it</td><td>Encapsulation</td></tr>
      <tr><td style="color:var(--p10)">Visitor</td><td>Many operations on stable class hierarchy</td><td>accept(visitor) → double dispatch</td><td>OCP, SRP</td></tr>
      <tr><td style="color:var(--p11)">Null Object</td><td>Null checks scattered everywhere</td><td>No-op implementation of same interface</td><td>SRP, LSP</td></tr>
      <tr><td style="color:var(--p12)">Interpreter</td><td>Building expression evaluator or DSL</td><td>Grammar as class hierarchy; interpret(context)</td><td>OCP</td></tr>
    </tbody>
  </table>
</div>

<!-- ===== PATTERN DEEP DIVES ===== -->
<div class="m4-view" id="m4-view-patterns">
  <div class="m4-pat-tabs">
    <div class="m4-pt-btn active" id="m4-pb0" onclick="m4SelPat(0)" style="border-top:3px solid var(--p1)"><span class="m4-btn-num" style="color:var(--p1)">01</span>Strategy</div>
    <div class="m4-pt-btn" id="m4-pb1" onclick="m4SelPat(1)" style="border-top:3px solid var(--p2)"><span class="m4-btn-num" style="color:var(--p2)">02</span>Observer</div>
    <div class="m4-pt-btn" id="m4-pb2" onclick="m4SelPat(2)" style="border-top:3px solid var(--p3)"><span class="m4-btn-num" style="color:var(--p3)">03</span>Chain</div>
    <div class="m4-pt-btn" id="m4-pb3" onclick="m4SelPat(3)" style="border-top:3px solid var(--p4)"><span class="m4-btn-num" style="color:var(--p4)">04</span>State</div>
    <div class="m4-pt-btn" id="m4-pb4" onclick="m4SelPat(4)" style="border-top:3px solid var(--p5)"><span class="m4-btn-num" style="color:var(--p5)">05</span>Command</div>
    <div class="m4-pt-btn" id="m4-pb5" onclick="m4SelPat(5)" style="border-top:3px solid var(--p6)"><span class="m4-btn-num" style="color:var(--p6)">06</span>Template</div>
    <div class="m4-pt-btn" id="m4-pb6" onclick="m4SelPat(6)" style="border-top:3px solid var(--p7)"><span class="m4-btn-num" style="color:var(--p7)">07</span>Iterator</div>
    <div class="m4-pt-btn" id="m4-pb7" onclick="m4SelPat(7)" style="border-top:3px solid var(--p8)"><span class="m4-btn-num" style="color:var(--p8)">08</span>Mediator</div>
    <div class="m4-pt-btn" id="m4-pb8" onclick="m4SelPat(8)" style="border-top:3px solid var(--p9)"><span class="m4-btn-num" style="color:var(--p9)">09</span>Memento</div>
    <div class="m4-pt-btn" id="m4-pb9" onclick="m4SelPat(9)" style="border-top:3px solid var(--p10)"><span class="m4-btn-num" style="color:var(--p10)">10</span>Visitor</div>
    <div class="m4-pt-btn" id="m4-pb10" onclick="m4SelPat(10)" style="border-top:3px solid var(--p11)"><span class="m4-btn-num" style="color:var(--p11)">11</span>Null Obj</div>
    <div class="m4-pt-btn" id="m4-pb11" onclick="m4SelPat(11)" style="border-top:3px solid var(--p12)"><span class="m4-btn-num" style="color:var(--p12)">12</span>Interpret</div>
  </div>

  <!-- 01 STRATEGY -->
  <div class="m4-pat-panel active" id="m4-pp0">
    <div class="m4-p-mast" style="--c:var(--p1)"><div class="m4-p-mast::before" style="background:var(--p1)"></div><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p1);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">01</div>
      <div class="m4-p-name">Strategy</div>
      <div class="m4-p-sys">REAL SYSTEM → Payment System (UPI / Card / Wallet)</div>
      <div class="m4-p-intent" style="border-left-color:var(--p1)">Define a family of algorithms, encapsulate each, make them interchangeable. Algorithm varies independently from the client. Eliminates if/else on algorithm type.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">PaymentStrategy.java<span class="m4-clang" style="color:var(--p1)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">PaymentStrategy</span> {
    <span class="m4-kw">boolean</span> <span class="m4-fn">pay</span>(<span class="m4-kw">double</span> amount);
}
<span class="m4-kw">class</span> <span class="m4-cls">UPIPayment</span> <span class="m4-kw">implements</span> <span class="m4-cls">PaymentStrategy</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">String</span> upiId;
    <span class="m4-kw">public boolean</span> <span class="m4-fn">pay</span>(<span class="m4-kw">double</span> amt) {
        <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Paid ₹"</span>+amt+<span class="m4-str">" via UPI: "</span>+upiId); <span class="m4-kw">return true</span>;
    }
}
<span class="m4-kw">class</span> <span class="m4-cls">WalletPayment</span> <span class="m4-kw">implements</span> <span class="m4-cls">PaymentStrategy</span> {
    <span class="m4-kw">private double</span> balance;
    <span class="m4-kw">public boolean</span> <span class="m4-fn">pay</span>(<span class="m4-kw">double</span> amt) {
        <span class="m4-kw">if</span> (balance &lt; amt) { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Insufficient"</span>); <span class="m4-kw">return false</span>; }
        balance -= amt; <span class="m4-kw">return true</span>;
    }
}

<span class="m4-cm">// Context — knows nothing about UPI/Wallet internals</span>
<span class="m4-kw">class</span> <span class="m4-cls">ShoppingCart</span> {
    <span class="m4-kw">private</span> <span class="m4-cls">PaymentStrategy</span> strategy;

    <span class="m4-kw">public void</span> <span class="m4-fn">setStrategy</span>(<span class="m4-cls">PaymentStrategy</span> s) { <span class="m4-kw">this</span>.strategy = s; }

    <span class="m4-kw">public boolean</span> <span class="m4-fn">checkout</span>() {
        <span class="m4-kw">return</span> strategy.<span class="m4-fn">pay</span>(<span class="m4-fn">getTotal</span>()); <span class="m4-cm">// Delegates — no if/else</span>
    }
}

<span class="m4-cm">// Swap algorithm at runtime:</span>
cart.<span class="m4-fn">setStrategy</span>(<span class="m4-kw">new</span> <span class="m4-cls">UPIPayment</span>(<span class="m4-str">"ajay@icici"</span>));  cart.<span class="m4-fn">checkout</span>();
cart.<span class="m4-fn">setStrategy</span>(<span class="m4-kw">new</span> <span class="m4-cls">WalletPayment</span>(<span class="m4-str">"PAYTM"</span>, <span class="m4-str">500</span>)); cart.<span class="m4-fn">checkout</span>();</pre></div>
    <div class="m4-tip-box"><em>Interview:</em> Strategy is OCP in action. Every if/else on algorithm type is a Strategy violation. When asked "how do you add a new payment method without changing existing m4-code?" — this is the answer.</div>
  </div>

  <!-- 02 OBSERVER -->
  <div class="m4-pat-panel" id="m4-pp1">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p2);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">02</div>
      <div class="m4-p-name">Observer</div>
      <div class="m4-p-sys">REAL SYSTEM → Stock Ticker / Event Bus</div>
      <div class="m4-p-intent" style="border-left-color:var(--p2)">Define a one-to-many dependency: when subject changes state, all observers are notified automatically. Decouples publisher from subscribers — neither knows about the other's implementation.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">StockTicker.java<span class="m4-clang" style="color:var(--p2)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">StockObserver</span> {
    <span class="m4-kw">void</span> <span class="m4-fn">update</span>(<span class="m4-cls">String</span> symbol, <span class="m4-kw">double</span> price, <span class="m4-kw">double</span> changePct);
}

<span class="m4-kw">class</span> <span class="m4-cls">StockTicker</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">List</span>&lt;<span class="m4-cls">StockObserver</span>&gt; observers = <span class="m4-kw">new</span> <span class="m4-cls">ArrayList</span>&lt;&gt;();
    <span class="m4-kw">private final</span> <span class="m4-cls">Map</span>&lt;<span class="m4-cls">String</span>, <span class="m4-cls">Double</span>&gt; prices = <span class="m4-kw">new</span> <span class="m4-cls">HashMap</span>&lt;&gt;();

    <span class="m4-kw">public void</span> <span class="m4-fn">subscribe</span>(<span class="m4-cls">StockObserver</span> o)   { observers.add(o); }
    <span class="m4-kw">public void</span> <span class="m4-fn">unsubscribe</span>(<span class="m4-cls">StockObserver</span> o) { observers.remove(o); }

    <span class="m4-kw">public void</span> <span class="m4-fn">updatePrice</span>(<span class="m4-cls">String</span> sym, <span class="m4-kw">double</span> newPrice) {
        <span class="m4-kw">double</span> old = prices.getOrDefault(sym, newPrice);
        <span class="m4-kw">double</span> pct = ((newPrice - old) / old) * <span class="m4-str">100</span>;
        prices.put(sym, newPrice);
        <span class="m4-cm">// PUSH model: send data directly to observers</span>
        observers.forEach(o -> o.<span class="m4-fn">update</span>(sym, newPrice, pct));
    }
}

<span class="m4-cm">// Concrete observers — totally independent of each other</span>
<span class="m4-kw">class</span> <span class="m4-cls">MobileApp</span> <span class="m4-kw">implements</span> <span class="m4-cls">StockObserver</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">update</span>(<span class="m4-cls">String</span> s, <span class="m4-kw">double</span> p, <span class="m4-kw">double</span> chg) {
        <span class="m4-cls">System</span>.out.printf(<span class="m4-str">"[App] %s: ₹%.2f (%+.2f%%)%n"</span>, s, p, chg);
    }
}
<span class="m4-kw">class</span> <span class="m4-cls">AlertService</span> <span class="m4-kw">implements</span> <span class="m4-cls">StockObserver</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">update</span>(<span class="m4-cls">String</span> s, <span class="m4-kw">double</span> p, <span class="m4-kw">double</span> chg) {
        <span class="m4-kw">if</span> (<span class="m4-cls">Math</span>.abs(chg) &gt; <span class="m4-str">5.0</span>) <span class="m4-cls">System</span>.out.println(<span class="m4-str">"🚨 BIG MOVE: "</span>+s);
    }
}</pre></div>
    <div class="m4-use-row">
      <div class="m4-use-box yes"><h4 style="color:var(--p2)">Push vs Pull</h4><ul><li><strong>Push:</strong> subject sends data in update(). Simpler, observer always has data.</li><li><strong>Pull:</strong> subject calls update(this). Observer fetches what it needs. More flexible.</li></ul></div>
      <div class="m4-use-box"><h4>Real-world Observers</h4><ul style="list-style:none"><li style="padding:3px 0;font-size:11px;color:var(--muted)">→ Java EventListener (ActionListener)</li><li style="padding:3px 0;font-size:11px;color:var(--muted)">→ Spring ApplicationEvent</li><li style="padding:3px 0;font-size:11px;color:var(--muted)">→ Kafka (producer → consumers)</li><li style="padding:3px 0;font-size:11px;color:var(--muted)">→ RxJava reactive streams</li></ul></div>
    </div>
    <div class="m4-tip-box"><em>Interview:</em> "Kafka is Observer at scale — stock ticker is the producer, topic is the subject, consumer groups are observers. The pattern scales from in-process EventBus to distributed Kafka."</div>
  </div>

  <!-- 03 CoR -->
  <div class="m4-pat-panel" id="m4-pp2">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p3);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">03</div><div class="m4-p-name">Chain of Responsibility</div>
      <div class="m4-p-sys">REAL SYSTEM → ATM Cash Dispenser</div>
      <div class="m4-p-intent" style="border-left-color:var(--p3)">Give multiple handlers a chance to process a request. Chain them; pass the request along until handled. Decouples sender from receiver — sender doesn't know which handler will process it.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">ATMDispenser.java<span class="m4-clang" style="color:var(--p3)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">abstract class</span> <span class="m4-cls">CashHandler</span> {
    <span class="m4-kw">protected</span> <span class="m4-cls">CashHandler</span> next;

    <span class="m4-cm">// Fluent chaining: h1.setNext(h2).setNext(h3)</span>
    <span class="m4-kw">public</span> <span class="m4-cls">CashHandler</span> <span class="m4-fn">setNext</span>(<span class="m4-cls">CashHandler</span> n) { <span class="m4-kw">this</span>.next = n; <span class="m4-kw">return</span> n; }
    <span class="m4-kw">public abstract void</span> <span class="m4-fn">dispense</span>(<span class="m4-kw">int</span> amount);
}

<span class="m4-kw">class</span> <span class="m4-cls">TwoThousandHandler</span> <span class="m4-kw">extends</span> <span class="m4-cls">CashHandler</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">dispense</span>(<span class="m4-kw">int</span> amount) {
        <span class="m4-kw">int</span> notes = amount / <span class="m4-str">2000</span>, rem = amount % <span class="m4-str">2000</span>;
        <span class="m4-kw">if</span> (notes &gt; <span class="m4-str">0</span>) <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Dispensing "</span>+notes+<span class="m4-str">"×₹2000"</span>);
        <span class="m4-kw">if</span> (rem &gt; <span class="m4-str">0</span> &amp;&amp; next != <span class="m4-kw">null</span>) next.<span class="m4-fn">dispense</span>(rem); <span class="m4-cm">// Pass remainder</span>
    }
}
<span class="m4-kw">class</span> <span class="m4-cls">FiveHundredHandler</span> <span class="m4-kw">extends</span> <span class="m4-cls">CashHandler</span> { <span class="m4-cm">/* similar */</span> }
<span class="m4-kw">class</span> <span class="m4-cls">HundredHandler</span>     <span class="m4-kw">extends</span> <span class="m4-cls">CashHandler</span> { <span class="m4-cm">/* similar */</span> }

<span class="m4-cm">// Build the chain</span>
<span class="m4-cls">CashHandler</span> atm = <span class="m4-kw">new</span> <span class="m4-cls">TwoThousandHandler</span>();
atm.<span class="m4-fn">setNext</span>(<span class="m4-kw">new</span> <span class="m4-cls">FiveHundredHandler</span>())
   .<span class="m4-fn">setNext</span>(<span class="m4-kw">new</span> <span class="m4-cls">HundredHandler</span>());

atm.<span class="m4-fn">dispense</span>(<span class="m4-str">3700</span>);
<span class="m4-cm">// → Dispensing 1×₹2000 | 3×₹500 | 2×₹100</span></pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Servlet Filters and Spring Interceptors are CoR — auth filter → logging filter → compression filter. Each handles its concern and passes to next. Order matters and is explicit."</div>
  </div>

  <!-- 04 STATE -->
  <div class="m4-pat-panel" id="m4-pp3">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p4);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">04</div><div class="m4-p-name">State</div>
      <div class="m4-p-sys">REAL SYSTEM → Vending Machine</div>
      <div class="m4-p-intent" style="border-left-color:var(--p4)">Allow an object to alter its behaviour when internal state changes. Eliminates switch-on-state. Each State class encapsulates one state's behaviour + valid transitions.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">VendingMachineState.java<span class="m4-clang" style="color:var(--p4)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">VendingMachineState</span> {
    <span class="m4-kw">void</span> <span class="m4-fn">insertCoin</span>(<span class="m4-cls">VendingMachine</span> m, <span class="m4-kw">int</span> amount);
    <span class="m4-kw">void</span> <span class="m4-fn">selectProduct</span>(<span class="m4-cls">VendingMachine</span> m, <span class="m4-cls">String</span> m4-code);
    <span class="m4-kw">void</span> <span class="m4-fn">dispense</span>(<span class="m4-cls">VendingMachine</span> m);
    <span class="m4-kw">void</span> <span class="m4-fn">cancel</span>(<span class="m4-cls">VendingMachine</span> m);
}

<span class="m4-kw">class</span> <span class="m4-cls">IdleState</span> <span class="m4-kw">implements</span> <span class="m4-cls">VendingMachineState</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">insertCoin</span>(<span class="m4-cls">VendingMachine</span> m, <span class="m4-kw">int</span> amt) {
        m.<span class="m4-fn">setAmount</span>(amt);
        m.<span class="m4-fn">setState</span>(<span class="m4-kw">new</span> <span class="m4-cls">HasMoneyState</span>()); <span class="m4-cm">// TRANSITION</span>
    }
    <span class="m4-kw">public void</span> <span class="m4-fn">selectProduct</span>(<span class="m4-cls">VendingMachine</span> m, <span class="m4-cls">String</span> c) {
        <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Insert coin first"</span>);  <span class="m4-cm">// Invalid in this state</span>
    }
    <span class="m4-kw">public void</span> <span class="m4-fn">dispense</span>(<span class="m4-cls">VendingMachine</span> m)         { <span class="m4-cm">/* invalid */</span> }
    <span class="m4-kw">public void</span> <span class="m4-fn">cancel</span>(<span class="m4-cls">VendingMachine</span> m)           { <span class="m4-cm">/* nothing to cancel */</span> }
}

<span class="m4-kw">class</span> <span class="m4-cls">HasMoneyState</span> <span class="m4-kw">implements</span> <span class="m4-cls">VendingMachineState</span> { <span class="m4-cm">/* ... */</span> }
<span class="m4-kw">class</span> <span class="m4-cls">DispensingState</span> <span class="m4-kw">implements</span> <span class="m4-cls">VendingMachineState</span> { <span class="m4-cm">/* ... */</span> }

<span class="m4-cm">// Context — delegates everything to current state</span>
<span class="m4-kw">class</span> <span class="m4-cls">VendingMachine</span> {
    <span class="m4-kw">private</span> <span class="m4-cls">VendingMachineState</span> state = <span class="m4-kw">new</span> <span class="m4-cls">IdleState</span>();

    <span class="m4-kw">public void</span> <span class="m4-fn">insertCoin</span>(<span class="m4-kw">int</span> amt) { state.<span class="m4-fn">insertCoin</span>(<span class="m4-kw">this</span>, amt); }
    <span class="m4-kw">public void</span> <span class="m4-fn">setState</span>(<span class="m4-cls">VendingMachineState</span> s) { <span class="m4-kw">this</span>.state = s; }
}</pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "State vs Strategy: State changes automatically based on internal transitions. Strategy is changed externally by the client. Both use the same polymorphism trick — the difference is who controls the switch and why."</div>
  </div>

  <!-- 05 COMMAND -->
  <div class="m4-pat-panel" id="m4-pp4">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p5);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">05</div><div class="m4-p-name">Command</div>
      <div class="m4-p-sys">REAL SYSTEM → Smart Home + Undo Stack</div>
      <div class="m4-p-intent" style="border-left-color:var(--p5)">Encapsulate a request as an object. Enables: undo/redo (store history), queuing (batch execution), logging (serialize commands), and macro commands (compose many as one).</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">SmartHomeCommand.java<span class="m4-clang" style="color:var(--p5)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">Command</span> { <span class="m4-kw">void</span> <span class="m4-fn">execute</span>(); <span class="m4-kw">void</span> <span class="m4-fn">undo</span>(); }

<span class="m4-kw">class</span> <span class="m4-cls">LightOnCommand</span> <span class="m4-kw">implements</span> <span class="m4-cls">Command</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">Light</span> light;
    <span class="m4-kw">public void</span> <span class="m4-fn">execute</span>() { light.<span class="m4-fn">turnOn</span>(); }
    <span class="m4-kw">public void</span> <span class="m4-fn">undo</span>()    { light.<span class="m4-fn">turnOff</span>(); } <span class="m4-cm">// Inverse operation</span>
}

<span class="m4-kw">class</span> <span class="m4-cls">ACTempCommand</span> <span class="m4-kw">implements</span> <span class="m4-cls">Command</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">AC</span> ac; <span class="m4-kw">private final int</span> newTemp;
    <span class="m4-kw">private int</span> prevTemp; <span class="m4-cm">// Saved for undo</span>

    <span class="m4-kw">public void</span> <span class="m4-fn">execute</span>() { prevTemp = ac.<span class="m4-fn">getTemp</span>(); ac.<span class="m4-fn">setTemp</span>(newTemp); }
    <span class="m4-kw">public void</span> <span class="m4-fn">undo</span>()    { ac.<span class="m4-fn">setTemp</span>(prevTemp); }
}

<span class="m4-cm">// Invoker — the smart home controller</span>
<span class="m4-kw">class</span> <span class="m4-cls">SmartHomeHub</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">Deque</span>&lt;<span class="m4-cls">Command</span>&gt; history = <span class="m4-kw">new</span> <span class="m4-cls">ArrayDeque</span>&lt;&gt;();

    <span class="m4-kw">public void</span> <span class="m4-fn">execute</span>(<span class="m4-cls">Command</span> cmd) {
        cmd.<span class="m4-fn">execute</span>(); history.<span class="m4-fn">push</span>(cmd); <span class="m4-cm">// Push to undo stack</span>
    }

    <span class="m4-kw">public void</span> <span class="m4-fn">undo</span>() {
        <span class="m4-kw">if</span> (!history.isEmpty()) history.<span class="m4-fn">pop</span>().<span class="m4-fn">undo</span>();
    }
}

hub.<span class="m4-fn">execute</span>(<span class="m4-kw">new</span> <span class="m4-cls">LightOnCommand</span>(bedroom));
hub.<span class="m4-fn">execute</span>(<span class="m4-kw">new</span> <span class="m4-cls">ACTempCommand</span>(ac, <span class="m4-str">20</span>));
hub.<span class="m4-fn">undo</span>(); <span class="m4-cm">// AC reverts to previous temp</span>
hub.<span class="m4-fn">undo</span>(); <span class="m4-cm">// Light turns off</span></pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Command is the pattern behind every undo stack — Photoshop, Word, VS Code all use it. Each user action is a Command object. Ctrl+Z pops the stack and calls undo(). Ctrl+Y pushes back and calls execute()."</div>
  </div>

  <!-- 06 TEMPLATE -->
  <div class="m4-pat-panel" id="m4-pp5">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p6);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">06</div><div class="m4-p-name">Template Method</div>
      <div class="m4-p-sys">REAL SYSTEM → Data Migration Pipeline</div>
      <div class="m4-p-intent" style="border-left-color:var(--p6)">Define the skeleton of an algorithm in a base class; defer specific steps to subclasses. The template method is final — skeleton never changes. Individual steps can be overridden (Hollywood Principle: "Don't call us, we'll call you").</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">DataMigrationPipeline.java<span class="m4-clang" style="color:var(--p6)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">abstract class</span> <span class="m4-cls">DataMigrationPipeline</span> {
    <span class="m4-cm">// TEMPLATE METHOD — final: order never changes</span>
    <span class="m4-kw">public final void</span> <span class="m4-fn">migrate</span>() {
        <span class="m4-fn">extractData</span>();    <span class="m4-cm">// abstract — must override</span>
        <span class="m4-fn">validateData</span>();   <span class="m4-cm">// hook    — may override</span>
        <span class="m4-fn">transformData</span>(); <span class="m4-cm">// abstract — must override</span>
        <span class="m4-fn">loadData</span>();       <span class="m4-cm">// abstract — must override</span>
        <span class="m4-fn">notifyDone</span>();     <span class="m4-cm">// hook    — default OK</span>
    }
    <span class="m4-kw">protected abstract void</span> <span class="m4-fn">extractData</span>();
    <span class="m4-kw">protected abstract void</span> <span class="m4-fn">transformData</span>();
    <span class="m4-kw">protected abstract void</span> <span class="m4-fn">loadData</span>();
    <span class="m4-kw">protected void</span> <span class="m4-fn">validateData</span>() { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Schema validation"</span>); }
    <span class="m4-kw">protected void</span> <span class="m4-fn">notifyDone</span>()   { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Migration done"</span>); }
}

<span class="m4-kw">class</span> <span class="m4-cls">MySQLToPostgres</span> <span class="m4-kw">extends</span> <span class="m4-cls">DataMigrationPipeline</span> {
    <span class="m4-kw">protected void</span> <span class="m4-fn">extractData</span>()   { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"SELECT * FROM MySQL"</span>); }
    <span class="m4-kw">protected void</span> <span class="m4-fn">transformData</span>() { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"ENUM→text, TINYINT→bool"</span>); }
    <span class="m4-kw">protected void</span> <span class="m4-fn">loadData</span>()      { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"COPY INTO Postgres"</span>); }
    <span class="m4-kw">protected void</span> <span class="m4-fn">validateData</span>()  { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"Row count + FK check"</span>); }
}

<span class="m4-kw">new</span> <span class="m4-cls">MySQLToPostgres</span>().<span class="m4-fn">migrate</span>(); <span class="m4-cm">// Runs steps in correct order — always</span></pre></div>
    <div class="m4-tip-box"><em>Strategy vs Template Method:</em> Strategy swaps the WHOLE algorithm at runtime via composition. Template Method keeps the skeleton fixed in a base class; only specific steps vary via inheritance. Strategy = runtime; Template = compile-time.</div>
  </div>

  <!-- 07-12: compact panels -->
  <div class="m4-pat-panel" id="m4-pp6">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p7);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">07</div><div class="m4-p-name">Iterator</div>
      <div class="m4-p-sys">→ Custom Playlist / Collections</div>
      <div class="m4-p-intent" style="border-left-color:var(--p7)">Traverse a collection sequentially without exposing its internal structure. Client only uses hasNext() / next() — doesn't care if internals are List, Tree, Graph, or LinkedList.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">PlaylistIterator.java<span class="m4-clang" style="color:var(--p7)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">Iterator</span>&lt;T&gt; { <span class="m4-kw">boolean</span> <span class="m4-fn">hasNext</span>(); T <span class="m4-fn">next</span>(); }

<span class="m4-kw">class</span> <span class="m4-cls">Playlist</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">List</span>&lt;<span class="m4-cls">Song</span>&gt; songs = <span class="m4-kw">new</span> <span class="m4-cls">ArrayList</span>&lt;&gt;();

    <span class="m4-kw">public</span> <span class="m4-cls">Iterator</span>&lt;<span class="m4-cls">Song</span>&gt; <span class="m4-fn">createIterator</span>() {
        <span class="m4-kw">return new</span> <span class="m4-cls">Iterator</span>&lt;<span class="m4-cls">Song</span>&gt;() {
            <span class="m4-kw">int</span> i = <span class="m4-str">0</span>;
            <span class="m4-kw">public boolean</span> <span class="m4-fn">hasNext</span>() { <span class="m4-kw">return</span> i &lt; songs.size(); }
            <span class="m4-kw">public</span> <span class="m4-cls">Song</span> <span class="m4-fn">next</span>()      { <span class="m4-kw">return</span> songs.get(i++); }
        };
    }
}
<span class="m4-cm">// Client — doesn't know internals are a List</span>
<span class="m4-cls">Iterator</span>&lt;<span class="m4-cls">Song</span>&gt; it = playlist.<span class="m4-fn">createIterator</span>();
<span class="m4-kw">while</span> (it.<span class="m4-fn">hasNext</span>()) play(it.<span class="m4-fn">next</span>());</pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Java's for-each loop uses Iterator internally. Any class implementing java.lang.Iterable gets free for-each support. This is Iterator pattern baked into the language."</div>
  </div>

  <div class="m4-pat-panel" id="m4-pp7">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p8);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">08</div><div class="m4-p-name">Mediator</div>
      <div class="m4-p-sys">→ Air Traffic Control</div>
      <div class="m4-p-intent" style="border-left-color:var(--p8)">Encapsulate how a set of objects interact. Objects don't refer to each other — they all communicate through the mediator. Reduces N² direct connections to N connections via hub.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">ATCTower.java<span class="m4-clang" style="color:var(--p8)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">ATC</span> {
    <span class="m4-kw">void</span> <span class="m4-fn">requestLanding</span>(<span class="m4-cls">Aircraft</span> a);
    <span class="m4-kw">void</span> <span class="m4-fn">requestTakeoff</span>(<span class="m4-cls">Aircraft</span> a);
    <span class="m4-kw">void</span> <span class="m4-fn">broadcast</span>(<span class="m4-cls">String</span> msg, <span class="m4-cls">Aircraft</span> source);
}

<span class="m4-kw">abstract class</span> <span class="m4-cls">Aircraft</span> {
    <span class="m4-kw">protected final</span> <span class="m4-cls">ATC</span> atc; <span class="m4-cm">// Only knows ATC — not other aircraft</span>
    <span class="m4-kw">public void</span> <span class="m4-fn">land</span>()    { atc.<span class="m4-fn">requestLanding</span>(<span class="m4-kw">this</span>); }
    <span class="m4-kw">public void</span> <span class="m4-fn">takeoff</span>() { atc.<span class="m4-fn">requestTakeoff</span>(<span class="m4-kw">this</span>); }
    <span class="m4-kw">public abstract void</span> <span class="m4-fn">receive</span>(<span class="m4-cls">String</span> msg);
}

<span class="m4-cm">// Aircraft talk ONLY to ATC tower — never directly to each other</span>
<span class="m4-cm">// ATC routes communication, manages runway, notifies all parties</span></pre></div>
    <div class="m4-tip-box"><em>Mediator vs Observer:</em> Observer = one-to-many (subject notifies all). Mediator = many-to-many (all peers route through hub). Chat room is Mediator — messages go hub → recipients, not sender → every recipient directly.</div>
  </div>

  <div class="m4-pat-panel" id="m4-pp8">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p9);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">09</div><div class="m4-p-name">Memento</div>
      <div class="m4-p-sys">→ Text Editor Undo / Game Save</div>
      <div class="m4-p-intent" style="border-left-color:var(--p9)">Capture object state without exposing internals. Originator creates memento; Caretaker stores it; Originator restores from it. Three-role pattern preserving encapsulation.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">TextEditorUndo.java<span class="m4-clang" style="color:var(--p9)">JAVA</span></div>
<pre class="m4-code"><span class="m4-cm">// MEMENTO — opaque snapshot (Caretaker can't read it)</span>
<span class="m4-kw">class</span> <span class="m4-cls">EditorMemento</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">String</span> m4-content;  <span class="m4-cm">// package-private — only Originator reads</span>
    <span class="m4-kw">private final int</span>    cursor;
    <span class="m4-cls">EditorMemento</span>(<span class="m4-cls">String</span> c, <span class="m4-kw">int</span> pos) { m4-content=c; cursor=pos; }
    <span class="m4-cls">String</span> <span class="m4-fn">getContent</span>() { <span class="m4-kw">return</span> m4-content; }
    <span class="m4-kw">int</span>    <span class="m4-fn">getCursor</span>()  { <span class="m4-kw">return</span> cursor; }
}

<span class="m4-cm">// ORIGINATOR — creates and restores from memento</span>
<span class="m4-kw">class</span> <span class="m4-cls">TextEditor</span> {
    <span class="m4-kw">private</span> <span class="m4-cls">StringBuilder</span> m4-content = <span class="m4-kw">new</span> <span class="m4-cls">StringBuilder</span>();
    <span class="m4-kw">private int</span> cursor = <span class="m4-str">0</span>;

    <span class="m4-kw">public</span> <span class="m4-cls">EditorMemento</span> <span class="m4-fn">save</span>()          { <span class="m4-kw">return new</span> <span class="m4-cls">EditorMemento</span>(m4-content.toString(), cursor); }
    <span class="m4-kw">public void</span> <span class="m4-fn">restore</span>(<span class="m4-cls">EditorMemento</span> m) { m4-content = <span class="m4-kw">new</span> <span class="m4-cls">StringBuilder</span>(m.<span class="m4-fn">getContent</span>()); cursor=m.<span class="m4-fn">getCursor</span>(); }
}

<span class="m4-cm">// CARETAKER — stores mementos, never reads inside them</span>
<span class="m4-kw">class</span> <span class="m4-cls">UndoManager</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">Deque</span>&lt;<span class="m4-cls">EditorMemento</span>&gt; stack = <span class="m4-kw">new</span> <span class="m4-cls">ArrayDeque</span>&lt;&gt;();
    <span class="m4-kw">public void</span>           <span class="m4-fn">push</span>(<span class="m4-cls">EditorMemento</span> m) { stack.<span class="m4-fn">push</span>(m); }
    <span class="m4-kw">public</span> <span class="m4-cls">EditorMemento</span> <span class="m4-fn">pop</span>()                  { <span class="m4-kw">return</span> stack.<span class="m4-fn">pop</span>(); }
}</pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Three roles: Originator (knows its own state), Memento (opaque snapshot), Caretaker (stores mementos, never reads them). Encapsulation is preserved because only Originator can interpret the Memento's internals."</div>
  </div>

  <div class="m4-pat-panel" id="m4-pp9">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p10);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">10</div><div class="m4-p-name">Visitor</div>
      <div class="m4-p-sys">→ Tax Calculator (GST + Import Duty)</div>
      <div class="m4-p-intent" style="border-left-color:var(--p10)">Add new operations to elements without changing their classes. Double dispatch: element.accept(visitor) → visitor.visit(element). New operations = new Visitor; no changes to Book/Electronics/Food.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">TaxVisitor.java — Double Dispatch<span class="m4-clang" style="color:var(--p10)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">TaxVisitor</span> {
    <span class="m4-kw">double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Book</span> b);
    <span class="m4-kw">double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Electronics</span> e);
    <span class="m4-kw">double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Food</span> f);
}
<span class="m4-kw">interface</span> <span class="m4-cls">Product</span> { <span class="m4-kw">double</span> <span class="m4-fn">accept</span>(<span class="m4-cls">TaxVisitor</span> v); } <span class="m4-cm">// DOUBLE DISPATCH key</span>

<span class="m4-kw">class</span> <span class="m4-cls">Book</span> <span class="m4-kw">implements</span> <span class="m4-cls">Product</span> {
    <span class="m4-kw">boolean</span> educational;
    <span class="m4-kw">public double</span> <span class="m4-fn">accept</span>(<span class="m4-cls">TaxVisitor</span> v) { <span class="m4-kw">return</span> v.<span class="m4-fn">visit</span>(<span class="m4-kw">this</span>); } <span class="m4-cm">// Passes self</span>
}

<span class="m4-kw">class</span> <span class="m4-cls">GSTCalculator</span> <span class="m4-kw">implements</span> <span class="m4-cls">TaxVisitor</span> {
    <span class="m4-kw">public double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Book</span> b)        { <span class="m4-kw">return</span> b.educational ? <span class="m4-str">0</span> : b.price*<span class="m4-str">0.12</span>; }
    <span class="m4-kw">public double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Electronics</span> e) { <span class="m4-kw">return</span> e.price * <span class="m4-str">0.18</span>; }
    <span class="m4-kw">public double</span> <span class="m4-fn">visit</span>(<span class="m4-cls">Food</span> f)        { <span class="m4-kw">return</span> f.processed ? f.price*<span class="m4-str">0.12</span> : <span class="m4-str">0</span>; }
}
<span class="m4-cm">// Add ImportDutyCalculator = new class only — Book/Electronics/Food untouched (OCP)</span></pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Double dispatch is the key. In Java, method dispatch is on the runtime type of ONE argument. Visitor simulates two-argument dispatch: element type × visitor type. accept() provides the second dispatch."</div>
  </div>

  <div class="m4-pat-panel" id="m4-pp10">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p11);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">11</div><div class="m4-p-name">Null Object</div>
      <div class="m4-p-sys">→ Logger / Optional Dependencies</div>
      <div class="m4-p-intent" style="border-left-color:var(--p11)">Provide a default do-nothing implementation to avoid null checks. Client m4-code never checks for null — calls methods on whatever was injected, safely.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">NullLogger.java<span class="m4-clang" style="color:var(--p11)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">Logger</span> { <span class="m4-kw">void</span> <span class="m4-fn">log</span>(<span class="m4-cls">String</span> msg); <span class="m4-kw">void</span> <span class="m4-fn">error</span>(<span class="m4-cls">String</span> msg); }

<span class="m4-kw">class</span> <span class="m4-cls">ConsoleLogger</span> <span class="m4-kw">implements</span> <span class="m4-cls">Logger</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">log</span>(<span class="m4-cls">String</span> msg)   { <span class="m4-cls">System</span>.out.println(<span class="m4-str">"[LOG] "</span>+msg); }
    <span class="m4-kw">public void</span> <span class="m4-fn">error</span>(<span class="m4-cls">String</span> msg) { <span class="m4-cls">System</span>.err.println(<span class="m4-str">"[ERR] "</span>+msg); }
}

<span class="m4-cm">// NULL OBJECT — same interface, does nothing</span>
<span class="m4-kw">class</span> <span class="m4-cls">NullLogger</span> <span class="m4-kw">implements</span> <span class="m4-cls">Logger</span> {
    <span class="m4-kw">public void</span> <span class="m4-fn">log</span>(<span class="m4-cls">String</span> msg)   { <span class="m4-cm">/* no-op */</span> }
    <span class="m4-kw">public void</span> <span class="m4-fn">error</span>(<span class="m4-cls">String</span> msg) { <span class="m4-cm">/* no-op */</span> }
}

<span class="m4-kw">class</span> <span class="m4-cls">PaymentService</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">Logger</span> log;
    <span class="m4-kw">public</span> <span class="m4-cls">PaymentService</span>(<span class="m4-cls">Logger</span> log) {
        <span class="m4-kw">this</span>.log = log != <span class="m4-kw">null</span> ? log : <span class="m4-kw">new</span> <span class="m4-cls">NullLogger</span>(); <span class="m4-cm">// Never null after this</span>
    }
    <span class="m4-kw">public void</span> <span class="m4-fn">process</span>(<span class="m4-kw">double</span> amt) {
        log.<span class="m4-fn">log</span>(<span class="m4-str">"Processing ₹"</span>+amt); <span class="m4-cm">// Safe — always. No null check.</span>
    }
}</pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Null Object is the pattern behind Optional in Java 8+ — instead of checking isPresent(), you call ifPresent() which is a no-op when empty. Eliminates NullPointerException from forgotten null checks."</div>
  </div>

  <div class="m4-pat-panel" id="m4-pp11">
    <div class="m4-p-mast"><div style="position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--p12);border-radius:10px 0 0 10px"></div>
      <div class="m4-p-num-bg">12</div><div class="m4-p-name">Interpreter</div>
      <div class="m4-p-sys">→ Math Expression Parser / Rules Engine</div>
      <div class="m4-p-intent" style="border-left-color:var(--p12)">Represent a grammar as a class hierarchy. Each grammar rule is a class. Compose terminal and non-terminal expressions into an AST. Call interpret(context) to evaluate.</div>
    </div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">ExpressionParser.java<span class="m4-clang" style="color:var(--p12)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">interface</span> <span class="m4-cls">Expression</span> { <span class="m4-kw">int</span> <span class="m4-fn">interpret</span>(<span class="m4-cls">Map</span>&lt;<span class="m4-cls">String</span>,<span class="m4-cls">Integer</span>&gt; ctx); }

<span class="m4-cm">// TERMINAL — leaves of the AST</span>
<span class="m4-kw">class</span> <span class="m4-cls">NumberExpr</span>   <span class="m4-kw">implements</span> <span class="m4-cls">Expression</span> {
    <span class="m4-kw">private final int</span> n;
    <span class="m4-kw">public int</span> <span class="m4-fn">interpret</span>(<span class="m4-cls">Map</span> ctx) { <span class="m4-kw">return</span> n; }
}
<span class="m4-kw">class</span> <span class="m4-cls">VariableExpr</span> <span class="m4-kw">implements</span> <span class="m4-cls">Expression</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">String</span> name;
    <span class="m4-kw">public int</span> <span class="m4-fn">interpret</span>(<span class="m4-cls">Map</span> ctx) { <span class="m4-kw">return</span> (<span class="m4-kw">int</span>) ctx.<span class="m4-fn">getOrDefault</span>(name, <span class="m4-str">0</span>); }
}

<span class="m4-cm">// NON-TERMINAL — composite nodes</span>
<span class="m4-kw">class</span> <span class="m4-cls">AddExpr</span> <span class="m4-kw">implements</span> <span class="m4-cls">Expression</span> {
    <span class="m4-kw">private final</span> <span class="m4-cls">Expression</span> l, r;
    <span class="m4-kw">public int</span> <span class="m4-fn">interpret</span>(<span class="m4-cls">Map</span> ctx) { <span class="m4-kw">return</span> l.<span class="m4-fn">interpret</span>(ctx) + r.<span class="m4-fn">interpret</span>(ctx); }
}

<span class="m4-cm">// Parse "a + b * 3" → a + (b * 3)</span>
<span class="m4-cls">Expression</span> expr = <span class="m4-kw">new</span> <span class="m4-cls">AddExpr</span>(
    <span class="m4-kw">new</span> <span class="m4-cls">VariableExpr</span>(<span class="m4-str">"a"</span>),
    <span class="m4-kw">new</span> <span class="m4-cls">MultiplyExpr</span>(<span class="m4-kw">new</span> <span class="m4-cls">VariableExpr</span>(<span class="m4-str">"b"</span>), <span class="m4-kw">new</span> <span class="m4-cls">NumberExpr</span>(<span class="m4-str">3</span>)));
expr.<span class="m4-fn">interpret</span>(<span class="m4-cls">Map</span>.of(<span class="m4-str">"a"</span>, <span class="m4-str">5</span>, <span class="m4-str">"b"</span>, <span class="m4-str">4</span>)); <span class="m4-cm">// → 17</span></pre></div>
    <div class="m4-tip-box"><em>Interview:</em> "Interpreter works well for simple grammars — math expressions, SQL WHERE parsers, firewall rules engines. For complex grammars, use a parser generator (ANTLR) instead. Composite pattern is Interpreter's structural cousin."</div>
  </div>
</div>

<!-- ===== DISTINCTIONS ===== -->
<div class="m4-view" id="m4-view-compare">
  <div class="m4-conf-grid">
    <div class="m4-conf-card">
      <div class="m4-conf-hd" style="border-top:2px solid var(--p1)">Strategy vs State vs Template Method</div>
      <div class="m4-conf-body">
        <strong>Strategy</strong> — Swap the whole algorithm at runtime. Changed externally by client. Uses composition.<br><br>
        <strong>State</strong> — Algorithm changes automatically as internal state transitions. States know about each other. Self-transitions.<br><br>
        <strong>Template Method</strong> — Algorithm skeleton fixed in base class. Only specific steps vary via inheritance. Compile-time decision.<br><br>
        <em style="color:var(--p1)">Rule:</em> Who controls the switch? Client→Strategy. Object→State. Compiler→Template.
      </div>
    </div>
    <div class="m4-conf-card">
      <div class="m4-conf-hd" style="border-top:2px solid var(--p2)">Observer vs Mediator vs CoR</div>
      <div class="m4-conf-body">
        <strong>Observer</strong> — 1-to-many: subject broadcasts to all registered observers. Observers don't know each other.<br><br>
        <strong>Mediator</strong> — Many-to-many: all peers talk through central hub. Hub coordinates responses. Peers know Mediator, not each other.<br><br>
        <strong>Chain of Responsibility</strong> — Request travels down a chain. Each handler decides to handle or pass. No hub — linear.<br><br>
        <em style="color:var(--p2)">Rule:</em> All notified? Observer. Hub decides routing? Mediator. Linear pass-through? CoR.
      </div>
    </div>
    <div class="m4-conf-card">
      <div class="m4-conf-hd" style="border-top:2px solid var(--p5)">Command vs Strategy vs Template</div>
      <div class="m4-conf-body">
        <strong>Command</strong> — Encapsulates a REQUEST (with undo, queue, log). About WHO initiated the action and when.<br><br>
        <strong>Strategy</strong> — Encapsulates an ALGORITHM (interchangeable). About HOW the action is performed.<br><br>
        <em style="color:var(--p5)">Rule:</em> Need undo/queue/log → Command. Need interchangeable algorithm → Strategy. Both look similar — the intent distinguishes them.
      </div>
    </div>
    <div class="m4-conf-card">
      <div class="m4-conf-hd" style="border-top:2px solid var(--p9)">Memento vs Command (for undo)</div>
      <div class="m4-conf-body">
        <strong>Memento undo</strong> — Saves entire state snapshot. Easy to implement. Heavy (stores full state).<br><br>
        <strong>Command undo</strong> — Stores inverse operations. Lightweight (stores only what changed). More complex.<br><br>
        <em style="color:var(--p9)">When to choose:</em> State changes are small and known → Command undo. State is complex or external → Memento snapshot.<br><br>
        Most real editors use Command undo for efficiency.
      </div>
    </div>
  </div>

  <div style="margin-top:20px;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:20px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:14px;">// QUICK ONE-LINE TEST FOR EACH PATTERN</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-family:'JetBrains Mono',monospace;font-size:11px;line-height:1.8;">
      <div><span style="color:var(--p1)">Strategy: </span><span style="color:var(--muted)">"Which algorithm should I use right now?"</span></div>
      <div><span style="color:var(--p2)">Observer: </span><span style="color:var(--muted)">"Notify everyone when this changes"</span></div>
      <div><span style="color:var(--p3)">CoR:      </span><span style="color:var(--muted)">"Try each handler until one succeeds"</span></div>
      <div><span style="color:var(--p4)">State:    </span><span style="color:var(--muted)">"I behave differently depending on mode"</span></div>
      <div><span style="color:var(--p5)">Command:  </span><span style="color:var(--muted)">"Record this action so I can undo it"</span></div>
      <div><span style="color:var(--p6)">Template: </span><span style="color:var(--muted)">"Same steps, different implementations"</span></div>
      <div><span style="color:var(--p7)">Iterator: </span><span style="color:var(--muted)">"Walk through this without knowing how it's stored"</span></div>
      <div><span style="color:var(--p8)">Mediator: </span><span style="color:var(--muted)">"Route all messages through a hub"</span></div>
      <div><span style="color:var(--p9)">Memento:  </span><span style="color:var(--muted)">"Take a snapshot I can restore later"</span></div>
      <div><span style="color:var(--p10)">Visitor:  </span><span style="color:var(--muted)">"Add operations without touching element classes"</span></div>
      <div><span style="color:var(--p11)">Null Obj: </span><span style="color:var(--muted)">"Do nothing instead of crashing on null"</span></div>
      <div><span style="color:var(--p12)">Interpret:</span><span style="color:var(--muted)">"Evaluate this expression in my mini-language"</span></div>
    </div>
  </div>
</div>

<!-- ===== STATE MACHINE ===== -->
<div class="m4-view" id="m4-view-state">
  <div style="margin-bottom:24px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:10px;">// STATE PATTERN IN ACTION</div>
    <div style="font-family:'DM Serif Display',serif;font-size:24px;color:var(--bright);margin-bottom:6px;">Seat State Machine — BookMyShow</div>
    <p style="font-size:13px;color:var(--muted);line-height:1.7;max-width:600px;">The seat lifecycle in BookMyShow is a perfect State pattern example. Each state defines which transitions are valid and which are illegal.</p>
  </div>

  <div class="m4-state-machine">
    <div class="m4-state-node" style="border-color:var(--p1);color:var(--p1)">AVAILABLE</div>
    <div class="m4-state-arrow"><div class="m4-arrow-line">→</div><div>tryLock(userId)</div><div>5s timeout</div></div>
    <div class="m4-state-node" style="border-color:var(--p9);color:var(--p9)">LOCKED</div>
    <div class="m4-state-arrow"><div class="m4-arrow-line">→</div><div>confirmPayment()</div></div>
    <div class="m4-state-node" style="border-color:var(--p5);color:var(--p5)">BOOKED</div>
    <div class="m4-state-arrow"><div class="m4-arrow-line">→</div><div>cancel()</div></div>
    <div class="m4-state-node" style="border-color:var(--p8);color:var(--p8)">CANCELLED</div>
  </div>

  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:16px;">
    <div style="background:var(--surface);border:1px solid var(--border);border-top:2px solid var(--p1);border-radius:6px;padding:14px;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--p1);margin-bottom:8px;">AVAILABLE</div>
      <div style="font-size:11px;color:var(--muted);line-height:1.6;">✓ tryLock(userId) → LOCKED<br>✗ confirmPayment() → error<br>✗ cancel() → error</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-top:2px solid var(--p9);border-radius:6px;padding:14px;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--p9);margin-bottom:8px;">LOCKED</div>
      <div style="font-size:11px;color:var(--muted);line-height:1.6;">✓ confirmPayment() → BOOKED<br>✓ timeout() → AVAILABLE<br>✓ cancel() → AVAILABLE<br>✗ tryLock() by others → error</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-top:2px solid var(--p5);border-radius:6px;padding:14px;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--p5);margin-bottom:8px;">BOOKED</div>
      <div style="font-size:11px;color:var(--muted);line-height:1.6;">✓ cancel() → CANCELLED<br>✗ tryLock() → error<br>✗ confirmPayment() → error</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-top:2px solid var(--p8);border-radius:6px;padding:14px;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--p8);margin-bottom:8px;">CANCELLED</div>
      <div style="font-size:11px;color:var(--muted);line-height:1.6;">✓ relist() → AVAILABLE<br>✗ all others → error<br>(terminal state)</div>
    </div>
  </div>

  <div style="margin-top:20px;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:20px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:12px;">// CONCURRENCY-SAFE SEAT LOCKING</div>
    <div class="m4-m4-code-wrap"><div class="m4-m4-code-hdr">Seat.java — Thread-safe State + Lock<span class="m4-clang" style="color:var(--p5)">JAVA</span></div>
<pre class="m4-code"><span class="m4-kw">class</span> <span class="m4-cls">Seat</span> {
    <span class="m4-kw">private volatile</span> <span class="m4-cls">SeatState</span> state = <span class="m4-cls">SeatState</span>.AVAILABLE;
    <span class="m4-kw">private final</span> <span class="m4-cls">ReentrantLock</span> lock = <span class="m4-kw">new</span> <span class="m4-cls">ReentrantLock</span>();
    <span class="m4-kw">private</span> <span class="m4-cls">String</span> lockedBy;

    <span class="m4-kw">public boolean</span> <span class="m4-fn">tryLock</span>(<span class="m4-cls">String</span> userId, <span class="m4-kw">long</span> timeoutMs) {
        <span class="m4-kw">try</span> {
            <span class="m4-kw">if</span> (lock.<span class="m4-fn">tryLock</span>(timeoutMs, <span class="m4-cls">TimeUnit</span>.MILLISECONDS)) {
                <span class="m4-kw">if</span> (state == <span class="m4-cls">SeatState</span>.AVAILABLE) {
                    state    = <span class="m4-cls">SeatState</span>.LOCKED;
                    lockedBy = userId;
                    <span class="m4-fn">scheduleLockExpiry</span>(<span class="m4-str">5_000</span>); <span class="m4-cm">// Auto-release after 5s</span>
                    <span class="m4-kw">return true</span>;
                }
                lock.<span class="m4-fn">unlock</span>(); <span class="m4-cm">// Not available — release lock</span>
            }
        } <span class="m4-kw">catch</span> (<span class="m4-cls">InterruptedException</span> e) { <span class="m4-cls">Thread</span>.currentThread().<span class="m4-fn">interrupt</span>(); }
        <span class="m4-kw">return false</span>; <span class="m4-cm">// Seat taken or timeout</span>
    }
}</pre></div>
  </div>
</div>

<!-- ===== BOOKMYSHOW ===== -->
<div class="m4-view" id="m4-view-bms">
  <div style="margin-bottom:24px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:10px;">MINI PROJECT</div>
    <div style="font-family:'DM Serif Display',serif;font-size:32px;color:var(--bright);margin-bottom:8px;">BookMyShow — LLD + Concurrency</div>
    <p style="font-size:13px;color:var(--muted);line-height:1.7;max-width:680px;">The capstone project for Module A4. Uses 6 behavioral patterns woven together with real concurrency handling. This is the most complex LLD problem so far.</p>
  </div>

  <div class="m4-bms-grid">
    <div class="m4-bms-card">
      <div class="m4-bms-icon">🎭</div>
      <div class="m4-bms-name">Seat State Machine</div>
      <div class="m4-bms-pattern" style="background:rgba(74,184,200,0.1);color:var(--p4)">State Pattern</div>
      <div class="m4-bms-desc">AVAILABLE → LOCKED → BOOKED → CANCELLED. Each state defines valid transitions. ReentrantLock ensures thread-safe transitions.</div>
    </div>
    <div class="m4-bms-card">
      <div class="m4-bms-icon">🔔</div>
      <div class="m4-bms-name">Booking Notifications</div>
      <div class="m4-bms-pattern" style="background:rgba(80,200,120,0.1);color:var(--p2)">Observer Pattern</div>
      <div class="m4-bms-desc">BookingService is Subject. User's email, SMS, push are observers. Notified on confirmation, cancellation, reminders.</div>
    </div>
    <div class="m4-bms-card">
      <div class="m4-bms-icon">↩️</div>
      <div class="m4-bms-name">Book / Cancel Actions</div>
      <div class="m4-bms-pattern" style="background:rgba(96,143,223,0.1);color:var(--p5)">Command Pattern</div>
      <div class="m4-bms-desc">BookSeatCommand + CancelBookingCommand with undo(). Stack enables cancellation with refund in reverse order of seats booked.</div>
    </div>
    <div class="m4-bms-card">
      <div class="m4-bms-icon">💰</div>
      <div class="m4-bms-name">Ticket Pricing</div>
      <div class="m4-bms-pattern" style="background:rgba(126,200,80,0.1);color:var(--p1)">Strategy Pattern</div>
      <div class="m4-bms-desc">WeekendPricingStrategy, WeekdayPricingStrategy, HolidayPricingStrategy — injected at show creation. Swap without touching BookingService.</div>
    </div>
    <div class="m4-bms-card">
      <div class="m4-bms-icon">🔗</div>
      <div class="m4-bms-name">Booking Pipeline</div>
      <div class="m4-bms-pattern" style="background:rgba(80,200,160,0.1);color:var(--p3)">Chain of Responsibility</div>
      <div class="m4-bms-desc">SeatAvailabilityHandler → PaymentHandler → BookingConfirmationHandler → NotificationHandler. Each step passes to next or aborts.</div>
    </div>
    <div class="m4-bms-card">
      <div class="m4-bms-icon">🏛️</div>
      <div class="m4-bms-name">BookingFacade</div>
      <div class="m4-bms-pattern" style="background:rgba(144,112,208,0.1);color:var(--p6)">Facade (from A3)</div>
      <div class="m4-bms-desc">bookSeats(userId, showId, seatIds) hides: seat locking, payment, ticket generation, observer notification, audit logging.</div>
    </div>
  </div>

  <div style="margin-top:20px;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:20px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:12px;">// PROJECT STRUCTURE</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#7a9870;line-height:1.9;">
      bookmyshow/<br>
      ├── model/          <span style="color:var(--muted)">Movie, Show, Screen, Seat, User, Booking, Ticket</span><br>
      ├── state/          <span style="color:var(--muted)">SeatState enum + state transition logic</span><br>
      ├── command/        <span style="color:var(--muted)">BookSeatCommand, CancelBookingCommand</span><br>
      ├── observer/       <span style="color:var(--muted)">BookingObserver, EmailNotifier, SMSNotifier, PushNotifier</span><br>
      ├── strategy/       <span style="color:var(--muted)">PricingStrategy, WeekendPricing, WeekdayPricing</span><br>
      ├── chain/          <span style="color:var(--muted)">BookingHandler chain: Availability → Payment → Confirm → Notify</span><br>
      ├── service/        <span style="color:var(--muted)">BookingService, PaymentService, NotificationService</span><br>
      ├── facade/         <span style="color:var(--muted)">BookingFacade — single public entry point</span><br>
      └── BookMyShowDemo.java <span style="color:var(--muted)">5 concurrent users, 1 show, race condition demo</span>
    </div>
  </div>
</div>

<!-- ===== TASKS ===== -->
<div class="m4-view" id="m4-view-tasks">
  <div class="m4-task-list">
    <div class="m4-task-card">
      <div class="m4-task-hd" onclick="m4ToggleTask(this)"><div class="m4-t-num">01</div><div class="m4-t-label">Pattern Recognition — 6 Scenarios</div><div class="m4-t-meta">~1.5 hrs</div><div class="m4-t-arr">›</div></div>
      <div class="m4-task-bd">
        <p>Identify the correct Behavioral pattern. 2-sentence justification each.</p>
        <pre>1. Text editor needs Ctrl+Z undo for bold, italic, insert, delete.
2. Social media notifies followers when user posts. Follower list changes dynamically.
3. Loan application: Credit Check → Income Verify → Background → Approval.
4. Traffic light cycles RED → GREEN → YELLOW. Valid actions differ per phase.
5. Zip utility supports DEFLATE/BZIP2/LZMA, switchable per file type at runtime.
6. Shopping cart: calculate total price, weight, customs duty as separate passes
   without adding methods to Product classes.</pre>
      </div>
    </div>
    <div class="m4-task-card">
      <div class="m4-task-hd" onclick="m4ToggleTask(this)"><div class="m4-t-num">02</div><div class="m4-t-label">Thread-safe EventBus (Observer)</div><div class="m4-t-meta">~2.5 hrs · m4-code</div><div class="m4-t-arr">›</div></div>
      <div class="m4-task-bd">
        <p>Build a generic publish/subscribe EventBus with thread safety.</p>
        <pre>API:
  subscribe(Class&lt;T&gt; eventType, Consumer&lt;T&gt; handler)
  unsubscribe(Class&lt;T&gt; eventType, Consumer&lt;T&gt; handler)
  publish(T event)

Events: OrderPlaced, PaymentFailed, ItemShipped

Requirements:
- Multiple handlers per event type
- Thread-safe: concurrent publish() + subscribe() calls
- Handlers run asynchronously (use ExecutorService)
- Failed handler must not block other handlers
- Unsubscribe mid-flight must not cause ConcurrentModificationException</pre>
      </div>
    </div>
    <div class="m4-task-card">
      <div class="m4-task-hd" onclick="m4ToggleTask(this)"><div class="m4-t-num">03</div><div class="m4-t-label">ReportGenerator — Template Method + Strategy</div><div class="m4-t-meta">~2 hrs · m4-code</div><div class="m4-t-arr">›</div></div>
      <div class="m4-task-bd">
        <p>Combine Template Method for pipeline structure with Strategy for delivery.</p>
        <pre>Template Method skeleton (in abstract base):
  gatherData() → processData() → formatOutput() → deliver()

Subclasses override formatOutput():
  HTMLReportGenerator → formatOutput() returns HTML string
  PDFReportGenerator  → formatOutput() returns byte[]

Strategy for deliver() (injected, runtime-swappable):
  EmailDelivery   — sends via SMTP
  SlackDelivery   — sends via Slack webhook

Show all 4 combinations work:
  new HTMLReportGenerator(new EmailDelivery()).generate()
  new HTMLReportGenerator(new SlackDelivery()).generate()
  new PDFReportGenerator(new EmailDelivery()).generate()
  new PDFReportGenerator(new SlackDelivery()).generate()</pre>
      </div>
    </div>
    <div class="m4-task-card" style="border-left:3px solid var(--p2)">
      <div class="m4-task-hd" onclick="m4ToggleTask(this)"><div class="m4-t-num" style="color:var(--p2)">★</div><div class="m4-t-label">BookMyShow — Full LLD + Concurrency</div><div class="m4-t-meta">~6 hrs · full project</div><div class="m4-t-arr">›</div></div>
      <div class="m4-task-bd">
        <p>Complete LLD implementation. The concurrency handling is the critical differentiator.</p>
        <pre>Implement all 6 pattern usages:
  State:   Seat state machine (AVAILABLE→LOCKED→BOOKED→CANCELLED)
  Observer: Booking confirmation/cancellation notifications
  Command: BookSeatCommand + CancelBookingCommand with undo()
  Strategy: Pricing (Weekend 1.5x, Holiday 2x, Weekday 1.0x)
  CoR:     Availability→Payment→Confirm→Notify handler chain
  Facade:  BookingFacade.bookSeats(userId, showId, seatIds)

Demo: 5 threads simultaneously try to book the last 2 seats
  → Only 2 succeed, 3 get "seat unavailable"
  → No double booking under any timing

Deliverable:
  1. Full Java implementation (all classes)
  2. Concurrency test showing thread-safe behaviour
  3. UML class diagram with all 6 patterns annotated</pre>
      </div>
    </div>
  </div>
</div>

<!-- ===== CHECKLIST ===== -->
<div class="m4-view" id="m4-view-checklist">
  <div class="m4-prog-row"><span id="m4-prog-lbl">0 / 12 completed</span><span style="color:var(--p1)">A4 → Behavioral Patterns</span></div>
  <div class="m4-prog-track"><div class="m4-prog-fill" id="m4-prog-fill"></div></div>
  <div class="m4-m4-chk-grid">
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Can implement Strategy, Observer, CoR, State, Command from memory</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Can implement Template Method, Iterator, Mediator, Memento, Visitor from memory</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Know Null Object and Interpreter well enough to apply and explain</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Can distinguish Strategy vs State vs Template Method with the one-line test</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Know Observer push vs pull model trade-offs</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Understand Command's role in undo/redo, queue, and macro commands</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Understand Visitor's double dispatch mechanism</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">Know Memento's 3-role structure (Originator, Memento, Caretaker)</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">✏️ Task 1: 6 pattern recognition scenarios answered correctly</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">✏️ Task 2: Thread-safe EventBus with async handlers implemented</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">✏️ Task 3: ReportGenerator combining Template Method + Strategy (4 combos)</div></div>
    <div class="m4-chk" onclick="m4Tick(this)"><div class="m4-m4-chk-box"></div><div class="m4-m4-chk-lbl">✏️ Mini Project: BookMyShow with concurrency proof + all 6 patterns + UML</div></div>
  </div>

  <div style="margin-top:28px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;padding:24px;border-top:2px solid var(--p2);">
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:10px;">NEXT MODULE</div>
    <div style="font-family:'DM Serif Display',serif;font-size:24px;color:var(--bright);margin-bottom:6px;">A5 — Concurrency in LLD</div>
    <div style="font-size:13px;color:var(--muted);line-height:1.7;">Thread safety, locks, semaphores, producer-consumer, thread pools, deadlock avoidance. Projects: Thread-safe Parking Lot, Rate Limiter, Pub/Sub Message Queue.</div>
  </div>
</div>

</div>
</div><!-- end m4-content -->

<!-- ── BOTTOM NAV ─────────────────────────────────────────────── -->
<div class="m4-bottom-nav" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--border2);padding-top:20px;">
  <a href="/learning/system-design/lld/module-a3-structural/" class="m4-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">← PREVIOUS: LLD A3</a>
  <a href="/learning/system-design/lld/module-a4-notes/" class="m4-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--p1);color:var(--p1);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" class="m4-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a5-concurrency/" class="m4-nav-footer-btn" style="padding:12px 24px;background:var(--p1);color:var(--paper);border-radius:4px;text-decoration:none;font-weight:600;">NEXT: LLD A5 →</a>
</div>
