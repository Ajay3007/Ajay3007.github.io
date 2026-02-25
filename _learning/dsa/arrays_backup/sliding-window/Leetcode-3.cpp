#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        vector<int> freq(256, -1);  // -1 denote the char is not present
        int l = 0, r = 0, ans = 0, len;
        while(r < n) {
            int idx = s[r] - ' ';
            len = r - l + 1;
            if(freq[idx] != -1) {  // A repeating char found
                // remove all chars from l to previous index of repeating char
                while(l <= freq[idx]) { 
                    freq[s[l]-' '] = -1;
                    l++;
                }
            } else 
                ans = max(ans, len);
            freq[idx] = r;  // update the current index of char
            r++;
        }
        return ans;
    }
};

int main(){
    Solution sol;
    string s = "abcabcbb";
    cout << "Length of Longest Substring Without Repeating Characters: " << sol.lengthOfLongestSubstring(s) << endl;
    return 0;
}