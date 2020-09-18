'''
https://leetcode.com/problems/two-sum/

Using a HashMap (python dict) for constant time lookup
For each element work out what number it would have to sum with to meet the target
If that number is in the dict then you've found a valid two sum

Time complexity		O(n)
Space complexity	O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
     