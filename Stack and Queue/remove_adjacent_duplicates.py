# Version 2 - From LC. Conceptually the same as V1 except you only push to the stack when you're changing chars
# and you discard the current char as soon as there are k of it
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        current = ""
        currentCount = 0
        for char in s:
            if char != current:
                stack.append((current, currentCount))
                current = char
                currentCount = 1
            else:
                currentCount += 1
                if currentCount == k:
                    current, currentCount = stack.pop()

        stack.append((current,currentCount))

        return "".join(char * count for char, count in stack)

# Version 1 - Stack that is the run-length encoded version of the list
# Looks like [[a, 2], [b, 1], [c, 3]] for aabccc
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if not stack:
                stack.append([s[i], 1])
            else:
                if s[i] == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack[-1][1] %= k
                    if stack[-1][1] == 0:
                        stack.pop()
                        continue
                    else:
                        stack.append([s[i], 1])
            i += 1

        stack[-1][1] %= k
        if stack[-1][1] == 0:
            stack.pop()

        return "".join(char * run_length for char, run_length in stack)