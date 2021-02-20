// https://leetcode.com/problems/merge-intervals/

// Version 1 - Sort then applying the rules given
// Time complexity      O(nlogn)
// Space complexity     O(n)
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Sort in ascending order (comparing ends of interval if starts are the same)
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b){
            return a[0] < b[0];
        });
        
        vector<vector<int>> output{intervals[0]};
        
        int n = intervals.size();
        for (int i = 1; i < n; ++i){ 
            if (output.back()[1] >= intervals[i][0]){
                // If the end of the current interval is greater than the end of the next 
                // then completely absorb it
                output.back()[1] = max(output.back()[1], intervals[i][1]); 
            }
            else output.push_back(intervals[i]);
        }
        
        return output;
    }
};