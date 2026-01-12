---
layout: default
title: Memory Management & Garbage Collection in Java
permalink: /learning/programming-language/java/03-core-java/memory-management-garbage-collection/
---

# 🧠 Memory Management & Garbage Collection in Java

This guide explains how Java manages memory using **Stack** and **Heap**, how objects and references work, and how the JVM performs **Garbage Collection (GC)** to free unused objects.

---

<div style="background: linear-gradient(135deg, rgba(102,126,234,0.08), rgba(118,75,162,0.08)); border-left: 4px solid #667eea; border-radius: 10px; padding: 1.5rem; margin: 2rem 0;">
  <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem;">
    <span style="font-size: 1.8rem;">📄</span>
    <h3 style="margin: 0; color: #2d3748;">Handwritten Notes (PDF)</h3>
  </div>
  <p style="margin: 0.5rem 0; color: #4a5568;">Original handwritten notes on Memory Management and Garbage Collection with detailed diagrams and annotations.</p>
  <a href="{{ '/learning/programming-language/java/03-core-java/MemoryManagentAndGC.pdf' | relative_url }}" style="display: inline-block; margin-top: 1rem; padding: 10px 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 6px; font-weight: 600; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
    📥 Download PDF Notes
  </a>
</div>

---

## Table of Contents

1. [Stack vs Heap](#1-stack-vs-heap)
2. [Stack Memory](#2-stack-memory)
3. [Heap Memory](#3-heap-memory)
4. [String Pool](#4-string-pool)
5. [Memory Allocation Example](#5-memory-allocation-example)
6. [Object Reachability & GC](#6-object-reachability--gc)
7. [Garbage Collection Algorithms](#7-garbage-collection-algorithms)
8. [Young Generation vs Old Generation](#8-young-generation-vs-old-generation)
9. [GC Types](#9-gc-types)
10. [Important Concepts](#10-important-concepts)

---

## 1. Stack vs Heap

Java memory is divided into two main regions:

| Aspect | Stack | Heap |
|--------|-------|------|
| **Stores** | Method frames, local variables, primitive values, object references | Objects, arrays, String pool |
| **Scope** | Per-thread (each thread has its own) | Shared across all threads |
| **Allocation** | LIFO order | Dynamic (no strict order) |
| **Deallocation** | Automatic when method ends | Via Garbage Collector |
| **Error when full** | `StackOverflowError` | `OutOfMemoryError` |
| **Speed** | Very fast | Slower than stack |

---

## 2. Stack Memory

**Stack** stores:
- Method call frames (scope)
- Local variables
- Primitive values (`int`, `double`, `boolean`, etc.)
- **References** to objects (the reference itself, not the object)

### Key Behaviors:

✅ **LIFO (Last In, First Out)** → Variables exist only within their scope

✅ **Automatic cleanup** → When a method ends, its stack frame is popped and local variables are removed

⚠️ **StackOverflowError** → Occurs if stack becomes full (common in infinite recursion)

### Example:
```java
void myMethod() {
    int x = 10;           // Stack: primitive stored here
    Person p = new Person();  // Stack: reference stored here
}
// When myMethod() ends → stack frame is popped → x & p reference removed
```

---

## 3. Heap Memory

**Heap** stores:
- Objects created using `new` keyword
- Arrays
- String pool (String interned values)

### Key Characteristics:

✅ **Shared across threads** → All threads can access heap objects

✅ **Garbage collected** → Objects freed when no longer referenced

⚠️ **OutOfMemoryError** → Occurs if heap becomes full

### Example:
```java
Person p = new Person();  // Reference 'p' in stack, object in heap
String s = "Hello";       // Literal "Hello" in String pool (heap)
```

---

## 4. String Pool

**String literals** are stored in a special area called the **String Constant Pool** (inside heap).

```java
String s1 = "Memory";      // Created in String pool
String s2 = "Memory";      // Points to SAME object in pool
String s3 = new String("Memory");  // NEW object in heap (not in pool)

System.out.println(s1 == s2);  // true (same reference)
System.out.println(s1 == s3);  // false (different objects)
```

---

## 5. Memory Allocation Example

### Code:
```java
int primitiveVar = 10;
Person personObj = new Person();
String stringLiteral = "Memory";
MemoryManagement memObj = new MemoryManagement();
memObj.memoryManagementTest(personObj);
```

### UML Class Diagram:

<div style="text-align:center;margin:2rem 0;">
  <img src="{{ '/assets/diagrams/learning/programming-language/java/03-core-java/memory-management-uml.svg' | relative_url }}" alt="Memory Management UML Diagram" class="diagram-img">
</div>

### Memory Layout Diagram:

<div style="text-align:center;margin:2rem 0;">
  <img src="{{ '/assets/images/stack-vs-heap.png' | relative_url }}" alt="Stack vs Heap Memory Diagram" style="max-width:100%;width:auto;max-height:600px;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,0.1);">
</div>

### PlantUML Generated Diagram:

<div style="text-align:center;margin:2rem 0;">
  <img src="{{ '/assets/diagrams/learning/programming-language/java/03-core-java/stack-vs-heap.svg' | relative_url }}" alt="Stack vs Heap Memory Diagram" class="diagram-img">
</div>

### What Happens in Memory:

| Variable | Storage Location | Details |
|----------|------------------|---------|
| `primitiveVar = 10` | Stack | Primitive value stored directly |
| `personObj` | Stack → Heap | Reference in stack, object in heap |
| `stringLiteral = "Memory"` | String Pool | Literal stored in pool (heap area) |
| `memObj` | Stack → Heap | Reference in stack, object in heap |

### When `memoryManagementTest()` ends:

- Its local variables' references are removed from stack
- Heap objects may become unreferenced
- Garbage Collector later cleans up unreachable objects

---

## 6. Object Reachability & GC

### When Does an Object Become Garbage Collectable?

An object is eligible for garbage collection when it becomes **unreachable from GC roots**.

### Common Ways Objects Become Unreachable:

#### ✅ Assigning to null
```java
Person obj = new Person();
obj = null;  // Object becomes unreachable
```

#### ✅ Reassignment
```java
Person obj1 = new Person();
Person obj2 = new Person();
obj1 = obj2;  // Old obj1 becomes unreachable (eligible for GC)
```

#### ✅ Method scope ends
```java
void test() {
    Person obj = new Person();
}  // When test() ends → reference removed → object may become unreachable
```

---

## 7. Garbage Collection Algorithms

### Mark → Sweep → Compact

The JVM performs garbage collection in three main steps:

#### Step 1: Mark
- Identifies all reachable objects from **GC Roots**
- Marks them as "live"

#### Step 2: Sweep
- Deallocates unmarked (unreachable) objects
- Frees heap memory

#### Step 3: Compaction
- Moves live objects together to reduce fragmentation
- Creates contiguous free space

### GC Roots (What Keeps Objects Alive):

Objects are considered **alive** if reachable from:
- Local variables in active threads
- Static variables
- Class references
- Thread objects

---

## 8. Young Generation vs Old Generation

### Heap Structure:

The JVM heap is divided into generations:

```
┌─────────────────────────────────┐
│         Young Generation        │
├──────────────┬──────────────────┤
│   Eden       │  Survivor (S0,S1)│
└──────────────┴──────────────────┘
         ↓ (promotion)
┌──────────────────────────────────┐
│      Old / Tenured Generation    │
└──────────────────────────────────┘
         
Metaspace (Non-Heap) - Class metadata
```

### Minor GC (Young Generation):

✅ Runs frequently and quickly

✅ Cleans up short-lived objects in Eden space

✅ Moves surviving objects between Survivor spaces (S0 ↔ S1)

✅ Tracks object age (how many GC cycles survived)

### Promotion to Old Generation:

When an object's **age exceeds threshold** (typically 8):
- Object promoted from Young → Old generation
- Reduces Young generation size

### Major/Full GC (Old Generation):

✅ Runs less frequently but heavier cleanup

✅ Higher pause time (application stops)

✅ Cleans up old long-lived objects

### Metaspace:

✅ Stores class metadata and static information

✅ Not part of heap (non-heap memory)

✅ Replaced `PermGen` in Java 8+

---

## 9. GC Types

Different garbage collectors with different trade-offs:

### Serial GC

- Single-threaded
- Stop-the-world pauses
- **Best for:** Small applications, limited CPU

### Parallel GC (Default in Java 8)

- Multiple GC threads
- Improved throughput
- **Best for:** Multi-core systems, server applications

### CMS (Concurrent Mark Sweep)

- Reduced stop-the-world time
- Attempts concurrent work with application
- Not fully pause-free
- **Best for:** Low-latency applications

### G1 GC (Garbage First)

- Balances throughput and latency
- Includes automatic compaction
- Aims to limit pause time
- **Best for:** Large heaps, modern systems

---

## 10. Important Concepts

### Stop-The-World (STW)

Many GC phases pause application threads:
- Serial GC pauses more
- G1 GC tries to limit pause time
- Longer pauses = noticeable application lag

### Java Memory Leaks

Even with automatic GC, leaks can occur when:
- References unintentionally kept alive
- Static maps growing unbounded
- Event listeners not removed
- Thread-local variables not cleaned up

**Definition:** A memory leak is when an object is no longer needed but remains **reachable**, preventing GC from freeing it.

### System.gc() is Optional

```java
System.gc();  // Just a SUGGESTION, not a command
```

- JVM may or may not run GC
- GC timing depends on memory pressure and implementation
- Rely on JVM to manage GC automatically

### Weak vs Soft References

#### Strong Reference (Default)
```java
Person p = new Person();  // GC won't delete while reachable
```

#### Weak Reference
```java
WeakReference<Person> wp = new WeakReference<>(new Person());
// GC can collect immediately during next GC cycle
```

#### Soft Reference
```java
SoftReference<Person> sp = new SoftReference<>(new Person());
// GC collects only when memory is desperately needed (cache scenarios)
```

---

## Quick Summary & Revision

| Concept | Key Points |
|---------|-----------|
| **Stack** | Per-thread, LIFO, stores primitives & references, fast deallocation |
| **Heap** | Shared, stores objects, freed by GC, slower allocation |
| **String Pool** | Special heap area for literal strings |
| **Young Gen** | Eden + Survivor spaces, frequent minor GC |
| **Old Gen** | Long-lived objects, major GC less frequent |
| **Mark-Sweep-Compact** | GC identifies reachable objects, removes unreachable, compacts memory |
| **Stop-The-World** | Application pauses during GC phases |
| **Memory Leak** | Object unreferenced but still reachable = GC can't clean |
| **Strong Reference** | Keeps object alive |
| **Weak Reference** | GC can collect anytime |
| **Soft Reference** | GC collects under memory pressure |

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/programming-language/java/03-core-java' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#1976d2;color:white;border-radius:5px;text-decoration:none;margin-right:10px;font-weight:600;">← Back to Core Java</a>
  <a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#388e3c;color:white;border-radius:5px;text-decoration:none;margin-right:10px;font-weight:600;">← Java Home</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#2d3748;color:white;border-radius:5px;text-decoration:none;font-weight:600;">🏠 Home</a>
</div>
