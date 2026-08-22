---
title: "Module A1 Notes — SOLID + OOP + UML"
description: "System Design Roadmap › Module A1 › Full Notes Module A1 — SOLID + OOP + UML Complete reference notes · Track A: LLD · Week 3 5 SOLID Principles 4 OOP Pillars 2 UML Diagrams 1…"
domain: system-design
track: system-design-lld
order: 3
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a1-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero" style="--ch-1:#00e5ff;--ch-2:#7c6fff;">
  <div class="breadcrumb">
    <a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
    <span class="separator">›</span>
    <a href="/learning/system-design/lld/module-a1-solid/">Module A1</a>
    <span class="separator">›</span>
    <span class="current">Full Notes</span>
  </div>
  <h1>Module A1 — SOLID + OOP + UML</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Week 3</p>
  <div class="hero-stats">
    <span class="stat-badge">5 SOLID Principles</span>
    <span class="stat-badge">4 OOP Pillars</span>
    <span class="stat-badge">2 UML Diagrams</span>
    <span class="stat-badge">1 Mini Project</span>
  </div>
</div>
<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a1-solid/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(0,229,255,0.1);border:1px solid rgba(0,229,255,0.3);color:#00e5ff;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>

---

## 🎯 Module Overview

**Duration:** 1 Week &nbsp;|&nbsp; **Track:** A — Low-Level Design (LLD) &nbsp;|&nbsp; **Prerequisites:** Phase 0 complete

**Goal:** Build the design instinct that underpins every one of the 23 patterns you'll learn in Weeks 4–7. SOLID is not a checklist — it's a way of thinking about change.

### Learning Objectives
By the end of Module A1, you will:
- Understand and apply all 5 SOLID principles with real violations and fixes
- Recognise when code violates SOLID and know the exact refactoring needed
- Read and write UML Class diagrams and Sequence diagrams fluently
- Apply OOP pillars (Encapsulation, Abstraction, Inheritance, Polymorphism) deliberately
- Complete the Parking Lot refactoring task — your first full LLD exercise

---

## OOP Foundations — The 4 Pillars

### 🔒 Pillar 1 — Encapsulation
**What it is:** Bundle data + behaviour together. Hide internal state. Expose only what is necessary.

**Bad (no encapsulation):**
```java
class BankAccount {
    public double balance;  // Anyone can set this to anything!
}
account.balance = -99999;  // No validation possible
```

**Good (encapsulated):**
```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        this.balance += amount;
    }

    public double getBalance() { return balance; }
}
```

**Why it matters in SD:** Encapsulation creates stable interfaces. When internals change (e.g., switching from double to BigDecimal for precision), callers don't break.

---

### 🎭 Pillar 2 — Abstraction
**What it is:** Expose WHAT a thing does, hide HOW it does it. Program to interfaces, not implementations.

```java
interface PaymentProcessor {
    boolean process(Payment payment);
}

class StripeProcessor implements PaymentProcessor {
    public boolean process(Payment payment) { /* Stripe API logic */ }
}

class PayPalProcessor implements PaymentProcessor {
    public boolean process(Payment payment) { /* PayPal API logic */ }
}

// Caller doesn't care which processor — just calls process()
PaymentProcessor processor = getProcessor(user.preference);
processor.process(payment);
```

**Interview Tip:** "Programming to an interface" is the foundation of the Strategy, Bridge, and Factory patterns.

---

### 🧬 Pillar 3 — Inheritance
**What it is:** Child class inherits state and behaviour from parent.

**Use inheritance for:** IS-A relationships (Dog IS-A Animal, SavingsAccount IS-A Account)
**Avoid inheritance for:** HAS-A relationships (Car HAS-A Engine — use composition instead)

```java
// IS-A: correct use
abstract class Vehicle {
    protected String licensePlate;
    abstract int getMaxSpeed();
}
class Car extends Vehicle {
    public int getMaxSpeed() { return 180; }
}

// HAS-A: use composition, NOT inheritance
class Car {
    private Engine engine;   // Composition
    private GPS gps;
}
```

**Critical rule:** Favour Composition Over Inheritance. When the parent changes, all children may break.

---

### 🔀 Pillar 4 — Polymorphism
**What it is:** Same interface, different behaviour. One method call, many possible implementations.

```java
// Runtime polymorphism
Shape[] shapes = { new Circle(5), new Rectangle(4, 6) };
for (Shape shape : shapes) {
    System.out.println(shape.area());  // Each calls its own area()
}

// Compile-time polymorphism (overloading)
class Logger {
    void log(String message) { ... }
    void log(String message, Level level) { ... }
    void log(Exception e) { ... }
}
```

---

## The SOLID Principles

### S — Single Responsibility Principle (SRP)
> **"A class should have only one reason to change."**

**Violation:**
```java
class Invoice {
    public double calculateTotal() { ... }    // Reason 1: business logic
    public void saveToDatabase() { ... }      // Reason 2: DB schema
    public void printInvoice() { ... }        // Reason 3: report format
    public void sendEmail() { ... }           // Reason 4: email provider
}
```

**Fix:**
```java
class Invoice          { public double calculateTotal() { ... } }
class InvoiceRepository { public void save(Invoice inv) { ... } }
class InvoicePrinter   { public void print(Invoice inv) { ... } }
class InvoiceEmailer   { public void send(Invoice inv, String email) { ... } }
```

**Interview Tip:** SRP violations are the #1 reason codebases become unmaintainable. Count "reasons to change" — should always be 1.

---

### O — Open/Closed Principle (OCP)
> **"Open for extension, but closed for modification."**

**Violation (if/else on type):**
```java
class DiscountCalculator {
    public double calculate(String customerType, double price) {
        if (customerType.equals("REGULAR")) return price * 0.95;
        if (customerType.equals("PREMIUM")) return price * 0.85;
        // Every new type requires modifying this class!
        return price;
    }
}
```

**Fix (Strategy Pattern):**
```java
interface DiscountStrategy { double apply(double price); }
class RegularDiscount implements DiscountStrategy { public double apply(double p) { return p * 0.95; } }
class PremiumDiscount implements DiscountStrategy { public double apply(double p) { return p * 0.85; } }
// Add VIP: create new class, touch NOTHING else
class VIPDiscount implements DiscountStrategy { public double apply(double p) { return p * 0.60; } }

class DiscountCalculator {
    public double calculate(DiscountStrategy strategy, double price) {
        return strategy.apply(price);
    }
}
```

**Interview Tip:** OCP is directly embodied by the Strategy Pattern (A2) and Template Method (A4).

---

### L — Liskov Substitution Principle (LSP)
> **"Subtypes must be substitutable for their base types without altering program correctness."**

**Violation (Rectangle/Square trap):**
```java
class Square extends Rectangle {
    public void setWidth(int w)  { this.width = w; this.height = w; }
    public void setHeight(int h) { this.width = h; this.height = h; }
}
// testArea(r): r.setWidth(5); r.setHeight(4); assert r.area() == 20;
// FAILS for Square (gives 16)!
```

**Fix:**
```java
interface Shape { int area(); }
class Rectangle implements Shape { ... }
class Square    implements Shape { ... }
// Both honour the Shape contract independently
```

**Interview Tip:** LSP violations appear as `instanceof` checks or `UnsupportedOperationException`. Classic trap: `Penguin extends Bird` (fly() throws!).

---

### I — Interface Segregation Principle (ISP)
> **"Clients should not be forced to depend on interfaces they do not use."**

**Violation:**
```java
interface Worker {
    void work();
    void eat();    // robots don't eat
    void sleep();  // robots don't sleep
}
class RobotWorker implements Worker {
    public void work() { ... }
    public void eat()  { throw new UnsupportedOperationException(); }
    public void sleep(){ throw new UnsupportedOperationException(); }
}
```

**Fix:**
```java
interface Workable { void work(); }
interface Feedable  { void eat(); }
interface Restable  { void sleep(); }

class HumanWorker implements Workable, Feedable, Restable { ... }
class RobotWorker implements Workable { ... }  // Only what it needs
```

---

### D — Dependency Inversion Principle (DIP)
> **"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

**Violation:**
```java
class OrderService {
    private MySQLDatabase database;  // Concrete!
    private EmailService emailer;    // Concrete!

    public OrderService() {
        this.database = new MySQLDatabase();  // Hard-coded
        this.emailer = new EmailService();
    }
}
```

**Fix (Constructor Injection):**
```java
interface OrderRepository    { void save(Order order); }
interface NotificationService { void notify(Order order); }

class OrderService {
    private final OrderRepository    repository;
    private final NotificationService notifier;

    public OrderService(OrderRepository repository, NotificationService notifier) {
        this.repository = repository;
        this.notifier = notifier;
    }
}

// Wiring:
new OrderService(new PostgreSQLRepository(), new SMSNotificationService());
```

**Interview Tip:** DIP is the principle that makes unit testing possible. Without it, you can't mock dependencies.

---

## SOLID Violations Quick-Reference

<div class="table-responsive">
<table class="insight-table">
<thead>
<tr><th>Code Smell</th><th>Principle Violated</th><th>Fix</th></tr>
</thead>
<tbody>
<tr><td>Class with 5+ unrelated methods</td><td>SRP</td><td>Split into focused classes</td></tr>
<tr><td><code>if/else</code> or <code>switch</code> on type</td><td>OCP</td><td>Strategy pattern</td></tr>
<tr><td>Subclass throws <code>UnsupportedOperationException</code></td><td>LSP</td><td>Redesign hierarchy or use composition</td></tr>
<tr><td><code>instanceof</code> checks in polymorphic code</td><td>LSP</td><td>Fix inheritance, use polymorphism properly</td></tr>
<tr><td>Fat interface with 10+ methods</td><td>ISP</td><td>Split into role-specific interfaces</td></tr>
<tr><td><code>new ConcreteClass()</code> inside service</td><td>DIP</td><td>Inject via constructor / DI container</td></tr>
<tr><td>Hard to unit test (can't mock)</td><td>DIP</td><td>Introduce interface, inject dependency</td></tr>
</tbody>
</table>
</div>

---

## UML Reference

### Class Diagram Relationships

```
Association (uses):          A ────────── B
Aggregation (has-a, weak):   A ◇────────── B   (B can exist without A)
Composition (has-a, strong): A ◆────────── B   (B cannot exist without A)
Inheritance (is-a):          A ────────▷ B
Interface Implementation:    A ─ ─ ─ ─ ▷ B    (dashed)
Dependency (transient):      A ─ ─ ─ ─ ─> B
```

Multiplicities: `1` | `0..1` | `*` | `1..*` | `2..5`

### Sequence Diagram Notation

```
Customer     ParkingLot    Floor      Spot
   |              |          |          |
   |──park(car)──>|          |          |
   |              |──findFloor()──>|    |
   |              |          |──findSpot()──>|
   |              |          |          |──reserve()
   |              |          |<──spot──-|
   |              |<──floor──|          |
   |<──ticket─────|          |          |
```

**UML Interview Tips:**
- Always start with a rough class diagram before writing code
- Composition (◆) = strong ownership. Aggregation (◇) = weak relationship
- Never draw a class diagram without multiplicities on relationships

---

## 📝 Interview Tips Summary

<div class="table-responsive">
<table class="insight-table">
<thead>
<tr><th>Principle</th><th>One-liner to say in interview</th><th>Pattern it enables</th></tr>
</thead>
<tbody>
<tr><td><strong>SRP</strong></td><td>"Each class has one reason to change"</td><td>— (foundational)</td></tr>
<tr><td><strong>OCP</strong></td><td>"Open for extension, closed for modification"</td><td>Strategy, Template Method</td></tr>
<tr><td><strong>LSP</strong></td><td>"Subtypes must honour the parent's contract"</td><td>— (prevents bad inheritance)</td></tr>
<tr><td><strong>ISP</strong></td><td>"Many focused interfaces &gt; one fat interface"</td><td>— (enables clean composition)</td></tr>
<tr><td><strong>DIP</strong></td><td>"Depend on abstractions, not concretions"</td><td>Factory, DI containers</td></tr>
</tbody>
</table>
</div>

---

## ✅ Module A1 Completion Checklist

- [ ] Can explain all 5 SOLID principles without notes
- [ ] Can identify SOLID violations in code with specific principle named
- [ ] Can read and draw UML class diagrams with correct relationship symbols
- [ ] Can draw sequence diagrams for multi-object interactions
- [ ] Know the difference between Composition, Aggregation, Association
- [ ] Completed Task 1 — SOLID Violation Hunt (4 snippets fixed)
- [ ] Completed Task 2 — Library UML Class Diagram
- [ ] Completed Task 3 — E-Commerce Sequence Diagram
- [ ] Completed Mini Project — Parking Lot Refactoring (violations listed + code + UML)

**→ When complete: Ready for Module A2 — Creational Design Patterns**

<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="/learning/system-design/lld/module-a1-solid/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(0,229,255,0.1);border:1px solid rgba(0,229,255,0.3);color:#00e5ff;text-decoration:none;font-weight:700;">⚡ Open Interactive Version</a>
  <a href="/learning/system-design/system-design-roadmap/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(30,42,64,0.6);border:1px solid #263450;color:#d4deff;text-decoration:none;font-weight:600;">↑ Back to Roadmap</a>
</div>
