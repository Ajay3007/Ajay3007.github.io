#include <bits/stdc++.h>
using namespace std;

class A
{
public:
    A()
    {
        cout << "A Constructor\n";
    }
    ~A()
    {
        cout << "A Destructor\n";
    }
    void display()
    {
        cout << "Display from A\n";
    }
};

int main()
{
    cout << "This is a placeholder test file for unique_ptr functionality.\n";
    {
        cout << "Demonstrating manual memory management (not recommended):\n";
        A *a = new A(); // Manual allocation; should be managed by unique_ptr in real usage
        a->display(); // Using the object
        cout << a << "\n"; // Displaying the address
        cout << "Manually deleting the object to avoid memory leak.\n";
        delete a; // Manual deletion; destructor called here
    }
    cout << "\nDemonstrating unique_ptr usage:\n";
    unique_ptr<A> ptr = make_unique<A>(); // Using unique_ptr for automatic memory management
    ptr->display();
    cout << ptr.get() << "\n"; // Displaying the address managed by unique_ptr

    //unique_ptr<A> ptr2 = ptr; // This line would cause a compile-time error due to unique_ptr's non-copyable nature
    cout << "Attempting to copy unique_ptr will result in a compile-time error as expected.\n";

    unique_ptr<A> ptr3 = std::move(ptr); // Transferring ownership using move semantics
    if (!ptr)
    {
        cout << "ptr is now nullptr after move.\n";
    }
    ptr3->display();
    cout << ptr3.get() << "\n"; // Displaying the address managed by ptr3
    cout << "Unique_ptr going out of scope, destructor will be called automatically.\n";
    cout << "Exiting main, unique_ptr will automatically clean up.\n";
    cout << "Please refer to smart_pointers/image_unique_ptr.cpp for actual unique_ptr usage example.\n";
    return 0;
}