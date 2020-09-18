'''
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

Have two 1D arrays
One to keep track of what the view of the skyline would look like from the top or bottom
One to keep track of what the view of the skyline would look like from the left or right

Iterate through the array and see what are the highest buidlings for either perspective
Then iterate through the array again and se how much you can increase the height of the other buidlings by
Return the total height increase of the buidling

The C++ solution implements this in a much neater way using max

Time complexity         O(n*m) where n and m are the side lengths
Space complxeity        O(n + m)
'''

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        result = 0
        
        sideLength = len(grid)
        
        if sideLength == 1: 
            return 0
        
        topBot = [0] * sideLength
        lefRi = [0] * sideLength
    
        for runThrough in range(2):
            for i in range(sideLength):
                for j in range(sideLength):
                    if runThrough == 0:
                        if grid[i][j] > topBot[j]:
                            topBot[j] = grid[i][j]
                        if grid[i][j] > lefRi[i]:
                            lefRi[i] = grid[i][j]
                    else:
                        diff = min(topBot[j], lefRi[i]) - grid[i][j]
                        if diff > 0:
                            result += diff
        
        return result
            
        
