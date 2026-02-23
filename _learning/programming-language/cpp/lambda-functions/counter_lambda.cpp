#include <bits/stdc++.h>
using namespace std;

/*
 Function that returns a lambda which captures a counter and increments it on each call.
 Compile: g++ -std=c++17 counter_lambda.cpp -o counter_lambda
 Run: ./counter_lambda
*/
function<int()> make_counter(int start = 0) {
    // capture by value the starting value, then mutable so the copy can change
    return [count = start]() mutable {
        return ++count;
    };
}

int main() {
    auto c1 = make_counter(5);
    cout << "c1: " << c1() << "\\n"; // 6
    cout << "c1: " << c1() << "\\n"; // 7

    auto c2 = make_counter();
    cout << "c2: " << c2() << "\\n"; // 1
    cout << "c2: " << c2() << "\\n"; // 2

    return 0;
}
