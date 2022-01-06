class Solution
{
public:
    int unhappyFriends(int n, vector<vector<int>> &preferences, vector<vector<int>> &pairs)
    {
        int rank[n][n];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < (n - 1); j++)
            {
                arr[i][preferences[i][j]] = j;
            }
        }

        int pair[n];
        for (int i = 0; i < (n / 2); i++)
        {
            pair[pairs[i][0]] = pairs[i][1];
            pair[pairs[i][1]] = pairs[i][0];
        }

        int res = 0, idx, val;
        for (int i = 0; i < n; i++)
        {
            idx = arr[i][pair[i]];
            for (int j = 0; j < idx; j++)
            {
                val = preferences[i][j];
                if (arr[val][pair[val]] > arr[val][i])
                {
                    res++;
                    break;
                }
            }
        }
        return res;
    }
};