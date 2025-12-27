#include <bits/stdc++.h>
using namespace std;

/*
 Sort strings by length using a lambda comparator
 Compile: g++ -std=c++17 sort_by_length.cpp -o sort_by_length
 Run: ./sort_by_length
*/
int main() {
    vector<string> v = {"apple", "kiwi", "banana", "fig", "strawberry", "pear"};
    cout << "Before:\n";
    for (auto &s: v) cout << s << " ";
    cout << "\n\nSort by length (ascending):\n";
    sort(v.begin(), v.end(), [](const string &a, const string &b){
        return a.size() < b.size();
    });
    for (auto &s: v) cout << s << " ";
    cout << "\n";
    return 0;
}
