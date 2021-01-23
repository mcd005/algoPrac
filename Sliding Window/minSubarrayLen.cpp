// https://leetcode.com/problems/minimum-size-subarray-sum/

// Version 1 - Two pointers
// Time Complexity      O(n)
// Space Complexity     O(1)
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        // Any valid contiguous array will have a len
        // less than this value, so if we check minSize
        // at the end and it's not less than this value
        // we know we have no valid subarrays
        int minSize = n + 1;
        int subSum = nums[0];
        
        int l = 0, r = 0;
        while (l < n){
            if (subSum >= s){
                minSize = min(r - l + 1, minSize);
                subSum -= nums[l];
                ++l;
            }
            else if (r < n - 1 && (l >= r || subSum < s)){
                ++r;
                subSum += nums[r];
            }
            // Either both l, r are at the end of the array
            // Or just r is but subSum is less than s and 
            // there are no more elements to add to it to make it bigger; cut our losses
            else break; 
        }
        return (minSize < n + 1) ? minSize : 0;
    }
};