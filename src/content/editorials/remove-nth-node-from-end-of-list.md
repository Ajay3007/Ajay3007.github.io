---
title: "Remove Nth Node From End of List Solution"
description: "Remove Nth Node From End of List — Two Approaches LeetCode 19 Difficulty: Medium --- Approach 1: Two-Pass Solution (Length Calculation) Intuition To remove the Nth node from…"
problem_id: "19"
date: 2026-02-25
url: /editorials/remove-nth-node-from-end-of-list/
---

# Remove Nth Node From End of List — Two Approaches

**LeetCode #19** | **Difficulty:** Medium

---

## Approach 1: Two-Pass Solution (Length Calculation)

### Intuition
To remove the Nth node from the end, we can first find the total length of the linked list.  
Once the length is known, the problem becomes removing the `(length - n)`th node from the start.  
This transforms the problem into a simple indexed deletion.

---

### Approach
1. Traverse the list once to count the total number of nodes.
2. Compute the position of the node to remove from the beginning:
   `from_start = total - n`.
3. Traverse again until reaching the node just before the target.
4. If `from_start == 0`, remove the head node.
5. Otherwise, adjust pointers to skip the target node.
6. Return the updated head.

---

### Complexity
- **Time complexity:**  
  $$O(n)$$ — two full traversals of the list.

- **Space complexity:**  
  $$O(1)$$ — only constant extra pointers.

---

### Code (Two-Pass)
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int total = 0;
        ListNode *curr = head;
        while(curr) {
            curr = curr->next;
            total++;
        }

        int from_start = total - n;
        curr = nullptr;

        while(from_start--) {
            curr = (curr == nullptr) ? head : curr->next;
        }

        if(!curr) return head->next;

        ListNode *temp = curr->next;
        curr->next = temp->next;
        temp == nullptr;

        return head;
    }
};
```

## Approach 2: One-Pass Solution (Fast & Slow Pointers)

### Intuition
If we maintain a fixed distance of `n` nodes between two pointers, then when the front pointer reaches the end, the back pointer will be positioned just before the node to be removed.
This allows us to remove the target node in a single traversal.

---

### Approach

1. Initialize two pointers `front` and `back` at `head`.
2. Move `front` forward by `n` steps.
3. If `front` becomes `NULL`, it means the head node must be removed.
4. Otherwise, move both `front` and `back` together until `front` reaches the end.
5. At this point, `back->next` is the node to be removed.
6. Adjust pointers to skip the target node.
7. Return the updated head.

---

### Complexity

- **Time complexity:**  
  $$O(n)$$ — single traversal of the list.

- **Space complexity:**  
  $$O(1)$$ — only constant extra pointers.

---

### Code (One-Pass)
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *front = head;
        ListNode *back = head;

        while(n--) front = front->next;

        if(!front) return head->next;

        front = front->next;

        while(front) {
            front = front->next;
            back = back->next;
        }

        back->next = back->next->next;
        return head;
    }
};

```

---

## Summary

| Approach  | Traversals | Time  | Space | Interview Preferred |
|-----------|------------|-------|-------|---------------------|
| Two-Pass  | 2          | O(n)  | O(1)  | ❌                  |
| One-Pass  | 1          | O(n)  | O(1)  | ✅                  |

- The **two-pass approach** is easier to understand.
- The **one-pass approach** is more efficient and preferred in interviews.

---

