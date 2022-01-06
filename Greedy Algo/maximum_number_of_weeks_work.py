import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        h = [-1 * stones for stones in milestones]
        heapq.heapify(h)
        num_weeks = 0
        while h:
            leader = heapq.heappop(h)
            top = heapq.heappop(h)
            diff = top - h[0]
            if diff:
                leader += diff
                top += diff

# You complete a milestone per week
# You can't work on the same project back to back

# Is there a problem with greedily working on the project with the most milestones left to compete
# whilst interspersing it with the project with the second most milestones

# We can do this problem in O(n)

# Priority Queue
# Might be quite slow to continously push and pop from a priority queue though
# Is there a way to speed things up?
# We are only decrementing once each time we push and pop
# And pushing takes logn time

# Decrement the top and the leader by the difference between the top and second from top + 1 extra if doesn't tie break
# If there is no difference between the top and the second from top, then just decrement the the leader and the top by one and 
# [10, 7, 5, 4] --> [7, 5, 5, 2] --> [6, 5, 4, 2] --> [5, 4, 4, 2] --> [4, 4, 3, 2] --> [3, 3, 3, 2]
# [14, 5, 5, 2] --> [12, 4, 4, 2] -->
# Run ahead until you go down a step
# The length of the step is 2 and the leader is 7
# So once we move the whole step down by 1 we'll have 5, 4, 4
# We intersect when we move the step down (7 - xn) = 5 - x
# Then from the edge of that step, you can walk back, decrementing each by 1
# What we need to do instead is work out what the diff is and decremting (diff / length of run) but div mod so we have some left over

# You either decrement the leader until it's the same as the second from top
# Or you decrement the top until it

# [5, 2, 1, 1] 
# Solve 5, 2 ---> 5 weeks --> 0, 1, 0, 1, 0
# Solve 3, 1 ---> 2 weeks --> 2, 0
# Solve 2, 1 ---> 2 weeks --> 3, 0
# [10, 7, 5, 4]
# 0101010101010102323232320
# Solve (0, 10), (1, 7) --> 15 weeks. Remainder is 2, which we push into heap
# Solve (2, 5), (3, 4) --> 9 weeks. Remainder is 0, which we discard
# Solve (0, 2), (2, 1) --> 3 weeks, remainder is 1, can't do anythin with
# Sums to 27                         

# Take the top of the heap
# Ask "How many weeks can we alternate this with the next thing on the heap"
# Does it matter if we totally deplete the project that is second from the top of the heap?
# No probably not
# From the POV of the biggest project all the other projects are the same

# What if we sort up front?
# Then you can alternate first and second,  until you deplete either below third
# What you're actually doing is decrementing the top two alternately
# [5, 2, 1] -> [4, 2, 1] - > [4, 1, 1]
# When you decrement the second until it's the same as the third to nth, you can pick any of the third to nth ones
# Maybe you want to decrement any o

# Sort the milestones
# Pop off the back and hold this as your leader
# If leader - queue[-1] > queue[-2] you do leader -= queue[-1]
# Otherwise you only want to do leader -= queue[-1] - queue[-2] and do queue[-1] = queue[-2]
# Then we run forward until we find a number that doesn't equal queue[-1] (or we hit the end)
# [10, 7, 5, 4] --> 0, 1, 0, 1, 0 --> [8, 5, 5, 4]
# [7, 7, 5, 4] --> 0, 1, 0, 1, 0 --> [8, 5, 5, 4]
# [7, 7, 7, 2]

# Can we do this DP?
# What is the max number of weeks you could work with only one project in the array
#       1 week
# What is the max number of weeks you could work with two projects
#       (first - second) * 2 + 1
#       5, 3 --> 5, 3, 5, 3, 5, 3, 5
# What is the max number of weeks you could work with three projects?
#       10, 3, 2 --> 10, 3, 10, 3, 10, 3, 10, 2, 10, 2
#       (first - second) * 2 + 1 + min(first - second, third) * 2 - 1
#       7 + 3 = 10
# What is the maximum number of weeks you could work with four projects?
#       10, 3, 2, 1 --> 10, 3, 10, 3, 10, 3, 10, 2, 10, 2, 10, 1, 10
#       (first - second) * 2 + 1 + min(remainder of bigger from base cas, third) * 2 - 1 + min(remainder, fourth) * 2 + 1
# What if there is a smaller discrepancy between the milestones
#       4, 3, 2 --> 4, 3, 4, 3, 4, 3, 
#       min(first, second) * 2 + 1 + min(remainder of bigger from base cas, third) * 2 - 1 + min(remainder, fourth) * 2 + 1

# For every two of those you can place one. Problem is you don't actually want to place the small ones until you have to
# Although does it matter if you place them early
