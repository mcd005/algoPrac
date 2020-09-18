/*
https://leetcode.com/problems/running-sum-of-1d-array/

Easiest question on leetcode, just make sure you don't fail on an edge case
*/

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if (nums.size() > 1){
            for (int i = 1; i < nums.size(); i++){
                nums[i] += nums[i - 1];
            }
        }
        return nums;
    }
};