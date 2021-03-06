// https://leetcode.com/problems/design-tic-tac-toe/
// Version 1 - O(1) checking 
// by keeping track of cols and rows
// Time complexity      O(m)
// Space complexity     O(n)
// where m is number of moves
class TicTacToe {
public:
    TicTacToe(int n) : sz(n) {
        rows.resize(n, 0), cols.resize(n, 0);
        leadDiag = otherDiag = 0;
    }
    
    int move(int row, int col, int player) {
        if (player == 1) {
            ++rows[row], ++cols[col];
            if (row == col)
                ++leadDiag;
            if (row == sz - 1 - col)
                ++otherDiag;
            if (rows[row] == sz || cols[col] == sz || leadDiag == sz || otherDiag == sz)
                return 1;
        }
        else {
            --rows[row], --cols[col];
            if (row == col)
                --leadDiag;
            if (row == sz - 1 - col)
                --otherDiag;
            if (rows[row] == -sz || cols[col] == -sz || leadDiag == -sz || otherDiag == -sz)
                return 2;
        }
        return 0;
    }

private:
    vector<int> rows, cols;
    int leadDiag, otherDiag;
    int sz;
};