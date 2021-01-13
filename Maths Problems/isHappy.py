# https://leetcode.com/problems/happy-number/
#
# We know a number will loop cause an endless loop if, after some number of iterations
# it produces a number that has already been produced.
#
# So we use a HashMap seen to keep track of these
# Other than that we implement the logic as described by the question
#
# Time complexity         ???
# Space complexity        ???

def squareDigits(num):
    out = 0
    while num > 0:
        out += (num % 10)**2
        num //= 10
    return out

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = squareDigits(n)
            if n in seen:
                return False
        return True