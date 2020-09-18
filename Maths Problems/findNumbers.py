'''
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0 
        for num in nums:
            if len(str(num))%2 == 0:
                evens += 1
        return evens

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0 
        for num in nums:
            size = 0 
            while (num > 1):
                num /= 10
                size += 1
            if (size % 2 == 0) and (size > 0):
                evens += 1
        return evens

#From LC discussions
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(math.log10(n)) % 2 for n in nums)