---
title: "Module A3 — Structural Patterns Notes"
description: "System Design Roadmap › Module A3 › Full Notes Module A3 — Structural Patterns Complete reference notes · Track A: LLD · Week 5 Adapter Decorator Proxy Composite Facade Bridge…"
domain: system-design
track: system-design-lld
order: 7
url: /learning/system-design/lld/module-a3-notes/
---

<div class="chapter-hero" style="--ch-1:#00e5ff;--ch-2:#7c6fff;">
  <div class="breadcrumb">
    <a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
    <span class="separator">›</span>
    <a href="/learning/system-design/lld/module-a3-structural/">Module A3</a>
    <span class="separator">›</span>
    <span class="current">Full Notes</span>
  </div>
  <h1>Module A3 — Structural Patterns</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Week 5</p>
  <div class="hero-stats">
    <span class="stat-badge">Adapter</span>
    <span class="stat-badge">Decorator</span>
    <span class="stat-badge">Proxy</span>
    <span class="stat-badge">Composite</span>
    <span class="stat-badge">Facade</span>
    <span class="stat-badge">Bridge</span>
    <span class="stat-badge">Flyweight</span>
  </div>
</div>

<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a3-structural/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(0,229,255,0.1);border:1px solid rgba(0,229,255,0.3);color:#00e5ff;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>

## 🎯 Module Overview

**Duration:** 1 Week  
**Track:** A — Low-Level Design (LLD)  
**Prerequisites:** Module A2 (Creational Patterns)  
**Goal:** Master all 7 Structural patterns. Structural patterns deal with object composition — how classes and objects are assembled into larger structures while keeping those structures flexible and efficient.

### Learning Objectives
By the end of Module A3, you will:
- Implement all 7 Structural patterns from memory in Java
- Know the exact structural problem each pattern solves
- Distinguish between similar patterns (Adapter vs Facade vs Proxy vs Decorator)
- Apply the Splitwise Simplify Algorithm as a real Facade + composite design problem
- Complete the Splitwise mini project with full LLD implementation

### The 7 Structural Patterns

| # | Pattern | Real System | Core Problem Solved |
|---|---------|-------------|---------------------|
| 1 | Adapter | Vending Machine | Make incompatible interfaces work together |
| 2 | Decorator | Pizza Billing System | Add responsibilities dynamically without subclassing |
| 3 | Proxy | Car Rental System | Control access to an object |
| 4 | Composite | File System | Treat individual objects and compositions uniformly |
| 5 | Facade | Splitwise | Provide a simplified interface to a complex subsystem |
| 6 | Bridge | CricBuzz | Decouple abstraction from implementation |
| 7 | Flyweight | TrueCaller | Share state to support large numbers of fine-grained objects |

---

## Pattern 1 — Adapter

### Intent
Convert the interface of a class into another interface that clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

### The Problem It Solves
You have existing code that works with interface A. You get a new component that only speaks interface B. You can't change either. Adapter wraps the new component to speak interface A.

**Real-world analogy:** A power plug adapter — the socket hasn't changed, the appliance hasn't changed, the adapter bridges the gap.

### Implementation — Vending Machine

```java
// Existing interface your system expects
interface VendingMachine {
    void insertCoin(int amount);
    void selectProduct(String code);
    void dispense();
    int getChange();
}

// New machine from a different vendor — incompatible interface
class NewVendorMachine {
    public void payAmount(double rupees)    { System.out.println("Paid: " + rupees); }
    public void chooseItem(int itemId)      { System.out.println("Selected: " + itemId); }
    public void releaseItem()              { System.out.println("Dispensing item"); }
    public double calculateChange()        { return 5.50; }
}

// ADAPTER — wraps NewVendorMachine, exposes VendingMachine interface
class VendingMachineAdapter implements VendingMachine {
    private final NewVendorMachine adaptee;
    private int    insertedAmount = 0;
    private String selectedCode   = null;
    private Map<String, Integer> codeToId = Map.of("A1", 1, "B2", 2, "C3", 3);

    public VendingMachineAdapter(NewVendorMachine machine) {
        this.adaptee = machine;
    }

    @Override
    public void insertCoin(int amount) {
        this.insertedAmount = amount;
        adaptee.payAmount(amount / 100.0);    // Converts paise → rupees
    }

    @Override
    public void selectProduct(String code) {
        this.selectedCode = code;
        int id = codeToId.getOrDefault(code, -1);
        if (id == -1) throw new IllegalArgumentException("Unknown code: " + code);
        adaptee.chooseItem(id);               // Translates string code → int id
    }

    @Override
    public void dispense() {
        adaptee.releaseItem();
    }

    @Override
    public int getChange() {
        return (int)(adaptee.calculateChange() * 100); // Rupees → paise
    }
}

// Client code unchanged — still uses VendingMachine interface
VendingMachine vm = new VendingMachineAdapter(new NewVendorMachine());
vm.insertCoin(1000);
vm.selectProduct("A1");
vm.dispense();
```

### Object Adapter vs Class Adapter
```
Object Adapter (preferred):
  - Uses composition — holds reference to adaptee
  - More flexible — can adapt subclasses of adaptee too
  - Java's goto choice (no multiple inheritance needed)

Class Adapter:
  - Uses multiple inheritance — extends both Target and Adaptee
  - Not possible in Java (single inheritance)
  - Possible in C++ or languages with multiple inheritance
```

### When to Use Adapter
✅ Integrating third-party library with incompatible interface  
✅ Legacy system integration  
✅ When you can't modify either the client or the adaptee  
✅ Payment gateway integration (different providers, same internal interface)

### SOLID Connection
- **OCP**: New vendor machines become new Adapter classes — existing client code unchanged
- **SRP**: Translation logic lives in Adapter, not in client or adaptee

### Interview Tip
> "Adapter is your go-to when integrating third-party systems. In production I'd create an internal `PaymentGateway` interface and write an Adapter for each provider (Stripe, PayPal, Razorpay). Switching providers means swapping the Adapter — zero client changes."

---

## Pattern 2 — Decorator

### Intent
Attach additional responsibilities to an object **dynamically**. Decorators provide a flexible alternative to subclassing for extending functionality.

### The Problem It Solves
You need to add features to an object at runtime, or in combinations, without an explosion of subclasses. The key insight: **a Decorator IS-A and HAS-A the same type simultaneously.**

### Implementation — Pizza Billing System

```java
// Component interface
interface Pizza {
    String getDescription();
    double getCost();
}

// Concrete Component — base pizza
class MargheritaPizza implements Pizza {
    public String getDescription() { return "Margherita"; }
    public double getCost()        { return 200.0; }
}

class FarmhousePizza implements Pizza {
    public String getDescription() { return "Farmhouse"; }
    public double getCost()        { return 280.0; }
}

// ABSTRACT DECORATOR — IS-A Pizza AND HAS-A Pizza
abstract class ToppingDecorator implements Pizza {
    protected final Pizza pizza;   // The wrapped pizza

    public ToppingDecorator(Pizza pizza) {
        this.pizza = pizza;
    }
    // Delegates to wrapped pizza by default
    public String getDescription() { return pizza.getDescription(); }
    public double getCost()        { return pizza.getCost(); }
}

// Concrete Decorators — each adds one topping
class CheeseDecorator extends ToppingDecorator {
    public CheeseDecorator(Pizza pizza) { super(pizza); }

    @Override
    public String getDescription() { return pizza.getDescription() + " + Cheese"; }

    @Override
    public double getCost() { return pizza.getCost() + 50.0; }
}

class MushroomDecorator extends ToppingDecorator {
    public MushroomDecorator(Pizza pizza) { super(pizza); }

    @Override
    public String getDescription() { return pizza.getDescription() + " + Mushroom"; }

    @Override
    public double getCost() { return pizza.getCost() + 35.0; }
}

class OliveDecorator extends ToppingDecorator {
    public OliveDecorator(Pizza pizza) { super(pizza); }

    @Override
    public String getDescription() { return pizza.getDescription() + " + Olive"; }

    @Override
    public double getCost() { return pizza.getCost() + 25.0; }
}

// Usage — wrap at runtime in any combination
Pizza order = new MargheritaPizza();              // 200
order = new CheeseDecorator(order);               // 200 + 50 = 250
order = new MushroomDecorator(order);             // 250 + 35 = 285
order = new OliveDecorator(order);                // 285 + 25 = 310
order = new CheeseDecorator(order);               // 310 + 50 = 360 (extra cheese!)

System.out.println(order.getDescription());
// → Margherita + Cheese + Mushroom + Olive + Cheese

System.out.println(order.getCost());
// → 360.0
```

### Why Not Subclassing?
```
Without Decorator — subclass explosion:
  MargheritaWithCheese
  MargheritaWithMushroom
  MargheritaWithCheeseAndMushroom
  MargheritaWithCheeseAndMushroomAndOlive
  FarmhouseWithCheese
  ... → 2^N combinations with N toppings!

With Decorator: N decorators, infinite runtime combinations.
```

### Real-world examples
- **Java I/O:** `new BufferedReader(new InputStreamReader(new FileInputStream("file.txt")))` — each wrapper adds a responsibility
- **HTTP middleware chains:** Express.js/Spring interceptors — each middleware decorates the request handler
- **Logging/Metrics wrappers:** `MetricService(CachingService(DatabaseService))` — cross-cutting concerns as decorators

### SOLID Connection
- **OCP**: New toppings = new Decorator class, zero modification to existing code
- **SRP**: Each Decorator has one responsibility (one topping)

---

## Pattern 3 — Proxy

### Intent
Provide a **surrogate or placeholder** for another object to control access to it.

### The Problem It Solves
You need to intercept calls to an object — to add access control, lazy initialisation, caching, logging, or remote access — without changing the object or its clients.

### Three Types of Proxy

```
Virtual Proxy:    Defers expensive object creation until actually needed
                  (lazy initialisation)

Protection Proxy: Controls access based on permissions
                  (authorization)

Remote Proxy:     Represents an object in a different address space
                  (RPC, gRPC stubs)
```

### Implementation — Car Rental System (Protection Proxy)

```java
// Subject interface
interface CarRentalService {
    Car rentCar(String carModel, User user);
    void returnCar(String carId, User user);
    List<Car> getAvailableCars();
}

// Real Subject — actual implementation
class CarRentalServiceImpl implements CarRentalService {
    private List<Car> availableCars = new ArrayList<>();

    public Car rentCar(String model, User user) {
        Car car = findCar(model);
        availableCars.remove(car);
        return car;
    }

    public void returnCar(String carId, User user) {
        availableCars.add(findReturnedCar(carId));
    }

    public List<Car> getAvailableCars() {
        return Collections.unmodifiableList(availableCars);
    }
}

// PROXY — controls access, adds cross-cutting concerns
class CarRentalProxy implements CarRentalService {
    private final CarRentalServiceImpl realService;
    private final Logger               logger;
    private final AuthService          auth;

    public CarRentalProxy(CarRentalServiceImpl svc, Logger log, AuthService auth) {
        this.realService = svc;
        this.logger      = log;
        this.auth        = auth;
    }

    @Override
    public Car rentCar(String model, User user) {
        // 1. Authorization check (Protection Proxy)
        if (!auth.hasValidLicense(user)) {
            throw new UnauthorizedException("User has no valid license: " + user.getId());
        }
        if (!auth.hasCreditCheck(user)) {
            throw new UnauthorizedException("Credit check failed for: " + user.getId());
        }

        // 2. Logging (cross-cutting concern)
        logger.log("User " + user.getId() + " renting: " + model);

        // 3. Delegate to real service
        Car car = realService.rentCar(model, user);

        // 4. Post-logging
        logger.log("Car " + car.getId() + " assigned to user " + user.getId());
        return car;
    }

    @Override
    public void returnCar(String carId, User user) {
        logger.log("Return initiated: carId=" + carId + " user=" + user.getId());
        realService.returnCar(carId, user);
        logger.log("Car " + carId + " returned successfully");
    }

    @Override
    public List<Car> getAvailableCars() {
        return realService.getAvailableCars(); // No auth needed for browsing
    }
}

// Client sees same interface — proxy is transparent
CarRentalService service = new CarRentalProxy(new CarRentalServiceImpl(), logger, auth);
service.rentCar("Toyota Camry", currentUser);
```

### Proxy vs Decorator vs Adapter — The Critical Distinction

```
Adapter:   Changes the interface (incompatible → compatible)
Decorator: Same interface, adds behaviour (wraps to enhance)
Proxy:     Same interface, controls access (wraps to intercept)

Key question: What is the wrapper's PURPOSE?
  Converting interface? → Adapter
  Adding behaviour?    → Decorator
  Controlling access?  → Proxy
```

### Real-world examples
- **Java RMI / gRPC stubs:** Remote proxy — call looks local, happens on server
- **Spring AOP `@Transactional`, `@Cacheable`:** Proxy generated at runtime to wrap method calls
- **Hibernate LazyLoading:** Virtual proxy — related entity loads from DB only when accessed
- **CDN:** Remote proxy for static assets

---

## Pattern 4 — Composite

### Intent
Compose objects into **tree structures** to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

### The Problem It Solves
When you have a tree structure (file system, org chart, UI widget tree) and want to treat leaf nodes and branch nodes identically through a single interface.

### Implementation — File System

```java
// Component interface — same for files AND directories
interface FileSystemComponent {
    String getName();
    long   getSize();
    void   display(String indent);
    void   delete();
}

// LEAF — has no children
class File implements FileSystemComponent {
    private final String name;
    private final long   size;

    public File(String name, long size) {
        this.name = name;
        this.size = size;
    }

    public String getName()          { return name; }
    public long   getSize()          { return size; }
    public void   delete()           { System.out.println("Deleting file: " + name); }
    public void   display(String indent) {
        System.out.println(indent + "📄 " + name + " (" + size + " bytes)");
    }
}

// COMPOSITE — has children (can be File or Directory)
class Directory implements FileSystemComponent {
    private final String name;
    private final List<FileSystemComponent> children = new ArrayList<>();

    public Directory(String name) { this.name = name; }

    public void add(FileSystemComponent component)    { children.add(component); }
    public void remove(FileSystemComponent component) { children.remove(component); }

    public String getName() { return name; }

    // Size = recursive sum of all children
    public long getSize() {
        return children.stream().mapToLong(FileSystemComponent::getSize).sum();
    }

    // Delete = recursively delete all children
    public void delete() {
        children.forEach(FileSystemComponent::delete);
        System.out.println("Deleting directory: " + name);
    }

    // Display = recursive traversal
    public void display(String indent) {
        System.out.println(indent + "📁 " + name + " (" + getSize() + " bytes)");
        children.forEach(c -> c.display(indent + "  "));
    }
}

// Usage — client treats File and Directory identically
Directory root = new Directory("root");
Directory src  = new Directory("src");
Directory test = new Directory("test");

src.add(new File("Main.java", 2048));
src.add(new File("Utils.java", 1024));
test.add(new File("MainTest.java", 512));

root.add(src);
root.add(test);
root.add(new File("README.md", 256));

root.display("");     // Prints entire tree
root.getSize();       // Returns total size recursively
```

### When to Use Composite
✅ Tree structures: file system, org charts, XML/JSON/HTML DOM  
✅ Menus and submenus (BookMyShow category tree)  
✅ UI component hierarchies (Panel → Button, Label, TextBox)  
✅ Bill of materials (product → sub-components → sub-sub-components)

---

## Pattern 5 — Facade

### Intent
Provide a **unified, simplified interface** to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

### The Problem It Solves
Complex subsystems have many classes with many methods. Clients shouldn't need to know all of them — they need a simple entry point for the most common operations.

### Implementation — Splitwise

```java
// Complex subsystems — many classes, many responsibilities
class UserService {
    public User findUser(String userId)         { ... }
    public boolean userExists(String userId)    { ... }
}

class ExpenseService {
    public Expense createExpense(String desc, double amount, String paidBy) { ... }
    public List<Expense> getGroupExpenses(String groupId)                   { ... }
}

class SplitCalculator {
    public Map<String, Double> calculateEqualSplit(Expense expense, List<String> memberIds) { ... }
    public Map<String, Double> calculatePercentageSplit(Expense expense, Map<String, Double> pct) { ... }
    public Map<String, Double> calculateExactSplit(Expense expense, Map<String, Double> amounts) { ... }
}

class BalanceService {
    public Map<String, Double> getNetBalances(String groupId)               { ... }
    public void settleBalance(String payerId, String payeeId, double amount){ ... }
    public List<Transaction> getPendingSettlements(String groupId)          { ... }
}

class NotificationService {
    public void notifyExpenseAdded(List<String> memberIds, Expense expense)  { ... }
    public void notifySettlement(String payerId, String payeeId, double amt) { ... }
}

// FACADE — simplified interface hiding all subsystem complexity
class SplitwiseFacade {
    private final UserService         userService;
    private final ExpenseService      expenseService;
    private final SplitCalculator     calculator;
    private final BalanceService      balanceService;
    private final NotificationService notifier;

    public SplitwiseFacade() {
        // Wires up all subsystems internally
        this.userService    = new UserService();
        this.expenseService = new ExpenseService();
        this.calculator     = new SplitCalculator();
        this.balanceService = new BalanceService();
        this.notifier       = new NotificationService();
    }

    // HIGH-LEVEL OPERATION 1: Add expense and split equally
    public void addExpenseEqualSplit(String groupId, String description,
                                     double amount, String paidBy,
                                     List<String> memberIds) {
        // Orchestrates 4 subsystems transparently
        Expense expense    = expenseService.createExpense(description, amount, paidBy);
        Map<String, Double> splits = calculator.calculateEqualSplit(expense, memberIds);
        balanceService.updateBalances(groupId, splits, paidBy);
        notifier.notifyExpenseAdded(memberIds, expense);
    }

    // HIGH-LEVEL OPERATION 2: Settle up between two users
    public void settleUp(String groupId, String payerId, String payeeId, double amount) {
        balanceService.settleBalance(payerId, payeeId, amount);
        notifier.notifySettlement(payerId, payeeId, amount);
    }

    // HIGH-LEVEL OPERATION 3: Get simplified settlement plan
    public List<Transaction> getSimplifiedSettlements(String groupId) {
        Map<String, Double> balances = balanceService.getNetBalances(groupId);
        return SimplifyAlgorithm.simplify(balances);  // See below
    }
}

// Client — only needs the Facade
SplitwiseFacade splitwise = new SplitwiseFacade();
splitwise.addExpenseEqualSplit("grp1", "Dinner", 1200.0, "ajay", List.of("ajay","ram","priya"));
splitwise.settleUp("grp1", "ram", "ajay", 400.0);
```

### The Splitwise Simplify Algorithm

This is the most interesting part of the Splitwise LLD — the "optimal accounting balance" algorithm.

**Problem:** Given a group where each person has a net balance (positive = owed money, negative = owes money), find the minimum number of transactions to settle all debts.

**Algorithm (Greedy with Two Pointers):**

```java
class SimplifyAlgorithm {
    public static List<Transaction> simplify(Map<String, Double> netBalances) {
        // Separate into creditors (owed money) and debtors (owe money)
        PriorityQueue<double[]> creditors = new PriorityQueue<>(
            (a, b) -> Double.compare(b[0], a[0]));  // Max heap
        PriorityQueue<double[]> debtors = new PriorityQueue<>(
            (a, b) -> Double.compare(a[0], b[0]));  // Min heap

        String[] names = netBalances.keySet().toArray(new String[0]);
        Map<Double, String> amountToName = new HashMap<>();

        for (Map.Entry<String, Double> entry : netBalances.entrySet()) {
            double balance = entry.getValue();
            if (balance > 0.001) {
                creditors.offer(new double[]{balance});
                // (simplified — track names in real impl)
            } else if (balance < -0.001) {
                debtors.offer(new double[]{balance});
            }
        }

        List<Transaction> transactions = new ArrayList<>();

        while (!creditors.isEmpty() && !debtors.isEmpty()) {
            double credit = creditors.poll()[0];
            double debt   = Math.abs(debtors.poll()[0]);

            double settled = Math.min(credit, debt);
            transactions.add(new Transaction(/* debtor pays creditor */ settled));

            if (credit > debt + 0.001)  creditors.offer(new double[]{credit - debt});
            else if (debt > credit + 0.001) debtors.offer(new double[]{-(debt - credit)});
        }

        return transactions;
        // Result: minimum number of transactions to clear all debts
    }
}
```

**Example:**
```
Net balances:
  Ajay:  +600  (owed 600)
  Ram:   -400  (owes 400)
  Priya: -200  (owes 200)

Naive: Ram→Ajay 400, Priya→Ajay 200 = 2 transactions
With 5 people this could be many more — algorithm minimises it.

Minimum: Ram pays Ajay 400, Priya pays Ajay 200 → 2 (optimal for this case)
```

### Facade vs Adapter vs Mediator
```
Facade:   Simplifies interface to a SUBSYSTEM (multiple classes)
          Subsystem classes don't know about Facade
          One-directional: client → facade → subsystem

Adapter:  Converts ONE incompatible interface
          Works with a single adaptee
          Purpose: compatibility, not simplification

Mediator: Encapsulates HOW objects interact (Module A4)
          Objects know about Mediator, talk through it
          Purpose: reduce coupling between peers
```

---

## Pattern 6 — Bridge

### Intent
**Decouple an abstraction from its implementation** so that the two can vary independently.

### The Problem It Solves
When you have two orthogonal dimensions of variation (e.g., notification type × notification channel) and subclassing both creates a combinatorial explosion.

### Implementation — CricBuzz

```java
// Implementation interface — HOW notifications are sent
interface NotificationSender {
    void send(String recipient, String message);
}

// Concrete Implementations
class SMSSender implements NotificationSender {
    public void send(String recipient, String message) {
        System.out.println("SMS to " + recipient + ": " + message);
    }
}

class EmailSender implements NotificationSender {
    public void send(String recipient, String message) {
        System.out.println("Email to " + recipient + ": " + message);
    }
}

class PushSender implements NotificationSender {
    public void send(String recipient, String message) {
        System.out.println("Push to " + recipient + ": " + message);
    }
}

// ABSTRACTION — WHAT type of notification
abstract class CricketNotification {
    protected final NotificationSender sender;  // THE BRIDGE

    public CricketNotification(NotificationSender sender) {
        this.sender = sender;
    }

    public abstract void notify(String recipient, Object event);
}

// Refined Abstractions — different notification types
class WicketNotification extends CricketNotification {
    public WicketNotification(NotificationSender sender) { super(sender); }

    @Override
    public void notify(String recipient, Object event) {
        String msg = "WICKET! " + event + " is out!";
        sender.send(recipient, msg);  // Uses injected sender
    }
}

class SixNotification extends CricketNotification {
    public SixNotification(NotificationSender sender) { super(sender); }

    @Override
    public void notify(String recipient, Object event) {
        sender.send(recipient, "SIX! " + event + " smashes it!");
    }
}

class ScoreUpdateNotification extends CricketNotification {
    public ScoreUpdateNotification(NotificationSender sender) { super(sender); }

    @Override
    public void notify(String recipient, Object event) {
        sender.send(recipient, "Score Update: " + event);
    }
}

// Usage — mix and match abstraction × implementation independently
CricketNotification wicketSMS   = new WicketNotification(new SMSSender());
CricketNotification wicketEmail = new WicketNotification(new EmailSender());
CricketNotification sixPush     = new SixNotification(new PushSender());

wicketSMS.notify("user@123", "Rohit Sharma");
wicketEmail.notify("fan@gmail.com", "Virat Kohli");
sixPush.notify("device_token_xyz", "MS Dhoni");
```

### Without Bridge (subclass explosion):
```
WicketSMSNotification
WicketEmailNotification
WicketPushNotification
SixSMSNotification
SixEmailNotification
SixPushNotification
ScoreUpdateSMSNotification
...
→ N types × M channels = N×M classes
With Bridge: N + M classes
```

### SOLID Connection
- **OCP**: Add new notification type OR new sender independently — no modification
- **SRP**: Abstraction handles WHAT, Implementation handles HOW

---

## Pattern 7 — Flyweight

### Intent
Use **sharing to support a large number of fine-grained objects efficiently**. Separate intrinsic state (shared, immutable) from extrinsic state (unique per instance, passed at runtime).

### The Problem It Solves
When you need huge numbers of similar objects that would consume too much memory if each stored all their state.

**Key insight:** Split state into:
- **Intrinsic:** Shared, context-independent, stored in Flyweight
- **Extrinsic:** Context-dependent, unique per use, passed by client

### Implementation — TrueCaller

```java
// Flyweight — stores INTRINSIC state (shared across many contacts)
class ContactMetadata {
    private final String operatorName;   // "Airtel", "Jio", "BSNL" — shared
    private final String countryCode;    // "+91", "+1" — shared
    private final String contactType;    // "SPAM", "PERSONAL", "BUSINESS" — shared
    private final String spamLabel;      // "Telemarketer", "Bank", null — shared

    public ContactMetadata(String operatorName, String countryCode,
                           String contactType, String spamLabel) {
        this.operatorName = operatorName;
        this.countryCode  = countryCode;
        this.contactType  = contactType;
        this.spamLabel    = spamLabel;
    }

    // Getters — immutable, so thread-safe
    public String getOperatorName() { return operatorName; }
    public String getContactType()  { return contactType; }
    public String getSpamLabel()    { return spamLabel; }
}

// Flyweight Factory — ensures shared instances
class ContactMetadataFactory {
    private static final Map<String, ContactMetadata> pool = new HashMap<>();

    public static ContactMetadata get(String operator, String country,
                                       String type, String spam) {
        String key = operator + "|" + country + "|" + type + "|" + spam;
        return pool.computeIfAbsent(key,
            k -> new ContactMetadata(operator, country, type, spam));
    }

    public static int poolSize() { return pool.size(); }
}

// Client context — stores EXTRINSIC state (unique per contact)
class PhoneContact {
    // Extrinsic — unique per contact
    private final String phoneNumber;
    private final String callerName;
    private final int    reportCount;

    // Intrinsic — SHARED flyweight object
    private final ContactMetadata metadata;

    public PhoneContact(String number, String name, int reports,
                        String operator, String country, String type, String spam) {
        this.phoneNumber = number;
        this.callerName  = name;
        this.reportCount = reports;
        // Get or create shared flyweight
        this.metadata = ContactMetadataFactory.get(operator, country, type, spam);
    }

    public void display() {
        System.out.println(callerName + " (" + phoneNumber + ")"
            + " | Op: " + metadata.getOperatorName()
            + " | Type: " + metadata.getContactType()
            + (metadata.getSpamLabel() != null ? " ⚠️ " + metadata.getSpamLabel() : ""));
    }
}

// Impact:
// 1 billion contacts in TrueCaller
// Without Flyweight: 1B × ~200 bytes metadata = 200 GB
// With Flyweight: ~1,000 unique metadata combos × 200 bytes = 200 KB shared
// Per contact: only stores phoneNumber + name + reportCount (extrinsic)
```

### When to Use Flyweight
✅ Huge numbers of similar objects (game particles, font glyphs, network packets)  
✅ Memory is a bottleneck  
✅ Most object state can be made extrinsic  
✅ App doesn't depend on object identity (shared objects can't be distinguished)

### Real-world examples
- **Java String Pool:** `"hello"` literals are interned — shared flyweights
- **Java Integer cache:** `Integer.valueOf(-128 to 127)` returns cached instances
- **Game engines:** Thousands of particle/bullet objects sharing texture/physics data
- **Font rendering:** Glyph shapes stored once, rendered at different positions

---

## 🏗️ Mini Project — Splitwise Clone (LLD)

### Overview
Design a complete Splitwise application using Structural patterns throughout. This project is the capstone for Module A3.

### Requirements
1. Users can form groups
2. Any member can add an expense (paid by one person, split multiple ways)
3. Support 3 split types: Equal, Percentage, Exact
4. Show net balances per user in a group
5. Simplify debts — minimum transactions to settle all balances
6. Notify members when expense is added or settlement happens
7. Allow settling up between two users

### Pattern Mapping in Splitwise

| Component | Pattern | Reason |
|-----------|---------|--------|
| `SplitwiseFacade` | Facade | Unified API over complex subsystems |
| `SplitStrategy` (Equal/Pct/Exact) | Strategy (preview of A4) | Interchangeable split algorithms |
| `ExpenseDecorator` (TaxDecorator, ServiceChargeDecorator) | Decorator | Add charges to base expense dynamically |
| `NotificationAdapter` (WhatsApp/Email/SMS) | Adapter | Normalize third-party notification APIs |
| `GroupComponent` (User/Group) | Composite | Treat individual user and group uniformly for notification |
| `SimplifyAlgorithm` | Algorithm within Facade | Minimize settlement transactions |

### Class Diagram (Key Classes)
```
SplitwiseFacade
├── UserService
├── GroupService
├── ExpenseService
│   └── SplitCalculator
│       ├── EqualSplit
│       ├── PercentageSplit
│       └── ExactSplit
├── BalanceService
│   └── SimplifyAlgorithm
└── NotificationService
    └── NotificationAdapter (Adapter pattern)
        ├── WhatsAppAdapter
        ├── EmailAdapter
        └── SMSAdapter

Expense (Component)
└── ExpenseDecorator
    ├── TaxDecorator
    └── ServiceChargeDecorator
```

### Deliverables
1. Full Java implementation (all classes above)
2. SimplifyAlgorithm fully implemented and tested with examples
3. UML class diagram showing all patterns used
4. Demo: 5-person group, 6 expenses, show balances, simplify, settle

---

## 📝 Tasks

### Task 1 — Pattern Recognition
For each scenario, identify which Structural pattern applies:

1. You need to use a payment library that accepts `PaymentRequest` objects but your system passes `Order` objects.
2. A security system needs to log all access attempts before allowing any database read/write — without modifying the database class.
3. You need to build a UI widget system where a `Panel` can contain `Button`, `Label`, or other `Panel` objects, and all support `render()` and `getSize()`.
4. A `HomeAutomation` system has `LightSubsystem`, `SecuritySubsystem`, `ClimateSubsystem` — you want a `HomeController.leaveHome()` method that handles everything.
5. An online game renders 10,000 bullets per second. Each bullet has position (unique) and appearance (shared: same color, texture, size for all bullets of same type).
6. A messaging platform can send notifications via Firebase, Twilio, or SendGrid — the core notification type (Alert, Reminder, Promo) should be independent of the delivery channel.

### Task 2 — Decorator Chain
Implement a `Logger` with decorators:
- `ConsoleLogger` — base logger, prints to stdout
- `TimestampDecorator` — prepends timestamp to every message
- `LevelDecorator` — prepends [INFO]/[WARN]/[ERROR] level
- `FileDecorator` — also writes to a file in addition to wrapped logger

Show that they can be stacked in any order and the output composes correctly.

### Task 3 — Proxy for Caching
Implement a `CachingProxy` for a `WeatherService`:
- `WeatherService` interface: `getWeather(String city): WeatherData`
- `RealWeatherService` makes an (expensive, slow) HTTP call
- `WeatherServiceProxy` caches results with a TTL of 5 minutes
- If cache has fresh data for city → return cache, skip HTTP call
- If cache miss or expired → call real service, store in cache

### Task 4 — Flyweight Memory Analysis
Given a game with 50,000 `Tree` objects. Each tree has:
- Intrinsic: `type` (Oak/Pine/Maple), `texture` (PNG path), `heightModel` (float[100])
- Extrinsic: `x`, `y`, `age`

Calculate:
1. Memory without Flyweight (all state per object)
2. Memory with Flyweight (shared intrinsic, extrinsic per object)
3. Show the Java implementation of `TreeFactory` and `Tree`

---

## 💡 Interview Tips Summary

| Pattern | One-liner | Critical distinction |
|---------|-----------|---------------------|
| Adapter | "Make incompatible interfaces work together" | Changes interface (unlike Proxy/Decorator) |
| Decorator | "Add behaviour dynamically without subclassing" | IS-A AND HAS-A same type; wraps to enhance |
| Proxy | "Control access to an object" | Same interface as real subject; wraps to intercept |
| Composite | "Treat part and whole uniformly" | Tree structure; client doesn't distinguish leaf vs node |
| Facade | "Simplified interface to complex subsystem" | Hides subsystem, doesn't add behaviour |
| Bridge | "Decouple abstraction from implementation" | Two independent class hierarchies connected by composition |
| Flyweight | "Share state to support massive numbers of objects" | Separate intrinsic (shared) from extrinsic (per-instance) |

**The most commonly confused trio:**
> "Adapter converts interfaces, Decorator adds behaviour through the same interface, Proxy controls access through the same interface. All three wrap an object — purpose distinguishes them."

---

## 🔄 Trade-off Summary

| Pattern | Advantage | Trade-off |
|---------|-----------|-----------|
| Adapter | Integration without modifying existing code | Extra indirection layer; translation bugs possible |
| Decorator | Infinite runtime combinations | Deep chains hard to debug; order of decoration matters |
| Proxy | Transparent cross-cutting concerns | Extra indirection; proxy bugs are subtle |
| Composite | Uniform treatment of hierarchy | Hard to restrict component types in the tree |
| Facade | Simplifies client code | May become god object if not kept focused |
| Bridge | Independent variation of two dimensions | Up-front complexity; need to identify dimensions correctly |
| Flyweight | Massive memory savings | Extrinsic state management burden on client; not identity-safe |

---

## ✅ Module A3 Completion Checklist

- [ ] Can implement all 7 Structural patterns from memory
- [ ] Can distinguish Adapter vs Decorator vs Proxy in 30 seconds
- [ ] Understand Composite's part-whole uniformity and when to use it
- [ ] Know Facade's role vs Mediator vs Adapter (all "simplify/translate")
- [ ] Can explain Bridge's two-dimensional variation problem
- [ ] Can identify intrinsic vs extrinsic state for Flyweight
- [ ] Completed Task 1 — Pattern Recognition (6 scenarios)
- [ ] Completed Task 2 — Logger Decorator chain
- [ ] Completed Task 3 — WeatherService CachingProxy
- [ ] Completed Task 4 — Flyweight memory analysis + Tree implementation
- [ ] Completed Mini Project — Splitwise clone with Simplify Algorithm + UML

**→ When complete: Ready for Module A4 — Behavioral Design Patterns**

<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="/learning/system-design/lld/module-a3-structural/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(0,229,255,0.1);border:1px solid rgba(0,229,255,0.3);color:#00e5ff;text-decoration:none;font-weight:700;">⚡ Open Interactive Version</a>
  <a href="/learning/system-design/system-design-roadmap/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(30,42,64,0.6);border:1px solid #263450;color:#d4deff;text-decoration:none;font-weight:600;">↑ Back to Roadmap</a>
</div>
