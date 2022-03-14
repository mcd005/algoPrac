# https://leetcode.com/problems/jump-game/
# Version 1 - Bottom-up (or rather top down) DP array converted to O(1)
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        min_idx_which_can_reach = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= min_idx_which_can_reach:
                min_idx_which_can_reach = i
        return min_idx_which_can_reach == 0

''' 
DP because can break down into sub problems
Base case: the array has length of one. We are at last so return true
Len == 2 
If index[0]

We want to create a boolean array can_reach
can_reach[-1] will always equal true
We iterate backwards through nums, starting from n - 2
If nums[n - 2] + n - 2 is greater than smallest index for which can_reach is true
then we set can_reach[n - 2] to true and update the index of the smallest index for which can reach is true
Once we are done iterating, we return the value of can_reach[0]

Because we are only really concerned with the min idx where can_reach is true, we don't need to store the whole array
and can instead solve the problem in O(1) space and O(n) time

Example 1
nums = [2,3,1,1,4]
can_reach = [F, F, T, T, T]
min_idx_for_can_reach = 2

Example 2
[3,2,1,0,4]
can_reach = [F, F, F, F, T]
min_idx_for_can_reach = 4
'''