#include<bits/stdc++.h>
using namespace std;

int main() {
    double a{10.5}, b{20.3};
    // Capture by value
    auto sum = [a,b]() {
        return a + b;
    };
    cout << "Sum: " << sum() << "\n";

    /*
    Capture by value example with modification outside the lambda
    */
    cout << "Capture by value example:\n";
    int c{10};
    
    auto func = [c]() {
        cout << "Value of c inside lambda: " << c << "\n";
    };

    for(int i = 0; i < 5; ++i) {
        cout << "Outside loop iteration " << c << "\n";
        func();
        ++c;  // Modifying c outside the lambda
    }

    /*
    Capture by reference example
    */
    cout << "\nCapture by reference example:\n";
    int d{20};
    auto func_ref = [&d]() {
        cout << "Value of d inside lambda: " << d << "\n";
    };
    for(int i = 0; i < 5; ++i) {
        cout << "Outside loop iteration " << d << "\n";
        func_ref();
        ++d;  // Modifying d outside the lambda
    }

    /*
    Capture all by value
    */
    cout << "\nCapture all by value example:\n";
    int x{5}, y{15};
    auto func_all_val = [=]() {
        cout << "Inside lambda: x = " << x << ", y = " << y << "\n";
    };
    for(int i = 0; i < 3; ++i) {
        cout << "Outside loop iteration: x = " << x << ", y = " << y << "\n";
        func_all_val();
        ++x; ++y;
    }

    /*
    Capture all by reference
    */
    cout << "\nCapture all by reference example:\n";
    int p{30}, q{40};
    auto func_all_ref = [&]() {
        cout << "Inside lambda: p = " << p << ", q = " << q << "\n";
    };  
    for(int i = 0; i < 3; ++i) {
        cout << "Outside loop iteration: p = " << p << ", q = " << q << "\n";
        func_all_ref();
        ++p; ++q;
    }
    return 0;
}
