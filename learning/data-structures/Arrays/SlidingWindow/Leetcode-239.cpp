#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        multiset<int> ms;
        vector<int> ans;
        int l = 0, r = k-1;
        for(int i=0; i<k; i++) {
            ms.insert(nums[i]);
        }
        while(r < n) {
            ans.push_back(*prev(ms.end()));
            auto it = ms.find(nums[l]);
            if (it != ms.end())
                ms.erase(it); 
            l++;
            r++;
            if (r < n) ms.insert(nums[r]);
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    vector<int> ans = sol.maxSlidingWindow(nums, k);
    for(int x : ans) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}