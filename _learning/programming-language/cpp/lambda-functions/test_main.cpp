#include<bits/stdc++.h>
using namespace std;

int main() {
    /*
    Lambda function syntax in C++17:
        1. Declaration without call:
            [capture](parameters) mutable-exception -> return_type {
                body
            };
        2. Declaration with call:
            [capture](parameters) mutable-exception -> return_type {
                body
            }();
        3. Assigning to a variable:
            auto lambda_name = [capture](parameters) mutable-exception -> return_type {
                body
            };
        4. Calling the lambda function:
            lambda_name();
        
    */
    cout << "Hello, World!" << endl;

    []() {
        cout << "This is a lambda function declaration without call in C++17." << endl;
    };

    []() {
        cout << "This is a lambda function declaration & call in C++17." << endl;
    }();

    auto fun = []() {
        cout << "This is a lambda function in C++17." << endl;
    };
    fun(); // Calling the lambda function

    [](double a, double b) {
        cout << "Sum: " << (a + b) << endl;
    }(3.5, 2.5); // Lambda function with parameters

    auto square = [](int x) -> int {
        return x * x;
    }; // Lambda function with return type
    cout << "Square of 5: " << square(5) << endl;

    auto res = [](int x, int y) mutable -> int {
        x += 10; // Modifying captured variable
        return x + y;
    }(5, 15); // Lambda function with mutable capture and parameters
    cout << "Result: " << res << endl;

    auto result = [](int x, int y) -> int {
        if (y == 0) {
            throw runtime_error("Division by zero");
        }
        return x / y;
    };
    try {
        cout << "Division: " << result(10, 2) << endl;
        cout << "Division: " << result(10, 0) << endl; // This will throw an exception
    } catch (const exception &e) {
        cout << "Error: " << e.what() << endl;
    }

    cout << "result : " << [](int a, int b) -> int {
        return a * b;
    }(4, 5) << endl; // Lambda function with parameters and return type called directly

    auto print = [](const string &msg) {
        cout << msg << endl;
    }; // Lambda function with parameter

    print("This is a message from the lambda function.");
    print("Lambda functions are powerful!");
    
    cout << "End of lambda function examples." << endl;
    return 0;
}