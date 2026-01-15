---
layout: default
title: Padding, Alignment and Packing
permalink: /learning/programming-language/c/c-basics/padding-packing/
---

# Padding, Alignment & Packing

Structure size may be bigger than expected due to padding.

Padding exists to satisfy alignment for faster CPU access.

---

## Example

```c
struct A {
    char c;  // 1
    int i;   // 4
};
```

Expected 5 bytes but actual often 8 bytes.

Layout:
```
| c | pad pad pad | i i i i |
```

---

## Reduce padding

Reorder fields: bigger → smaller.

```c
struct X {
    double d;
    int i;
    char c;
};
```

---

## Packing

Used in:
- network headers
- binary file parsing

### GCC packed attribute

```c
struct __attribute__((packed)) P {
    char c;
    int i;
};
```

### pragma pack

```c
#pragma pack(1)
struct P { char c; int i; };
#pragma pack()
```

⚠️ Packed structs may reduce performance (unaligned access).
