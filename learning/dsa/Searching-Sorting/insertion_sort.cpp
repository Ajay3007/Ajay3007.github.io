#include<bits/stdc++.h>
using namespace std;

/* Insertion Sort implementation */
void insertion_sort(vector<int> &arr) {
    int n = arr.size();
    for(int i=1; i<n; i++) {
        int j = i;
        while(j>0 && arr[j-1] > arr[j]) {
            swap(arr[j], arr[j-1]);
            j--;
        }
    }
}

int main() {
    vector<int> arr = {64, 25, 12, 11, 22, 11, 88};
    int n = arr.size();
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
    insertion_sort(arr);
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
    
}