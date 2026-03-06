# Module A1 — SOLID Principles + OOP + UML
## System Design Mastery Course | Track A: LLD | Week 3

---

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** A — Low-Level Design (LLD)  
**Prerequisites:** Phase 0 complete  
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

Before SOLID, you must be crisp on the four OOP pillars. These are not definitions to recite — they are tools to wield.

### Pillar 1 — Encapsulation
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

### Pillar 2 — Abstraction
**What it is:** Expose WHAT a thing does, hide HOW it does it. Program to interfaces, not implementations.

```java
// Abstraction: callers know WHAT, not HOW
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

**Interview Tip:** "Programming to an interface" is the foundation of the Strategy, Bridge, and Factory patterns. Every time you see an interface in LLD, ask: what is being abstracted away?

---

### Pillar 3 — Inheritance
**What it is:** Child class inherits state and behaviour from parent. Enables code reuse and IS-A relationships.

**Use inheritance for:** IS-A relationships (Dog IS-A Animal, SavingsAccount IS-A Account)  
**Avoid inheritance for:** HAS-A relationships (Car HAS-A Engine — use composition instead)

```java
// IS-A: correct use of inheritance
abstract class Vehicle {
    protected String licensePlate;
    abstract int getMaxSpeed();
}

class Car extends Vehicle {
    public int getMaxSpeed() { return 180; }
}

// HAS-A: use composition, NOT inheritance
class Car {
    private Engine engine;   // Composition — Car HAS-A Engine
    private GPS gps;
}
```

**Critical rule:** Favour Composition Over Inheritance. Inheritance creates tight coupling. When the parent changes, all children may break.

---

### Pillar 4 — Polymorphism
**What it is:** Same interface, different behaviour. One method call, many possible implementations.

```java
// Runtime polymorphism
Shape[] shapes = { new Circle(5), new Rectangle(4, 6), new Triangle(3, 4, 5) };

for (Shape shape : shapes) {
    System.out.println(shape.area());  // Each calls its own area()
}
```

**Compile-time polymorphism (overloading):**
```java
class Logger {
    void log(String message) { ... }
    void log(String message, Level level) { ... }
    void log(Exception e) { ... }
}
```

---

## The SOLID Principles

SOLID is an acronym coined by Robert C. Martin (Uncle Bob). Each principle addresses a specific category of design rot.

---

### S — Single Responsibility Principle (SRP)

> **"A class should have only one reason to change."**

One class = one responsibility = one axis of change.

**Violation:**
```java
class Invoice {
    // Responsibility 1: Business logic
    public double calculateTotal() { ... }
    
    // Responsibility 2: Persistence (reason to change: DB schema changes)
    public void saveToDatabase() { ... }
    
    // Responsibility 3: Presentation (reason to change: report format changes)
    public void printInvoice() { ... }
    
    // Responsibility 4: Email (reason to change: email provider changes)
    public void sendEmail() { ... }
}
```

This class has 4 reasons to change. Any change to DB logic forces redeployment of the printing logic. Violation.

**Fix:**
```java
class Invoice {
    public double calculateTotal() { ... }  // Only business logic
}

class InvoiceRepository {
    public void save(Invoice invoice) { ... }  // Only persistence
}

class InvoicePrinter {
    public void print(Invoice invoice) { ... }  // Only printing
}

class InvoiceEmailer {
    public void send(Invoice invoice, String email) { ... }  // Only email
}
```

**Real-world example:** A `UserService` that validates users, sends welcome emails, AND manages sessions violates SRP. Split into `UserValidator`, `WelcomeEmailService`, `SessionManager`.

**Interview Tip:** SRP violations are the #1 reason codebases become unmaintainable. In interviews, when asked "what's wrong with this design?", look for classes doing too many things.

---

### O — Open/Closed Principle (OCP)

> **"Software entities should be open for extension, but closed for modification."**

Add new behaviour without changing existing code. Achieved via abstraction + polymorphism.

**Violation:**
```java
class DiscountCalculator {
    public double calculate(String customerType, double price) {
        if (customerType.equals("REGULAR")) return price * 0.95;
        if (customerType.equals("PREMIUM")) return price * 0.85;
        if (customerType.equals("EMPLOYEE")) return price * 0.70;
        // Every new customer type requires modifying this class!
        return price;
    }
}
```

Every new customer type means modifying (and re-testing) existing code. Violation.

**Fix:**
```java
interface DiscountStrategy {
    double apply(double price);
}

class RegularDiscount implements DiscountStrategy {
    public double apply(double price) { return price * 0.95; }
}

class PremiumDiscount implements DiscountStrategy {
    public double apply(double price) { return price * 0.85; }
}

// To add new customer type: create new class, touch nothing else
class VIPDiscount implements DiscountStrategy {
    public double apply(double price) { return price * 0.70; }
}

class DiscountCalculator {
    public double calculate(DiscountStrategy strategy, double price) {
        return strategy.apply(price);  // Closed for modification
    }
}
```

**Real-world example:** Payment processors. Adding PayTM support should not require changing existing Stripe or PayPal code.

**Interview Tip:** OCP is directly embodied by the Strategy Pattern (Module A2) and Template Method Pattern (Module A4). When you see OCP being applied, a Strategy or Template Method is usually the mechanism.

---

### L — Liskov Substitution Principle (LSP)

> **"Subtypes must be substitutable for their base types without altering program correctness."**

If S is a subtype of T, anywhere you use T, you should be able to use S without breaking anything.

**Violation — the classic Rectangle/Square trap:**
```java
class Rectangle {
    protected int width, height;
    
    public void setWidth(int w) { this.width = w; }
    public void setHeight(int h) { this.height = h; }
    public int area() { return width * height; }
}

class Square extends Rectangle {
    // Square must keep width == height, so it overrides both setters
    public void setWidth(int w) { this.width = w; this.height = w; }
    public void setHeight(int h) { this.width = h; this.height = h; }
}

// Test that works for Rectangle breaks for Square:
void testArea(Rectangle r) {
    r.setWidth(5);
    r.setHeight(4);
    assert r.area() == 20;  // Passes for Rectangle, FAILS for Square (gives 16)
}
```

Square IS-A Rectangle mathematically, but NOT in the OOP sense — it breaks the contract.

**Fix:** Use abstraction instead of inheritance:
```java
interface Shape {
    int area();
}

class Rectangle implements Shape { ... }
class Square implements Shape { ... }
```

**Another common violation:**
```java
class Bird {
    public void fly() { ... }
}

class Penguin extends Bird {
    public void fly() {
        throw new UnsupportedOperationException("Penguins can't fly!");
    }
}
// Any code that calls bird.fly() breaks when given a Penguin!
```

**Interview Tip:** LSP violations often show up as `instanceof` checks or `UnsupportedOperationException` throws. These are code smells that scream "inheritance hierarchy is wrong."

---

### I — Interface Segregation Principle (ISP)

> **"Clients should not be forced to depend on interfaces they do not use."**

Many small, specific interfaces > one large, fat interface.

**Violation:**
```java
interface Worker {
    void work();
    void eat();
    void sleep();
}

class HumanWorker implements Worker {
    public void work() { ... }
    public void eat() { ... }
    public void sleep() { ... }
}

class RobotWorker implements Worker {
    public void work() { ... }
    public void eat() { throw new UnsupportedOperationException(); }  // Robots don't eat!
    public void sleep() { throw new UnsupportedOperationException(); } // Robots don't sleep!
}
```

RobotWorker is forced to implement methods it doesn't need. Violation.

**Fix:**
```java
interface Workable { void work(); }
interface Feedable  { void eat(); }
interface Restable  { void sleep(); }

class HumanWorker implements Workable, Feedable, Restable { ... }
class RobotWorker implements Workable { ... }  // Only what it needs
```

**Real-world example:** Java's `Comparable` vs `Comparator` — two focused interfaces instead of one bloated one. Or Spring's many small callback interfaces (InitializingBean, DisposableBean, etc.)

**Interview Tip:** ISP violations are common in legacy codebases. Look for: classes implementing interface methods that throw `UnsupportedOperationException`, or interfaces with 10+ methods that clients rarely use fully.

---

### D — Dependency Inversion Principle (DIP)

> **"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

> **"Abstractions should not depend on details. Details should depend on abstractions."**

**Violation:**
```java
class OrderService {
    private MySQLDatabase database;  // Depends on concrete class!
    private EmailService emailer;    // Depends on concrete class!
    
    public OrderService() {
        this.database = new MySQLDatabase();  // Hard-coded dependency
        this.emailer = new EmailService();
    }
    
    public void placeOrder(Order order) {
        database.save(order);
        emailer.sendConfirmation(order);
    }
}
// To switch to PostgreSQL or SMS — must modify OrderService!
```

**Fix (using Dependency Injection):**
```java
interface OrderRepository { void save(Order order); }
interface NotificationService { void notify(Order order); }

class OrderService {
    private final OrderRepository repository;       // Depends on abstraction
    private final NotificationService notifier;    // Depends on abstraction
    
    // Dependencies injected from outside (DI)
    public OrderService(OrderRepository repository, NotificationService notifier) {
        this.repository = repository;
        this.notifier = notifier;
    }
    
    public void placeOrder(Order order) {
        repository.save(order);
        notifier.notify(order);
    }
}

// Wiring (done in factory / DI container):
new OrderService(new PostgreSQLRepository(), new SMSNotificationService());
// Or:
new OrderService(new MongoDBRepository(), new EmailNotificationService());
```

**Real-world example:** Spring's @Autowired, @Inject — the DI container manages all dependencies. Your classes declare what they need (interface), Spring provides it.

**Interview Tip:** DIP is the principle that makes unit testing possible. Without it, you can't mock dependencies. In LLD interviews, always inject dependencies via constructor — never instantiate them inside the class.

---

## UML — Unified Modelling Language

Two diagrams you must know cold: Class Diagrams and Sequence Diagrams.

### Class Diagrams

A class diagram shows the static structure: classes, their attributes/methods, and relationships.

**Class notation:**
```
┌──────────────────────────┐
│      ClassName           │  ← Class name (bold/italics for abstract)
├──────────────────────────┤
│ - privateField: Type     │  ← Attributes
│ # protectedField: Type   │     - = private
│ + publicField: Type      │     # = protected
├──────────────────────────┤     + = public
│ + publicMethod(): Type   │  ← Methods
│ - privateMethod(): void  │
└──────────────────────────┘
```

**Relationships (memorise these symbols):**

```
Association (uses):          A ────────── B
                             "A uses B"

Aggregation (has-a, weak):   A ◇────────── B
                             "A has B, B can exist without A"
                             (Department ◇── Employee)

Composition (has-a, strong): A ◆────────── B
                             "A owns B, B cannot exist without A"
                             (House ◆── Room)

Inheritance (is-a):          A ────────▷ B
                             "A extends B"

Interface Implementation:    A ─ ─ ─ ─ ▷ B
                             "A implements B" (dashed arrow)

Dependency (depends on):     A ─ ─ ─ ─ ─> B
                             "A depends on B transiently"
```

**Multiplicity:**
```
1        — exactly one
0..1     — zero or one (optional)
*        — zero or more
1..*     — one or more
2..5     — between 2 and 5
```

**Example — Parking Lot class diagram:**
```
         ┌──────────────────┐
         │   ParkingLot     │
         ├──────────────────┤
         │ - name: String   │
         │ - capacity: int  │
         ├──────────────────┤
         │ + park(): Ticket │
         │ + unpark(): Bill │
         └────────┬─────────┘
                  ◆ 1..*
         ┌────────┴─────────┐
         │   ParkingFloor   │
         ├──────────────────┤
         │ - floorNum: int  │
         ├──────────────────┤
         │ + getSpots()     │
         └────────┬─────────┘
                  ◆ 1..*
         ┌────────┴─────────┐
         │   ParkingSpot    │◁─────────────────────────┐
         ├──────────────────┤                          │
         │ - spotNum: int   │          ┌───────────────┴────┐
         │ - occupied: bool │          │  <<interface>>     │
         ├──────────────────┤          │    SpotType        │
         │ + isAvailable()  │          ├────────────────────┤
         └──────────────────┘          │ COMPACT, LARGE,    │
                                       │ HANDICAPPED        │
                                       └────────────────────┘
```

---

### Sequence Diagrams

A sequence diagram shows the dynamic behaviour: how objects interact over time.

```
Notation:
  Actor/Object:  Box at top with name
  Lifeline:      Vertical dashed line below each object
  Message:       Horizontal arrow between lifelines (→ sync, --> async)
  Activation:    Thin rectangle on lifeline (object is active)
  Return:        Dashed arrow back (←- -)
  Self-call:     Arrow looping back to same lifeline

Example — Parking a vehicle:

Customer     ParkingLot    Floor      Spot      Ticket
   |              |          |          |          |
   |──park(car)──>|          |          |          |
   |              |──findFloor()──>|    |          |
   |              |          |──findSpot()──>|     |
   |              |          |          |──reserve()|
   |              |          |<──spot──-|          |
   |              |<──floor──|          |          |
   |              |──────────────────────createTicket()──>|
   |<──ticket─────|          |          |          |
```

---

## SOLID Violations Quick-Reference

| Smell | Principle Violated | Fix |
|-------|-------------------|-----|
| Class with 5+ unrelated methods | SRP | Split into focused classes |
| `if/else` or `switch` on type | OCP | Strategy pattern |
| Subclass throws `UnsupportedOperationException` | LSP | Redesign hierarchy or use composition |
| `instanceof` checks in polymorphic code | LSP | Fix inheritance, use polymorphism properly |
| Fat interface with 10+ methods | ISP | Split into role-specific interfaces |
| `new ConcreteClass()` inside service | DIP | Inject via constructor / DI container |
| Hard to unit test (can't mock) | DIP | Introduce interface, inject dependency |

---

## 📝 Tasks

### Task 1 — SOLID Violation Hunt
For each code snippet below, identify: which SOLID principle is violated, why, and write the fixed version.

**Snippet A:**
```java
class Report {
    public String generateHTML() { ... }
    public String generatePDF() { ... }
    public void saveToFile(String path) { ... }
    public void uploadToS3() { ... }
    public void emailReport(String to) { ... }
}
```

**Snippet B:**
```java
class Rectangle {
    public int area() { return width * height; }
}
class Square extends Rectangle {
    public void setWidth(int w) { this.width = w; this.height = w; }
    public void setHeight(int h) { this.width = h; this.height = h; }
}
```

**Snippet C:**
```java
interface Printable {
    void print();
    void scan();
    void fax();
    void copyDocument();
}
class BasicPrinter implements Printable {
    public void print() { ... }
    public void scan() { throw new UnsupportedOperationException(); }
    public void fax() { throw new UnsupportedOperationException(); }
    public void copyDocument() { throw new UnsupportedOperationException(); }
}
```

**Snippet D:**
```java
class NotificationService {
    public void notify(String type, String message) {
        if (type.equals("EMAIL")) sendEmail(message);
        else if (type.equals("SMS")) sendSMS(message);
        else if (type.equals("PUSH")) sendPush(message);
    }
}
```

### Task 2 — UML Class Diagram
Draw the UML class diagram for a Library Management System with these entities: Library, Member, Book, BookCopy, Loan, Librarian.

Include: all attributes (with types), all methods, and all relationships (with correct notation: composition/aggregation/association/inheritance) and multiplicities.

### Task 3 — Sequence Diagram
Draw a sequence diagram for the following flow in an e-commerce system:
*"Customer places an order → system validates payment → reserves inventory → sends confirmation email"*

Include: Customer, OrderService, PaymentService, InventoryService, EmailService.

### ⭐ Mini Project — Parking Lot Refactoring

**Problem:** The following Parking Lot implementation has multiple SOLID violations. Your task is to identify ALL violations and produce a fully refactored version with a proper class diagram.

**Violating code:**
```java
class ParkingLot {
    private int totalSpots = 100;
    private int occupiedSpots = 0;
    private List<String[]> parkedVehicles = new ArrayList<>();
    
    public String parkVehicle(String vehicleType, String licensePlate) {
        if (occupiedSpots >= totalSpots) return "Lot is full";
        
        // Violation: type-based branching (OCP)
        double rate;
        if (vehicleType.equals("CAR")) rate = 20.0;
        else if (vehicleType.equals("BIKE")) rate = 10.0;
        else if (vehicleType.equals("TRUCK")) rate = 40.0;
        else return "Unknown vehicle type";
        
        // Violation: mixing parking logic + billing logic (SRP)
        String ticketId = "T" + System.currentTimeMillis();
        parkedVehicles.add(new String[]{ticketId, licensePlate, vehicleType, 
                           String.valueOf(System.currentTimeMillis()), String.valueOf(rate)});
        occupiedSpots++;
        
        // Violation: printing inside business logic (SRP)
        System.out.println("Parked " + vehicleType + " at spot. Ticket: " + ticketId);
        
        // Violation: direct DB call inside domain class (DIP)
        saveToDatabase(ticketId, licensePlate);
        return ticketId;
    }
    
    private void saveToDatabase(String ticketId, String plate) {
        // Hardcoded MySQL logic
        System.out.println("Saving to MySQL: " + ticketId);
    }
    
    public double calculateBill(String ticketId) {
        // Violation: all billing logic crammed here (SRP)
        for (String[] vehicle : parkedVehicles) {
            if (vehicle[0].equals(ticketId)) {
                long entryTime = Long.parseLong(vehicle[3]);
                double hours = (System.currentTimeMillis() - entryTime) / 3600000.0;
                double rate = Double.parseDouble(vehicle[4]);
                return Math.ceil(hours) * rate;
            }
        }
        return 0;
    }
}
```

**Your deliverable:**
1. List every SOLID violation with the line(s) involved
2. Produce the refactored Java code
3. Draw the UML class diagram of your refactored design

---

## 💡 Interview Tips Summary

| Principle | One-liner to say in interview | Pattern it enables |
|-----------|------------------------------|-------------------|
| SRP | "Each class has one reason to change" | — (foundational) |
| OCP | "Open for extension, closed for modification" | Strategy, Template Method |
| LSP | "Subtypes must honour the parent's contract" | — (prevents bad inheritance) |
| ISP | "Many focused interfaces > one fat interface" | — (enables clean composition) |
| DIP | "Depend on abstractions, not concretions" | Factory, DI containers |

**UML tips:**
- In interviews, always start with a rough class diagram before writing code
- Composition (◆) = strong ownership. Aggregation (◇) = weak relationship
- Sequence diagrams: draw them left-to-right, time flows downward
- Never draw a class diagram without multiplicities on relationships

---

## 🔄 Trade-off Summary

| Decision | Trade-off |
|----------|-----------|
| Strict SRP | More classes → more navigation overhead, but each class is simpler to change |
| OCP via Strategy | More objects → slightly more memory, but zero modification of existing code |
| Composition over Inheritance | More explicit wiring, but far less coupling and easier testing |
| Interface per role (ISP) | More files/interfaces, but each client depends only on what it needs |
| DIP via constructor injection | Slightly more boilerplate, but 100% testable and swappable |

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
