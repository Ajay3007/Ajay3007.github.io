---
layout: post
title: "Two Pointer Technique Explained"
date: 2025-01-05
categories: [dsa, algorithms]
excerpt: "Learn the Two Pointer Technique, a powerful approach used in DSA and algorithms to solve array and string problems efficiently."
---

## What is the Two Pointer Technique?

The **Two Pointer Technique** is a common algorithmic approach where we use **two indices (pointers)** to traverse a data structure like an array or string.

It is widely used in:
- **DSA**
- **Algorithms**
- **Competitive Programming**

---

## Why use Two Pointers?

- Reduces time complexity
- Avoids unnecessary nested loops
- Makes solutions cleaner and faster

---

## Example Problem

**Problem:**  
Check if there exists a pair in a sorted array whose sum is equal to `X`.

### Approach
- One pointer at the start
- One pointer at the end
- Move pointers based on the current sum

---

## Sample Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool hasPairWithSum(vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == x) return true;
        else if (sum < x) left++;
        else right--;
    }
    return false;
}
```