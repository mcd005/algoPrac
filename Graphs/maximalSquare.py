# https://leetcode.com/problems/maximal-square/
# Version 1 - A BFS-esque soltuion
# where we build up a square layer by layer

# First we iterate through the grid
# Once we find a cell with a 1, we call bfs() and check the cells in the following fashion 
# 
# 1 * --->  1 1 * --->  1 1 1 *
# * !       1 1 *       1 1 1 *                  
#           * * !       1 1 1 *
#                       * * * !
# 
# Using the ! as an origin, the BFS iterates over the * cells
# if either ! or * are out of the grids range 
# or contain a 0
# then that layer is invalid and we stop the BFS
# otherwise  we can keep adding layers, and do so until we find an invalid layer

# Time complexity       O((n*m)^2)
# Space complexity      O(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSideLength = 0
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    sideLength = self.bfs(matrix, i, j, n, m)
                    maxSideLength = max(maxSideLength, sideLength)
        return maxSideLength ** 2
    
    def bfs(self, matrix, r, c, rMax, cMax):
        sideLength = 0
        while r < rMax and c < cMax and matrix[r][c] == "1":
            for i in range(1, sideLength + 1):
                if  r - i < 0 or c - i < 0 or matrix[r - i][c] != "1" or matrix[r][c - i] != "1":
                    return sideLength
            r += 1
            c += 1
            sideLength += 1
        return sideLength

# Version 2 - Fastest from LC
# Time complexity       O(n*m + n*m)
# Space complexity      O(m)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        # Cols[j] represents the number uninterrupted 1s in cells
        # above matrix[i][j], including matrix[i][j]. 
        # Interrupted means there is a zero among those cells
        # [ ["1","0","1","0","0"], -> cols = ["1","0","1","0","0"]
        #   ["1","0","1","1","1"], -> cols = ["2","0","2","1","1"]
        #   ["1","1","1","1","1"], -> cols = ["3","1","3","2","2"]
        #   ["1","0","0","1","0"]] -> cols = ["4","0","0","3","0"]
        # i.e. this is the height of a potential square whose bottom edge
        # starts is at matrix[i][j]
        cols = [0 for _ in matrix[0]]
        for row in matrix:
            for i, col in enumerate(row):
                if col == "0":
                    cols[i] = 0
                else:
                    cols[i] += 1
            max_square = self.helper(cols, max_square)
        return max_square * max_square
        
    def helper(self, cols: List[int], max_square) -> int:
        # next_max is so we don't waste our time
        # looking for a square smaller than our current max
        next_max = max_square + 1
        
        count = 0
        
        # If our next_max = 4
        # We are looking in cols for a contigous subsequence
        # of length 4
        # whose vals are all at least 4
        for c in cols:
            if c >= next_max:
                count += 1
            else:
                count = 0
            if count == next_max:
                return max_square + 1
        
        return max_square

# How can we determine it is a square?
#       All sides are the same length
#       And all the middle is filled in
#       Four vertices that are (0, 0), (x, 0), (0, -x), (x, -x)
#           How do we determine what is a vertex?
#               A vertex is when has same number of neighbour 1s as zeros
# If it has 4 vertices and it's area is a square is it valid?