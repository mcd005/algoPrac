class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int result = 0;
        int rows = grid.size(); 
        int cols = grid[0].size();
        for (int i = rows-1; i >= 0; --i){
            for (int j = cols-1; j >= 0; --j){
                if (grid[i][j] < 0){
                    result++;
                }
                else{
                    break;
                }
            }
        }
        return result;
    }
};

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m(grid.size()), n(grid[0].size()), r(0), c(n - 1);
        int ans = 0;
        while (r < m) {
            while (c >= 0 && grid[r][c] < 0) c--;
            ans += n - c - 1;
            r++;
        }
        return ans;
    }
};

//Starts on the top row, rightmost column and moves left.
//Once it finds a positive number, records number of negatives seen (ans+=) and moves down a row to start again
