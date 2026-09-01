#include <bits/stdc++.h>
using namespace std;

bool matches(vector<int> &freqS1, vector<int> &freqS2)
{
    for (int i = 0; i < 26; i++)
    {
        if (freqS1[i] != freqS2[i])
            return false;
    }
    return true;
}

bool checkInclusion(string s1, string s2)
{
    int k = s1.length(), n = s2.length();
    if (k > n)
        return false;
    vector<int> freqS1(26, 0), freqS2(26, 0);
    for (int i = 0; i < k; i++)
    {
        freqS1[s1[i] - 'a']++;
        freqS2[s2[i] - 'a']++;
    }
    // slide the window through s2 and compare the freqMaps
    for (int i = 0; i < n - k; i++)
    {
        if (matches(freqS1, freqS2))
            return true;
        freqS2[s2[i + k] - 'a']++; // Add new char to the window
        freqS2[s2[i] - 'a']--;     // Remove old char from the window
    }
    // Check for the last window
    return matches(freqS1, freqS2);
}

int main()
{
    string s1, s2;
    cin >> s1 >> s2;
    if (checkInclusion(s1, s2))
        cout << "True\n";
    else
        cout << "False\n";
    return 0;
}