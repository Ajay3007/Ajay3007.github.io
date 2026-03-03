---
permalink: /editorials/max-depth-binary-tree/
layout: editorial
title: "Max Depth Binary Tree Solution"
problem_id: "104"
date: 2026-03-03T09:24:48.323Z
---

# Maximum Depth of Binary Tree — Recursive DFS, Iterative DFS & BFS

**LeetCode #104** | **Difficulty:** Easy

# Intuition
The maximum depth of a binary tree is the number of nodes
along the longest path from the root to a leaf.

For any node:
    depth = 1 + max(depth of left subtree, depth of right subtree)

This naturally suggests a Depth First Search solution.
However, the problem can also be solved using:
- Recursive DFS
- Iterative DFS (using stack)
- Iterative BFS (level order traversal)

---

# Approach 1: Recursive DFS

1. **Base Case**
   - If the node is `nullptr`, its depth is 0.

2. **Recursive Case**
   - Recursively compute:
     - Depth of left subtree.
     - Depth of right subtree.
   - Return:
     
       1 + max(leftDepth, rightDepth)

3. The recursion naturally traverses the entire tree in a Depth-First manner,
   computing height bottom-up.

This is a classic example of postorder DFS where we compute results
from children before returning to the parent.

## Complexity
- Time complexity:
  O(n)

  Each node is visited exactly once.

- Space complexity:
  O(h)

  Where `h` is the height of the tree.
  In the worst case (skewed tree), this becomes O(n).
  In a balanced tree, it is O(log n).

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
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

---

# Approach 2: Iterative DFS (Using Stack)

Instead of recursion, we simulate DFS using a stack.

Store:
    pair<TreeNode*, depth>

Process nodes and keep track of maximum depth.

## Complexity
- Time complexity: O(n)
- Space complexity: O(h)

## Code
```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        stack<pair<TreeNode*, int>> nodeStack;
        int maxDepth = 0, depth;
        nodeStack.push({root, 1});
        while(!nodeStack.empty()) {
            TreeNode *node = nodeStack.top().first;
            depth = nodeStack.top().second;
            nodeStack.pop();
            maxDepth = max(maxDepth, depth);
            if(node->left) nodeStack.push({node->left, depth + 1});
            if(node->right) nodeStack.push({node->right, depth + 1});
        }
        return maxDepth;
    }
};
```

---

# Approach 3: Iterative BFS (Level Order Traversal)

We traverse the tree level by level.
Each level increases the depth by 1.

Use a queue:
- Push root.
- For each level:
    - Process all nodes at that level.
    - Increment depth.

## Complexity
- Time complexity: O(n)
- Space complexity: O(w)
  (w = maximum width of tree)

## Code
```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        queue<pair<TreeNode*, int>> nodeQ;
        int maxDepth = 0, depth;
        nodeQ.push({root, 1});
        while(!nodeQ.empty()) {
            TreeNode *node = nodeQ.front().first;
            depth = nodeQ.front().second;
            nodeQ.pop();
            maxDepth = max(maxDepth, depth);
            if(node->left) nodeQ.push({node->left, depth + 1});
            if(node->right) nodeQ.push({node->right, depth + 1});
        }
        return maxDepth;
    }
};
```

---

# Summary

| Approach        | Time | Space | Notes |
|---------------|------|-------|-------|
| Recursive DFS | O(n) | O(h)  | Clean & most common |
| Iterative DFS | O(n) | O(h)  | Avoids recursion |
| BFS           | O(n) | O(w)  | Natural level counting |

All three approaches are optimal in time complexity.
