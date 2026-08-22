---
title: "Pointers in C"
description: "Pointers in C/C++ Pointers store addresses ."
domain: languages
track: c-fundamentals
order: 2
url: /learning/programming-language/c/c-basics/pointers/
---

# Pointers in C/C++

Pointers store **addresses**. In C, they are core to arrays, strings, DMA, and callbacks.

Example:
```c
int a = 5;
int *p = &a;

printf("%d\n", a);    // 5
printf("%p\n", (void*)&a);
printf("%p\n", (void*)p);
printf("%d\n", *p);   // 5
```

---

## Pointer size

Depends on architecture, not type:

- 32-bit → 4 bytes
- 64-bit → 8 bytes

So `int*`, `char*`, `double*` all same size on same machine.

---

## Why pointer type matters?

Pointer type decides:
1) how many bytes to read on dereference  
2) pointer arithmetic step size

Example:
```c
int a = 1025;
int *p = &a;
char *c = (char*)p;

printf("%d\n", *p); // reads 4 bytes
printf("%d\n", *c); // reads 1 byte
```

This also relates to **endianness**.

---

## Dereferencing

- `*p` = value stored at address present in pointer.

```c
int a = 10;
int *p = &a;
printf("%d", *p);
```

---

### Pointer Diagram

![Pointer](/assets/diagrams/learning/programming-language/c/c-basics/diagrams/pointers-object.svg){:class="diagram-img"}

*Explains the pointer mental model—how an `int*` points to an integer variable and how an `int**` (pointer-to-pointer) points to the `int*` pointer.*

---

## Special pointer types

### 1) NULL pointer

```c
int *ptr = NULL;
```

Always init pointers to avoid wild pointers.

### 2) void pointer

Generic pointer:
```c
void *vp;
```
- cannot dereference without casting
- `malloc` returns `void*`

Example:
```c
int a=10;
void *vp=&a;
printf("%d\n", *(int*)vp);
```

---

## Wild pointer vs Dangling pointer

Wild:
```c
int *p; // uninitialized
```

Dangling:
```c
int *p = malloc(4);
free(p);   // p now dangling
p = NULL;
```

---

## Pointer arithmetic

If `p` is `int*` and p=200:
- `p+1` = 204

Formula:
```
p + n == p + n*sizeof(*p)
```

### Pointer subtraction

Allowed if inside same array:
```c
ptr2 - ptr1
```

returns element distance.

❌ Adding pointers is invalid.

---

## Pointer to pointer

```c
int x = 5;
int *p = &x;
int **q = &p;
int ***r = &q;
```

Used in:
- modifying pointer from function
- dynamic 2D allocation
- linked list operations

---

## Call by value vs reference

C is call-by-value, but we emulate reference using pointers.

### Value

```c
void inc(int a) { a++; }
```

### Reference

```c
void inc(int *p) { (*p)++; }
```

---

## Common pointer bugs (must know)

1. dereferencing wild pointer
2. dereferencing NULL
3. use-after-free
4. buffer overflow/out-of-bounds
5. wrong cast causing misaligned access
