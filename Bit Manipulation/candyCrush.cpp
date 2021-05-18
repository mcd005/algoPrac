// Version 2 - Use two pointers to iterate over rows and cols crushing candies
// Use bitmasking to mark candies to be crushed
// Use two pointers again to actually crush the candies

// For all algos:
// Time complexity      O(n*m)
// Space complexity     O(1)
class Solution
{
public:
    vector<vector<int>> candyCrush(vector<vector<int>> &board)
    {
        N = board.size(), M = board[0].size();
        while (!isBoardStable)
        {
            isBoardStable = true;
            crushCandiesInRows(board);
            crushCandiesInCols(board);
            dropCandies(board);
        }

        return board;
    }

private:
    bool isBoardStable = false;
    int N, M;

    void crushCandiesInRows(vector<vector<int>>& board)
    {
        for (int i = 0; i < N; ++i)
        {

            bool isCrushable = false;
            int slow = 0, fast = 0;
            while (slow < M)
            {
                if (board[i][slow] == 0) ++slow, ++fast;
                else if (fast < M && board[i][slow] == board[i][fast])
                {
                    ++fast;
                    isCrushable = (fast - slow) >= 3;
                } 
                else 
                {
                    board[i][slow] += 0x1000 * isCrushable;
                    ++slow;
                    if (isCrushable) isBoardStable = false;
                }
            }
        }
    }

    void crushCandiesInCols(vector<vector<int>>& board)
    {
        for (int j = 0; j < M; ++j)
        {

            bool isCrushable = false;
            int slow = 0, fast = 0;
            while (slow < N)
            {
                if (board[slow][j] == 0) ++slow, ++fast;
                else if (fast < N && (board[slow][j] & 0xFFF) == (board[fast][j] & 0xFFF))
                {
                    ++fast;
                    isCrushable = (fast - slow) >= 3;
                } 
                else 
                {
                    board[slow][j] |= 0x1000 * isCrushable;
                    ++slow;
                    if (isCrushable) isBoardStable = false;
                }
            }
        }
    }

    void dropCandies(vector<vector<int>>& board)
    {
        for (int j = 0; j < M; ++j)
        {
            int read = N - 1, write = N - 1;
            while (read >= 0)
            {
                if (board[read][j] != 0 && (board[read][j] & 0x1000) != 0x1000)
                {
                    board[write][j] = board[read][j];
                    --write;
                }
                --read;
            }
            while (write >= 0)
            {
                board[write][j] = 0;
                --write;
            }
        }
    }

};

// Version 3 - From LC
// Mark candies to be crushed by making them negative, but read abs values
// Rather than two pointer to determine crushed candies, just read all possible consecutive rows and cols of three
// Then recursively call candyCrush on board if candies were just crushed (i.e. unstable)
class Solution
{
public:
    vector<vector<int>> candyCrush(vector<vector<int>> &board)
    {
        const int row = board.size();
        const int col = board[0].size();

        bool needToCrush = false;

        for (int i = 0; i < row - 2; ++i)
        {
            for (int j = 0; j < col; ++j)
            {
                int val = abs(board[i][j]);
                if (val > 0 && (abs(board[i + 1][j]) == val) && (abs(board[i + 2][j]) == val))
                {
                    board[i][j] = -val;
                    board[i + 1][j] = -val;
                    board[i + 2][j] = -val;
                    needToCrush = true;
                }
            }
        }

        for (int i = 0; i < row; ++i)
        {
            for (int j = 0; j < col - 2; ++j)
            {
                int val = abs(board[i][j]);
                if (val > 0 && (abs(board[i][j + 1]) == val) && (abs(board[i][j + 2]) == val))
                {
                    board[i][j] = -val;
                    board[i][j + 1] = -val;
                    board[i][j + 2] = -val;
                    needToCrush = true;
                }
            }
        }

        for (int i = 0; i < col; ++i)
        {
            int writeRow = row - 1;
            for (int r = row - 1; r >= 0; --r)
            {
                if (board[r][i] > 0)
                {
                    board[writeRow--][i] = board[r][i];
                }
            }

            while (writeRow >= 0)
            {
                board[writeRow--][i] = 0;
            }
        }

        return needToCrush ? candyCrush(board) : board;
    }
};

// Version 1 - Attempt at Recursive DFS to tell which candies to crush. Currently not working
class Solution
{
public:
    vector<vector<int>> candyCrush(vector<vector<int>> &board)
    {
        N = board.size(), M = board[0].size();
        while (!isBoardStable)
        {
            isBoardStable = true;
            crushCandies(board);
            dropCandies(board);
        }

        return board;
    }

private:
    bool isBoardStable = false;
    int N, M;

    void crushCandies(vector<vector<int>>& board)
    {
            for (int i = 0; i < N; ++i)
            {
                for (int j = 0; j < M; ++j)
                {
                    if (board[i][j] != 0)
                    {
                        checkIfCrushableRow(board, i, j, 0, board[i][j]);
                        checkIfCrushableCol(board, i, j, 0, board[i][j]);
                    }
                }
            }
    }

    void dropCandies(vector<vector<int>>& board)
    {
        for (int j = 0; j < M; ++j)
        {
            int read = N - 1, write = N - 1;
            while (read >= 0)
            {
                if (board[read][j] != 0)
                {
                    board[write][j] = board[read][j];
                    --write;
                }
                --read;
            }
            while (write >= 0)
            {
                board[write][j] = 0;
                --write;
            }
        }
    }

    bool checkIfCrushableRow(vector<vector<int>>& board, int r, int c, int numAdj, int prevCandyType)
    {
        if (r >= N || c >= M || board[r][c] != prevCandyType)
        {
            return numAdj >= 3;
        }
        bool isCrushableRow = checkIfCrushableRow(board, r, c + 1, numAdj + 1, prevCandyType);
        bool isCrushableCol = checkIfCrushableCol(board, r + 1, c, 1, prevCandyType);
        if (isCrushableRow || isCrushableCol)
        {
            board[r][c] = 0;
            isBoardStable = false;
        }
        return isCrushableRow;
    }

    bool checkIfCrushableCol(vector<vector<int>>& board, int r, int c, int numAdj, int prevCandyType)
    {
        if (r >= N || c >= M || board[r][c] != prevCandyType)
        {
            return numAdj >= 3;
        }
        bool isCrushableCol = checkIfCrushableCol(board, r + 1, c, numAdj + 1, prevCandyType);
        bool isCrushableRow = checkIfCrushableRow(board, r, c + 1, 1, prevCandyType);
        if (isCrushableCol || isCrushableRow)
        {
            board[r][c] = 0;
            isBoardStable = false;
        }
        return isCrushableCol;
    }
};
