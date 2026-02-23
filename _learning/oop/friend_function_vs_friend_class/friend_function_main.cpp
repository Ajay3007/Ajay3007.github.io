#include <bits/stdc++.h>
using namespace std;

class Employee
{
private:
    string name;
    string company;
    int age;
public:
    Employee(string n, string c, int a) : name(n), company(c), age(a) {}

    void introduceYourself() {
        cout << "Name: " << name << ", Company: " << company << ", Age: " << age << endl;
    }

    friend void changeName(Employee &emp, const string &newName);

};

void changeName(Employee &emp, const string &newName) {
    emp.name = newName;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Employee emp("John", "ABC Corp", 30);
    emp.introduceYourself();
    // emp.name = "Doe"; // This line will cause a compilation error since 'name' is private
    changeName(emp, "Doe");
    emp.introduceYourself();
    return 0;
}