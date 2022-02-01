# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Version 1 - Modified binary search
# Time Complexity       O(logn)
# Space Complexity      O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Is the left half an unbroken sorted segment?
            if nums[left] <= nums[mid]: 
                # If it is an target lies within that segment search there
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # Is the left half an unbroken sorted segment?
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
                
        return left if nums[left] == target else -1


'''
Determine which half is the unbroken sorted half (i.e. does not contain pivot)
If the target value lies within the two values at the ends of the sorted half, we shrink our search to that half
Otherwise we must shrink our search to the other half of the array
And we repeat this recursively until our idxs converge

Need to be careful about overlapping idxs 
Need to add logic to return -1

### Key Lessons ###
For search, you just need to get the rought idea of how you slice things up first
    then you do examples to make sure you are shrinking the search space and choosing the right slice
'''