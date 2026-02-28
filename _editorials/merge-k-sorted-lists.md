---
layout: editorial
title: "Merge k Sorted Lists"
problem_id: "23"
date: 2026-02-27T13:23:22.323Z
---

# Sequential Pairwise Merging of K Lists (Iterative Two-List Merge)

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

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
