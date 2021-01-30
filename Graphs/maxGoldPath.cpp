// https://leetcode.com/problems/path-with-maximum-gold/submissions/

// Version 2 - V1 upgraded
// Brute force DFS but refactored so fewer unecessary
// recursive calls are put on the stack
class Solution {
public:
    int sum;
    void dfs(vector<vector<int>>& grid, int r, int c, int n, int m, int s){
        int temp = grid[r][c];
        grid[r][c] = 0;
        s += temp;
        sum = max(s, sum);
        if (c - 1 >= 0 && grid[r][c - 1] != 0) {
            dfs(grid, r, c - 1, n, m, s);
        }
        if (c + 1 < m && grid[r][c + 1] != 0){
            dfs(grid, r, c + 1, n, m, s);
        }
        if (r - 1 >= 0 && grid[r - 1][c] != 0){
            dfs(grid, r - 1, c, n, m, s);
        }
        if (r + 1 < n && grid[r + 1][c] != 0){
            dfs(grid, r + 1, c, n, m, s);
        }
        grid[r][c] = temp;
    }
    
    int getMaximumGold(vector<vector<int>>& grid) {
        
        sum = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] != 0){
                    dfs(grid, i, j, n, m, 0);
                }
            }
        }
        
        return sum;
    }
};


// Version 1 - DFS but brute force
// Time complexity      O((n * m)^2)
// Space complexity      O(n * m)
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int globalMax = 0;
        
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] != 0){
                    globalMax = max(globalMax, dfs(grid, i, j, n, m));
                }
            }
        }
        
        return globalMax;
    }
        
        int dfs(vector<vector<int>>& grid, int r, int c, int n, int m){
            if (r < 0 || r >= n || c < 0 || c >= m) return 0;
            if (grid[r][c] == 0) return 0;
            int temp = grid[r][c];
            grid[r][c] = 0;
            int neighbours[4];
            neighbours[0] = dfs(grid, r, c - 1, n, m);
            neighbours[1] = dfs(grid, r, c + 1, n, m);
            neighbours[2] = dfs(grid, r - 1, c, n, m);
            neighbours[3] = dfs(grid, r + 1, c, n, m);
            int localMax = 0;
            for (auto nb : neighbours){
                localMax = max(nb, localMax);
            }
            grid[r][c] = temp;
            return temp + localMax;
        }
};