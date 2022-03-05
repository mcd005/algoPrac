# https://leetcode.com/problems/sliding-window-maximum/
# Version 2 - Monotonic queue
# When we know what the largest value for the window is, we can disregard all other values
# at an index left of that value that are smaller. 
# They won't be needed to determine the max for subsequent windows
# So we use a monotonic queue: in this case the elements of the queue decrease in size as you move
# from head to tail
# So when we enqueue an element, we off all elements in front of it that are smaller
# This could be O(n) for any given time we enqueue but is amortised to O(1), because there
# can only be a max of n elements in our queue
# Time complexity       O(n)
# Space complexity      O(n)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # This will store indices so we can be sure we only looking at elements in the current window
        for i, num in enumerate(nums):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            if i >= k - 1:
                output.append(nums[q[0]])
        return output

# Version 1 - Heap and counter
# Time complexity       O(k + nlogn)
# Space complexity      O(n)
from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums[:k])
        h = [-key for key in counts.keys()]
        heapify(h)
        output = [-h[0]]
        n = len(nums)
        for i in range(n - k):
            counts[nums[i]] -= 1
            if counts[nums[i + k]] == 0:
                heappush(h, -nums[i + k])
            counts[nums[i + k]] += 1
            while counts[-h[0]] == 0:
                heappop(h)
            output.append(-h[0])
        return output

'''
Naive
For each window, we iterate over all the elements and check save the max
TC  O(n * k)

But we are doing unecessary computation
Only two of the elements in the window have changed (i.e. we lost one and gained one)
So why check all the elements again?
What we need to know is: did we just lose the max? Did we just gain a new max?

We could use a heap
Push the first k elements onto the heap
When we iterate forward one we first check if the top of the heap is still in the window
If it isn't then we pop it off
Then we push the new value to the heap
We then check to see what the max is
Time complexity is  O(klogk + nlogk)

Is there a way to query what the max of a window is in O(1)?

The maximum from window to window will change if
    The leftmost element was the sole max
    The righmost element is greater than the max of the previous window

So we could build a counter from the first k elements
While we build it we can keep track of the max

How would I build a max queue
    How did I build a max stack
        A min stack had two structures
        One which was simply a stack
        The other which was a stack of mins 
    q   = 1 3 2 7
    heap = 7 3 2 1
    counts =

How can we use what we learned from the max stack problem to solve this?
    Stack as usual
    Then we just had a stack to keep track
        We could do that because there was only one way the max could change
            Either popping or pushing
'''