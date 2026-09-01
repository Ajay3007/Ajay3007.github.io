#include<bits/stdc++.h>
using namespace std;

class Smartphone
{
public:
    // Attributes
    string brand;
    string model;
    double price;

    // Constructor
    Smartphone(string b = "", string m = "", double p = 0.0) : brand(b), model(m), price(p) {}

    // Overloaded + operator to combine prices of two smartphones
    Smartphone operator+(const Smartphone &other) const
    {
        return Smartphone(brand, model, price + other.price);
    }

    // Overloaded = operator for assignment
    Smartphone &operator=(const Smartphone &other)
    {
        if (this != &other)
        {
            this->brand = other.brand;
            this->model = other.model;
            this->price = other.price;
        }
        return *this;
    }

    // Friend function to overload << operator for easy output
    friend ostream &operator<<(ostream &os, const Smartphone &s)
    {
        os << "Brand: " << s.brand << ", Model: " << s.model << ", Price: $" << s.price;
        return os;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Smartphone s1("Apple", "iPhone 13", 999.99);
    Smartphone s2("Samsung", "Galaxy S21", 799.99); 
    cout << s1 << endl << s2 << endl;
    // cout << "Smartphone 1: " << s1 << "\n";
    // cout << "Smartphone 2: " << s2 << "\n";  
    Smartphone s3 = s1 + s2;
    // cout << "Combined Price Smartphone: " << s3 << "\n";  
    Smartphone s4;
    s4 = s1;
    // cout << "Assigned Smartphone 4 from Smartphone 1: " << s4 << "\n";
    return 0;
}