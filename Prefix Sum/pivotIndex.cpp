// https://leetcode.com/problems/find-pivot-index/

// Version 1 - left and right sum
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return -1;
        
        int left = 0;
        int right = accumulate(nums.begin() + 1, nums.end(), 0);
        
        for (int i = 0; i < n; ++i){
            if (left == right) return i;
            left += nums[i];
            right -= nums[i + 1];
        }
        
        return -1; 
    }
};

// Version 2
// Here we sum "right" ourselves rather than using accumulate.
// It's faster but less concise
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return -1;
        
        int left = 0;
        int right = 0;
        for (int i = 1; i < n; ++i){
            right += nums[i];
        }
        
        for (int i = 0; i < n; ++i){
            if (left == right) return i;
            left += nums[i];
            right -= nums[i + 1];
        }
        
        return -1; 
    }
};