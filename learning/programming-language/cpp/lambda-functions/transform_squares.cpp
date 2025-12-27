#include <bits/stdc++.h>
using namespace std;

/*
 Use std::transform with a generic lambda to compute squares
 Compile: g++ -std=c++17 transform_squares.cpp -o transform_squares
 Run: ./transform_squares
*/
int main() {
    vector<int> v = {1,2,3,4,5};
    vector<int> out;
    out.resize(v.size());
    // generic lambda (C++14+) though we compile with C++17
    std::transform(v.begin(), v.end(), out.begin(), [](auto x){ return x * x; });
    cout << "Original: ";
    for (auto x: v) cout << x << " ";
    cout << "\nSquares:  ";
    for (auto x: out) cout << x << " ";
    cout << "\n";
    return 0;
}
