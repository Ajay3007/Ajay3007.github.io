#include <bits/stdc++.h>
using namespace std;

class Complex
{
public:
    double real;
    double imag;

    Complex(double r = 0.0, double i = 0.0) : real(r), imag(i) {}

    Complex operator+(const Complex &other) const
    {
        return Complex(real + other.real, imag + other.imag);
    }

    Complex &operator=(const Complex &other)
    {
        if (this != &other)
        {
            this->real = other.real;
            this->imag = other.imag;
        }
        return *this;
    }

    friend ostream &operator<<(ostream &os, const Complex &c)
    {
        os << c.real << (c.imag >= 0 ? "+" : "") << c.imag << "i";
        return os;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Complex c1(3, 2);
    Complex c2(1, 7);  
    cout << "c1: " << c1 << "\n";
    cout << "c2: " << c2 << "\n";  
    Complex c3 = c1 + c2;
    cout << "c3 (c1 + c2): " << c3 << "\n";  
    Complex c4;
    c4 = c1;
    cout << "c4 (assigned from c1): " << c4 << "\n";
    return 0;
}