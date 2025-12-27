#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int left = 0, right = 0;
        vector<int> freq(26, 0);
        int maxFreq = 0; // To keep track of the maximum frequency of a single character in the current window
        int maxLength = 0;

        while (right < n) {
            freq[s[right] - 'A']++;
            maxFreq = max(maxFreq, freq[s[right] - 'A']);

            // Current window size is right - left + 1
            // If we need more than k replacements, shrink the window from the left
            while ((right - left + 1) - maxFreq > k) {
                freq[s[left] - 'A']--;
                left++;
                // Recalculate maxFreq after shrinking the window
                maxFreq = *max_element(freq.begin(), freq.end());
            }

            // Update maxLength if the current window is valid
            maxLength = max(maxLength, right - left + 1);
            right++;
        }

        return maxLength;
    }
};

int main() {
    Solution sol;
    string s;
    int k;
    cin >> s >> k;
    cout << sol.characterReplacement(s, k) << "\n";
    return 0;
}   