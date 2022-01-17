# https://leetcode.com/problems/brick-wall/
# Version 1 - Hashmap with number of edges at each x
# Time complexity         O(nm)
# Space complexity        O(m)
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges_at_x = defaultdict(lambda: 0)
        max_edges_for_any_x = 0
        for layer in wall:
            x = 0
            m = len(layer)
            for i in range(m - 1):
                x += layer[i]
                edges_at_x[x] += 1
                max_edges_for_any_x = max(max_edges_for_any_x, edges_at_x[x])
        
        return len(wall) - max_edges_for_any_x

'''
[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

edges = {1: 3, 2: 1, 3: 3, 4: 4, 5: 2}

Determine the x value at which the most edges occur 
Count how many bricks you intersect at (number of edges at the index - total number of layers)

We have a dict that looks like (x_coord: number of edges at x)
We iterate through each of the layers and build up the dict
In the meantime we are tracking our max number of edges at x
At the end we return n - that max (i.e total number of layers - max number of edges at any given index)
'''
