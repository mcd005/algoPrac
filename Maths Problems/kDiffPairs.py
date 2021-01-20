# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Version 1 - Counters hashmap
# Time complexity       O(n)
# Space complexity      O(n)
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        countedNums = Counter(nums)
        numPairs = 0
        for num in countedNums:
            if num + k in countedNums and k > 0:
                numPairs += 1
            elif k == 0 and countedNums[num] > 1:
                numPairs += 1
        return numPairs