# https://leetcode.com/problems/first-missing-positive/
# Version 1 - Cyclic Sort
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            idx_to_swap_to = nums[i] - 1
            if nums[i] > 0 and idx_to_swap_to != i and idx_to_swap_to < n and nums[i] != nums[idx_to_swap_to]: 
                nums[i], nums[idx_to_swap_to] = nums[idx_to_swap_to], nums[i]
            else:
                i += 1
        target = 1
        for num in nums:
            if num != target:
                return target
            target += 1
        return target

'''
If we wanted to solve with O(n) memory
We'd declare a boolean array of length n called seen
If we see positive integer i in nums we marks seen[i - 1] = True
We'd then iterate seen and on the first false return it's index + 1

Cyclic sort
    Iterate through nums
    If num is postive try and swap it with the value at nums[num - 1]
    If num - 1 is out of range, do nothing or already same as value
    Once you've "sorted", iterate through again
    We a first looking for 1
    If nums[0] is == 1 then we can icnrement the number we are looking for
    If a number is postive try and swap it 

### Key Lesson ###
If you have to do things with constant space, most of the time you will need to use the memory you're given
Be careful! This can cause bugs: nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
    I thought it was strictly atomic but as the values at the indicies change the swap will reflect this
'''