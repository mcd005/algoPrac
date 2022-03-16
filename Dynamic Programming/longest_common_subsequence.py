# https://leetcode.com/problems/longest-common-subsequence/
# Version 1 - DP Tabularisation
# Time complexity       O(nm)
# Space complexity      O(nm)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][m]


'''
Careful, this is not sliding window because if you boild down text2 into a counter, you lose sense of order

We create an array dp[i][j] 
where we store the result of the longest common subsequence between s[0:i+1] and t[0:j+1]
'''
