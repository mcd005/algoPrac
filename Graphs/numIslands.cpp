// https://leetcode.com/problems/number-of-islands/

// Version 1 - iterative BFS
// Iterate over the grid
// When you encounter an unmarked part of the island do a BFS
//      Add that coord to a q
//      Iterating through the q if a coord correpsonds to a 1 add it's neighbours to the q
// And so on until the q is empty and all the elements have been marked "#"

// Time complexity       O(n * m)
// Space complexity       O(n * m)
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;

        int rows = grid.size();
        int cols = grid[0].size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    queue <vector<int>> q;
                    vector<int> coords{ i , j };
                    q.push(coords);
                    while (!q.empty()) {
                        int r = q.front()[0];
                        int c = q.front()[1];
                        q.pop();
                        if ((r >= 0 && r < rows) && (c >= 0 && c < cols)) {
                            if (grid[r][c] == '1') {
                                grid[r][c] = '#';
                                vector<int> cd1{ r, c + 1 };
                                vector<int> cd2{ r + 1, c };
                                vector<int> cd3{ r, c - 1 };
                                vector<int> cd4{ r - 1, c };
                                q.push(cd1);
                                q.push(cd2);
                                q.push(cd3);
                                q.push(cd4);
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
};
