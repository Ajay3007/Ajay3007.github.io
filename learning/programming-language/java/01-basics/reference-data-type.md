---
layout: default
title: Java Reference Data Types – Core Notes
---

# Java Reference Data Types – Core Notes

Concise points about **non-primitive (reference) types** and related concepts.

---

## Table of Contents

- [1. What Is a Reference Type?](#1-what-is-a-reference-type)
- [2. Object References and Mutability](#2-object-references-and-mutability)
- [3. Passing Objects to Methods](#3-passing-objects-to-methods)
- [4. Strings as Reference Types](#4-strings-as-reference-types)
- [5. Interfaces as Reference Types](#5-interfaces-as-reference-types)
- [6. Primitive vs Reference (Snapshot)](#6-primitive-vs-reference-snapshot)
- [7. Wrapper Classes](#7-wrapper-classes)
- [8. Autoboxing & Unboxing](#8-autoboxing--unboxing)
- [9. Wrapper Caching (Favorite)](#9-wrapper-caching-favorite)
- [10. Constants (final / static final)](#10-constants-final--static-final)
- [11. Collections Require Wrappers](#11-collections-require-wrappers)
- [12. Performance Note](#12-performance-note)
- [13. Primitive vs Wrapper (Quick Compare)](#13-primitive-vs-wrapper-quick-compare)
- [14. Carry-Forward Points](#14-carry-forward-points)

---

## 1. What Is a Reference Type?

- Stores an **address** to an object (not the data).
- Examples: class objects, strings, arrays, interfaces.
- Mental model: variable = remote control; object = TV.

---

## 2. Object References and Mutability

```java
Employee empObj = new Employee();
empObj.empId = 110010;
```

- `empObj` holds a reference; fields live inside the object.
- Multiple references can point to the same object.

---

## 3. Passing Objects to Methods

```java
modify(empObj);

void modify(Employee e) {
    e.empId = 110025;
}
```

- Java is pass-by-value; the **reference value** is copied.
- Mutations via the copy are visible to all references.
- You cannot rebind the caller’s reference from inside the method.

---

## 4. Strings as Reference Types

```java
String s1 = "hello";
String s2 = "hello";
```

- Strings are reference types but **immutable**.
- Pooling allows `s1` and `s2` to share the same object.
- `==` compares references; `equals()` compares content (always use `equals()`).

### 4.1 Literal vs `new String()`

```java
String s1 = "hello";            // pooled
String s3 = new String("hello"); // new heap object
```

- Same content, different references; `new String()` always creates a new object.

---

## 5. Interfaces as Reference Types

```java
Person p = new Engineer();
```

- Interface reference can point to any implementing class; dispatch is runtime.
- Cannot instantiate an interface directly (`new Person()` ❌).
- Principle: program to an interface, not an implementation.

---

## 6. Primitive vs Reference (Snapshot)

| Concept | Primitive | Reference |
|---|---|---|
| Stores | Value | Address |
| Method passing | Copy of value | Copy of reference |
| Can be null | ❌ | ✅ |
| Mutation visible | ❌ | ✅ |

---

## 7. Wrapper Classes

- Convert primitives to **objects**.

| Primitive | Wrapper |
|---|---|
| `int` | `Integer` |
| `double` | `Double` |
| `char` | `Character` |
| `boolean` | `Boolean` |

**Why**: collections/APIs expect objects; wrappers add methods; allow `null`.

---

## 8. Autoboxing & Unboxing

```java
int a = 10;
Integer obj = a;      // autoboxing -> Integer.valueOf(a)
int b = obj;          // unboxing   -> obj.intValue()
```

- Compiler inserts conversions.
- Unboxing a `null` wrapper throws `NullPointerException`.

---

## 9. Wrapper Caching (Favorite)

```java
Integer a = 100, b = 100; // cached → a == b is true
Integer x = 200, y = 200; // new objects → x == y is false
```

- Cache range: **-128 to 127**.
- Use `equals()` for comparison.

---

## 10. Constants (`final` / `static final`)

```java
final int MAX = 100;
public static final int MAX_USERS = 1000;
```

- `final`: cannot be reassigned; encourages immutability.
- `static final`: one shared, compile-time constant; name in `UPPER_CASE_WITH_UNDERSCORES`.

```java
public static final Integer LIMIT = 10; // wrapper constant (avoid null)
```

Prefer primitives for constants unless an object is required.

---

## 11. Collections Require Wrappers

```java
// List<int> list = new ArrayList<>(); // ❌
List<Integer> list = new ArrayList<>(); // ✅

list.add(10);        // autoboxing
int x = list.get(0); // unboxing
```

- Collections store objects; wrappers bridge the gap.

---

## 12. Performance Note

- Autoboxing allocates; avoid in tight numeric loops.
- Rule: use primitives for computation; wrappers for collections/APIs.

---

## 13. Primitive vs Wrapper (Quick Compare)

| Feature | Primitive | Wrapper |
|---|---|---|
| Object | ❌ | ✅ |
| Can be null | ❌ | ✅ |
| Collections | ❌ | ✅ |
| Performance | Faster | Slower |
| Methods | ❌ | ✅ |

---

## 14. Carry-Forward Points

- References point to objects; mutations are shared across references.
- Java passes references **by value**.
- Strings are immutable; compare with `equals()`.
- Wrappers enable collections/APIs and `null`; mind autoboxing cost.
- Use `equals()` for wrappers; use `static final` for true constants.

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/learning/programming-language/java/01-basics' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Basics</a>
  <a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">☕ Java Hub</a>
</div>
