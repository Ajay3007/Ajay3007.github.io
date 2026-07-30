---
layout: learning
title: Java Compilation & Execution Flow
permalink: /learning/programming-language/java/00-foundation/compilation-execution/
---

# Java Compilation & Execution Flow

This document explains **how Java source code is compiled and executed**, from writing a `.java` file to running it inside the JVM.  
This understanding is critical for **Java fundamentals, JVM internals, and interviews**.

---

## 1. High-Level Overview

Java execution happens in **two major phases**:

1. **Compilation phase** – Source code → Bytecode
2. **Execution phase** – Bytecode → Native machine instructions

Java follows the principle:

> **Write Once, Run Anywhere (WORA)**

This is possible because Java compiles code into **platform-independent bytecode**, not native machine code.

---

## 2. Compilation Phase (`javac`)

### Step 1: Write Source Code

```java
Employee.java
```

This file contains human-readable Java code.

### Step 2: Compile Using javac

```bash
javac Employee.java
```

What happens internally:

- Syntax checking
- Type checking
- Bytecode generation

Output:

```
Employee.class
```

📌 The .class file contains bytecode, not machine code.

---

## 3. Execution Phase (`java`)

### Step 3: Run Using java

```bash
java Employee
```

This starts the Java Virtual Machine (JVM).

---

## 4. Real Execution Command (IDE Example)

When running from IntelliJ, the command looks like:

```
"C:\Program Files\Java\jdk-21\bin\java.exe"
-javaagent:idea_rt.jar=49735
-Dfile.encoding=UTF-8
-classpath out\production\javafoundry
com.ajay.javafoundry.foundation.intro.Employee
```

This command tells the JVM:

- Which Java runtime to use
- Which classpath contains compiled classes
- Which class contains the main() method

---

## 5. Key Components Involved

### 5.1 java.exe

- Native launcher that starts the JVM
- Allocates memory (Heap, Stack, Metaspace)
- Initializes classloaders

### 5.2 Classpath (-classpath or -cp)

Classpath tells JVM where to find compiled .class files.

Example:

```
out/production/javafoundry
```

JVM searches classes in this order:

1. Bootstrap ClassLoader
2. Platform ClassLoader
3. Application ClassLoader

### 5.3 Fully Qualified Class Name

```
com.ajay.javafoundry.foundation.intro.Employee
```

This maps to:

```
com/ajay/javafoundry/foundation/intro/Employee.class
```

The class must contain:

```java
public static void main(String[] args)
```

---

## 6. JVM Execution Steps (In Order)

1. JVM starts
2. ClassLoader loads the class
3. Bytecode verification
4. Memory allocation
5. Static blocks execute
6. main() method starts
7. Program runs

---

## 7. Role of Bytecode

- Bytecode is platform-independent
- JVM converts bytecode into machine code using:
  - Interpreter
  - JIT (Just-In-Time Compiler)

This is why Java is portable across OS and CPU architectures.

---

## 8. Why Java Needs Both javac and java

| Tool | Purpose |
|---|---|
| javac | Compiles source code |
| java | Executes bytecode |

📌 Compilation happens once, execution can happen many times.

---

## 9. Common Interview Questions

### Q: Is Java interpreted or compiled?

**Answer:**
Java is both compiled and interpreted.
It is compiled to bytecode and interpreted/JIT-compiled at runtime.

### Q: What happens if main() is missing?

**Answer:**
JVM throws:

```
Error: Main method not found
```

### Q: Can JVM run without JDK?

**Answer:**
Yes. JVM is part of JRE, JDK is needed only for compilation.

---

## 10. Key Takeaways

- Java source code is compiled into bytecode
- JVM executes bytecode, not source code
- Classpath is critical for class loading
- JVM provides portability and runtime optimizations
- Understanding this flow is essential for JVM, LLD, and system design

---

## 11. Mapping to JavaFoundry

This topic connects directly to:

- JVM internals
- Class loading
- Memory management
- Debugging and performance tuning

This knowledge will be reused in:

- Multithreading
- Garbage collection
- Backend system design

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/learning/programming-language/java/00-foundation' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Foundation</a>
  <a href="{{ '/learning/programming-language/java' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">☕ Java Hub</a>
</div>
