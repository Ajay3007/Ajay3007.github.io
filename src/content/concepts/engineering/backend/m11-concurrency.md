---
title: "M11 — Concurrency & Performance"
description: "Phase 4 · Module 11 Concurrency Performance Threading models · Synchronization · Lock-free · epoll/io uring · Caching · Load Balancing pthreads epoll io uring stdatomic.h Redis…"
domain: engineering
track: backend
order: 11
ownHeader: true
url: /learning/backend/m11-concurrency/
---

<style>
/* ── Base ────────────────────────────────────────────────── */
.mod-wrap{font-family:'Segoe UI',system-ui,sans-serif;max-width:960px;margin:0 auto;padding:1.5rem 1rem 4rem;}
/* ── Header ──────────────────────────────────────────────── */
.mod-header{background:linear-gradient(135deg,#1a1f36 0%,#2d3561 100%);color:#fff;border-radius:14px;padding:2rem 2.4rem;margin-bottom:1.8rem;border-left:6px solid #f59e0b;position:relative;overflow:hidden;}
.mod-header::before{content:'';position:absolute;top:-40px;right:-40px;width:180px;height:180px;background:rgba(245,158,11,.12);border-radius:50%;}
.mod-kicker{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:#f59e0b;font-weight:700;margin-bottom:.4rem;}
.mod-title{font-size:1.9rem;font-weight:800;margin:0 0 .5rem;line-height:1.2;}
.mod-sub{color:#a0aec0;font-size:.95rem;margin:0 0 1.1rem;}
.mod-chips{display:flex;flex-wrap:wrap;gap:.45rem;}
.chip{background:rgba(245,158,11,.18);color:#f59e0b;border:1px solid rgba(245,158,11,.35);border-radius:20px;padding:.2rem .75rem;font-size:.72rem;font-weight:600;}
/* ── Tabs ─────────────────────────────────────────────────── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:1.4rem;}
.tab-btn{background:#f1f5f9;border:none;border-radius:8px;padding:.45rem 1rem;font-size:.82rem;font-weight:600;cursor:pointer;color:#475569;transition:all .18s;}
.tab-btn.active{background:linear-gradient(135deg,#f59e0b,#f97316);color:#fff;box-shadow:0 3px 10px rgba(245,158,11,.35);}
.tab-pane{display:none;}.tab-pane.active{display:block;}
/* ── Callouts ─────────────────────────────────────────────── */
.ins,.warn,.note,.analogy{border-radius:9px;padding:.85rem 1.1rem;margin:.9rem 0;font-size:.88rem;border-left:4px solid;}
.ins{background:#f0fdf4;border-color:#22c55e;color:#166534;}
.warn{background:#fef3c7;border-color:#f59e0b;color:#92400e;}
.note{background:#eff6ff;border-color:#3b82f6;color:#1e40af;}
.analogy{background:#fdf4ff;border-color:#a855f7;color:#6b21a8;}
/* ── Cards ────────────────────────────────────────────────── */
.cp{border-radius:11px;margin:.9rem 0;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.07);}
.cp-hdr{padding:.6rem 1.1rem;font-weight:700;font-size:.82rem;letter-spacing:.04em;display:flex;align-items:center;gap:.5rem;}
.cp-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7;}
.p-amber .cp-hdr{background:linear-gradient(90deg,#f59e0b,#f97316);color:#fff;}
.p-amber .cp-body{background:#fffbeb;}
.p-orange .cp-hdr{background:linear-gradient(90deg,#f97316,#ea580c);color:#fff;}
.p-orange .cp-body{background:#fff7ed;}
.p-blue .cp-hdr{background:linear-gradient(90deg,#3b82f6,#2563eb);color:#fff;}
.p-blue .cp-body{background:#eff6ff;}
.p-teal .cp-hdr{background:linear-gradient(90deg,#14b8a6,#0d9488);color:#fff;}
.p-teal .cp-body{background:#f0fdfa;}
.p-green .cp-hdr{background:linear-gradient(90deg,#22c55e,#16a34a);color:#fff;}
.p-green .cp-body{background:#f0fdf4;}
.p-purple .cp-hdr{background:linear-gradient(90deg,#a855f7,#9333ea);color:#fff;}
.p-purple .cp-body{background:#faf5ff;}
.p-red .cp-hdr{background:linear-gradient(90deg,#ef4444,#dc2626);color:#fff;}
.p-red .cp-body{background:#fef2f2;}
.p-indigo .cp-hdr{background:linear-gradient(90deg,#6366f1,#4f46e5);color:#fff;}
.p-indigo .cp-body{background:#eef2ff;}
/* ── Flow list ────────────────────────────────────────────── */
.flow-list{list-style:none;padding:0;margin:.5rem 0;}
.fl-step{display:flex;gap:.8rem;align-items:flex-start;padding:.65rem .9rem;margin:.35rem 0;border-radius:8px;background:linear-gradient(90deg,rgba(245,158,11,.09),rgba(249,115,22,.05));border-left:3px solid #f59e0b;font-size:.86rem;}
.fl-num{background:linear-gradient(135deg,#f59e0b,#f97316);color:#fff;border-radius:50%;width:22px;height:22px;min-width:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;}
/* ── Code blocks ──────────────────────────────────────────── */
.cb{background:#0f172a;border-radius:10px;padding:1.2rem 1.4rem;margin:.85rem 0;overflow-x:auto;font-size:.8rem;line-height:1.7;font-family:'Fira Code','Cascadia Code',monospace;}
.cm{color:#64748b;}.ck{color:#f59e0b;font-weight:600;}.cv{color:#38bdf8;}.cs{color:#86efac;}.cn{color:#fbbf24;}.cf{color:#e879f9;}
/* ── Tables ───────────────────────────────────────────────── */
.t-table{width:100%;border-collapse:collapse;font-size:.84rem;margin:.8rem 0;}
.t-table th{background:linear-gradient(90deg,#f59e0b,#f97316);color:#fff;padding:.6rem .9rem;text-align:left;font-weight:700;}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top;}
.t-table tr:nth-child(even) td{background:#fafafa;}
.t-table tr:hover td{background:#fff7ed;}
/* ── Two-col ──────────────────────────────────────────────── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0;}
@media(max-width:600px){.two-col{grid-template-columns:1fr;}}
/* ── Lab box ──────────────────────────────────────────────── */
.lab-box{border:2px solid #f59e0b;border-radius:12px;margin:1.2rem 0;overflow:hidden;}
.lab-hdr{background:linear-gradient(90deg,#f59e0b,#f97316);padding:.7rem 1.2rem;color:#fff;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.6rem;}
.lab-body{padding:1rem 1.2rem;background:#fffbeb;}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;margin:.45rem 0;font-size:.86rem;}
.sn{background:#f59e0b;color:#fff;border-radius:50%;width:20px;height:20px;min-width:20px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;margin-top:.1rem;}
/* ── Checklist ────────────────────────────────────────────── */
.cl{list-style:none;padding:0;}
.cl li{padding:.45rem .7rem;margin:.3rem 0;border-radius:7px;background:#f8fafc;border-left:3px solid #e2e8f0;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem;}
.cl li::before{content:'□';color:#cbd5e1;font-size:1rem;line-height:1;}
.cl li.ok::before{content:'✓';color:#22c55e;}
.cl-section{font-weight:700;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:#64748b;margin:1rem 0 .4rem;}
/* ── Nav ──────────────────────────────────────────────────── */
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding-top:1.2rem;border-top:2px solid #f1f5f9;flex-wrap:wrap;gap:.7rem;}
.nb{background:linear-gradient(135deg,#f59e0b,#f97316);color:#fff;text-decoration:none;padding:.5rem 1.2rem;border-radius:8px;font-weight:700;font-size:.85rem;transition:opacity .18s;}
.nb:hover{opacity:.88;}
.nb.sec{background:#f1f5f9;color:#475569;}
/* ── Separator ────────────────────────────────────────────── */
.sep{height:1px;background:linear-gradient(90deg,transparent,#e2e8f0,transparent);margin:1.4rem 0;}
/* ── Diagram ──────────────────────────────────────────────── */
.diagram-box{background:#0f172a;border-radius:10px;padding:1.2rem 1.6rem;margin:.9rem 0;font-family:'Fira Code','Cascadia Code',monospace;font-size:.78rem;line-height:1.8;color:#e2e8f0;overflow-x:auto;}
.dg-amber{color:#fbbf24;font-weight:700;}
.dg-blue{color:#60a5fa;}
.dg-green{color:#86efac;}
.dg-red{color:#f87171;}
.dg-gray{color:#64748b;}
</style>

<div class="mod-wrap">

<div class="mod-header">
  <div class="mod-kicker">Phase 4 · Module 11</div>
  <div class="mod-title">Concurrency &amp; Performance</div>
  <div class="mod-sub">Threading models · Synchronization · Lock-free · epoll/io_uring · Caching · Load Balancing</div>
  <div class="mod-chips">
    <span class="chip">pthreads</span>
    <span class="chip">epoll</span>
    <span class="chip">io_uring</span>
    <span class="chip">stdatomic.h</span>
    <span class="chip">Redis</span>
    <span class="chip">pgBouncer</span>
    <span class="chip">C / Linux</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('threading',this)">Threading Models</button>
  <button class="tab-btn" onclick="vt('sync',this)">Sync Primitives</button>
  <button class="tab-btn" onclick="vt('lockfree',this)">Lock-Free</button>
  <button class="tab-btn" onclick="vt('iomux',this)">I/O Multiplexing</button>
  <button class="tab-btn" onclick="vt('caching',this)">Caching</button>
  <button class="tab-btn" onclick="vt('scaling',this)">Scaling</button>
  <button class="tab-btn" onclick="vt('impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('labs',this)">Labs &amp; Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 1 — OVERVIEW
     ══════════════════════════════════════════════════════════ -->
<div id="tab-overview" class="tab-pane active">

<div class="cp p-amber">
  <div class="cp-hdr">⚡ Why This Phase Matters</div>
  <div class="cp-body">
    <p>A backend that is correct but slow is a bug. Phase 4 closes the gap between writing code that <em>works</em> and writing code that <em>scales</em>. The concepts here — event loops, lock-free atomics, epoll — are what separate a 100 req/s prototype from a 100,000 req/s production service.</p>
    <p>Everything builds on Phase 0 (Linux syscalls) and Phase 2 (TCP/HTTP): you need to understand file descriptors and sockets before epoll makes sense, and you need HTTP to understand why C10K matters.</p>
  </div>
</div>

<div class="two-col">
  <div class="cp p-teal">
    <div class="cp-hdr">🔗 Prerequisites</div>
    <div class="cp-body">
      <ul>
        <li><strong>Ph0</strong> — Linux syscalls, file descriptors, process model</li>
        <li><strong>Ph2</strong> — TCP sockets, HTTP request/response lifecycle</li>
        <li>Basic C: pointers, structs, malloc/free</li>
        <li>M01 (networking stack) and M06 (HTTP internals) recommended</li>
      </ul>
    </div>
  </div>
  <div class="cp p-blue">
    <div class="cp-hdr">🎯 What You Will Build</div>
    <div class="cp-body">
      <ul>
        <li>Edge-triggered <strong>epoll event loop</strong> in C handling 10K+ conns</li>
        <li>Thread pool with mutex + condition variable work queue</li>
        <li>Lock-free MPSC queue using <code>stdatomic.h</code> CAS</li>
        <li>In-process <strong>LRU cache</strong> (hash map + doubly-linked list)</li>
        <li>Benchmark: thread-per-conn vs epoll event loop</li>
      </ul>
    </div>
  </div>
</div>

<div class="sep"></div>
<div class="cp p-orange">
  <div class="cp-hdr">📋 Module Roadmap — 10 Concepts</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>#</th><th>Concept</th><th>Tab</th><th>Key Insight</th></tr></thead>
      <tbody>
        <tr><td>C1</td><td>Threading models</td><td>Threading</td><td>Thread-per-req wastes 8KB stack × N; event loop reuses one thread</td></tr>
        <tr><td>C2</td><td>Synchronization primitives</td><td>Sync</td><td>Mutex = binary; semaphore = counting; condvar = signaling</td></tr>
        <tr><td>C3</td><td>Lock-free CAS / stdatomic.h</td><td>Lock-Free</td><td>Atomic read-modify-write without kernel involvement</td></tr>
        <tr><td>C4</td><td>I/O multiplexing evolution</td><td>I/O Mux</td><td>select→poll→epoll→io_uring; O(n)→O(1) notification</td></tr>
        <tr><td>C5</td><td>C10K problem</td><td>I/O Mux</td><td>OS scheduling kills thread-per-conn; epoll is the fix</td></tr>
        <tr><td>C6</td><td>In-process LRU/LFU caching</td><td>Caching</td><td>Hash map + doubly-linked list = O(1) get/put/evict</td></tr>
        <tr><td>C7</td><td>Cache stampede / Redis</td><td>Caching</td><td>Mutex lock or probabilistic early expiry prevents thundering herd</td></tr>
        <tr><td>C8</td><td>Connection pool management</td><td>Scaling</td><td>Pool exhaustion → queue with timeout + backpressure</td></tr>
        <tr><td>C9</td><td>Load balancing algorithms</td><td>Scaling</td><td>Consistent hashing minimizes redistribution on node change</td></tr>
        <tr><td>C10</td><td>Stateless horizontal scaling</td><td>Scaling</td><td>Externalize all state; make ops idempotent</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 2 — THREADING MODELS
     ══════════════════════════════════════════════════════════ -->
<div id="tab-threading" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🧵 C1 — Four Threading Models Every Backend Engineer Must Know</div>
  <div class="cp-body">
    <p>The threading model is the most consequential architectural decision in a concurrent server. It determines memory footprint, latency profile, CPU utilisation, and how hard the code is to reason about. There are four canonical models.</p>
  </div>
</div>

<table class="t-table">
  <thead><tr><th>Model</th><th>How It Works</th><th>Memory / 10K Conns</th><th>Best For</th><th>Real Examples</th></tr></thead>
  <tbody>
    <tr><td><strong>Thread-per-request</strong></td><td>One OS thread per active connection; blocks on I/O</td><td>~80 MB (8KB stack × 10K)</td><td>Low concurrency, simple CRUD</td><td>Apache prefork, early Java servlets</td></tr>
    <tr><td><strong>Thread pool</strong></td><td>Fixed N threads; work queue; threads pick up tasks</td><td>~800 KB (N=100 threads)</td><td>CPU-bound tasks, mixed workloads</td><td>Apache worker MPM, gRPC server</td></tr>
    <tr><td><strong>Event loop</strong></td><td>Single thread; I/O multiplexing (epoll); non-blocking</td><td>~kilobytes per conn</td><td>High-concurrency I/O-bound services</td><td>Nginx, Node.js, Redis</td></tr>
    <tr><td><strong>Green threads / M:N</strong></td><td>Userspace scheduler maps M goroutines → N OS threads</td><td>~2 KB stack (growable)</td><td>Mixed I/O+CPU; simple code</td><td>Go goroutines, Rust async/tokio, Erlang</td></tr>
  </tbody>
</table>

<div class="two-col">
  <div class="cp p-red">
    <div class="cp-hdr">⚠️ Why Thread-per-Request Breaks at Scale</div>
    <div class="cp-body">
      <ul>
        <li><strong>Stack memory</strong>: Linux default 8 MB ulimit, minimum 4–8 KB actual; 10K threads = 40–80 MB <em>minimum</em></li>
        <li><strong>Context switching</strong>: Each OS thread switch costs ~1–10 µs (TLB flush, register save); 10K threads fighting for CPU = scheduling storm</li>
        <li><strong>Blocking I/O</strong>: Thread sits idle during syscall (read, write, accept). CPU does nothing useful</li>
        <li><strong>Memory bandwidth</strong>: Each sleeping thread's stack still occupies virtual memory — page faults on wake</li>
      </ul>
    </div>
  </div>
  <div class="cp p-green">
    <div class="cp-hdr">✅ Event Loop Model Advantages</div>
    <div class="cp-body">
      <ul>
        <li><strong>No blocking</strong>: All I/O is async; thread never waits</li>
        <li><strong>One thread → thousands of connections</strong>: epoll delivers ready FDs in O(1)</li>
        <li><strong>Cache-friendly</strong>: Single thread has hot L1/L2; no context switch overhead</li>
        <li><strong>Predictable latency</strong>: No lock contention between connections</li>
        <li><strong>Limitation</strong>: CPU-bound tasks block the loop — offload to thread pool</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔩 Thread Pool Pattern — Bounded Work Queue</div>
  <div class="cp-body">
    <p>Best of both worlds: event loop accepts connections, but dispatches CPU-bound work to a thread pool. The key design decisions are queue depth (prevents unbounded memory growth), number of workers (usually CPU cores × 1–2), and what to do when the queue is full (reject with 503, or block with timeout).</p>
    <div class="diagram-box">
<span class="dg-amber">Incoming Requests</span>
        │
        ▼
<span class="dg-blue">[ Accept Thread ] ──── epoll event loop</span>
        │
        ▼ enqueue task
<span class="dg-green">[ Bounded Work Queue ]  capacity = 1024</span>
        │
    ┌───┴─────────────────────────────────┐
    ▼           ▼           ▼             ▼
<span class="dg-amber">Worker 1    Worker 2    Worker 3  ...  Worker N</span>
 (thread)    (thread)    (thread)       (thread)
    │
    ▼ queue full?
<span class="dg-red">→ 503 Service Unavailable  (backpressure)</span>
    </div>
  </div>
</div>

<div class="analogy">
  <strong>Analogy — Restaurant Kitchen:</strong> Thread-per-request = hire a new chef for every diner (chaos, expensive). Thread pool = hire 8 chefs, queue orders (Apache worker MPM). Event loop = one chef who never waits — checks oven, assembles plate, checks next order, never blocks (Nginx). Green threads = chef clones who can pause mid-task and swap (Go goroutines).
</div>

<div class="cp p-indigo">
  <div class="cp-hdr">🔧 pthreads Quick Reference</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;pthread.h&gt;</span>
<span class="cm">// Link with -lpthread</span>

<span class="cm">/* Create a thread */</span>
<span class="ck">pthread_t</span> tid;
<span class="cf">pthread_create</span>(<span class="cv">&amp;tid</span>, <span class="cv">NULL</span>, worker_fn, arg);
<span class="cf">pthread_join</span>(tid, <span class="cv">NULL</span>);       <span class="cm">/* block until done */</span>
<span class="cf">pthread_detach</span>(tid);             <span class="cm">/* auto-cleanup on exit */</span>

<span class="cm">/* Thread function signature */</span>
<span class="ck">void</span> *<span class="cf">worker_fn</span>(<span class="ck">void</span> *arg) {
    <span class="ck">int</span> *val = (<span class="ck">int</span> *)arg;
    <span class="cm">/* ... do work ... */</span>
    <span class="ck">return</span> <span class="cv">NULL</span>;
}</div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 3 — SYNCHRONIZATION PRIMITIVES
     ══════════════════════════════════════════════════════════ -->
<div id="tab-sync" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🔐 C2 — Synchronization Primitives: When to Use Each</div>
  <div class="cp-body">
    <p>Every synchronization primitive solves a specific problem. Using the wrong one either causes deadlock, starvation, or unnecessary serialization. Master this decision table before writing any concurrent code.</p>
  </div>
</div>

<table class="t-table">
  <thead><tr><th>Primitive</th><th>Semantics</th><th>pthreads API</th><th>Use When</th><th>Pitfall</th></tr></thead>
  <tbody>
    <tr><td><strong>Mutex</strong></td><td>Binary lock — exclusive access to critical section</td><td><code>pthread_mutex_t</code></td><td>Protecting shared data structure (queue, hash map)</td><td>Lock ordering violations → deadlock</td></tr>
    <tr><td><strong>RW Lock</strong></td><td>Multiple concurrent readers OR one exclusive writer</td><td><code>pthread_rwlock_t</code></td><td>Read-heavy workloads (config, caches, routing tables)</td><td>Writer starvation if readers never yield</td></tr>
    <tr><td><strong>Semaphore</strong></td><td>Counting lock — allows N simultaneous holders</td><td><code>sem_t</code> / <code>sem_init</code></td><td>Rate limiting, connection pools, resource counting</td><td>Forgetting sem_post → deadlock; don't use as mutex</td></tr>
    <tr><td><strong>Condition Variable</strong></td><td>Wait for a predicate; always paired with mutex</td><td><code>pthread_cond_t</code></td><td>Producer/consumer, work queues, thread pools</td><td>Spurious wakeups — always check predicate in loop</td></tr>
    <tr><td><strong>Spinlock</strong></td><td>Busy-wait loop; no kernel involvement</td><td><code>pthread_spinlock_t</code></td><td>Very short critical sections on multi-core only</td><td>Wastes CPU if held for >~100 ns; never block inside</td></tr>
  </tbody>
</table>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🔒 Mutex Pattern — Work Queue</div>
    <div class="cp-body">
<div class="cb"><span class="ck">pthread_mutex_t</span> lock = PTHREAD_MUTEX_INITIALIZER;
<span class="ck">pthread_cond_t</span>  cond = PTHREAD_COND_INITIALIZER;
<span class="ck">int</span> queue_size = <span class="cn">0</span>;

<span class="cm">/* Producer */</span>
<span class="cf">pthread_mutex_lock</span>(<span class="cv">&amp;lock</span>);
enqueue(item);
queue_size++;
<span class="cf">pthread_cond_signal</span>(<span class="cv">&amp;cond</span>);
<span class="cf">pthread_mutex_unlock</span>(<span class="cv">&amp;lock</span>);

<span class="cm">/* Consumer — always loop on predicate */</span>
<span class="cf">pthread_mutex_lock</span>(<span class="cv">&amp;lock</span>);
<span class="ck">while</span> (queue_size == <span class="cn">0</span>)        <span class="cm">/* spurious wakeup guard */</span>
    <span class="cf">pthread_cond_wait</span>(<span class="cv">&amp;cond</span>, <span class="cv">&amp;lock</span>);
item = dequeue();
queue_size--;
<span class="cf">pthread_mutex_unlock</span>(<span class="cv">&amp;lock</span>);</div>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">📖 RW Lock Pattern — Config Cache</div>
    <div class="cp-body">
<div class="cb"><span class="ck">pthread_rwlock_t</span> rwlock = PTHREAD_RWLOCK_INITIALIZER;

<span class="cm">/* Multiple threads reading simultaneously */</span>
<span class="cf">pthread_rwlock_rdlock</span>(<span class="cv">&amp;rwlock</span>);
val = config_get(<span class="cs">"max_conns"</span>);
<span class="cf">pthread_rwlock_unlock</span>(<span class="cv">&amp;rwlock</span>);

<span class="cm">/* One thread writing (reloads config) */</span>
<span class="cf">pthread_rwlock_wrlock</span>(<span class="cv">&amp;rwlock</span>);
config_reload();            <span class="cm">/* exclusive */</span>
<span class="cf">pthread_rwlock_unlock</span>(<span class="cv">&amp;rwlock</span>);</div>
    </div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">🔢 Semaphore Pattern — Connection Pool Rate Limiter</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;semaphore.h&gt;</span>

sem_t pool_sem;
<span class="cf">sem_init</span>(<span class="cv">&amp;pool_sem</span>, <span class="cn">0</span>, <span class="cn">20</span>);    <span class="cm">/* allow 20 concurrent DB conns */</span>

<span class="cm">/* Acquire a slot — blocks if pool is exhausted */</span>
<span class="cf">sem_wait</span>(<span class="cv">&amp;pool_sem</span>);            <span class="cm">/* decrement; block if 0 */</span>
conn = pool_acquire();
do_query(conn);
pool_release(conn);
<span class="cf">sem_post</span>(<span class="cv">&amp;pool_sem</span>);            <span class="cm">/* increment; wake waiter */</span>

<span class="cm">/* Non-blocking try */</span>
<span class="ck">if</span> (<span class="cf">sem_trywait</span>(<span class="cv">&amp;pool_sem</span>) == <span class="cn">-1</span>) {
    <span class="cm">/* pool full → return 503 immediately */</span>
}</div>
  </div>
</div>

<div class="warn">
  <strong>Deadlock Recipe:</strong> Lock A then B in thread 1; lock B then A in thread 2. Prevent with a global lock ordering (always acquire in same order by address or enum), or use <code>pthread_mutex_trylock</code> with backoff.
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📐 Lock Granularity Rule</div>
  <div class="cp-body">
    <p>Hold locks for the <em>shortest time possible</em>. Never do I/O, system calls, or expensive computation while holding a mutex. Extract the data you need under the lock, release, then process. This maximises throughput and minimises tail latency.</p>
    <table class="t-table">
      <thead><tr><th>Anti-Pattern</th><th>Fix</th></tr></thead>
      <tbody>
        <tr><td>Call <code>send()</code> while holding mutex</td><td>Copy data out, release lock, then send</td></tr>
        <tr><td>malloc inside critical section</td><td>Pre-allocate or allocate before locking</td></tr>
        <tr><td>Nested locks without ordering</td><td>Define global lock hierarchy by module/enum</td></tr>
        <tr><td>Spinlock on single-core machine</td><td>Use mutex — spinning just wastes quanta</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 4 — LOCK-FREE
     ══════════════════════════════════════════════════════════ -->
<div id="tab-lockfree" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">⚛️ C3 — Lock-Free Programming with CAS and stdatomic.h</div>
  <div class="cp-body">
    <p>Lock-free algorithms allow multiple threads to make progress without mutual exclusion. The foundation is <strong>Compare-And-Swap (CAS)</strong> — an atomic operation that reads, compares, and conditionally writes in a single uninterruptible hardware instruction.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔑 CAS Semantics</div>
  <div class="cp-body">
    <p>The operation atomically performs:</p>
<div class="cb"><span class="cm">// Conceptual (not actual C):</span>
<span class="ck">bool</span> <span class="cf">CAS</span>(<span class="ck">int</span> *ptr, <span class="ck">int</span> expected, <span class="ck">int</span> desired) {
    <span class="ck">if</span> (*ptr == expected) {
        *ptr = desired;
        <span class="ck">return</span> <span class="cn">true</span>;    <span class="cm">// success: we made the swap</span>
    }
    expected = *ptr;   <span class="cm">// update caller's expected value</span>
    <span class="ck">return</span> <span class="cn">false</span>;      <span class="cm">// failure: retry with new expected</span>
}

<span class="cm">// Hardware instruction: LOCK CMPXCHG on x86</span>
<span class="cm">// One bus cycle; no kernel involvement; no mutex needed</span></div>
    <p>Retry loops (optimistic concurrency) are used when CAS fails — re-read the current value and try again. Progress is guaranteed for at least one thread in each round.</p>
  </div>
</div>

<div class="two-col">
  <div class="cp p-teal">
    <div class="cp-hdr">📦 C11 stdatomic.h</div>
    <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;stdatomic.h&gt;</span>

<span class="ck">atomic_int</span> counter = ATOMIC_VAR_INIT(<span class="cn">0</span>);

<span class="cm">/* Atomic increment — replaces mutex for counters */</span>
<span class="cf">atomic_fetch_add</span>(<span class="cv">&amp;counter</span>, <span class="cn">1</span>);

<span class="cm">/* Load / store with explicit memory order */</span>
<span class="ck">int</span> val = <span class="cf">atomic_load_explicit</span>(
    <span class="cv">&amp;counter</span>, memory_order_acquire);
<span class="cf">atomic_store_explicit</span>(
    <span class="cv">&amp;counter</span>, <span class="cn">42</span>, memory_order_release);

<span class="cm">/* CAS — strong (no spurious failures) */</span>
<span class="ck">int</span> expected = <span class="cn">0</span>;
<span class="ck">bool</span> ok = <span class="cf">atomic_compare_exchange_strong</span>(
    <span class="cv">&amp;counter</span>, <span class="cv">&amp;expected</span>, <span class="cn">1</span>);</div>
    </div>
  </div>
  <div class="cp p-orange">
    <div class="cp-hdr">🔧 GCC __atomic Builtins (Pre-C11)</div>
    <div class="cp-body">
<div class="cb"><span class="cm">/* GCC atomic builtins — widely supported */</span>
<span class="ck">int</span> old = <span class="cf">__atomic_fetch_add</span>(
    <span class="cv">&amp;counter</span>, <span class="cn">1</span>, __ATOMIC_SEQ_CST);

<span class="ck">int</span> expected = <span class="cn">5</span>, desired = <span class="cn">6</span>;
<span class="ck">bool</span> ok = <span class="cf">__atomic_compare_exchange_n</span>(
    <span class="cv">&amp;counter</span>,
    <span class="cv">&amp;expected</span>,
    desired,
    <span class="cn">false</span>,             <span class="cm">/* strong */</span>
    __ATOMIC_SEQ_CST,
    __ATOMIC_SEQ_CST
);

<span class="cm">/* Memory orders (fastest to strongest):
   RELAXED → ACQUIRE/RELEASE → SEQ_CST
   Use ACQUIRE for loads, RELEASE for stores */</span></div>
    </div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">🐛 The ABA Problem</div>
  <div class="cp-body">
    <p>CAS checks <em>value equality</em> not <em>identity</em>. If a pointer changes A → B → A between your read and your CAS, the CAS succeeds even though the world has changed underneath you — leading to use-after-free or silent data corruption in lock-free linked lists and queues.</p>
    <table class="t-table">
      <thead><tr><th>Problem</th><th>Fix</th></tr></thead>
      <tbody>
        <tr><td>Pointer A freed and reallocated at same address</td><td>Double-width CAS: combine pointer + version counter (128-bit CAS on x86-64)</td></tr>
        <tr><td>Node popped from stack, pushed back</td><td>Tagged pointer — store generation counter in low bits (alignment gives free bits)</td></tr>
        <tr><td>Hazard pointer technique</td><td>Threads publish pointers they are reading; reclamation checks the hazard list before freeing</td></tr>
      </tbody>
    </table>
<div class="cb"><span class="cm">/* Tagged pointer — 64-bit pointer, low 16 bits = generation */</span>
<span class="ck">typedef struct</span> { <span class="ck">uintptr_t</span> ptr; <span class="ck">uint64_t</span> gen; } TaggedPtr;
<span class="ck">_Alignas</span>(<span class="cn">16</span>) <span class="ck">atomic_</span>TaggedPtr head;  <span class="cm">/* needs 128-bit CAS */</span>

<span class="cm">/* x86-64: use CMPXCHG16B via GCC __int128 trick */</span></div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">📨 Lock-Free MPSC Queue (Practical Pattern)</div>
  <div class="cp-body">
    <p>Multi-producer single-consumer queues are the most practical lock-free structure for server internals. Producers do a CAS on the tail; the single consumer pops without a lock (no CAS needed on head with SPSC guarantee).</p>
<div class="cb"><span class="ck">typedef struct</span> Node {
    <span class="ck">void</span>             *data;
    <span class="ck">_Atomic</span>(<span class="ck">struct</span> Node *) next;
} Node;

<span class="ck">typedef struct</span> {
    <span class="ck">_Atomic</span>(Node *) head;   <span class="cm">/* consumer reads */</span>
    <span class="ck">_Atomic</span>(Node *) tail;   <span class="cm">/* producers CAS  */</span>
} MPSCQueue;

<span class="ck">void</span> <span class="cf">mpsc_push</span>(MPSCQueue *q, Node *n) {
    <span class="cf">atomic_store_explicit</span>(<span class="cv">&amp;n</span>->next, <span class="cv">NULL</span>, memory_order_relaxed);
    Node *prev = <span class="cf">atomic_exchange_explicit</span>(<span class="cv">&amp;q</span>->tail, n, memory_order_acq_rel);
    <span class="cm">/* Link — at most one writer per prev slot */</span>
    <span class="cf">atomic_store_explicit</span>(<span class="cv">&amp;prev</span>->next, n, memory_order_release);
}</div>
  </div>
</div>

<div class="note">
  <strong>Memory Ordering Rules of Thumb:</strong> Use <code>memory_order_relaxed</code> for statistics counters (no ordering needed). Use <code>acquire/release</code> pairs for producer-consumer handoffs. Use <code>seq_cst</code> only when you need a global total order — it is the slowest (full fence on x86, heavyweight on ARM).
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 5 — I/O MULTIPLEXING
     ══════════════════════════════════════════════════════════ -->
<div id="tab-iomux" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🔀 C4 + C5 — I/O Multiplexing Evolution &amp; the C10K Problem</div>
  <div class="cp-body">
    <p>I/O multiplexing lets a single thread wait on <em>multiple</em> file descriptors simultaneously, being notified only when one is ready — eliminating the need for a thread per connection. The Linux kernel has evolved four generations of this interface over 30 years.</p>
  </div>
</div>

<table class="t-table">
  <thead><tr><th>API</th><th>Year</th><th>Notification Model</th><th>Max FDs</th><th>Complexity</th><th>Verdict</th></tr></thead>
  <tbody>
    <tr><td><code>select</code></td><td>1983</td><td>Bitmask scan on return</td><td>1024 (FD_SETSIZE)</td><td>O(n) per call</td><td>Legacy only</td></tr>
    <tr><td><code>poll</code></td><td>1986</td><td>Linear scan of pollfd array</td><td>Unlimited</td><td>O(n) per call</td><td>Portable but slow</td></tr>
    <tr><td><code>epoll</code></td><td>2002</td><td>Kernel event queue; ready list</td><td>Unlimited</td><td>O(1) add/wait</td><td>Linux standard</td></tr>
    <tr><td><code>io_uring</code></td><td>2019</td><td>Ring buffers; zero syscall per I/O</td><td>Unlimited</td><td>O(1) + amortised</td><td>Linux 5.1+, future</td></tr>
  </tbody>
</table>

<div class="cp p-blue">
  <div class="cp-hdr">🔵 epoll Deep Dive — the Three-Syscall API</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;sys/epoll.h&gt;</span>

<span class="cm">/* 1. Create epoll instance — returns epoll fd */</span>
<span class="ck">int</span> epfd = <span class="cf">epoll_create1</span>(EPOLL_CLOEXEC);

<span class="cm">/* 2. Register / modify / remove FDs */</span>
<span class="ck">struct</span> epoll_event ev;
ev.events   = EPOLLIN | EPOLLET;  <span class="cm">/* EPOLLET = edge-triggered */</span>
ev.data.fd  = client_fd;
<span class="cf">epoll_ctl</span>(epfd, EPOLL_CTL_ADD, client_fd, <span class="cv">&amp;ev</span>);
<span class="cm">/* EPOLL_CTL_MOD to change, EPOLL_CTL_DEL to remove */</span>

<span class="cm">/* 3. Wait — returns only ready FDs */</span>
<span class="ck">struct</span> epoll_event events[<span class="cn">128</span>];
<span class="ck">int</span> n = <span class="cf">epoll_wait</span>(epfd, events, <span class="cn">128</span>, <span class="cn">-1</span>);  <span class="cm">/* -1 = block forever */</span>
<span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i &lt; n; i++) {
    handle(events[i].data.fd, events[i].events);
}</div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-teal">
    <div class="cp-hdr">Edge-Triggered (ET) vs Level-Triggered (LT)</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Mode</th><th>When kernel notifies</th><th>Read behaviour</th></tr></thead>
        <tbody>
          <tr><td><strong>LT</strong> (default)</td><td>Every time FD is readable</td><td>Can read partial — notified again</td></tr>
          <tr><td><strong>ET</strong> (<code>EPOLLET</code>)</td><td>Only on state <em>transition</em> (new data arrives)</td><td>Must read until <code>EAGAIN</code> — otherwise miss data</td></tr>
        </tbody>
      </table>
      <div class="note" style="margin-top:.5rem">ET is higher performance (fewer wakeups) but demands non-blocking FDs and looping reads. LT is safer for beginners.</div>
    </div>
  </div>
  <div class="cp p-orange">
    <div class="cp-hdr">Non-Blocking FD Setup</div>
    <div class="cp-body">
<div class="cb"><span class="ck">static void</span> <span class="cf">set_nonblocking</span>(<span class="ck">int</span> fd) {
    <span class="ck">int</span> flags = <span class="cf">fcntl</span>(fd, F_GETFL, <span class="cn">0</span>);
    <span class="cf">fcntl</span>(fd, F_SETFL, flags | O_NONBLOCK);
}

<span class="cm">/* ET read loop — drain until EAGAIN */</span>
<span class="ck">while</span> (<span class="cn">1</span>) {
    <span class="ck">ssize_t</span> n = <span class="cf">read</span>(fd, buf, <span class="ck">sizeof</span>(buf));
    <span class="ck">if</span> (n == <span class="cn">-1</span> &amp;&amp; errno == EAGAIN) <span class="ck">break</span>;
    <span class="ck">if</span> (n &lt;= <span class="cn">0</span>) { close(fd); <span class="ck">break</span>; }
    process(buf, n);
}</div>
    </div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🚀 io_uring — The Next Generation</div>
  <div class="cp-body">
    <p>Linux 5.1 (2019) introduced <code>io_uring</code>, built around two lock-free ring buffers shared between kernel and userspace:</p>
    <div class="diagram-box">
<span class="dg-amber">Userspace</span>                         <span class="dg-amber">Kernel</span>

<span class="dg-blue">SQ (Submission Queue)</span>  ─────────▶  Kernel picks up SQEs
 └─ SQE: op=READ, fd=5, buf=…            and executes async

<span class="dg-green">CQ (Completion Queue)</span>  ◀─────────  Kernel writes CQE: res=42
 └─ CQE: user_data=…, res=42

<span class="dg-gray">No syscall needed per operation if SQ ring has space.
io_uring_enter() batches multiple submits in one syscall.
io_uring_setup() + mmap() to set up rings.</span>
    </div>
    <table class="t-table">
      <thead><tr><th>Feature</th><th>epoll</th><th>io_uring</th></tr></thead>
      <tbody>
        <tr><td>Syscall per I/O</td><td>Yes (read/write + epoll_wait)</td><td>No (ring buffer, batched)</td></tr>
        <tr><td>Zero-copy</td><td>No</td><td>Yes (fixed buffers)</td></tr>
        <tr><td>Async file I/O</td><td>No (files always "ready")</td><td>Yes (true async)</td></tr>
        <tr><td>Portability</td><td>Linux only</td><td>Linux 5.1+ only</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">💣 C5 — The C10K Problem Explained</div>
  <div class="cp-body">
    <p>Dan Kegel's 1999 paper posed the question: how do you handle 10,000 simultaneous connections on a single server? At the time, the dominant model was one thread per connection. The math:</p>
    <ul>
      <li><strong>10K threads × 8 KB stack</strong> = 80 MB minimum (but pages are faulted in, TLB pressure)</li>
      <li><strong>Context switch cost</strong>: ~1–10 µs each; 10K threads × 100 context switches/sec = 1–10 seconds of CPU time per second just switching</li>
      <li><strong>Kernel scheduler</strong>: O(log n) for CFS scheduler; 10K sleeping threads compete for wake-up slots</li>
    </ul>
    <p><strong>Solution</strong>: epoll event loop. One thread. No context switches between connections. O(1) delivery of ready events. Nginx handles 50K–100K concurrent connections on a single core with this model.</p>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 6 — CACHING
     ══════════════════════════════════════════════════════════ -->
<div id="tab-caching" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🗃️ C6 + C7 — In-Process Caching and Distributed Caching</div>
  <div class="cp-body">
    <p>Caching is the single most impactful performance optimisation available to a backend engineer. The key insight: most production workloads exhibit a power-law access pattern — 20% of keys account for 80% of requests. Keeping that hot 20% in memory eliminates most database round-trips.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔗 C6 — LRU Cache: Hash Map + Doubly-Linked List</div>
  <div class="cp-body">
    <p>The classic O(1) LRU implementation combines:</p>
    <ul>
      <li><strong>Hash map</strong>: O(1) lookup — <em>key → pointer to list node</em></li>
      <li><strong>Doubly-linked list</strong>: O(1) insert/remove; MRU at head, LRU at tail</li>
    </ul>
    <div class="diagram-box">
<span class="dg-amber">GET "user:42"  →  hash_map["user:42"]  →  Node* ptr</span>
                                               │
                        <span class="dg-blue">doubly-linked list     ▼</span>
<span class="dg-green"> HEAD ←→ [user:99] ←→ [user:42] ←→ [user:01] ←→ TAIL</span>
  MRU   ←────────────────────────────────────── LRU

<span class="dg-amber">After GET hit: move user:42 to HEAD</span>
<span class="dg-green"> HEAD ←→ [user:42] ←→ [user:99] ←→ [user:01] ←→ TAIL</span>

<span class="dg-red">On capacity: evict TAIL node (user:01), remove from map</span>
    </div>
<div class="cb"><span class="ck">typedef struct</span> Node {
    <span class="ck">char</span>          key[<span class="cn">64</span>];
    <span class="ck">void</span>         *value;
    <span class="ck">struct</span> Node  *prev, *next;
} Node;

<span class="ck">typedef struct</span> {
    Node        *head, *tail;  <span class="cm">/* sentinel nodes */</span>
    <span class="ck">int</span>          size, capacity;
    <span class="cm">/* hash_map: key → Node* (uthash or open-addressing) */</span>
} LRUCache;

<span class="cm">/* get: hash lookup → move to head → return value */</span>
<span class="cm">/* put: hash lookup → if hit update+move; if miss insert head; if full evict tail */</span></div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-teal">
    <div class="cp-hdr">📊 LFU — Least Frequently Used</div>
    <div class="cp-body">
      <p>Evicts the key accessed the fewest times. Better than LRU for workloads where old-but-popular keys should stay (e.g. homepage, top products).</p>
      <p><strong>Implementation</strong>: min-heap keyed by frequency counter + hash map. On each access, increment freq, re-heapify. O(log n) per operation. Min-heap of doubly-linked lists (one list per frequency bucket) gives O(1).</p>
    </div>
  </div>
  <div class="cp p-orange">
    <div class="cp-hdr">📏 Cache Capacity Planning</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Metric</th><th>Formula / Target</th></tr></thead>
        <tbody>
          <tr><td>Hit rate</td><td>cache_hits / (hits + misses) → target &gt;90%</td></tr>
          <tr><td>Working set size</td><td>unique_hot_keys × avg_value_bytes</td></tr>
          <tr><td>Memory budget</td><td>JVM/process heap × 30% (leave room for GC, buffers)</td></tr>
          <tr><td>TTL vs eviction</td><td>TTL for correctness; capacity eviction for memory</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">⚡ C7 — Cache Stampede (Thundering Herd)</div>
  <div class="cp-body">
    <p>When a popular key's TTL expires simultaneously for N threads/processes, they all miss the cache and hammer the database together. The database sees a sudden N× spike in traffic. Three mitigations:</p>
    <ul>
      <li>
        <strong>Mutex lock on cache miss</strong>: First miss acquires lock and refreshes; other waiters read the freshly populated value. Problem: lock adds latency for all waiters.
      </li>
      <li>
        <strong>Probabilistic early expiry (XFetch)</strong>: Randomly refresh before TTL expires — probability increases as expiry approaches. Zero extra infrastructure, no lock. Formula: <code>if current_time - ttl * β * log(rand()) > expiry_time → refresh</code>
      </li>
      <li>
        <strong>Background refresh</strong>: Serve stale value immediately; async worker refreshes in background. Requires stale-while-revalidate semantics — acceptable when slight staleness is OK.
      </li>
    </ul>
<div class="cb"><span class="cm">/* Redis SETNX-based mutex for stampede prevention */</span>
<span class="ck">char</span> *<span class="cf">cache_get_with_lock</span>(<span class="ck">const char</span> *key) {
    <span class="ck">char</span> *val = <span class="cf">redis_get</span>(key);
    <span class="ck">if</span> (val) <span class="ck">return</span> val;

    <span class="ck">char</span> lock_key[<span class="cn">128</span>];
    <span class="cf">snprintf</span>(lock_key, <span class="ck">sizeof</span>(lock_key), <span class="cs">"lock:%s"</span>, key);

    <span class="ck">if</span> (<span class="cf">redis_setnx</span>(lock_key, <span class="cs">"1"</span>, <span class="cm">/* ttl */</span><span class="cn">5</span>)) {
        val = <span class="cf">db_fetch</span>(key);
        <span class="cf">redis_set</span>(key, val, TTL);
        <span class="cf">redis_del</span>(lock_key);
    } <span class="ck">else</span> {
        <span class="cm">/* Another thread is refreshing — wait and retry */</span>
        <span class="cf">usleep</span>(<span class="cn">5000</span>);
        val = <span class="cf">redis_get</span>(key);
    }
    <span class="ck">return</span> val;
}</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔥 Redis Hotspot Key Sharding</div>
  <div class="cp-body">
    <p>A single Redis key receiving millions of reads/sec overloads one shard. Solutions:</p>
    <ul>
      <li><strong>Local in-process replica</strong>: Read from Redis once, cache in process for 100 ms. Stale but radically cheaper.</li>
      <li><strong>Key splitting</strong>: Store <code>hotkey:0</code> through <code>hotkey:N-1</code>; reader picks <code>hotkey:{random 0..N-1}</code>. Write to all N. Reads spread across N slots/shards.</li>
      <li><strong>Read replicas</strong>: Route reads to Redis replicas, writes to primary. Redis Cluster supports this natively.</li>
    </ul>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 7 — SCALING
     ══════════════════════════════════════════════════════════ -->
<div id="tab-scaling" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">📈 C8–C10 — Connection Pools, Load Balancing &amp; Horizontal Scaling</div>
  <div class="cp-body">
    <p>Scaling means keeping latency flat as traffic grows. The three levers are: pooling (amortise connection setup cost), load balancing (distribute traffic optimally), and stateless design (allow trivial horizontal replication).</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔌 C8 — Connection Pool Management</div>
  <div class="cp-body">
    <p>Opening a TCP connection + TLS handshake + PostgreSQL auth takes 2–50 ms. A connection pool amortises this by keeping a set of pre-established connections ready to use. Key parameters:</p>
    <table class="t-table">
      <thead><tr><th>Parameter</th><th>Meaning</th><th>Typical Value</th></tr></thead>
      <tbody>
        <tr><td><code>pool_size</code></td><td>Max simultaneous connections</td><td>10–50 per service instance</td></tr>
        <tr><td><code>min_idle</code></td><td>Keep-warm connections</td><td>2–5</td></tr>
        <tr><td><code>acquire_timeout</code></td><td>Wait before returning error</td><td>500 ms – 2 s</td></tr>
        <tr><td><code>max_lifetime</code></td><td>Force recycle (leak prevention)</td><td>30 min</td></tr>
        <tr><td><code>idle_timeout</code></td><td>Close idle conns above min_idle</td><td>5–10 min</td></tr>
      </tbody>
    </table>
    <div class="warn">
      <strong>Pool Exhaustion:</strong> When all connections are busy and a new request arrives, options are: <strong>queue</strong> (wait up to acquire_timeout), <strong>reject immediately</strong> (return 503), or <strong>open a temporary overflow connection</strong> (be careful — can overwhelm the DB). Always emit a metric when queuing occurs; sustained queuing means the pool is undersized.
    </div>
    <p><strong>pgBouncer</strong> operates at the proxy level — thousands of app connections multiplex onto a smaller PostgreSQL connection pool (transaction-mode pooling). Reduces PostgreSQL's backend process count from thousands to tens.</p>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">⚖️ C9 — Load Balancing Algorithms</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Algorithm</th><th>How</th><th>Best For</th><th>Avoid When</th></tr></thead>
      <tbody>
        <tr><td><strong>Round Robin</strong></td><td>Request 1 → backend 1, request 2 → backend 2, …</td><td>Homogeneous backends, uniform request duration</td><td>Variable request times (some backends pile up)</td></tr>
        <tr><td><strong>Weighted Round Robin</strong></td><td>Backend with weight 2 gets 2× requests</td><td>Heterogeneous hardware (some servers are more powerful)</td><td>Dynamic load changes</td></tr>
        <tr><td><strong>Least Connections</strong></td><td>Always route to backend with fewest active connections</td><td>Variable request durations (DB queries, uploads)</td><td>Requires tracking active count — adds state to LB</td></tr>
        <tr><td><strong>IP Hash</strong></td><td>hash(client_ip) mod N</td><td>Session stickiness (non-Redis session stores)</td><td>Horizontal scaling changes N → all sessions remapped</td></tr>
        <tr><td><strong>Consistent Hashing</strong></td><td>Virtual nodes on a ring; hash(key) → nearest clockwise node</td><td>Caching layers (Redis cluster), CDN routing</td><td>Very small node counts (variance in distribution)</td></tr>
      </tbody>
    </table>
    <div class="diagram-box">
<span class="dg-amber">Consistent Hashing Ring (3 nodes, 6 virtual nodes):</span>

            0°
            │
    <span class="dg-red">B₁</span>      │      <span class="dg-blue">A₁</span>
  (120°)  ──┼──  (60°)
    <span class="dg-green">C₁</span>      │      <span class="dg-red">B₂</span>
  (180°)    │    (300°)
            │
         <span class="dg-blue">A₂</span>(240°)   <span class="dg-green">C₂</span>(320°)

<span class="dg-gray">hash("user:42") = 180° → nearest clockwise = C₁</span>
<span class="dg-gray">When node C is removed: only C's keys move to A; A,B unaffected.</span>
<span class="dg-gray">Traditional modulo: ALL keys remap when N changes.</span>
    </div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🌐 C10 — Stateless Horizontal Scaling</div>
  <div class="cp-body">
    <p>The golden rule: <strong>no instance-local state</strong>. If you can kill any instance and restart it on a different host without losing data, the service is stateless and horizontally scalable.</p>
    <table class="t-table">
      <thead><tr><th>State Type</th><th>Externalise To</th><th>Note</th></tr></thead>
      <tbody>
        <tr><td>User sessions</td><td>Redis (with TTL)</td><td>Session ID in cookie; data in Redis</td></tr>
        <tr><td>File uploads / blobs</td><td>S3 / object storage</td><td>Never write to local disk in stateless service</td></tr>
        <tr><td>Rate limit counters</td><td>Redis INCR + EXPIRE</td><td>Sliding window or token bucket in Redis</td></tr>
        <tr><td>Distributed locks</td><td>Redis SET NX EX / Redlock</td><td>For leader election or single-writer guarantees</td></tr>
        <tr><td>Job queues</td><td>Redis Streams, SQS, Kafka</td><td>Workers are stateless consumers</td></tr>
      </tbody>
    </table>
    <div class="ins">
      <strong>Idempotency Pattern:</strong> Every mutating operation should be idempotent — safe to retry without double-effects. Use a client-generated <code>idempotency_key</code> (UUID) stored in the DB with a unique constraint. On retry, the server detects the duplicate key and returns the original result without re-processing.
    </div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 8 — C IMPLEMENTATION
     ══════════════════════════════════════════════════════════ -->
<div id="tab-impl" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🔧 Complete C Implementations</div>
  <div class="cp-body">All examples compile on Linux with <code>gcc -std=c11 -O2 -lpthread</code>. The epoll server requires Linux ≥ 2.6.27.</div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">1️⃣ Thread Pool with Work Queue</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;pthread.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdlib.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>

<span class="ck">#define</span> POOL_SIZE  <span class="cn">8</span>
<span class="ck">#define</span> QUEUE_CAP  <span class="cn">1024</span>

<span class="ck">typedef void</span> (*Task)(<span class="ck">void</span> *);

<span class="ck">typedef struct</span> {
    Task   fn;
    <span class="ck">void</span>  *arg;
} WorkItem;

<span class="ck">typedef struct</span> {
    WorkItem          queue[QUEUE_CAP];
    <span class="ck">int</span>               head, tail, count;
    <span class="ck">pthread_mutex_t</span>   lock;
    <span class="ck">pthread_cond_t</span>    not_empty;
    <span class="ck">pthread_cond_t</span>    not_full;
    <span class="ck">int</span>               shutdown;
    <span class="ck">pthread_t</span>         threads[POOL_SIZE];
} ThreadPool;

<span class="ck">static void</span> *<span class="cf">worker</span>(<span class="ck">void</span> *arg) {
    ThreadPool *p = arg;
    <span class="ck">while</span> (<span class="cn">1</span>) {
        <span class="cf">pthread_mutex_lock</span>(<span class="cv">&amp;p</span>->lock);
        <span class="ck">while</span> (p->count == <span class="cn">0</span> &amp;&amp; !p->shutdown)
            <span class="cf">pthread_cond_wait</span>(<span class="cv">&amp;p</span>->not_empty, <span class="cv">&amp;p</span>->lock);
        <span class="ck">if</span> (p->shutdown &amp;&amp; p->count == <span class="cn">0</span>) {
            <span class="cf">pthread_mutex_unlock</span>(<span class="cv">&amp;p</span>->lock);
            <span class="ck">break</span>;
        }
        WorkItem w = p->queue[p->head];
        p->head = (p->head + <span class="cn">1</span>) % QUEUE_CAP;
        p->count--;
        <span class="cf">pthread_cond_signal</span>(<span class="cv">&amp;p</span>->not_full);
        <span class="cf">pthread_mutex_unlock</span>(<span class="cv">&amp;p</span>->lock);
        w.fn(w.arg);
    }
    <span class="ck">return</span> <span class="cv">NULL</span>;
}

ThreadPool *<span class="cf">pool_create</span>(<span class="ck">void</span>) {
    ThreadPool *p = <span class="cf">calloc</span>(<span class="cn">1</span>, <span class="ck">sizeof</span>(*p));
    <span class="cf">pthread_mutex_init</span>(<span class="cv">&amp;p</span>->lock, <span class="cv">NULL</span>);
    <span class="cf">pthread_cond_init</span>(<span class="cv">&amp;p</span>->not_empty, <span class="cv">NULL</span>);
    <span class="cf">pthread_cond_init</span>(<span class="cv">&amp;p</span>->not_full, <span class="cv">NULL</span>);
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i &lt; POOL_SIZE; i++)
        <span class="cf">pthread_create</span>(<span class="cv">&amp;p</span>->threads[i], <span class="cv">NULL</span>, worker, p);
    <span class="ck">return</span> p;
}

<span class="ck">int</span> <span class="cf">pool_submit</span>(ThreadPool *p, Task fn, <span class="ck">void</span> *arg) {
    <span class="cf">pthread_mutex_lock</span>(<span class="cv">&amp;p</span>->lock);
    <span class="ck">while</span> (p->count == QUEUE_CAP)           <span class="cm">/* backpressure */</span>
        <span class="cf">pthread_cond_wait</span>(<span class="cv">&amp;p</span>->not_full, <span class="cv">&amp;p</span>->lock);
    p->queue[p->tail] = (WorkItem){fn, arg};
    p->tail = (p->tail + <span class="cn">1</span>) % QUEUE_CAP;
    p->count++;
    <span class="cf">pthread_cond_signal</span>(<span class="cv">&amp;p</span>->not_empty);
    <span class="cf">pthread_mutex_unlock</span>(<span class="cv">&amp;p</span>->lock);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">2️⃣ epoll Edge-Triggered Event Loop</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;sys/epoll.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;sys/socket.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;netinet/in.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;fcntl.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;unistd.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;errno.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>

<span class="ck">#define</span> MAX_EVENTS <span class="cn">256</span>
<span class="ck">#define</span> PORT       <span class="cn">8080</span>

<span class="ck">static void</span> <span class="cf">set_nonblocking</span>(<span class="ck">int</span> fd) {
    <span class="cf">fcntl</span>(fd, F_SETFL, <span class="cf">fcntl</span>(fd, F_GETFL, <span class="cn">0</span>) | O_NONBLOCK);
}

<span class="ck">static void</span> <span class="cf">handle_client</span>(<span class="ck">int</span> epfd, <span class="ck">int</span> cfd) {
    <span class="ck">char</span> buf[<span class="cn">4096</span>];
    <span class="ck">while</span> (<span class="cn">1</span>) {                             <span class="cm">/* drain until EAGAIN (ET) */</span>
        <span class="ck">ssize_t</span> n = <span class="cf">read</span>(cfd, buf, <span class="ck">sizeof</span>(buf));
        <span class="ck">if</span> (n == -<span class="cn">1</span>) {
            <span class="ck">if</span> (errno == EAGAIN || errno == EWOULDBLOCK) <span class="ck">break</span>;
            <span class="cf">perror</span>(<span class="cs">"read"</span>); <span class="cf">close</span>(cfd); <span class="ck">return</span>;
        }
        <span class="ck">if</span> (n == <span class="cn">0</span>) { <span class="cf">close</span>(cfd); <span class="ck">return</span>; }  <span class="cm">/* EOF */</span>
        <span class="cf">write</span>(cfd, buf, n);                   <span class="cm">/* echo */</span>
    }
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
    <span class="ck">int</span> lfd = <span class="cf">socket</span>(AF_INET, SOCK_STREAM, <span class="cn">0</span>);
    <span class="ck">int</span> opt = <span class="cn">1</span>;
    <span class="cf">setsockopt</span>(lfd, SOL_SOCKET, SO_REUSEADDR, <span class="cv">&amp;opt</span>, <span class="ck">sizeof</span>(opt));
    <span class="ck">struct</span> sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = INADDR_ANY,
        .sin_port = <span class="cf">htons</span>(PORT)
    };
    <span class="cf">bind</span>(lfd, (<span class="ck">struct</span> sockaddr *)&amp;addr, <span class="ck">sizeof</span>(addr));
    <span class="cf">listen</span>(lfd, SOMAXCONN);
    <span class="cf">set_nonblocking</span>(lfd);

    <span class="ck">int</span> epfd = <span class="cf">epoll_create1</span>(EPOLL_CLOEXEC);
    <span class="ck">struct</span> epoll_event ev = { .events = EPOLLIN, .data.fd = lfd };
    <span class="cf">epoll_ctl</span>(epfd, EPOLL_CTL_ADD, lfd, <span class="cv">&amp;ev</span>);

    <span class="ck">struct</span> epoll_event events[MAX_EVENTS];
    <span class="ck">for</span> (;;) {
        <span class="ck">int</span> n = <span class="cf">epoll_wait</span>(epfd, events, MAX_EVENTS, <span class="cn">-1</span>);
        <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i &lt; n; i++) {
            <span class="ck">if</span> (events[i].data.fd == lfd) {
                <span class="ck">int</span> cfd = <span class="cf">accept</span>(lfd, <span class="cv">NULL</span>, <span class="cv">NULL</span>);
                <span class="cf">set_nonblocking</span>(cfd);
                ev.events   = EPOLLIN | EPOLLET;
                ev.data.fd  = cfd;
                <span class="cf">epoll_ctl</span>(epfd, EPOLL_CTL_ADD, cfd, <span class="cv">&amp;ev</span>);
            } <span class="ck">else</span> {
                <span class="cf">handle_client</span>(epfd, events[i].data.fd);
            }
        }
    }
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">3️⃣ Atomic Reference Counter (stdatomic.h)</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;stdatomic.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;stdlib.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;assert.h&gt;</span>

<span class="ck">typedef struct</span> {
    <span class="ck">atomic_int</span>  refcount;
    <span class="ck">char</span>        data[<span class="cn">256</span>];
} SharedBuffer;

SharedBuffer *<span class="cf">buf_new</span>(<span class="ck">const char</span> *src) {
    SharedBuffer *b = <span class="cf">malloc</span>(<span class="ck">sizeof</span>(*b));
    <span class="cf">atomic_init</span>(<span class="cv">&amp;b</span>->refcount, <span class="cn">1</span>);
    <span class="cf">snprintf</span>(b->data, <span class="ck">sizeof</span>(b->data), <span class="cs">"%s"</span>, src);
    <span class="ck">return</span> b;
}

SharedBuffer *<span class="cf">buf_retain</span>(SharedBuffer *b) {
    <span class="cf">atomic_fetch_add_explicit</span>(<span class="cv">&amp;b</span>->refcount, <span class="cn">1</span>, memory_order_relaxed);
    <span class="ck">return</span> b;
}

<span class="ck">void</span> <span class="cf">buf_release</span>(SharedBuffer *b) {
    <span class="cm">/* Release store pairs with acquire load in last retainer */</span>
    <span class="ck">if</span> (<span class="cf">atomic_fetch_sub_explicit</span>(<span class="cv">&amp;b</span>->refcount, <span class="cn">1</span>, memory_order_release) == <span class="cn">1</span>) {
        <span class="cf">atomic_thread_fence</span>(memory_order_acquire);
        <span class="cf">free</span>(b);
    }
}

<span class="cm">/* Lock-free CAS retry loop */</span>
<span class="ck">static atomic_int</span> global_seq = <span class="cn">0</span>;

<span class="ck">int</span> <span class="cf">increment_if_even</span>(<span class="ck">void</span>) {
    <span class="ck">int</span> cur = <span class="cf">atomic_load_explicit</span>(<span class="cv">&amp;global_seq</span>, memory_order_relaxed);
    <span class="ck">do</span> {
        <span class="ck">if</span> (cur % <span class="cn">2</span> != <span class="cn">0</span>) <span class="ck">return</span> <span class="cn">0</span>;   <span class="cm">/* odd — give up */</span>
    } <span class="ck">while</span> (!<span class="cf">atomic_compare_exchange_weak_explicit</span>(
        <span class="cv">&amp;global_seq</span>, <span class="cv">&amp;cur</span>, cur + <span class="cn">1</span>,
        memory_order_acq_rel, memory_order_relaxed));
    <span class="ck">return</span> <span class="cn">1</span>;
}</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">4️⃣ LRU Cache — Hash Map + Doubly-Linked List</div>
  <div class="cp-body">
<div class="cb"><span class="ck">#include</span> <span class="cs">&lt;stdlib.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>

<span class="ck">#define</span> CACHE_CAP  <span class="cn">128</span>
<span class="ck">#define</span> HT_SIZE    <span class="cn">257</span>   <span class="cm">/* prime */</span>

<span class="ck">typedef struct</span> LRUNode {
    <span class="ck">char</span>           key[<span class="cn">64</span>];
    <span class="ck">long</span>           value;
    <span class="ck">struct</span> LRUNode *prev, *next;
    <span class="ck">struct</span> LRUNode *ht_next;  <span class="cm">/* hash table chaining */</span>
} LRUNode;

<span class="ck">typedef struct</span> {
    LRUNode  *ht[HT_SIZE];
    LRUNode   head, tail;    <span class="cm">/* sentinels */</span>
    <span class="ck">int</span>       size, cap;
} LRUCache;

<span class="ck">static unsigned</span> <span class="cf">hash_key</span>(<span class="ck">const char</span> *k) {
    <span class="ck">unsigned</span> h = <span class="cn">5381</span>;
    <span class="ck">while</span> (*k) h = h * <span class="cn">33</span> ^ (<span class="ck">unsigned char</span>)*k++;
    <span class="ck">return</span> h % HT_SIZE;
}

<span class="ck">static void</span> <span class="cf">list_remove</span>(LRUNode *n) {
    n->prev->next = n->next;
    n->next->prev = n->prev;
}

<span class="ck">static void</span> <span class="cf">list_push_front</span>(LRUCache *c, LRUNode *n) {
    n->next = c->head.next;
    n->prev = <span class="cv">&amp;c</span>->head;
    c->head.next->prev = n;
    c->head.next = n;
}

<span class="ck">void</span> <span class="cf">lru_init</span>(LRUCache *c, <span class="ck">int</span> cap) {
    <span class="cf">memset</span>(c, <span class="cn">0</span>, <span class="ck">sizeof</span>(*c));
    c->cap = cap;
    c->head.next = <span class="cv">&amp;c</span>->tail;
    c->tail.prev = <span class="cv">&amp;c</span>->head;
}

<span class="ck">long</span> <span class="cf">lru_get</span>(LRUCache *c, <span class="ck">const char</span> *key) {
    LRUNode *n = c->ht[<span class="cf">hash_key</span>(key)];
    <span class="ck">for</span> (; n; n = n->ht_next)
        <span class="ck">if</span> (<span class="cf">strcmp</span>(n->key, key) == <span class="cn">0</span>) {
            <span class="cf">list_remove</span>(n);
            <span class="cf">list_push_front</span>(c, n);
            <span class="ck">return</span> n->value;
        }
    <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* miss */</span>
}

<span class="ck">void</span> <span class="cf">lru_put</span>(LRUCache *c, <span class="ck">const char</span> *key, <span class="ck">long</span> val) {
    <span class="cm">/* Evict LRU if at capacity */</span>
    <span class="ck">if</span> (c->size == c->cap) {
        LRUNode *lru = c->tail.prev;
        <span class="cf">list_remove</span>(lru);
        <span class="cm">/* remove from hash table */</span>
        <span class="ck">unsigned</span> h = <span class="cf">hash_key</span>(lru->key);
        LRUNode **pp = <span class="cv">&amp;c</span>->ht[h];
        <span class="ck">while</span> (*pp != lru) pp = &(*pp)->ht_next;
        *pp = lru->ht_next;
        <span class="cf">free</span>(lru);
        c->size--;
    }
    LRUNode *n = <span class="cf">calloc</span>(<span class="cn">1</span>, <span class="ck">sizeof</span>(*n));
    <span class="cf">strncpy</span>(n->key, key, <span class="ck">sizeof</span>(n->key) - <span class="cn">1</span>);
    n->value = val;
    <span class="cf">list_push_front</span>(c, n);
    <span class="ck">unsigned</span> h = <span class="cf">hash_key</span>(key);
    n->ht_next = c->ht[h];
    c->ht[h] = n;
    c->size++;
}</div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 9 — LABS & CHECKLIST
     ══════════════════════════════════════════════════════════ -->
<div id="tab-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 1 — Thread Pool Benchmark: Thread-per-Request vs Pool vs Event Loop</div>
  <div class="lab-body">
    <p>Build three versions of an echo server and compare throughput and latency under 10K concurrent connections using <code>wrk</code> or <code>ab</code>.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write <code>server_threaded.c</code>: accept loop spawns <code>pthread_create</code> for each connection. Use <code>pthread_detach</code> to avoid join overhead.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write <code>server_pool.c</code>: single accept thread enqueues connections to the ThreadPool from this module. Pool has POOL_SIZE=8 workers.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write <code>server_epoll.c</code>: single-threaded epoll event loop, edge-triggered, non-blocking. Handles reads in the same loop.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Stress test: <code>wrk -t4 -c10000 -d30s http://localhost:8080/</code>. Record req/sec, latency p50/p99, and CPU utilisation (<code>pidstat</code>).</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Increase connection count to 50K. Observe where thread-per-request fails (<code>ENOMEM</code>, or scheduler thrash visible in <code>htop</code>).</div></div>
    <div class="lab-step"><div class="sn">6</div><div>Expected result: epoll handles 50K with ~1% CPU idle; threaded crashes or hits ulimit around 4–8K threads depending on stack size.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 2 — Lock-Free Counter vs Mutex Counter Micro-Benchmark</div>
  <div class="lab-body">
    <p>Measure the performance difference between a mutex-protected counter and an atomic counter under high contention.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write <code>bench_counter.c</code>: two versions of a global counter incremented 10M times across 16 threads.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Version A: <code>pthread_mutex_t</code> wrapping <code>counter++</code></div></div>
    <div class="lab-step"><div class="sn">3</div><div>Version B: <code>atomic_fetch_add(&amp;counter, 1, memory_order_relaxed)</code></div></div>
    <div class="lab-step"><div class="sn">4</div><div>Compile: <code>gcc -O2 -std=c11 bench_counter.c -lpthread -o bench</code>. Run 5× and average. Expected: atomic 3–10× faster.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Add a third version: per-thread counter (no sharing), sum at the end. This shows the theoretical maximum — eliminates cache line bouncing entirely.</div></div>
    <div class="lab-step"><div class="sn">6</div><div>Explain the result in terms of <strong>cache coherence traffic</strong>: each atomic increment on a shared cache line triggers an MESI invalidation broadcast to all cores holding the line.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 3 — In-Process LRU Cache with Thread Safety</div>
  <div class="lab-body">
    <p>Extend the LRU cache from the C Implementation tab to be thread-safe, then measure hit rate under a Zipf-distributed workload (80/20 rule).</p>
    <div class="lab-step"><div class="sn">1</div><div>Add a <code>pthread_rwlock_t</code> to the <code>LRUCache</code> struct. Protect <code>lru_get</code> with rdlock and <code>lru_put</code> with wrlock.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write a Zipf key generator: key = <code>rand() % (n * zipf_skew)</code> where lower keys are accessed more often. Use 1000 unique keys.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Spawn 8 threads, each performing 1M get/put operations. Count hits and misses with atomic counters.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Vary cache capacity (32, 64, 128, 256 entries). Plot hit rate vs capacity. Observe the "knee" where doubling capacity no longer meaningfully improves hit rate.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Profile with <code>perf stat</code>: compare cache-miss events at different capacities. Observe L1/L2 hit rates alongside LRU hit rates.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 4 — Consistent Hashing Implementation</div>
  <div class="lab-body">
    <p>Implement a consistent hash ring in C and measure key redistribution when adding/removing nodes.</p>
    <div class="lab-step"><div class="sn">1</div><div>Represent the ring as a sorted array of <code>{hash_value, node_id}</code> pairs. Use 150 virtual nodes per physical node (improves balance). Hash function: <code>fnv1a(node_name + "_vnode_" + i)</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement <code>ring_add_node(ring, "node1")</code> and <code>ring_remove_node(ring, "node1")</code> — insert/delete 150 entries, keeping array sorted (insertion sort or <code>qsort</code>).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Implement <code>ring_get_node(ring, key)</code>: hash the key, binary-search the sorted array for the nearest clockwise entry.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Generate 100K random keys. Assign each to a 3-node ring. Add a 4th node. Count how many keys moved to the new node. Expected: ~25% (100K / 4). Verify.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Compare with modulo hashing: same 100K keys on 3→4 nodes. Count remapped keys. Expected: ~75% remapped (traditional modulo). Consistent hashing wins.</div></div>
  </div>
</div>

<div class="sep"></div>
<div class="cp-hdr" style="background:linear-gradient(90deg,#f59e0b,#f97316);color:#fff;padding:.6rem 1.1rem;border-radius:8px 8px 0 0;font-weight:700;">✅ Phase 4 Completion Checklist</div>
<div style="background:#fffbeb;border:1px solid #f59e0b;border-top:none;border-radius:0 0 8px 8px;padding:1rem;">
  <div class="cl-section">Threading Models</div>
  <ul class="cl">
    <li>Can explain thread-per-request memory/scheduling cost at 10K connections</li>
    <li>Can implement a bounded thread pool with mutex + condvar work queue in C</li>
    <li>Understand event loop model: single thread, non-blocking I/O, epoll notification</li>
    <li>Know when to use green threads (Go/Rust) vs explicit thread pools</li>
  </ul>
  <div class="cl-section">Synchronization Primitives</div>
  <ul class="cl">
    <li>Can choose between mutex, RW lock, semaphore, condvar for a given use case</li>
    <li>Know the deadlock recipe and how to prevent it with lock ordering</li>
    <li>Always wrap pthread_cond_wait in a while loop (spurious wakeup guard)</li>
    <li>Understand spinlock trade-offs: only for sub-100ns critical sections on SMP</li>
  </ul>
  <div class="cl-section">Lock-Free Programming</div>
  <ul class="cl">
    <li>Can explain CAS semantics: atomically read, compare, conditionally swap</li>
    <li>Know the ABA problem and two mitigations (tagged pointers, hazard pointers)</li>
    <li>Can use <code>stdatomic.h</code>: atomic_load/store/fetch_add/compare_exchange</li>
    <li>Understand memory ordering: relaxed vs acquire/release vs seq_cst</li>
  </ul>
  <div class="cl-section">I/O Multiplexing</div>
  <ul class="cl">
    <li>Know select/poll/epoll/io_uring evolution and O(n)→O(1) improvement</li>
    <li>Can implement an epoll edge-triggered event loop in C from scratch</li>
    <li>Understand ET vs LT: ET requires reading until EAGAIN, LT re-notifies</li>
    <li>Know io_uring ring buffer design and why it reduces syscall overhead</li>
    <li>Can explain why 10K threads fail (stack, context switch cost)</li>
  </ul>
  <div class="cl-section">Caching</div>
  <ul class="cl">
    <li>Can implement LRU cache with O(1) get/put using doubly-linked list + hash map</li>
    <li>Understand LFU vs LRU trade-offs for different access distributions</li>
    <li>Can explain cache stampede and implement mutex-lock or XFetch mitigation</li>
    <li>Know Redis hotspot key sharding strategies (key splitting, local replica)</li>
  </ul>
  <div class="cl-section">Scaling</div>
  <ul class="cl">
    <li>Know pgBouncer transaction-mode pooling and when pool exhaustion triggers</li>
    <li>Can compare round-robin, least-conn, and consistent hashing for a use case</li>
    <li>Understand consistent hashing: O(K/N) key redistribution vs O(K) for modulo</li>
    <li>Can design a stateless service: externalise sessions, use idempotency keys</li>
  </ul>
</div>

<div class="mod-nav">
  <a href="/learning/backend/m09-auth-jwt/" class="nb sec">← M09 Auth &amp; JWT</a>
  <a href="/learning/backend/" class="nb sec">↑ Roadmap</a>
  <a href="/learning/backend/m13-messaging/" class="nb">M13 Messaging →</a>
</div>

</div>
</div><!-- .mod-wrap -->

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}
</script>
