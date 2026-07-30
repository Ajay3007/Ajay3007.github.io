---
layout: learning
title: Merge Two Sorted Lists - Solution
permalink: /learning/dsa/linked-list/leetcode-21-solution/
---

# Merge Two Sorted Lists - Solution

**LeetCode #21** | **Difficulty:** Easy

---

## Intuition
Both input linked lists are already sorted.  
To merge them into a single sorted list, we can repeatedly choose the smaller value from the heads of both lists and append it to the result.  
This is similar to the merge step in merge sort and can be done efficiently in one pass.

Using a dummy node helps simplify the logic by avoiding special handling for the first node.

## Approach
1. Create a dummy node to act as the starting point of the merged list.
2. Use a pointer `curr` to build the merged list.
3. While both `list1` and `list2` are not null:
   - Compare `list1->val` and `list2->val`.
   - Attach the smaller node to `curr->next`.
   - Move the corresponding list pointer forward.
   - Move `curr` forward.
4. After the loop, one list may still have remaining nodes.
   - Attach the remaining part directly to `curr->next`.
5. Return `dummy.next` as the head of the merged list.

This merges both lists in-place without creating new nodes.

## Complexity
- **Time complexity:**  
  $$O(n + m)$$  
  Where `n` and `m` are the lengths of `list1` and `list2`. Each node is processed once.

- **Space complexity:**  
  $$O(1)$$  
  No extra data structures are used; the merge is done in-place.

## Code
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode *curr = &dummy;

        while(list1 && list2) {
            if(list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }

        if(!list1) curr->next = list2;
        if(!list2) curr->next = list1;

        return dummy.next;
    }
};
```

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
