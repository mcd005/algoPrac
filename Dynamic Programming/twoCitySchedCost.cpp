// https://leetcode.com/problems/two-city-scheduling/submissions/

// Version 3 - Based on a soltion found on leetcode
// We sort costs by the difference between bCosti - aCosti
// This allows see what globally (not greedily) the best choice is to minimise cost
// After costs is sorted, for any given pair:
//      costs[0] represents the biggest cost saving we could get by choosing element A
//      costs[n - 1] represents the biggest cost saving we could get by choosing element B
// Time complexity      O(nlogn)
// Space complexity     O(1)
class Solution
{
public:
    int twoCitySchedCost(vector<vector<int>> &costs)
    {
        sort(costs.begin(), costs.end(), [](vector<int> &a, vector<int> &b) { return a[1] - a[0] > b[1] - b[0]; });
        int min = 0;
        for (int i = 0; i < costs.size(); ++i)
        {
            if (i < costs.size() / 2)
                min += costs[i][0];
            else
                min += costs[i][1];
            // std::cout << costs[i][0] << " " << costs[i][1] << "\n";
        }

        return min;
    }
};

// Version 2 - DP tabularisation using only one row
// Time complexity      O(n^2)
// Space complexity      O(n)
class Solution
{
public:
    int twoCitySchedCost(vector<vector<int>> &costs)
    {
        int n = costs.size() / 2;

        // We create a DP vector where dp[j] on iteration i represents the min cost given i flights to A and j flights to B
        vector<int> dp(n + 1, 0);
        for (int j = 1; j < n + 1; ++j)
        {
            dp[j] = dp[j - 1] + costs[j - 1][0];
        }

        for (int i = 1; i < n + 1; ++i)
        {
            dp[0] += costs[i - 1][1];
            for (int j = 1; j < n + 1; ++j)
            {
                dp[j] = min(dp[j] + costs[i + j - 1][1], dp[j - 1] + costs[i + j - 1][0]);
            }
        }

        return dp[n];
    }
};

// Version 1 - DP tabularisation
// Time complexity      O(n^2)
// Space complexity      O(n^2)
class Solution
{
public:
    int twoCitySchedCost(vector<vector<int>> &costs)
    {
        int n = costs.size() / 2;

        // We create a DP table where dp[i][j] represents the min cost given i flights to A and j flights to B
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        for (int k = 1; k < n + 1; ++k)
        {
            dp[0][k] = dp[0][k - 1] + costs[k - 1][0];
            dp[k][0] = dp[k - 1][0] + costs[k - 1][1];
        }
        for (int i = 1; i < n + 1; ++i)
        {
            for (int j = 1; j < n + 1; ++j)
            {
                dp[i][j] = min(dp[i - 1][j] + costs[i + j - 1][1], dp[i][j - 1] + costs[i + j - 1][0]);
            }
        }

        return dp[n][n];
    }
};


/*
The constraints mean you can't just pick the min in each case
because the min could be the bCost everytime
then n people to each city is not satisfied

Each person has to go to a city
So you're trying to decide which city should this person go to
You could do it greedily and say
    "Well currently city A's total cost is more than city B's total cost, so lets send to B"
    
Instead needs to be thought of like this
    If I allocate this one to B which future one do I now have to allocate to A
    
A brute force would look something like
    The first n go to A then the next n go to B
    Then we look at which ones we can swap to minimise the total cost
    
We construct a DP table
*/
