---
layout: post
title: "Slow and Fast Pointer"
date: 2025-12-25
---

Slow and Fast pointer are very useful in Linked List.

## Concept



## Problems

**1. <a href="https://leetcode.com/problems/middle-of-the-linked-list/description/" target="_blank" rel="noopener">Leetcode 876. Middle of the Linked List</a>**


```cpp
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

**For Full Solution <a href="{{ '/learning/dsa/LinkedList/leetcode-876.cpp' | relative_url }}" target="_blank" rel="noopener">CLICK HERE</a>**

---

Enjoy blogging!
