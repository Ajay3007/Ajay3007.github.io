#include<bits/stdc++.h>
using namespace std;

class Strudent
{
    public:
        // Attributes
        string name;
        int rollNumber;
        vector<string> booksIssued;
        
        // Constructor
        Strudent(string n = "", int r = 0) : name(n), rollNumber(r) {}

        // Overloaded + operator to combine books issued by two students
        Strudent operator+(const Strudent &other) const
        {
            Strudent combinedStudent;
            combinedStudent.name = this->name + " & " + other.name;
            combinedStudent.rollNumber = -1; // Indicating combined student
            combinedStudent.booksIssued = this->booksIssued;
            combinedStudent.booksIssued.insert(combinedStudent.booksIssued.end(),
                                               other.booksIssued.begin(),
                                               other.booksIssued.end());
            return combinedStudent;
        }

        // Overloaded = operator for assignment
        Strudent &operator=(const Strudent &other)
        {
            if (this != &other)
            {
                this->name = other.name;
                this->rollNumber = other.rollNumber;
                this->booksIssued = other.booksIssued;
            }
            return *this;
        }

        // Friend function to overload << operator for easy output
        friend ostream &operator<<(ostream &os, const Strudent &s)
        {
            os << "Name: " << s.name << ", Roll Number: " << s.rollNumber << ", Books Issued: [";
            for (size_t i = 0; i < s.booksIssued.size(); ++i)
            {
                os << s.booksIssued[i];
                if (i != s.booksIssued.size() - 1)
                    os << ", ";
            }
            os << "]";
            return os;
        }
};