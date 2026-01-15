---
layout: default
title: Arrays and Pointers
permalink: /learning/programming-language/c/c-basics/arrays-and-pointers/
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
