# https://leetcode.com/problems/3sum/submissions/
# Time complexity       O(n^2)
# Space complexity      O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        old_nums_i, triplets = set(), set()
        n = len(nums)
        seen = {} # This was in the i loop before but we don't need to repopulate it for every target
        for i in range(n):
            if nums[i] not in old_nums_i: # When we've checked a target once, we don't need to search for it again
                for j in range(i + 1, n): # We've already checked nums[:i + 1] when we did other targets
                        nums_k = -nums[i] - nums[j]
                        if nums_k in seen and seen[nums_k] == i: # We only need to check if nums_k is a valid complement for *this* iteration
                            triplet = [nums[i], nums[j], nums_k]
                            triplet.sort()
                            triplets.add(tuple(triplet))
                        seen[nums[j]] = i
                old_nums_i.add(nums[i])
        return list(triplets)

'''
Brute force 
    Iterate over the elements
    Then iterate over the elements behind current element (call these other elements)
    For each combination of current and other, iterate over the remaining elements looking for 0 - (current + other)
    This would take O(n^3)

In two sum we can make one of the linear searches constant by using a map
For each current element, we just need to see if target - current is in our map
We can do the same here to reduce complexity  to O(n^2)

If we sort the array in ascending it can allow us to finishes searches quicker
If the smaller element + the current element in our search is greater than target, we can end the search
This would give a time complexity of O(nlogn + n) so not really worthwihle

Can we do better than O(n^2)?
We have to pick targets in linear time don't we?
    Yes
Is there a way we can do the search in O(1)?
    No
So I think O(n^2) is the best case


### Key Lessons ###
Write out your algebra so you're sure it's correct
You can still get TLE even with best case run time. Try to reuse work and reduce unecessary computation
    See the comments for examples of this
'''