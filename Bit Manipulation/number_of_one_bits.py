# https://leetcode.com/problems/number-of-1-bits/
# Time complexity       O(n) where n is the number of bits used to represent the integer. Here it's 32
# Space complexity      O(1)
# If this was being called multiple times you would memoise the result
class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n:
            num_ones += (n % 2 == 1)
            n >>= 1
        return num_ones

class Solution:
    def hammingWeight(self, n):
        c = 0
        while n:
            n &= n - 1 # This gets rid of the rightmost LS one bit. If n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000
            c += 1
        return c

class Solution:
    def hammingWeight(self, n):
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555)) # We first count how many ones are in each pair
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n