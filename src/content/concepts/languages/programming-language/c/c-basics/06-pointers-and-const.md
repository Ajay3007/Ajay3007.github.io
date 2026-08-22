---
title: "Pointers and const"
description: "Pointers and const Rule: ✅ const binds to left side; if none, binds to right."
domain: languages
track: c-fundamentals
order: 6
ownHeader: true
url: /learning/programming-language/c/c-basics/pointers-const/
---

# Pointers and `const`

Rule:
✅ `const` binds to left side; if none, binds to right.

---

## 1) Pointer to const (data const)

```c
int a=10,b=20;
const int *p = &a;
```

- can change pointer ✅
- cannot change data through p ❌

```c
p = &b;   // ✅
*p = 5;   // ❌
```

---

## 2) Const pointer (pointer const)

```c
int * const p = &a;
```

- cannot change pointer ❌
- can change data ✅

```c
*p = 5;  // ✅
p = &b;  // ❌
```

---

## 3) Const pointer to const data

```c
const int * const p = &a;
```

Both cannot change.

---

## Summary table

| Declaration | Change pointer? | Change data? |
|-----------|------------------|--------------|
| `const int *p` | ✅ yes | ❌ no |
| `int *const p` | ❌ no | ✅ yes |
| `const int *const p` | ❌ no | ❌ no |

---

## Reading trick (right to left)

- `int * const p` → p is const pointer to int
- `const int * p` → p is pointer to const int
