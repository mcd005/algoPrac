// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

//Version 1
//Starts on the top row, rightmost column and moves left.
//Increments ans on each negative it encounters
//Once it finds a positive number,  it skips to the next row

//Time complexity   O(n * m)
//Space complexity  O(1)
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

//Version 2
//Starts on the top row, rightmost column and moves left.
//Once it finds a positive number, records number of negatives seen (ans+=) and moves down a row to start again
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m(grid.size()), n(grid[0].size()), r(0), c(n - 1);
        int ans = 0;
        while (r < m) {
            while (c >= 0 && grid[r][c] < 0) c--;
            //When it encounters the end of the row 
            //or postive number 
            //it adds the all the negative numbers it has seen in the row so far to ans
            ans += n - c - 1; 
            r++;
        }
        return ans;
    }
};


