#include <math.h>

//The rolled out cpp version of my list comprehension python solution
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++){
            count += (int)(log10(nums[i])) % 2;
            }
        return count;
    }
};