---
layout: editorial
title: "Linked List Cycle Solution"
problem_id: "141"
date: 2026-02-25T01:03:22.320Z
---

# Linked List Cycle - Solution

**LeetCode #141** | **Difficulty:** Easy

---

## Approach

### Problem
Detect if a linked list has a cycle. A cycle exists if a node's next pointer eventually points back to a previously visited node.

### Two Strategies

**1. Brute Force - Hash Map (Cache)**
- Store each visited node in a hash map as we traverse
- If we encounter a node already in the map, a cycle exists
- **Time:** O(n), **Space:** O(n)

**2. Optimized - Two Pointers (Floyd's Cycle Detection)**
- Use slow pointer (moves 1 step) and fast pointer (moves 2 steps)
- If they meet, a cycle exists; if fast reaches null, no cycle
- **Time:** O(n), **Space:** O(1)

The two-pointer approach is optimal because it uses constant space and detects cycles in a single pass.

---

## Algorithm Explanation

### Brute Force Approach

1. Create an empty hash map to track visited nodes
2. Traverse the list with a position counter
3. For each node:
   - Check if it exists in the hash map
   - If yes, return `true` (cycle detected)
   - If no, add it to the map with current position
4. Move to the next node
5. If we reach `null`, return `false` (no cycle)

### Optimized Approach (Floyd's Algorithm)

1. Initialize:
   - `slow` pointer to `nullptr` (will advance 1 step)
   - `fast` pointer to `head` (will advance 2 steps)

2. Traverse while `fast` and `fast->next` are not null:
   - Check if `slow == fast` → cycle detected
   - Move `slow` forward by 1 (or start at head if null)
   - Move `fast` forward by 2
   
3. If fast reaches null, no cycle exists

**Why it works:** In a cycle, the fast pointer "laps" the slow pointer, and they must meet at some point.

---

## Complexity Analysis

### Brute Force
- **Time Complexity:** O(n) - traverse each node once
- **Space Complexity:** O(n) - hash map stores all visited nodes

### Optimized (Two Pointers)
- **Time Complexity:** O(n) - traverse the list once; if cycle exists, they meet within n steps
- **Space Complexity:** O(1) - only two pointers, no extra data structures

---

## C++ Solution

### Brute Force Approach

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode *, int> cache;
        ListNode* cur = head;
        int curPos = 0;
        while(cur != nullptr) {
            if(cache.count(cur) != 0) {
                int pos = cache[cur];
                cout<<pos<<endl;
                return true;
            } else {
                cache[cur] = curPos++;
            }
            cur = cur->next;
        }
        return false;
    }
};
```

### Optimized Approach (Floyd's Cycle Detection)

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = nullptr;
        ListNode* fast = head;
        while(fast != nullptr && fast->next != nullptr) {
            if(slow == fast) return true;
            slow = (slow == nullptr) ? head : slow->next;
            fast = fast->next->next;
        }
        return false;
    }
};
```

---

## Key Insights

1. **Floyd's Algorithm:** The two-pointer technique is elegant and space-efficient
2. **Pointer Comparison:** We compare pointers (memory addresses), not values
3. **Meeting Point:** In a cycle, fast pointer catches slow pointer guaranteed
4. **No Extra Space:** Unlike hash map, pointers use constant space
5. **Single Pass:** Both approaches traverse the list once effectively

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
