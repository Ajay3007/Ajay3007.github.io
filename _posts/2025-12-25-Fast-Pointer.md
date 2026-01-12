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

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/blogs' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← All Blogs</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Home 🏠</a>
</div>
