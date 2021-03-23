# Version 1 - https://leetcode.com/problems/meeting-rooms-ii/

# We first sort the meetings by start time
# We put the end time for the first meeting of the day in priority q 
# this will be used track the rooms that are still in use at any given time
# It uses min heap: the top of the heap will be the meeting ending soonest
# We iterate through the meetings
# If the next meeting starts after the the top of the heap, then we don't need another room
# We just pop the top meeting off (i.e. we vacate that room)
# And then push the meeting onto the heap
# So either we use the room that has just been vacated or use a new room

# Time complexity       O(nlogn + nlogn) 
# Space complexity      O(n)
# to sort a list of n intervals, and then insert n intervals into a heap
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if heap[0] <= start:
                heappop(heap)
            heappush(heap, end)
        return len(heap)

# Version 2 - Two pointer
# Time complexity       O(nlogn + n) 
# Space complexity      O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        rooms = 0
        sp, ep = 0, 0
        while sp < len(intervals):
            # For every start time there is a corresponding end time
            # If there are multiple start times before a given end time
            # We know we will need multiple rooms
            if starts[sp] < ends[ep]:
                rooms += 1
            else:
                ep += 1
            sp += 1
        return rooms


