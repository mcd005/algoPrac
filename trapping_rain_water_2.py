# Version 1 - Tried to directly adapt 2D solution. Doesn't account for leaks
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        north = [[0 for j in range(n)] for i in range(m)]
        east = [[0 for j in range(n)] for i in range(m)]
        south = [[0 for j in range(n)] for i in range(m)]
        west = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i != 0:
                    north[i][j] = max(north[i - 1][j], heightMap[i - 1][j])
                if j != 0:
                    west[i][j] = max(west[i][j - 1], heightMap[i][j - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1:
                    south[i][j] = max(south[i + 1][j], heightMap[i + 1][j])
                if j != n - 1:
                    east[i][j] = max(east[i][j + 1], heightMap[i][j + 1])

        total = 0
        for i in range(m):
            for j in range(n):
                local_trapped = min(north[i][j], east[i][j], south[i][j], west[i][j]) - heightMap[i][j]
                if local_trapped > 0:
                    total += local_trapped

        return total

# Version 2 
from collections import deque
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.m = len(heightMap)        
        self.n = len(heightMap[0])
        neighb_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        total_trapped = 0
        for i in range(self.m):
            for j in range(self.n):
                for di, dj in neighb_list:
                    if self.isInBounds(i + di, j + dj) and heightMap[i + di][j + dj] > heightMap[i][j]:
                        current_trapped = 0
                        peak_height = heightMap[i + di][j + dj]
                        leak_height = peak_height
                        is_leaking = False
                        visited = set()
                        q = deque([(i, j)])
                        while q:
                            i_s, j_s = q.popleft()
                            current_trapped += peak_height - heightMap[i_s][j_s]
                            visited.add((i_s, j_s))
                            for di_s, dj_s in neighb_list:
                                if self.isInBounds(i_s + di_s, j_s + dj_s) and peak_height > heightMap[i_s + di_s][j_s + dj_s]  and (i_s + di_s, j_s + dj_s) not in visited:
                                    q.append()
                                elif not self.isInBounds(i_s + di_s, j_s + dj_s):
                                    is_leaking = True
                                    leak_height = min(leak_height, heightMap[i_s][j_s])
                        total_trapped += current_trapped * (not is_leaking)
                        for i_v, j_v in visited:
                            if not is_leaking:
                                heightMap[i_v][j_v] = peak_height
                            else:
                                heightMap[i_v][j_v] = min(peak_height, heightMap[i_v][j_v] + (peak_height - leak_height) )

        return total_trapped

    def isInBounds(self, i, j):
        return (0 <= i < self.m) and (0 <= j < self.n)

'''
[[1,4,3,1,3,2],
 [3,2,1,3,2,4],
 [2,3,3,2,3,1]]

q = 
i_s, j_s = 0, 0
visited = 0,0

total_trapped = 0
current_trapped = 3 
peak_height = 4
leak_height = 1
is_leaking = True

Algo would look like
    Iterate
    If a square has one it's neighbours at a greater height then we possibly have a place for trapping water. Begin BFS
    BFS works by enqueueing all adjacent squares whose height is less than or equal to the peak we descended from
    Increment count as we go
    We also save the coords of the squares we're visiting for our current search
    If we hit the edge of the given area with our BFS, we have found a leak
    We continue the search

    At the end of the search there were two possible outcomes
        Either we didn not find a leak and thus can bank all the water we counted
            We can also "fill in" the respective holes by setting their height to the height of the peak we descended from 
        Or we found a leak. We do not bank any water
            We also need to mark the each of the squares we searched so we don't search them again
                We do this by doing a similiar "fill" operation
                We take the min height of any of the leaks we found
                And to each square we searched we add (peak_height - min_leak_height)
                But only to a max of peak_height
                This means that all squares with a height above the leak are levelled (i.e. they can't trap water)
                But squares with a height below the leak are kept
The flaw with is logic however is that it will fill holes that aren't connected to some leaks

Edge case where we fill loads of times?


We need to do it the other way around where we iterate around the boundary looking for leaks and then BFS to find which areas are compromised
How do we know when to stop the BFS?

    If you discover a wall that is higher than that then you start to queue the other
    When we encounter a hole like in the minimum of example 2, we know that it can't leak to anywhere
    It's surrounded on all sides by tiles that are greater than it
    So even if things leaked off them nothing can leak from that hole
    So the definition of a hole is an 

Algo would look like
    We start a BFS from each coord on the boundary
    We enqueue all adjacent squares that are of greater or equal height (because they would drain to current square if water fell on them)
    We keep track of the max peak we encounter as well as the lowest height of any other leaks
    What happens if we encounter a square that is smaller?
        Maybe we don't touch it and only after we are done filling in we go over and look for holes?

Algo would look like
    We start our BFS at 0,0
    We enqueue all neighbouring tiles in a priority q, which puts the tiles at the lowest height at the top
    When we pop a tile off the queue we increment the count of the area for that level
    If we pop all tiles of the lowest height off the q and haven't encountered a leak at that level, we bank the rain that is trapped there
        We do this by taking the doing (total area * (2nd lowest height - current lowest height)) * isLeaking at that height
    If we do encounter a leak
        I think we have to continue BFS, but we say that all tiles greater than that height would drain to that leakage
    We keep track of each tile visited by marking it with a -1


How about a DFS
    Each tile we look at the neighbours
    We pick the neighbour with the lowest height
    We call dfs on it
    The base case is either one of our neigbours is out of bounds, in which case we have a leak
    Or all the neigbours are higher


In the 2D version you trap is equal to
    min(max height of a peak to left of index, max height of a peak to right of index) - height at index

So in the 3D version you trap is equal to
    min(max height of a peak to north of index,
        max height of a peak to east of index,
        max height of a peak to south of index,
        max height of a peak to west of index) - height at index

We need a matrix called north[i][j] which gives you the max peak to the north of i and j
We need the same for the three other directions

Then we just iterate through our square and we can ask for each i, j which is the 
min of the 4 peaks in either direction

TC O(5n)
SC O(4n)

Is there a way to do it in fewer passes?
Yes can populate north and east at the same time

However the problem with this is that we don't account for leaks


Was going to say you find the max height of any given point and then look at all slices from zero to that height
but that could be 2 * 10^4 iterations


We need to do some kind of BFS
What criteria do you need to start the search?
When do you stop counting?
If you discover a leak how do you forget that count?
How would you do this with count islands?

How about you iterate as you usually would
But when you go down a level you've found a possible location to trap water
You only bank that trapped amount when you've exhausted your search
How do we deal with leaks?
    Define a leak as when our region intersects with the edge of the area 

Maybe we have a set that marks if we have checked a coord for a certian level 
 
Holes are not possible


### Key lessons ###
Leaks prevent you from treating rows/cols individually
'''