#include <iostream>
#include <memory>
#include <string>
#include <cstring>
using namespace std;

class ModernBuffer {
private:
    unique_ptr<char[]> data;   // smart pointer manages memory automatically
    size_t size;

public:
    ModernBuffer(const char* str)
        : size(strlen(str)),
          data(make_unique<char[]>(strlen(str) + 1))
    {
        strcpy(data.get(), str);
        cout << "[ModernBuffer] ctor: allocated " << static_cast<void*>(data.get())
             << " -> \"" << data.get() << "\"\n";
    }

    // No destructor
    // No copy constructor
    // No copy assignment
    // No move constructor
    // No move assignment
    // The compiler generates correct ones automatically (Rule of 0)

    void print() const {
        cout << "Buffer: \"" << data.get() << "\" at " << static_cast<const void*>(data.get()) << "\n";
    }
};

int main() {
    ModernBuffer b1("Hello Modern C++");
    b1.print();

    cout << "\nNow let's demonstrate move semantics automatically:\n";
    ModernBuffer b2 = std::move(b1);  // uses compiler-generated move constructor

    cout << "After move:\n";
    cout << "b1 (moved-from):\n";
    b1.print();   // data.get() is nullptr after move

    cout << "b2 (moved-to):\n";
    b2.print();

    return 0;
}
