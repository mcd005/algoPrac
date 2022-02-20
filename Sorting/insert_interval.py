# Version 3 - Like version 2 expect we can break out when we no longer have overlaps
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def insert(self, intervals, newInterval):
        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)
            elif n[1] < i[0]:
                res.append(n)
                return res + intervals[index:]
            else:
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        res.append(n)
        return res

# Version 2 - Create list for interval that are to the left and right of the region of intervals being merged
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right

# https://leetcode.com/problems/insert-interval/
# Version 1 - Binary serach for insertion point and see what needs to be merged either side
# Time complexity       O(logn + n)
# Space complexity       O(1)
import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        i = bisect.bisect_left(intervals, newInterval)
        start, first = None, None
        if i > 0:
            if intervals[i - 1][1] >= newInterval[1]:
                return intervals
            if intervals[i - 1][1] >= newInterval[0]:
                start = intervals[i - 1][0] # start 2
                first = i - 1 # first 0
        if start is None:
            if i == n or newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval) 
                return intervals
            start, first = newInterval[0], i
        end, last = newInterval[1], first + 1 # end 7, first = 1
        for j in range(i, n):
            if end < intervals[j][0]:
                break
            end = max(end, intervals[j][1])
            last = j + 1
        intervals[first:last] = [[start, end]]
        return intervals

'''
We don't want to have to pop intervals from the middle of the list, that is an O(n) operation
We'd rather just work out what intervals we need to keep and modiy and then reconstruct the list

Use bisect to get the position at which the interval should be inserted, lets call this index i
We then inspect i - 1 for 3 scenearios
    Complete overlap
        We return the list unmodified
    Partial overlap
        Lower bound is set the lower of i - 1
    No overlap of the new interval to be inserted
        Lower bound is set by our inserted value
Then iterate from i - 1 (if it exists) checking if  current interval overlaps the next interval partyl or entirely

I decided slicing was the best way to do it but there were probably better ways

Overlap lower /
No overlap /
Overlap upper / 
Lower fully overlaps / 
Prepend /
Append / 
Partial overlaps lower and upper /
Fully overlaps multiple
'''
