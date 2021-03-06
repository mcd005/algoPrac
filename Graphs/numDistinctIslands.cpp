// https://leetcode.com/problems/number-of-distinct-islands
// Version 1 - DFS using an unordered set of strings
// to keep track of shapes
// Time complexity      O(n*m)
// Space complexity     O(n*m)
// where n and m are the length of the sides of the grid
class Solution {
public:
    int n = 0;
    int m = 0;
    
    int numDistinctIslands(vector<vector<int>>& grid) {
        n = grid.size();
        if (n == 0) return 0;
        m = grid[0].size();
        
        unordered_set<string> seen;
        
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] == 1){
                    string shape;
                    dfs(grid, i, j, shape, 'o');
                    seen.insert(shape);
                }
            }
        }
        
        return seen.size();
    }
    
private:
    void dfs(vector<vector<int>>& grid, int r, int c, string& shape, char dir){
        if (r < 0 || r >= n || c < 0 || c >= m || grid[r][c] == 0) {
            shape.push_back('f'); // this attempt failed
            return;
        }
        grid[r][c] = 0;
        shape.push_back(dir);
        dfs(grid, r + 1, c, shape, 'n');
        dfs(grid, r, c + 1, shape, 'e');
        dfs(grid, r - 1, c, shape, 's');
        dfs(grid, r, c - 1, shape, 'w');
    }
};