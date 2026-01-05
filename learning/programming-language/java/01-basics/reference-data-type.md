---
layout: default
title: Java Reference Data Types – Core Notes
---

# Java Reference Data Types – Core Notes

This note captures the essential points about **non-primitive (reference) types in Java** using the examples provided.

---

## 1. What Is a Reference Type?

### 1.1 Core Idea

- A reference type does not store the actual data; it stores an **address** pointing to an object in memory.
- Examples: objects of classes, strings, arrays, interfaces.
- Mental model: the variable is the **remote control**, the object is the **TV**.

---

## 2. Object References and Mutability

### 2.1 Concept

- Creating an object stores its address in the variable, not the fields themselves.

### 2.2 Example

```java
Employee empObj = new Employee();
empObj.empId = 110010;
```

- `empObj` holds a **reference** to an `Employee` object; `empId` lives inside that object.
- Multiple variables can point to the **same object**.

---

## 3. Passing Objects to Methods (Very Important)

### 3.1 Pass-by-Value for References

- Java is pass-by-value; for objects, the **value being copied is the reference**.

### 3.2 Example

```java
modify(empObj);

void modify(Employee e) {
		e.empId = 110025;
}
```

**What happens**
- `empObj` reference is copied into `e`.
- Both references point to the **same object**.
- Mutations via `e` are visible through `empObj`.

**Key rule**
- You cannot change the reference itself inside the method, but you can change the object it points to.

---

## 4. Strings as Reference Types (Special Case)

### 4.1 Immutability

- Strings are reference types but **immutable**.

### 4.2 Example

```java
String s1 = "hello";
String s2 = "hello";
```

- Both can point to the same String object in the **String Constant Pool**.

### 4.3 Comparisons

- `s1 == s2` compares references.
- `s1.equals(s2)` compares content.

**Golden rule:** always use `equals()` to compare strings.

---

## 5. new String() vs String Literal

### 5.1 Example

```java
String s1 = "hello";
String s3 = new String("hello");
```

- `s1` → points to String Pool entry.
- `s3` → creates a **new object on the heap**.
- Contents are the same; **references differ**.

**Interview line:** `new String()` always creates a new object.

---

## 6. Interface as a Reference Type (Polymorphism)

### 6.1 Core Idea

- Interfaces define **what** to do, not **how** to do it.

### 6.2 Example

```java
Person p = new Engineer();
```

- `Person` is a reference type and can point to any implementing class.
- Method dispatch is resolved at **runtime** (polymorphism).

**Principle:** program to an interface, not an implementation.

---

## 7. What You Cannot Do with Interfaces

```java
// Person p = new Person(); // ❌ cannot instantiate an interface
```

- Interfaces are **abstract**.
- They have **no constructor** and cannot be directly instantiated.

---

## 8. Primitive vs Reference Types (Mental Model)

| Concept | Primitive | Reference |
|---|---|---|
| Stores | Actual value | Address to object |
| Method passing | Copy of value | Copy of reference |
| Can be null | ❌ | ✅ |
| Mutation visible | ❌ | ✅ |

---

## 9. Final Takeaways

- Reference variables point to objects; mutation is visible across references.
- Java passes **references by value** (the reference itself is copied).
- Strings are **immutable** but still reference-based; use `equals()` for comparison.
- Interfaces enable **polymorphism**; you cannot instantiate them directly.
- `==` → reference comparison; `equals()` → content comparison.

---

<div style="text-align:center;margin-top:2.5rem;">
	<a href="{{ '/learning/programming-language/java/01-basics' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Basics</a>
	<a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">☕ Java Hub</a>
</div>
