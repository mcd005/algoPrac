# https://leetcode.com/problems/find-peak-element/
# Version 1 - Binary search
# Time complexity       O(logn)
# Space complexity      O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

'''
Naive solution
Check all triplets in linear time

log n suggest that some kind of binary search solution exists
Because each nums[i] != nums[i + 1] and out of bounds are -inf we can guarantee there is at least one peak
nums is comprised of multiple decreasing or increasing subsequences
So we use the local slope to direct us towards a peak
    If there is only one peak we will converge on that
    If there are lots of peaks, we'll bounce aroudn but eventually left and right will lie on the same slope
'''