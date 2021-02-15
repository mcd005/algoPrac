// https://leetcode.com/problems/minimum-time-difference/

// Version 1 - convert then sort
// Time complexity      O(nlogn)
// Space complexity     O(n)
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> tps;
        for (auto t: timePoints){
            // Using the ascii value of each digit
            // Convert each time into the number of minutes since the start of the day
            tps.push_back(( (t[0] - 48) * 10 + t[1] - 48) * 60 + //hrs
                            (t[3] - 48) * 10 + t[4] - 48);       //mins
        }
        
        sort(tps.begin(), tps.end());
        
        int minDiff = 12 * 60, curDiff = 12 * 60;
        int n = tps.size();
        for (int i = 0; i < n; ++i){
            // Iterate through the vector and and subtract each timepoint from the one in front of it
            if (i < n - 1){
                curDiff = tps[i + 1] - tps[i];
            }
            // For the final timepoint, assume that the one in front of it 
            // is the first timepoint but 24 hrs ahead (i.e. the day after the final tp)
            else curDiff = tps[0] + (24 * 60) - tps[i];
            minDiff = min(curDiff, minDiff);
        }
        
        return minDiff;
    }
};