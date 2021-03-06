// https://leetcode.com/problems/edit-distance/
// Version 1 - DP tabularisation
// Time complexity      O(n*m)
// Space complexity     O(n*m)
// where n = word1.size(), m = word2.size();
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        // We create a grid dp[i][j] which represents the number of ops
        // to go from string word1[0...i) to word1[0...j) 
        // Base cases are:
        // word1 = word1[0...i) ---> word2 = ""     i.e. just deleting chars
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = i;
        }
        // word1 = "" ---> word2 = word2[0...j)     i.e. just inserting chars
        for (int j = 1; j <= m; ++j) {
            dp[0][j] = j;
        }
        // or word1 = "" ---> word2 = ""            i.e do nothing
        // We then iterate through all the possible start and target strings
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    // if the current char in start is same as char in target
                    // do nothing. Same number of ops as the word1[0...i - 1) ---> word2[0...j -1)
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Otherwise we are either going to have to replace, insert or delete
                    // Replace = dp[i - 1][j - 1] + 1
                    // Insert = dp[i - 1][j] + 1
                    // Delete = dp[i][j - 1] + 1
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }
        return dp[n][m];
    }
};

// Version 1 - DP O(m) space
// Time complexity      O(n*m)
// Space complexity     O(m)
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size(), pre;
        vector<int> cur(m + 1, 0);
        for (int j = 1; j <= m; ++j) {
            cur[j] = j;
        }
        for (int i = 1; i <= n; ++i) {
            pre = cur[0];
            cur[0] = i;
            for (int j = 1; j <= m; ++j) {
                int temp = cur[j];
                if (word1[i - 1] == word2[j - 1]) {
                    cur[j] = pre;
                } else {
                    cur[j] = min(pre, min(cur[j - 1], cur[j])) + 1;
                }
                pre = temp;
            }
        }
        return cur[m];
    }
};

