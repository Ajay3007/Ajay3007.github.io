#include<bits/stdc++.h>
using namespace std;

/* Bubble Sort Algorithm. */
void bubble_sort(vector<int> &arr) {
    int n = arr.size();
    // To optimize the algorithm by stopping if the array is already sorted
    bool swapped = false; 
    for(int i=0; i<n-1; i++) {
        swapped = false; // Reset swapped for each pass
        for(int j=0; j<n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                swapped = true; // A swap occurred
                swap(arr[j], arr[j+1]);
            }
        }
        // If no two elements were swapped in the inner loop, the array is sorted
        if(!swapped) return;
    }
}

int main() {
    vector<int> arr = {64, 25, 12, 22, 11};
    int n = arr.size();
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
    bubble_sort(arr); // Sorting the array using bubble sort
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
}