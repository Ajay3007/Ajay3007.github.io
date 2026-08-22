---
title: "Multidimensional Arrays & Pointers"
description: "Multidimensional Arrays & Pointers C stores multidimensional arrays in row-major order ."
domain: languages
track: c-fundamentals
order: 5
ownHeader: true
url: /learning/programming-language/c/c-basics/multidimensional-arrays/
---

# Multidimensional Arrays & Pointers

C stores multidimensional arrays in **row-major order**.

Example:
```c
int B[2][3];
```

Meaning:
- array of 2 rows
- each row has 3 ints

So type of `B` is:
```c
int (*)[3]
```

---

## Correct pointer for 2D array

Wrong:
```c
int *p = B; // ❌
```

Correct:
```c
int (*p)[3] = B; // ✅
```

---

## Address arithmetic

Assume base address B=400  
Row size = 3 * 4 = 12 bytes

- `B` → 400
- `B+1` → 412

---

## Access formula

```c
B[i][j] == *(*(B+i) + j)
```

---

## Passing 2D array to function

Must specify column size:

```c
void f(int B[][3], int r);
```
or
```c
void f(int (*B)[3], int r);
```

---

## 3D arrays

```c
int arr[2][2][3];
int (*p)[2][3] = arr;
```

Dimensions after first must match.
