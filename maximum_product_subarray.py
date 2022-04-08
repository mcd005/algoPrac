class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] > 0 and dp[i - 1] > 0:
                dp[i] = dp[i - 1] * nums[i]
            if nums[i] <= 0 and dp[i - 1] <- 0:
            dp[i] = max(dp[i - 1] * nums[i], dp[i - 1], nums[i])
        return dp[n - 1]


'''
[2,3,-2,4]

[2, 6, ]
'''