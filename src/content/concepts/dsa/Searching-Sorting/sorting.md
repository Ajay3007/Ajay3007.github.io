---
title: "Sorting"
description: "Sorting Master Guide (Interview-Focused) Sorting Algorithms You MUST Know (Interview Level) [Sorting an Array using Recursion](/learning/dsa/recursion/sort array using rec.cpp)…"
domain: dsa
order: 99
url: /learning/dsa/searching-sorting/sorting/
---

# <img src="/assets/icons/rocket.svg" class="inline-icon" alt=""> Sorting Master Guide (Interview-Focused)

## Sorting Algorithms You MUST Know (Interview Level)

### [Sorting an Array using Recursion](/learning/dsa/recursion/sort_array_using_rec.cpp)

---

### 🔶 1. Selection Sort (Basic)

#### 🔹 Intuition

Selection Sort works on a very simple idea:
```
Repeatedly select the minimum element from the unsorted part and place it at the correct position in the sorted part.
```

Think of it like:

- You scan the entire array

- Pick the smallest element

- Put it at the beginning

- Shrink the unsorted region

- Repeat

**🔹 C++ Implementation**

```cpp
void selectionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}
```

1. Complexity:

    - Time: O(N²)

    - Space: O(1)

2. Not Stable
    - Relative order not preserve.
    - Can  be made stable by shifting elements instead of swapping, but it increases cost.

3. Not Adaptive
    - Doesn't take advantage of existing order of input.

4. Not used in interviews except conceptual warmup

#### [For more on Stable and Adaptive sorting CLICK HERE](/learning/dsa/searching-sorting/stable-adaptive-sort.pdf){:target="_blank" rel="noopener noreferrer"}

---

### 🔶 2. Bubble Sort

#### 🔹 Intuition

```
Keep swapping adjacent elements if they are in the wrong order until the largest element bubbles to the end.
```

Largest elements bubble up to the right in each pass.

1. Complexity

    - Time: O(N²)

    - Space: O(1)

2. Space: O(1)

3. Stable: ✅ Yes

4. Adaptive: ✅ Yes (with optimization)

5. Again, basic; rarely asked.

#### 🔹 Optimized Bubble Sort (IMPORTANT)

If no swaps occur in a pass, array is already sorted → stop early.

#### [👉 Bubble Sort Code](/learning/dsa/searching-sorting/bubble_sort.cpp)

---

### 🔶 3. Insertion Sort

#### 🔹 Intuition

```
Take the next element and insert it into its correct position in the already sorted part.
```

Exactly how you sort playing cards in hand.

#### 🔹 Algorithm Steps

- Assume first element is sorted

- Pick next element (key)

- Shift larger elements one step right

- Insert key at correct position

- Repeat

#### [👉 Insertion Sort Code](/learning/dsa/searching-sorting/insertion_sort.cpp)

1. Complexity
    - Time: O(N²)
    - Space: O(1)
    - Best case O(N) when array is nearly sorted

2. Internally used in:
    - TimSort
    - Hybrid sorts in C++ STL

3. Stable: ✅ Yes

4. Adaptive: ✅ Yes

5. 👉 Conceptually important.

6. Used inside:

    - C++ STL sort()

    - Java / Python TimSort

**Insertion sort is preferred over bubble sort** because it performs **fewer swaps** and is significantly faster on nearly sorted data.

---

### 🔥 Which Sorting Algorithm Is Used in C++ STL sort()?

C++ STL sort() uses **Introsort**, a hybrid algorithm combining **Quick Sort, Heap Sort, and Insertion Sort**.

#### <img src="/assets/icons/brain.svg" class="inline-icon" alt=""> What Is Introsort? (Deep but Clear)

**Introsort** (Introspective Sort) starts like **Quick Sort**, but:

- Monitors recursion depth

- If recursion goes too deep (risk of O(n²)),
→ switches to Heap Sort

- For small subarrays, it uses **Insertion Sort**

**Why?**

To guarantee:

- Average case: O(n log n)

- Worst case: O(n log n) (Quick Sort alone can degrade)

- High practical performance

#### <img src="/assets/icons/puzzle.svg" class="inline-icon" alt=""> STL sort() Strategy (Step-by-Step)

1. Start with Quick Sort

    - Very fast due to cache locality

2. If recursion depth > 2 × log₂(n)

    - Switch to Heap Sort

3. If subarray size ≤ 16 (or small constant)

    - Use Insertion Sort

#### 📌 If you need stability, use:

```cpp
stable_sort()
```

which uses **Merge Sort**.

#### 🧪 Interview Trap Question

Q: Is `std::sort()` stable?
❌ No

Q: Why not use merge sort always?
✅ Extra memory + slower in practice due to cache misses.

---

### 🔶 4. Merge Sort (VERY IMPORTANT)

#### 🔹 Intuition (Say This in Interviews)

- **Merge Sort uses Divide & Conquer:**
- Divide the array into halves until single elements remain, then merge them back in sorted order.

#### 🔹 High-Level Steps

- Divide array into two halves

- Recursively sort both halves

- Merge two sorted halves

#### [👉 Merge Sort Code](/learning/dsa/searching-sorting/merge_sort.cpp)


1. Used in:

    - `stable_sort()` in C++

    - Sorting linked lists

    - Counting inversions

1. ⏱ Time Complexity

    - Best: O(n log n)

    - Average: O(n log n)

    - Worst: O(n log n)

    - Depth of recursion tree: `log n`

    - Work at each level: `n`

3.  <img src="/assets/icons/brain.svg" class="inline-icon" alt=""> Space Complexity

    - Extra array: O(n)

    - Recursion stack: O(log n)

    - 👉 Overall: O(n)

4. Stability, In-Place, Adaptive

| Property | Merge Sort |
| -------- | ---------- |
| Stable   | ✅ Yes      |
| In-place | ❌ No       |
| Adaptive | ❌ No       |


#### 📌 You MUST know:

- How merge works

- Recursion tree

- Space complexity reasoning

#### 📌 Interview problems that use Merge Sort technique:

- Count inversions in array

- Sort linked list

- Merge k sorted lists

- Count smaller elements after self

**🔹 Why Merge Sort Is Preferred for Linked Lists**

👉 Arrays need extra space for merging
👉 Linked lists can merge by changing pointers

- ✔ No extra array
- ✔ Truly O(1) extra space
- ✔ Still stable

#### 🔹 Interview Problems Based on Merge Sort
**🔥 MUST-DO**

1. Merge two sorted arrays

2. Merge sorted linked lists

3. Count inversions in array

4. Sort linked list

5. Count smaller elements after self

**🔥 HARD (Advanced)**

1. Reverse pairs

2. Range sum count

3. Skyline problem

---

### 🔶 5. Quick Sort (VERY IMPORTANT)

The most commonly asked theoretical sorting algorithm.

- Average: O(N log N)

- Worst case: O(N²)

- In-place

- Not stable

📌 You must know:

- Partitioning (Lomuto/Hoare)

- Recursion depth

- Randomized quick sort (expected O(N log N))

- Why it's used in practice (cache-friendly)

---

### 🔶 6. Heap Sort

- Time: O(N log N)

- Space: O(1)

- Not stable

Used indirectly in:

- Top-K problems

- Priority queue interview questions

---

### 🔶 7. Counting Sort

- Time: O(N + K)

- Space: O(K)

- Only for small, bounded integer ranges

Used in:

- Sorting colors (Dutch National Flag)

- Bucket-based questions

---

### 🔶 8. Bucket Sort

- Used when input is uniformly distributed.

Used in:

- Maximum gap problem

- Sorting decimals/floats

- LeetCode "Min Time to Make Rope Colorful" type problems indirectly

---

### 🔶 9. Radix Sort

- Time: O(d * (N + K))

- Works for integers and strings (ASCII-wide)

Used in:

- Phone number sorting

- Large dataset / distributed systems

---

## Sorting in C++ (VERY IMPORTANT for interviews)

### C++ STL sorts you must know

1. `sort()` → IntroSort (Quick + Heap + Insertion)
Time: O(N log N)

2. `stable_sort()` → Merge Sort

3. `partial_sort()`

4. `nth_element()` → QuickSelect (VERY IMPORTANT)

### ❗ Interviewers often ask:

- How does `sort()` work internally?

- Is C++ `sort` stable? (Answer: No)

- Why use `stable_sort()`?

- How to sort using custom comparator?

---

## Coding Templates You Must Know

### 🔹 Merge Sort (Template)

```cpp
void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;

    int mid = l + (r - l) / 2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);

    merge(arr, l, mid, r);
}
```

### 🔹 Quick Sort (Lomuto Partition)

```cpp
int partition(vector<int>& a, int l, int r) {
    int pivot = a[r];
    int i = l;
    for (int j = l; j < r; j++) {
        if (a[j] < pivot) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[r]);
    return i;
}
```

---

# MUST DO PROBLEMS

### Level 1 (Basic)

1. [Leetcode 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/merge-sorted-array/solutions/7417731/merge-sorted-array-in-place-backward-two-j35p/){:target="_blank" rel="noopener noreferrer"}**



Meeting rooms II

### Level 2 (Medium)

1. [Leetcode 148. Sort List](https://leetcode.com/problems/sort-list/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/sort-list/solutions/7428100/merge-sort-on-linked-list-on-log-n-time-v8lx2/){:target="_blank" rel="noopener noreferrer"}**


2. [Leetcode 179. Largest Number](https://leetcode.com/problems/largest-number/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/largest-number/solutions/7429080/largest-number-custom-sorting-by-concate-z4et/){:target="_blank" rel="noopener noreferrer"}**


3. [Leetcode 75. Sort Colors](https://leetcode.com/problems/sort-colors/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link - Dutch National Flag Algorithm](https://leetcode.com/problems/sort-colors/solutions/7418299/sort-colors-dutch-national-flag-algorith-e7eo/){:target="_blank" rel="noopener noreferrer"}**



K closest points

Minimum arrows to burst balloons

Group anagrams

Reduce array size to half (bucket sort)

### Level 3 (Hard)


Count inversions

Maximum gap

Merge k sorted lists

Count smaller elements after self

Skyline problem



