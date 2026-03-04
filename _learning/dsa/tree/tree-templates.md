# 🔥 Binary Tree Templates (Reusable for 20+ Problems)

These templates cover:
- Height / Depth
- Diameter
- Balanced Tree
- Path Sum
- Maximum Path Sum
- Level Order
- Zigzag
- Right View
- LCA
- BST validation
- and many more

---

# 1️⃣ Generic Recursive DFS Template (Postorder)

Use this when answer depends on children.

```cpp
int dfs(TreeNode* root) {
    if(!root) return BASE_VALUE;

    int left = dfs(root->left);
    int right = dfs(root->right);

    // Process current node
    return combine(left, right, root);
}
```

### Use for:
- Maximum Depth
- Diameter
- Balanced Binary Tree
- Maximum Path Sum
- Subtree problems

---

# 2️⃣ Height Template (Depth Problems)

```cpp
int height(TreeNode* root) {
    if(!root) return 0;
    return 1 + max(height(root->left), height(root->right));
}
```

### Used in:
- Max Depth
- Min Depth (slight modification)
- Diameter
- Balanced Tree

---

# 3️⃣ Diameter Template (Very Important)

```cpp
int diameter = 0;

int dfs(TreeNode* root) {
    if(!root) return 0;

    int left = dfs(root->left);
    int right = dfs(root->right);

    diameter = max(diameter, left + right);

    return 1 + max(left, right);
}
```

Pattern:
- Return height
- Update global answer

---

# 4️⃣ Balanced Binary Tree Template

```cpp
int dfs(TreeNode* root) {
    if(!root) return 0;

    int left = dfs(root->left);
    if(left == -1) return -1;

    int right = dfs(root->right);
    if(right == -1) return -1;

    if(abs(left - right) > 1) return -1;

    return 1 + max(left, right);
}
```

Pattern:
- Use special return value (-1) to propagate failure.

---

# 5️⃣ Path Sum Template (Root to Leaf)

```cpp
bool dfs(TreeNode* root, int target) {
    if(!root) return false;

    if(!root->left && !root->right)
        return target == root->val;

    return dfs(root->left, target - root->val) ||
           dfs(root->right, target - root->val);
}
```

Pattern:
- Reduce target as you go down.

---

# 6️⃣ Maximum Path Sum Template

```cpp
int maxSum = INT_MIN;

int dfs(TreeNode* root) {
    if(!root) return 0;

    int left = max(0, dfs(root->left));
    int right = max(0, dfs(root->right));

    maxSum = max(maxSum, left + right + root->val);

    return root->val + max(left, right);
}
```

Pattern:
- Ignore negative paths
- Update global result

---

# 7️⃣ Level Order (BFS Template)

```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if(!root) return result;

    queue<TreeNode*> q;
    q.push(root);

    while(!q.empty()) {
        int size = q.size();
        vector<int> level;

        for(int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();

            level.push_back(node->val);

            if(node->left) q.push(node->left);
            if(node->right) q.push(node->right);
        }

        result.push_back(level);
    }

    return result;
}
```

Used for:
- Level Order
- Zigzag (reverse alternate levels)
- Right Side View
- Average of Levels

---

# 8️⃣ Lowest Common Ancestor (LCA)

```cpp
TreeNode* lca(TreeNode* root, TreeNode* p, TreeNode* q) {
    if(!root || root == p || root == q)
        return root;

    TreeNode* left = lca(root->left, p, q);
    TreeNode* right = lca(root->right, p, q);

    if(left && right) return root;
    return left ? left : right;
}
```

Pattern:
- If both sides return non-null → current is LCA

---

# 9️⃣ Validate BST Template

```cpp
bool validate(TreeNode* root, long minVal, long maxVal) {
    if(!root) return true;

    if(root->val <= minVal || root->val >= maxVal)
        return false;

    return validate(root->left, minVal, root->val) &&
           validate(root->right, root->val, maxVal);
}
```

Call with:

```cpp
validate(root, LONG_MIN, LONG_MAX);
```

---

# 🧠 MASTER PATTERN SUMMARY

Most Tree Problems Follow One of These:

1. Return height + update global variable
2. Return boolean and propagate failure
3. Return sum and track max
4. BFS level counting
5. LCA two-branch logic
6. BST range validation

---

# 🚀 If You Master These 9 Templates

You can solve:
- 104. Max Depth
- 110. Balanced Tree
- 543. Diameter
- 124. Max Path Sum
- 112/113 Path Sum
- 199 Right Side View
- 102 Level Order
- 98 Validate BST
- 236 LCA
- and many more

Tree problems become pattern matching instead of thinking from scratch.
