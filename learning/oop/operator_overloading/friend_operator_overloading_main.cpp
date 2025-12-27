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

    friend ostream& operator<<(ostream& os, const Employee& emp);
};

ostream& operator<<(ostream& os, const Employee& emp)
{
    os << "Name: " << emp.name << ", Company: " << emp.company << ", Age: " << emp.age;
    return os;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Employee emp("John", "ABC Corp", 30);
    cout << emp << endl << emp << endl; // you can use the overloaded operator << to print Employee details -> chaining
    return 0;
}