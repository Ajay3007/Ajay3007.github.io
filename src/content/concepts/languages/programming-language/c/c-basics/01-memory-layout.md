---
title: "Memory Layout in C"
description: "Memory Layout in C Memory layout means how your program’s code + data is arranged in memory while execution."
domain: languages
track: c-fundamentals
order: 1
url: /learning/programming-language/c/c-basics/memory-layout/
---

# Memory Layout in C

Memory layout means **how your program’s code + data is arranged in memory** while execution.

A typical C process memory is divided into segments:

```
High Address
+-----------------------------------------------+
| Stack                                         |
| - function calls (stack frames)               |
| - local variables                             |
| - return address                              |
+-----------------------------------------------+
| (gap/guard pages)                             |
+-----------------------------------------------+
| Heap                                          |
| - dynamic memory (malloc/calloc/realloc)      |
| - grows as requested                          |
+-----------------------------------------------+
| BSS                                           |
| - uninitialized globals/statics (zero)        |
+-----------------------------------------------+
| Data                                          |
| - initialized globals/statics                 |
+-----------------------------------------------+
| Text / Code                                   |
| - machine instructions                        |
| - read-only constants, string literals (.rodata)
+-----------------------------------------------+
Low Address
```

✅ **Stack grows downward** (towards low addresses)  
✅ **Heap grows upward** (towards high addresses)

When heap and stack collide → memory exhausted / crash.

---

### Memory Layout Diagram

![Memory Layout](/assets/diagrams/learning/programming-language/c/c-basics/diagrams/memory-layout.svg){:class="diagram-img"}

*Shows how a C program is organized in memory into segments like text, data, bss, heap, and stack, including heap/stack growth direction.* 

---

## 1) Text Segment (Code Segment)

- Stores **compiled machine instructions**
- Usually **read-only**
- Often split into:
  - `.text` : instructions
  - `.rodata` : read-only constants / string literals

Example:
```c
printf("Hello"); // "Hello" typically in read-only region
```

---

## 2) Data Segment

Stores **global and static variables**.

### 2.1 Initialized Data

```c
int a = 10;        // global
static int b = 20; // static
```

These variables appear inside executable with their initial values.

### 2.2 Uninitialized Data (BSS)

```c
int x;         // global uninitialized
static int y;  // static uninitialized
```

- auto initialized to **0**
- not stored in binary (only size info)
- reduces executable size

---

## 3) Heap Segment

Heap used for **dynamic allocation**.

Functions:
- `malloc(size)` → allocates bytes (garbage/uninitialized)
- `calloc(n,size)` → allocates & initializes to 0
- `realloc(ptr,new)` → resize block
- `free(ptr)` → release block

### Heap key points

- memory persists beyond function scope
- must free manually (else leak)
- allocator stores metadata → some overhead
- fragmentation possible

---

## 4) Stack Segment

Used for function execution.

A stack frame usually contains:
- local vars
- args (depending ABI)
- return address
- saved registers / old frame pointer

### Why stack is fast?

Because stack allocation is just moving stack pointer.

### Stack limitations

- fixed size (per thread)
- deep recursion → stack overflow
- huge local arrays also risky

---

## When is memory allocated? (important)

- Compile time: compiler checks syntax + generates binary
- Load time: OS maps program into memory (text/data/bss)
- Run time: heap/stack change while program runs

---

## Quick experiment

```c
#include <stdio.h>
#include <stdlib.h>

int g1 = 10;      // data
int g2;           // bss
static int s1=7;  // data

int main() {
    int local = 5;        // stack
    int *p = malloc(4);   // heap
    *p = 99;

    printf("&g1=%p\n", (void*)&g1);
    printf("&g2=%p\n", (void*)&g2);
    printf("&s1=%p\n", (void*)&s1);
    printf("&local=%p\n", (void*)&local);
    printf("heap p=%p\n", (void*)p);

    free(p);
}
```

Observe: stack addr usually higher than heap.

---

## Tools (Linux)

```bash
size a.out
nm -S a.out | head
readelf -S a.out | less
```
