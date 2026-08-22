---
title: "Greedy Algorithms"
description: "🌿 Greedy Algorithms Greedy algorithms make the locally optimal choice at each step, hoping it leads to a globally optimal solution."
domain: dsa
order: 0
ownHeader: true
url: /learning/dsa/greedy/
---

# 🌿 Greedy Algorithms

Greedy algorithms make the **locally optimal choice** at each step, hoping it leads to a globally optimal solution. They work when the problem has **greedy choice property** and **optimal substructure**.

---

## Core Patterns

| Pattern | Approach | Example |
|---------|----------|------------|
| **Sort first** | Sort by key, then greedily pick | Interval scheduling, fractional knapsack |
| **Interval scheduling** | Sort by end time, greedily pick non-overlapping | Activity selection, meeting rooms |
| **Two-pass greedy** | Forward pass + backward pass | Candy distribution, temperature ratings |
| **Jump/reach tracking** | Track max reachable index | Jump Game |
| **Local → Global** | Prove local optimum = global optimum | Gas station circuit |

## Templates

```cpp
// Interval scheduling — non-overlapping intervals (sort by end time)
sort(intervals.begin(), intervals.end(),
     [](auto& a, auto& b){ return a[1] < b[1]; });
int count = 0, end = INT_MIN;
for (auto& iv : intervals) {
    if (iv[0] >= end) { count++; end = iv[1]; }
}

// Jump Game — max reachable index
int maxReach = 0;
for (int i = 0; i <= maxReach && i < n; i++)
    maxReach = max(maxReach, i + nums[i]);
return maxReach >= n - 1;

// Two-pass greedy (Candy)
vector<int> candy(n, 1);
for (int i = 1; i < n; i++)         // left to right
    if (ratings[i] > ratings[i-1]) candy[i] = candy[i-1] + 1;
for (int i = n-2; i >= 0; i--)      // right to left
    if (ratings[i] > ratings[i+1]) candy[i] = max(candy[i], candy[i+1] + 1);
```

## Complexity

| Pattern | Time | Space |
|---------|------|-------|
| Sort-based greedy | O(n log n) | O(1) |
| Linear scan greedy | O(n) | O(1) |
| Two-pass greedy | O(n) | O(n) |

---

<div class="topic-crosslinks">
  <a href="/learning/dsa/greedy/greedy-problems/" class="topic-hub-link topic-hub-link--primary">📋 Practice Problems →</a>
  <a href="/learning/dsa/" class="topic-hub-link">← DSA Hub</a>
  <a href="/roadmap/#ch7" class="topic-hub-link">📍 Roadmap Ch 7</a>
</div>
