---
title: "Module A2 — Creational Patterns Notes"
description: "System Design Roadmap › Module A2 › Full Notes Module A2 — Creational Patterns Complete reference notes · Track A: LLD · Week 4 Singleton Factory Method Abstract Factory…"
domain: system-design
track: system-design-lld
order: 5
chrome: bare
ownHeader: true
url: /learning/system-design/lld/module-a2-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero" style="--ch-1:#f0a500;--ch-2:#cf7500;">
  <div class="breadcrumb">
    <a href="/learning/system-design/system-design-roadmap/">System Design Roadmap</a>
    <span class="separator">›</span>
    <a href="/learning/system-design/lld/module-a2-creational/">Module A2</a>
    <span class="separator">›</span>
    <span class="current">Full Notes</span>
  </div>
  <h1>Module A2 — Creational Patterns</h1>
  <p class="ch-subtitle">Complete reference notes · Track A: LLD · Week 4</p>
  <div class="hero-stats">
    <span class="stat-badge">Singleton</span>
    <span class="stat-badge">Factory Method</span>
    <span class="stat-badge">Abstract Factory</span>
    <span class="stat-badge">Builder</span>
    <span class="stat-badge">Prototype</span>
  </div>
</div>
<div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
  <a href="/learning/system-design/lld/module-a2-creational/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.2rem;border-radius:8px;background:rgba(240,165,0,0.1);border:1px solid rgba(240,165,0,0.3);color:#f0a500;text-decoration:none;font-weight:700;font-size:0.85rem;">
    ⚡ Interactive Visual Version
  </a>
  <span style="color:var(--c-muted,#666);font-size:0.85rem;">← Recommended for learning. This page is the printable reference.</span>
</div>
<div class="insight-box">
  <div class="ib-title">Overview</div>
  <p>Creational design patterns abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented. As systems evolve, they often rely more on object composition than class inheritance, shifting the emphasis away from hard-coding a fixed set of behaviours toward defining a smaller set of fundamental behaviours that can be composed into any number of more complex ones. Thus, creating objects with specific behaviours requires more than simply instantiating a class.</p>
</div>

## 1. Singleton

**Definition:** Ensure a class has only one instance, and provide a global point of access to it.

**When to Use:**
*   When there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point (e.g., a central Logger, a configuration manager, a database connection pool).
*   When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code.

### Implementation: Enum Singleton (Preferred in Java)
Joshua Bloch (Effective Java) recommends the Enum approach. It provides built-in serialization machinery, guarantees against multiple instantiations, and handles reflection attacks perfectly.

```java
public enum ConfigManager {
    INSTANCE;

    private Map<String, String> properties;

    ConfigManager() {
        properties = new HashMap<>(); // load from file
    }

    public String getProperty(String key) {
        return properties.get(key);
    }
}
```

### Implementation: Double-Checked Locking (Thread-Safe)
If you explicitly need lazy initialization and cannot use Enums.

```java
public class DatabasePool {
    private static volatile DatabasePool instance;

    private DatabasePool() { 
        // private constructor prevents instantiation
    }

    public static DatabasePool getInstance() {
        if (instance == null) { // 1st check (no lock, fast-path)
            synchronized (DatabasePool.class) {
                if (instance == null) { // 2nd check (safe)
                    instance = new DatabasePool();
                }
            }
        }
        return instance;
    }
}
```
*Note: The `volatile` keyword is crucial. It ensures that multiple threads handle the `instance` variable correctly when it is being initialized.*

<div class="highlight-box">
  <h4>SOLID Impact: Singleton</h4>
  <p><strong>Violates SRP:</strong> The class manages its own lifecycle AND performs its primary business logic.<br>
  <strong>Recommendation:</strong> In modern architectures (e.g., Spring framework), use Dependency Injection containers to manage the "singleton" scope of an object, rather than hardcoding the Singleton pattern structurally.</p>
</div>

---

## 2. Factory Method

**Definition:** Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

**When to Use:**
*   A class can't anticipate the class of objects it must create.
*   A class wants its subclasses to specify the objects it creates.
*   Classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate.

**Real-world analogy:** A logistics company has a `TransportBuilder`. Its subclasses `RoadLogistics` and `SeaLogistics` decide whether to create a `Truck` or a `Ship`.

### Implementation Example

```java
// Product Interface
interface Notification {
    void send(String message);
}

// Concrete Products
class EmailNotification implements Notification {
    public void send(String msg) { System.out.println("Emailing: " + msg); }
}
class PushNotification implements Notification {
    public void send(String msg) { System.out.println("Pushing: " + msg); }
}

// Creator (The Factory)
abstract class NotificationCreator {
    public abstract Notification createNotification(); // Factory Method
    
    // Core business logic relying on the product
    public void broadcast(String msg) {
        Notification notification = createNotification();
        notification.send(msg);
    }
}

// Concrete Creators
class EmailCreator extends NotificationCreator {
    public Notification createNotification() { return new EmailNotification(); }
}
class PushCreator extends NotificationCreator {
    public Notification createNotification() { return new PushNotification(); }
}
```

---

## 3. Abstract Factory

**Definition:** Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

**Difference from Factory Method:**
*   **Factory Method** creates *one* product. It uses inheritance.
*   **Abstract Factory** creates a *family of related products*. It typically uses composition to delegate creation methods to different Factory objects.

**When to Use:**
*   A system should be independent of how its products are created, composed, and represented.
*   A system should be configured with one of multiple families of products (e.g., Mac UI vs. Windows UI).
*   You want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.

### Implementation Example

```java
// Abstract Factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// Concrete Factory 1: Mac
class MacFactory implements GUIFactory {
    public Button createButton() { return new MacButton(); }
    public Checkbox createCheckbox() { return new MacCheckbox(); }
}

// Concrete Factory 2: Win
class WinFactory implements GUIFactory {
    public Button createButton() { return new WinButton(); }
    public Checkbox createCheckbox() { return new WinCheckbox(); }
}

// Client Code: Injects the factory
class Application {
    private Button button;
    public Application(GUIFactory factory) {
        button = factory.createButton(); // Client doesn't care if it's Mac or Win
    }
}
```

---

## 4. Builder

**Definition:** Separate the construction of a complex object from its representation so that the same construction process can create different representations.

**When to Use:**
*   The algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
*   The construction process must allow different representations for the object that's constructed.
*   To solve the "Telescoping Constructor" anti-pattern (constructors with many optional parameters).

### Implementation

```java
public class UserProfile {
    // Final fields make the object immutable
    private final String firstName; // Required
    private final String lastName;  // Required
    private final int age;          // Optional
    private final String phone;     // Optional
    private final String address;   // Optional

    private UserProfile(Builder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
        this.phone = builder.phone;
        this.address = builder.address;
    }

    public static class Builder {
        private final String firstName;
        private final String lastName;
        private int age = 0;              // Default optional
        private String phone = "";        // Default optional
        private String address = "";      // Default optional

        public Builder(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder phone(String phone) {
            this.phone = phone;
            return this;
        }

        public Builder address(String address) {
            this.address = address;
            return this;
        }

        public UserProfile build() {
            // Validation logic goes here before object creation
            if(age < 0) throw new IllegalArgumentException("Age cannot be negative");
            return new UserProfile(this);
        }
    }
}

// Usage:
UserProfile user = new UserProfile.Builder("Ajay", "Dev")
                        .age(28)
                        .address("123 Tech Lane")
                        .build();
```

---

## 5. Prototype

**Definition:** Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

**When to Use:**
*   When the classes to instantiate are specified at run-time (dynamic loading).
*   To avoid building a class hierarchy of factories that parallels the class hierarchy of products.
*   When instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually each time.

### Implementation (Deep vs Shallow Clone)

Java's default `clone()` method provides a *shallow copy* (references to nested objects are shared). In System Design, you usually want a *deep copy*, executed manually via a Copy Constructor.

```java
abstract class Shape {
    public int x, y;
    public String color;

    // Copy constructor
    public Shape(Shape target) {
        if (target != null) {
            this.x = target.x;
            this.y = target.y;
            this.color = target.color;
        }
    }

    public abstract Shape clone();
}

class Circle extends Shape {
    public int radius;

    public Circle(Circle target) {
        super(target); // Copy parent properties
        if (target != null) {
            this.radius = target.radius;
        }
    }

    @Override
    public Shape clone() {
        return new Circle(this); // Passes itself to copy constructor
    }
}

// Registry used to cache prototypes
class ShapeRegistry {
    private Map<String, Shape> cache = new HashMap<>();

    public ShapeRegistry() {
        Circle circle = new Circle(null);
        circle.x = 10; circle.y = 10; circle.radius = 20; circle.color = "Red";
        cache.put("Big Red Circle", circle);
    } // Create expensive object ONCE

    public Shape get(String key) {
        return cache.get(key).clone(); // Return cloned instances cheaply
    }
}
```

---

## Comparison Summary Table

<div class="table-responsive">
<table class="insight-table">
  <thead>
    <tr>
      <th>Pattern</th>
      <th>Creates</th>
      <th>Mechanism</th>
      <th>Primary SOLID Principle Enforced</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Singleton</strong></td>
      <td>A single, globally accessible instance</td>
      <td>Private constructor + static accessor</td>
      <td>SRP (Though it often violates it practically, conceptually it manages one state globally).</td>
    </tr>
    <tr>
      <td><strong>Factory Method</strong></td>
      <td>One specific product object</td>
      <td>Subclass overrides a creator method</td>
      <td>OCP (Add new creators without modifying existing ones).</td>
    </tr>
    <tr>
      <td><strong>Abstract Factory</strong></td>
      <td>A family of related product objects</td>
      <td>Interface injection with multiple factory methods</td>
      <td>OCP and ISP (Interface Segregation).</td>
    </tr>
    <tr>
      <td><strong>Builder</strong></td>
      <td>A complex object, step-by-step</td>
      <td>Inner Builder class, chained setters, `build()` method</td>
      <td>SRP (Separates construction logic from the data model).</td>
    </tr>
    <tr>
      <td><strong>Prototype</strong></td>
      <td>A clone of an existing object</td>
      <td>`clone()` interfaces and copy constructors</td>
      <td>OCP (Cloning avoids concrete dependencies on classes).</td>
    </tr>
  </tbody>
</table>
</div>

---

<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="/learning/system-design/lld/module-a2-creational/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(240,165,0,0.1);border:1px solid rgba(240,165,0,0.3);color:#f0a500;text-decoration:none;font-weight:700;">⚡ Open Interactive Version</a>
  <a href="/learning/system-design/system-design-roadmap/" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.7rem 1.4rem;border-radius:8px;background:rgba(30,42,64,0.6);border:1px solid #263450;color:#d4deff;text-decoration:none;font-weight:600;">↑ Back to Roadmap</a>
</div>
