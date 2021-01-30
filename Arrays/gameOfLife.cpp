// https://leetcode.com/problems/game-of-life

// Version 1 - modify in place
// 0 = 0 now
// 1 = 1 now
// 2 = 0 now 1 next
// 3 = 1 now 0 next
// Then make a second pass and translate
// Time complexity      O(m * n)
// Space complexity     O(1)  
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        
        for (int pass = 0; pass < 2; ++pass){
            for (int i = 0; i < m; ++i){
                for (int j = 0; j < n; ++j){
                    if (pass == 0){
                        int numLiveNeighbs = countLiveNeighbours(board, i, j, m, n);
                        if (board[i][j] && (numLiveNeighbs < 2 || numLiveNeighbs > 3)) board[i][j] = 3;
                        else if (!board[i][j] && numLiveNeighbs == 3) board[i][j] = 2;
                    }
                    else{
                        if (board[i][j] == 2) board[i][j] = 1;
                        else if (board[i][j] == 3) board[i][j] = 0;
                    }
                }
            }
        }
    }
    
    int countLiveNeighbours(vector<vector<int>>& board, int i, int j, int m, int n){
        int sum = 0;
        
        vector<vector<int>> neighbCoords{
        {i - 1, j - 1}, {i - 1, j}, {i - 1, j + 1},
        {i, j - 1}, {i, j + 1},
        {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}
        };
        
        for (auto nbc : neighbCoords){
            if (0 <= nbc[0] && nbc[0] < m &&
                0 <= nbc[1] && nbc[1] < n &&
                board[nbc[0]][nbc[1]] % 2 == 1)
                ++sum;
        }
        
        return sum;
    }
};

