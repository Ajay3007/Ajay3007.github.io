---
layout: default
title: Function Pointers
permalink: /learning/programming-language/c/c-basics/function-pointers/
---

# Function Pointers

A function pointer stores the **address of a function**.

Used in:
- callbacks
- event-driven design
- state machines
- implementing polymorphism-like behavior in C

---

## Declaration syntax

```c
return_type (*ptr)(params);
```

Example:
```c
int (*fp)(int,int);
```

Wrong (function returning pointer):
```c
int *fp(int,int);
```

---

## Example

```c
#include <stdio.h>

int add(int a,int b){ return a+b; }

int main(){
    int (*fp)(int,int) = add;
    printf("%d\n", fp(2,3));     // 5
    printf("%d\n", (*fp)(2,3));  // 5
}
```

---

## Callback example

```c
int add(int a,int b){ return a+b; }
int sub(int a,int b){ return a-b; }

int operate(int x,int y, int (*op)(int,int)){
    return op(x,y);
}
```

Usage:
```c
operate(10,5,add);
operate(10,5,sub);
```

---

### Function Pointer Callback Flow Diagram

![Function Pointer Callback Flow]({{ '/assets/diagrams/learning/programming-language/c/c-basics/diagrams/function-pointer-callback.svg' | relative_url }}){:class="diagram-img"}

*Illustrates how function pointers enable callbacks, where a function like `operate()` calls different operations (`add/sub`) via a passed function pointer.*

---

## Array of function pointers

```c
int (*ops[2])(int,int) = {add, sub};
printf("%d\n", ops[0](10,5));
printf("%d\n", ops[1](10,5));
```

---

## Function pointer inside struct

```c
typedef struct {
    int value;
    void (*print)(int);
} Obj;
```

Used heavily in embedded and C libraries.
