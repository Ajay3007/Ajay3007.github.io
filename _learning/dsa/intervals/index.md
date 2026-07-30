---
layout: learning
title: Intervals
permalink: /learning/dsa/intervals/
---

# 📏 Intervals

Interval problems involve ranges `[start, end]`. The key insight: **sort by start time**, then handle overlaps greedily. Most problems reduce to merge, insert, or count operations.

---

## Core Patterns

| Pattern | Approach | Example |
|---------|----------|---------|
| **Merge overlapping** | Sort by start, merge when `curr.start ≤ prev.end` | Merge Intervals |
| **Insert & merge** | Find position, expand new interval to cover overlaps | Insert Interval |
| **Count non-overlapping** | Sort by end, greedily keep non-overlapping | Activity selection |
| **Interval intersection** | Two-pointer on sorted lists, advance smaller end | Interval List Intersections |
| **Min interval for queries** | Sort both, use min-heap keyed by interval size | Query coverage |

## Templates

```cpp
// Merge Intervals — sort by start, then merge
sort(intervals.begin(), intervals.end());
vector<vector<int>> res;
for (auto& iv : intervals) {
    if (res.empty() || iv[0] > res.back()[1])
        res.push_back(iv);
    else
        res.back()[1] = max(res.back()[1], iv[1]);
}

// Insert Interval — three-phase scan
vector<vector<int>> res;
int i = 0, n = intervals.size();
// Phase 1: intervals entirely before newInterval
while (i < n && intervals[i][1] < newInterval[0])
    res.push_back(intervals[i++]);
// Phase 2: merge overlapping
while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = min(newInterval[0], intervals[i][0]);
    newInterval[1] = max(newInterval[1], intervals[i][1]);
    i++;
}
res.push_back(newInterval);
// Phase 3: intervals entirely after
while (i < n) res.push_back(intervals[i++]);
```

## Overlap Condition

Two intervals `[a, b]` and `[c, d]` overlap iff `a ≤ d && c ≤ b`.
They do **not** overlap iff `b < c` (first ends before second starts) or `d < a`.

## Complexity

| Pattern | Time | Space |
|---------|------|-------|
| Merge / Insert | O(n log n) | O(n) |
| Intersection (two sorted lists) | O(m + n) | O(m + n) |

---

<div class="topic-crosslinks">
  <a href="{{ '/learning/dsa/intervals/intervals-problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">📋 Practice Problems →</a>
  <a href="{{ '/learning/dsa/' | relative_url }}" class="topic-hub-link">← DSA Hub</a>
  <a href="{{ '/roadmap/#ch8' | relative_url }}" class="topic-hub-link">📍 Roadmap Ch 8</a>
</div>
