# https://leetcode.com/problems/longest-increasing-subsequence/
# Version 1
# The length of the longest subsequence ending at any given element is 
# the max length of the longest subsqeuence ending at elements before it
# whose values are less than it
# + 1
# We can check those elements in slightly less time
# If we maintain a priority queue whose elements are [value of element from original array, longest seq ending at that element
# Time complexity       O(nlogn + n^2)
# Space complexity      O(n)
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        globalMax = 1
        # Intialise a priority queue that will look like (value of element, longest seq ending at that element)
        bsa = [[nums[0], 1]]
        n = len(nums)
        for i in range(1, n):
            curVal = nums[i]
            j = 0
            m = len(bsa)
            localMax = 0
            # We iterate through our priority queue
            while j < m and curVal > bsa[j][0]:
                # For elements in that queue with values less than curVal
                # we check if the lenght of LIS ending at that value is greater than the
                localMax = max(localMax, bsa[j][1])
                j += 1
            # When we reach an element in the pq that bigger than curVal
            # or the end of the pq
            # We update the global LIS if 
            globalMax = max(globalMax, localMax + 1)
            insort_left(bsa, [curVal, localMax + 1])
        return globalMax

# Version 2 - Monotonic quasi-stack
# Time complexity       O(nlogn)
# Space complexity      O(n)
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We initialise a quasi-stack who can only have elements
        # pushed to it if they are greater than the top of the stack
        mos = []
        for num in nums:
            if not mos or num > mos[-1]:
                mos.append(num)
            else:
                # if the element cannot go on top of the stack 
                # then it will be smaller than an element that is somewhere else in the stack
                # replacing that existing element in the stack with the smaller element
                # gives us more room to put other, not quite so big elements, on the stack
                # making it easier to increase it size (i.e. to increase the LIS)
                idx = bisect_left(mos, num)
                mos[idx] = num
        return len(mos)

#TODO explain
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0 for _ in range(len(nums))]
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if x <= tails[m]:
                    j = m
                else:
                    i = m + 1
            tails[i] = x
            size = max(size, i + 1)
        
        return size