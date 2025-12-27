# Problem Link 

- **[Allocate Minimum Pages - GFG](https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1)**
- **[Allocate Books - InterviewBit](https://www.interviewbit.com/problems/allocate-books/)**


# Intuition
We want to distribute books among `k` students such that:
1. Every student gets a **contiguous block** of books.
2. We minimize the **maximum number of pages** assigned to any student.

If we fix a value `X` as the *maximum pages a student is allowed to read*, we can greedily check whether this `X` is feasible.  

Since increasing `X` makes the allocation easier and decreasing `X` makes it harder, the answer lies in a **monotonic search space**.  
This naturally suggests using **Binary Search on the answer**.

---

# Approach
1. Let `low` be the maximum pages of a single book (no student can take fewer than this).  
   Let `high` be the sum of all book pages (one student takes all books).
2. Apply **Binary Search** on range `[low, high]`:
   - `mid` = the assumed maximum pages a student is allowed.
   - Check whether allocation is possible with `mid` using the helper `isValid()`:
     - Greedily assign books to students.
     - When the current student exceeds `mid`, assign the next student.
     - If we require more than `k` students, the allocation is invalid.
3. If `mid` is valid, store it as a potential answer and try a smaller value (move left).  
   If invalid, we must increase `mid` (move right).
4. Continue until `low > high`.  
   The stored value is the **minimum possible maximum pages**.

---

# Complexity
- **Time complexity:**  
  $$O(n \cdot \log(\text{sum of pages}))$$  
  Where `n` is the number of books.  
  Each binary search step takes `O(n)` for validation.

- **Space complexity:**  
  $$O(1)$$  
  Only a few variables are used.

---

# Code
```cpp
class Solution {
  public:
    bool isValid(vector<int> &arr, int k, int curMax) {
        int n = arr.size();
        int student = 1;
        int currPage = 0;
        for(int i=0; i<n; i++) {
            currPage += arr[i];
            if(currPage > curMax) {
                student++;
                currPage = arr[i];
            }
            if(student > k) return false;
        }
        return true;
    }
    
    int findPages(vector<int> &arr, int k) {
        int n = arr.size();
        if(k > n) return -1;
        int low = 0, high = 0, mid;
        for(int i = 0; i < n; i++) {
            low = max(low, arr[i]);
            high += arr[i];
        }
        int maxPages = -1;
        while(low <= high) {
            mid = low + (high - low)/2;
            if(isValid(arr, k, mid)) {
                maxPages = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return maxPages;
    }
};
```