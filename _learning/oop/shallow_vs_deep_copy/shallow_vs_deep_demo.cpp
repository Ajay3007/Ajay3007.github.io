#include <bits/stdc++.h>
using namespace std;

// -------------------------
// SHALLOW example
// -------------------------
// No user-defined copy ctor → compiler provides a shallow copy
class Shallow {
public:
    char* data;

    Shallow(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
        cout << "[Shallow] ctor: allocated " << static_cast<void*>(data) << " -> \"" << data << "\"\n";
    }

    // Note: no copy ctor implemented here -> default (shallow) copy used

    void release() {            // helper: free and null the pointer
        delete[] data;
        data = nullptr;
        cout << "[Shallow] release(): freed data, pointer set to nullptr\n";
    }

    ~Shallow() {
        if (data) {
            cout << "[Shallow] dtor: deleting " << static_cast<void*>(data) << "\n";
            delete[] data;
        } else {
            cout << "[Shallow] dtor: data is nullptr, nothing to delete\n";
        }
    }
};


// -------------------------
// DEEP example
// -------------------------
class Deep {
public:
    char* data;

    Deep(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
        cout << "[Deep] ctor: allocated " << static_cast<void*>(data) << " -> \"" << data << "\"\n";
    }

    // user-defined copy constructor → performs DEEP COPY
    Deep(const Deep& other) {
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
        cout << "[Deep] copy ctor: allocated " << static_cast<void*>(data)
             << " (copy of " << static_cast<const void*>(other.data) << ")\n";
    }

    // user-defined copy assignment (for completeness)
    Deep& operator=(const Deep& other) {
        if (this == &other) return *this;
        delete[] data;
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
        cout << "[Deep] copy assign: allocated " << static_cast<void*>(data) << "\n";
        return *this;
    }

    ~Deep() {
        cout << "[Deep] dtor: deleting " << static_cast<void*>(data) << "\n";
        delete[] data;
    }
};


// -------------------------
// Demo driver
// -------------------------
int main() {
    cout << "----- SHALLOW COPY DEMO -----\n";
    {
        Shallow s1("Hello");
        cout << "s1.data addr: " << static_cast<void*>(s1.data) << " -> \"" << s1.data << "\"\n";

        // Default copy constructor -> shallow copy: pointer value copied (same address)
        Shallow s2 = s1;   // shallow copy
        cout << "After shallow copy: s2.data addr: " << static_cast<void*>(s2.data)
             << " -> \"" << (s2.data ? s2.data : (char*)"nullptr") << "\"\n";

        cout << "\nSimulate resource release by s1 (bad scenario):\n";
        s1.release();   // s1 frees the buffer and sets pointer to nullptr

        cout << "Now s2.data still points to the old address: " << static_cast<void*>(s2.data) << "\n";
        cout << "If s2's destructor later tries to delete the same pointer, it causes double-delete / UB.\n";

        // To avoid crash in this demo, clear s2.data harmlessly (what a robust program would do
        // if it transfers ownership or after noticing resource was freed elsewhere).
        s2.data = nullptr;
        cout << "For demo safety, we set s2.data = nullptr to avoid double-delete in destructor.\n";
    } // s1 and s2 go out of scope here; destructors run (but we've nulled s2 so no double-delete)

    cout << "\n----- DEEP COPY DEMO -----\n";
    {
        Deep d1("World");
        cout << "d1.data addr: " << static_cast<void*>(d1.data) << " -> \"" << d1.data << "\"\n";

        // Deep copy constructor is called
        Deep d2 = d1;
        cout << "After deep copy: d2.data addr: " << static_cast<void*>(d2.data)
             << " -> \"" << d2.data << "\"\n";

        cout << "\nModify original buffer's first char to 'w' to show copies are independent.\n";
        d1.data[0] = 'w';   // changes only d1
        cout << "d1.data -> \"" << d1.data << "\"\n";
        cout << "d2.data -> \"" << d2.data << "\"  (unchanged)\n";
    } // d1 and d2 destructors run; each deletes its own buffer safely

    cout << "\nDemo complete.\n";
    return 0;
}
