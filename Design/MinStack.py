# Version 1 - Conventional stack and a stack to hold the min of the stack at a given size
# Time complexity           O(1)
# Space complexity          O(n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val
        if self.mins and self.mins[-1] < val:
            new_min = self.mins[-1]
        self.mins.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

'''
## Key Lessons ##
The only place the stack is changing is the top, so once we've determined what the min is there,
it won't change until that point becomes the top of again
'''