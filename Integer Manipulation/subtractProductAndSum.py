
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Fairly trivial maths

# Time complexity         O(n) for an n digit number
# Space complexity        O(1)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        while(n > 0):
            rem = n % 10
            sum += rem
            prod *= rem
            n = (n - rem)/10
        return int(prod - sum)