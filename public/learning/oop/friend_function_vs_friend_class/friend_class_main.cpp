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

    void introduceYourself()
    {
        cout << "Name: " << name << ", Company: " << company << ", Age: " << age << endl;
    }

    friend class Manager;
};

class Manager
{
public:
    void changeEmployeeName(Employee &emp, const string &newName)
    {
        emp.name = newName;
    }
    void enhanceEmployeeAge(Employee &emp)
    {
        emp.age += 1;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Employee emp("John", "ABC Corp", 30);
    emp.introduceYourself();
    // emp.name = "Doe"; // This line will cause a compilation error since 'name' is private
    Manager mgr;
    mgr.changeEmployeeName(emp, "Doe");
    mgr.enhanceEmployeeAge(emp);
    emp.introduceYourself();
    return 0;
}