---
layout: learning
title: C Pointer Practice
permalink: /learning/programming-language/c/c-basics/pointer-practice/
---

# C Pointer Practice Pack Documentation

This document explains pointer, memory, and data structure concepts
using practical C examples.

---

<!-- C Pointer Practice -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #3b82f6; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🔗</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">C Pointer Practice</h3>
    </div>
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">This code contains pointer, memory, and data structure concepts using practical C examples.</p>
    <a href="{{ '/learning/programming-language/c/practice/pointer_practice.c' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Code →
    </a>
  </div>

---

## Compilation

``` bash
gcc -O0 -g pointer_practice.c -o pointer_practice
./pointer_practice
```

---

## Task 1: Pointer Basics

Demonstrates address-of, dereference, and modifying data via pointer.

``` c
void update(int *p);
```

Concepts: - `&` operator - `*` dereference - Stack vs heap address

---

## Task 2: Swap Using Pointers

Swaps two integers using pointer indirection.

``` c
void swap_int(int *a, int *b);
```

Concept: Pass-by-address.

---

## Task 3: Array Sum Using Pointers

Traverse array using pointer arithmetic.

``` c
int sum_array(int *arr, int n);
```

Concept: `*(arr+i)` vs `arr[i]`.

---

## Task 4: Find Max Element

Returns pointer to maximum element.

``` c
int* max_ptr(int *arr, int n);
```

Concept: Returning addresses.

---

## Task 5: Reverse Array

In-place reversal using two pointers.

``` c
void reverse_int_array(int *arr, int n);
```

Concept: Two-pointer technique.

---

## Task 6: Custom strlen

Manual string length calculation.

``` c
size_t my_strlen(const char *s);
```

Concept: Null-terminated strings.

---

## Task 7: Custom strcpy

Copies string including null terminator.

``` c
void my_strcpy(char *dst, const char *src);
```

Concept: Safe copying.

---

## Task 8: Reverse String

In-place string reversal.

``` c
void reverse_str(char *s);
```

Concept: Pointer traversal.

---

## Task 9: Char Array vs Char Pointer

Difference between stack array and string literal.

``` c
char arr[] = "hello";
const char *ptr = "hello";
```

Concept: Mutability and storage.

---

## Task 10: 2D Array with Pointers

Printing matrix using pointer arithmetic.

``` c
void print2D(int (*p)[4], int rows);
```

Concept: Pointer to array.

---

## Task 11: Row Sum

Calculates row-wise sum.

``` c
void row_sum(int (*p)[4], int rows, int *out);
```

---

## Task 12: 3D Array Access

Access 3D array elements using pointers.

``` c
int get3D(int (*p)[3][4], int i, int j, int k);
```

---

## Task 13: Const Pointers

Understanding const with pointers.

``` c
const int *p1;
int *const p2;
const int *const p3;
```

---

## Task 14: Const Correctness

Demonstrates const-safe APIs.

``` c
int sum_const(const int *arr, int n);
```

---

## Task 15: Dynamic Allocation

Heap allocation using malloc/free.

``` c
int* create_array(int n);
```

Concept: Manual memory management.

---

## Task 16: Dynamic 2D Allocation

Contiguous 2D allocation.

``` c
int** alloc2D(int rows, int cols);
```

Freeing:

``` c
free(m[0]);
free(m);
```

---

## Task 18-20: Structures

Using structs and pointers.

``` c
struct User;
struct User* create_user(...);
```

Concepts: - Arrow operator - Heap objects

---

## Task 21: Packet Header Parsing

Parsing binary buffer safely.

``` c
int parse_header(const uint8_t *buf, int size, struct Header *out);
```

Concepts: - Endianness - Buffer validation - Protocol parsing

---

## Key Learnings

-   Pointer arithmetic
-   Safe memory handling
-   String manipulation
-   Multi-dimensional arrays
-   Struct management
-   Buffer parsing

---

## Interview Relevance

These exercises are relevant for:

-   Systems programming
-   Networking/dataplane
-   Embedded C
-   Performance engineering

---

<!-- C Pointer Practice -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #3b82f6; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🔗</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">C Pointer Practice</h3>
    </div>
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">This code contains pointer, memory, and data structure concepts using practical C examples.</p>
    <a href="{{ '/learning/programming-language/c/practice/pointer_practice.c' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Code →
    </a>
  </div>

---