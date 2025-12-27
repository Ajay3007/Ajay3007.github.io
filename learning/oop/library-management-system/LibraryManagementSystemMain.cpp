#include<bits/stdc++.h>
using namespace std;

class LibraryManagementSystem
{
public:
    // Attributes
    string libraryName;
    vector<string> departments;
    unordered_map<string, vector<string>> books;

    // Constructor
    LibraryManagementSystem(string name = "") : libraryName(name) {}

    // Method to add a department
    void addDepartment(const string &dept) {
        departments.push_back(dept);
    }

    // Method to add a book to a department
    void addBook(const string &dept, const string &book) {
        books[dept].push_back(book);
    }

    // Method to display library details
    void displayLibrary() const {
        cout << "Library Name: " << libraryName << "\nDepartments:\n";
        for (const auto &dept : departments) {
            cout << "- " << dept << "\nBooks in " << dept << ":\n";
            for (const auto &book : books.at(dept)) {
                cout << "  * " << book << "\n";
            }
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    LibraryManagementSystem library("City Library");
    library.addDepartment("Science Fiction");
    library.addDepartment("History");
    library.addDepartment("Technology");

    library.addBook("Science Fiction", "Dune by Frank Herbert");
    library.addBook("Science Fiction", "Neuromancer by William Gibson");
    library.addBook("History", "Sapiens by Yuval Noah Harari");
    library.addBook("Technology", "Clean Code by Robert C. Martin");

    library.displayLibrary();

    return 0;
}