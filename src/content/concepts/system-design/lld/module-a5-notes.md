---
title: "Module A5 — Concurrency in LLD (Notes)"
description: "System Design Roadmap › LLD Hub › Module A5 › Full Notes Module A5 — Concurrency in LLD Complete reference notes · Track A: LLD · Week 8 Java Memory Model Locks & Semaphores…"
domain: system-design
track: system-design-lld
order: 11
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a5-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero" style="--ch-1:#7c6fff;--ch-2:#00d4aa;">
  <div class="breadcrumb">
<a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
<span class="separator">›</span>
<a href="/learning/system-design/lld/">LLD Hub</a>
<span class="separator">›</span>
<a href="/learning/system-design/lld/module-a5-concurrency/">Module A5</a>
<span class="separator">›</span>
<span class="current">Full Notes</span>
  </div>
  <h1>Module A5 — Concurrency in LLD</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Week 8</p>
  <div class="hero-stats">
<span class="stat-badge">Java Memory Model</span>
<span class="stat-badge">Locks & Semaphores</span>
<span class="stat-badge">Producer-Consumer</span>
<span class="stat-badge">Thread Pool</span>
<span class="stat-badge">Rate Limiter</span>
  </div>
</div>
<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a5-concurrency/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(124,111,255,0.1);border:1px solid rgba(124,111,255,0.3);color:#7c6fff;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>

# Module A5 — Concurrency in LLD
## System Design Mastery Course | Track A: LLD | Week 8

---

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** A — Low-Level Design (LLD)  
**Prerequisites:** Module A4 (Behavioral Patterns)  
**Goal:** Master concurrent programming primitives and apply them to real LLD problems. This is the module that separates junior engineers from seniors in interviews — most candidates know the patterns; few know how to make them thread-safe.

### Learning Objectives
- Understand Java's memory model: visibility, atomicity, happens-before
- Master synchronization primitives: synchronized, volatile, locks, semaphores
- Implement classic concurrency patterns: Producer-Consumer, Reader-Writer, Thread Pool
- Apply concurrency correctly to real LLD problems
- Identify and fix deadlocks, race conditions, and starvation

### Module Structure

| Topic | Core Problem Solved |
|-------|-------------------|
| Java Memory Model | Why threads see stale data |
| Synchronization Primitives | Building blocks for thread safety |
| ReentrantLock & Conditions | Fine-grained coordination |
| Semaphore | Limiting concurrent access |
| Producer-Consumer | Decoupled async processing |
| Reader-Writer Lock | Concurrent reads, exclusive writes |
| Thread Pool | Managing worker threads |
| Rate Limiter | Token bucket / leaky bucket |
| Projects | Parking Lot, Pub/Sub Queue |

---

## 1. Java Memory Model (JMM)

### The Problem: Visibility + Atomicity

```java
// Without proper synchronization — BROKEN in two ways
class BrokenCounter {
    private int count = 0;  // NOT thread-safe

    public void increment() { count++; }  // NOT atomic!
    public int  getCount()  { return count; }
}

// Thread 1 and Thread 2 each call increment() 500 times
// Expected: 1000.  Actual: anything 500–1000 (lost updates)
```

### Why `count++` is NOT Atomic
```
count++  =  THREE bytecode instructions:
  GETFIELD  — read count from memory into register
  IADD 1    — add 1 to register
  PUTFIELD  — write register back to memory

Race condition:
  Thread 1 reads: 5
  Thread 2 reads: 5    ← both see same value before either writes
  Thread 1 writes: 6
  Thread 2 writes: 6   ← Thread 1's increment is LOST
  Result: 6 instead of 7
```

### The `volatile` Keyword

```java
class StopFlag {
    private volatile boolean running = true;  // volatile: visibility guaranteed

    public void stop() {
        running = false;  // Immediately visible to all threads
    }

    public void run() {
        while (running) {   // Always reads from main memory, not CPU cache
            doWork();
        }
    }
}
```

**volatile guarantees:**
- ✅ Visibility: write immediately flushed to main memory; read always from main memory
- ✅ Ordering: establishes happens-before relationship
- ❌ NOT atomic: `count++` is still unsafe with volatile alone

**When to use volatile:**
✅ Single writer, multiple readers  
✅ Boolean flags: `running`, `shutdown`, `initialized`  
✅ Double-checked locking guard variable  
❌ Compound operations (read-modify-write, check-then-act)

---

## 2. Synchronization Primitives

### `synchronized` — Intrinsic Lock

```java
class ThreadSafeCounter {
    private int count = 0;

    public synchronized void increment() {
        count++;  // Only one thread executes at a time
    }

    public synchronized int getCount() {
        return count;  // Also synchronized — ensures visibility
    }

    // Block-level — more granular than method-level
    public void incrementIfPositive(int delta) {
        synchronized (this) {
            if (count > 0) count += delta;
        }
    }
}
```

### `ReentrantLock` — Explicit Lock

```java
class BankAccount {
    private double balance;
    private final ReentrantLock lock = new ReentrantLock();

    public void deposit(double amount) {
        lock.lock();
        try {
            balance += amount;
        } finally {
            lock.unlock();  // ALWAYS in finally — releases even on exception
        }
    }

    // tryLock — non-blocking attempt
    public boolean tryDeposit(double amount) {
        if (lock.tryLock()) {
            try {
                balance += amount;
                return true;
            } finally {
                lock.unlock();
            }
        }
        return false;  // Lock held by another thread
    }

    // tryLock with timeout
    public boolean tryDepositTimeout(double amount, long ms)
            throws InterruptedException {
        if (lock.tryLock(ms, TimeUnit.MILLISECONDS)) {
            try {
                balance += amount;
                return true;
            } finally {
                lock.unlock();
            }
        }
        return false;
    }
}
```

### `synchronized` vs `ReentrantLock`

| Feature | synchronized | ReentrantLock |
|---------|-------------|---------------|
| Syntax | Language keyword | Java class |
| Try-lock (non-blocking) | ❌ | ✅ `tryLock()` |
| Timeout | ❌ | ✅ `tryLock(ms, unit)` |
| Interruptible | ❌ | ✅ `lockInterruptibly()` |
| Multiple conditions | ❌ One: wait/notify | ✅ Many: `newCondition()` |
| Fairness | ❌ | ✅ `new ReentrantLock(true)` |
| Auto-release | ✅ (block exit) | ❌ Must call unlock() |

**Rule:** Use `synchronized` for simple cases. Use `ReentrantLock` when you need timeout, interruptibility, multiple conditions, or fairness.

---

## 3. Atomic Operations — Lock-Free

```java
import java.util.concurrent.atomic.*;

class AtomicCounter {
    private final AtomicInteger count = new AtomicInteger(0);

    // All operations atomic via CAS (Compare-And-Swap)
    public void    increment()          { count.incrementAndGet(); }
    public void    decrement()          { count.decrementAndGet(); }
    public int     getCount()           { return count.get(); }
    public int     addAndGet(int delta) { return count.addAndGet(delta); }

    // CAS — update only if current value matches expected
    public boolean compareAndSet(int expected, int update) {
        return count.compareAndSet(expected, update);
    }
}

// AtomicReference — for complex object references
AtomicReference<String> ref = new AtomicReference<>("initial");
ref.compareAndSet("initial", "updated");  // Atomic swap

// LongAdder — better than AtomicLong under HIGH write contention
// Internally stripes (shards) the counter across cells
LongAdder adder = new LongAdder();
adder.increment();        // Writers distributed across cells
long total = adder.sum(); // Sums all cells — slightly stale but fast
```

### When to Use Each
```
AtomicInteger/Long:   Single counter, moderate contention
LongAdder:            Counter, very high write contention (metrics collection)
AtomicReference:      Single reference swap (lock-free stack/queue nodes)
AtomicBoolean:        Flag with CAS semantics
volatile boolean:     Simple flag (single writer, no CAS needed)
```

---

## 4. Semaphore — Bounded Concurrency

```java
class DatabaseConnectionPool {
    private final Semaphore              semaphore;
    private final Queue<Connection>      pool;
    private static final int MAX = 10;

    public DatabaseConnectionPool() {
        semaphore = new Semaphore(MAX, true);  // fair=true: FIFO ordering
        pool = new ConcurrentLinkedQueue<>();
        for (int i = 0; i < MAX; i++) pool.offer(createConnection());
    }

    public Connection acquire() throws InterruptedException {
        semaphore.acquire();   // Blocks if 10 connections already in use
        return pool.poll();    // Should always succeed after semaphore acquired
    }

    public Connection acquire(long timeoutMs) throws InterruptedException {
        if (!semaphore.tryAcquire(timeoutMs, TimeUnit.MILLISECONDS)) {
            throw new TimeoutException("No connection available in " + timeoutMs + "ms");
        }
        return pool.poll();
    }

    public void release(Connection conn) {
        pool.offer(conn);      // Return connection to pool
        semaphore.release();   // Signal that a slot is free
    }
}
```

### Semaphore Mental Model
```
Semaphore(N): N permits available
acquire():    Take one permit — block if 0 available
release():    Return one permit — wake one blocked thread

Typical uses:
  N = 10: DB connection pool
  N = 5:  Rate limit concurrent HTTP calls to third-party
  N = 1:  Binary semaphore (like a mutex, but can be released by different thread)
```

---

## 5. Producer-Consumer with BlockingQueue

```java
class LogPipeline {
    // LinkedBlockingQueue: thread-safe, blocks on put() if full, take() if empty
    private final BlockingQueue<LogEvent> queue =
        new LinkedBlockingQueue<>(1000);  // Bounded — backpressure!
    private volatile boolean running = true;

    // PRODUCER — any application thread
    public void log(String level, String msg) {
        try {
            queue.put(new LogEvent(level, msg, Instant.now()));  // Blocks if full
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public boolean tryLog(String level, String msg) {
        return queue.offer(new LogEvent(level, msg, Instant.now())); // False if full
    }

    // CONSUMER — background thread
    public void startConsumer() {
        Thread t = new Thread(() -> {
            while (running || !queue.isEmpty()) {
                try {
                    // poll with timeout — allows checking 'running' flag
                    LogEvent event = queue.poll(100, TimeUnit.MILLISECONDS);
                    if (event != null) writeToSink(event);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }, "log-consumer");
        t.setDaemon(true);
        t.start();
    }
}
```

### BlockingQueue Implementations

| Type | Capacity | Notes |
|------|----------|-------|
| `ArrayBlockingQueue(n)` | Bounded | One shared lock, fair option |
| `LinkedBlockingQueue(n)` | Optionally bounded | Separate head/tail locks — higher throughput |
| `PriorityBlockingQueue` | Unbounded | Ordered by priority |
| `SynchronousQueue` | Zero | Each put() blocks until take() |
| `DelayQueue` | Unbounded | Elements available after delay |

---

## 6. ReadWriteLock — Concurrent Reads

```java
class ConfigCache {
    private final Map<String, String>   cache  = new HashMap<>();
    private final ReadWriteLock         rwLock = new ReentrantReadWriteLock();
    private final Lock                  rLock  = rwLock.readLock();
    private final Lock                  wLock  = rwLock.writeLock();

    // MULTIPLE threads can read simultaneously
    public String get(String key) {
        rLock.lock();
        try {
            return cache.get(key);
        } finally {
            rLock.unlock();
        }
    }

    // EXCLUSIVE — blocks all readers and other writers
    public void put(String key, String value) {
        wLock.lock();
        try {
            cache.put(key, value);
        } finally {
            wLock.unlock();
        }
    }

    // Double-checked computeIfAbsent
    public String computeIfAbsent(String key, Function<String, String> loader) {
        rLock.lock();                          // Try read first (fast path)
        try {
            String val = cache.get(key);
            if (val != null) return val;
        } finally {
            rLock.unlock();
        }

        wLock.lock();                          // Cache miss — write lock
        try {
            String val = cache.get(key);       // Double-check after write lock
            if (val != null) return val;
            val = loader.apply(key);
            cache.put(key, val);
            return val;
        } finally {
            wLock.unlock();
        }
    }
}
```

### ReadWriteLock Rules
```
Multiple readers:      ✅ Allowed concurrently
Reader + Writer:       ❌ Writer waits for all readers to finish
Multiple writers:      ❌ Exclusive one at a time
Java lock downgrade:   ✅ write→read allowed (acquire read, release write)
Java lock upgrade:     ❌ read→write NOT allowed (deadlock risk)

Use when:  reads >> writes  (config cache, lookup tables, routing tables)
Skip when: writes are frequent (lock overhead not worth it)
```

---

## 7. Condition Variables — Fine-Grained Wait/Signal

```java
class BoundedBuffer<T> {
    private final Object[]       buffer;
    private int                  count = 0, putPos = 0, takePos = 0;
    private final ReentrantLock  lock     = new ReentrantLock();
    private final Condition      notFull  = lock.newCondition();
    private final Condition      notEmpty = lock.newCondition();

    public BoundedBuffer(int capacity) { buffer = new Object[capacity]; }

    public void put(T item) throws InterruptedException {
        lock.lock();
        try {
            while (count == buffer.length) notFull.await();  // ← while, not if!
            buffer[putPos] = item;
            putPos = (putPos + 1) % buffer.length;
            count++;
            notEmpty.signal();   // Wake exactly one waiting consumer
        } finally { lock.unlock(); }
    }

    @SuppressWarnings("unchecked")
    public T take() throws InterruptedException {
        lock.lock();
        try {
            while (count == 0) notEmpty.await();             // ← while, not if!
            T item = (T) buffer[takePos];
            buffer[takePos] = null;
            takePos = (takePos + 1) % buffer.length;
            count--;
            notFull.signal();    // Wake exactly one waiting producer
            return item;
        } finally { lock.unlock(); }
    }
}
```

### Critical Rule: `await()` ALWAYS in a `while` Loop
```java
// WRONG — spurious wakeups break this
if (buffer.isFull()) {
    notFull.await();
}

// CORRECT — always re-check condition after wakeup
while (buffer.isFull()) {
    notFull.await();
}
// WHY: JVM/OS can wake a thread spuriously (no signal was sent).
//      Must always re-check the guard condition after waking.
```

---

## 8. Thread Pool — ExecutorService

```java
class TaskScheduler {
    // Fixed pool: CPU-bound tasks → size = #CPU cores
    private final ExecutorService cpuPool =
        Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

    // Cached pool: short-lived I/O tasks (threads reused/created on demand)
    private final ExecutorService ioPool =
        Executors.newCachedThreadPool();

    // Scheduled pool: periodic / delayed tasks
    private final ScheduledExecutorService scheduler =
        Executors.newScheduledThreadPool(2);

    // Custom pool — full control over all parameters
    private final ThreadPoolExecutor custom = new ThreadPoolExecutor(
        4,                                      // corePoolSize
        16,                                     // maximumPoolSize
        60L, TimeUnit.SECONDS,                  // idle thread keepAlive
        new LinkedBlockingQueue<>(1000),         // bounded work queue
        new ThreadPoolExecutor.CallerRunsPolicy() // rejection policy
    );

    public <T> Future<T> submitCPU(Callable<T> task) {
        return cpuPool.submit(task);
    }

    public void scheduleEvery(Runnable task, long periodMs) {
        scheduler.scheduleAtFixedRate(task, 0, periodMs, TimeUnit.MILLISECONDS);
    }

    public void gracefulShutdown() throws InterruptedException {
        cpuPool.shutdown();
        if (!cpuPool.awaitTermination(30, TimeUnit.SECONDS)) {
            cpuPool.shutdownNow();  // Force after 30s
        }
    }
}
```

### Rejection Policies Compared
```
AbortPolicy (default):   Throw RejectedExecutionException — caller must handle
CallerRunsPolicy:        Caller thread runs task → natural backpressure
DiscardPolicy:           Silently drop → use when loss is acceptable
DiscardOldestPolicy:     Drop oldest queued task, retry submit

Production recommendation: CallerRunsPolicy for most services
(It slows the submitter, signals system is overloaded)
```

---

## 9. Deadlock — Detection, Prevention, Avoidance

### Classic Deadlock Example
```java
// BROKEN — Thread 1: lock(from)→lock(to), Thread 2: lock(to)→lock(from)
void transfer(Account from, Account to, double amount) {
    synchronized (from) {       // Thread 1 holds "from"
        synchronized (to) {     // Thread 2 holds "to" and waits for "from"
            from.debit(amount); // DEADLOCK — circular wait
            to.credit(amount);
        }
    }
}
```

### Fix 1: Consistent Lock Ordering

```java
void transfer(Account from, Account to, double amount) {
    // Always lock the account with the lower ID first
    Account first  = from.getId() < to.getId() ? from : to;
    Account second = from.getId() < to.getId() ? to   : from;

    synchronized (first) {
        synchronized (second) {
            from.debit(amount);
            to.credit(amount);
        }
    }
}
```

### Fix 2: tryLock with Backoff

```java
void transfer(Account from, Account to, double amount) throws Exception {
    while (true) {
        if (from.lock.tryLock(50, TimeUnit.MILLISECONDS)) {
            try {
                if (to.lock.tryLock(50, TimeUnit.MILLISECONDS)) {
                    try {
                        from.debit(amount);
                        to.credit(amount);
                        return;
                    } finally { to.lock.unlock(); }
                }
            } finally { from.lock.unlock(); }
        }
        Thread.sleep((long)(Math.random() * 10)); // Randomised backoff
    }
}
```

### Coffman Conditions — Break Any One to Prevent Deadlock
```
ALL four must hold for deadlock:
  1. Mutual Exclusion:  Resource held exclusively by one thread
  2. Hold and Wait:     Thread holds a resource while waiting for another
  3. No Preemption:     Resources cannot be forcibly taken
  4. Circular Wait:     A cycle in the resource-wait graph

How to break each:
  Circular Wait   → Lock ordering (always acquire in same global order)
  Hold & Wait     → Acquire all locks atomically (tryLock all-or-nothing)
  No Preemption   → tryLock with timeout (release held locks, retry)
```

---

## 10. Rate Limiter — Token Bucket

```java
class TokenBucketRateLimiter {
    private final long   capacity;          // Max burst size
    private final double refillRatePerMs;   // Tokens per millisecond
    private double       tokens;
    private long         lastRefillTime;

    public TokenBucketRateLimiter(long capacity, long requestsPerSecond) {
        this.capacity        = capacity;
        this.refillRatePerMs = requestsPerSecond / 1000.0;
        this.tokens          = capacity;
        this.lastRefillTime  = System.currentTimeMillis();
    }

    private void refill() {
        long now = System.currentTimeMillis();
        tokens = Math.min(capacity, tokens + (now - lastRefillTime) * refillRatePerMs);
        lastRefillTime = now;
    }

    public synchronized boolean tryAcquire() {
        refill();
        if (tokens >= 1) { tokens--; return true; }
        return false;
    }

    public synchronized void acquire() throws InterruptedException {
        while (true) {
            refill();
            if (tokens >= 1) { tokens--; return; }
            long waitMs = (long) Math.ceil((1 - tokens) / refillRatePerMs);
            wait(waitMs);
        }
    }
}

// Per-user rate limiter
class UserRateLimiter {
    private final ConcurrentHashMap<String, TokenBucketRateLimiter> buckets
        = new ConcurrentHashMap<>();
    private final Map<UserTier, Long> tierLimits = Map.of(
        UserTier.FREE,       10L,
        UserTier.PRO,       100L,
        UserTier.ENTERPRISE,1000L
    );

    public boolean tryAcquire(String userId, UserTier tier) {
        TokenBucketRateLimiter limiter = buckets.computeIfAbsent(
            userId,
            k -> new TokenBucketRateLimiter(tierLimits.get(tier) * 10,
                                             tierLimits.get(tier))
        );
        return limiter.tryAcquire();
    }
}
```

### Token Bucket vs Leaky Bucket vs Sliding Window
```
Token Bucket:
  - Tokens accumulate up to burst capacity
  - Allows short bursts (saved tokens)
  - Best for: APIs allowing burst traffic, most HTTP rate limiting

Leaky Bucket:
  - Output rate is constant regardless of input
  - No bursts — smooth rate
  - Best for: network traffic shaping

Sliding Window Counter:
  - Count requests in rolling time window
  - More accurate than fixed window
  - Best for: per-user quotas where accuracy matters
```

---

## 11. ⭐ Project 1 — Thread-Safe Parking Lot

```java
class ParkingLot {
    private final Map<String, ParkingSpot> spots = new ConcurrentHashMap<>();
    private final AtomicInteger availableCar   = new AtomicInteger();
    private final AtomicInteger availableBike  = new AtomicInteger();
    private final AtomicInteger availableTruck = new AtomicInteger();
    private final Semaphore     carSemaphore;
    private final Semaphore     bikeSemaphore;
    private final Semaphore     truckSemaphore;
    private final TokenBucketRateLimiter entryLimiter =
        new TokenBucketRateLimiter(20, 5);  // 5 entries/sec, burst 20

    public ParkingLot(int cars, int bikes, int trucks) {
        carSemaphore   = new Semaphore(cars,   true);
        bikeSemaphore  = new Semaphore(bikes,  true);
        truckSemaphore = new Semaphore(trucks, true);
        availableCar.set(cars);
        availableBike.set(bikes);
        availableTruck.set(trucks);
        initSpots(cars, bikes, trucks);
    }

    public Ticket park(Vehicle vehicle) throws InterruptedException {
        // Rate limit entries
        if (!entryLimiter.tryAcquire()) {
            throw new RateLimitException("Entry rate limit exceeded");
        }

        Semaphore sem = getSemaphore(vehicle.getType());
        sem.acquire();  // Blocks until a spot is free

        ParkingSpot spot = claimSpot(vehicle.getType());
        decrementAvailable(vehicle.getType());

        return new Ticket(UUID.randomUUID().toString(),
                          vehicle, spot, Instant.now());
    }

    public Receipt unpark(Ticket ticket) {
        ParkingSpot spot = ticket.getSpot();
        spot.setOccupied(false);
        spot.setVehicle(null);

        incrementAvailable(ticket.getVehicle().getType());
        getSemaphore(ticket.getVehicle().getType()).release();

        double fee = calculateFee(ticket.getEntryTime(), Instant.now());
        return new Receipt(ticket, fee, Instant.now());
    }

    // CAS-based claiming — no explicit lock needed
    private ParkingSpot claimSpot(String type) {
        for (ParkingSpot spot : spots.values()) {
            if (spot.getType().equals(type)
                    && spot.getOccupied().compareAndSet(false, true)) {
                return spot;  // Atomically claimed
            }
        }
        throw new IllegalStateException("No spot after semaphore acquire — bug!");
    }

    private double calculateFee(Instant entry, Instant exit) {
        long minutes = ChronoUnit.MINUTES.between(entry, exit);
        long billableHours = Math.max(0, (minutes / 60) - 2);  // First 2h free
        return billableHours * 50.0;
    }

    public int available(String type) {
        return switch (type) {
            case "CAR"   -> availableCar.get();
            case "BIKE"  -> availableBike.get();
            case "TRUCK" -> availableTruck.get();
            default      -> 0;
        };
    }
}

class ParkingSpot {
    private final String        type;
    private final int           number;
    private final AtomicBoolean occupied = new AtomicBoolean(false);
    private volatile Vehicle    vehicle;

    public AtomicBoolean getOccupied()           { return occupied; }
    public void          setOccupied(boolean b)  { occupied.set(b); }
    public void          setVehicle(Vehicle v)   { vehicle = v; }
}
```

---

## 12. ⭐ Project 2 — Pub/Sub Message Queue

```java
class MessageQueue<T> {
    private final BlockingQueue<Message<T>>             queue;
    private final ConcurrentHashMap<String,
                  CopyOnWriteArrayList<MessageHandler<T>>> subscribers;
    private final ExecutorService                       dispatchPool;
    private volatile boolean                            running = true;

    public MessageQueue(int capacity, int dispatchThreads) {
        queue        = new LinkedBlockingQueue<>(capacity);
        subscribers  = new ConcurrentHashMap<>();
        dispatchPool = Executors.newFixedThreadPool(dispatchThreads);
        startDispatcher();
    }

    // Thread-safe publish
    public boolean publish(String topic, T payload) {
        return queue.offer(new Message<>(topic, payload, Instant.now()));
    }

    // Thread-safe subscribe — CopyOnWriteArrayList handles concurrent iteration
    public void subscribe(String topic, MessageHandler<T> handler) {
        subscribers.computeIfAbsent(topic, k -> new CopyOnWriteArrayList<>())
                   .add(handler);
    }

    public void unsubscribe(String topic, MessageHandler<T> handler) {
        CopyOnWriteArrayList<MessageHandler<T>> list = subscribers.get(topic);
        if (list != null) list.remove(handler);
    }

    private void startDispatcher() {
        Thread t = new Thread(() -> {
            while (running || !queue.isEmpty()) {
                try {
                    Message<T> msg = queue.poll(100, TimeUnit.MILLISECONDS);
                    if (msg == null) continue;

                    // CopyOnWriteArrayList: safe to iterate while others subscribe
                    CopyOnWriteArrayList<MessageHandler<T>> handlers =
                        subscribers.get(msg.getTopic());
                    if (handlers == null) continue;

                    // Dispatch each handler independently
                    for (MessageHandler<T> handler : handlers) {
                        dispatchPool.submit(() -> {
                            try {
                                handler.handle(msg);
                            } catch (Exception e) {
                                // Isolated: one failing handler doesn't affect others
                                System.err.println("Handler error: " + e.getMessage());
                            }
                        });
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }, "mq-dispatcher");
        t.setDaemon(true);
        t.start();
    }

    public void shutdown() throws InterruptedException {
        running = false;
        dispatchPool.shutdown();
        dispatchPool.awaitTermination(30, TimeUnit.SECONDS);
    }
}
```

---

## 📝 Tasks

### Task 1 — Race Condition Identification
For each snippet, name the bug and write the fix:

```java
// Snippet A — Lazy Singleton
class Config {
    private static Config instance;
    public static Config getInstance() {
        if (instance == null) {           // Bug?
            instance = new Config();
        }
        return instance;
    }
}

// Snippet B — Check-then-act
class TicketSeller {
    private int tickets = 100;
    public boolean sell() {
        if (tickets > 0) {                // Bug?
            tickets--;
            return true;
        }
        return false;
    }
}

// Snippet C — Compound AtomicInteger
AtomicInteger count = new AtomicInteger(0);
public int getAndDoubleIfEven() {
    if (count.get() % 2 == 0) {          // Bug?
        return count.getAndAdd(count.get());
    }
    return count.get();
}

// Snippet D — Visibility
class Worker {
    boolean done = false;
    void finish() { done = true; }
    void run()    { while (!done) work(); } // Bug?
}
```

### Task 2 — Thread-Safe LRU Cache

Implement an `LRUCache` that:
- `get(key)` — O(1), returns -1 if absent
- `put(key, value)` — O(1), evicts LRU entry on capacity exceeded
- Thread-safe under concurrent get/put from multiple threads
- Approach: `LinkedHashMap` + `ReadWriteLock`
- Benchmark: 8 threads × 100k operations, measure throughput vs single-threaded

### Task 3 — Dining Philosophers

Implement the classic problem:
- 5 philosophers, 5 forks shared between adjacent pairs
- Lifecycle: think → pick both forks → eat → put down forks
- Show why naive implementation deadlocks (circular wait)
- Implement two correct solutions:
  1. Lock ordering (odd philosopher picks left first, even picks right first)
  2. Arbitrator pattern (only 4 philosophers allowed to try simultaneously)

### Task 4 — Per-User Rate Limiter

Extend the Token Bucket implementation:
- `tryAcquire(userId, tier)` — per-user bucket
- Tiers: FREE=10/sec, PRO=100/sec, ENTERPRISE=1000/sec
- Evict inactive users after 5 minutes (use `ScheduledExecutorService`)
- Thread-safe: 10,000 concurrent users
- Test: assert no request exceeds its tier's limit under load

### ⭐ Mini Project — Production-Grade Parking Lot

```
Requirements:
  - 3 types: Car (100 spots), Bike (50), Truck (20)
  - 50 concurrent threads simulating arrivals
  - Display board: real-time count (read-heavy, write on every park/unpark)
  - Ticket: vehicleId, spotId, entryTime, UUID
  - Fee: first 2 hours free, ₹50/hour after
  - Entry rate limit: max 5 vehicles/second (Token Bucket)

Thread-safety proof:
  - Zero double-bookings (verify spot never assigned twice)
  - Final available count == initial count (verify no leaks)
  - All entry timestamps valid and ordered
  - Display board reads never block entry/exit

Deliver:
  1. Full Java implementation
  2. JUnit test with 50 threads, assertions on invariants
  3. UML class diagram annotated with synchronization mechanisms
```

---

## 💡 Interview Tips — Concurrency

| Question | Strong Answer |
|----------|--------------|
| "volatile vs synchronized?" | "volatile: visibility only (no caching). synchronized: visibility + atomicity. Use volatile for flags; synchronized/locks for compound ops." |
| "What is a race condition?" | "When program correctness depends on thread timing — outcome varies non-deterministically." |
| "When does ConcurrentHashMap not help?" | "When you need to do a compound operation atomically — e.g., check-then-put. Use computeIfAbsent() or explicit sync." |
| "How to prevent deadlock?" | "Break circular wait: always acquire locks in same global order. Or break hold-and-wait: tryLock with timeout and retry." |
| "AtomicInteger vs synchronized?" | "AtomicInteger uses CAS — lock-free, lower overhead for single variable. synchronized for compound operations or multiple variables that must change together." |
| "What is a spurious wakeup?" | "A thread waking from wait()/await() without being notified — possible in any JVM implementation. Always check the condition in a while loop after waking." |

---

## ✅ Module A5 Completion Checklist

- [ ] Understand JMM: visibility, atomicity, happens-before
- [ ] Know when to use volatile vs synchronized vs AtomicXxx
- [ ] Can implement Producer-Consumer with BlockingQueue from memory
- [ ] Understand ReadWriteLock and when concurrent reads are safe
- [ ] Can implement Semaphore-based bounded pool from memory
- [ ] Know all 4 Coffman conditions + how to break each
- [ ] Can implement Token Bucket rate limiter from memory
- [ ] Understand ExecutorService types: fixed, cached, scheduled, custom
- [ ] Completed Task 1 — Race condition identification and fixes
- [ ] Completed Task 2 — Thread-safe LRU Cache
- [ ] Completed Task 3 — Dining Philosophers (deadlock-free, 2 solutions)
- [ ] Completed Task 4 — Per-user Rate Limiter
- [ ] Completed Mini Project — Production Parking Lot with concurrency proof

**→ When complete: Ready for Track B — High-Level System Design**
