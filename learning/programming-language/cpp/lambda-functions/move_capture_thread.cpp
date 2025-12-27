#include <bits/stdc++.h>
using namespace std;

/*
 Capture a std::unique_ptr into a lambda and use it inside a thread safely (move-capture)
 Compile: g++ -std=c++17 move_capture_thread.cpp -pthread -o move_capture_thread
 Run: ./move_capture_thread
*/
int main() {
    auto ptr = make_unique<int>(42);
    // move the unique_ptr into the lambda using init-capture (C++14+)
    auto worker = [p = std::move(ptr)]() {
        // p is owned by the lambda now
        cout << "Inside thread: value = " << *p << "\n";
    };

    // ptr is now null (moved)
    if (!ptr) cout << "ptr moved to lambda\n";

    thread t(std::move(worker));
    t.join();

    return 0;
}
