---
layout: default
title: "Module A5 — Concurrency in LLD | LLD Track"
custom_css: sd-module-a5
custom_js: sd-module-a5
permalink: /learning/system-design/lld/module-a5-concurrency/
---
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<header>
  <div class="hdr-top">
    <div class="hdr-left">
      <div class="signal-badge"><div class="sig-dot"></div>TRACK A · LLD · MODULE A5 · WEEK 8 · LIVE</div>
      <h1>Concurrency<br><span>in LLD</span></h1>
      <div class="hdr-sub">
        Threads · Locks · Semaphores · Producer-Consumer<br>
        Rate Limiter · Deadlock · Thread Pool · Pub/Sub Queue
      </div>
    </div>
    <div class="stats-panel">
      <div class="stat-box">
        <div class="stat-val" style="color:var(--cyan)">9</div>
        <div class="stat-lbl">TOPICS</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" style="color:var(--green)">2</div>
        <div class="stat-lbl">PROJECTS</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" style="color:var(--amber)">4</div>
        <div class="stat-lbl">TASKS</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" style="color:var(--purple)">A5</div>
        <div class="stat-lbl">MODULE</div>
      </div>
    </div>
  </div>
  <div class="cbar">
    <div class="cbar-seg" style="background:var(--cyan)"></div>
    <div class="cbar-seg" style="background:var(--green)"></div>
    <div class="cbar-seg" style="background:var(--amber)"></div>
    <div class="cbar-seg" style="background:var(--red)"></div>
    <div class="cbar-seg" style="background:var(--purple)"></div>
    <div class="cbar-seg" style="background:var(--teal)"></div>
    <div class="cbar-seg" style="background:var(--orange)"></div>
  </div>
</header>

<nav class="nav">
  <div class="nav-tab active" onclick="show('jmm',this)">JMM</div>
  <div class="nav-tab" onclick="show('primitives',this)">Primitives</div>
  <div class="nav-tab" onclick="show('patterns',this)">Patterns</div>
  <div class="nav-tab" onclick="show('deadlock',this)">Deadlock</div>
  <div class="nav-tab" onclick="show('ratelimiter',this)">Rate Limiter</div>
  <div class="nav-tab" onclick="show('projects',this)">Projects</div>
  <div class="nav-tab" onclick="show('tasks',this)">Tasks</div>
  <div class="nav-tab" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- ===== JMM ===== -->
<div class="view active" id="view-jmm">
  <div class="sec-hd">Java Memory Model — why threads see stale data</div>

  <div class="thread-demo">
    <div style="font-family:'Share Tech Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:14px;">// THREAD EXECUTION — RACE CONDITION VISUALISED</div>
    <div class="thread-row">
      <div class="thread-lbl">THREAD-1</div>
      <div class="thread-track"><div class="thread-bar t1-bar">GETFIELD → IADD → PUTFIELD</div></div>
      <div class="thread-val" id="tv1">count?</div>
    </div>
    <div class="thread-row">
      <div class="thread-lbl">THREAD-2</div>
      <div class="thread-track"><div class="thread-bar t2-bar">GETFIELD → IADD → PUTFIELD</div></div>
      <div class="thread-val" id="tv2">count?</div>
    </div>
    <div class="thread-row">
      <div class="thread-lbl">THREAD-3</div>
      <div class="thread-track"><div class="thread-bar t3-bar">GETFIELD → IADD → PUTFIELD</div></div>
      <div class="thread-val" id="tv3">count?</div>
    </div>
    <div style="margin-top:12px;font-family:'Share Tech Mono',monospace;font-size:10px;color:var(--amber);">⚠ count++ is 3 bytecode ops — threads interleave, updates get lost</div>
  </div>

  <div class="concept-grid">
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--red)"></div>
      <div class="cc-num">PROBLEM 01</div>
      <div class="cc-name">Visibility</div>
      <div class="cc-desc">Thread writes to local CPU cache. Other threads see stale value from main memory. JMM does NOT guarantee when (or if) cache is flushed without synchronization.</div>
    </div>
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--amber)"></div>
      <div class="cc-num">PROBLEM 02</div>
      <div class="cc-name">Atomicity</div>
      <div class="cc-desc"><code style="color:var(--cyan);font-family:'Share Tech Mono',monospace">count++</code> is 3 bytecode instructions: read → modify → write. Threads can interleave between any two, causing lost updates.</div>
    </div>
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--cyan)"></div>
      <div class="cc-num">GUARANTEE</div>
      <div class="cc-name">Happens-Before</div>
      <div class="cc-desc">JMM guarantee: if A happens-before B, B sees all of A's memory writes. Established by: synchronized exit/enter, volatile write/read, thread start/join, lock release/acquire.</div>
    </div>
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--green)"></div>
      <div class="cc-num">FIX 01</div>
      <div class="cc-name">volatile</div>
      <div class="cc-desc">Ensures visibility only. Writes immediately flushed to main memory; reads always from main memory. Does NOT fix atomicity — <code style="color:var(--cyan);font-family:'Share Tech Mono',monospace">count++</code> still broken with volatile.</div>
    </div>
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--purple)"></div>
      <div class="cc-num">FIX 02</div>
      <div class="cc-name">synchronized</div>
      <div class="cc-desc">Ensures both visibility AND atomicity. Only one thread executes synchronized block at a time. Establishes happens-before on exit/enter. Correct but heavier than atomic ops.</div>
    </div>
    <div class="concept-card">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--teal)"></div>
      <div class="cc-num">FIX 03</div>
      <div class="cc-name">AtomicInteger</div>
      <div class="cc-desc">Lock-free via CAS (Compare-And-Swap). Hardware instruction: atomic read-modify-write. Best for single counters/references under moderate contention. No blocking.</div>
    </div>
  </div>

  <div class="code-block">
    <div class="code-hdr">volatile vs synchronized vs Atomic<span class="clang">JAVA</span></div>
<pre class="code"><span class="cm">// ❌ BROKEN — race condition on count++</span>
<span class="kw">class</span> <span class="cls">BrokenCounter</span>   { <span class="kw">private int</span> count = <span class="num">0</span>; <span class="kw">void</span> <span class="fn">inc</span>() { count++; } }

<span class="cm">// ❌ STILL BROKEN — volatile fixes visibility, not atomicity</span>
<span class="kw">class</span> <span class="cls">VolatileCounter</span>  { <span class="kw">private volatile int</span> count = <span class="num">0</span>; <span class="kw">void</span> <span class="fn">inc</span>() { count++; } }

<span class="cm">// ✅ FIXED — synchronized ensures atomicity + visibility</span>
<span class="kw">class</span> <span class="cls">SyncCounter</span>      { <span class="kw">private int</span> count = <span class="num">0</span>; <span class="kw">synchronized void</span> <span class="fn">inc</span>() { count++; } }

<span class="cm">// ✅ FIXED — lock-free CAS, better than synchronized for single counter</span>
<span class="kw">class</span> <span class="cls">AtomicCounter</span>    { <span class="kw">private final</span> <span class="cls">AtomicInteger</span> count = <span class="kw">new</span> <span class="cls">AtomicInteger</span>(<span class="num">0</span>);
                           <span class="kw">void</span> <span class="fn">inc</span>() { count.<span class="fn">incrementAndGet</span>(); } }

<span class="cm">// volatile IS correct for simple flags (single writer, no compound op)</span>
<span class="kw">class</span> <span class="cls">Service</span> {
    <span class="kw">private volatile boolean</span> running = <span class="kw">true</span>;   <span class="cm">// ✅ correct: simple write/read</span>
    <span class="kw">public void</span> <span class="fn">stop</span>()  { running = <span class="kw">false</span>; }     <span class="cm">// single writer</span>
    <span class="kw">public void</span> <span class="fn">run</span>()   { <span class="kw">while</span> (running) <span class="fn">work</span>(); } <span class="cm">// multi-reader</span>
}</pre>
  </div>

  <div class="alert warn">⚠ <em>Common interview trap:</em> "Is volatile enough for a counter?" — No. volatile fixes visibility but count++ still has the read-modify-write race. Use AtomicInteger or synchronized.</div>
</div>

<!-- ===== PRIMITIVES ===== -->
<div class="view" id="view-primitives">
  <div class="sec-hd">Synchronization Primitives</div>

  <table class="prim-table">
    <thead><tr><th>PRIMITIVE</th><th>ATOMICITY</th><th>VISIBILITY</th><th>TRY-LOCK</th><th>TIMEOUT</th><th>FAIRNESS</th><th>BEST FOR</th></tr></thead>
    <tbody>
      <tr><td>synchronized</td><td class="yes">✓</td><td class="yes">✓</td><td class="no">✗</td><td class="no">✗</td><td class="no">✗</td><td style="color:var(--text)">Simple mutual exclusion</td></tr>
      <tr><td>ReentrantLock</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td style="color:var(--text)">Complex locking needs</td></tr>
      <tr><td>volatile</td><td class="no">✗</td><td class="yes">✓</td><td class="no">N/A</td><td class="no">N/A</td><td class="no">N/A</td><td style="color:var(--text)">Simple flags, single writer</td></tr>
      <tr><td>AtomicInteger</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">CAS</td><td class="no">✗</td><td class="no">✗</td><td style="color:var(--text)">Lock-free single counter</td></tr>
      <tr><td>Semaphore</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td style="color:var(--text)">Limiting concurrent access (N&gt;1)</td></tr>
      <tr><td>ReadWriteLock</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td><td style="color:var(--text)">Read-heavy access patterns</td></tr>
      <tr><td>LongAdder</td><td class="yes">✓</td><td class="yes">✓</td><td class="no">N/A</td><td class="no">N/A</td><td class="no">N/A</td><td style="color:var(--text)">High-contention counter (striped)</td></tr>
    </tbody>
  </table>

  <div class="code-block">
    <div class="code-hdr">ReentrantLock — full API<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">BankAccount</span> {
    <span class="kw">private double</span>              balance = <span class="num">0</span>;
    <span class="kw">private final</span> <span class="cls">ReentrantLock</span> lock = <span class="kw">new</span> <span class="cls">ReentrantLock</span>(<span class="kw">true</span>); <span class="cm">// fair=true</span>

    <span class="cm">// Basic lock — ALWAYS unlock in finally</span>
    <span class="kw">public void</span> <span class="fn">deposit</span>(<span class="kw">double</span> amount) {
        lock.<span class="fn">lock</span>();
        <span class="kw">try</span>     { balance += amount; }
        <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }  <span class="cm">// ← never skip this</span>
    }

    <span class="cm">// tryLock — non-blocking, returns false if unavailable</span>
    <span class="kw">public boolean</span> <span class="fn">tryDeposit</span>(<span class="kw">double</span> amount) {
        <span class="kw">if</span> (lock.<span class="fn">tryLock</span>()) {
            <span class="kw">try</span>     { balance += amount; <span class="kw">return true</span>; }
            <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
        }
        <span class="kw">return false</span>;
    }

    <span class="cm">// tryLock with timeout — blocks at most N ms</span>
    <span class="kw">public boolean</span> <span class="fn">tryDepositTimeout</span>(<span class="kw">double</span> amount, <span class="kw">long</span> ms)
            <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        <span class="kw">if</span> (lock.<span class="fn">tryLock</span>(ms, <span class="cls">TimeUnit</span>.MILLISECONDS)) {
            <span class="kw">try</span>     { balance += amount; <span class="kw">return true</span>; }
            <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
        }
        <span class="kw">return false</span>;  <span class="cm">// Timeout — didn't acquire</span>
    }
}
</pre>
  </div>

  <div class="code-block">
    <div class="code-hdr">ReadWriteLock — concurrent reads, exclusive writes<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">ConfigCache</span> {
    <span class="kw">private final</span> <span class="cls">Map</span>&lt;<span class="cls">String</span>,<span class="cls">String</span>&gt; cache  = <span class="kw">new</span> <span class="cls">HashMap</span>&lt;&gt;();
    <span class="kw">private final</span> <span class="cls">ReadWriteLock</span>        rwLock = <span class="kw">new</span> <span class="cls">ReentrantReadWriteLock</span>();
    <span class="kw">private final</span> <span class="cls">Lock</span>                 rLock  = rwLock.<span class="fn">readLock</span>();
    <span class="kw">private final</span> <span class="cls">Lock</span>                 wLock  = rwLock.<span class="fn">writeLock</span>();

    <span class="cm">// ✅ MANY threads can read simultaneously</span>
    <span class="kw">public</span> <span class="cls">String</span> <span class="fn">get</span>(<span class="cls">String</span> key) {
        rLock.<span class="fn">lock</span>();
        <span class="kw">try</span>     { <span class="kw">return</span> cache.<span class="fn">get</span>(key); }
        <span class="kw">finally</span> { rLock.<span class="fn">unlock</span>(); }
    }

    <span class="cm">// ✅ EXCLUSIVE — blocks all readers + other writers</span>
    <span class="kw">public void</span> <span class="fn">put</span>(<span class="cls">String</span> key, <span class="cls">String</span> val) {
        wLock.<span class="fn">lock</span>();
        <span class="kw">try</span>     { cache.<span class="fn">put</span>(key, val); }
        <span class="kw">finally</span> { wLock.<span class="fn">unlock</span>(); }
    }

    <span class="cm">// Double-checked pattern — read fast path, write fallback</span>
    <span class="kw">public</span> <span class="cls">String</span> <span class="fn">computeIfAbsent</span>(<span class="cls">String</span> key, <span class="cls">Function</span>&lt;<span class="cls">String</span>,<span class="cls">String</span>&gt; fn) {
        rLock.<span class="fn">lock</span>();                             <span class="cm">// 1. Try read (fast path)</span>
        <span class="kw">try</span> { <span class="kw">if</span> (cache.<span class="fn">get</span>(key) != <span class="kw">null</span>) <span class="kw">return</span> cache.<span class="fn">get</span>(key); }
        <span class="kw">finally</span> { rLock.<span class="fn">unlock</span>(); }
        wLock.<span class="fn">lock</span>();                             <span class="cm">// 2. Write lock</span>
        <span class="kw">try</span> {
            <span class="kw">if</span> (cache.<span class="fn">get</span>(key) != <span class="kw">null</span>) <span class="kw">return</span> cache.<span class="fn">get</span>(key); <span class="cm">// 3. Double-check</span>
            <span class="cls">String</span> v = fn.<span class="fn">apply</span>(key);
            cache.<span class="fn">put</span>(key, v); <span class="kw">return</span> v;
        } <span class="kw">finally</span> { wLock.<span class="fn">unlock</span>(); }
    }
}</pre>
  </div>

  <div class="alert info">ℹ <em>ReadWriteLock rule:</em> Lock downgrade (write→read) is allowed in Java. Lock upgrade (read→write) is NOT — it deadlocks. Always release read lock before acquiring write lock.</div>
</div>

<!-- ===== PATTERNS ===== -->
<div class="view" id="view-patterns">
  <div class="sec-hd">Concurrency Patterns</div>

  <div class="sec-hd" style="margin-top:0">Producer-Consumer — BlockingQueue</div>
  <div class="code-block">
    <div class="code-hdr">LogPipeline.java — classic producer-consumer<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">LogPipeline</span> {
    <span class="cm">// LinkedBlockingQueue: bounded, separate head/tail locks — high throughput</span>
    <span class="kw">private final</span> <span class="cls">BlockingQueue</span>&lt;<span class="cls">LogEvent</span>&gt; queue =
        <span class="kw">new</span> <span class="cls">LinkedBlockingQueue</span>&lt;&gt;(<span class="num">1000</span>); <span class="cm">// Bounded — backpressure!</span>
    <span class="kw">private volatile boolean</span> running = <span class="kw">true</span>;

    <span class="cm">// PRODUCER — any app thread calls this</span>
    <span class="kw">public void</span> <span class="fn">log</span>(<span class="cls">String</span> level, <span class="cls">String</span> msg) {
        <span class="kw">try</span> {
            queue.<span class="fn">put</span>(<span class="kw">new</span> <span class="cls">LogEvent</span>(level, msg)); <span class="cm">// Blocks if queue full (backpressure)</span>
        } <span class="kw">catch</span> (<span class="cls">InterruptedException</span> e) { <span class="cls">Thread</span>.currentThread().<span class="fn">interrupt</span>(); }
    }

    <span class="kw">public boolean</span> <span class="fn">tryLog</span>(<span class="cls">String</span> level, <span class="cls">String</span> msg) {
        <span class="kw">return</span> queue.<span class="fn">offer</span>(<span class="kw">new</span> <span class="cls">LogEvent</span>(level, msg)); <span class="cm">// Non-blocking, drops if full</span>
    }

    <span class="cm">// CONSUMER — background thread drains queue</span>
    <span class="kw">private void</span> <span class="fn">consume</span>() {
        <span class="kw">while</span> (running || !queue.<span class="fn">isEmpty</span>()) {
            <span class="kw">try</span> {
                <span class="cls">LogEvent</span> e = queue.<span class="fn">poll</span>(<span class="num">100</span>, <span class="cls">TimeUnit</span>.MILLISECONDS); <span class="cm">// timeout: re-check 'running'</span>
                <span class="kw">if</span> (e != <span class="kw">null</span>) <span class="fn">writeToSink</span>(e);
            } <span class="kw">catch</span> (<span class="cls">InterruptedException</span> e) { <span class="cls">Thread</span>.currentThread().<span class="fn">interrupt</span>(); <span class="kw">break</span>; }
        }
    }
}</pre>
  </div>

  <div class="sec-hd" style="margin-top:24px">Condition Variables — await() ALWAYS in while</div>
  <div class="code-block">
    <div class="code-hdr">BoundedBuffer.java — two conditions<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">BoundedBuffer</span>&lt;T&gt; {
    <span class="kw">private final</span> <span class="cls">Object</span>[]      buf;
    <span class="kw">private int</span>                  count=<span class="num">0</span>, put=<span class="num">0</span>, take=<span class="num">0</span>;
    <span class="kw">private final</span> <span class="cls">ReentrantLock</span> lock     = <span class="kw">new</span> <span class="cls">ReentrantLock</span>();
    <span class="kw">private final</span> <span class="cls">Condition</span>     notFull  = lock.<span class="fn">newCondition</span>();
    <span class="kw">private final</span> <span class="cls">Condition</span>     notEmpty = lock.<span class="fn">newCondition</span>();

    <span class="kw">public void</span> <span class="fn">put</span>(T item) <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        lock.<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="kw">while</span> (count == buf.length) notFull.<span class="fn">await</span>();  <span class="cm">// ← WHILE not IF! (spurious wakeups)</span>
            buf[put] = item; put = (put+<span class="num">1</span>)%buf.length; count++;
            notEmpty.<span class="fn">signal</span>();  <span class="cm">// Wake one consumer</span>
        } <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
    }

    <span class="kw">public</span> T <span class="fn">take</span>() <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        lock.<span class="fn">lock</span>();
        <span class="kw">try</span> {
            <span class="kw">while</span> (count == <span class="num">0</span>) notEmpty.<span class="fn">await</span>();         <span class="cm">// ← WHILE not IF!</span>
            T item = (T) buf[take]; buf[take]=<span class="kw">null</span>; take=(take+<span class="num">1</span>)%buf.length; count--;
            notFull.<span class="fn">signal</span>();   <span class="cm">// Wake one producer</span>
            <span class="kw">return</span> item;
        } <span class="kw">finally</span> { lock.<span class="fn">unlock</span>(); }
    }
}</pre>
  </div>
  <div class="alert warn">⚠ <em>Spurious wakeups:</em> The JVM can wake a thread from await() without signal() — allowed by spec. ALWAYS re-check the guard condition in a while loop after await(). This is one of the most common concurrency bugs.</div>

  <div class="sec-hd" style="margin-top:24px">Semaphore — bounded resource pool</div>
  <div class="code-block">
    <div class="code-hdr">DBConnectionPool.java<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">DBConnectionPool</span> {
    <span class="kw">private final</span> <span class="cls">Semaphore</span>         sem;
    <span class="kw">private final</span> <span class="cls">Queue</span>&lt;<span class="cls">Connection</span>&gt;  pool = <span class="kw">new</span> <span class="cls">ConcurrentLinkedQueue</span>&lt;&gt;();

    <span class="kw">public</span> <span class="cls">DBConnectionPool</span>(<span class="kw">int</span> max) {
        sem = <span class="kw">new</span> <span class="cls">Semaphore</span>(max, <span class="kw">true</span>);  <span class="cm">// fair=true: FIFO, no starvation</span>
        <span class="kw">for</span> (<span class="kw">int</span> i=<span class="num">0</span>; i&lt;max; i++) pool.<span class="fn">offer</span>(<span class="fn">createConnection</span>());
    }

    <span class="kw">public</span> <span class="cls">Connection</span> <span class="fn">acquire</span>() <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        sem.<span class="fn">acquire</span>();         <span class="cm">// Blocks until a slot is free</span>
        <span class="kw">return</span> pool.<span class="fn">poll</span>();
    }

    <span class="kw">public</span> <span class="cls">Connection</span> <span class="fn">acquire</span>(<span class="kw">long</span> ms) <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        <span class="kw">if</span> (!sem.<span class="fn">tryAcquire</span>(ms, <span class="cls">TimeUnit</span>.MILLISECONDS))
            <span class="kw">throw new</span> <span class="cls">TimeoutException</span>(<span class="str">"No connection in "</span>+ms+<span class="str">"ms"</span>);
        <span class="kw">return</span> pool.<span class="fn">poll</span>();
    }

    <span class="kw">public void</span> <span class="fn">release</span>(<span class="cls">Connection</span> c) {
        pool.<span class="fn">offer</span>(c);
        sem.<span class="fn">release</span>();         <span class="cm">// Signal one slot free → unblocks next waiter</span>
    }
}</pre>
  </div>
</div>

<!-- ===== DEADLOCK ===== -->
<div class="view" id="view-deadlock">
  <div class="sec-hd">Deadlock — Detection, Prevention, Avoidance</div>

  <div class="alert error">⛔ <em>Deadlock:</em> Thread A holds Lock-1 waiting for Lock-2. Thread B holds Lock-2 waiting for Lock-1. Neither can proceed. Program hangs forever.</div>

  <div class="dl-grid">
    <div class="dl-card">
      <div class="dl-hdr" style="background:rgba(255,64,96,0.1);color:var(--red)">❌ BROKEN — circular wait</div>
      <div class="dl-body">
        <div class="code-block" style="margin:0">
<pre class="code"><span class="cm">// Thread-1: lock(from) then lock(to)</span>
<span class="cm">// Thread-2: lock(to)   then lock(from)</span>
<span class="cm">// → DEADLOCK when called concurrently</span>
<span class="kw">void</span> <span class="fn">transfer</span>(<span class="cls">Account</span> from, <span class="cls">Account</span> to, <span class="kw">double</span> amt) {
    <span class="kw">synchronized</span> (from) {
        <span class="kw">synchronized</span> (to) {   <span class="cm">// ← order varies!</span>
            from.<span class="fn">debit</span>(amt);
            to.<span class="fn">credit</span>(amt);
        }
    }
}</pre>
        </div>
      </div>
    </div>
    <div class="dl-card">
      <div class="dl-hdr" style="background:rgba(0,255,136,0.08);color:var(--green)">✅ FIX 1 — consistent lock ordering</div>
      <div class="dl-body">
        <div class="code-block" style="margin:0">
<pre class="code"><span class="cm">// Always lock lower account ID first</span>
<span class="kw">void</span> <span class="fn">transfer</span>(<span class="cls">Account</span> from, <span class="cls">Account</span> to, <span class="kw">double</span> amt) {
    <span class="cls">Account</span> first  = from.id &lt; to.id ? from : to;
    <span class="cls">Account</span> second = from.id &lt; to.id ? to   : from;
    <span class="kw">synchronized</span> (first) {
        <span class="kw">synchronized</span> (second) { <span class="cm">// ← same order always</span>
            from.<span class="fn">debit</span>(amt);
            to.<span class="fn">credit</span>(amt);
        }
    }
}</pre>
        </div>
      </div>
    </div>
    <div class="dl-card">
      <div class="dl-hdr" style="background:rgba(0,255,136,0.08);color:var(--green)">✅ FIX 2 — tryLock with backoff</div>
      <div class="dl-body">
        <div class="code-block" style="margin:0">
<pre class="code"><span class="kw">void</span> <span class="fn">transfer</span>(<span class="cls">Account</span> f, <span class="cls">Account</span> t, <span class="kw">double</span> amt) <span class="kw">throws</span> <span class="cls">Exception</span> {
    <span class="kw">while</span> (<span class="kw">true</span>) {
        <span class="kw">if</span> (f.lock.<span class="fn">tryLock</span>(<span class="num">50</span>, <span class="cls">TimeUnit</span>.MILLISECONDS)) {
            <span class="kw">try</span> {
                <span class="kw">if</span> (t.lock.<span class="fn">tryLock</span>(<span class="num">50</span>, <span class="cls">TimeUnit</span>.MILLISECONDS)) {
                    <span class="kw">try</span> { f.<span class="fn">debit</span>(amt); t.<span class="fn">credit</span>(amt); <span class="kw">return</span>; }
                    <span class="kw">finally</span> { t.lock.<span class="fn">unlock</span>(); }
                }
            } <span class="kw">finally</span> { f.lock.<span class="fn">unlock</span>(); }
        }
        <span class="cls">Thread</span>.<span class="fn">sleep</span>((<span class="kw">long</span>)(<span class="cls">Math</span>.<span class="fn">random</span>()*<span class="num">10</span>)); <span class="cm">// random backoff</span>
    }
}</pre>
        </div>
      </div>
    </div>
    <div class="dl-card">
      <div class="dl-hdr" style="background:rgba(0,180,255,0.08);color:var(--cyan)">🔑 Coffman Conditions</div>
      <div class="dl-body" style="font-family:'Share Tech Mono',monospace;font-size:11px;line-height:2;color:var(--text)">
        ALL four must hold for deadlock:<br>
        <span style="color:var(--amber)">1. Mutual Exclusion</span> — resource held exclusively<br>
        <span style="color:var(--amber)">2. Hold &amp; Wait</span> — holds one, waits for another<br>
        <span style="color:var(--amber)">3. No Preemption</span> — resource can't be taken away<br>
        <span style="color:var(--amber)">4. Circular Wait</span> — A→B→C→A dependency cycle<br><br>
        <span style="color:var(--green)">Break ANY ONE to prevent deadlock:</span><br>
        → Ordering breaks Circular Wait<br>
        → tryLock breaks Hold &amp; Wait + No Preemption
      </div>
    </div>
  </div>
</div>

<!-- ===== RATE LIMITER ===== -->
<div class="view" id="view-ratelimiter">
  <div class="sec-hd">Rate Limiter — Token Bucket Algorithm</div>

  <div class="flow-row">
    <div class="flow-box" style="border-color:var(--cyan);color:var(--cyan)">Bucket<br><div class="flow-label">capacity N tokens</div></div>
    <div class="flow-arrow">←</div>
    <div class="flow-box" style="border-color:var(--green);color:var(--green)">Refill<br><div class="flow-label">+rate/ms tokens</div></div>
    <div class="flow-arrow" style="margin-left:30px">Request →</div>
    <div class="flow-box" style="border-color:var(--amber);color:var(--amber)">Check<br><div class="flow-label">tokens ≥ 1?</div></div>
    <div class="flow-arrow">→ YES →</div>
    <div class="flow-box" style="border-color:var(--green);color:var(--green)">Allow<br><div class="flow-label">tokens--</div></div>
    <div class="flow-arrow">→ NO →</div>
    <div class="flow-box" style="border-color:var(--red);color:var(--red)">Reject<br><div class="flow-label">429 / wait</div></div>
  </div>

  <div class="code-block">
    <div class="code-hdr">TokenBucketRateLimiter.java<span class="clang">JAVA</span></div>
<pre class="code"><span class="kw">class</span> <span class="cls">TokenBucketRateLimiter</span> {
    <span class="kw">private final long</span>   capacity;
    <span class="kw">private final double</span> refillRatePerMs;
    <span class="kw">private double</span>       tokens;
    <span class="kw">private long</span>         lastRefill;

    <span class="kw">public</span> <span class="cls">TokenBucketRateLimiter</span>(<span class="kw">long</span> capacity, <span class="kw">long</span> rps) {
        <span class="kw">this</span>.capacity        = capacity;
        <span class="kw">this</span>.refillRatePerMs = rps / <span class="num">1000.0</span>;
        <span class="kw">this</span>.tokens          = capacity;   <span class="cm">// Start full</span>
        <span class="kw">this</span>.lastRefill      = <span class="cls">System</span>.<span class="fn">currentTimeMillis</span>();
    }

    <span class="kw">private void</span> <span class="fn">refill</span>() {
        <span class="kw">long</span> now = <span class="cls">System</span>.<span class="fn">currentTimeMillis</span>();
        tokens = <span class="cls">Math</span>.<span class="fn">min</span>(capacity, tokens + (now - lastRefill) * refillRatePerMs);
        lastRefill = now;
    }

    <span class="cm">// Non-blocking — returns false if rate exceeded</span>
    <span class="kw">public synchronized boolean</span> <span class="fn">tryAcquire</span>() {
        <span class="fn">refill</span>();
        <span class="kw">if</span> (tokens &gt;= <span class="num">1</span>) { tokens--; <span class="kw">return true</span>; }
        <span class="kw">return false</span>;
    }

    <span class="cm">// Blocking — waits until token available</span>
    <span class="kw">public synchronized void</span> <span class="fn">acquire</span>() <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        <span class="kw">while</span> (<span class="kw">true</span>) {
            <span class="fn">refill</span>();
            <span class="kw">if</span> (tokens &gt;= <span class="num">1</span>) { tokens--; <span class="kw">return</span>; }
            <span class="kw">long</span> waitMs = (<span class="kw">long</span>) <span class="cls">Math</span>.<span class="fn">ceil</span>((<span class="num">1</span>-tokens)/refillRatePerMs);
            <span class="fn">wait</span>(waitMs);
        }
    }
}

<span class="cm">// Per-user limiter — each user gets own bucket</span>
<span class="kw">class</span> <span class="cls">UserRateLimiter</span> {
    <span class="kw">private final</span> <span class="cls">ConcurrentHashMap</span>&lt;<span class="cls">String</span>, <span class="cls">TokenBucketRateLimiter</span>&gt; buckets
        = <span class="kw">new</span> <span class="cls">ConcurrentHashMap</span>&lt;&gt;();
    <span class="kw">private final</span> <span class="cls">Map</span>&lt;<span class="cls">Tier</span>,<span class="cls">Long</span>&gt; limits = <span class="cls">Map</span>.of(
        <span class="cls">Tier</span>.FREE,<span class="num">10L</span>, <span class="cls">Tier</span>.PRO,<span class="num">100L</span>, <span class="cls">Tier</span>.ENTERPRISE,<span class="num">1000L</span>);

    <span class="kw">public boolean</span> <span class="fn">tryAcquire</span>(<span class="cls">String</span> userId, <span class="cls">Tier</span> tier) {
        <span class="kw">return</span> buckets.<span class="fn">computeIfAbsent</span>(userId,
            k -> <span class="kw">new</span> <span class="cls">TokenBucketRateLimiter</span>(limits.get(tier)*<span class="num">10</span>, limits.get(tier))
        ).<span class="fn">tryAcquire</span>();
    }
}</pre>
  </div>

  <table class="prim-table">
    <thead><tr><th>ALGORITHM</th><th>BURST ALLOWED</th><th>RATE SMOOTHING</th><th>BEST FOR</th></tr></thead>
    <tbody>
      <tr><td>Token Bucket</td><td class="yes">✓ (saved tokens)</td><td class="no">Partial</td><td style="color:var(--text)">APIs, HTTP rate limiting — most common</td></tr>
      <tr><td>Leaky Bucket</td><td class="no">✗ (constant drain)</td><td class="yes">✓ Strict</td><td style="color:var(--text)">Network traffic shaping</td></tr>
      <tr><td>Sliding Window</td><td class="no">✗</td><td class="yes">✓ Accurate</td><td style="color:var(--text)">Per-user quotas, billing accuracy</td></tr>
      <tr><td>Fixed Window</td><td class="yes">✓ at window start</td><td class="no">✗ Bursty edges</td><td style="color:var(--text)">Simple quotas (daily/hourly limits)</td></tr>
    </tbody>
  </table>
</div>

<!-- ===== PROJECTS ===== -->
<div class="view" id="view-projects">
  <div class="sec-hd">Production LLD Projects</div>

  <div class="proj-grid">
    <div class="proj-card">
      <div class="proj-hdr" style="border-left:3px solid var(--cyan)">
        <div class="proj-icon">🚗</div>
        <div>
          <div class="proj-name">Thread-Safe Parking Lot</div>
          <div class="proj-type">PROJECT 1 · PARKING · CONCURRENCY</div>
        </div>
      </div>
      <div class="proj-body">
        <div style="font-size:12px;color:var(--muted);line-height:1.7;margin-bottom:12px;">
          50 concurrent threads, 3 vehicle types, zero double-bookings. Combines Semaphore + AtomicBoolean CAS + ReadWriteLock for the display board + Token Bucket for entry rate limiting.
        </div>
        <div class="tech-stack">
          <span class="tech-tag" style="border-color:var(--cyan);color:var(--cyan)">Semaphore</span>
          <span class="tech-tag" style="border-color:var(--green);color:var(--green)">AtomicBoolean.CAS</span>
          <span class="tech-tag" style="border-color:var(--purple);color:var(--purple)">ReadWriteLock</span>
          <span class="tech-tag" style="border-color:var(--amber);color:var(--amber)">TokenBucket</span>
          <span class="tech-tag" style="border-color:var(--teal);color:var(--teal)">ConcurrentHashMap</span>
        </div>
        <div class="code-block" style="margin-top:14px">
          <div class="code-hdr">Key concurrency design<span class="clang">JAVA</span></div>
<pre class="code"><span class="cm">// 1. Semaphore limits concurrent parkers per type</span>
sem.<span class="fn">acquire</span>();  <span class="cm">// blocks if no spots</span>

<span class="cm">// 2. CAS claims specific spot — no explicit lock</span>
<span class="kw">if</span> (spot.occupied.<span class="fn">compareAndSet</span>(<span class="kw">false</span>, <span class="kw">true</span>)) { ...claim... }

<span class="cm">// 3. ReadWriteLock on display board</span>
<span class="cm">//    many readers, write only on park/unpark</span>

<span class="cm">// 4. AtomicInteger for available count — no lock</span>
availableCar.<span class="fn">decrementAndGet</span>();

<span class="cm">// 5. TokenBucket at entry gate — 5 entries/sec</span>
<span class="kw">if</span> (!entryLimiter.<span class="fn">tryAcquire</span>()) <span class="kw">throw</span> rateLimitEx;</pre>
        </div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-hdr" style="border-left:3px solid var(--green)">
        <div class="proj-icon">📨</div>
        <div>
          <div class="proj-name">Pub/Sub Message Queue</div>
          <div class="proj-type">PROJECT 2 · MESSAGING · ASYNC</div>
        </div>
      </div>
      <div class="proj-body">
        <div style="font-size:12px;color:var(--muted);line-height:1.7;margin-bottom:12px;">
          Thread-safe publish/subscribe with async fan-out dispatch. Producers don't block consumers. One failing handler doesn't affect others. Uses CopyOnWriteArrayList for safe iteration during subscribe/unsubscribe.
        </div>
        <div class="tech-stack">
          <span class="tech-tag" style="border-color:var(--cyan);color:var(--cyan)">LinkedBlockingQueue</span>
          <span class="tech-tag" style="border-color:var(--green);color:var(--green)">CopyOnWriteArrayList</span>
          <span class="tech-tag" style="border-color:var(--purple);color:var(--purple)">ExecutorService</span>
          <span class="tech-tag" style="border-color:var(--amber);color:var(--amber)">ConcurrentHashMap</span>
          <span class="tech-tag" style="border-color:var(--teal);color:var(--teal)">volatile</span>
        </div>
        <div class="code-block" style="margin-top:14px">
          <div class="code-hdr">Key concurrency design<span class="clang">JAVA</span></div>
<pre class="code"><span class="cm">// 1. Producer: non-blocking publish</span>
queue.<span class="fn">offer</span>(msg);  <span class="cm">// false if full — backpressure</span>

<span class="cm">// 2. CopyOnWriteArrayList: safe to iterate</span>
<span class="cm">//    while other threads subscribe/unsubscribe</span>
subscribers.<span class="fn">computeIfAbsent</span>(topic,
    k -> <span class="kw">new</span> <span class="cls">CopyOnWriteArrayList</span>&lt;&gt;()).<span class="fn">add</span>(h);

<span class="cm">// 3. Dispatcher fans out to thread pool</span>
<span class="kw">for</span> (<span class="cls">MessageHandler</span> h : handlers) {
    dispatchPool.<span class="fn">submit</span>(() -> {
        <span class="kw">try</span> { h.<span class="fn">handle</span>(msg); }
        <span class="kw">catch</span> (<span class="cls">Exception</span> e) { <span class="cm">/* isolated */</span> }
    });
}

<span class="cm">// 4. Shutdown: drain queue before stopping</span>
running = <span class="kw">false</span>;
pool.<span class="fn">awaitTermination</span>(<span class="num">30</span>, <span class="cls">TimeUnit</span>.SECONDS);</pre>
        </div>
      </div>
    </div>
  </div>

  <div class="alert good">✅ <em>Why CopyOnWriteArrayList for subscribers?</em> Iteration is snapshot-based — adding/removing subscribers mid-dispatch doesn't throw ConcurrentModificationException. Write operations are O(n) but dispatch iteration is lock-free. Perfect for read-heavy, write-rare lists like subscriber registries.</div>
</div>

<!-- ===== TASKS ===== -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">01</div><div class="t-label">Race Condition Identification — 4 Snippets</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Name the concurrency bug in each snippet and write a correct fix.</p>
        <pre>// A — Lazy Singleton
class Config {
    private static Config instance;
    public static Config getInstance() {
        if (instance == null) { instance = new Config(); }  // Bug?
        return instance;
    }
}

// B — Check-then-act
class TicketSeller {
    private int tickets = 100;
    public boolean sell() {
        if (tickets > 0) { tickets--; return true; }        // Bug?
        return false;
    }
}

// C — Compound AtomicInteger
AtomicInteger count = new AtomicInteger(0);
public int getAndDoubleIfEven() {
    if (count.get() % 2 == 0)                              // Bug?
        return count.getAndAdd(count.get());
    return count.get();
}

// D — Visibility
class Worker {
    boolean done = false;
    void finish() { done = true; }
    void run()    { while (!done) work(); }                 // Bug?
}</pre>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">02</div><div class="t-label">Thread-Safe LRU Cache</div><div class="t-meta">~2.5 hrs · code</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Implement an LRU Cache with concurrent access from multiple threads.</p>
        <pre>API:
  int  get(int key)           // O(1), returns -1 if absent
  void put(int key, int val)  // O(1), evicts LRU on capacity exceeded

Approach: LinkedHashMap (accessOrder=true) + ReentrantReadWriteLock
          OR: ConcurrentHashMap + ConcurrentLinkedDeque + explicit sync

Requirements:
  - Correct under 8 concurrent threads × 100k operations
  - No ConcurrentModificationException
  - LRU eviction order correct under concurrent access

Bonus: Benchmark vs Collections.synchronizedMap(new LinkedHashMap())
  Measure: throughput (ops/sec), latency p50/p99</pre>
      </div>
    </div>

    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">03</div><div class="t-label">Dining Philosophers — Two Solutions</div><div class="t-meta">~2 hrs · code</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Implement and then fix the classic deadlock problem.</p>
        <pre>Setup: 5 philosophers, 5 forks (shared between adjacent pairs)
Lifecycle: think() → pickBothForks() → eat() → putDownForks()

Step 1: Implement naive version — show it deadlocks
  (5 threads all pick left fork simultaneously → circular wait)

Step 2: Fix with lock ordering
  Odd philosophers:  pick left, then right
  Even philosophers: pick right, then left
  → Breaks circular wait

Step 3: Fix with arbitrator (Semaphore)
  Only 4 philosophers allowed to try picking up forks at once
  → At most 4 can compete, guaranteeing one can always complete
  new Semaphore(4) wrapping pickBothForks()

Verify: 100 rounds, each philosopher eats at least once (no starvation)</pre>
      </div>
    </div>

    <div class="task-card" style="border-top:2px solid var(--cyan)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--cyan)">★</div><div class="t-label">Mini Project — Production Parking Lot</div><div class="t-meta">~5 hrs · full LLD</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <pre>Requirements:
  - 3 types: Car(100), Bike(50), Truck(20) spots
  - 50 concurrent threads simulating arrivals/departures
  - Display board with real-time counts (read-heavy)
  - Ticket: vehicleId, spotId, entryTime, UUID
  - Fee: first 2h free, ₹50/hour after
  - Entry rate limit: 5 vehicles/sec (Token Bucket)

Concurrency mechanisms:
  Spot claim:      AtomicBoolean.compareAndSet (lock-free)
  Type counting:   AtomicInteger (lock-free)
  Capacity guard:  Semaphore(N, fair=true)
  Display board:   ReadWriteLock (concurrent reads)
  Entry gate:      TokenBucketRateLimiter (synchronized)

Correctness proof (JUnit assertions):
  1. Zero double-bookings: assert each spotId assigned to ≤ 1 vehicle
  2. Count invariant: final available + occupied == initial capacity
  3. All tickets have valid entry timestamps
  4. Fee calculation correct for 0, 2, 3, 5 hour durations

Deliverable: Full Java code + JUnit test + UML with sync annotations</pre>
      </div>
    </div>
  </div>
</div>

<!-- ===== CHECKLIST ===== -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl" style="color:var(--muted)">0 / 13 completed</span><span style="color:var(--cyan)">MODULE A5 · CONCURRENCY IN LLD</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Understand JMM: visibility, atomicity, happens-before — and their differences</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know when to use volatile vs synchronized vs AtomicXxx vs LongAdder</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">synchronized vs ReentrantLock: know every advantage of each</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can implement Producer-Consumer with BlockingQueue from memory</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">ReadWriteLock: know rule — read downgrade allowed, upgrade not</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Semaphore: can implement bounded pool and explain acquire/release semantics</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Condition variables: know await() MUST be in while loop, and why</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">All 4 Coffman conditions + how to break each one</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can implement Token Bucket rate limiter from memory</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">ExecutorService types: fixed, cached, scheduled, custom — when each</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1–3 completed (race conditions, LRU, dining philosophers)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Mini Project: Parking Lot — zero double-bookings verified under load</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Pub/Sub Queue implemented and tested with concurrent publishers</div></div>
  </div>

  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--border2);padding:22px;border-top:2px solid var(--cyan);">
    <div style="font-family:'Share Tech Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:2px;margin-bottom:10px;">// TRACK A COMPLETE → MOVING TO TRACK B</div>
    <div style="font-family:'Orbitron',monospace;font-size:22px;color:var(--bright);margin-bottom:6px;">Track B — High-Level System Design</div>
    <div style="font-size:13px;color:var(--muted);line-height:1.7;font-family:'Share Tech Mono',monospace;">
      B1: HLD Fundamentals (CAP, consistency models, availability patterns)<br>
      B2: Databases at Scale (sharding, replication, SQL vs NoSQL tradeoffs)<br>
      B3: Caching (Redis, CDN, cache invalidation strategies)<br>
      B4: Message Queues (Kafka, RabbitMQ, at-least-once vs exactly-once)<br>
      B5: URL Shortener · Pastebin · TinyURL design<br>
      B6: Design Twitter Feed · Instagram · Netflix
    </div>
  </div>
</div>

</div><!-- end content -->

<script>
function show(tab, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}

function tt(hd) {
  const bd  = hd.nextElementSibling;
  const arr = hd.querySelector('.t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function tick(el) {
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.chk').length;
  const done  = document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done/total)*100}%`;
}

// Animated thread counter
let counts = [0, 0, 0];
function animateCounts() {
  counts = counts.map((c, i) => {
    const delta = Math.floor(Math.random() * 3);
    return Math.min(1000, c + delta);
  });
  document.getElementById('tv1').textContent = counts[0];
  document.getElementById('tv2').textContent = counts[1];
  document.getElementById('tv3').textContent = counts[2];
}
setInterval(animateCounts, 400);
</script>
<div class="m5-bottom-nav" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid var(--border2);padding-top:20px;">
  <a href="/learning/system-design/lld/module-a4-behavioral/" class="m5-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">← PREVIOUS: LLD A4</a>
  <a href="/learning/system-design/lld/module-a5-notes/" class="m5-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--cyan);color:var(--cyan);border-radius:4px;text-decoration:none;font-weight:600;">📄 READ STUDY NOTES</a>
  <a href="/learning/system-design/system-design-roadmap/" class="m5-nav-footer-btn" style="padding:12px 24px;border:1px solid var(--border2);border-radius:4px;color:var(--muted);text-decoration:none;">↑ ROADMAP</a>
  <a href="/learning/system-design/lld/module-a6-case-studies/" class="m5-nav-footer-btn" style="padding:12px 24px;background:var(--cyan);color:var(--bg);border-radius:4px;text-decoration:none;font-weight:600;">NEXT: LLD A6 →</a>
</div>
