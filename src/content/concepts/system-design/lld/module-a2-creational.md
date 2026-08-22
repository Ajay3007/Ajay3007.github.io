---
title: "Module A2 — Creational Patterns"
description: "TRACK A · LLD · MODULE A2 · WEEK 4 CREATIONAL PATTERNS Singleton · Factory Method · Abstract Factory · Builder · Prototype 01 SINGLETON 02 FACTORY METHOD 03 ABSTRACT FACTORY 04…"
domain: system-design
track: system-design-lld
order: 4
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a2-creational/
---

<link rel="stylesheet" href="/assets/css/sd-module-a2.css">

<div class="m2-page">

<header class="m2-header">
  <div class="m2-header-eyebrow">TRACK A · LLD · MODULE A2 · WEEK 4</div>
  <h1>CREATIONAL<br><em>PATTERNS</em></h1>
  <div class="m2-header-sub">Singleton · Factory Method · Abstract Factory · Builder · Prototype</div>
  <div class="m2-pattern-strip">
    <div class="m2-p-badge" style="color:var(--p1);border-color:rgba(240,165,0,0.3);">01 SINGLETON</div>
    <div class="m2-p-badge" style="color:var(--p2);border-color:rgba(224,123,0,0.3);">02 FACTORY METHOD</div>
    <div class="m2-p-badge" style="color:var(--p3);border-color:rgba(201,77,30,0.3);">03 ABSTRACT FACTORY</div>
    <div class="m2-p-badge" style="color:var(--p4);border-color:rgba(106,143,106,0.3);">04 BUILDER</div>
    <div class="m2-p-badge" style="color:var(--p5);border-color:rgba(90,122,154,0.3);">05 PROTOTYPE</div>
  </div>
</header>

<nav class="m2-nav">
  <div class="m2-nav-tab active" onclick="m2Show('overview',this)">Overview</div>
  <div class="m2-nav-tab" onclick="m2Show('patterns',this)">Pattern Deep Dives</div>
  <div class="m2-nav-tab" onclick="m2Show('compare',this)">Comparison</div>
  <div class="m2-nav-tab" onclick="m2Show('atm',this)">ATM Project</div>
  <div class="m2-nav-tab" onclick="m2Show('tasks',this)">Tasks</div>
  <div class="m2-nav-tab" onclick="m2Show('checklist',this)">Checklist</div>
</nav>

<div class="m2-content">

<!-- ===== OVERVIEW ===== -->
<div class="m2-view active" id="m2-view-overview">
  <div style="margin-bottom:28px;">
    <p style="font-size:14px;color:var(--muted);line-height:1.7;max-width:680px;">
      Creational patterns abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented. Each solves a different flavour of the same question: <em style="color:var(--gold)">how do we create objects in a flexible, decoupled way?</em>
    </p>
  </div>

  <div class="m2-overview-grid">
    <div class="m2-overview-card m2-oc-1" onclick="m2GoToPattern('p1')">
      <div class="m2-oc-num">01</div>
      <div class="m2-oc-name">Singleton</div>
      <div class="m2-oc-system">→ Logging System</div>
      <div class="m2-oc-problem">Ensure exactly one instance exists globally and provide a single access point to it.</div>
    </div>
    <div class="m2-overview-card m2-oc-2" onclick="m2GoToPattern('p2')">
      <div class="m2-oc-num">02</div>
      <div class="m2-oc-name">Factory Method</div>
      <div class="m2-oc-system">→ Parking Lot</div>
      <div class="m2-oc-problem">Decouple object creation from usage. Let subclasses decide which class to instantiate.</div>
    </div>
    <div class="m2-overview-card m2-oc-3" onclick="m2GoToPattern('p3')">
      <div class="m2-oc-num">03</div>
      <div class="m2-oc-name">Abstract Factory</div>
      <div class="m2-oc-system">→ Snake & Ladder</div>
      <div class="m2-oc-problem">Create families of related objects that must be used together consistently.</div>
    </div>
    <div class="m2-overview-card m2-oc-4" onclick="m2GoToPattern('p4')">
      <div class="m2-oc-num">04</div>
      <div class="m2-oc-name">Builder</div>
      <div class="m2-oc-system">→ Chess Game</div>
      <div class="m2-oc-problem">Construct complex objects step-by-step. Separate construction from representation.</div>
    </div>
    <div class="m2-overview-card m2-oc-5" onclick="m2GoToPattern('p5')">
      <div class="m2-oc-num">05</div>
      <div class="m2-oc-name">Prototype</div>
      <div class="m2-oc-system">→ File System</div>
      <div class="m2-oc-problem">Clone expensive objects efficiently instead of creating from scratch each time.</div>
    </div>
  </div>

  <div style="background:var(--surface);border:1px solid var(--border);border-radius:4px;padding:24px;margin-top:8px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--gold);letter-spacing:2px;margin-bottom:16px;">// WHEN TO REACH FOR EACH PATTERN</div>
    <div class="table-responsive">
    <table class="m2-comp-table">
      <thead><tr><th>SMELL / TRIGGER</th><th>PATTERN</th><th>REPLACES</th></tr></thead>
      <tbody>
        <tr><td>global state needed, exactly one instance</td><td style="color:var(--p1)">Singleton</td><td>static global variables</td></tr>
        <tr><td>if/else picks which class to new up</td><td style="color:var(--p2)">Factory Method</td><td>switch-on-type creation</td></tr>
        <tr><td>multiple products must be used together consistently</td><td style="color:var(--p3)">Abstract Factory</td><td>mixed product families</td></tr>
        <tr><td>4+ constructor params, many optional</td><td style="color:var(--p4)">Builder</td><td>telescoping constructors</td></tr>
        <tr><td>creating object is expensive, need many similar ones</td><td style="color:var(--p5)">Prototype</td><td>repeated expensive construction</td></tr>
      </tbody>
    </table>
    </div>
  </div>

</div>

<!-- ===== PATTERNS ===== -->
<div class="m2-view" id="m2-view-patterns">
  <div class="m2-pat-nav">
    <div class="m2-pat-btn p1 active" onclick="m2SelPat('p1',this)">01 · Singleton</div>
    <div class="m2-pat-btn p2" onclick="m2SelPat('p2',this)">02 · Factory Method</div>
    <div class="m2-pat-btn p3" onclick="m2SelPat('p3',this)">03 · Abstract Factory</div>
    <div class="m2-pat-btn p4" onclick="m2SelPat('p4',this)">04 · Builder</div>
    <div class="m2-pat-btn p5" onclick="m2SelPat('p5',this)">05 · Prototype</div>
  </div>

  <!-- SINGLETON -->
  <div class="m2-pat-panel active" id="m2-pat-p1">
    <div class="m2-pat-header">
      <div class="m2-pat-number" style="color:var(--p1)">01</div>
      <div class="m2-pat-info">
        <div class="m2-pat-name">Singleton</div>
        <div class="m2-pat-system">REAL SYSTEM → Logging System</div>
        <div class="m2-pat-intent" style="border-left-color:var(--p1)">Ensure a class has exactly one instance and provide a global access point to it. Useful for resources that must be shared and must exist only once.</div>
      </div>
    </div>

    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin-bottom:12px;">// THREAD-SAFE IMPLEMENTATION (DOUBLE-CHECKED LOCKING)</div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">Logger.java — Thread-safe Singleton <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-kw">public class</span> <span class="m2-cls">Logger</span> {
    <span class="m2-cm">// volatile: prevents CPU caching the reference across threads</span>
    <span class="m2-kw">private static volatile</span> <span class="m2-cls">Logger</span> instance;
    <span class="m2-kw">private</span> <span class="m2-cls">List</span>&lt;<span class="m2-cls">String</span>&gt; logs = <span class="m2-kw">new</span> <span class="m2-cls">ArrayList</span>&lt;&gt;();

    <span class="m2-kw">private</span> <span class="m2-fn">Logger</span>() {}  <span class="m2-cm">// No public constructor</span>

    <span class="m2-kw">public static</span> <span class="m2-cls">Logger</span> <span class="m2-fn">getInstance</span>() {
        <span class="m2-kw">if</span> (instance == <span class="m2-kw">null</span>) {              <span class="m2-cm">// 1st check — no lock (fast path)</span>
            <span class="m2-kw">synchronized</span> (<span class="m2-cls">Logger</span>.class) {
                <span class="m2-kw">if</span> (instance == <span class="m2-kw">null</span>) {          <span class="m2-cm">// 2nd check — with lock (safe)</span>
                    instance = <span class="m2-kw">new</span> <span class="m2-cls">Logger</span>();
                }
            }
        }
        <span class="m2-kw">return</span> instance;
    }

    <span class="m2-kw">public void</span> <span class="m2-fn">log</span>(<span class="m2-cls">String</span> message) {
        logs.add(<span class="m2-str">"["</span> + <span class="m2-cls">LocalDateTime</span>.now() + <span class="m2-str">"] "</span> + message);
    }
}</div>
    </div>

    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin:20px 0 12px;">// BETTER: ENUM SINGLETON (PREFERRED)</div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">Logger.java — Enum Singleton <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-kw">public enum</span> <span class="m2-cls">Logger</span> {
    INSTANCE;  <span class="m2-cm">// JVM guarantees: single init + thread-safe + serialisation-safe</span>

    <span class="m2-kw">private final</span> <span class="m2-cls">List</span>&lt;<span class="m2-cls">String</span>&gt; logs = <span class="m2-kw">new</span> <span class="m2-cls">ArrayList</span>&lt;&gt;();

    <span class="m2-kw">public void</span> <span class="m2-fn">log</span>(<span class="m2-cls">String</span> msg) { logs.add(msg); }
    <span class="m2-kw">public</span> <span class="m2-cls">List</span>&lt;<span class="m2-cls">String</span>&gt; <span class="m2-fn">getLogs</span>() { <span class="m2-kw">return</span> <span class="m2-cls">Collections</span>.unmodifiableList(logs); }
}

<span class="m2-cm">// Usage</span>
<span class="m2-cls">Logger</span>.INSTANCE.<span class="m2-fn">log</span>(<span class="m2-str">"Server started"</span>);
<span class="m2-cls">Logger</span>.INSTANCE.<span class="m2-fn">log</span>(<span class="m2-str">"User 42 logged in"</span>);</div>
    </div>
    <div class="m2-when-grid">
      <div class="m2-when-card yes">
        <h4>✓ Use Singleton</h4>
        <ul class="m2-when-list">
          <li>Logger / Audit trail</li>
          <li>Configuration manager</li>
          <li>DB connection pool</li>
          <li>Thread pool manager</li>
          <li>Cache manager</li>
        </ul>
      </div>
      <div class="m2-when-card no">
        <h4>✗ Avoid Singleton</h4>
        <ul class="m2-when-list">
          <li>"Just because only one now" — global state is dangerous</li>
          <li>When testability matters (hard to mock)</li>
          <li>In microservices (process-scoped only)</li>
          <li>When DI container can scope it instead</li>
        </ul>
      </div>
    </div>
    <div class="m2-tip-box">In production: use DI container with singleton scope (@Singleton, @Bean) instead of static getInstance(). Same behaviour — fully injectable and mockable. This satisfies DIP.</div>
  </div>

  <!-- FACTORY METHOD -->
  <div class="m2-pat-panel" id="m2-pat-p2">
    <div class="m2-pat-header">
      <div class="m2-pat-number" style="color:var(--p2)">02</div>
      <div class="m2-pat-info">
        <div class="m2-pat-name">Factory Method</div>
        <div class="m2-pat-system">REAL SYSTEM → Parking Lot Spot Creation</div>
        <div class="m2-pat-intent" style="border-left-color:var(--p2)">Define an interface for creating an object, but let subclasses decide which class to instantiate. Decouples the caller from the concrete class being created.</div>
      </div>
    </div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">ParkingSpot Factory — Factory Method Pattern <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-cm">// Product interface</span>
<span class="m2-kw">interface</span> <span class="m2-cls">ParkingSpot</span> {
    <span class="m2-kw">boolean</span> <span class="m2-fn">canFit</span>(<span class="m2-cls">Vehicle</span> v);
    <span class="m2-kw">double</span>  <span class="m2-fn">getHourlyRate</span>();
}

<span class="m2-cm">// Concrete Products</span>
<span class="m2-kw">class</span> <span class="m2-cls">CarSpot</span> <span class="m2-kw">implements</span> <span class="m2-cls">ParkingSpot</span> {
    <span class="m2-kw">public boolean</span> <span class="m2-fn">canFit</span>(<span class="m2-cls">Vehicle</span> v) { <span class="m2-kw">return</span> v.getType() == <span class="m2-cls">VehicleType</span>.CAR; }
    <span class="m2-kw">public double</span>  <span class="m2-fn">getHourlyRate</span>()      { <span class="m2-kw">return</span> <span class="m2-num">20.0</span>; }
}
<span class="m2-kw">class</span> <span class="m2-cls">BikeSpot</span>  <span class="m2-kw">implements</span> <span class="m2-cls">ParkingSpot</span> { <span class="m2-cm">/* similar */</span> }
<span class="m2-kw">class</span> <span class="m2-cls">TruckSpot</span> <span class="m2-kw">implements</span> <span class="m2-cls">ParkingSpot</span> { <span class="m2-cm">/* similar */</span> }

<span class="m2-cm">// Creator — defines the FACTORY METHOD</span>
<span class="m2-kw">abstract class</span> <span class="m2-cls">SpotCreator</span> {
    <span class="m2-kw">public abstract</span> <span class="m2-cls">ParkingSpot</span> <span class="m2-fn">createSpot</span>(<span class="m2-kw">int</span> spotNum);

    <span class="m2-kw">public</span> <span class="m2-cls">ParkingSpot</span> <span class="m2-fn">createAndRegister</span>(<span class="m2-kw">int</span> n) {
        <span class="m2-cls">ParkingSpot</span> spot = <span class="m2-fn">createSpot</span>(n); <span class="m2-cm">// ← calls subclass impl</span>
        <span class="m2-cls">SpotRegistry</span>.<span class="m2-fn">register</span>(spot);
        <span class="m2-kw">return</span> spot;
    }
}

<span class="m2-cm">// Concrete Creators — each overrides createSpot()</span>
<span class="m2-kw">class</span> <span class="m2-cls">CarSpotCreator</span>   <span class="m2-kw">extends</span> <span class="m2-cls">SpotCreator</span> {
    <span class="m2-kw">public</span> <span class="m2-cls">ParkingSpot</span> <span class="m2-fn">createSpot</span>(<span class="m2-kw">int</span> n) { <span class="m2-kw">return new</span> <span class="m2-cls">CarSpot</span>(n); }
}
<span class="m2-kw">class</span> <span class="m2-cls">TruckSpotCreator</span> <span class="m2-kw">extends</span> <span class="m2-cls">SpotCreator</span> {
    <span class="m2-kw">public</span> <span class="m2-cls">ParkingSpot</span> <span class="m2-fn">createSpot</span>(<span class="m2-kw">int</span> n) { <span class="m2-kw">return new</span> <span class="m2-cls">TruckSpot</span>(n); }
}
<span class="m2-cm">// Adding BikeSpotCreator = new class only, ZERO modification to existing code (OCP)</span></div>
    </div>
    <div class="m2-tip-box">Tell-tale sign Factory Method is needed: if/else or switch chains that call `new ConcreteType()` based on a string or enum. The fix: one Creator subclass per product type.</div>
  </div>

  <!-- ABSTRACT FACTORY -->
  <div class="m2-pat-panel" id="m2-pat-p3">
    <div class="m2-pat-header">
      <div class="m2-pat-number" style="color:var(--p3)">03</div>
      <div class="m2-pat-info">
        <div class="m2-pat-name">Abstract Factory</div>
        <div class="m2-pat-system">REAL SYSTEM → Snake & Ladder (Themed Game)</div>
        <div class="m2-pat-intent" style="border-left-color:var(--p3)">Provide an interface for creating families of related objects without specifying concrete classes. Swapping one factory swaps the entire product family.</div>
      </div>
    </div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">GameFactory — Abstract Factory Pattern <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-cm">// Abstract Factory interface — creates a FAMILY of products</span>
<span class="m2-kw">interface</span> <span class="m2-cls">GameFactory</span> {
    <span class="m2-cls">Board</span>  <span class="m2-fn">createBoard</span>();
    <span class="m2-cls">Dice</span>   <span class="m2-fn">createDice</span>();
    <span class="m2-cls">Snake</span>  <span class="m2-fn">createSnake</span>();
    <span class="m2-cls">Ladder</span> <span class="m2-fn">createLadder</span>();
}

<span class="m2-cm">// Concrete Factory 1 — Classic theme (all classic products)</span>
<span class="m2-kw">class</span> <span class="m2-cls">ClassicGameFactory</span> <span class="m2-kw">implements</span> <span class="m2-cls">GameFactory</span> {
    <span class="m2-kw">public</span> <span class="m2-cls">Board</span>  <span class="m2-fn">createBoard</span>()  { <span class="m2-kw">return new</span> <span class="m2-cls">ClassicBoard</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Dice</span>   <span class="m2-fn">createDice</span>()   { <span class="m2-kw">return new</span> <span class="m2-cls">ClassicDice</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Snake</span>  <span class="m2-fn">createSnake</span>()  { <span class="m2-kw">return new</span> <span class="m2-cls">ClassicSnake</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Ladder</span> <span class="m2-fn">createLadder</span>() { <span class="m2-kw">return new</span> <span class="m2-cls">ClassicLadder</span>(); }
}

<span class="m2-cm">// Concrete Factory 2 — Digital theme (all digital products)</span>
<span class="m2-kw">class</span> <span class="m2-cls">DigitalGameFactory</span> <span class="m2-kw">implements</span> <span class="m2-cls">GameFactory</span> {
    <span class="m2-kw">public</span> <span class="m2-cls">Board</span>  <span class="m2-fn">createBoard</span>()  { <span class="m2-kw">return new</span> <span class="m2-cls">DigitalBoard</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Dice</span>   <span class="m2-fn">createDice</span>()   { <span class="m2-kw">return new</span> <span class="m2-cls">DigitalDice</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Snake</span>  <span class="m2-fn">createSnake</span>()  { <span class="m2-kw">return new</span> <span class="m2-cls">DigitalSnake</span>(); }
    <span class="m2-kw">public</span> <span class="m2-cls">Ladder</span> <span class="m2-fn">createLadder</span>() { <span class="m2-kw">return new</span> <span class="m2-cls">DigitalLadder</span>(); }
}

<span class="m2-cm">// Client — knows NOTHING about Classic vs Digital specifics</span>
<span class="m2-kw">class</span> <span class="m2-cls">SnakeLadderGame</span> {
    <span class="m2-kw">private final</span> <span class="m2-cls">Board</span> board; <span class="m2-kw">private final</span> <span class="m2-cls">Dice</span> dice;

    <span class="m2-kw">public</span> <span class="m2-cls">SnakeLadderGame</span>(<span class="m2-cls">GameFactory</span> factory) {
        <span class="m2-cm">// Swap theme by passing different factory — zero code change here</span>
        board = factory.<span class="m2-fn">createBoard</span>();
        dice  = factory.<span class="m2-fn">createDice</span>();
    }
}

<span class="m2-cm">// One-line theme switch:</span>
<span class="m2-kw">new</span> <span class="m2-cls">SnakeLadderGame</span>(<span class="m2-kw">new</span> <span class="m2-cls">ClassicGameFactory</span>());
<span class="m2-kw">new</span> <span class="m2-cls">SnakeLadderGame</span>(<span class="m2-kw">new</span> <span class="m2-cls">DigitalGameFactory</span>());</div>
    </div>
    <div class="m2-tip-box">Abstract Factory vs Factory Method: Factory Method creates ONE product via subclassing. Abstract Factory creates a FAMILY of products via composition (inject factory object). When products must be consistent together → Abstract Factory.</div>
  </div>

  <!-- BUILDER -->
  <div class="m2-pat-panel" id="m2-pat-p4">
    <div class="m2-pat-header">
      <div class="m2-pat-number" style="color:var(--p4)">04</div>
      <div class="m2-pat-info">
        <div class="m2-pat-name">Builder</div>
        <div class="m2-pat-system">REAL SYSTEM → Chess Game (Piece Construction)</div>
        <div class="m2-pat-intent" style="border-left-color:var(--p4)">Separate the construction of a complex object from its representation. Required fields in constructor, optional fields via method chaining, validate before build, result is immutable.</div>
      </div>
    </div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">ChessPiece.Builder — Builder Pattern <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-kw">class</span> <span class="m2-cls">ChessPiece</span> {
    <span class="m2-cm">// All fields FINAL — immutable after build()</span>
    <span class="m2-kw">private final</span> <span class="m2-cls">String</span>  type, color;   <span class="m2-cm">// required</span>
    <span class="m2-kw">private final int</span>     file, rank;    <span class="m2-cm">// required</span>
    <span class="m2-kw">private final boolean</span> hasMoved;      <span class="m2-cm">// optional</span>
    <span class="m2-kw">private final</span> <span class="m2-cls">String</span>  sprite;        <span class="m2-cm">// optional</span>
    <span class="m2-kw">private final int</span>     pointValue;    <span class="m2-cm">// optional</span>

    <span class="m2-kw">private</span> <span class="m2-cls">ChessPiece</span>(<span class="m2-cls">Builder</span> b) {
        type = b.type; color = b.color; file = b.file; rank = b.rank;
        hasMoved = b.hasMoved; sprite = b.sprite; pointValue = b.pointValue;
    }

    <span class="m2-kw">public static class</span> <span class="m2-cls">Builder</span> {
        <span class="m2-kw">private final</span> <span class="m2-cls">String</span> type, color;  <span class="m2-cm">// required — set in constructor</span>
        <span class="m2-kw">private final int</span>    file, rank;

        <span class="m2-kw">private boolean</span> hasMoved   = <span class="m2-kw">false</span>;    <span class="m2-cm">// optional defaults</span>
        <span class="m2-kw">private</span> <span class="m2-cls">String</span>  sprite     = <span class="m2-str">"default"</span>;
        <span class="m2-kw">private int</span>     pointValue = <span class="m2-num">1</span>;

        <span class="m2-kw">public</span> <span class="m2-cls">Builder</span>(<span class="m2-cls">String</span> type, <span class="m2-cls">String</span> color, <span class="m2-kw">int</span> file, <span class="m2-kw">int</span> rank) {
            <span class="m2-kw">this</span>.type = type; <span class="m2-kw">this</span>.color = color;
            <span class="m2-kw">this</span>.file = file; <span class="m2-kw">this</span>.rank = rank;
        }

        <span class="m2-cm">// Fluent setters — each returns this for chaining</span>
        <span class="m2-kw">public</span> <span class="m2-cls">Builder</span> <span class="m2-fn">hasMoved</span>(<span class="m2-kw">boolean</span> m) { hasMoved = m; <span class="m2-kw">return this</span>; }
        <span class="m2-kw">public</span> <span class="m2-cls">Builder</span> <span class="m2-fn">sprite</span>(<span class="m2-cls">String</span> s)    { sprite = s;   <span class="m2-kw">return this</span>; }
        <span class="m2-kw">public</span> <span class="m2-cls">Builder</span> <span class="m2-fn">points</span>(<span class="m2-kw">int</span> p)        { pointValue=p; <span class="m2-kw">return this</span>; }

        <span class="m2-kw">public</span> <span class="m2-cls">ChessPiece</span> <span class="m2-fn">build</span>() {
            <span class="m2-kw">if</span> (file &lt; <span class="m2-num">0</span> || file &gt; <span class="m2-num">7</span>) <span class="m2-kw">throw new</span> <span class="m2-cls">IllegalArgumentException</span>(<span class="m2-str">"Bad file"</span>);
            <span class="m2-kw">if</span> (rank &lt; <span class="m2-num">0</span> || rank &gt; <span class="m2-num">7</span>) <span class="m2-kw">throw new</span> <span class="m2-cls">IllegalArgumentException</span>(<span class="m2-str">"Bad rank"</span>);
            <span class="m2-kw">return new</span> <span class="m2-cls">ChessPiece</span>(<span class="m2-kw">this</span>);
        }
    }
}

<span class="m2-cm">// Readable construction — no nulls, order of optionals doesn't matter</span>
<span class="m2-cls">ChessPiece</span> queen = <span class="m2-kw">new</span> <span class="m2-cls">ChessPiece</span>.<span class="m2-cls">Builder</span>(<span class="m2-str">"QUEEN"</span>, <span class="m2-str">"WHITE"</span>, <span class="m2-num">3</span>, <span class="m2-num">0</span>)
    .<span class="m2-fn">points</span>(<span class="m2-num">9</span>)
    .<span class="m2-fn">sprite</span>(<span class="m2-str">"queen_white.png"</span>)
    .<span class="m2-fn">hasMoved</span>(<span class="m2-kw">false</span>)
    .<span class="m2-fn">build</span>();</div>
    </div>
    <div class="m2-tip-box">Required fields go in the Builder constructor (can't miss them). Optional fields use method chaining. validate() inside build() before object is created. The product's private constructor ensures only Builder can create it.</div>
  </div>

  <!-- PROTOTYPE -->
  <div class="m2-pat-panel" id="m2-pat-p5">
    <div class="m2-pat-header">
      <div class="m2-pat-number" style="color:var(--p5)">05</div>
      <div class="m2-pat-info">
        <div class="m2-pat-name">Prototype</div>
        <div class="m2-pat-system">REAL SYSTEM → File System (Node Cloning)</div>
        <div class="m2-pat-intent" style="border-left-color:var(--p5)">Clone objects instead of creating from scratch. Register expensive-to-build templates in a registry, clone on demand. Deep copy = independent, shallow copy = shared state.</div>
      </div>
    </div>
    <div class="m2-code-wrap">
      <div class="m2-code-header">FileSystemItem + Registry — Prototype Pattern <span class="m2-code-lang">JAVA</span></div>
      <div class="m2-code-body"><span class="m2-kw">abstract class</span> <span class="m2-cls">FileSystemItem</span> {
    <span class="m2-kw">protected</span> <span class="m2-cls">String</span> name, path, permissions;
    <span class="m2-kw">protected long</span>   size;

    <span class="m2-cm">// Copy constructor — each subclass calls super(other)</span>
    <span class="m2-kw">protected</span> <span class="m2-cls">FileSystemItem</span>(<span class="m2-cls">FileSystemItem</span> other) {
        <span class="m2-kw">this</span>.name = other.name; <span class="m2-kw">this</span>.path = other.path;
        <span class="m2-kw">this</span>.size = other.size; <span class="m2-kw">this</span>.permissions = other.permissions;
    }

    <span class="m2-kw">public abstract</span> <span class="m2-cls">FileSystemItem</span> <span class="m2-fn">clone</span>();  <span class="m2-cm">// Each subclass deep-copies itself</span>
}

<span class="m2-kw">class</span> <span class="m2-cls">FileNode</span> <span class="m2-kw">extends</span> <span class="m2-cls">FileSystemItem</span> {
    <span class="m2-kw">private</span> <span class="m2-cls">String</span> contentType, encoding;

    <span class="m2-kw">private</span> <span class="m2-cls">FileNode</span>(<span class="m2-cls">FileNode</span> other) {
        <span class="m2-kw">super</span>(other);
        <span class="m2-kw">this</span>.contentType = other.contentType;
        <span class="m2-kw">this</span>.encoding = other.encoding;
    }

    <span class="m2-ann">@Override</span>
    <span class="m2-kw">public</span> <span class="m2-cls">FileNode</span> <span class="m2-fn">clone</span>() { <span class="m2-kw">return new</span> <span class="m2-cls">FileNode</span>(<span class="m2-kw">this</span>); }
}

<span class="m2-cm">// Prototype Registry — build once, clone many times</span>
<span class="m2-kw">class</span> <span class="m2-cls">FileTemplateRegistry</span> {
    <span class="m2-kw">private</span> <span class="m2-cls">Map</span>&lt;<span class="m2-cls">String</span>, <span class="m2-cls">FileSystemItem</span>&gt; templates = <span class="m2-kw">new</span> <span class="m2-cls">HashMap</span>&lt;&gt;();

    <span class="m2-kw">public void</span> <span class="m2-fn">register</span>(<span class="m2-cls">String</span> key, <span class="m2-cls">FileSystemItem</span> t) { templates.put(key, t); }

    <span class="m2-kw">public</span> <span class="m2-cls">FileSystemItem</span> <span class="m2-fn">get</span>(<span class="m2-cls">String</span> key) {
        <span class="m2-kw">return</span> templates.get(key).<span class="m2-fn">clone</span>(); <span class="m2-cm">// Always return CLONE, never template</span>
    }
}

<span class="m2-cm">// Usage: create expensive template once</span>
<span class="m2-cls">FileNode</span> cfg = <span class="m2-kw">new</span> <span class="m2-cls">FileNode</span>(<span class="m2-str">"config"</span>, <span class="m2-str">"/"</span>, <span class="m2-num">0</span>, <span class="m2-str">"rw-r--r--"</span>, <span class="m2-str">"application/json"</span>);
registry.<span class="m2-fn">register</span>(<span class="m2-str">"json-config"</span>, cfg);

<span class="m2-cm">// Cheap clones — no re-initialisation</span>
<span class="m2-cls">FileNode</span> appCfg = (<span class="m2-cls">FileNode</span>) registry.<span class="m2-fn">get</span>(<span class="m2-str">"json-config"</span>);
appCfg.<span class="m2-fn">setName</span>(<span class="m2-str">"app-config.json"</span>);  <span class="m2-cm">// Independent — doesn't affect template</span></div>
    </div>
    <div class="m2-tip-box">Deep vs Shallow: Java's Object.clone() is shallow — nested objects are shared. Always implement deep copy manually via copy constructors. Spring's prototype-scoped beans use this exact pattern.</div>
  </div>
</div>

<!-- ===== COMPARISON ===== -->
<div class="m2-view" id="m2-view-compare">
  <div class="table-responsive">
  <table class="m2-comp-table">
    <thead>
      <tr>
        <th>PATTERN</th>
        <th>CREATES</th>
        <th>MECHANISM</th>
        <th>SOLID ENFORCED</th>
        <th>TRADE-OFF</th>
        <th>REAL-WORLD</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="color:var(--p1)">Singleton</td>
        <td>Single shared instance</td>
        <td>Private constructor + static accessor</td>
        <td>
          <span class="m2-solid-badge" style="background:rgba(201,77,30,0.15);color:var(--rust)">SRP</span>
        </td>
        <td>Hard to test, global state, hidden deps</td>
        <td>Logger, Config, ThreadPool</td>
      </tr>
      <tr>
        <td style="color:var(--p2)">Factory Method</td>
        <td>One product (varies by subclass)</td>
        <td>Abstract creator; subclass overrides createXxx()</td>
        <td>
          <span class="m2-solid-badge" style="background:rgba(106,143,106,0.15);color:var(--sage)">OCP</span>
          <span class="m2-solid-badge" style="background:rgba(90,122,154,0.15);color:var(--steel)">DIP</span>
        </td>
        <td>One extra class per product type</td>
        <td>ParkingSpot, Notification types</td>
      </tr>
      <tr>
        <td style="color:var(--p3)">Abstract Factory</td>
        <td>Family of consistent products</td>
        <td>Factory interface injected; swap factory = swap family</td>
        <td>
          <span class="m2-solid-badge" style="background:rgba(106,143,106,0.15);color:var(--sage)">OCP</span>
          <span class="m2-solid-badge" style="background:rgba(90,122,154,0.15);color:var(--steel)">DIP</span>
          <span class="m2-solid-badge" style="background:rgba(240,165,0,0.15);color:var(--gold)">ISP</span>
        </td>
        <td>Adding new product type = update all factories</td>
        <td>Java AWT, JDBC, Spring contexts</td>
      </tr>
      <tr>
        <td style="color:var(--p4)">Builder</td>
        <td>Complex object step-by-step</td>
        <td>Inner Builder class; method chaining; validate on build()</td>
        <td>
          <span class="m2-solid-badge" style="background:rgba(201,77,30,0.15);color:var(--rust)">SRP</span>
          <span class="m2-solid-badge" style="background:rgba(106,143,106,0.15);color:var(--sage)">OCP</span>
        </td>
        <td>Doubles code volume for the object</td>
        <td>StringBuilder, HttpRequest, Protobuf</td>
      </tr>
      <tr>
        <td style="color:var(--p5)">Prototype</td>
        <td>Clone of existing object</td>
        <td>clone() method + copy constructor + registry</td>
        <td>
          <span class="m2-solid-badge" style="background:rgba(90,122,154,0.15);color:var(--steel)">DIP</span>
        </td>
        <td>Deep copy complexity, track shallow vs deep boundaries</td>
        <td>Spring prototype beans, JS Object.create()</td>
      </tr>
    </tbody>
  </table>
  </div>

  <div style="margin-top:28px;background:var(--surface);border:1px solid var(--border);padding:24px;border-radius:4px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--gold);letter-spacing:2px;margin-bottom:16px;">// FACTORY FAMILY COMPARISON</div>
    <div class="table-responsive">
    <table class="m2-comp-table">
      <thead><tr><th>DIMENSION</th><th>SIMPLE FACTORY</th><th>FACTORY METHOD</th><th>ABSTRACT FACTORY</th></tr></thead>
      <tbody>
        <tr><td>GoF Pattern?</td><td>No (idiom)</td><td>Yes</td><td>Yes</td></tr>
        <tr><td>Creates</td><td>One product</td><td>One product</td><td>Family of products</td></tr>
        <tr><td>Mechanism</td><td>Static method</td><td>Subclass inheritance</td><td>Interface injection</td></tr>
        <tr><td>OCP compliance</td><td>Poor (modify factory)</td><td>Good (new subclass)</td><td>Good (new factory)</td></tr>
        <tr><td>Adding product type</td><td>Modify factory</td><td>New Creator subclass</td><td>Update all factories</td></tr>
        <tr><td>Use when</td><td>Simple, few types</td><td>Product type varies</td><td>Product families must be consistent</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</div>

<!-- ===== ATM PROJECT ===== -->
<div class="m2-view" id="m2-view-atm">
  <div style="margin-bottom:24px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--gold);letter-spacing:2px;margin-bottom:12px;">// MINI PROJECT — ATM SYSTEM</div>
    <p style="font-size:14px;color:var(--muted);line-height:1.7;max-width:680px;">Design a complete ATM system using all 5 Creational patterns. Each pattern is used where it naturally fits — not forced. The challenge is choosing correctly.</p>
  </div>

  <div class="m2-atm-layout">
    <div class="m2-atm-pattern">
      <div class="m2-atm-p-icon">🔁</div>
      <div class="m2-atm-p-name" style="color:var(--p1)">Singleton</div>
      <div class="m2-atm-p-use">TransactionLogger — single audit log across all ATM machines</div>
    </div>
    <div class="m2-atm-pattern">
      <div class="m2-atm-p-icon">🏭</div>
      <div class="m2-atm-p-name" style="color:var(--p2)">Factory Method</div>
      <div class="m2-atm-p-use">AccountFactory — creates Savings / Current / FixedDeposit by type</div>
    </div>
    <div class="m2-atm-pattern">
      <div class="m2-atm-p-icon">🏗️</div>
      <div class="m2-atm-p-name" style="color:var(--p3)">Abstract Factory</div>
      <div class="m2-atm-p-use">ATMFactory — Basic / Full / Premium ATM module sets</div>
    </div>
    <div class="m2-atm-pattern">
      <div class="m2-atm-p-icon">🔨</div>
      <div class="m2-atm-p-name" style="color:var(--p4)">Builder</div>
      <div class="m2-atm-p-use">Receipt.Builder — required + optional fields, immutable result</div>
    </div>
    <div class="m2-atm-pattern">
      <div class="m2-atm-p-icon">📋</div>
      <div class="m2-atm-p-name" style="color:var(--p5)">Prototype</div>
      <div class="m2-atm-p-use">CardTemplateRegistry — clone pre-built card templates per card type</div>
    </div>
  </div>

  <div style="background:var(--surface);border:1px solid var(--border);border-radius:4px;padding:20px;margin-top:20px;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin-bottom:12px;">// PROJECT STRUCTURE</div>
    <pre style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:#a89060;line-height:1.9;background:none;border:none;padding:0;margin:0;white-space:pre-wrap;">atm-system/
├── singleton/
│   └── TransactionLogger.java
├── factory/
│   ├── Account.java             <span style="color:var(--muted)">← interface</span>
│   ├── SavingsAccount.java
│   ├── CurrentAccount.java
│   ├── FixedDepositAccount.java
│   └── AccountFactory.java      <span style="color:var(--muted)">← abstract creator</span>
├── abstractfactory/
│   ├── ATMFactory.java           <span style="color:var(--muted)">← abstract factory interface</span>
│   ├── BasicATMFactory.java
│   ├── FullATMFactory.java
│   └── PremiumATMFactory.java
├── builder/
│   └── Receipt.java             <span style="color:var(--muted)">← with inner Builder class</span>
├── prototype/
│   ├── CardTemplate.java
│   └── CardTemplateRegistry.java
└── ATMController.java           <span style="color:var(--muted)">← wires all patterns together</span></pre>
  </div>

  <div style="margin-top:20px;padding:16px 20px;background:rgba(240,165,0,0.04);border:1px solid rgba(240,165,0,0.15);border-radius:4px;">
    <div style="font-size:13px;color:var(--gold);font-weight:600;margin-bottom:8px;">Evaluation Criteria</div>
    <div style="font-size:12px;color:var(--muted);line-height:1.8;">
      1. Each pattern used correctly — not forced where inappropriate<br>
      2. SOLID principles maintained throughout (no new violations introduced)<br>
      3. UML class diagram covers all 5 pattern implementations<br>
      4. ATMController can: create account, log transaction, build receipt, clone card, assemble ATM
    </div>
  </div>
</div>

<!-- ===== TASKS ===== -->
<div class="m2-view" id="m2-view-tasks">
  <div class="m2-tasks-list">
    <div class="m2-task-item">
      <div class="m2-task-hd" onclick="m2ToggleTask(this)">
        <div class="m2-t-num" style="background:rgba(240,165,0,0.1);color:var(--p1)">TASK 01</div>
        <div class="m2-t-label">Pattern Recognition — 5 Scenarios</div>
        <div class="m2-t-meta">~1.5 hrs</div>
        <div class="m2-t-arr">›</div>
      </div>
      <div class="m2-task-bd">
        <p>Identify the correct Creational pattern for each scenario. Write 2-sentence justification.</p>
        <pre>1. A game needs 1,000 enemy soldiers. Each has complex AI
   state (navigation, behaviour tree, inventory) but
   they're all nearly identical.
 
2. A reporting system builds PDFs with required fields
   (title, date, author) and 12 optional fields (logo,
   watermark, footer, page numbers, custom message...).
 
3. An OS needs to create UI elements (Button, TextBox,
   Dialog) consistently across Windows, macOS, Linux.
 
4. A payment system must write every transaction to a
   single audit file that persists for the app's lifetime.
 
5. A notification service creates the right notification
   object based on user's channel (EMAIL, SMS, PUSH, WEBHOOK).
 
Output: Pattern + 2-sentence justification for each.</pre>
      </div>
    </div>

    <div class="m2-task-item">
      <div class="m2-task-hd" onclick="m2ToggleTask(this)">
        <div class="m2-t-num" style="background:rgba(224,123,0,0.1);color:var(--p2)">TASK 02</div>
        <div class="m2-t-label">Thread-safe ConnectionPool Singleton</div>
        <div class="m2-t-meta">~2 hrs · code</div>
        <div class="m2-t-arr">›</div>
      </div>
      <div class="m2-task-bd">
        <p>Implement a thread-safe Singleton ConnectionPool that manages exactly 10 database connections.</p>
        <pre>Requirements:
- Exactly 10 connections, created lazily on first getInstance()
- getConnection(): returns an available connection
  → if all 10 in use: block (wait) OR throw? You decide — justify.
- releaseConnection(conn): returns connection to pool
- Thread-safe: multiple threads calling simultaneously
- Explain in comments why your synchronisation is correct
 
Bonus: Add a timeout to getConnection() that throws
       ConnectionTimeoutException after N milliseconds.</pre>
      </div>
    </div>

    <div class="m2-task-item">
      <div class="m2-task-hd" onclick="m2ToggleTask(this)">
        <div class="m2-t-num" style="background:rgba(106,143,106,0.1);color:var(--p4)">TASK 03</div>
        <div class="m2-t-label">HttpRequest Builder — Immutable with Validation</div>
        <div class="m2-t-meta">~2 hrs · code</div>
        <div class="m2-t-arr">›</div>
      </div>
      <div class="m2-task-bd">
        <p>Implement an immutable HttpRequest class with a Builder. All fields must be final.</p>
        <pre>Required fields:
  url    (String)      — must start with http:// or https://
  method (enum)        — GET, POST, PUT, DELETE
 
Optional fields (with defaults):
  headers        (Map&lt;String,String&gt;)  default: empty map
  body           (String)              default: null
  timeoutMs      (int)                 default: 30000
  followRedirects(boolean)             default: true
  retryCount     (int)                 default: 0
 
Validation rules (throw IllegalStateException on violation):
  - URL must start with http:// or https://
  - body only valid for POST or PUT requests
  - timeoutMs must be > 0
  - retryCount must be >= 0
 
Usage should look like:
  HttpRequest req = new HttpRequest.Builder("https://api.com/users", POST)
      .header("Authorization", "Bearer token")
      .body("{\"name\": \"Ajay\"}")
      .timeoutMs(5000)
      .build();</pre>
      </div>
    </div>

    <div class="m2-task-item">
      <div class="m2-task-hd" onclick="m2ToggleTask(this)">
        <div class="m2-t-num" style="background:rgba(90,122,154,0.1);color:var(--p5)">TASK 04</div>
        <div class="m2-t-label">Deep vs Shallow Clone — ShoppingCart Test</div>
        <div class="m2-t-meta">~1 hr · test</div>
        <div class="m2-t-arr">›</div>
      </div>
      <div class="m2-task-bd">
        <p>Demonstrate shallow clone causing shared-state bugs and deep clone fixing them.</p>
        <pre>Create:
  class CartItem { String name; int quantity; double price; }
  class ShoppingCart {
      List&lt;CartItem&gt; items;
      String userId;
      ShoppingCart shallowClone() { ... }
      ShoppingCart deepClone()   { ... }
  }
 
Test to write:
  1. Create cart1 with 2 items
  2. shallowClone() → cart2
  3. Modify cart2.items.get(0).quantity = 99
  4. Assert: cart1.items.get(0).quantity is ALSO 99 (shared state bug!)
  5. deepClone() → cart3
  6. Modify cart3.items.get(0).quantity = 99
  7. Assert: cart1.items.get(0).quantity is UNCHANGED
 
Explain in comments: why does this happen? When is
shallow clone intentional? When is it a bug?</pre>
      </div>
    </div>
  </div>
</div>

<!-- ===== CHECKLIST ===== -->
<div class="m2-view" id="m2-view-checklist">
  <div class="m2-prog-row">
    <span id="m2-prog-lbl">0 / 11 completed</span>
    <span style="color:var(--gold)">A2 → Creational Patterns</span>
  </div>
  <div class="m2-prog-track"><div class="m2-prog-fill" id="m2-prog-fill"></div></div>

  <div class="m2-chk-list">
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Can implement thread-safe Singleton (DCL + Enum) from memory</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Know why Enum Singleton beats DCL (serialisation, reflection safety)</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Can explain Factory Method vs Simple Factory vs Abstract Factory clearly</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Can implement Abstract Factory with 2 concrete factories from memory</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Can implement Builder with required fields, optional chaining, and validate on build()</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Understand deep vs shallow clone — can explain when each is intentional</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">Know which SOLID principle(s) each pattern enforces</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">✏️ Task 1: Pattern recognition — 5 scenarios identified correctly</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">✏️ Task 2: Thread-safe ConnectionPool Singleton implemented</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">✏️ Task 3: HttpRequest Builder with immutability + validation</div></div>
    <div class="m2-chk" onclick="m2Tick(this)"><div class="m2-chk-box"></div><div class="m2-chk-lbl">✏️ Tasks 4 + Project: Deep/shallow clone test + ATM System (all 5 patterns)</div></div>
  </div>

  <div style="margin-top:28px;padding:20px 24px;background:var(--surface);border:1px solid var(--border);border-radius:4px;border-top:2px solid var(--p3);">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);letter-spacing:2px;margin-bottom:8px;">NEXT MODULE</div>
    <div style="font-family:'Barlow Condensed',sans-serif;font-size:22px;font-weight:700;color:var(--bright);margin-bottom:6px;">A3 — Structural Design Patterns</div>
    <div style="font-size:13px;color:var(--muted);line-height:1.6;">Adapter, Decorator, Proxy, Composite, Facade, Bridge, Flyweight — mapped to Vending Machine, Pizza Billing, Car Rental, File System, Splitwise, CricBuzz, TrueCaller. Mini Project: Splitwise + Simplify Algorithm.</div>
  </div>
</div>

</div><!-- end content -->

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--border);padding-top:20px;">
  <a href="/learning/system-design/lld/module-a1-solid/" style="padding:12px 24px;border:1px solid var(--border);border-radius:4px;color:var(--muted);text-decoration:none;">← LLD A1: SOLID + OOP + UML</a>
  <a href="/learning/system-design/lld/module-a2-notes/" style="padding:12px 24px;border:1px solid var(--gold);color:var(--gold);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid var(--border);border-radius:4px;color:var(--muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a3-structural/" style="padding:12px 24px;background:var(--gold);color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: LLD A3 →</a>
</div>


<script src="/assets/js/sd-module-a2.js" defer></script>