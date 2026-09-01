#include <bits/stdc++.h>
using namespace std;

int maxProfit(vector<int> &prices)
{
    int n = prices.size();
    int buy = prices[0];
    int maxProfit = 0;
    for (int r = 1; r < n; r++)
    {
        int currProfit = prices[r] - buy;
        if (currProfit > maxProfit)
        {
            maxProfit = currProfit;
        }
        if (prices[r] < buy)
            buy = prices[r];
    }
    return maxProfit;
}

int main()
{
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    // vector<int> prices = {5, 4, 2, 1};
    cout << "Maximum Profit: " << maxProfit(prices) << endl;
    return 0;
}