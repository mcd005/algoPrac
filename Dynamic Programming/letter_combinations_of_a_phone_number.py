# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
# Version 1 - Recursive list comprehension
# Time complexity       O(4^n)
# Space complexity      O(n) which is the depth of the recursive tree
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        return self.generate(digits)
        
    def generate(self, digits):
        if len(digits) == 1:
            return self.digit_letters[digits]
        all_other_letters = self.generate(digits[1:])
        return [first_letter + other_letters for first_letter in self.digit_letters[digits[0]] for other_letters in all_other_letters]