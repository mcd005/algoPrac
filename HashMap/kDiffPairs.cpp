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