// https://leetcode.com/problems/candy/

// Create DP array where dp[i] is the number of candies for the ith child
// Iterate forward through the array
//      If child before current has a lesser rating, 
//      give current child same number of candies as one before + 1
//      If they have as lesser rating they can just have 1 candy for now
// Then iterate backward through the array and apply the same logic
// so that each child with a greater rating sitting in front of one with a lesser rating
// has a least one more candy
// keeping a running sum of all candies as we go

// Time complexity      O(n)
// Space complexity     O(n)
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if (n == 1) return 1;

        vector<int> dp(n, 1);
        
        for (int i = 1; i < n; ++i)
        {
           if (ratings[i] > ratings[i - 1])
           {
               dp[i] = dp[i - 1] + 1;
           } 
        }
        
        int result = dp[n - 1];
        for (int i = n - 2; i > -1; --i)
        {
            if (ratings[i] > ratings[i + 1] && dp[i] <= dp[i + 1])
            {
                dp[i] = dp[i + 1] + 1;
            }
            result += dp[i];
        }
        return result;
    }
};
