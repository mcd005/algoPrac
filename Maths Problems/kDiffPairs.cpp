// https://leetcode.com/problems/k-diff-pairs-in-an-array/

//Version 2 - presort
// Before we made the assumtion that nums[i] - nums[j] == +- k
// however since k > 0 we only need to check for +k

// Time complexity          O(nlogn)      but faster in ms compared to V1
// Space complexity         O(1)
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        
        // Presorting the array and using us two pointers allows us to check for all possible diffs in linear time
        sort(nums.begin(), nums.end());
        
        int l = 0, r = 1;
        int n = nums.size();
        int numPairs = 0;
        
        while(l < n && r < n) {
            // If our current diff is greater than k we need nums[l] to be bigger; we advance the left pointer
            if(nums[r] - nums[l] > k){
                ++l;
            }
            // Vice versa for if diff less than k. We also don't want left to be bigger than right
            else if(l == r || nums[r] - nums[l] < k){
                ++r;
            }
            // We've found Diff == k
            else {
                ++numPairs;
                ++l;
                // Because we now found the pair (nums[l], nums[r])
                // we skip the rest of nums with value == nums[l]
                // Because they won't yield unique pairs
                while(l < n && nums[l] == nums[l-1]) ++l; 
            }
        }
        
        return numPairs;
    }
};

//Version 1 - two sets
// Time complexity          O(n)
// Space complexity         O(n)
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int numPairs = 0;
        
        set<int> targets;
        set<vector<int>> pairsSeen;
        
        int n = nums.size();
        for (int i = 0; i < n; ++i){
            
            vector<int> hi{nums[i], nums[i] + k};
            vector<int> lo{nums[i] - k, nums[i]};
            
            if (targets.find(hi[1]) != targets.end() && pairsSeen.find(hi) == pairsSeen.end()){
                ++numPairs;
                pairsSeen.insert(hi);
            }
            if (targets.find(lo[0]) != targets.end() && pairsSeen.find(lo) == pairsSeen.end()){
                ++numPairs;
                pairsSeen.insert(lo);
            }
            targets.insert(nums[i]);
        }
        
        return numPairs;
    }
};