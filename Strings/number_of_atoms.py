# https://leetcode.com/problems/number-of-atoms/
# Version 2 - Iterative and just use stack to track multiplier
# Time complexity           O(n)
# Space complexity          O(n)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        record = collections.defaultdict(int)
        num = ''
        coeff = 1
        ele = ''
        stack = []
        for i in formula[::-1]:
            if i.isdigit():
                num += i
            elif i.islower():
                ele += i
            elif i.isupper():
                ele += i
                record[ele[::-1]] += (int(num[::-1]) if num else 1)*coeff
                ele = ''
                num = ''
            elif i == ')':
                coeff *= int(num[::-1]) if num else 1
                stack.append(int(num[::-1]) if num else 1)
                num = ''
            elif i == '(':
                coeff //= stack.pop()
        return ''.join([k+(str(c) if c != 1 else '') for k,c in sorted(record.items())])

# Version 1 - Recursive
# Time complexity           O(n)
# Space complexity          O(n)
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.element_counts = defaultdict(lambda: 0)
        self.formula = formula
        self.expand(len(formula) - 1, 1)
        return "".join(el + (str(self.element_counts[el]) if self.element_counts[el] > 1 else "") for el in sorted(self.element_counts))
        
    def expand(self, i, multiplier):
        count, pow_ten = 1, 0
        letters = []
        reset_counts = False
        while i > -1:
            if self.formula[i].isdigit():
                count *= not (count == 1 and pow_ten == 0)
                count += int(self.formula[i]) * 10**pow_ten
                pow_ten += 1
            elif self.formula[i].isalpha():
                letters.append(self.formula[i])
                if self.formula[i].isupper():
                    element = "".join( letters[j] for j in range(len(letters) - 1, -1, -1) )
                    self.element_counts[element] += count * multiplier
                    reset_counts = True
            elif self.formula[i] == ')':
                i = self.expand(i - 1, count * multiplier)
                reset_counts = True
            elif self.formula[i] == '(':
                return i
            if reset_counts:
                count, pow_ten = 1, 0
                letters = []
                reset_counts = False
            i -= 1

        return i

# Case is Uuuuuuuu22222(Case)
# Might it be better to do this backwards

# We have a dict to store element counts
# Iterate backwards through the string
# We first expect a series of digits
#  As we encounter the digits we go up successive powers of 10
# Then we iterate until we find either and uppercase letter or a closed bracket
#       Each letter we append to a list and will form a word when we do a join on an generator that reverses the list
# If we find an uppercase letter we can just add it to our dict times by the number
# Other wise we make a recursive call to a function that starts on the otherside of the bracket, and 
# continues to add to our dict in the way described above, except with a multiplier given
# This recursive call will return the index of just after the closing bracket so that the call below it on the stack can continue
# At the end we can sort the dict by keys and then either ast.literal eval or manually eval the dict to get the result

### Lessons learned ###
# Think about what you actually need to put on the stack. Why put a call when you could just put an integer
# RTFQ. Didn't want dict wanted RLE string
# Sometimes the logic has to be messy and nested