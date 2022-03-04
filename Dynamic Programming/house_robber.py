# https://leetcode.com/problems/house-robber/
# Version 2 - DP with O(1) space
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, n):
            cur, pre = max(nums[i] + pre, cur), cur
        return cur

# Version 1 - DP with O(n) space
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]  * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]

'''
Classic 1D DP
If there are 1 houses we rob just 1
If there are 2 we rob whichever has more
If there are 3 we either rob house 0 and 2 or house 1 whichever combo has more
And so on
'''