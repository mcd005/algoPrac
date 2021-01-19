def dfs(grid, r, c, rMax, cMax):
    if not (0 <= r < rMax) or not (0 <= c < cMax):
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '#'
    dfs(grid, r, c + 1, rMax, cMax)
    dfs(grid, r + 1, c, rMax, cMax)
    dfs(grid, r , c - 1, rMax, cMax)
    dfs(grid, r - 1 , c, rMax, cMax)
    return

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(grid, row, col, rows, cols)
        
        return count