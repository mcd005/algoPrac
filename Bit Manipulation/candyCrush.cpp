// Version 2 - Use two pointers to iterate over rows and cols crushing candies
// Use bitmasking to mark candies to be crushed
// Use two pointers again to actually crush the candies
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

/* 
Need to first establish which candies are to be crushed
    Probably some kind of DFS, where you see how many are adjacent
    ans set current to 0 if adjacent gte 3
    Will also need to check non-zero
    Was going to do two pointers but if you delete some while it may mean other candies are not crused at the right time    

Then need to iterate over the board and move candies to be dropped
    Two pointer bottom to top would be better
    Both pointers start at the bottom, a write head and a fast read head
    When read points to non-zero, put the value at read at write and iterate both pointers
    If read is at a zero, iterate until it's at a non zero
    If read is at the end, then iterate write, writing zeros

And repeat until there are no more candies to drop or crush
    Set a numCrushed and numDroppe??

See how abstracting it/refactoring affects performance

Is crushable row
Base case is out of bounds or different char
Return adjcent greater than 3
When you call vertical on a horizontal Nim adjacent should be zero
What happens if you encounter a massive block
If you start zeroing out will it cut off some sections


Start with both pointers at start of row
Increment the right pointer, whilst the two values are the same
When the two values are not the same check the number of elements between the two pointers
If it's greater than 3 you can mark all the elements with a bit
Since all elements on the board are 2000 or less, you can mark elements for deletion by adding 0x1000
When reading for original values bitmask OxFFF

When it comes to deletion, iterate over and if bitmased 0x1000 = 0x1000 then treat as zero
*/