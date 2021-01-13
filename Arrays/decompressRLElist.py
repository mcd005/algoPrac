'''
https://leetcode.com/problems/decompress-run-length-encoded-list/

Orginally implemented the below solution but then converted it into a list comprehension solution

Time complexity 	O(n*m)		where m is the freq of a number n
Space complexity 	O(n*m)
'''

# Version 2 - List comprehension
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [x for i in range(0, len(nums), 2) for x in [nums[i+1]] * nums[i] ]

# Version 1 - standard python for loop
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
       	decompressed = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            #print(freq, val)
            for j in range(freq):
                decompressed.append(val)
        return decompressed
        