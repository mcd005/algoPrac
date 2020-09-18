class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        r = l = 0
        for char in s:
            if char == 'R':
                r += 1
            else:
                l += 1
            if (r == l):
                result += 1
                r = l = 0
        return result