# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
# Version 1 - Classic stack as counter for parentheses question
# Time complexity        O(n)
# Space complexity       O(n)
class Solution:
    def maxDepth(self, s: str) -> int:
        depth, max_depth = 0, 0
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')' and depth > 0:
                max_depth = max(max_depth, depth)
                depth -= 1

        return max_depth
'''
(((3))

depth = 0
local_max = 0

We have a counter which increments every time we see an open bracket
When we see a closed bracket and the counter is greater than zero
        we save it's value. This value is a candidate for max nesting depth
        We then decrement the counter
Each time the depth counter hits zero we know have traversed a VPS so save our current candidate for max depth

(asd(asdasd(kjnasd()iasdsad)))

Because s must be a VPS and a VPS can't include a single bracket
all brackets must be matched
That means that we don't need to confirm we have reached the end (i.e. don't need to do the check when the counter hits zero)
So everytime we match a bracket we know we are at a valid depth

### Key Lesson ###
Pay attention to the constraints of the question
'''
