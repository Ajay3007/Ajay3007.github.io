---
layout: default
title: Stack Frame and Call Stack
permalink: /learning/programming-language/c/c-basics/stack-frame/
---

# Stack Frame and Call Stack

The **call stack** tracks active function calls.

Every function call creates a **stack frame** and pushes it on stack.
When function returns → frame popped.

So stack follows **LIFO**.

---

## What is inside a stack frame?

Usually includes:
- arguments
- local variables
- return address
- saved registers
- old frame pointer

> Actual layout depends on compiler + ABI (x86_64/ARM).

---

## Example call stack

```
main()
  |
  +-- funcA()
        |
        +-- funcB()
```

Stack while inside funcB:

```
Top
+-------------------+  funcB frame
| locals of funcB   |
| return → funcA    |
+-------------------+  funcA frame
| locals of funcA   |
| return → main     |
+-------------------+  main frame
| locals of main    |
+-------------------+
Bottom
```

---

## Stack Overflow

Occurs when stack memory exceeds limit.

Common causes:

- infinite recursion
- very large local arrays
- extremely deep call stack

---

## One stack per thread

Each thread has its own stack.
