---
title: "Structures in C"
description: "Structures in C Structure groups variables of different types."
domain: languages
track: c-fundamentals
order: 9
url: /learning/programming-language/c/c-basics/structures/
---

# Structures in C

Structure groups variables of different types.

Example:
```c
struct Person {
    int age;
    char grade;
};
```

---

## Declaring and using

```c
struct Person p1;
p1.age = 10;
p1.grade = 'A';
```

---

## Dot vs Arrow

```c
struct Person *ptr = &p1;
printf("%d", ptr->age);
```

- `.` for variable
- `->` for pointer

---

## Initialization

```c
struct Person p2 = {10,'A'};
```

Designated init:
```c
struct Person p3 = {.grade='B', .age=20};
```

---

## Passing struct

By value:
```c
void f(struct Person p);
```

By pointer (recommended):
```c
void f(struct Person *p);
```

---

## typedef

```c
typedef struct Person {
    int age;
    char grade;
} Person;
```

---

## Shallow vs Deep copy (important)

If struct contains pointer:

```c
typedef struct {
    char *name;
    int age;
} Emp;
```

Copying:
```c
Emp e2 = e1;
```
Only pointer copied → shallow copy.

Need deep copy manually (malloc + strcpy).

---

## Self referential struct

Used in linked list:

```c
typedef struct Node{
    int data;
    struct Node *next;
} Node;
```
