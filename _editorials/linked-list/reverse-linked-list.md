---
permalink: /editorials/reverse-linked-list/
layout: editorial
title: "Reverse Linked List Solution"
problem_id: "206"
date: 2026-02-25T01:03:22.321Z
---

# 🔗 Reverse Linked List - Solution

**LeetCode #206** | **Difficulty:** Easy

---

## Approach

Use an **iterative three-pointer technique** to reverse the linked list in-place:

- Maintain three pointers: `pre` (previous node), `cur` (current node), and `temp` (temporary storage)
- Traverse the list once, reversing the `next` pointer of each node to point backwards
- No extra data structure needed - reverse by changing pointer directions
- Handle edge case: empty list returns `nullptr`

This approach achieves O(1) space complexity by modifying pointers in-place without creating a new list.

---

## Algorithm Explanation

1. **Base Case:** If the list is empty (`head == nullptr`), return `nullptr`
2. **Initialize Pointers:**
   - `pre` = `nullptr` (previous node, starts as null)
   - `cur` = `head` (current node being processed)
   - `temp` (temporary pointer for swapping)
3. **Iteration:** While `cur` is not null:
   - Store current node in `temp`
   - Move `cur` to next node
   - Reverse the link: point `temp->next` to `pre`
   - Move `pre` to `temp`
4. **Return:** `pre` (new head of reversed list)

---

## Complexity Analysis

- **Time Complexity:** O(n) - Single pass through the list
- **Space Complexity:** O(1) - Only using constant extra space

---

## C++ Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr) return nullptr;
        ListNode* pre = nullptr;
        ListNode* cur = head;
        ListNode* temp;
        while(cur) {
            temp = cur;
            cur = cur->next;
            temp->next = pre;
            pre = temp;
        }
        return pre;
    }
};
```

---

