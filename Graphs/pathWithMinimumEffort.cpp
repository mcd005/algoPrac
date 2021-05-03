// https://leetcode.com/problems/path-with-minimum-effort/
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        
    }
};

/* 
Note you only need to track max effort (i.e. greatest change from consecutive cells)

Shall we do a greedy where in each case we check which cell has the smallest change?

Will not always leads to the globally optimum result. Say you follow a path of ones that will take you to a cul-de-sac

Maybe you can do DP by asking: What is the smallest delta from the neighbouring squares

The min effort from (0, 0) --> (n, m) is the min((1, 0) to end, (0, 1) to end)

You could do this recursive function and check all the paths but that is quite expensive

*/