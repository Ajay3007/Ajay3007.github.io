---
title: "Reverse Linked List - Solution"
description: "🔗 Reverse Linked List - Solution LeetCode 206 Difficulty: Easy --- Approach Use an iterative three-pointer technique to reverse the linked list in-place: - Maintain three…"
domain: dsa
order: 99
url: /learning/dsa/linked-list/leetcode-206-solution/
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

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/learning/dsa/linked-list/linked-list-problems" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="/learning/dsa/linked-list" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
