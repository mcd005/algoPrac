# https://leetcode.com/problems/container-with-most-water/
# Version 1 - Two pointer
# Time complexity       O(n)
# Space complexity       O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            if height[left] <= height[right]:
                max_water = max(max_water, (right - left) *  height[left])
                left += 1
            else:
                max_water = max(max_water, (right - left) *  height[right])
                right -= 1
        return max_water

'''
The amount of water trapped between two peaks is equal to the min height of the two peaks
times by the distance between them

I think what we want to do is have two pointers, one starts at index 0 and the other starts at index n - 1
For every combination of peaks we want to compute how much water is being trapped and save it if it's max
Then whichever pointers is on the smaller of the two peaks, we move that inward

If the peaks are the same height we move the left pointer
'''