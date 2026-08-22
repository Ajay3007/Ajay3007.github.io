---
title: "Hashing"
description: "️⃣ Hashing (Hashmaps & Sets) Hash maps offer O(1) average insert, lookup, and delete."
domain: dsa
order: 0
url: /learning/dsa/hashing/
---

# #️⃣ Hashing (Hashmaps & Sets)

Hash maps offer **O(1) average** insert, lookup, and delete. Sets track existence; maps track frequency or mapping.

---

## Core Patterns

| Pattern | Tool | Example |
|---------|------|---------|
| **Existence check** | `unordered_set` | Duplicates, anagram detection |
| **Frequency count** | `unordered_map<T,int>` | Count chars, top-k elements |
| **Two-sum lookup** | `unordered_map<T,int>` | Find pair that sums to target |
| **Grouping** | `unordered_map<key, vector>` | Group anagrams by sorted key |
| **Prefix sum + map** | `unordered_map<int,int>` | Count subarrays with target sum |

## Templates

```cpp
// Frequency count
unordered_map<int, int> freq;
for (int x : arr) freq[x]++;

// Two-sum lookup
unordered_map<int, int> seen; // value → index
for (int i = 0; i < nums.size(); i++) {
    if (seen.count(target - nums[i]))
        return {seen[target - nums[i]], i};
    seen[nums[i]] = i;
}

// Group anagrams
unordered_map<string, vector<string>> groups;
for (string& s : strs) {
    string key = s; sort(key.begin(), key.end());
    groups[key].push_back(s);
}
```

## Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert / Lookup / Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

---

<div class="topic-crosslinks">
  <a href="/learning/dsa/hashing/hashing-problems/" class="topic-hub-link topic-hub-link--primary">📋 Practice Problems →</a>
  <a href="/learning/dsa/" class="topic-hub-link">← DSA Hub</a>
  <a href="/roadmap/#ch2" class="topic-hub-link">📍 Roadmap Ch 2</a>
</div>
