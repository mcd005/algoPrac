# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Version 1 - Push and pop to a K sized heap 
# Time complexity       O(nlogk)
# Space complexity      O(k)
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

# TODO Look at these solutions https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).