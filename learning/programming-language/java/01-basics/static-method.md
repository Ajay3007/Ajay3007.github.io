---
layout: default
title: Static Methods in Java
---

# Static Methods in Java

Complete guide to static methods, method hiding, overriding behavior, and design considerations.

---

## Table of Contents

- [1. Static Methods in Java](#1-static-methods-in-java)
- [2. Static Methods and Overriding in Java](#2-static-methods-and-overriding-in-java)
- [3. Static Method Definition and Design Considerations](#3-static-method-definition-and-design-considerations)

---

## 1. Static Methods in Java

### 1.1 What Is a Static Method?

A static method belongs to the **class**, not to an individual object.

**Characteristics:**
- Called using class name
- Loaded once when the class is loaded
- Does not depend on object state

```java
StaticMethod.getOddSum(10);
```

📌 **Key idea:** static methods operate at the class level, not object level.

---

### 1.2 How Static Methods Are Declared

```java
public static int getBurgerPrice() {
    return burgerPrice;
}
```

- `static` keyword makes the method class-level
- No object is required to call it

---

### 1.3 Static Methods and Instance Variables

```java
// ❌ Not Allowed
price++;
```

**Reason:**
- `price` is an instance variable
- Static methods do not know which object to use

📌 **Rule:** static methods cannot directly access non-static members.

---

### 1.4 Static Methods and Static Variables

```java
// ✅ Allowed
burgerPrice += 10;
```

**Reason:**
- Static variables are also class-level
- Shared across all objects

📌 **Mental model:** static talks only to static.

---

### 1.5 Calling Non-Static Methods from Static Methods

```java
// ❌ Direct call not allowed
printSum(sum);

// ✅ Correct approach
StaticMethod obj = new StaticMethod();
obj.printSum(sum);
```

📌 **Why?** Non-static methods need an object context.

---

### 1.6 How Static Methods Should Be Called

```java
// ❌ Allowed but discouraged
obj.getOddSum(11);

// ✅ Recommended
StaticMethod.getOddSum(11);
```

📌 **Best practice:** always call static methods using the class name.

---

### 1.7 Static Methods and Polymorphism

- Static methods **cannot be overridden**
- They are resolved at **compile time**
- Method call depends on **reference type**, not object type

📌 **This is called method hiding, not overriding.**

---

### 1.8 Common Use Cases of Static Methods

- Utility/helper methods
- Mathematical calculations
- Factory methods
- Constants-related operations
- Entry point: `main()` method

---

### 1.9 Static vs Instance Methods (Quick Comparison)

| Feature | Static Method | Instance Method |
|---|---|---|
| Belongs to | Class | Object |
| Access instance data | ❌ | ✅ |
| Requires object | ❌ | ✅ |
| Can be overridden | ❌ | ✅ |
| Polymorphism | ❌ | ✅ |

---

### 1.10 Final Carry-Forward Points

- Static methods belong to the **class**
- Cannot directly access **instance members**
- Can access **static variables and methods**
- Should be called using **class name**
- Do **not support runtime polymorphism**

---

## 2. Static Methods and Overriding in Java

### 2.1 Can Static Methods Be Overridden?

No. Static methods cannot be overridden in Java.

- Static methods belong to the class, not to objects.
- Overriding requires runtime polymorphism, which static methods do not support.

---

### 2.2 Why `@Override` Is Not Allowed on Static Methods

**Parent class**

```java
class Person {
    public static void profession() {
        System.out.println("I'm in Person Class.");
    }
}
```

**Child class (with `@Override`)**

```java
class Doctor extends Person {

    @Override
    public static void profession() {
        System.out.println("Doctor profession");
    }
}
```

**Result:** ❌ Compile-time error

**Reason:**
- `@Override` means: this method must override a parent method.
- Static methods do not participate in overriding.
- Hence, the compiler rejects it.

📌 **Rule:** `@Override` can only be used with instance methods.

---

### 2.3 Why Code Works After Removing `@Override`

```java
class Doctor extends Person {

    public static void profession() {
        System.out.println("Doctor profession");
    }
}
```

**What is happening here?**
- This is **not** overriding; it is **method hiding**.
- Both methods exist separately.

📌 **Key Concept:** static methods with the same signature in parent and child cause method hiding, not overriding.

---

### 2.4 What Is Method Hiding?

**Definition**
- Method hiding occurs when a child class defines a static method with the same signature as a static method in the parent class.
- Only applies to static methods.
- Resolved at **compile time**.
- Depends on **class name**, not object.

---

### 2.5 Behavior at Runtime (Observation Explained)

**Test code**

```java
Doctor.profession();
Person.profession();
```

**Output**

```
Doctor profession
I'm in Person Class.
```

**Why this happens**
- Static methods are called using the class name.
- JVM does not use dynamic dispatch for static methods.

📌 **Important:** static method calls are bound at compile time.

---

### 2.6 Static vs Instance Method Resolution

**Instance method (overriding)**

```java
Person p = new Doctor();
p.profession();   // calls Doctor's method
```

✔ Runtime polymorphism; object type matters.

**Static method (hiding)**

```java
Person.profession();
Doctor.profession();
```

✔ Compile-time binding; class name matters. ❌ No polymorphism.

---

### 2.7 Why Static Methods Cannot Be Overridden

| Reason | Explanation |
|---|---|
| No object context | Static methods are class-level |
| Compile-time binding | Decision made before runtime |
| No dynamic dispatch | JVM does not choose at runtime |

📌 **One-liner:** Overriding needs runtime polymorphism; static methods don't have it.

---

### 2.8 Common Interview Trap

```java
Person p = new Doctor();
p.profession();   // calls Person.profession()
```

**Explanation**
- Method is static.
- Reference type (`Person`) decides the call.
- Object type (`Doctor`) is ignored.

---

### 2.9 Static vs Instance Methods (Quick Comparison)

| Feature | Instance Method | Static Method |
|---|---|---|
| Can be overridden | ✅ | ❌ |
| Polymorphism | Runtime | ❌ |
| Binding time | Runtime | Compile time |
| Uses `@Override` | ✅ | ❌ |
| Belongs to | Object | Class |

---

### 2.10 Final Carry-Forward Points

- Static methods cannot be overridden.
- Using `@Override` on static methods → compile error.
- Same static method in child = **method hiding**.
- Static calls depend on **class name**.
- No runtime polymorphism for static methods.

✅ **Mental Model:**
- Instance methods → object behavior.
- Static methods → class behavior.

---

## 📘 Instance Methods vs Static Methods

| Aspect | Instance Methods | Static Methods |
|---|---|---|
| Belong to | Object | Class |
| Object required to call | ✅ Yes | ❌ No |
| Accessed using | Object reference | Class name |
| Access instance variables | ✅ Yes | ❌ No |
| Access static variables | ✅ Yes | ✅ Yes |
| Polymorphism | ✅ Supported | ❌ Not supported |
| Method resolution | Runtime (dynamic binding) | Compile time (static binding) |
| Overriding | ✅ Allowed | ❌ Not allowed |
| Method hiding | ❌ Not applicable | ✅ Possible |
| Use of @Override | ✅ Valid | ❌ Compile-time error |
| Depends on | Object type | Reference / class name |
| Inheritance behavior | Inherited and overridden | Inherited but hidden |
| Uses this keyword | ✅ Yes | ❌ No |
| Typical use case | Object-specific behavior | Utility / class-level behavior |
| Example | obj.calculate() | Math.max() |
| Memory | One copy per object | One copy per class |
| Can be abstract | ✅ Yes | ❌ No |
| Can be final | ✅ Yes | ✅ Yes |

---

## 3. Static Method Definition and Design Considerations

This example highlights how static and instance methods should be designed, and where developers must be careful.

### 3.1 Valid Static Method (Best Practice)

```java
public static int sum(int a, int b) {
    return a + b;
}
```

**Why this is good design:**
- Uses only method parameters
- Does not depend on object state
- Produces predictable results
- Easy to test and reuse

📌 **Rule:** A static method should ideally be stateless.

---

### 3.2 Valid Instance Method Using Static Variable

```java
public int sum2(int a, int b) {
    carPrice += a + b;
    return a + b;
}
```

**Why this is acceptable:**
- Instance methods have access to:
  - Instance variables
  - Static variables
- Object context is available
- Behavior is explicit

📌 **Key point:** Instance methods can safely modify static variables, but such design must be intentional.

---

### 3.3 Static Method Modifying Static Variable (⚠️ Caution)

```java
public static int sum3(int a, int b) {
    carPrice += a + b;
    return a + b;
}
```

**Why this is risky:**
- Static variable is shared across all objects
- Any call can change global state
- Order of calls affects result
- Harder to debug and reason about

📌 **Important:** Static methods modifying static variables introduce hidden side effects.

---

### 3.4 Key Design Difference Highlighted

| Method | Uses Object State | Modifies Global State | Risk Level |
|---|---|---|---|
| sum() | ❌ | ❌ | ✅ Safe |
| sum2() | ✅ | ✅ | ⚠️ Moderate |
| sum3() | ❌ | ✅ | ❌ High |

---

### 3.5 Why This Matters in Real Projects

**Static methods are often treated as utility methods.**

Utility methods are expected to be:
- Stateless
- Predictable
- Thread-safe

**Modifying static variables breaks these expectations.**

📌 **Interview Insight:** Static methods should not change shared state unless explicitly required.

---

### 3.6 Best Practices to Remember

- Prefer pure static methods (no shared state)
- Use instance methods when behavior depends on object data
- Avoid static methods that mutate static variables
- Treat static variables as global state

---

### 3.7 One-Line Mental Model

**Static methods should compute, not mutate.**

**Instance methods represent behavior tied to state.**

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/learning/programming-language/java/01-basics' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Basics</a>
  <a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">☕ Java Hub</a>
</div>
