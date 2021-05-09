// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/

/*
Iterate through the the array
    Take 60 - (time[i] % 60)
        If that key is in the map, increment numPairs by the value that corresponds to
    Increment time[i] % 60 by 1
*/

// Version 2 - Using a vector 
// Time complexity      O(n)
// Space complexity     O(n)
class Solution
{
public:
    int numPairsDivisibleBy60(vector<int> &time)
    {
        int numPairs = 0;
        vector<int> durationCount(60, 0); //Constant space - 60
        for (auto t : time)
        {
            int curr = t % 60;
            numPairs += (curr == 0 ? durationCount[0] : durationCount[60 - curr]);
            durationCount[curr]++;
        }
        return numPairs;
    }
};

// Version 1 - Unordered_map
// Time complexity      O(n)
// Space complexity     O(n)
class Solution
{
public:
    int numPairsDivisibleBy60(vector<int> &time)
    {
        int numPairs = 0;
        unordered_map<int, int> durationCount;

        for (auto t: time)
        {
            int currentDuration = t % 60;
            if (durationCount.find(60 - currentDuration) != durationCount.end())
            {
                numPairs += durationCount[60 - currentDuration];
            }
            ++durationCount[currentDuration + 60 * (currentDuration == 0)];
        }

        return numPairs;
    }
};
