// https://leetcode.com/problems/minimum-knight-moves/
// Version 2 - Constant time solution
// You can see predictable patterns emerge in the dp table
// The numbers from the patterns can be turned into the formula below
class Solution
{
public:
    vector<vector<int>> localRegion = {
        {0, 3, 2},
        {3, 2, 1},
        {2, 1, 4}};

    int minKnightMoves(int x, int y)
    {
        x = abs(x);
        y = abs(y);
        if (x < y) std::swap(x, y);

        if (x <= 2 && y <= 2) return localRegion[x][y];

        int groupId;
        if ((x - 3) >= (y - 3) * 2) groupId = (x - 1) / 2 + 1;
        else groupId = (x + y - 2) / 3 + 1;
        return groupId + ((x + y + groupId) % 2);
    }
};

// Version 1 - DP
// We have a table dp[y][x] which gives the min number of moves to get to x, y from 0, 0
// This is general is given by min(dp[y - 2][x - 1], dp[y - 1][x - 1]) + 1
// However there are edge cases for when y < 2
// When we are assigning dp[y][x] we can also set dp[x][y] equal to that value as well
// This allows us to iterate up to the leading diagonal
// Time complexity      O(x * y)
// Space complexity     O(x * y)
class Solution
{
public:
    int minKnightMoves(int x, int y)
    {
        x = abs(x);
        y = abs(y);
        if (x <= 2 && y <= 2) return dp[y][x];

        int n = max(x, y);
        for (int i = 0; i < 3; ++i)
        {
            dp[i].resize(n + 1);
        }
        dp.resize(n + 1, vector<int>(n + 1));

        for (int xi = 3; xi <= n; ++xi)
        {
            for (int yi = 0; yi <= xi; ++yi)
            {
                if (yi == 0) updateDP(xi, yi, dp[yi + 1][xi - 2] + 1);
                else if (yi == 1) updateDP(xi, yi, min(dp[yi - 1][xi - 2], dp[yi + 1][xi - 2]) + 1);
                else updateDP(xi, yi, min(dp[yi - 2][xi - 1], dp[yi - 1][xi - 2]) + 1);
                if ((xi == x && yi == y) || (xi == y && yi == x)) return dp[yi][xi];
            }
        }
        return dp[y][x];
    }
private:
    vector<vector<int>> dp = {
        {0, 3, 2},
        {3, 2, 1},
        {2, 1, 4}
    };

    void updateDP(int xi, int yi, int val)
    {
        dp[yi][xi] = val;
        dp[xi][yi] = val;
    }
};


// Version 2 - BFS. Currently not working
class Solution
{
private:
    vector<vector<int>> directions = {{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
public:
    int minKnightMoves(int x, int y)
    {
        x = abs(x);
        y = abs(y);

        queue<vector<int>> q;
        q.push({0 , 0});

        std::unordered_set<string> visited;

        int result = 0;
        while (!q.empty())
        {
            int n = q.size();
            for (int i = 0; i < n; ++i)
            {
                vector<int> cur = q.front();
                q.pop();
                if (cur[0] == x && cur[1] == y) return result;

                visited.insert(std::to_string(cur[0]) + std::to_string(cur[1]));

                for (auto& dir : directions)
                {
                    int newX = cur[0] + dir[0];
                    int newY = cur[1] + dir[1];
                    if (visited.count(std::to_string(newX) + std::to_string(newY)) == 0 && newX >= -1 && newY >= -1)
                    {
                        q.push({newX, newY});
                    }
                }
            }
            ++result;
        }
        return -1;
    }
};

// Each hop either takes you 2x and 1y closer or 2y and 1x closer
// We will take some combination of horizontal and vertical hops until we are in the neigbhourhood, then we possibly
// We need to taek (2x + y)n + (x + 2y)m = Tx + Ty
