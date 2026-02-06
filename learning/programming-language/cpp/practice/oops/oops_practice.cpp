/*
 * oops_practice.cpp
 * C++ OOP Practice Pack (Interview Oriented)
 *
 * Topics:
 * - Class & Object
 * - Encapsulation
 * - Constructors / Destructors
 * - Inheritance
 * - Polymorphism
 * - Virtual / Override
 * - Abstraction
 * - Static members
 * - Operator Overloading
 * - Rule of 3 / 5
 * - Smart Pointers
 * - Templates
 * - Exceptions
 * - Singleton Pattern
 *
 * Compile:
 *   g++ -std=c++17 -O0 -g oops_practice.cpp -o oops_practice
 *
 * Run:
 *   ./oops_practice
 */

#include <iostream>
#include <memory>
#include <vector>
#include <stdexcept>

using namespace std;

/* ============================================================
 * TASK 1: Basic Class & Object
 * ============================================================ */

class Person {
private:
    string name;
    int age;

public:
    // TODO: constructor

    // TODO: setters/getters

    void print();
};

void task1_basic_class() {
    cout << "\n[TASK 1] Basic Class\n";

    // TODO: create object and test
}

/* ============================================================
 * TASK 2: Encapsulation
 * ============================================================ */

class BankAccount {
private:
    double balance;

public:
    // TODO: constructor

    void deposit(double amt);
    bool withdraw(double amt);

    double getBalance() const;
};

void task2_encapsulation() {
    cout << "\n[TASK 2] Encapsulation\n";

    // TODO: test account
}

/* ============================================================
 * TASK 3: Constructors & Destructors
 * ============================================================ */

class Resource {
public:
    Resource();
    ~Resource();
};

void task3_ctor_dtor() {
    cout << "\n[TASK 3] Constructor / Destructor\n";

    // TODO: create local object
}

/* ============================================================
 * TASK 4: Inheritance
 * ============================================================ */

class Employee {
protected:
    int id;

public:
    Employee(int i);
    void show();
};

class Manager : public Employee {
private:
    int teamSize;

public:
    // TODO: constructor
    void show();
};

void task4_inheritance() {
    cout << "\n[TASK 4] Inheritance\n";

    // TODO
}

/* ============================================================
 * TASK 5: Polymorphism (Virtual Functions)
 * ============================================================ */

class Shape {
public:
    virtual double area() = 0;   // pure virtual
    virtual ~Shape() {}
};

class Rectangle : public Shape {
    double w, h;

public:
    // TODO: constructor
    double area() override;
};

class Circle : public Shape {
    double r;

public:
    // TODO: constructor
    double area() override;
};

void task5_polymorphism() {
    cout << "\n[TASK 5] Polymorphism\n";

    // TODO: vector<Shape*> and compute area
}

/* ============================================================
 * TASK 6: Abstraction (Interface)
 * ============================================================ */

class Logger {
public:
    virtual void log(string msg) = 0;
    virtual ~Logger() {}
};

class ConsoleLogger : public Logger {
public:
    void log(string msg) override;
};

void task6_abstraction() {
    cout << "\n[TASK 6] Abstraction\n";

    // TODO
}

/* ============================================================
 * TASK 7: Static Members
 * ============================================================ */

class Counter {
private:
    static int count;

public:
    Counter();

    static int getCount();
};

void task7_static() {
    cout << "\n[TASK 7] Static Members\n";

    // TODO
}

/* ============================================================
 * TASK 8: Operator Overloading
 * ============================================================ */

class Complex {
public:
    double r, i;

    Complex(double r=0, double i=0);

    // TODO: overload +
    // TODO: overload <<
};

void task8_operator_overload() {
    cout << "\n[TASK 8] Operator Overloading\n";

    // TODO
}

/* ============================================================
 * TASK 9: Rule of 3 / 5
 * ============================================================ */

class Buffer {
private:
    int* data;
    int size;

public:
    Buffer(int s);

    // TODO:
    // Destructor
    // Copy ctor
    // Copy assign
    // Move ctor
    // Move assign
};

void task9_rule_of_five() {
    cout << "\n[TASK 9] Rule of 5\n";

    // TODO
}

/* ============================================================
 * TASK 10: Smart Pointers
 * ============================================================ */

class Node {
public:
    int val;
    shared_ptr<Node> next;

    Node(int v);
};

void task10_smart_ptr() {
    cout << "\n[TASK 10] Smart Pointers\n";

    // TODO: build linked list
}

/* ============================================================
 * TASK 11: Templates
 * ============================================================ */

template <typename T>
T myMax(T a, T b) {
    // TODO
    return a;
}

void task11_templates() {
    cout << "\n[TASK 11] Templates\n";

    // TODO
}

/* ============================================================
 * TASK 12: Exception Handling
 * ============================================================ */

int divide(int a, int b) {
    // TODO: throw if b==0
    return a/b;
}

void task12_exceptions() {
    cout << "\n[TASK 12] Exceptions\n";

    // TODO
}

/* ============================================================
 * TASK 13: Singleton Pattern
 * ============================================================ */

class Config {
private:
    static Config* instance;

    Config();   // private

public:
    static Config* getInstance();

    void show();
};

void task13_singleton() {
    cout << "\n[TASK 13] Singleton\n";

    // TODO
}

/* ============================================================
 * MAIN
 * ============================================================ */

int main() {

    cout << "=== OOP PRACTICE PACK ===\n";

    task1_basic_class();
    task2_encapsulation();
    task3_ctor_dtor();
    task4_inheritance();
    task5_polymorphism();
    task6_abstraction();
    task7_static();
    task8_operator_overload();
    task9_rule_of_five();
    task10_smart_ptr();
    task11_templates();
    task12_exceptions();
    task13_singleton();

    cout << "\n=== DONE ===\n";

    return 0;
}
