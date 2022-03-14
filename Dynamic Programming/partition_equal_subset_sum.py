# https://leetcode.com/problems/partition-equal-subset-sum/
# Version 2 - DP tabularisation compressed to a single row
# Time complexity       O(n * total)
# Space complexity      O(total)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[idx][sub_1] is a boolean array that tells us if with any combination of nums from index 0 to idx, our value of sub_1 == sub_2
        total = sum(nums)
        if total % 2 == 1:
            return False
        half_total = total // 2
        dp = [True] + [False] * half_total
        for num in nums:
            for sum_val in range(half_total, num - 1, -1):
                dp[sum_val] |= dp[sum_val - num]
        return dp[half_total]

# Version 1 - 0/1 Knapsack Problem. We can either pick an element or not to put into our first subset
# Quite slow and expensive given lots of recursive calls and a dict 
# Can instead do it with DP tabularisation, and make that 1D so it gives O(n) space 
# Time complexity       O(n * total)
# Space complexity      O(n * total)
from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.n = len(nums)
        self.total = sum(nums)
        self.memo = defaultdict(lambda: defaultdict(bool))
        return self.choose(0, 0)

    def choose(self, idx, sub_1):
        if self.memo.get(idx, {}).get(sub_1, None) == None:
            sub_2 = self.total - sub_1
            if (idx == self.n) or (sub_2 == 0):
                self.memo[idx][sub_1] = False
            elif sub_1 == sub_2:
                self.memo[idx][sub_1] = True
            else:
                self.memo[idx][sub_1] = self.choose(idx + 1, sub_1 + self.nums[idx]) or self.choose(idx + 1, sub_1)
        return self.memo[idx][sub_1]

'''
For each element we can either choose to add it to our to the "left" subset or not
If we do we increment the size of our left subset and decrement the size 
'''