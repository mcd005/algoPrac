// Version 1 - DP O(m) space
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

// Version 1 - DP O(n*m) space
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= m; ++j) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }
        return dp[n][m];
    }
};