# https://leetcode.com/problems/detect-capital/
# 
# If all the letters are the same case it is fine
# And the only acceptable change in case 
# is from the first letter (uppper) to the second letter (lower)
#
# Time complexity       O(n)
# Space complexity      O(1)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        prevCase = word[0].isupper()
        for i in range(1, n):
            curCase = word[i].isupper()
            if curCase != prevCase:
                if i != 1 or curCase == 1:
                    return False
            prevCase = curCase
        return True