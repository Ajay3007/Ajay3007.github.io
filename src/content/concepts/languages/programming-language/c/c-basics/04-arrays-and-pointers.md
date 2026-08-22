---
title: "Arrays and Pointers"
description: "Arrays and Pointers Arrays and pointers are different but connected."
domain: languages
track: c-fundamentals
order: 4
url: /learning/programming-language/c/c-basics/arrays-and-pointers/
---

# Arrays and Pointers

Arrays and pointers are different but connected.

Example:
```c
int A[5] = {2,4,5,8,1};
```

- stored contiguously
- base address = `&A[0]`

---

## Address and value mapping

Address:
```c
&A[i] == (A+i)
```

Value:
```c
A[i] == *(A+i)
```

So `[]` is syntactic sugar.

---

### Arrays and Pointers Diagram

![Arrays and Pointers](/assets/diagrams/learning/programming-language/c/c-basics/diagrams/arrays-pointers-object.svg){:class="diagram-img"}

*Demonstrates how arrays and pointers are related, including base address concept, memory layout of elements, and pointer arithmetic like `A[i] == *(A+i)`*

---

## Why `A++` is invalid?

Array name is constant base address (non-modifiable lvalue).

```c
A++; // ❌
```

But pointer is modifiable:
```c
int *p = A;
p++; // ✅
```

---

## sizeof array vs pointer

```c
sizeof(A)  // full size
sizeof(p)  // pointer size
```

---

## Array Decay (Passing array to function)

When passed to function, array becomes pointer.

```c
int sum(int A[], int n) { ... }
```

Inside function:

```c
sizeof(A) == sizeof(int*)
```

---

## Character arrays and strings

C strings must be null terminated.

```c
char s[] = "Hello"; // includes \0
```

### strlen vs sizeof

```c
strlen(s) // 5
sizeof(s) // 6
```

---

## Array vs pointer for string literal

```c
char c1[] = "Hello"; // modifiable copy
char *c2 = "Hello";  // read-only literal
```

`c2[0]='A'` is undefined behavior.

---

## Pointer to array (array pointer)

Normal pointer:
```c
int *p = A;
```

Pointer to full array:
```c
int (*pa)[5] = &A;
```

Pointer arithmetic:
- `p+1` → next int
- `pa+1` → next whole array
