# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Version 1 - Stack
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left / right))
        return stack[0]