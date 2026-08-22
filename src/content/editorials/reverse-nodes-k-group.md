---
title: "Reverse Nodes in k-Group"
description: "Iterative Block Reversal with Tail Reconnection (O(n) Time O(1) Space) LeetCode 25 Difficulty: Hard Intuition The problem asks us to reverse nodes in groups of size k ."
problem_id: "25"
date: 2026-02-28
url: /editorials/reverse-nodes-k-group/
---

# Iterative Block Reversal with Tail Reconnection (O(n) Time | O(1) Space)

**LeetCode #25** | **Difficulty:** Hard

## Intuition
The problem asks us to reverse nodes in groups of size `k`.

Instead of reversing the entire list at once, we can think in terms of **independent blocks of size k**:
- If a block has exactly `k` nodes → reverse it.
- If fewer than `k` nodes remain → leave them as it is.

So the problem reduces to repeating three operations:
1. Check if `k` nodes exist.
2. Reverse exactly `k` nodes.
3. Reconnect the reversed block with the previous and next parts.

The key challenge is handling pointer connections correctly between groups.

## Approach
1. Maintain:
   - `head` → start of current group.
   - `cur` → used to check if k nodes exist.
   - `newHead` → head of final modified list.
   - `kTail` → tail of previously reversed group.

2. For each group:
   - Move `cur` forward `k` steps to check if `k` nodes are available.
   - If count == k:
     - Reverse the `k` nodes using helper `reverseLL`.
     - If this is the first reversed group, update `newHead`.
     - Connect previous group’s tail (`kTail`) to the reversed head.
     - Update `kTail` to current group's original head (which becomes tail after reversal).
     - Move `head` forward to the next group start.

3. If fewer than `k` nodes remain:
   - Attach remaining nodes as-is.

4. Return:
   - `newHead` if at least one reversal happened.
   - Otherwise original `head`.

### Helper Function
`reverseLL(head, k)`:
- Iteratively reverses exactly `k` nodes.
- Uses standard 3-pointer technique.
- Returns new head of reversed block.

## Complexity
- Time complexity:
  O(n)

  Each node is visited a constant number of times.
  Every node participates in exactly one reversal.

- Space complexity:
  O(1)

  Only a few pointer variables are used.
  No recursion or extra data structures.

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
    ListNode* reverseLL(ListNode* head, int k) {
        ListNode* cur = head;
        ListNode* pre = nullptr;
        while(k>0) {
            ListNode* temp = cur;
            cur = cur->next;
            temp->next = pre;
            pre = temp;
            k--;
        }
        return pre;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* cur = head;
        ListNode* newHead = nullptr;
        ListNode* kTail = nullptr;
        while(cur) {
            int count = 0;
            cur = head;
            while(count<k && cur) {
                cur = cur->next;
                count++;
            }
            if(count==k) {
                ListNode* revHead = reverseLL(head, k);
                if(newHead == nullptr) newHead = revHead;
                if(kTail!=nullptr) kTail->next = revHead;
                kTail = head;
                head = cur;
            }
        }
        if(kTail!=nullptr) kTail->next = head;
        return (newHead==nullptr) ? head : newHead;
    }
};
```

---

