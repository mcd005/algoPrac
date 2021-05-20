// https://leetcode.com/problems/count-square-submatrices-with-all-ones/submissions/

// Version 2 - DP memoisation
// We convert matrix[i][j] into dp[i][j]
// which represents the number of squares whose bottom right corner are in matrix[i][j]
// This cell can only be the bottom right corner of a square if all it's neighbours are non-zero
// The size of the square is the min of the neighbours
// Time complexity      O(n^m)
// Space complexity     O(1)
class Solution
{
public:
    int countSquares(vector<vector<int>> &matrix)
    {
        int result = 0;

        int n = matrix.size(), m = matrix[0].size();
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (matrix[i][j] == 1)
                    if (i == 0 || j == 0)
                    {
                        ++result;
                    }
                    else
                    {
                        int cellValue = min({matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]}) + 1 ;
                        result += cellValue;
                        matrix[i][j] = cellValue;
                    }
            }
        }
        return result;
    }
};

// Version 1 - Recursive BFS. Quite slow though
// Iterate over the grid
// Once we find a cell with a 1, we call bfs() and check the cells in the following fashion
//
// 1 * --->  1 1 * --->  1 1 1 *
// * !       1 1 *       1 1 1 *
//           * * !       1 1 1 *
//                       * * * !
//
// Using the ! as an origin, the BFS iterates over the * cells
// if ! is out of range
// or that layer contains a 0
// then that layer is invalid and we stop the BFS
// otherwise  we can keep adding layers, and do so until we find an invalid layer
// Time complexity      O((n^m)^4)
// Space complexity     O(min(n, m))
class Solution
{
private:
    int N, M;
public:
    int countSquares(vector<vector<int>> &matrix)
    {
        int result = 0;

        N = matrix.size(), M = matrix[0].size();
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                if (matrix[i][j] == 1)
                {
                    result += bfs(matrix, i, j, 1);
                }
           }
        }

        return result;
    }

    int bfs(vector<vector<int>>& matrix, int r0, int c0, int sideLength)
    {
        if (r0 >= N || c0 >= M) return 0;
        for (int offset = 0; offset < sideLength; ++offset)
        {
            if (matrix[r0 - offset][c0] == 0 || matrix[r0][c0 - offset] == 0) return 0;
        }
        return 1 + bfs(matrix, r0 + 1, c0 + 1, sideLength + 1);
    }
};
