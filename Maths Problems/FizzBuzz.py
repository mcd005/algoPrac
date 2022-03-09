# https://leetcode.com/problems/fizz-buzz/
# Version 2 - List comprehension
# Time complexity     O(n)
# Space complexity    O(1)
def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

# Version 1 - For loop, build string
# Time complexity     O(n)
# Space complexity    O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            current_ = ""
            if i % 3 == 0:
                result += "Fizz"
            if i % 5 == 0:
                result += "Buzz"
            if not result:
                result = str(i)
            output.append(result)
        return output
'''
Classic algo problem

Make sure you avoid mistakes with bad if else statements
Account for the multiples of 15 edge cases
'''