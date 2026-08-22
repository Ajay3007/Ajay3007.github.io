---
permalink: /editorials/binary-tree-level-order-traversal/
layout: editorial
title: "Binary Tree Level Order Traversal Solution"
problem_id: "102"
date: 2026-03-04T10:24:48.323Z
---

# Clean BFS using Queue Size (Level-by-Level Traversal)

**LeetCode #102** | **Difficulty:** Easy  

# Intuition
Level order traversal means visiting nodes level by level from top to bottom.

Breadth First Search (BFS) is naturally suited for this because a queue processes nodes
in the same order they appear in each level.

Instead of storing depth explicitly, we observe that at any moment the queue contains
all nodes of the current level. So by storing the **current queue size**, we know exactly
how many nodes belong to that level.

We process those nodes, store their values, and push their children for the next level.

# Approach
1. If `root` is `nullptr`, return an empty result.
2. Initialize a queue and push the root node.
3. While the queue is not empty:
   - Determine the number of nodes in the current level using `queue.size()`.
   - Create a temporary vector to store values for that level.
4. Process all nodes of the current level:
   - Pop a node from the queue.
   - Add its value to the level vector.
   - Push its left and right children (if they exist) into the queue.
5. After processing the level, add the level vector to the result.
6. Continue until the queue becomes empty.

# Complexity
- Time complexity:
  $$O(n)$$

  Every node is visited exactly once.

- Space complexity:
  $$O(n)$$

  In the worst case, the queue can store all nodes at the largest level of the tree.

# Code
```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;
        queue<TreeNode*> nodeQ;
        nodeQ.push(root);
        while(!nodeQ.empty()) {
            int levelSize = nodeQ.size();
            vector<int> levelNodes;
            for(int i=0; i<levelSize; i++) {
                TreeNode* node = nodeQ.front();
                nodeQ.pop();
                levelNodes.push_back(node->val);
                if(node->left) nodeQ.push(node->left);
                if(node->right) nodeQ.push(node->right);
            }
            result.push_back(levelNodes);
        }
        return result;
    }
};
```

# DFS with Level Tracking (Recursive Level Order Traversal)

## Intuition
Level order traversal is typically solved using Breadth First Search (BFS) with a queue.  
However, we can also achieve the same result using Depth First Search (DFS) if we keep track of the current depth (level) of each node.

While traversing the tree recursively, each node knows which level it belongs to.  
If we maintain a result vector where each index represents a level, we can directly append the node value to its corresponding level.

Whenever we visit a level for the first time, we create a new vector for that level.

## Approach
1. Create a recursive function `order(node, level, result)`.

2. When visiting a node:
   - If `result.size() == level`, it means this level is being visited for the first time.
   - Create a new vector for this level and push it into `result`.

3. Add the current node's value to `result[level]`.

4. Recursively traverse:
   - Left child with `level + 1`
   - Right child with `level + 1`

5. Start recursion from the root with level `0`.

This effectively groups nodes according to their depth and produces the same output as a standard level order traversal.

## Complexity
- Time complexity:
  O(n)

  Each node is visited exactly once.

- Space complexity:
  O(n)

  - Result vector stores all nodes.
  - Recursive call stack may grow up to the tree height `h`.
  - Worst case (skewed tree): `O(n)`

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
    void order(TreeNode* node, int level, vector<vector<int>>& result) {
        if(result.size() == level) {
            vector<int> v;
            result.push_back(v);
        }
        result[level].push_back(node->val);
        if(node->left) order(node->left, level+1, result);
        if(node->right) order(node->right, level+1, result);
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;
        order(root, 0, result);
        return result;
    }
};
```
