# https://leetcode.com/problems/range-module/

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# Version 1 - Sorted list of disjoint intervals. Found on LC
# Time complexity      O(n) for add or remove O(logn) for query
# Space complexity      O(n)
class RangeModule:

    def __init__(self):
        # List of disjoint intervals
        # Even elements open a range, odd close them
        self.track = []

    def addRange(self, left, right):
        # bisect_left(a, x) ---> insert x before all other entries of x already in a
        # bisect_right(a, x) ---> insert x after all other entries of x already in a
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        # if start is even it is opening a new interval between existing intervals so keep it
        # if it were odd it would lie witihin an interval so there would already be an element bounding it
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
        
        
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        # start and end must be same for [left, right) to be completely enclosed
        # Must also be odd so that lies within existing range
        return start == end and start % 2 == 1

    
    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        # if start is even it's not covered by an existing range so there is no need to remove
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack

# Version 1 - Currently not working. Hacky attempt with merge intervals
import bisect
class RangeModule:

    def __init__(self):
        self.interval_list = []        

    def addRange(self, left: int, right: int) -> None:
        insert_point = bisect_right(self.interval_list, [left, right - 1]) 
        self.interval_list = self.mergeIntervals(self.interval_list, insert_point, [left, right - 1])
        print(self.interval_list)

    def queryRange(self, left: int, right: int) -> bool:
        interval_idx = bisect_right(self.interval_list, [left, right - 1]) 
        if interval_idx == 0:
            return False
        if self.interval_list[interval_idx - 1][0] <= left and self.interval_list[interval_idx - 1][1] >= right - 1:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_list = []
        for interval in self.interval_list:
            cur_left, cur_right = interval[0], interval[1]
            if cur_left >= right or cur_right < left:
                new_list.append(interval)
            elif cur_right >= left and cur_right < right:
                new_list.append([cur_left, left - 1])
            elif cur_left <= right and cur_left >= left:
                new_list.append([right, cur_right])
            elif cur_left <= left and cur_right >= right:
                new_list.append([cur_left, left - 1])
                new_list.append([right, cur_right])
        self.interval_list = new_list
        print(self.interval_list)

    def mergeIntervals(self, interval_list, insert_point, new_interval):
        merged = interval_list[:insert_point]

        for i in range(insert_point - 1, len(interval_list)):
            if i > (insert_point - 1):
                new_interval = interval_list[i]
            if not merged or merged[-1][-1] < new_interval[0]:
                merged.append(new_interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], new_interval[-1])

        return merged
