# Version 2 - Constant space
# Imagine all n players are in a list [1, 2, 3, 4, ... n]
# if n = 1 then we return index 0 (i.e. 1)
# if n = 2 then we return index (0 + k) % n
# if n = 3 then we return index (f(2) + k) % n
# So generally we return (f(n - 1) + k) % n
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0 #f(0)
        for i in range(1, n + 1):
            result = (result + k) % i
        return result + 1

# Version 1 - Queue
from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque((i for i in range(1, n + 1)))
        while len(q) > 1:
            q.rotate(-k + 1)
            q.popleft()
        return q[0]

# Naive solution
# Have a circular linked list or equivalent, one node per person
# Start with ptr at head
# Increment the ptr k node
# Remove that node and start from the next node
# Repeat until only one node

# However I suspect there may be a way to solve this analytically
# And we probably don't even need a linked list, a queue coudl do the job

# Ops would look like
# Remove k % n
# Remove ((k % n) + k ) % n
# Remove (((k % n) + k ) % n) + k) % n

# There must be an analytical solution
# Hypothesis: answer is (k % n) + 1
# Hypothesis not true when k = 1
# Hypothesis not true when k = 2
# Because mod operator is not distributive maybe there is no analytical soln and may we do have to do n ops

## Key Lessons ##
# Implement the basic version first
# Although it seems like it, there may not be an O(1) analytical solution that is easy to get to