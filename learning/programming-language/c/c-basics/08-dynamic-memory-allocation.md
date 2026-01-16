---
layout: default
title: Dynamic Memory Allocation
permalink: /learning/programming-language/c/c-basics/dynamic-memory/
---

# Dynamic Memory Allocation (Heap)

Dynamic memory allocation gives control over:
- when to allocate
- how much to allocate
- when to free

Used when:
- size unknown at compile time
- need resizable data structures

---

## malloc()

```c
void *malloc(size_t size);
```

- allocates bytes
- uninitialized memory
- returns NULL if fail

Example:
```c
int *p = malloc(sizeof(int));
if(!p) return;
*p = 10;
free(p);
p = NULL;
```

---

## calloc()

```c
void *calloc(size_t n, size_t size);
```

- allocates n blocks
- initializes all to 0

---

## realloc()

```c
void *realloc(void *ptr, size_t newSize);
```

May move block. Use safe pattern:

```c
int *tmp = realloc(p, newSize);
if(tmp) p = tmp;  // else old p valid
```

---

## Allocating arrays safely

```c
int n = 10;
int *arr = malloc(n * sizeof(*arr));
```

---

## free()

```c
free(p);
p = NULL;
```

---

### Dynamic Memory Allocation (malloc/free lifecycle) Diagram

![Dynamic Memory Allocation (malloc/free lifecycle)]({{ '/assets/diagrams/learning/programming-language/c/c-basics/diagrams/dma-activity.svg' | relative_url }}){:class="diagram-img"}

*Shows the lifecycle of dynamic allocation on heap using malloc/calloc, safe usage, and cleanup using `free()` and setting pointer to `NULL`.*

---

## Dynamic 2D array (important)

### Method 1: row pointers

```c
int r=3,c=4;
int **a = malloc(r*sizeof(*a));
for(int i=0;i<r;i++)
    a[i] = malloc(c*sizeof(**a));
```

Free:
```c
for(int i=0;i<r;i++) free(a[i]);
free(a);
```

### Method 2: contiguous block (faster)

```c
int *data = malloc(r*c*sizeof(int));
int (*a)[c] = (int (*)[c])data;
```

---

## Common DMA bugs

1) memory leak  
2) double free  
3) use-after-free  
4) forgetting NULL check  
5) overflow write
