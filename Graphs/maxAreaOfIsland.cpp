// https://leetcode.com/problems/max-area-of-island/

// Version 1 - Iterate through the grid
// Recursively DFS when you encounter a 1
// Time complexity      O(n*m)
// Space complexity     O(n*m)
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] == 1){
                    maxArea = max(maxArea, dfs(grid, i, j, n, m));
                }
            }
        }
        
        return maxArea;
    }
    
    int dfs(vector<vector<int>>& grid, int r, int c, int maxR, int maxC){
        if (r < 0 || r >= maxR || c < 0 || c >= maxC) return 0;
        if (grid[r][c] == 0) return 0;
        grid[r][c] = 0;
        return 1 +
        dfs(grid, r - 1, c, maxR, maxC) +
        dfs(grid, r, c + 1, maxR, maxC) +
        dfs(grid, r + 1, c, maxR, maxC) +
        dfs(grid, r, c - 1, maxR, maxC);
    }
};

// Version 2 - Same as V1 but slightly faster in ms
// Fewer recursive function calls are put on the stack
// because you pre-check if the coord next in the dfs is:
//      1) within bounds
//      2) non-zero
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] == 1){
                    maxArea = max(maxArea, dfs(grid, i, j, n, m));
                }
            }
        }
        
        return maxArea;
    }
    
    int dfs(vector<vector<int>>& grid, int r, int c, int maxR, int maxC){
        grid[r][c] = 0;
        int sum = 1;
        if (r - 1 >= 0 && grid[r - 1][c] != 0) sum += dfs(grid, r - 1, c, maxR, maxC);
        if (c + 1 < maxC && grid[r][c + 1] != 0) sum += dfs(grid, r, c + 1, maxR, maxC);
        if (r + 1 < maxR && grid[r + 1][c] != 0) sum += dfs(grid, r + 1, c, maxR, maxC);
        if (c - 1 >= 0 && grid[r][c - 1] != 0) sum += dfs(grid, r, c - 1, maxR, maxC);
        return sum;
    }
};