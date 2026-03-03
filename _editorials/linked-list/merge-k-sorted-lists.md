---
permalink: /editorials/merge-k-sorted-lists/
layout: editorial
title: "Merge k Sorted Lists"
problem_id: "23"
date: 2026-02-27T13:23:22.323Z
---

# Sequential Pairwise Merging of K Lists (Iterative Two-List Merge)

**LeetCode #23** | **Difficulty:** Hard

## Intuition
To merge k sorted linked lists, we can reuse the classic
“merge two sorted lists” technique.

Instead of trying to merge all k lists at once,
we merge them one by one:

- Merge list 0 and list 1
- Merge the result with list 2
- Merge the result with list 3
- Continue until all lists are merged

Since merging two sorted lists can be done efficiently in linear time,
we repeatedly apply this operation until only one final list remains.

This is a straightforward and intuitive extension of
the 2-list merge problem.

## Approach
1. Handle edge cases:
   - If `k == 0`, return `nullptr`
   - If `k == 1`, return the only list

2. Use a helper function `mergeTwoLists`:
   - Create a dummy node.
   - Compare nodes from both lists.
   - Attach the smaller node to the result.
   - Move pointers forward.
   - Append remaining nodes at the end.

3. Sequentially merge:
   - Start with `head = lists[0]`
   - For every `i` from 1 to k-1:
       head = mergeTwoLists(head, lists[i])

4. Return the final merged head.

This approach is simple and leverages reusable logic.

## Complexity
Let:
- k = number of lists
- N = total number of nodes across all lists

- Time complexity:
  O(N * k)

  Each merge operation can take up to O(N),
  and we perform it (k - 1) times in the worst case.

- Space complexity:
  O(1)

  We only use a few pointers and a dummy node.
  No extra data structures are used.

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
        ListNode dummy = ListNode(0);
        ListNode* cur = &dummy;
        while(list1 && list2) {
            if(list1->val <= list2->val) {
                cur->next = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        if(list1) cur->next = list1;
        if(list2) cur->next = list2;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int k = lists.size();
        if(k == 0) return nullptr;
        if(k == 1) return lists[0];
        ListNode* head = lists[0];
        for(int i=1; i<k; i++) {
            head = mergeTwoLists(head, lists[i]);
        }
        return head;
    }
};
```

---

# Min-Heap (Priority Queue) Approach – Optimal O(N log k)

## Intuition
At any moment while merging k sorted lists, the next smallest element
must be among the heads of the k lists.

So instead of merging lists sequentially, we can:
- Always pick the smallest current node among all lists.
- After picking a node, push its next node into consideration.

This is exactly what a Min-Heap (Priority Queue) helps us do efficiently.

The heap will always contain at most k elements —
one current node from each list.

## Approach
1. Handle edge case:
   - If lists is empty, return nullptr.

2. Create a Min-Heap (Priority Queue):
   - Store ListNode* in the heap.
   - Use a custom comparator to order nodes by value.

3. Push the head of each non-empty list into the heap.

4. Create a dummy node to build the result list.

5. While heap is not empty:
   - Pop the smallest node.
   - Attach it to the result.
   - If the popped node has a next node,
     push that next node into the heap.

6. Return dummy.next.

This ensures we always select the globally smallest available node.

## Complexity
Let:
- k = number of lists
- N = total number of nodes across all lists

- Time complexity:
  O(N log k)

  Each of the N nodes is pushed and popped from the heap once.
  Heap operations take O(log k).

- Space complexity:
  O(k)

  Heap stores at most k nodes at any time.

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
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // min-heap
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;

        // Push first node of each list
        for(auto node : lists) {
            if(node) pq.push(node);
        }

        ListNode dummy(0);
        ListNode* cur = &dummy;

        while(!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();

            cur->next = node;
            cur = cur->next;

            if(node->next) {
                pq.push(node->next);
            }
        }

        return dummy.next;
    }
};
```

---

