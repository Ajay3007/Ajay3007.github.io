#include<bits/stdc++.h>
using namespace std;

/* Merge function to merge two sorted halves */
void merge(vector<int> &arr, int l, int mid, int r) {
    int n1 = mid - l + 1;
    int n2 = r - mid;
    vector<int> left(n1), right(n2);
    for(int i=0; i<n1; i++) left[i] = arr[l+i];
    for(int i=0; i<n2; i++) right[i] = arr[mid+1+i];
    int i = 0, j = 0, k = l;
    while(i < n1 && j < n2) {
        if(left[i] <= right[j]) arr[k++] = left[i++];
        else arr[k++] = right[j++];
    }
    while(i < n1) arr[k++] = left[i++];
    while(j < n2) arr[k++] = right[j++];
}

/* Merge Sort implementation */
void merge_sort(vector<int> &arr, int l, int r) {
    if(l >= r) return;
    int mid = l + (r - l)/2;
    merge_sort(arr, l, mid);
    merge_sort(arr, mid+1, r);
    merge(arr, l, mid, r);
}

int main() {
    vector<int> arr = {64, 25, 12, 11, 22, 11, 88};
    int n = arr.size();
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
    merge_sort(arr, 0, n-1);
    for(auto a : arr) cout<<a<<" ";
    cout<<endl;
}