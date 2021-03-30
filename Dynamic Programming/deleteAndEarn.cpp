// https://leetcode.com/problems/delete-and-earn/

// Version 1
// We use an ordered map to create a counter {num : countOfNum} (num is asc)
// Then we create a dp array of that is the same length as counter
// We set dp[0] = counter[0] is for the first value
// We then iterate through counter, starting from counter[1]
// If counters next key = counters + 1
//      dp[i] = max(dp[i - 1], counters[i] + dp[i - 2])
// else dp[i] = dp[i - 1] + counters[i]
// Since we only ever need dp[i - 1] and dp[i - 2]
// we don't need an array and instead use 
// cur = dp[i]
// pre = dp[i - 1]
// prePre = dp[i - 2]
// Time complexity      O(nlogn)
// Space complexity     O(n)
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        std::map<int, int> counter;
        
        for (auto num: nums)
        {
            if (counter.find(num) != counter.end())
            {
                counter[num] += num;
            }
            else counter[num] = num;
        }

        int prePre = 0;
        int pre = counter.begin()->second;
        int cur;
        for (auto it = next(counter.begin()); it != counter.end(); ++it)
        {
            if (it->first > prev(it)->first + 1)
            {
                cur = pre + it->second;
            }
            else
            {
                cur = max(pre, prePre + it->second);
            }
            prePre = pre;
            pre = cur;
        }

        return pre;
    }
};
