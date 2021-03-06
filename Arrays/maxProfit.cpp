// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Version 1 - Find the maximum following each local minimum
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        int curMin = prices[0];
        
        int n = prices.size();
        for (int i = 1; i < n; ++i)
        {
            if (prices[i] > curMin)
            {
                result = max(result, prices[i] - curMin);
            }
            else curMin = prices[i];
        }
        
        return result;
    }
};