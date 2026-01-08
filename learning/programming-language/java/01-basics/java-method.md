---
layout: default
title: Java Methods – Declaration & Access Specifiers
---

# Java Methods – Declaration & Access Specifiers

Complete guide to method declaration, components, and access control in Java.

---

## Table of Contents

- [1. What Is a Method in Java?](#1-what-is-a-method-in-java)
- [2. Method Declaration Syntax](#2-method-declaration-syntax)
- [3. Access Specifiers](#3-access-specifiers)
- [4. Access Matrix](#4-access-matrix)
- [5. Real-World Design Insight](#5-real-world-design-insight)
- [6. Interview Takeaways](#6-interview-takeaways)
- [7. Types of Methods in Java](#7-types-of-methods-in-java)
 - [8. Final Methods in Java](#final-methods)
 - [9. Abstract Methods in Java](#abstract-methods)

## 1. What Is a Method in Java?

A method is a **block of code** that performs a specific task and runs only when called.

**Why methods matter:**
- Reusability of code
- Better readability
- Logical separation of functionality

**In simple terms:** a method defines *what to do* and *how to do it*, and it executes on demand.

---

## 2. Method Declaration Syntax

### 2.1 General Syntax

```java
accessModifier returnType methodName(parameters) {
    // method body
}
```

### 2.2 Components Explained

| Component | Purpose |
|---|---|
| **Access Modifier** | Controls visibility (`public`, `protected`, default, `private`) |
| **Return Type** | Specifies what the method returns (`int`, `String`, `void`, etc.) |
| **Method Name** | Identifier used to call the method (camelCase convention) |
| **Parameters** | Input values passed to the method (optional) |
| **Method Body** | Contains the logic to be executed |

### 2.3 Example with Return Value

```java
public int add(int a, int b) {
    return a + b;
}
```

**Breakdown:**
- `public` → accessible everywhere
- `int` → returns an integer
- `add` → method name
- `(int a, int b)` → parameters

### 2.4 Example: No Return Value

```java
public void printMessage() {
    System.out.println("Hello");
}
```

- `void` → returns nothing

---

## 3. Access Specifiers

Java provides **four access levels** to control method visibility across classes, packages, and inheritance hierarchies.

### 3.1 `public` Methods

**Concept:**
- Accessible from **anywhere**
- Across packages and inheritance

```java
public void getInvoice() { }
```

**Use case:** APIs and entry points

---

### 3.2 `private` Methods

**Concept:**
- Accessible **only inside the same class**
- Not visible to same package, subclasses, or other packages

```java
private void salaryDetails() { }
```

**What this enforces:**
- Encapsulation
- Internal logic hiding

📌 **Golden rule:** `private` methods are **not inherited**.

---

### 3.3 `protected` Methods

**Concept:**
- Accessible in:
  - Same class
  - Same package
  - Subclasses (even in other packages)

```java
protected void getBonusDetails() { }
```

**Inheritance behavior:**

```java
class JobPortal extends Invoice {
    getBonusDetails(); // allowed
}
```

📌 **Important:** `protected` works through **inheritance**, not object reference.

---

### 3.4 Default (Package-Private) Methods

**Concept:**
- **No access modifier** specified
- Accessible only within the **same package**

```java
void getRetentionDetails() { }
```

**Critical rule:**

```java
class Child extends Parent {
    // ❌ default methods are NOT inherited across packages
}
```

📌 **Common mistake:** default ≠ protected

---

## 4. Access Matrix

| Modifier | Same Class | Same Package | Subclass (other pkg) | Other Package |
|---|---|---|---|---|
| `public` | ✅ | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| default | ✅ | ✅ | ❌ | ❌ |
| `private` | ✅ | ❌ | ❌ | ❌ |

---

## 5. Real-World Design Insight

**Enterprise pattern example:**
- `EmployeeFirst` → HR-facing APIs
- `Invoice` → Finance-restricted logic
- `JobPortal` → Inherited but controlled access

📌 **Design principle:** expose only what is needed, hide everything else.

---

## 6. Interview Takeaways

### 6.1 Key Points

- `private` → encapsulation
- `protected` → inheritance
- default → package boundary
- `public` → API surface

### 6.2 Rules to Remember

- Access is checked at **compile time**
- Default methods are **not inherited across packages**
- `private` methods cannot be overridden
- `protected` enables inheritance across packages

### 6.3 Mental Model (One Line Each)

- `public` → everywhere
- `protected` → family + package
- default → package only
- `private` → class only

---

## 7. Types of Methods in Java

In Java, methods can be broadly classified based on who defines them and how they behave.

### 7.1 System-Defined Methods

**What are they?** Methods provided by Java libraries.

**Examples:** `System.out.println()`, `Math.max()`, `String.length()`

```java
System.out.println("Hello");
```

📌 Key point: you use them, you don’t define them.

---

### 7.2 User-Defined Methods

**What are they?** Methods written by the programmer for specific tasks.

```java
public void profession() {
    System.out.println("I'm in Person Class.");
}
```

📌 Why they matter: code reuse, readability, and business logic separation.

---

### 7.3 Method Overloading {#method-overloading}

**Definition:** Multiple methods with the same name but different parameter lists (type/count/order).

```java
int add(int a, int b) { return a + b; }
int add(int a, int b, int c) { return a + b + c; }
```

**Rules:**
- Happens in the same class
- Return type alone is not sufficient
- Resolved at compile time → compile-time polymorphism

📎 See also: [Varargs – flexible parameters](var-args.md)

---

### 7.4 Method Overriding {#method-overriding}

**Definition:** A child class provides its own implementation of a method defined in the parent class.

```java
class Doctor extends Person {
    @Override
    public void profession() {
        System.out.println("Doctor profession");
    }
}

Person obj = new Doctor();
obj.profession(); // calls Doctor’s implementation
```

**Runtime behavior:**
- Reference type → `Person`
- Object type → `Doctor`
- Method called → child implementation (runtime polymorphism)

---

### 7.5 Rules for Method Overriding (Must Remember) {#overriding-rules}

- Method name must be the same
- Parameter list must be the same
- Return type must be same (or covariant)
- Access level cannot be reduced
- Happens across inheritance
- Resolved at runtime
- 📌 Use `@Override` to avoid mistakes

---

### 7.6 Overloading vs Overriding (Quick Comparison)

| Feature | Overloading | Overriding |
|---|---|---|
| Same class | ✅ | ❌ |
| Inheritance needed | ❌ | ✅ |
| Parameters differ | ✅ | ❌ |
| Return type differs | Allowed | Restricted |
| Polymorphism | Compile-time | Runtime |

---

### 7.7 One-Line Mental Models

- System-defined → provided by Java
- User-defined → written by developer
- Overloaded → same name, different inputs
- Overridden → same method, different behavior

---

### 7.8 Final Interview Takeaways

- Overloading = compile-time polymorphism
- Overriding = runtime polymorphism
- Method call depends on object type (for overriding), not reference type
- Always use `@Override` on overridden methods

---

<div style="text-align:center;margin:2.5rem 0;padding:1.5rem;background:linear-gradient(135deg, #667eea 0%, #764ba2 100%);border-radius:10px;">
  <p style="color:white;font-size:1.1rem;margin-bottom:1rem;font-weight:600;">📚 Continue Learning</p>
  <a href="{{ '/learning/programming-language/java/01-basics/static-method' | relative_url }}" style="display:inline-block;padding:0.75rem 2rem;background:white;color:#667eea;text-decoration:none;border-radius:8px;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,0.2);">⚡ Static Methods in Java & Best Practices → Click Here</a>
</div>

---

## 8. Final Methods in Java {#final-methods}

### 8.1 What Is a Final Method?

A final method is a method whose implementation cannot be overridden by subclasses.

```java
public final void profession() { }
```

📌 **Meaning:** The behavior of this method is fixed and guaranteed.

---

### 8.2 Why Java Provides Final Methods

Final methods are used when:
- Core behavior must never change
- Consistency across subclasses is required
- Security and correctness are important

📌 **Example use cases:**
- Authentication logic
- Validation logic
- Framework lifecycle methods

---

### 8.3 What Happens When You Try to Override a Final Method

```java
class Doctor extends Person {
    public void profession() { }
}
```

**Result:** ❌ Compile-time error

**Reason:**
- The parent method is marked final
- Java prevents any subclass from changing it

📌 **Compiler rule:** A final method cannot be overridden.

---

### 8.4 Final vs Overriding

| Feature | Normal Method | Final Method |
|---|---|---|
| Can be overridden | ✅ Yes | ❌ No |
| Polymorphism | ✅ Yes | ❌ Fixed behavior |
| Inheritance | Behavior can change | Behavior is locked |
| Design flexibility | High | Restricted |

---

### 8.5 Final Methods and Polymorphism

```java
Person p = new Doctor();
p.profession();
```

**Behavior:**
- Always calls Person's implementation
- Child class has no influence

📌 **Key Insight:** Final methods disable runtime polymorphism.

---

### 8.6 Final vs Static Methods (Important Distinction)

| Aspect | Final Method | Static Method |
|---|---|---|
| Overridable | ❌ | ❌ |
| Polymorphism | ❌ | ❌ |
| Belongs to | Object | Class |
| Inherited | ✅ | Hidden |
| Uses @Override | ❌ | ❌ |

📌 **Important:** Final prevents overriding; static prevents polymorphism.

---

### 8.7 One-Line Mental Model

**Final method → behavior is locked**

**Static method → behavior is class-level**

---

### 8.8 Interview Carry-Forward Points

- Final methods cannot be overridden
- Attempting to override causes compile-time error
- Used to enforce consistent behavior
- Often used in frameworks and core APIs
- Helps prevent misuse of inheritance


---

## 9. Abstract Methods in Java {#abstract-methods}

### 9.1 What Is an Abstract Method?

An abstract method is a method **without a body**. It only defines what needs to be done, not how.

```java
public abstract void work();
```

📌 **Key idea:** Abstract methods force subclasses to provide an implementation.

---

### 9.2 Where Can Abstract Methods Exist?

- Abstract methods can exist **only inside abstract classes**.
- A class containing at least one abstract method **must be abstract**.

```java
public abstract class Person { }
```

---

### 9.3 Abstract Class with Both Concrete and Abstract Methods

Abstract classes can mix concrete and abstract behavior:

```java
public abstract class Person {

        public void profession() { }

        public abstract void work();
}
```

📌 **Design insight:** Abstract classes provide partial implementation.

---

### 9.4 Implementing Abstract Methods in Child Class

```java
public class Doctor extends Person {

        @Override
        public void work() {
                System.out.println("Doctor work");
        }
}
```

**Rule:**
- Child class must implement **all** abstract methods, otherwise it must also be declared abstract.

---

### 9.5 Abstract Methods and Overriding

```java
@Override
public void work() { }
```

- Abstract methods are meant to be overridden.
- `@Override` is recommended and valid; it enforces correct signature.

📌 **Important:** Abstract methods enable runtime polymorphism.

---

### 9.6 Abstract Method vs Final Method

| Feature | Abstract Method | Final Method |
|---|---|---|
| Has body | ❌ | ✅ |
| Can be overridden | Must be | ❌ |
| Enforces implementation | ✅ | ❌ |
| Used for | Contracts | Locked behavior |

📌 **Rule:** A method cannot be both abstract and final.

---

### 9.7 Abstract Methods and Polymorphism

```java
Person p = new Doctor();
p.work();
```

- Reference type → `Person`
- Object type → `Doctor`
- Method executed → `Doctor.work()`

📌 **Key Insight:** Abstract methods are the foundation of runtime polymorphism.

---

### 9.8 Why Use Abstract Methods?

- To define mandatory behavior
- To enforce design contracts
- To allow flexibility in implementation
- To avoid incomplete classes being instantiated

---

### 9.9 Restrictions on Abstract Methods

- Cannot be `private`
- Cannot be `static`
- Cannot be `final`
- Must be implemented by concrete subclasses

---

### 9.10 One-Line Mental Model

**Abstract method → “you must implement this.”**

**Concrete method → “you may use this as-is.”**

---

### 9.11 Interview Carry-Forward Points

- Abstract methods have **no body**
- Abstract classes can have **both abstract and concrete methods**
- Subclasses **must** implement abstract methods
- Abstract methods **enable polymorphism**
- Abstract ≠ interface (abstract classes can have state)

---

<div style="text-align:center;margin-top:2.5rem;">
    <a href="{{ '/learning/programming-language/java/01-basics' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Basics</a>
    <a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">☕ Java Hub</a>
</div>
