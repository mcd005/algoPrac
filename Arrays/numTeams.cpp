// https://leetcode.com/problems/count-number-of-teams/

// Version 1 - pointer to find ratings
// Time complexity      O(n^2)
// Space complexity     O(1)
// Unfortunately fairly slow, look for BIT solutions
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int count = 0;
        
        int n = rating.size();
        for (int j = 0; j < n; ++j){
            int leftSmaller = 0, leftLarger = 0;
            int rightSmaller = 0, rightLarger = 0;
            for (int i = 0; i < j; ++i){
                if (rating[i] < rating[j]) ++leftSmaller;
                else if (rating[i] > rating[j]) ++leftLarger;
            }
            for (int k = j; k < n; ++k){
                if (rating[j] > rating[k]) ++rightSmaller;
                else if (rating[j] < rating[k]) ++rightLarger;
            }
            count += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        
        return count;
    }
};