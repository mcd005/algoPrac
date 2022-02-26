# https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
# Version 2 - We try to build a stack of sum terms
# This means we treat + and - as only a sign for each of those terms. They don't need to be kept on the stack as operators
# TODO extract the operator if statements as a method
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                    # tmp = stack.pop()
                    # if tmp//num < 0 and tmp%num != 0:
                    #     stack.append(tmp//num+1)
                    # else:
                    #     stack.append(tmp//num)
                num = 0
                sign = s[i]
        return sum(stack)

# Version 1 - We store both nums and ops on a stack. We can compress multiply and divide terms
# We then iterate over the stack and compute add and subtract terms
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_value = 0
        for char in s:
            if char is " ":
                continue
            if char.isdigit():
                cur_value = (cur_value * 10) + int(char)
            elif char in "+-/*":
                if not stack or stack[-1] in "+-":
                    stack.append(cur_value)
                    stack.append(char)
                else:
                    top_op = stack.pop()
                    top_val = stack.pop()
                    if top_op == "*":
                        stack.append(top_val * cur_value)
                    elif top_op == "/":
                        stack.append(top_val // cur_value)
                    stack.append(char)
                cur_value = 0

        if stack:
            top_op = stack[-1]
            if top_op in "*/":
                top_val = stack[-2]
                stack[-2:] = [top_val * cur_value] if top_op == "*" else [top_val // cur_value]
            else:
                stack.append(cur_value)

            m = len(stack)
            cur_value = stack[0]
            for i in range(1, m, 2):
                next_op, next_val = stack[i], stack[i + 1]
                if next_op == "+":
                    cur_value += next_val
                else:
                    cur_value -= next_val

        return cur_value

'''
PEMDAS
String must look like: spaces digit digit spaces operator spaces digit 
With tidying it's basically a lots of int operator pairs, with the last element no having a corresponding operator

We declare a stack that will hold collected values and operators
We iterate through the string
While we have a space and no collected do nothing
When we encounter a digit we times the current value of digit by ten and add the new digit
If we encounter a space then we just keep iterating until we see an operator
    We push both the value and the operator to the stack
    We reset value of integer and operator and look for the next int operator pair
When we encounter it we check if the order of precedence of the new operator matches that at the top of the stack 
If it does we apply the top of the stacks value and operator to current held value
We update the top of the stack with this new value and the new operator
If the operation precedence, doesn't match we push to the stack
At the we undwind the stack

Check how well zeroes are dealt with
    We don't expect leading zeros and single digit zero is fine
Is doing intermediate int division going to mess things up?
    It looks like it relies on the orders the ops are written
What happens if there are divide multiply terms at the end
    Find because we are unwinding stack from top they are dealt with first
Divide by zero?
    Not an allowed input
    Zeroes will arise but only as numerators

There could be a solution that uses .split()

### Key Lessons ###
Need to anticipate pitfalls before you start coding and keep them in mind when you do start
    i.e dealing with zeroes, intermediate int division
Try to boil the problem down to it's fundamentals more (e.g. can represent the expression as a sum of signed ints)
Write logic first then rearrange it
'''