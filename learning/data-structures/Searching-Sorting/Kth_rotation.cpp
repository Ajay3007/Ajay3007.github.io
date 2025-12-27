#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int findKRotation(vector<int> &arr) {
        int n = arr.size();
        int l = 0, r = n-1, mid;
        if(n == 1) return 0;
        while(l < r) {
            mid = l + (r - l)/2;
            if(mid == 0) {
                if(arr[mid] < arr[mid+1]) return 0;
                else return 1;
            }
            if(mid == n-1) {
                if(arr[mid-1] < arr[mid]) return 0;
                else return n-1;
            }
            if(arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1]) {
                if(arr[0]> arr[mid]) r = mid - 1;
                else l = mid + 1;
            } else if(arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1]) {
                return mid + 1;
            } else {
                return mid;
            }
        }
        return 0;
    }
};

int main() {
    int t = 1;
    // cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution obj;
        cout << obj.findKRotation(arr) << endl;
    }
    return 0;
}