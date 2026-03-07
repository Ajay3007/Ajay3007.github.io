---
layout: default
title: "Module A3 — Structural Patterns"
custom_css: sd-module-a3
custom_js: sd-module-a3
permalink: /learning/system-design/lld/module-a3-structural/
---

<div class="m3-page m3-bg">
<header class="m3-header">
  <div class="m3-colour-bar">
    <div class="m3-colour-seg" style="background:var(--c1)"></div>
    <div class="m3-colour-seg" style="background:var(--c2)"></div>
    <div class="m3-colour-seg" style="background:var(--c3)"></div>
    <div class="m3-colour-seg" style="background:var(--c4)"></div>
    <div class="m3-colour-seg" style="background:var(--c5)"></div>
    <div class="m3-colour-seg" style="background:var(--c6)"></div>
    <div class="m3-colour-seg" style="background:var(--c7)"></div>
  </div>
  <div class="m3-header-top">
    <div class="m3-header-left">
      <div class="m3-kicker">Track A · LLD · Module A3 · Week 5</div>
      <h1>Structural<br>Patterns</h1>
      <div class="m3-header-sub">
        Adapter · Decorator · Proxy · Composite<br>
        Facade · Bridge · Flyweight
      </div>
    </div>
    <div class="m3-header-right">
      <div class="m3-meta-stack">
        <div class="m3-meta-item"><span>Week</span><strong>5 of 24</strong></div>
        <div class="m3-meta-item"><span>Patterns</span><strong>7</strong></div>
        <div class="m3-meta-item"><span>Systems</span><strong>7 real</strong></div>
        <div class="m3-meta-item"><span>Project</span><strong>Splitwise</strong></div>
        <div class="m3-meta-item"><span>Prereq</span><strong>A1 + A2</strong></div>
      </div>
    </div>
  </div>
</header>

<m3-nav class="m3-nav">
  <div class="m3-nav-tab active" onclick="m3Show('overview',this)">Overview</div>
  <div class="m3-nav-tab" onclick="m3Show('patterns',this)">Pattern Deep Dives</div>
  <div class="m3-nav-tab" onclick="m3Show('distinctions',this)">Key Distinctions</div>
  <div class="m3-nav-tab" onclick="m3Show('splitwise',this)">Splitwise Project</div>
  <div class="m3-nav-tab" onclick="m3Show('tasks',this)">Tasks</div>
  <div class="m3-nav-tab" onclick="m3Show('checklist',this)">Checklist</div>
</m3-nav>

<div class="m3-content">

<!-- ===== OVERVIEW ===== -->
<div class="m3-view active" id="m3-view-overview">
  <p style="font-size:14px;color:var(--muted);line-height:1.8;max-width:700px;margin-bottom:32px;font-style:italic;">
    Structural patterns deal with <strong style="color:var(--ink)">object composition</strong> — how classes and objects are assembled into larger structures. They ensure that when one part changes, the entire structure doesn't need to be redesigned.
  </p>

  <div class="m3-overview-grid">
    <div class="m3-ov-card" onclick="m3GoToPattern(0)">
      <div class="m3-ov-top" style="background:var(--c1)"></div>
      <div class="m3-ov-num">01</div>
      <div class="m3-ov-name">Adapter</div>
      <div class="m3-ov-sys">→ Vending Machine</div>
      <div class="m3-ov-problem">Make incompatible interfaces work together.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(1)">
      <div class="m3-ov-top" style="background:var(--c2)"></div>
      <div class="m3-ov-num">02</div>
      <div class="m3-ov-name">Decorator</div>
      <div class="m3-ov-sys">→ Pizza Billing</div>
      <div class="m3-ov-problem">Add responsibilities dynamically. Avoids subclass explosion.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(2)">
      <div class="m3-ov-top" style="background:var(--c3)"></div>
      <div class="m3-ov-num">03</div>
      <div class="m3-ov-name">Proxy</div>
      <div class="m3-ov-sys">→ Car Rental</div>
      <div class="m3-ov-problem">Control access to an object. Same interface, intercepted calls.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(3)">
      <div class="m3-ov-top" style="background:var(--c4)"></div>
      <div class="m3-ov-num">04</div>
      <div class="m3-ov-name">Composite</div>
      <div class="m3-ov-sys">→ File System</div>
      <div class="m3-ov-problem">Treat leaf and branch uniformly through one interface.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(4)">
      <div class="m3-ov-top" style="background:var(--c5)"></div>
      <div class="m3-ov-num">05</div>
      <div class="m3-ov-name">Facade</div>
      <div class="m3-ov-sys">→ Splitwise</div>
      <div class="m3-ov-problem">Simplified interface hiding a complex subsystem.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(5)">
      <div class="m3-ov-top" style="background:var(--c6)"></div>
      <div class="m3-ov-num">06</div>
      <div class="m3-ov-name">Bridge</div>
      <div class="m3-ov-sys">→ CricBuzz</div>
      <div class="m3-ov-problem">Decouple two dimensions of variation. Replaces subclass explosion.</div>
    </div>
    <div class="m3-ov-card" onclick="m3GoToPattern(6)">
      <div class="m3-ov-top" style="background:var(--c7)"></div>
      <div class="m3-ov-num">07</div>
      <div class="m3-ov-name">Flyweight</div>
      <div class="m3-ov-sys">→ TrueCaller</div>
      <div class="m3-ov-problem">Share intrinsic state across millions of objects. Memory efficiency.</div>
    </div>
  </div>

  <div style="margin-top:8px;">
    <table class="m3-sd-table">
      <thead><tr><th>PATTERN</th><th>TRIGGER / SMELL</th><th>KEY MECHANISM</th><th>REAL WORLD</th></tr></thead>
      <tbody>
        <tr><td style="color:var(--c1)">Adapter</td><td>Incompatible interface from third-party/legacy</td><td>Wrapper translates interface A → interface B</td><td>Payment gateways, legacy DB drivers</td></tr>
        <tr><td style="color:var(--c2)">Decorator</td><td>N features × M objects = too many subclasses</td><td>IS-A + HAS-A same type; wraps and delegates</td><td>Java I/O streams, HTTP middleware</td></tr>
        <tr><td style="color:var(--c3)">Proxy</td><td>Need auth/caching/logging without touching real object</td><td>Same interface, intercepts before delegating</td><td>Spring AOP, Hibernate lazy loading, CDN</td></tr>
        <tr><td style="color:var(--c4)">Composite</td><td>Tree structure; want uniform treatment of leaf/branch</td><td>Component interface; Composite holds children</td><td>HTML DOM, UI widget trees, file system</td></tr>
        <tr><td style="color:var(--c5)">Facade</td><td>Client must coordinate many subsystem classes</td><td>High-level class orchestrates subsystems</td><td>Spring ApplicationContext, SDK clients</td></tr>
        <tr><td style="color:var(--c6)">Bridge</td><td>Two orthogonal dimensions exploding into N×M classes</td><td>Abstraction holds Implementation reference (bridge)</td><td>Notification type × channel, JDBC drivers</td></tr>
        <tr><td style="color:var(--c7)">Flyweight</td><td>Millions of objects exhausting memory</td><td>Shared intrinsic state in factory pool; extrinsic passed in</td><td>Java String pool, game particles, TrueCaller</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ===== PATTERNS ===== -->
<div class="m3-view" id="m3-view-patterns">
  <div class="m3-pat-selector">
    <div class="m3-ps-btn active" id="m3-psb0" onclick="m3SelPat(0)" style="border-top:4px solid var(--c1)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c1)">01</span>Adapter
    </div>
    <div class="m3-ps-btn" id="m3-psb1" onclick="m3SelPat(1)" style="border-top:4px solid var(--c2)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c2)">02</span>Decorator
    </div>
    <div class="m3-ps-btn" id="m3-psb2" onclick="m3SelPat(2)" style="border-top:4px solid var(--c3)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c3)">03</span>Proxy
    </div>
    <div class="m3-ps-btn" id="m3-psb3" onclick="m3SelPat(3)" style="border-top:4px solid var(--c4)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c4)">04</span>Composite
    </div>
    <div class="m3-ps-btn" id="m3-psb4" onclick="m3SelPat(4)" style="border-top:4px solid var(--c5)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c5)">05</span>Facade
    </div>
    <div class="m3-ps-btn" id="m3-psb5" onclick="m3SelPat(5)" style="border-top:4px solid var(--c6)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c6)">06</span>Bridge
    </div>
    <div class="m3-ps-btn" id="m3-psb6" onclick="m3SelPat(6)" style="border-top:4px solid var(--c7)">
      <span class="m3-m3-ps-btn-num" style="color:var(--c7)">07</span>Flyweight
    </div>
  </div>

  <!-- ADAPTER -->
  <div class="m3-pat-panel active" id="m3-pp0">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">01</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Adapter</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → Vending Machine Integration</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c1)">Convert the interface of a class into another interface clients expect. Lets classes work together that couldn't otherwise because of incompatible interfaces.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">VendingMachineAdapter.java<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-cm">// Your system expects this interface</span>
<span class="m3-kw">interface</span> <span class="m3-cls">VendingMachine</span> {
    <span class="m3-kw">void</span> <span class="m3-fn">insertCoin</span>(<span class="m3-kw">int</span> amount);      <span class="m3-cm">// amount in paise</span>
    <span class="m3-kw">void</span> <span class="m3-fn">selectProduct</span>(<span class="m3-cls">String</span> m3-code); <span class="m3-cm">// e.g. "A1", "B2"</span>
    <span class="m3-kw">void</span> <span class="m3-fn">dispense</span>();
    <span class="m3-kw">int</span>  <span class="m3-fn">getChange</span>();
}

<span class="m3-cm">// Third-party machine — incompatible interface</span>
<span class="m3-kw">class</span> <span class="m3-cls">NewVendorMachine</span> {
    <span class="m3-kw">public void</span> <span class="m3-fn">payAmount</span>(<span class="m3-kw">double</span> rupees) { <span class="m3-cm">/* ... */</span> }
    <span class="m3-kw">public void</span> <span class="m3-fn">chooseItem</span>(<span class="m3-kw">int</span> itemId)   { <span class="m3-cm">/* ... */</span> }
    <span class="m3-kw">public void</span> <span class="m3-fn">releaseItem</span>()             { <span class="m3-cm">/* ... */</span> }
    <span class="m3-kw">public double</span> <span class="m3-fn">calculateChange</span>()       { <span class="m3-kw">return</span> 5.50; }
}

<span class="m3-cm">// ADAPTER — wraps new vendor machine, speaks old interface</span>
<span class="m3-kw">class</span> <span class="m3-cls">VendingMachineAdapter</span> <span class="m3-kw">implements</span> <span class="m3-cls">VendingMachine</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">NewVendorMachine</span> adaptee;

    <span class="m3-kw">public</span> <span class="m3-cls">VendingMachineAdapter</span>(<span class="m3-cls">NewVendorMachine</span> m) { <span class="m3-kw">this</span>.adaptee = m; }

    <span class="m3-ann">@Override</span>
    <span class="m3-kw">public void</span> <span class="m3-fn">insertCoin</span>(<span class="m3-kw">int</span> amount) {
        adaptee.<span class="m3-fn">payAmount</span>(amount / <span class="m3-str">100.0</span>); <span class="m3-cm">// paise → rupees</span>
    }
    <span class="m3-ann">@Override</span>
    <span class="m3-kw">public void</span> <span class="m3-fn">selectProduct</span>(<span class="m3-cls">String</span> m3-code) {
        <span class="m3-kw">int</span> id = codeToId.get(m3-code);         <span class="m3-cm">// "A1" → 1</span>
        adaptee.<span class="m3-fn">chooseItem</span>(id);
    }
    <span class="m3-ann">@Override</span>
    <span class="m3-kw">public void</span>  <span class="m3-fn">dispense</span>()   { adaptee.<span class="m3-fn">releaseItem</span>(); }
    <span class="m3-ann">@Override</span>
    <span class="m3-kw">public int</span>   <span class="m3-fn">getChange</span>()  { <span class="m3-kw">return</span> (<span class="m3-kw">int</span>)(adaptee.<span class="m3-fn">calculateChange</span>() * <span class="m3-str">100</span>); }
}

<span class="m3-cm">// Client m3-code unchanged — still speaks VendingMachine</span>
<span class="m3-cls">VendingMachine</span> vm = <span class="m3-kw">new</span> <span class="m3-cls">VendingMachineAdapter</span>(<span class="m3-kw">new</span> <span class="m3-cls">NewVendorMachine</span>());
vm.<span class="m3-fn">insertCoin</span>(<span class="m3-str">1000</span>); vm.<span class="m3-fn">selectProduct</span>(<span class="m3-str">"A1"</span>); vm.<span class="m3-fn">dispense</span>();</pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "I use Adapter when integrating third-party systems — create an internal interface, write an Adapter per provider. Stripe, PayPal, Razorpay all become swappable behind one PaymentGateway interface."</div>
  </div>

  <!-- DECORATOR -->
  <div class="m3-pat-panel" id="m3-pp1">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">02</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Decorator</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → Pizza Billing System</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c2)">Attach additional responsibilities dynamically. IS-A AND HAS-A the same type simultaneously. Infinitely composable runtime combinations — no subclass explosion.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">PizzaDecorator.java<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-kw">interface</span> <span class="m3-cls">Pizza</span> { <span class="m3-cls">String</span> <span class="m3-fn">getDescription</span>(); <span class="m3-kw">double</span> <span class="m3-fn">getCost</span>(); }

<span class="m3-kw">class</span> <span class="m3-cls">MargheritaPizza</span> <span class="m3-kw">implements</span> <span class="m3-cls">Pizza</span> {
    <span class="m3-kw">public</span> <span class="m3-cls">String</span> <span class="m3-fn">getDescription</span>() { <span class="m3-kw">return</span> <span class="m3-str">"Margherita"</span>; }
    <span class="m3-kw">public double</span> <span class="m3-fn">getCost</span>()        { <span class="m3-kw">return</span> <span class="m3-str">200.0</span>; }
}

<span class="m3-cm">// ABSTRACT DECORATOR — IS-A Pizza AND HAS-A Pizza</span>
<span class="m3-kw">abstract class</span> <span class="m3-cls">ToppingDecorator</span> <span class="m3-kw">implements</span> <span class="m3-cls">Pizza</span> {
    <span class="m3-kw">protected final</span> <span class="m3-cls">Pizza</span> pizza;
    <span class="m3-kw">public</span> <span class="m3-cls">ToppingDecorator</span>(<span class="m3-cls">Pizza</span> p) { <span class="m3-kw">this</span>.pizza = p; }
}

<span class="m3-cm">// Concrete decorators — each adds exactly one topping</span>
<span class="m3-kw">class</span> <span class="m3-cls">CheeseDecorator</span> <span class="m3-kw">extends</span> <span class="m3-cls">ToppingDecorator</span> {
    <span class="m3-kw">public</span> <span class="m3-cls">CheeseDecorator</span>(<span class="m3-cls">Pizza</span> p) { <span class="m3-kw">super</span>(p); }
    <span class="m3-kw">public</span> <span class="m3-cls">String</span> <span class="m3-fn">getDescription</span>() { <span class="m3-kw">return</span> pizza.<span class="m3-fn">getDescription</span>() + <span class="m3-str">" + Cheese"</span>; }
    <span class="m3-kw">public double</span> <span class="m3-fn">getCost</span>()        { <span class="m3-kw">return</span> pizza.<span class="m3-fn">getCost</span>() + <span class="m3-str">50.0</span>; }
}
<span class="m3-kw">class</span> <span class="m3-cls">MushroomDecorator</span> <span class="m3-kw">extends</span> <span class="m3-cls">ToppingDecorator</span> {
    <span class="m3-kw">public</span> <span class="m3-cls">String</span> <span class="m3-fn">getDescription</span>() { <span class="m3-kw">return</span> pizza.<span class="m3-fn">getDescription</span>() + <span class="m3-str">" + Mushroom"</span>; }
    <span class="m3-kw">public double</span> <span class="m3-fn">getCost</span>()        { <span class="m3-kw">return</span> pizza.<span class="m3-fn">getCost</span>() + <span class="m3-str">35.0</span>; }
    <span class="m3-kw">public</span> <span class="m3-cls">MushroomDecorator</span>(<span class="m3-cls">Pizza</span> p) { <span class="m3-kw">super</span>(p); }
}

<span class="m3-cm">// Runtime composition — any order, any combination</span>
<span class="m3-cls">Pizza</span> order = <span class="m3-kw">new</span> <span class="m3-cls">CheeseDecorator</span>(
                 <span class="m3-kw">new</span> <span class="m3-cls">MushroomDecorator</span>(
                    <span class="m3-kw">new</span> <span class="m3-cls">CheeseDecorator</span>(   <span class="m3-cm">// double cheese!</span>
                       <span class="m3-kw">new</span> <span class="m3-cls">MargheritaPizza</span>())));
<span class="m3-cm">// → "Margherita + Cheese + Mushroom + Cheese"  cost: 335.0</span></pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "Java I/O is Decorator: BufferedReader(InputStreamReader(FileInputStream)). Each wrapper adds one responsibility. Real production use: MetricService(CachingService(DatabaseService)) — cross-cutting concerns as transparent wrappers."</div>
  </div>

  <!-- PROXY -->
  <div class="m3-pat-panel" id="m3-pp2">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">03</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Proxy</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → Car Rental (Protection Proxy)</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c3)">Provide a surrogate to control access. Same interface as real subject — client can't tell the difference. Purpose: intercept calls for auth, caching, logging, or lazy init.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">CarRentalProxy.java — Protection Proxy<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-kw">interface</span> <span class="m3-cls">CarRentalService</span> {
    <span class="m3-cls">Car</span> <span class="m3-fn">rentCar</span>(<span class="m3-cls">String</span> model, <span class="m3-cls">User</span> user);
    <span class="m3-kw">void</span> <span class="m3-fn">returnCar</span>(<span class="m3-cls">String</span> carId, <span class="m3-cls">User</span> user);
}

<span class="m3-kw">class</span> <span class="m3-cls">CarRentalProxy</span> <span class="m3-kw">implements</span> <span class="m3-cls">CarRentalService</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">CarRentalServiceImpl</span> real;
    <span class="m3-kw">private final</span> <span class="m3-cls">AuthService</span> auth;
    <span class="m3-kw">private final</span> <span class="m3-cls">Logger</span> log;

    <span class="m3-ann">@Override</span>
    <span class="m3-kw">public</span> <span class="m3-cls">Car</span> <span class="m3-fn">rentCar</span>(<span class="m3-cls">String</span> model, <span class="m3-cls">User</span> user) {
        <span class="m3-cm">// 1. Authorization (Protection Proxy)</span>
        <span class="m3-kw">if</span> (!auth.<span class="m3-fn">hasValidLicense</span>(user))
            <span class="m3-kw">throw new</span> <span class="m3-cls">UnauthorizedException</span>(<span class="m3-str">"No valid license"</span>);

        <span class="m3-cm">// 2. Pre-logging</span>
        log.<span class="m3-fn">log</span>(<span class="m3-str">"Renting "</span> + model + <span class="m3-str">" for user "</span> + user.<span class="m3-fn">getId</span>());

        <span class="m3-cm">// 3. Delegate to real service</span>
        <span class="m3-cls">Car</span> car = real.<span class="m3-fn">rentCar</span>(model, user);

        <span class="m3-cm">// 4. Post-logging</span>
        log.<span class="m3-fn">log</span>(<span class="m3-str">"Assigned car "</span> + car.<span class="m3-fn">getId</span>());
        <span class="m3-kw">return</span> car;
    }
    <span class="m3-cm">// returnCar similarly delegates after logging</span>
}

<span class="m3-cm">// Client sees same interface — proxy is completely transparent</span>
<span class="m3-cls">CarRentalService</span> svc = <span class="m3-kw">new</span> <span class="m3-cls">CarRentalProxy</span>(real, auth, log);
<span class="m3-cls">Car</span> c = svc.<span class="m3-fn">rentCar</span>(<span class="m3-str">"Camry"</span>, currentUser);</pre></div>
    <div class="m3-concept-row">
      <div class="m3-concept-box"><h4 style="color:var(--c3)">Three Proxy Types</h4>
        <ul><li><strong>Virtual:</strong> Lazy initialisation — defer expensive creation</li><li><strong>Protection:</strong> Auth/permissions check before delegating</li><li><strong>Remote:</strong> Represents object in different process (gRPC stub)</li></ul>
      </div>
      <div class="m3-concept-box"><h4>Real-World Proxies</h4>
        <ul><li>Spring @Transactional, @Cacheable → runtime proxy</li><li>Hibernate lazy loading → Virtual proxy</li><li>gRPC generated stubs → Remote proxy</li><li>CDN → Remote proxy for assets</li></ul>
      </div>
    </div>
    <div class="m3-tip-box"><em>Interview:</em> "Spring AOP generates proxies at runtime — @Cacheable wraps method, checks cache first. @Transactional wraps method in DB transaction. Understanding this means understanding how Spring works internally."</div>
  </div>

  <!-- COMPOSITE -->
  <div class="m3-pat-panel" id="m3-pp3">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">04</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Composite</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → File System (File + Directory)</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c4)">Compose objects into tree structures. Client treats leaf (File) and composite (Directory) identically — one interface, recursive operations, no instanceof checks needed.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">FileSystemComponent.java<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-cm">// Uniform component interface — same for File AND Directory</span>
<span class="m3-kw">interface</span> <span class="m3-cls">FileSystemComponent</span> {
    <span class="m3-cls">String</span> <span class="m3-fn">getName</span>();
    <span class="m3-kw">long</span>   <span class="m3-fn">getSize</span>();
    <span class="m3-kw">void</span>   <span class="m3-fn">display</span>(<span class="m3-cls">String</span> indent);
    <span class="m3-kw">void</span>   <span class="m3-fn">delete</span>();
}

<span class="m3-cm">// LEAF — no children</span>
<span class="m3-kw">class</span> <span class="m3-cls">File</span> <span class="m3-kw">implements</span> <span class="m3-cls">FileSystemComponent</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> name; <span class="m3-kw">private final long</span> size;
    <span class="m3-kw">public long</span>   <span class="m3-fn">getSize</span>()           { <span class="m3-kw">return</span> size; }
    <span class="m3-kw">public void</span>   <span class="m3-fn">display</span>(<span class="m3-cls">String</span> ind) { <span class="m3-cls">System</span>.out.println(ind + <span class="m3-str">"📄 "</span> + name); }
    <span class="m3-kw">public void</span>   <span class="m3-fn">delete</span>()            { <span class="m3-cls">System</span>.out.println(<span class="m3-str">"Delete file: "</span> + name); }
    <span class="m3-kw">public</span> <span class="m3-cls">String</span> <span class="m3-fn">getName</span>()           { <span class="m3-kw">return</span> name; }
    <span class="m3-kw">public</span> <span class="m3-cls">File</span>(<span class="m3-cls">String</span> n, <span class="m3-kw">long</span> s)   { name=n; size=s; }
}

<span class="m3-cm">// COMPOSITE — holds children, operations recurse</span>
<span class="m3-kw">class</span> <span class="m3-cls">Directory</span> <span class="m3-kw">implements</span> <span class="m3-cls">FileSystemComponent</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> name;
    <span class="m3-kw">private final</span> <span class="m3-cls">List</span>&lt;<span class="m3-cls">FileSystemComponent</span>&gt; children = <span class="m3-kw">new</span> <span class="m3-cls">ArrayList</span>&lt;&gt;();

    <span class="m3-kw">public void</span> <span class="m3-fn">add</span>(<span class="m3-cls">FileSystemComponent</span> c) { children.add(c); }

    <span class="m3-cm">// Recursive — works for any depth of nesting</span>
    <span class="m3-kw">public long</span> <span class="m3-fn">getSize</span>() {
        <span class="m3-kw">return</span> children.stream().mapToLong(<span class="m3-cls">FileSystemComponent</span>::getSize).sum();
    }
    <span class="m3-kw">public void</span> <span class="m3-fn">display</span>(<span class="m3-cls">String</span> ind) {
        <span class="m3-cls">System</span>.out.println(ind + <span class="m3-str">"📁 "</span> + name + <span class="m3-str">" ("</span> + <span class="m3-fn">getSize</span>() + <span class="m3-str">" B)"</span>);
        children.forEach(c -> c.<span class="m3-fn">display</span>(ind + <span class="m3-str">"  "</span>));
    }
    <span class="m3-kw">public void</span> <span class="m3-fn">delete</span>() { children.forEach(<span class="m3-cls">FileSystemComponent</span>::delete); }
    <span class="m3-kw">public</span> <span class="m3-cls">String</span> <span class="m3-fn">getName</span>() { <span class="m3-kw">return</span> name; }
    <span class="m3-kw">public</span> <span class="m3-cls">Directory</span>(<span class="m3-cls">String</span> n) { name = n; }
}

<span class="m3-cm">// Client — no instanceof, no type checks needed</span>
<span class="m3-cls">Directory</span> root = <span class="m3-kw">new</span> <span class="m3-cls">Directory</span>(<span class="m3-str">"root"</span>);
root.<span class="m3-fn">add</span>(<span class="m3-kw">new</span> <span class="m3-cls">File</span>(<span class="m3-str">"README.md"</span>, <span class="m3-str">256</span>));
root.<span class="m3-fn">add</span>(src);          <span class="m3-cm">// src is a Directory — same add() call</span>
root.<span class="m3-fn">getSize</span>();         <span class="m3-cm">// Recursively sums all nested files</span></pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "Composite is the pattern behind the HTML DOM — a div can contain buttons or other divs, all support the same operations. When you see a tree where leaf and branch must be interchangeable, Composite is the answer."</div>
  </div>

  <!-- FACADE -->
  <div class="m3-pat-panel" id="m3-pp4">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">05</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Facade</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → Splitwise Expense Management</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c5)">Provide a unified, simplified interface to a complex subsystem. Subsystem classes remain usable directly but Facade provides the common-path shortcut. Client only needs to know Facade.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">SplitwiseFacade.java<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-cm">// Complex subsystems — many classes, many responsibilities</span>
<span class="m3-kw">class</span> <span class="m3-cls">ExpenseService</span>   { <span class="m3-cls">Expense</span> <span class="m3-fn">createExpense</span>(...) {...} }
<span class="m3-kw">class</span> <span class="m3-cls">SplitCalculator</span> { <span class="m3-cls">Map</span> <span class="m3-fn">calculateEqualSplit</span>(...) {...} }
<span class="m3-kw">class</span> <span class="m3-cls">BalanceService</span>  { <span class="m3-cls">Map</span> <span class="m3-fn">getNetBalances</span>(...) {...} }
<span class="m3-kw">class</span> <span class="m3-cls">NotificationService</span> { <span class="m3-kw">void</span> <span class="m3-fn">notifyMembers</span>(...) {...} }

<span class="m3-cm">// FACADE — one class, simple operations, hides all complexity</span>
<span class="m3-kw">class</span> <span class="m3-cls">SplitwiseFacade</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">ExpenseService</span>      expenses;
    <span class="m3-kw">private final</span> <span class="m3-cls">SplitCalculator</span>    calculator;
    <span class="m3-kw">private final</span> <span class="m3-cls">BalanceService</span>     balances;
    <span class="m3-kw">private final</span> <span class="m3-cls">NotificationService</span> notifier;

    <span class="m3-cm">// High-level operation — orchestrates 4 subsystems</span>
    <span class="m3-kw">public void</span> <span class="m3-fn">addExpenseEqualSplit</span>(<span class="m3-cls">String</span> groupId, <span class="m3-cls">String</span> desc,
                                      <span class="m3-kw">double</span> amount, <span class="m3-cls">String</span> paidBy,
                                      <span class="m3-cls">List</span>&lt;<span class="m3-cls">String</span>&gt; members) {
        <span class="m3-cls">Expense</span> expense = expenses.<span class="m3-fn">createExpense</span>(desc, amount, paidBy);
        <span class="m3-cls">Map</span> splits      = calculator.<span class="m3-fn">calculateEqualSplit</span>(expense, members);
        balances.<span class="m3-fn">updateBalances</span>(groupId, splits, paidBy);
        notifier.<span class="m3-fn">notifyExpenseAdded</span>(members, expense);
    }

    <span class="m3-kw">public</span> <span class="m3-cls">List</span>&lt;<span class="m3-cls">Transaction</span>&gt; <span class="m3-fn">getSimplifiedSettlements</span>(<span class="m3-cls">String</span> groupId) {
        <span class="m3-cls">Map</span>&lt;<span class="m3-cls">String</span>, <span class="m3-cls">Double</span>&gt; netBalances = balances.<span class="m3-fn">getNetBalances</span>(groupId);
        <span class="m3-kw">return</span> <span class="m3-cls">SimplifyAlgorithm</span>.<span class="m3-fn">simplify</span>(netBalances); <span class="m3-cm">// min transactions</span>
    }
}

<span class="m3-cm">// Client — one method call does what used to take 10</span>
<span class="m3-cls">SplitwiseFacade</span> sw = <span class="m3-kw">new</span> <span class="m3-cls">SplitwiseFacade</span>();
sw.<span class="m3-fn">addExpenseEqualSplit</span>(<span class="m3-str">"grp1"</span>, <span class="m3-str">"Dinner"</span>, <span class="m3-str">1200.0</span>, <span class="m3-str">"ajay"</span>, members);</pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "Facade vs Adapter: Facade simplifies access to a SUBSYSTEM (multiple classes). Adapter converts ONE incompatible interface. Facade vs Mediator: Facade is one-directional — client talks to Facade. Mediator encapsulates how PEERS communicate with each other."</div>
  </div>

  <!-- BRIDGE -->
  <div class="m3-pat-panel" id="m3-pp5">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">06</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Bridge</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → CricBuzz Notification System</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c6)">Decouple abstraction from implementation so both can vary independently. Replaces N×M subclass explosion with N+M classes. The "bridge" is a reference held in the abstraction.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">CricBuzzBridge.java — Notification Type × Channel<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-cm">// IMPLEMENTATION — HOW to send (one dimension)</span>
<span class="m3-kw">interface</span> <span class="m3-cls">NotificationSender</span> { <span class="m3-kw">void</span> <span class="m3-fn">send</span>(<span class="m3-cls">String</span> to, <span class="m3-cls">String</span> msg); }
<span class="m3-kw">class</span> <span class="m3-cls">SMSSender</span>   <span class="m3-kw">implements</span> <span class="m3-cls">NotificationSender</span> { <span class="m3-cm">/* ... */</span> }
<span class="m3-kw">class</span> <span class="m3-cls">EmailSender</span> <span class="m3-kw">implements</span> <span class="m3-cls">NotificationSender</span> { <span class="m3-cm">/* ... */</span> }
<span class="m3-kw">class</span> <span class="m3-cls">PushSender</span>  <span class="m3-kw">implements</span> <span class="m3-cls">NotificationSender</span> { <span class="m3-cm">/* ... */</span> }

<span class="m3-cm">// ABSTRACTION — WHAT to send (other dimension)</span>
<span class="m3-kw">abstract class</span> <span class="m3-cls">CricketNotification</span> {
    <span class="m3-kw">protected final</span> <span class="m3-cls">NotificationSender</span> sender; <span class="m3-cm">// THE BRIDGE</span>
    <span class="m3-kw">public</span> <span class="m3-cls">CricketNotification</span>(<span class="m3-cls">NotificationSender</span> s) { <span class="m3-kw">this</span>.sender = s; }
    <span class="m3-kw">public abstract void</span> <span class="m3-fn">notify</span>(<span class="m3-cls">String</span> recipient, <span class="m3-cls">Object</span> event);
}

<span class="m3-cm">// Refined abstractions — each is a notification type</span>
<span class="m3-kw">class</span> <span class="m3-cls">WicketNotification</span> <span class="m3-kw">extends</span> <span class="m3-cls">CricketNotification</span> {
    <span class="m3-kw">public</span> <span class="m3-cls">WicketNotification</span>(<span class="m3-cls">NotificationSender</span> s) { <span class="m3-kw">super</span>(s); }
    <span class="m3-kw">public void</span> <span class="m3-fn">notify</span>(<span class="m3-cls">String</span> r, <span class="m3-cls">Object</span> e) {
        sender.<span class="m3-fn">send</span>(r, <span class="m3-str">"WICKET! "</span> + e + <span class="m3-str">" is out!"</span>); <span class="m3-cm">// uses bridge</span>
    }
}
<span class="m3-kw">class</span> <span class="m3-cls">SixNotification</span> <span class="m3-kw">extends</span> <span class="m3-cls">CricketNotification</span> {
    <span class="m3-kw">public</span> <span class="m3-cls">SixNotification</span>(<span class="m3-cls">NotificationSender</span> s) { <span class="m3-kw">super</span>(s); }
    <span class="m3-kw">public void</span> <span class="m3-fn">notify</span>(<span class="m3-cls">String</span> r, <span class="m3-cls">Object</span> e) {
        sender.<span class="m3-fn">send</span>(r, <span class="m3-str">"SIX! "</span> + e + <span class="m3-str">" smashes it!"</span>);
    }
}

<span class="m3-cm">// Mix and match — N types × M channels without N×M classes</span>
<span class="m3-kw">new</span> <span class="m3-cls">WicketNotification</span>(<span class="m3-kw">new</span> <span class="m3-cls">SMSSender</span>()).<span class="m3-fn">notify</span>(<span class="m3-str">"user1"</span>, <span class="m3-str">"Kohli"</span>);
<span class="m3-kw">new</span> <span class="m3-cls">WicketNotification</span>(<span class="m3-kw">new</span> <span class="m3-cls">EmailSender</span>()).<span class="m3-fn">notify</span>(<span class="m3-str">"fan@email"</span>, <span class="m3-str">"Rohit"</span>);
<span class="m3-kw">new</span> <span class="m3-cls">SixNotification</span>(<span class="m3-kw">new</span> <span class="m3-cls">PushSender</span>()).<span class="m3-fn">notify</span>(<span class="m3-str">"device_xyz"</span>, <span class="m3-str">"Dhoni"</span>);</pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "The tell-tale sign for Bridge: two independent dimensions of variation (what × how, shape × rendering, device × OS). Without Bridge: N×M subclasses. With Bridge: N+M classes connected by composition."</div>
  </div>

  <!-- FLYWEIGHT -->
  <div class="m3-pat-panel" id="m3-pp6">
    <div class="m3-pat-masthead"><div class="m3-pat-big-num" style="color:#eee">07</div>
      <div class="m3-pat-info-block">
        <div class="m3-pat-name-big">Flyweight</div>
        <div class="m3-pat-system-m3-label">REAL SYSTEM → TrueCaller (1 billion contacts)</div>
        <div class="m3-pat-intent" style="border-left-color:var(--c7)">Share intrinsic state across huge numbers of objects. Extrinsic state is passed in at runtime. Factory ensures pool reuse. Result: 10,000× memory reduction possible.</div>
      </div>
    </div>
    <div class="m3-m3-code-section"><div class="m3-m3-code-hdr">TrueCallerFlyweight.java<span class="m3-m3-code-lang">JAVA</span></div>
<pre class="m3-code"><span class="m3-cm">// FLYWEIGHT — stores INTRINSIC state (shared, immutable)</span>
<span class="m3-kw">class</span> <span class="m3-cls">ContactMetadata</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> operatorName;  <span class="m3-cm">// "Jio", "Airtel" — thousands share this</span>
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> contactType;   <span class="m3-cm">// "SPAM", "BUSINESS" — few unique values</span>
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> spamLabel;     <span class="m3-cm">// "Telemarketer", null — shared</span>
    <span class="m3-cm">// All final — immutable, so safely shared across threads</span>
}

<span class="m3-cm">// FLYWEIGHT FACTORY — pool ensures reuse</span>
<span class="m3-kw">class</span> <span class="m3-cls">ContactMetadataFactory</span> {
    <span class="m3-kw">private static final</span> <span class="m3-cls">Map</span>&lt;<span class="m3-cls">String</span>,<span class="m3-cls">ContactMetadata</span>&gt; pool = <span class="m3-kw">new</span> <span class="m3-cls">HashMap</span>&lt;&gt;();

    <span class="m3-kw">public static</span> <span class="m3-cls">ContactMetadata</span> <span class="m3-fn">get</span>(<span class="m3-cls">String</span> op, <span class="m3-cls">String</span> type, <span class="m3-cls">String</span> spam) {
        <span class="m3-cls">String</span> key = op + <span class="m3-str">"|"</span> + type + <span class="m3-str">"|"</span> + spam;
        <span class="m3-kw">return</span> pool.<span class="m3-fn">computeIfAbsent</span>(key, k -> <span class="m3-kw">new</span> <span class="m3-cls">ContactMetadata</span>(op, type, spam));
    }
}

<span class="m3-cm">// CLIENT CONTEXT — stores EXTRINSIC state (unique per contact)</span>
<span class="m3-kw">class</span> <span class="m3-cls">PhoneContact</span> {
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> phoneNumber;  <span class="m3-cm">// unique — extrinsic</span>
    <span class="m3-kw">private final</span> <span class="m3-cls">String</span> callerName;   <span class="m3-cm">// unique — extrinsic</span>
    <span class="m3-kw">private final</span> <span class="m3-cls">ContactMetadata</span> meta; <span class="m3-cm">// SHARED — flyweight</span>

    <span class="m3-kw">public</span> <span class="m3-cls">PhoneContact</span>(<span class="m3-cls">String</span> num, <span class="m3-cls">String</span> name, <span class="m3-cls">String</span> op, <span class="m3-cls">String</span> type, <span class="m3-cls">String</span> spam) {
        <span class="m3-kw">this</span>.phoneNumber = num;
        <span class="m3-kw">this</span>.callerName  = name;
        <span class="m3-kw">this</span>.meta = <span class="m3-cls">ContactMetadataFactory</span>.<span class="m3-fn">get</span>(op, type, spam); <span class="m3-cm">// pool lookup</span>
    }
}

<span class="m3-cm">// Memory impact (1 billion contacts):
// Without Flyweight: 1B × 200B metadata = 200 GB
// With Flyweight:    ~1000 unique combos × 200B = 200 KB shared
//                   + 1B × ~30B (phone + name only) = 30 GB extrinsic</span></pre></div>
    <div class="m3-tip-box"><em>Interview:</em> "Java's String pool IS Flyweight — string literals are interned and shared. Integer.valueOf(-128 to 127) returns cached instances. Game engines use Flyweight for particles: one texture/physics object shared by 100,000 bullets."</div>
  </div>
</div>

<!-- ===== DISTINCTIONS ===== -->
<div class="m3-view" id="m3-view-distinctions">
  <div class="m3-distinction">
    <div class="m3-m3-distinction-header">THE MOST COMMONLY CONFUSED TRIO: ADAPTER vs DECORATOR vs PROXY</div>
    <div class="m3-m3-distinction-row" style="background:var(--lighter)">
      <div class="m3-m3-distinction-cell m3-label">Dimension</div>
      <div class="m3-m3-distinction-cell m3-label" style="color:var(--c1)">Adapter</div>
      <div class="m3-m3-distinction-cell m3-label" style="color:var(--c2)">Decorator</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Purpose</div>
      <div class="m3-m3-distinction-cell">Convert incompatible interface</div>
      <div class="m3-m3-distinction-cell">Add behaviour dynamically</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Interface</div>
      <div class="m3-m3-distinction-cell"><strong>Changes</strong> the interface (A→B)</div>
      <div class="m3-m3-distinction-cell"><strong>Same</strong> interface as component</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Wrapped type</div>
      <div class="m3-m3-distinction-cell">Adaptee (different type)</div>
      <div class="m3-m3-distinction-cell">Same component type (IS-A + HAS-A)</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">When to use</div>
      <div class="m3-m3-distinction-cell">Third-party/legacy integration</div>
      <div class="m3-m3-distinction-cell">Adding features without subclassing</div>
    </div>
  </div>

  <div class="m3-distinction" style="margin-top:16px;">
    <div class="m3-m3-distinction-header">ADAPTER vs DECORATOR vs PROXY (continued)</div>
    <div class="m3-m3-distinction-row" style="background:var(--lighter)">
      <div class="m3-m3-distinction-cell m3-label">Dimension</div>
      <div class="m3-m3-distinction-cell m3-label" style="color:var(--c3)">Proxy</div>
      <div class="m3-m3-distinction-cell m3-label" style="color:var(--c5)">Facade</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Purpose</div>
      <div class="m3-m3-distinction-cell">Control access to one object</div>
      <div class="m3-m3-distinction-cell">Simplify interface to a subsystem</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Interface</div>
      <div class="m3-m3-distinction-cell">Same as real subject</div>
      <div class="m3-m3-distinction-cell">New simplified interface</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">Scope</div>
      <div class="m3-m3-distinction-cell">One object</div>
      <div class="m3-m3-distinction-cell">Entire subsystem (many objects)</div>
    </div>
    <div class="m3-m3-distinction-row">
      <div class="m3-m3-distinction-cell m3-label">When to use</div>
      <div class="m3-m3-distinction-cell">Auth, caching, logging, lazy init</div>
      <div class="m3-m3-distinction-cell">Client shouldn't know subsystem details</div>
    </div>
  </div>

  <div style="margin-top:24px;background:var(--ink);color:var(--paper);padding:24px 28px;">
    <div style="font-family:'Inconsolata',monospace;font-size:11px;color:#888;letter-spacing:2px;margin-bottom:16px;">// THE ONE-LINE TEST</div>
    <div style="font-size:14px;line-height:2;font-family:'Inconsolata',monospace;">
      <span style="color:var(--c1)">Adapter:</span> <span style="color:#aaa">"I need to use this component but its interface is wrong"</span><br>
      <span style="color:var(--c2)">Decorator:</span> <span style="color:#aaa">"I need to add features to this object without modifying its class"</span><br>
      <span style="color:var(--c3)">Proxy:</span> <span style="color:#aaa">"I need to control who/how accesses this object"</span><br>
      <span style="color:var(--c4)">Composite:</span> <span style="color:#aaa">"I have a tree and want leaf + branch to behave the same"</span><br>
      <span style="color:var(--c5)">Facade:</span> <span style="color:#aaa">"I want to hide this complex subsystem behind one simple class"</span><br>
      <span style="color:var(--c6)">Bridge:</span> <span style="color:#aaa">"I have two dimensions of variation and don't want N×M subclasses"</span><br>
      <span style="color:var(--c7)">Flyweight:</span> <span style="color:#aaa">"I have millions of similar objects and I'm running out of memory"</span>
    </div>
  </div>

  <table class="m3-sd-table" style="margin-top:24px;">
    <thead><tr><th>PATTERN</th><th>ADVANTAGE</th><th>TRADE-OFF</th></tr></thead>
    <tbody>
      <tr><td style="color:var(--c1)">Adapter</td><td>Integration without touching existing m3-code</td><td>Extra indirection; translation bugs possible</td></tr>
      <tr><td style="color:var(--c2)">Decorator</td><td>Infinite runtime combinations, no subclass explosion</td><td>Deep chains hard to debug; decoration order matters</td></tr>
      <tr><td style="color:var(--c3)">Proxy</td><td>Transparent cross-cutting concerns</td><td>Extra indirection; proxy-related bugs subtle</td></tr>
      <tr><td style="color:var(--c4)">Composite</td><td>Uniform tree operations, no instanceof</td><td>Hard to restrict component types in tree</td></tr>
      <tr><td style="color:var(--c5)">Facade</td><td>Simplifies client m3-code dramatically</td><td>Can become a god object if over-loaded</td></tr>
      <tr><td style="color:var(--c6)">Bridge</td><td>Two dimensions vary independently</td><td>Up-front complexity; must identify dimensions correctly</td></tr>
      <tr><td style="color:var(--c7)">Flyweight</td><td>Massive memory savings</td><td>Client must manage extrinsic state; no object identity</td></tr>
    </tbody>
  </table>
</div>

<!-- ===== SPLITWISE ===== -->
<div class="m3-view" id="m3-view-splitwise">
  <div style="margin-bottom:28px;">
    <div style="font-family:'Inconsolata',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin-bottom:12px;">MINI PROJECT</div>
    <div style="font-family:'Playfair Display',serif;font-size:32px;font-weight:900;margin-bottom:8px;">Splitwise Clone</div>
    <p style="font-size:14px;color:var(--muted);line-height:1.7;max-width:680px;">Complete LLD implementation with the Simplify Algorithm. This is the most architecturally rich problem in Module A3 — it naturally requires Facade + Algorithm + Adapter + Decorator + Composite.</p>
  </div>

  <div class="m3-algorithm-box">
    <div class="m3-algorithm-header">The Splitwise Simplify Algorithm — Minimum Transactions</div>
    <div class="m3-algorithm-body">
      <p style="font-size:13px;color:var(--muted);margin-bottom:16px;line-height:1.7;"><strong style="color:var(--ink)">Problem:</strong> Given a group's net balances (positive = owed money, negative = owes money), find the minimum number of transactions to settle all debts.</p>
      <ul class="m3-step-list">
        <li class="m3-step-item"><div class="m3-step-num">1</div><div>Calculate <strong>net balance</strong> per person: sum what they paid, minus what they owe across all expenses.</div></li>
        <li class="m3-step-item"><div class="m3-step-num">2</div><div>Separate into <strong>creditors</strong> (positive balance — owed money) and <strong>debtors</strong> (negative balance — owe money).</div></li>
        <li class="m3-step-item"><div class="m3-step-num">3</div><div>Use two priority queues: <strong>max-heap of creditors</strong>, <strong>min-heap of debtors</strong>.</div></li>
        <li class="m3-step-item"><div class="m3-step-num">4</div><div><strong>Greedy loop</strong>: take largest creditor + largest debtor. Settle min(credit, debt). If credit > debt, creditor still has balance → re-insert remainder.</div></li>
        <li class="m3-step-item"><div class="m3-step-num">5</div><div>Each loop iteration = <strong>one transaction</strong>. Loop ends when all queues empty = all debts settled.</div></li>
      </ul>
      <div style="margin-top:16px;padding:14px;background:var(--lighter);font-family:'Inconsolata',monospace;font-size:12px;line-height:1.8;">
        Example: Ajay:+600, Ram:-400, Priya:-200, Rahul:+100, Sita:-100<br>
        Naive: up to 4 transactions. Algorithm: <strong>3 minimum</strong><br>
        → Ram pays Ajay 400 | Priya pays Ajay 200 | Sita pays Rahul 100
      </div>
    </div>
  </div>

  <div style="margin-top:20px;background:var(--paper);border:1px solid var(--light);padding:20px;">
    <div style="font-family:'Inconsolata',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin-bottom:16px;">PATTERN USAGE IN SPLITWISE</div>
    <table class="m3-sd-table">
      <thead><tr><th>COMPONENT</th><th>PATTERN</th><th>WHY THIS PATTERN</th></tr></thead>
      <tbody>
        <tr><td>SplitwiseFacade</td><td style="color:var(--c5)">Facade</td><td>Unified API hiding UserService, ExpenseService, BalanceService, Notifier</td></tr>
        <tr><td>EqualSplit / PctSplit / ExactSplit</td><td style="color:var(--muted)">Strategy (preview A4)</td><td>Interchangeable algorithms for splitting an expense</td></tr>
        <tr><td>TaxDecorator, ServiceChargeDecorator</td><td style="color:var(--c2)">Decorator</td><td>Add charges to base expense dynamically at runtime</td></tr>
        <tr><td>WhatsAppAdapter, EmailAdapter</td><td style="color:var(--c1)">Adapter</td><td>Normalize incompatible third-party notification APIs</td></tr>
        <tr><td>User + Group (for notifications)</td><td style="color:var(--c4)">Composite</td><td>Notify individual or entire group with same call</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ===== TASKS ===== -->
<div class="m3-view" id="m3-view-tasks">
  <div class="m3-task-list">
    <div class="m3-task-card">
      <div class="m3-task-hd" onclick="m3ToggleTask(this)"><div class="m3-t-num">01</div><div class="t-m3-label">Pattern Recognition — 6 Scenarios</div><div class="m3-t-meta">~1.5 hrs</div><div class="m3-t-arr">›</div></div>
      <div class="m3-task-bd">
        <p>Identify the correct Structural pattern. One sentence justification each.</p>
        <pre>1. Payment lib accepts PaymentRequest, your system has Order objects.
2. Security system logs all DB access attempts without modifying DB class.
3. Panel can contain Button, Label, or another Panel. All support render().
4. HomeController.leaveHome() controls Lights, Security, Climate at once.
5. 10,000 bullets/sec — each bullet has unique position, shared appearance.
6. Notification type (Alert/Reminder) independent of channel (SMS/Email/Push).</pre>
      </div>
    </div>
    <div class="m3-task-card">
      <div class="m3-task-hd" onclick="m3ToggleTask(this)"><div class="m3-t-num">02</div><div class="t-m3-label">Logger Decorator Chain</div><div class="m3-t-meta">~2 hrs · m3-code</div><div class="m3-t-arr">›</div></div>
      <div class="m3-task-bd">
        <p>Implement Logger decorators that compose in any order.</p>
        <pre>Base: ConsoleLogger — prints to stdout
Decorators:
  TimestampDecorator — prepends "[2024-01-15 14:23:05]"
  LevelDecorator     — prepends [INFO] / [WARN] / [ERROR]
  FileDecorator      — ALSO writes to a log file

Test all 4 combinations:
  new TimestampDecorator(new LevelDecorator(new ConsoleLogger()))
  new LevelDecorator(new TimestampDecorator(new ConsoleLogger()))
  new FileDecorator(new TimestampDecorator(new ConsoleLogger()))
  new FileDecorator(new LevelDecorator(new TimestampDecorator(new ConsoleLogger())))

Show output for each — confirm composition is correct.</pre>
      </div>
    </div>
    <div class="m3-task-card">
      <div class="m3-task-hd" onclick="m3ToggleTask(this)"><div class="m3-t-num">03</div><div class="t-m3-label">CachingProxy for WeatherService</div><div class="m3-t-meta">~2 hrs · m3-code</div><div class="m3-t-arr">›</div></div>
      <div class="m3-task-bd">
        <p>Implement a Virtual+Caching Proxy for an expensive weather API.</p>
        <pre>interface WeatherService {
  WeatherData getWeather(String city);  // expensive HTTP call
}

class RealWeatherService implements WeatherService {
  // Simulate 500ms HTTP call
}

class WeatherServiceProxy implements WeatherService {
  // Cache: Map&lt;city, CacheEntry(data, timestamp)&gt;
  // TTL: 5 minutes
  // Hit: return cache, log "cache hit"
  // Miss: call real service, store, log "cache miss"
}

Test: Call getWeather("Mumbai") 3 times within 5 min
      → only 1 real HTTP call, 2 cache hits
      Wait 5 min, call again → cache miss, new HTTP call</pre>
      </div>
    </div>
    <div class="m3-task-card" style="border-left-color:var(--c5)">
      <div class="m3-task-hd" onclick="m3ToggleTask(this)"><div class="m3-t-num" style="color:var(--c5)">★</div><div class="t-m3-label">Mini Project — Splitwise with Simplify Algorithm</div><div class="m3-t-meta">~5 hrs · full LLD</div><div class="m3-t-arr">›</div></div>
      <div class="m3-task-bd">
        <p>Complete LLD implementation of Splitwise clone.</p>
        <pre>Implement:
1. SplitwiseFacade with all 4 subsystems
2. EqualSplit, PercentageSplit, ExactSplit strategies
3. SimplifyAlgorithm (greedy, priority queue approach)
4. TaxDecorator and ServiceChargeDecorator for Expense
5. NotificationAdapter for at least 2 channels
6. UML class diagram showing all patterns

Demo scenario:
  - 5 members: Ajay, Ram, Priya, Rahul, Sita
  - Add 6 expenses (mix of split types)
  - Print net balances
  - Print simplified settlement plan
  - Settle one transaction, reprint balances</pre>
      </div>
    </div>
  </div>
</div>

<!-- ===== CHECKLIST ===== -->
<div class="m3-view" id="m3-view-checklist">
  <div class="m3-prog-wrap">
    <div class="m3-prog-info"><span id="m3-prog-lbl">0 / 11 completed</span><span>Module A3 → Structural Patterns</span></div>
    <div class="m3-prog-track"><div class="m3-prog-fill" id="m3-prog-fill"></div></div>
  </div>
  <div class="m3-m3-chk-grid">
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Can implement all 7 Structural patterns from memory</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Can distinguish Adapter / Decorator / Proxy in 30 seconds using the one-line test</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Understand Composite's part-whole uniformity — no instanceof needed</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Know Facade vs Mediator vs Adapter (three "simplify/translate" patterns)</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Can identify Bridge's two independent dimensions and the N×M explosion it prevents</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Can separate intrinsic from extrinsic state for Flyweight and calculate memory savings</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">Know which real-world frameworks use each pattern (Spring AOP, Java I/O, String pool)</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">✏️ Task 1: 6 pattern recognition scenarios answered correctly</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">✏️ Task 2: Logger Decorator chain — all 4 compositions tested</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">✏️ Task 3: WeatherService CachingProxy with TTL implemented</div></div>
    <div class="m3-chk" onclick="m3Tick(this)"><div class="m3-m3-chk-box"></div><div class="m3-m3-chk-lbl">✏️ Mini Project: Splitwise clone with Simplify Algorithm + UML complete</div></div>
  </div>

  <div style="margin-top:28px;background:var(--ink);color:var(--paper);padding:24px 28px;">
    <div style="font-family:'Inconsolata',monospace;font-size:10px;color:#666;letter-spacing:2px;margin-bottom:10px;">NEXT MODULE</div>
    <div style="font-family:'Playfair Display',serif;font-size:24px;font-weight:900;margin-bottom:6px;">A4 — Behavioral Design Patterns</div>
    <div style="font-size:13px;color:#888;line-height:1.7;">12 patterns: Strategy, Observer, Chain of Responsibility, State, Command, Iterator, Mediator, Memento, Template Method, Visitor, Null Object, Interpreter. Mini Project: BookMyShow with concurrency handling.</div>
  </div>
</div>

</div><!-- end m3-content -->

<!-- ── BOTTOM NAV ─────────────────────────────────────────────── -->
<div class="m3-bottom-nav" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--border2);padding-top:20px;">
  <a href="/learning/system-design/lld/module-a2-creational/" class="m3-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">← PREVIOUS: LLD A2</a>
  <a href="/learning/system-design/lld/module-a3-notes/" class="m3-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--c1);color:var(--c1);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" class="m3-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a4-behavioral/" class="m3-nav-footer-btn" style="padding:12px 24px;background:var(--c1);color:var(--paper);border-radius:4px;text-decoration:none;font-weight:600;">NEXT: LLD A4 →</a>
</div>
