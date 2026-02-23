#include <iostream>
#include <string>

using namespace std;

class Employee {
private:
    int id;
    string name;
    double salary;
public:
    // Constructor
    Employee(int empId, const string& empName, double empSalary)
        : id(empId), name(empName), salary(empSalary) {}
    // Getter for ID
    int getId() const {
        return id;
    }
    // Getter for Name
    string getName() const {
        return name;
    }
    // Getter for Salary
    double getSalary() const {
        return salary;
    }
    // Setter for Salary
    void setSalary(double newSalary) {
        salary = newSalary;
    }
    // Method to display employee details
    void displayInfo() const {
        cout << "Employee ID: " << id << endl;
        cout << "Employee Name: " << name << endl;
        cout << "Employee Salary: $" << salary << endl;
    }
};

int main() {
    // Create an Employee object
    Employee emp(101, "John Doe", 55000.0);
    
    // Display employee information
    emp.displayInfo();
    
    // Update salary
    emp.setSalary(60000.0);
    
    // Display updated employee information
    cout << "\nAfter salary update:\n";
    emp.displayInfo();
    
    return 0;
}