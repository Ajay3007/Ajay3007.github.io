#include<bits/stdc++.h>
using namespace std;

class Resource
{
public:
    Resource() { cout << "Resource acquired\n"; }
    ~Resource() { cout << "Resource released\n"; }
    void greet() { cout << "Hello from Resource\n"; }
};

class Manager
{
private:
    shared_ptr<Resource> resourcePtr;
public:
    Manager(shared_ptr<Resource> res) : resourcePtr(res) {}
    void useResource()
    {
        resourcePtr->greet();
    }
};

int main()
{
    {
        auto resPtr = make_shared<Resource>();
        {
            cout << "Reference count after creation: " << resPtr.use_count() << "\n";
            Manager mgr1(resPtr);
            mgr1.useResource();
            cout << "Reference count after passing to mgr1: " << resPtr.use_count() << "\n";

            {
                Manager mgr2(resPtr);
                mgr2.useResource();
                cout << "Reference count after passing to mgr2: " << resPtr.use_count() << "\n";
            } // mgr2 goes out of scope here

            cout << "Reference count after mgr2 goes out of scope: " << resPtr.use_count() << "\n";
        } // mgr1 goes out of scope here
        cout << "Reference count after mgr1 goes out of scope: " << resPtr.use_count() << "\n";
    } // Resource will be automatically released here when mgr goes out of scope

    return 0;
}