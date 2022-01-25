# Version 2 - Stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i,c in enumerate(s):
            if c =='(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

# Version 1 - Use sets to track chars for deletion
# Time complexity           O(2n)
# Space complexity          O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = set()
        closed = set()
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                opened.add(i)
            elif s[i] == ')':
                if len(opened) > 0:
                    opened.pop()
                else:
                    closed.add(i)

        print(opened)
        return "".join(s[i] for i in range(n) if i not in opened and i not in closed)