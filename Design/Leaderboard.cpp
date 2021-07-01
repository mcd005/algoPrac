// https://leetcode.com/problems/design-a-leaderboard/submissions/

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */

// Version 1
// Function  |  Time Complexity  |  Space Complexity
// --------------------------------------------------
// addScore          O(1)                 O(n)
// top               O(n + nlogK)         O(n)
// reset             O(1)                 O(n)
class Leaderboard
{
public:
    Leaderboard() : map(10000, 0) {}

    void addScore(int playerId, int score)
    {
        map[playerId - 1] += score;
        maxID = max(playerId - 1, maxID);
    }

    int top(int K)
    {
        // Copy only the part of the vector that's populated
        vector<int> copy(map.begin(), map.begin() + maxID + 1);
        // Sort so first K elements are the largest
        partial_sort(copy.begin(), copy.begin() + K, copy.end(), greater<int>());
        // Sum those elements
        return accumulate(copy.begin(), copy.begin() + K, 0);
    }

    void reset(int playerId)
    {
        map[playerId - 1] = 0;
    }

private:
    vector<int> map;
    int maxID = -1;
};


// Version 2
// Function  |  Time Complexity  |  Space Complexity
// --------------------------------------------------
// addScore          O(logn)             O(n)
// top               O(K)                O(n)
// reset             O(logn)             O(n)
class Leaderboard
{
private:
    unordered_map<int, int> index;
    multiset<int> scores;

public:
    Leaderboard() {}

    void addScore(int playerId, int score)
    {
        if (index.count(playerId) >= 1)
        {
            scores.erase(scores.lower_bound(index[playerId])); // remove previous score held by playerId
        }
        index[playerId] += score;
        scores.insert(index[playerId]); // add new score
    }

    int top(int K)
    {
        int sum = 0;
        // A multiset maintains an asc order. Iterate backward through it K times for the K greatest scores
        for (auto it = scores.rbegin(); it != scores.rend() && K-- > 0; it++)
            sum += *it;
        return sum;
    }

    void reset(int playerId)
    {
        scores.erase(scores.lower_bound(index[playerId]));
        index[playerId] = 0;
    }
};
