---
title: "Singly Linked List"
description: "📘 Singly Linked List – Basics & Problem-Solving Guide Complete guide to singly linked lists, fundamental operations, patterns, and interview strategies."
domain: dsa
order: 99
ownHeader: true
url: /learning/dsa/linked-list/singly-linked-list/
---

# 📘 Singly Linked List – Basics & Problem-Solving Guide

Complete guide to singly linked lists, fundamental operations, patterns, and interview strategies.

---

## Table of Contents

**Part 1: Fundamentals**
- [1. What Is a Linked List?](#what-is-linked-list)
- [2. Why Linked Lists?](#why-linked-lists)
- [3. Core Terminology](#core-terminology)

**Part 2: Operations & Patterns**
- [4. Fundamental Operations](#fundamental-operations)
  - [4.1 Traverse](#traverse)
  - [4.2 Insert at Head](#insert-head)
  - [4.3 Insert at Tail](#insert-tail)
  - [4.4 Delete Head](#delete-head)
  - [4.5 Delete by Value](#delete-value)
- [5. Golden Rules for Linked Lists](#golden-rules)

**Part 3: Problem-Solving**
- [6. How to Approach Any Linked List Problem](#approach-strategy)
- [7. Most Important Patterns](#important-patterns)
- [8. Common Mistakes to Avoid](#common-mistakes)

**Part 4: Interview Guide**
- [9. Practice Order](#practice-order)
- [10. Interview Mindset Tip](#interview-mindset)

---

## 1. What Is a Linked List? {#what-is-linked-list}

A linked list is a **linear data structure** where each element (node) contains:

- **data** — the value stored
- **a pointer to the next node** — the link

Nodes are **not stored contiguously in memory**.

### 1.1 Singly Linked List Node

```cpp
struct ListNode {
    int val;
    ListNode* next;
};
```

---

## 2. Why Linked Lists? {#why-linked-lists}

| Feature | Array | Linked List |
|---|---|---|
| **Memory** | Contiguous | Non-contiguous |
| **Access** | O(1) random | O(n) sequential |
| **Insertion** | Costly | O(1) (if pointer known) |
| **Size** | Fixed | Dynamic |

👉 **Linked lists shine when frequent insertions/deletions are needed.**

---

## 3. Core Terminology {#core-terminology}

- **Head** → first node
- **Tail** → last node
- **NULL / nullptr** → end of list
- **Traversal** → visiting nodes sequentially

---

## 4. Fundamental Operations {#fundamental-operations}

### 4.1 Traverse a Linked List {#traverse}

```cpp
ListNode* curr = head;
while (curr != nullptr) {
    cout << curr->val << " ";
    curr = curr->next;
}
```

### 4.2 Insert at Head {#insert-head}

```cpp
ListNode* insertAtHead(ListNode* head, int val) {
    ListNode* node = new ListNode(val);
    node->next = head;
    return node;
}
```

### 4.3 Insert at Tail {#insert-tail}

```cpp
ListNode* insertAtTail(ListNode* head, int val) {
    ListNode* node = new ListNode(val);
    if (!head) return node;

    ListNode* curr = head;
    while (curr->next) curr = curr->next;
    curr->next = node;
    return head;
}
```

### 4.4 Delete Head {#delete-head}

```cpp
ListNode* deleteHead(ListNode* head) {
    if (!head) return nullptr;
    ListNode* temp = head;
    head = head->next;
    delete temp;
    return head;
}
```

### 4.5 Delete by Value {#delete-value}

```cpp
ListNode* deleteByValue(ListNode* head, int val) {
    if (!head) return nullptr;
    if (head->val == val) return deleteHead(head);

    ListNode* curr = head;
    while (curr->next && curr->next->val != val)
        curr = curr->next;

    if (curr->next) {
        ListNode* temp = curr->next;
        curr->next = temp->next;
        delete temp;
    }
    return head;
}
```

---

## 5. Golden Rules for Linked Lists {#golden-rules}

### 🔑 Rule 1: Never Lose the Head

Always keep a pointer to the head. If you lose it, the entire list becomes inaccessible.

### 🔑 Rule 2: Before Accessing

| Access | Condition |
|---|---|
| `node->val` | `node != nullptr` |
| `node->next` | `node != nullptr` |
| `node->next->next` | `node && node->next` |

### 🔑 Rule 3: Dummy Node Pattern

Use dummy nodes to simplify edge cases.

```cpp
ListNode dummy;
dummy.next = head;
ListNode* curr = &dummy;
```

**Used in:**
- Merge lists
- Delete Nth node
- Partition list

---

## 6. How to Approach Any Linked List Problem {#approach-strategy}

### ✅ Step-by-Step Strategy

**Step 1: Identify the Pattern**

Ask yourself:
- Traversal?
- Two pointers?
- Reversal?
- Merge?
- Cycle detection?

**Step 2: Handle Base Cases First**

```cpp
if (!head || !head->next) return head;
```

**Step 3: Draw the List (Mentally or on Paper)**

Visualize:
```
1 → 2 → 3 → 4 → NULL
```

Track pointer movement step-by-step.

**Step 4: Move Pointers Carefully**

Update pointers before losing access:

```cpp
next = curr->next;
curr->next = prev;
```

**Step 5: Return the Correct Node**

- Sometimes return `head`
- Sometimes return `dummy.next`
- Sometimes return `slow` or `prev`

---

## 7. Most Important Patterns {#important-patterns}

### 🔁 Reversal Pattern

**Used in:**
- Reverse List
- Reverse K Group
- Palindrome List

### 🐢🐇 Slow–Fast Pointer (Floyd's Algorithm)

**Used in:**
- Find middle
- Detect cycle
- Remove Nth from end

### 🔗 Merge Pattern

**Used in:**
- Merge sorted lists
- Sort list (merge sort)

---

## 8. Common Mistakes to Avoid {#common-mistakes}

❌ Accessing `next` without null check  
❌ Forgetting to break links  
❌ Losing head pointer  
❌ Returning wrong node  
❌ Mixing object & pointer (`ListNode` vs `ListNode*`)

---

## 9. Practice Order (Highly Recommended) {#practice-order}

### Beginner
- Traverse list
- Insert/Delete
- Reverse list

### Intermediate
- Middle of list
- Detect cycle
- Merge two lists

### Advanced
- Sort list
- Reverse K group
- Copy random pointer list

---

## 10. Interview Mindset Tip {#interview-mindset}

**When stuck:**

> "Let me use a dummy node to simplify edge cases."

This line alone shows strong linked list maturity to interviewers.

---

---

<div style="background: linear-gradient(135deg, #fecaca 0%, #fca5a5 100%); border-left: 4px solid #ec4899; border-radius: 12px; padding: 2rem; margin: 2.5rem 0; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.15);">
  <div style="text-align: center;">
<h2 style="margin-top: 0; color: #be123c;">Ready to Practice?</h2>
<p style="color: #7c2d12; margin: 0.5rem 0 1.5rem 0;">Test your understanding with curated problems from top platforms</p>
<a href="/learning/dsa/linked-list/linked-list-problems/" style="display:inline-block;padding:14px 32px;background:linear-gradient(135deg, #ec4899 0%, #f43f5e 100%);color:white;border-radius:8px;text-decoration:none;font-weight:600;font-size:1.05rem;box-shadow:0 4px 12px rgba(244, 63, 94, 0.3);transition:transform 0.2s;">
      📝 Practice Problems
</a>
  </div>
</div>

---

<div style="text-align: center; margin-top: 2rem;">
  <a href="/learning/dsa/linked-list" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;">← Back to Linked List</a>
  <a href="/learning/dsa" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;margin-left:10px;">DSA Hub 🏠</a>
</div>

