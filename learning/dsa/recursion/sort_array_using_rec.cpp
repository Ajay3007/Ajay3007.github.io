#include<bits/stdc++.h>
using namespace std;

/* Helper function to insert an element in sorted order into a sorted array. */
void rec_insert(vector<int> &arr, int x) {
    if(arr.size() == 0) {
        arr.push_back(x);
        return;
    }
    int last = *(arr.end() - 1);
    if(last <= x) {
        arr.push_back(x);
        return;
    }
    arr.pop_back();
    rec_insert(arr, x);
    arr.push_back(last);
}

/* Recursive insertion sort implementation */
void rec_sort(vector<int> &arr) {
    if(arr.size() == 0) return;
    int last = *(arr.end() - 1);
    arr.pop_back();
    rec_sort(arr);
    rec_insert(arr, last);
    return;
}

int main() {
    // Example usage
    vector<int> arr = {6, 3, 5, -2, 9, 3, 10, 5};
    for(auto a : arr) cout<<a<<" ";
    rec_sort(arr); // Sorting the array using recursion
    cout<<endl;
    for(auto a : arr) cout<<a<<" ";
}