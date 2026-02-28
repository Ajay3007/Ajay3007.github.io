---
layout: editorial
title: "Reorder List"
problem_id: "143"
date: 2026-02-25T13:23:22.323Z
---

# Split, Reverse Second Half, and Merge Alternately

**LeetCode #143** | **Difficulty:** Medium

## Intuition
The required reordering pattern is:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

If we observe carefully, this pattern can be achieved by:
1. Splitting the list into two halves.
2. Reversing the second half.
3. Merging the two halves alternately (zig-zag).

So the problem naturally reduces to three smaller linked list operations:
- Find middle
- Reverse second half
- Merge alternately

## Approach
1. **Find the middle of the list**
   - Use slow and fast pointer technique.
   - Fast moves 2 steps, slow moves 1 step.
   - When fast reaches the end, slow is at the midpoint.

2. **Reverse the second half**
   - Reverse the list starting from `slow->next`.
   - Disconnect the first half by setting `slow->next = nullptr`.

3. **Merge the two halves**
   - Take one node from first half.
   - Then one node from reversed second half.
   - Continue alternating until first half is exhausted.

## Complexity
- Time complexity:
  **`O(n)`**

  Finding middle: **`O(n)`** 
  Reversing list: **`O(n)`**  
  Merging lists: **`O(n)`** 
  Total: **`O(n)`**

- Space complexity:
  **`O(n)`**

  Due to recursive stack used in the reverse function.
  (Can be optimized to O(1) using iterative reversal.)

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

    ListNode *reverse(ListNode *head) {
        if(!head || !head->next) return head;
        ListNode *temp = reverse(head->next);
        head->next->next = head;
        head->next = nullptr;
        return temp;
    }

    ListNode *mergeZigZag(ListNode *l1, ListNode* l2) {
        ListNode *head = l1;
        ListNode *temp;
        bool flag = true;
        while(l1) {
            if(flag) {
                temp = l1;
                l1 = l1->next;
                temp->next = l2;
            } else {
                temp = l2;
                l2 = l2->next;
                temp->next = l1;
            }
            flag = !flag;
        }
        return head;
    }

    void reorderList(ListNode* head) {
        if(!head || !head->next) return;
        ListNode *slow = nullptr;
        ListNode *fast = head;
        while(fast && fast->next) {
            slow = (slow == nullptr) ? head : slow->next;
            fast = fast->next->next;
        }
        // slow pointing to mid. Reverse after slow
        ListNode *l2 = reverse(slow->next);
        slow->next = nullptr;
        head = mergeZigZag(head, l2);
    }
};
```

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
