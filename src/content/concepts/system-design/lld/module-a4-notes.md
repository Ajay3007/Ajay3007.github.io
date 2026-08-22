---
title: "Module A4 — Behavioral Patterns Notes"
description: "System Design Roadmap › Module A4 › Full Notes Module A4 — Behavioral Patterns Complete reference notes · Track A: LLD · Week 6 Strategy Observer Command State Template Method…"
domain: system-design
track: system-design-lld
order: 9
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a4-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero" style="--ch-1:#ef4444;--ch-2:#dc2626;">
  <div class="breadcrumb">
<a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
<span class="separator">›</span>
<a href="/learning/system-design/lld/module-a4-behavioral/">Module A4</a>
<span class="separator">›</span>
<span class="current">Full Notes</span>
  </div>
  <h1>Module A4 — Behavioral Patterns</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Week 6</p>
  <div class="hero-stats">
<span class="stat-badge">Strategy</span>
<span class="stat-badge">Observer</span>
<span class="stat-badge">Command</span>
<span class="stat-badge">State</span>
<span class="stat-badge">Template Method</span>
<span class="stat-badge">Chain of Responsibility</span>
<span class="stat-badge">12 Behavioral Patterns</span>
  </div>
</div>
<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a4-behavioral/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:#fb7185;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>

## 🎯 Module Overview

**Duration:** 2 Weeks  
**Track:** A — Low-Level Design (LLD)  
**Prerequisites:** Module A3 (Structural Patterns)  
**Goal:** Master all 12 Behavioral patterns. Behavioral patterns deal with algorithms and the assignment of responsibilities between objects — specifically how they communicate and coordinate.

### The 12 Behavioral Patterns

| # | Pattern | Real System | Core Problem Solved |
|---|---------|-------------|---------------------|
| 1 | Strategy | Payment System | Swap algorithms at runtime |
| 2 | Observer | Stock Ticker / Event Bus | Notify dependents automatically |
| 3 | Chain of Responsibility | ATM Dispenser | Pass request along a chain |
| 4 | State | Vending Machine | Change behaviour when state changes |
| 5 | Command | Smart Home / Undo | Encapsulate requests as objects |
| 6 | Template Method | Data Migration | Define skeleton, defer steps to subclass |
| 7 | Iterator | Custom Collections | Traverse without exposing internals |
| 8 | Mediator | Air Traffic Control | Reduce peer-to-peer coupling |
| 9 | Memento | Text Editor Undo | Capture and restore state |
| 10 | Visitor | Tax Calculator | Add operations without changing classes |
| 11 | Null Object | Logging / No-ops | Eliminate null checks |
| 12 | Interpreter | Math Expression Parser | Grammar-based language evaluation |

---

## Pattern 1 — Strategy

### Intent
Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.

### The Problem It Solves
When you have multiple ways to do the same thing (sort, pay, compress, validate) and the choice must be made at runtime. Eliminates if/else chains on algorithm type.

### Implementation — Payment System

```java
// Strategy interface — all payment methods implement this
interface PaymentStrategy {
    boolean pay(double amount);
    String  getPaymentMode();
}

// Concrete Strategies
class CreditCardPayment implements PaymentStrategy {
    private final String cardNumber;
    private final String cvv;

    public CreditCardPayment(String cardNumber, String cvv) {
        this.cardNumber = cardNumber;
        this.cvv        = cvv;
    }

    @Override
    public boolean pay(double amount) {
        System.out.println("Paid ₹" + amount + " via Credit Card ending " + cardNumber.substring(12));
        return true; // Simulate success
    }

    @Override
    public String getPaymentMode() { return "CREDIT_CARD"; }
}

class UPIPayment implements PaymentStrategy {
    private final String upiId;

    public UPIPayment(String upiId) { this.upiId = upiId; }

    @Override
    public boolean pay(double amount) {
        System.out.println("Paid ₹" + amount + " via UPI: " + upiId);
        return true;
    }

    @Override
    public String getPaymentMode() { return "UPI"; }
}

class WalletPayment implements PaymentStrategy {
    private double balance;
    private final String walletId;

    public WalletPayment(String walletId, double initialBalance) {
        this.walletId = walletId;
        this.balance  = initialBalance;
    }

    @Override
    public boolean pay(double amount) {
        if (balance < amount) {
            System.out.println("Insufficient wallet balance");
            return false;
        }
        balance -= amount;
        System.out.println("Paid ₹" + amount + " via Wallet: " + walletId);
        return true;
    }

    @Override
    public String getPaymentMode() { return "WALLET"; }
}

// Context — uses a strategy without knowing which one
class ShoppingCart {
    private final List<Item>    items = new ArrayList<>();
    private       PaymentStrategy paymentStrategy;  // injected

    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;  // swap at runtime!
    }

    public double getTotalAmount() {
        return items.stream().mapToDouble(Item::getPrice).sum();
    }

    public boolean checkout() {
        if (paymentStrategy == null)
            throw new IllegalStateException("No payment strategy set");
        double total = getTotalAmount();
        return paymentStrategy.pay(total);
    }
}

// Usage — strategy can change at runtime
ShoppingCart cart = new ShoppingCart();
cart.addItem(new Item("Book", 499.0));

cart.setPaymentStrategy(new UPIPayment("ajay@okicici"));
cart.checkout();   // Pays via UPI

cart.setPaymentStrategy(new WalletPayment("PAYTM_123", 1000.0));
cart.checkout();   // Now pays via Wallet — cart code unchanged
```

### Strategy vs OCP
Strategy is the primary mechanism that enforces OCP. Adding a new payment method = new class implementing `PaymentStrategy`. Zero modification to `ShoppingCart`.

### SOLID Connection: OCP + DIP + SRP (one algorithm per class)

---

## Pattern 2 — Observer

### Intent
Define a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically.

### The Problem It Solves
When a change in one object requires updating many others, and you don't know how many objects need to change. Decouples the publisher (subject) from subscribers (observers).

### Implementation — Stock Ticker

```java
// Observer interface — all subscribers implement this
interface StockObserver {
    void update(String stockSymbol, double price, double changePercent);
}

// Subject interface
interface StockSubject {
    void addObserver(StockObserver observer);
    void removeObserver(StockObserver observer);
    void notifyObservers();
}

// Concrete Subject — the stock ticker
class StockTicker implements StockSubject {
    private final List<StockObserver> observers = new ArrayList<>();
    private final Map<String, Double> stockPrices = new HashMap<>();

    public void addObserver(StockObserver o)    { observers.add(o); }
    public void removeObserver(StockObserver o) { observers.remove(o); }

    public void updateStockPrice(String symbol, double newPrice) {
        double oldPrice  = stockPrices.getOrDefault(symbol, newPrice);
        double changePct = ((newPrice - oldPrice) / oldPrice) * 100;
        stockPrices.put(symbol, newPrice);
        notifyObservers(symbol, newPrice, changePct);
    }

    private void notifyObservers(String symbol, double price, double changePct) {
        observers.forEach(o -> o.update(symbol, price, changePct));
    }

    @Override
    public void notifyObservers() { /* full-refresh version */ }
}

// Concrete Observers
class MobileApp implements StockObserver {
    private final String userId;

    public MobileApp(String userId) { this.userId = userId; }

    @Override
    public void update(String symbol, double price, double changePct) {
        String direction = changePct >= 0 ? "📈" : "📉";
        System.out.printf("[%s Mobile] %s: ₹%.2f %s %.2f%%%n",
            userId, symbol, price, direction, changePct);
    }
}

class AlertService implements StockObserver {
    private final Map<String, Double> thresholds = new HashMap<>();

    public void setAlert(String symbol, double threshold) {
        thresholds.put(symbol, threshold);
    }

    @Override
    public void update(String symbol, double price, double changePct) {
        Double threshold = thresholds.get(symbol);
        if (threshold != null && Math.abs(changePct) >= threshold) {
            System.out.println("🚨 ALERT: " + symbol + " moved " + changePct + "%!");
        }
    }
}

// Usage
StockTicker ticker = new StockTicker();
ticker.addObserver(new MobileApp("ajay_123"));
ticker.addObserver(new AlertService());

ticker.updateStockPrice("RELIANCE", 2850.0);  // Both observers notified
ticker.updateStockPrice("TCS", 3950.0);        // Both observers notified
```

### Push vs Pull Model
```
Push model (above): Subject pushes data to observers in update() call
  ✓ Observer gets exactly what it needs immediately
  ✗ Observer must accept ALL data even if it doesn't need it

Pull model: Subject calls update(this) — observer pulls what it needs
  ✓ Observer fetches only what it needs
  ✗ Observer must know Subject's API
```

### Real-world examples
- **Java `EventListener`:** `ActionListener`, `MouseListener` — all Observer pattern
- **Spring `ApplicationEvent`:** publish/subscribe across beans
- **RxJava / Reactor:** reactive streams are Observer at scale
- **Kafka:** producer (subject) → topic → consumers (observers)

---

## Pattern 3 — Chain of Responsibility

### Intent
Give more than one object a chance to handle a request. Chain the receiving objects and pass the request along the chain until an object handles it.

### The Problem It Solves
When you want to decouple sender from receiver, or when multiple handlers could process a request and the handler isn't known upfront.

### Implementation — ATM Cash Dispenser

```java
// Handler interface
abstract class CashHandler {
    protected CashHandler next;

    public CashHandler setNext(CashHandler next) {
        this.next = next;
        return next;  // Enables fluent chaining: h1.setNext(h2).setNext(h3)
    }

    public abstract void dispense(int amount);
}

// Concrete Handlers — each handles one denomination
class TwoThousandHandler extends CashHandler {
    @Override
    public void dispense(int amount) {
        int notes = amount / 2000;
        int remainder = amount % 2000;
        if (notes > 0) System.out.println("Dispensing " + notes + " × ₹2000 notes");
        if (remainder > 0 && next != null) next.dispense(remainder);
    }
}

class FiveHundredHandler extends CashHandler {
    @Override
    public void dispense(int amount) {
        int notes = amount / 500;
        int remainder = amount % 500;
        if (notes > 0) System.out.println("Dispensing " + notes + " × ₹500 notes");
        if (remainder > 0 && next != null) next.dispense(remainder);
    }
}

class HundredHandler extends CashHandler {
    @Override
    public void dispense(int amount) {
        int notes = amount / 100;
        int remainder = amount % 100;
        if (notes > 0) System.out.println("Dispensing " + notes + " × ₹100 notes");
        if (remainder > 0) System.out.println("Cannot dispense ₹" + remainder + " — smallest denomination");
    }
}

// Setup the chain
CashHandler dispenser = new TwoThousandHandler();
dispenser.setNext(new FiveHundredHandler())
         .setNext(new HundredHandler());

// Usage
dispenser.dispense(3700);
// Output:
// Dispensing 1 × ₹2000 notes
// Dispensing 3 × ₹500 notes
// Dispensing 2 × ₹100 notes
```

### Real-world CoR examples
- **Servlet Filters / Spring Interceptors:** each filter handles part of request (auth → logging → compression)
- **Exception handling:** catch chains — each catch handles specific exception type
- **Middleware in Express.js:** `app.use(logger).use(auth).use(rateLimiter)`
- **Support escalation:** L1 → L2 → L3 support tickets

### When to Use
✅ Multiple handlers but handler isn't known upfront  
✅ More than one object can handle a request  
✅ Set of handlers changes dynamically  
✅ Request must pass through multiple handlers (logging pipeline)

---

## Pattern 4 — State

### Intent
Allow an object to alter its behaviour when its internal state changes. The object will appear to change its class.

### The Problem It Solves
When an object's behaviour depends heavily on its current state and it must change behaviour at runtime. Eliminates large if/else or switch statements based on state.

### Implementation — Vending Machine

```java
// State interface — all states implement the same operations
interface VendingMachineState {
    void insertCoin(VendingMachine machine, int amount);
    void selectProduct(VendingMachine machine, String productCode);
    void dispense(VendingMachine machine);
    void cancel(VendingMachine machine);
}

// Context — the Vending Machine
class VendingMachine {
    private VendingMachineState currentState;
    private int insertedAmount = 0;
    private Map<String, Product> inventory;

    public VendingMachine() {
        this.currentState = new IdleState();
        this.inventory    = new HashMap<>();
    }

    // Delegates all operations to current state
    public void insertCoin(int amount) { currentState.insertCoin(this, amount); }
    public void selectProduct(String code) { currentState.selectProduct(this, code); }
    public void dispense()  { currentState.dispense(this); }
    public void cancel()    { currentState.cancel(this); }

    // State transition — called by states
    public void setState(VendingMachineState state) { this.currentState = state; }

    // Accessors used by states
    public int     getInsertedAmount()              { return insertedAmount; }
    public void    setInsertedAmount(int amount)    { this.insertedAmount = amount; }
    public Product getProduct(String code)          { return inventory.get(code); }
    public String  getCurrentStateName()            { return currentState.getClass().getSimpleName(); }
}

// Concrete States
class IdleState implements VendingMachineState {
    @Override
    public void insertCoin(VendingMachine m, int amount) {
        m.setInsertedAmount(amount);
        System.out.println("Coin inserted: ₹" + amount);
        m.setState(new HasMoneyState());  // Transition!
    }

    @Override
    public void selectProduct(VendingMachine m, String code) {
        System.out.println("Please insert coin first");
    }

    @Override
    public void dispense(VendingMachine m) { System.out.println("Insert coin first"); }

    @Override
    public void cancel(VendingMachine m)   { System.out.println("Nothing to cancel"); }
}

class HasMoneyState implements VendingMachineState {
    private String selectedCode;

    @Override
    public void insertCoin(VendingMachine m, int amount) {
        m.setInsertedAmount(m.getInsertedAmount() + amount);
        System.out.println("Added ₹" + amount + ". Total: ₹" + m.getInsertedAmount());
    }

    @Override
    public void selectProduct(VendingMachine m, String code) {
        Product p = m.getProduct(code);
        if (p == null) { System.out.println("Product not found"); return; }
        if (m.getInsertedAmount() < p.getPrice()) {
            System.out.println("Insufficient amount. Need ₹" + (p.getPrice() - m.getInsertedAmount()) + " more");
            return;
        }
        this.selectedCode = code;
        m.setState(new DispensingState(code));
        m.dispense();  // Auto-dispense once selected
    }

    @Override
    public void dispense(VendingMachine m) { System.out.println("Select a product first"); }

    @Override
    public void cancel(VendingMachine m) {
        System.out.println("Returning ₹" + m.getInsertedAmount());
        m.setInsertedAmount(0);
        m.setState(new IdleState());
    }
}

class DispensingState implements VendingMachineState {
    private final String productCode;

    public DispensingState(String code) { this.productCode = code; }

    @Override
    public void dispense(VendingMachine m) {
        Product p = m.getProduct(productCode);
        int change = m.getInsertedAmount() - p.getPrice();
        System.out.println("Dispensing: " + p.getName());
        if (change > 0) System.out.println("Returning change: ₹" + change);
        m.setInsertedAmount(0);
        m.setState(new IdleState());  // Back to idle
    }

    @Override
    public void insertCoin(VendingMachine m, int a) { System.out.println("Dispensing in progress"); }
    @Override
    public void selectProduct(VendingMachine m, String c) { System.out.println("Dispensing in progress"); }
    @Override
    public void cancel(VendingMachine m) { System.out.println("Cannot cancel — dispensing"); }
}
```

### State vs Strategy
```
State:    Object changes behaviour as its INTERNAL STATE changes
          States know about each other (transitions)
          Context typically transitions automatically

Strategy: Algorithm swapped EXTERNALLY by the client
          Strategies don't know each other
          Client picks which strategy to use
```

---

## Pattern 5 — Command

### Intent
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

### The Problem It Solves
When you need to decouple the object that invokes an operation from the object that performs it. Also the key pattern for implementing undo/redo.

### Implementation — Smart Home + Undo

```java
// Command interface
interface Command {
    void execute();
    void undo();
}

// Receivers — the objects that do the actual work
class Light {
    private boolean on = false;
    private final String location;

    public Light(String location) { this.location = location; }

    public void turnOn()  { on = true;  System.out.println(location + " light ON"); }
    public void turnOff() { on = false; System.out.println(location + " light OFF"); }
}

class AirConditioner {
    private int temperature = 24;

    public void setTemperature(int temp) {
        this.temperature = temp;
        System.out.println("AC set to " + temp + "°C");
    }

    public int getTemperature() { return temperature; }
}

// Concrete Commands
class LightOnCommand implements Command {
    private final Light light;

    public LightOnCommand(Light light) { this.light = light; }

    @Override public void execute() { light.turnOn(); }
    @Override public void undo()    { light.turnOff(); }
}

class LightOffCommand implements Command {
    private final Light light;

    public LightOffCommand(Light light) { this.light = light; }

    @Override public void execute() { light.turnOff(); }
    @Override public void undo()    { light.turnOn(); }
}

class ACTemperatureCommand implements Command {
    private final AirConditioner ac;
    private final int newTemp;
    private int prevTemp;  // Saved for undo

    public ACTemperatureCommand(AirConditioner ac, int newTemp) {
        this.ac      = ac;
        this.newTemp = newTemp;
    }

    @Override
    public void execute() {
        prevTemp = ac.getTemperature();  // Save current for undo
        ac.setTemperature(newTemp);
    }

    @Override
    public void undo() {
        ac.setTemperature(prevTemp);     // Restore previous
    }
}

// Macro Command — execute multiple commands as one
class MacroCommand implements Command {
    private final List<Command> commands;

    public MacroCommand(List<Command> commands) { this.commands = commands; }

    @Override
    public void execute() { commands.forEach(Command::execute); }

    @Override
    public void undo() {
        // Undo in reverse order!
        ListIterator<Command> it = commands.listIterator(commands.size());
        while (it.hasPrevious()) it.previous().undo();
    }
}

// Invoker — the remote control / smart home hub
class SmartHomeController {
    private final Deque<Command> history = new ArrayDeque<>();

    public void execute(Command command) {
        command.execute();
        history.push(command);  // Push to undo stack
    }

    public void undo() {
        if (history.isEmpty()) { System.out.println("Nothing to undo"); return; }
        Command last = history.pop();
        last.undo();
    }

    public void undoAll() {
        while (!history.isEmpty()) undo();
    }
}

// Usage
Light        bedroomLight = new Light("Bedroom");
AirConditioner ac         = new AirConditioner();
SmartHomeController hub   = new SmartHomeController();

hub.execute(new LightOnCommand(bedroomLight));
hub.execute(new ACTemperatureCommand(ac, 20));
hub.execute(new LightOffCommand(bedroomLight));

hub.undo();  // Re-turns light ON
hub.undo();  // Sets AC back to 24
hub.undo();  // Turns light OFF
```

---

## Pattern 6 — Template Method

### Intent
Define the **skeleton of an algorithm** in a base class, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps without changing the algorithm's structure.

### The Problem It Solves
When multiple classes share the same algorithm skeleton but differ in specific steps. Avoids code duplication while allowing customisation at specific extension points.

### Implementation — Data Migration Pipeline

```java
// Abstract class defines the TEMPLATE (skeleton)
abstract class DataMigrationPipeline {

    // Template Method — final so nobody reorders steps
    public final void migrate() {
        extractData();
        validateData();
        transformData();
        loadData();
        notifyCompletion();
    }

    // Required to override (abstract)
    protected abstract void extractData();
    protected abstract void transformData();
    protected abstract void loadData();

    // Optional hook — subclass may override or not
    protected void validateData() {
        System.out.println("Default validation: schema check");
    }

    protected void notifyCompletion() {
        System.out.println("Migration complete");
    }
}

// Concrete Pipelines
class MySQLToPostgresMigration extends DataMigrationPipeline {
    @Override
    protected void extractData() {
        System.out.println("Extracting from MySQL: SELECT * FROM legacy_db");
    }

    @Override
    protected void transformData() {
        System.out.println("Converting MySQL ENUM → Postgres text/check constraints");
        System.out.println("Converting TINYINT(1) → BOOLEAN");
    }

    @Override
    protected void loadData() {
        System.out.println("COPY INTO Postgres via JDBC batch insert");
    }

    @Override
    protected void validateData() {
        System.out.println("Validating row counts, FK integrity, data types");
    }
}

class CSVToMongoMigration extends DataMigrationPipeline {
    @Override
    protected void extractData() {
        System.out.println("Reading CSV files from S3 bucket");
    }

    @Override
    protected void transformData() {
        System.out.println("Flattening CSV rows into JSON documents");
        System.out.println("Adding metadata fields");
    }

    @Override
    protected void loadData() {
        System.out.println("Bulk insert into MongoDB collection");
    }
    // Uses default validateData() and notifyCompletion()
}

// Usage
DataMigrationPipeline migration = new MySQLToPostgresMigration();
migration.migrate();  // Calls steps in correct order, every time
```

### Hollywood Principle
> "Don't call us, we'll call you."
The base class calls the subclass's methods — not the other way around. Subclasses don't control the flow; they just implement the steps.

### Template Method vs Strategy
```
Template Method: Variation through INHERITANCE — subclass overrides steps
                 Algorithm skeleton in base class; steps in subclasses
                 Compile-time decision

Strategy:        Variation through COMPOSITION — inject different algorithm
                 Entire algorithm swappable via interface
                 Runtime decision
```

---

## Pattern 7 — Iterator

### Intent
Provide a way to access elements of an aggregate object sequentially without exposing its underlying representation.

### Implementation — Custom Playlist Iterator

```java
interface Iterator<T> {
    boolean hasNext();
    T       next();
}

interface Iterable<T> {
    Iterator<T> createIterator();
}

class Song {
    String title, artist;
    Song(String t, String a) { title = t; artist = a; }
}

class Playlist implements Iterable<Song> {
    private final List<Song> songs = new ArrayList<>();
    private final String name;

    public Playlist(String name) { this.name = name; }
    public void addSong(Song s)  { songs.add(s); }

    @Override
    public Iterator<Song> createIterator() {
        return new PlaylistIterator(songs);
    }

    // Inner iterator — knows the internal structure
    private static class PlaylistIterator implements Iterator<Song> {
        private final List<Song> songs;
        private int index = 0;

        PlaylistIterator(List<Song> songs) { this.songs = songs; }

        @Override
        public boolean hasNext() { return index < songs.size(); }

        @Override
        public Song next() {
            if (!hasNext()) throw new NoSuchElementException();
            return songs.get(index++);
        }
    }
}

// Client — doesn't know if internal structure is List, Array, Tree...
Playlist playlist = new Playlist("Workout Mix");
playlist.addSong(new Song("Eye of the Tiger", "Survivor"));
playlist.addSong(new Song("Lose Yourself", "Eminem"));

Iterator<Song> it = playlist.createIterator();
while (it.hasNext()) {
    Song s = it.next();
    System.out.println(s.title + " by " + s.artist);
}
```

---

## Pattern 8 — Mediator

### Intent
Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly.

### The Problem It Solves
When multiple objects communicate directly with each other, creating a tangled web of dependencies. Mediator routes all communication through a central hub.

### Implementation — Air Traffic Control

```java
// Mediator interface
interface AirTrafficControl {
    void requestLanding(Aircraft aircraft);
    void requestTakeoff(Aircraft aircraft);
    void notifyAll(String message, Aircraft source);
}

// Colleague — Aircraft
abstract class Aircraft {
    protected final AirTrafficControl atc;
    protected final String            flightId;

    public Aircraft(AirTrafficControl atc, String flightId) {
        this.atc      = atc;
        this.flightId = flightId;
    }

    public void land()   { atc.requestLanding(this); }
    public void takeoff() { atc.requestTakeoff(this); }

    public abstract void receive(String message);

    public String getFlightId() { return flightId; }
}

class CommercialFlight extends Aircraft {
    public CommercialFlight(AirTrafficControl atc, String id) { super(atc, id); }

    @Override
    public void receive(String message) {
        System.out.println("[" + flightId + "] Received: " + message);
    }
}

// Concrete Mediator — the ATC tower
class ATCTower implements AirTrafficControl {
    private final List<Aircraft>  aircraft = new ArrayList<>();
    private       boolean         runwayClear = true;
    private final Queue<Aircraft> landingQueue = new LinkedList<>();

    public void registerAircraft(Aircraft a) { aircraft.add(a); }

    @Override
    public void requestLanding(Aircraft requesting) {
        if (runwayClear) {
            runwayClear = false;
            notifyAll("Runway " + requesting.getFlightId() + " landing — hold pattern", requesting);
            System.out.println("[ATC] " + requesting.getFlightId() + " cleared to land");
            // Simulate landing complete
            runwayClear = true;
            processQueue();
        } else {
            landingQueue.offer(requesting);
            requesting.receive("Enter holding pattern — runway busy");
        }
    }

    @Override
    public void requestTakeoff(Aircraft requesting) {
        if (runwayClear) {
            runwayClear = false;
            System.out.println("[ATC] " + requesting.getFlightId() + " cleared for takeoff");
            runwayClear = true;
        } else {
            requesting.receive("Hold — runway busy");
        }
    }

    @Override
    public void notifyAll(String message, Aircraft source) {
        aircraft.stream()
            .filter(a -> !a.equals(source))
            .forEach(a -> a.receive(message));
    }

    private void processQueue() {
        if (!landingQueue.isEmpty()) requestLanding(landingQueue.poll());
    }
}

// Aircraft talk ONLY to ATC — never to each other directly
ATCTower atc = new ATCTower();
CommercialFlight ai101 = new CommercialFlight(atc, "AI-101");
CommercialFlight ek500 = new CommercialFlight(atc, "EK-500");

atc.registerAircraft(ai101);
atc.registerAircraft(ek500);

ai101.land();    // Requests landing via ATC
ek500.land();    // ATC queues it, notifies AI-101
```

---

## Pattern 9 — Memento

### Intent
Without violating encapsulation, capture and externalise an object's internal state so the object can be restored to that state later.

### The Problem It Solves
Undo/redo, snapshots, transactions. You need to save state but don't want to expose the internals of the object.

### Implementation — Text Editor Undo

```java
// Memento — snapshot of editor state (immutable)
class EditorMemento {
    private final String  content;
    private final int     cursorPosition;
    private final Instant timestamp;

    public EditorMemento(String content, int cursorPos) {
        this.content        = content;
        this.cursorPosition = cursorPos;
        this.timestamp      = Instant.now();
    }

    // Only the originator can access state — package-private
    String getContent()        { return content; }
    int    getCursorPosition() { return cursorPosition; }
    Instant getTimestamp()     { return timestamp; }
}

// Originator — the text editor
class TextEditor {
    private StringBuilder content = new StringBuilder();
    private int cursorPosition = 0;

    public void type(String text) {
        content.insert(cursorPosition, text);
        cursorPosition += text.length();
    }

    public void delete(int chars) {
        int start = Math.max(0, cursorPosition - chars);
        content.delete(start, cursorPosition);
        cursorPosition = start;
    }

    public void moveCursor(int pos) {
        cursorPosition = Math.max(0, Math.min(pos, content.length()));
    }

    // Save state
    public EditorMemento save() {
        return new EditorMemento(content.toString(), cursorPosition);
    }

    // Restore state
    public void restore(EditorMemento memento) {
        this.content        = new StringBuilder(memento.getContent());
        this.cursorPosition = memento.getCursorPosition();
        System.out.println("Restored to: '" + content + "' cursor@" + cursorPosition);
    }

    public String getContent() { return content.toString(); }
}

// Caretaker — manages undo stack, doesn't look inside mementos
class UndoManager {
    private final Deque<EditorMemento> undoStack = new ArrayDeque<>();
    private final Deque<EditorMemento> redoStack = new ArrayDeque<>();

    public void save(EditorMemento state) {
        undoStack.push(state);
        redoStack.clear();  // New action clears redo history
    }

    public EditorMemento undo(EditorMemento current) {
        if (undoStack.isEmpty()) return current;
        redoStack.push(current);
        return undoStack.pop();
    }

    public EditorMemento redo(EditorMemento current) {
        if (redoStack.isEmpty()) return current;
        undoStack.push(current);
        return redoStack.pop();
    }
}

// Usage
TextEditor editor = new TextEditor();
UndoManager undo  = new UndoManager();

undo.save(editor.save());        // Save initial state
editor.type("Hello");
undo.save(editor.save());        // Save after "Hello"
editor.type(" World");
undo.save(editor.save());        // Save after " World"
editor.type("!!!");

editor.restore(undo.undo(editor.save()));  // Undo → "Hello World"
editor.restore(undo.undo(editor.save()));  // Undo → "Hello"
editor.restore(undo.redo(editor.save()));  // Redo → "Hello World"
```

---

## Pattern 10 — Visitor

### Intent
Represent an operation to be performed on elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

### The Problem It Solves
When you need to perform many distinct and unrelated operations across objects in a hierarchy without polluting their classes. Add operations without modifying the element classes.

### Implementation — Tax Calculator

```java
// Visitor interface — one visit() per element type
interface TaxVisitor {
    double visit(Book book);
    double visit(Electronics electronics);
    double visit(Food food);
}

// Element interface — accepts a visitor
interface Product {
    double getPrice();
    double accept(TaxVisitor visitor);  // Double dispatch!
}

// Concrete Elements
class Book implements Product {
    private final double price;
    private final boolean educational;

    public Book(double price, boolean educational) {
        this.price       = price;
        this.educational = educational;
    }

    public double getPrice()           { return price; }
    public boolean isEducational()     { return educational; }

    @Override
    public double accept(TaxVisitor visitor) {
        return visitor.visit(this);  // Passes itself to visitor
    }
}

class Electronics implements Product {
    private final double price;
    private final int    wattage;

    public Electronics(double price, int wattage) {
        this.price   = price;
        this.wattage = wattage;
    }

    public double getPrice()  { return price; }
    public int    getWattage(){ return wattage; }

    @Override
    public double accept(TaxVisitor visitor) { return visitor.visit(this); }
}

class Food implements Product {
    private final double price;
    private final boolean processed;

    public Food(double price, boolean processed) {
        this.price     = price;
        this.processed = processed;
    }

    public double getPrice()    { return price; }
    public boolean isProcessed(){ return processed; }

    @Override
    public double accept(TaxVisitor visitor) { return visitor.visit(this); }
}

// Concrete Visitors — each is a complete tax rule set
class GSTCalculator implements TaxVisitor {
    @Override
    public double visit(Book book) {
        // Educational books: 0% GST; others: 12%
        return book.isEducational() ? 0 : book.getPrice() * 0.12;
    }

    @Override
    public double visit(Electronics electronics) {
        // High-wattage appliances: 28% GST; others: 18%
        return electronics.getWattage() > 1500
            ? electronics.getPrice() * 0.28
            : electronics.getPrice() * 0.18;
    }

    @Override
    public double visit(Food food) {
        // Processed food: 12% GST; fresh: 0%
        return food.isProcessed() ? food.getPrice() * 0.12 : 0;
    }
}

class ImportDutyCalculator implements TaxVisitor {
    @Override
    public double visit(Book book)         { return 0; }             // No import duty on books
    @Override
    public double visit(Electronics e)     { return e.getPrice() * 0.15; } // 15% import duty
    @Override
    public double visit(Food food)         { return food.getPrice() * 0.05; }
}

// Usage — add new tax rule (new Visitor) without touching Book/Electronics/Food
List<Product> cart = List.of(
    new Book(500, true),
    new Electronics(25000, 2000),
    new Food(200, true)
);

TaxVisitor gst    = new GSTCalculator();
TaxVisitor import_ = new ImportDutyCalculator();

double totalGST = cart.stream().mapToDouble(p -> p.accept(gst)).sum();
double totalDuty = cart.stream().mapToDouble(p -> p.accept(import_)).sum();
```

---

## Pattern 11 — Null Object

### Intent
Provide a default object with do-nothing behaviour to avoid null checks throughout the codebase.

### The Problem It Solves
Null pointer exceptions from forgotten null checks. Replaces `if (obj != null) obj.doSomething()` with a safe default object that does nothing (or returns sensible defaults).

### Implementation — Logger

```java
interface Logger {
    void log(String message);
    void warn(String message);
    void error(String message);
}

// Real implementation
class ConsoleLogger implements Logger {
    @Override public void log(String msg)   { System.out.println("[LOG] " + msg); }
    @Override public void warn(String msg)  { System.out.println("[WARN] " + msg); }
    @Override public void error(String msg) { System.err.println("[ERROR] " + msg); }
}

// NULL OBJECT — implements same interface but does nothing
class NullLogger implements Logger {
    @Override public void log(String msg)   { /* no-op */ }
    @Override public void warn(String msg)  { /* no-op */ }
    @Override public void error(String msg) { /* no-op */ }
}

// Usage — no null checks needed anywhere
class PaymentService {
    private final Logger logger;

    // If no logger provided, use NullLogger — never null
    public PaymentService(Logger logger) {
        this.logger = logger != null ? logger : new NullLogger();
    }

    public void processPayment(double amount) {
        logger.log("Processing payment: ₹" + amount);  // Safe — always
        // ... payment logic ...
        logger.log("Payment complete");
    }
}

// User with logging
new PaymentService(new ConsoleLogger()).processPayment(999);

// User without logging — no null check needed in PaymentService
new PaymentService(null).processPayment(999);
// Or explicitly:
new PaymentService(new NullLogger()).processPayment(999);
```

---

## Pattern 12 — Interpreter

### Intent
Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

### The Problem It Solves
When you need to interpret expressions in a simple language or DSL — like SQL WHERE clauses, mathematical expressions, regular expressions, or configuration rules.

### Implementation — Math Expression Parser

```java
// Abstract expression
interface Expression {
    int interpret(Map<String, Integer> context);
}

// Terminal expressions (leaves)
class NumberExpression implements Expression {
    private final int number;
    public NumberExpression(int n) { this.number = n; }
    @Override public int interpret(Map<String, Integer> ctx) { return number; }
}

class VariableExpression implements Expression {
    private final String name;
    public VariableExpression(String name) { this.name = name; }
    @Override public int interpret(Map<String, Integer> ctx) {
        return ctx.getOrDefault(name, 0);
    }
}

// Non-terminal expressions (composites)
class AddExpression implements Expression {
    private final Expression left, right;
    public AddExpression(Expression l, Expression r) { left=l; right=r; }
    @Override public int interpret(Map<String, Integer> ctx) {
        return left.interpret(ctx) + right.interpret(ctx);
    }
}

class MultiplyExpression implements Expression {
    private final Expression left, right;
    public MultiplyExpression(Expression l, Expression r) { left=l; right=r; }
    @Override public int interpret(Map<String, Integer> ctx) {
        return left.interpret(ctx) * right.interpret(ctx);
    }
}

// Usage: interpret "a + b * 3" = a + (b * 3)
Map<String, Integer> vars = Map.of("a", 5, "b", 4);

Expression expr = new AddExpression(
    new VariableExpression("a"),
    new MultiplyExpression(
        new VariableExpression("b"),
        new NumberExpression(3)
    )
);

int result = expr.interpret(vars);  // 5 + (4 * 3) = 17
```

---

## 📝 Tasks

### Task 1 — Pattern Recognition (6 Scenarios)
Identify the correct Behavioral pattern and justify in 2 sentences:

1. A text editor needs Ctrl+Z undo that works for bold, italic, insert, delete operations.
2. A social media app needs to notify followers when a user posts. Follower list changes dynamically.
3. A loan application passes through Credit Check → Income Verification → Background Check → Final Approval. Each step may approve or escalate.
4. A traffic light cycles through RED → GREEN → YELLOW → RED. The valid actions at each phase differ.
5. A zip utility needs to support DEFLATE, BZIP2, LZMA algorithms, switchable at runtime based on file type.
6. A shopping cart has Products. You need to calculate: total price, total weight, customs duty — as separate passes without adding methods to Product.

### Task 2 — Observer: Event Bus
Implement a generic `EventBus` (publish/subscribe system):
- `subscribe(eventType, handler)`: register a handler for an event type
- `unsubscribe(eventType, handler)`: remove a handler
- `publish(event)`: notify all handlers subscribed to that event type
- Support multiple event types: `OrderPlaced`, `PaymentFailed`, `ItemShipped`
- Thread-safe: multiple threads can publish/subscribe concurrently

### Task 3 — Strategy + Template Method
Implement a `ReportGenerator` that:
- Template Method defines the skeleton: gatherData() → processData() → formatOutput() → deliver()
- `HTMLReportGenerator` and `PDFReportGenerator` implement `formatOutput()` differently
- `EmailDelivery` and `SlackDelivery` implement `deliver()` differently
- Use Strategy for the delivery method (injected, swappable at runtime)
- Template Method for the overall pipeline structure (fixed skeleton)
- Show that you can mix: PDF + Email, HTML + Slack, HTML + Email

### ⭐ Mini Project — BookMyShow (LLD + Concurrency)
Design BookMyShow with real concurrency handling:

**Requirements:**
1. Browse movies playing in a city
2. Select show time + screen
3. Book seats (handle concurrent users trying to book same seat)
4. Payment processing with retry
5. Booking confirmation with ticket
6. Cancellation with refund policy

**Patterns required:**
- State: `Seat` (AVAILABLE → LOCKED → BOOKED → CANCELLED)
- Observer: Notify user on booking confirmation / cancellation
- Command: Book seat, cancel booking (undoable)
- Strategy: Pricing strategy (weekend vs weekday, VIP vs regular)
- Chain of Responsibility: Payment → BookingService → NotificationService
- Facade: `BookingFacade` hides all subsystem complexity

**Critical: Concurrency handling**
```java
// Seat must be locked before booking — prevent double booking
class Seat {
    private volatile SeatState state = SeatState.AVAILABLE;
    private final ReentrantLock lock = new ReentrantLock();

    public boolean tryLock(String userId, long timeoutMs) {
        try {
            if (lock.tryLock(timeoutMs, TimeUnit.MILLISECONDS)) {
                if (state == SeatState.AVAILABLE) {
                    state = SeatState.LOCKED;
                    this.lockedBy = userId;
                    scheduleLockExpiry(5_000); // 5s timeout
                    return true;
                }
                lock.unlock();
            }
        } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        return false;
    }
}
```

---

## 💡 Interview Tips — Behavioral Patterns

| Pattern | One-liner | When to reach for it |
|---------|-----------|---------------------|
| Strategy | "Swap algorithms at runtime via interface" | if/else on algorithm type |
| Observer | "Publisher notifies subscribers automatically" | One change → many notifications |
| CoR | "Pass request along a chain until handled" | Multiple possible handlers, unknown upfront |
| State | "Behaviour changes when state changes" | switch/if on state field that grows |
| Command | "Encapsulate request as object for undo/queue" | Need undo, retry, queue, or logging of operations |
| Template Method | "Fixed skeleton, variable steps via inheritance" | Same algorithm structure, different implementations |
| Iterator | "Traverse without exposing internals" | Custom collection with sequential access |
| Mediator | "Central hub decouples many-to-many peers" | N objects all talk to each other (N² connections) |
| Memento | "Snapshot state for undo without breaking encapsulation" | Need save/restore; can't expose internals |
| Visitor | "New operations without changing element classes" | Many operations on stable class hierarchy |
| Null Object | "Default do-nothing object eliminates null checks" | Everywhere you'd pass null as optional dep |
| Interpreter | "Evaluate grammar/DSL expressions" | Building an expression evaluator, rules engine |

**The most commonly confused:**
> "Strategy swaps the whole algorithm; Template Method keeps the skeleton and varies steps. Strategy uses composition (inject); Template Method uses inheritance (override)."

---

## ✅ Module A4 Completion Checklist

- [ ] Can implement Strategy, Observer, CoR, State, Command from memory
- [ ] Can implement Template Method, Iterator, Mediator, Memento, Visitor from memory
- [ ] Know Null Object and Interpreter well enough to explain and apply
- [ ] Can distinguish Strategy vs Template Method vs State clearly
- [ ] Know Observer's push vs pull model trade-offs
- [ ] Understand Command's role in undo/redo and command queuing
- [ ] Understand double dispatch in Visitor
- [ ] Completed Task 1 — Pattern Recognition (6 scenarios)
- [ ] Completed Task 2 — Thread-safe EventBus (Observer)
- [ ] Completed Task 3 — ReportGenerator (Template Method + Strategy)
- [ ] Completed Mini Project — BookMyShow with concurrency (all 6 patterns)

**→ When complete: Ready for Module A5 — Concurrency in LLD**

<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="/learning/system-design/lld/module-a4-behavioral/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:#fb7185;text-decoration:none;font-weight:700;">⚡ Open Interactive Version</a>
  <a href="/learning/system-design/system-design-roadmap/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(30,42,64,0.6);border:1px solid #263450;color:#d4deff;text-decoration:none;font-weight:600;">↑ Back to Roadmap</a>
</div>
