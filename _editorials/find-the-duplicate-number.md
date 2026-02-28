---
layout: editorial
title: "Find the Duplicate Number"
problem_id: "287"
date: 2026-02-25T13:23:22.323Z
---

# Better Approach: Mark Visited Indices (Modify Array)

## Intuition
Since the numbers are in the range [1, n] and the array size is n+1,
there must be at least one duplicate.

Each value can be treated as a pointer to the next index.
If we keep following these pointers, eventually we will revisit
an index due to duplication.

So instead of using extra space like a hash set,
we can mark an index as visited by modifying its value.

If we encounter an index that is already marked,
that index is the duplicate.

## Approach
1. Start from index 0.
2. Let `x = nums[0]`.
3. Repeat:
   - If `nums[x] == 0`, it means we have already visited this index.
     So return `x` as the duplicate.
   - Otherwise:
     - Store `nums[x]` in a temporary variable.
     - Mark `nums[x] = 0` (visited).
     - Move to the next index using the stored value.
4. Continue until duplicate is found.

⚠ This modifies the input array, which violates the strict constraint
of the problem that asks not to modify the array.

## Complexity
- Time complexity:
  O(n)

  Each index is visited at most once.

- Space complexity:
  O(1)

  No extra data structures are used.

## Code
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int x = nums[0];
        while(1) {
            if(nums[x] == 0) return x;
            int y = nums[x];
            nums[x] = 0;
            x = y;
        }
    }
};
```


# Optimal Approach: Floyd’s Tortoise and Hare (Cycle Detection)

## Intuition
Since numbers are in the range [1, n], we can treat the array
like a linked list where:

index → nums[index]

Because there are n+1 numbers but only n possible values,
there must be a cycle in this structure.

The duplicate number is exactly the entry point of the cycle.

So we can use Floyd’s Cycle Detection Algorithm:
- Phase 1: Detect the cycle.
- Phase 2: Find the entrance of the cycle.

## Approach
1. Initialize:
   - `slow = nums[0]`
   - `fast = nums[nums[0]]`

2. Move:
   - `slow = nums[slow]`
   - `fast = nums[nums[fast]]`
   until they meet (cycle detected).

3. Reset `slow = 0`.

4. Move both one step at a time:
   - `slow = nums[slow]`
   - `fast = nums[fast]`
   until they meet again.

5. The meeting point is the duplicate number.

This works because:
- The duplicate creates a cycle.
- Floyd’s algorithm guarantees finding the cycle entrance.

This does NOT modify the array and satisfies all constraints.

## Complexity
- Time complexity:
  O(n)

  Phase 1: O(n)  
  Phase 2: O(n)

- Space complexity:
  O(1)

  Only two pointers are used.

## Code
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0], fast = nums[nums[0]];
        while(slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        slow = 0;
        while(slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};
```

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/linked-list/linked-list-problems' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Problems</a>
  <a href="{{ '/learning/dsa/linked-list' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Linked List Hub 🏠</a>
</div>
