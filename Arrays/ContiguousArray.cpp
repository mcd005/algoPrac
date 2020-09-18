/*
This solution is currently incorrect
Doesn't work for 1010
At the moment assumes a contiguous subarray can't be in included in bigger subarrays
Hacky way could be to add them together
Maybe just need a different criteria for when to advance the rear pointer
*/

#include <algorithm> //For max

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        if (n == 0 || n == 1) return 0;
        
        int num0s = 0, num1s = 0; //Counters for zeroes and ones in a subarray
        int maxLength = 0;
           
        int front = 0; //front pointer
        for (int back = 0; back < n; back++){
            while (front < n){
                nums[front] ? num1s++ : num0s++;
                front++;
                if (num0s == num1s){
                    maxLength = max(maxLength, front - back);
                    break;
                }
            }
            nums[back] ? num1s-- : num0s--;
        }
        return maxLength;
    }
};
// doesn't work