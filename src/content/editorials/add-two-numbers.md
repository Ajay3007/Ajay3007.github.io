---
title: "Add Two Numbers Solution"
description: "Add Two Numbers — Two Approaches LeetCode 2 Difficulty: Medium Approach 1: Dummy-Node Version (New List) Intuition Each linked list represents a number in reverse order, where…"
problem_id: "2"
date: 2026-02-25
url: /editorials/add-two-numbers/
---

# Add Two Numbers — Two Approaches

**LeetCode #2** | **Difficulty:** Medium

## Approach 1: Dummy-Node Version (New List)

### Intuition
Each linked list represents a number in reverse order, where each node contains one digit.  
To add the two numbers, we simulate elementary addition digit by digit, keeping track of the carry.  

Instead of modifying the input lists, we build a new result list using a dummy head node.  
This avoids special handling for the first node and makes the implementation simpler and safer.

---

### Approach
1. Create a dummy node to serve as the head of the result list.
2. Use a pointer `curr` to build the result list.
3. Initialize `carry = 0`.
4. Traverse both lists while at least one list has nodes or `carry` is non-zero:
   - Add current digits from `l1` and `l2` (if present) and `carry`.
   - Compute:
     - `digit = sum % 10`
     - `carry = sum / 10`
   - Create a new node with `digit` and attach it to the result.
5. Move pointers forward in `l1` and `l2` when possible.
6. After traversal, return `dummy.next` as the result list.

This handles different list lengths and carry propagation automatically.

---

### Complexity
- **Time complexity:**  
  $$O(max(m, n))$$  
  Each node of both lists is processed once.

- **Space complexity:**  
  $$O(max(m, n))$$  
  A new list is created to store the result.

---

### Code (Dummy-Node Version)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* curr = &dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            int sum = carry;

            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            carry = sum / 10;

            curr->next = new ListNode(sum % 10);
            curr = curr->next;
        }

        return dummy.next;
    }
};
```

---

## Approach 2: In-Place Version (O(1) Space)

### Intuition
The two linked lists represent two non-negative integers in reverse order, where each node stores one digit.  
To add these numbers, we simulate manual addition digit by digit, starting from the least significant digit.  
At each step, we add the corresponding digits along with a carry and store the result back into the first list.  
By modifying `l1` in-place, we avoid creating a new linked list.

### Approach
1. Initialize `carry = 0` and use `l1` as the base list to store the result.
2. Traverse both lists simultaneously while both have next nodes:
   - Add `l1->val`, `l2->val`, and `carry`.
   - Update the current node value with `sum % 10`.
   - Update `carry = sum / 10`.
   - Move both pointers forward.
3. Process the last aligned nodes after the loop.
4. If `l1` ends before `l2`, attach the remaining part of `l2` to `l1`.
5. Propagate the carry forward in `l1`:
   - Keep adding `carry` to remaining nodes.
6. If a carry still remains after reaching the end, create a new node and append it.
7. Return the head of `l1` as the final result.

This approach performs addition directly on the first list and extends it only when needed.

### Complexity
- **Time complexity:**  
  $$O(max(m, n))$$  
  Each node of both lists is processed at most once.

- **Space complexity:**  
  $$O(1)$$  
  The addition is done in-place without using extra data structures (excluding the possible last node).

# Code (In-Place Version)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int num, carry = 0;
        ListNode *head = l1;

        while(l1->next && l2->next) {
            num = l1->val + l2->val + carry;
            carry = num / 10;
            num = num % 10;

            l1->val = num;
            l1 = l1->next;
            l2 = l2->next;
        }

        num = l1->val + l2->val + carry;
        carry = num / 10;
        num = num % 10;
        l1->val = num;

        if(!l1->next) { // l1 ends before l2
            l1->next = l2->next;
        }

        ListNode *pre = l1;
        l1 = l1->next;

        while(carry && l1) {
            pre = l1;

            num = l1->val + carry;
            carry = num / 10;
            num = num % 10;

            l1->val = num;
            l1 = l1->next;
        }

        if(carry) {
            pre->next = new ListNode(carry);
        }

        return head;
    }
};
```

---

