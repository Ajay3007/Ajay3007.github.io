---
layout: default
title: Middle of the Linked List - Solution
permalink: /learning/dsa/linked-list/leetcode-876-solution/
---

# 🔗 Middle of the Linked List - Solution

**LeetCode #876** | **Difficulty:** Easy

---

## Approach

Use the **slow and fast pointer (tortoise and hare) technique** to find the middle node:

- Initialize two pointers: `slow` and `fast`, both starting at head
- Move `slow` one step at a time, `fast` two steps at a time
- When `fast` reaches the end, `slow` will be at the middle
- Handles both odd and even length lists correctly
- No need to count nodes first - single pass solution

This approach achieves O(1) space complexity with optimal O(n/2) time complexity.

---

## Algorithm Explanation

1. **Initialize Pointers:**
   - `slow` = `head` (moves one step at a time)
   - `fast` = `head` (moves two steps at a time)

2. **Traverse the List:**
   - While `fast != nullptr` AND `fast->next != nullptr`:
     - Move `slow` one step forward: `slow = slow->next`
     - Move `fast` two steps forward: `fast = fast->next->next`

3. **Return Result:**
   - When loop ends, `slow` points to the middle node
   - For even-length lists, returns the second middle node

---

## Complexity Analysis

- **Time Complexity:** O(n/2) ≈ O(n) - Fast pointer traverses half the list at double speed
- **Space Complexity:** O(1) - Only using two pointer variables

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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
