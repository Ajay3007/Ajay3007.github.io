---
permalink: /editorials/binary-tree-zigzag-level-order-traversal/
layout: editorial
title: "Binary Tree Zigzag Level Order Traversal Solution"
problem_id: "103"
date: 2026-03-04T15:36:08.323Z
---

# BFS Level Order Traversal with Direction Toggle (Queue + Deque)

**LeetCode #103** | **Difficulty:** Medium

## Intuition
The zigzag traversal is very similar to a normal **level order traversal (BFS)** of a binary tree.  
The only difference is that the direction of traversal alternates for each level:

- Level 0 → Left to Right
- Level 1 → Right to Left
- Level 2 → Left to Right
- ...

So instead of changing how we traverse the tree, we can simply change **how we store the values of each level**.

A boolean flag can help track whether the current level should be processed **left-to-right** or **right-to-left**.

## Approach
1. **Handle edge case**
   - If the root is `nullptr`, return an empty result.

2. **Use BFS (Queue) for level traversal**
   - Push the root node into a queue.
   - Process nodes level by level.

3. **Track traversal direction**
   - Maintain a boolean `is_order_left`.
   - If `true`, store values normally.
   - If `false`, store values in reverse order.

4. **Process each level**
   - Record the current queue size (number of nodes in that level).
   - For each node:
     - Pop it from the queue.
     - If traversal is left-to-right → append value to vector.
     - Otherwise → push value to the **front of a deque**.

5. **Convert reversed order**
   - If the level was processed right-to-left, copy elements from the deque to the vector.

6. **Push the level result**
   - Add the vector to the final result.
   - Toggle the direction flag.

7. **Continue until queue becomes empty**

This ensures every level is processed once while alternating the direction of value storage.

## Complexity
- Time complexity:
  $$O(n)$$

  Each node in the tree is visited exactly once.

- Space complexity:
  $$O(n)$$

  In the worst case, the queue may store all nodes of the largest level of the tree.

## Code
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;
        queue<TreeNode*> nodeQ;
        bool is_order_left = true;
        nodeQ.push(root);
        while(!nodeQ.empty()) {
            int sizeQ = nodeQ.size();
            vector<int> v;
            deque<int> dq;
            for(int i=0; i<sizeQ; i++) {
                TreeNode* node = nodeQ.front();
                nodeQ.pop();
                if(is_order_left) {
                    v.push_back(node->val);
                } else {
                    dq.push_front(node->val);
                }
                if(node->left) nodeQ.push(node->left);
                if(node->right) nodeQ.push(node->right);
            }
            if(!is_order_left) {
                v.assign(dq.begin(), dq.end());
            }
            result.push_back(v);
            is_order_left = !is_order_left;
        }
        return result;
    }
};
```


# Clean BFS with Direct Index Placement (No Deque Needed)

## Intuition
The problem is a variation of normal **level order traversal (BFS)** of a binary tree.
The only difference is that the direction alternates at each level.

Instead of reversing a vector or using a deque, we can place elements directly in their correct positions while processing the level.

If the traversal direction is reversed, we simply calculate the correct index
for each element.

## Approach
1. If the tree is empty, return an empty result.

2. Use a **queue** to perform BFS traversal.

3. Maintain a boolean `leftToRight` to track traversal direction.

4. For each level:
   - Get the current queue size.
   - Create a vector of that size.
   - Process each node in the level.

5. Determine the index for insertion:
   - If `leftToRight` → `index = i`
   - Otherwise → `index = size - 1 - i`

6. Insert node values directly into the correct index.

7. Push children into the queue.

8. After finishing the level, toggle the direction.

## Complexity
- Time complexity:
  $$O(n)$$

  Each node is visited exactly once.

- Space complexity:
  $$O(n)$$

  The queue stores nodes of the largest level of the tree.

## Code
```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;

        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;

        while(!q.empty()) {
            int size = q.size();
            vector<int> level(size);

            for(int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                int index = leftToRight ? i : size - 1 - i;
                level[index] = node->val;

                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }

            result.push_back(level);
            leftToRight = !leftToRight;
        }

        return result;
    }
};
```
