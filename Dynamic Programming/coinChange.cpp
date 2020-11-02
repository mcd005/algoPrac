class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        
        int dp[amount + 1];
        dp[0] = 0;
        for (int i = 1; i < amount + 1; i++){
            dp[i] = pow(10, 4) + 1;
        }
        
        for (int i = 1; i < n + 1; i++){
            for (int j = coins[i - 1]; j < amount + 1; j++){
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1);
            }
        }
        
        return  dp[amount] == pow(10,4) + 1 ? -1 : dp[amount];
    }
};