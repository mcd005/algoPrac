// https://leetcode.com/problems/product-of-array-except-self/
// Version 2
// product except self = product of all elements to the left * products of all elements to the right
// prefixProd represents elements to the left
// suffixProd represents elements to the right 
// Time complexity      O(n)
// Space complexity     O(n) if we include prefix
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixProd(n , 1);

        //if we wanted to account for n < 2
        if (n == 0 || n == 1) return {}; 

        for(int i = 0; i + 1 < n; ++i)
        {
          prefixProd[i + 1] = prefixProd[i] * nums[i];
        }

        int suffixProd = 1;

        for (int i = n - 1; i > -1; --i)
        {
            prefixProd[i] *= suffixProd;
            suffixProd *= nums[i];
        }

        return prefixProd;
    }
};

// Version 1 - Calculates product of whole array
// Accounts for zeros
// However uses division
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int idxOfZero = -1;
        
        int n = nums.size();
        for (int i = 0; i < n; ++i)
        {
            if (nums[i] == 0)
            {
                if (idxOfZero == -1) idxOfZero = i;
                else
                {
                    fill(nums.begin(), nums.end(), 0);
                    return nums;
                }
            }
            else product *= nums[i];
        }

        if (idxOfZero != -1)
        {
            fill(nums.begin(), nums.end(), 0);
            nums[idxOfZero] = product;
            return nums;
        }
        
        for (auto &n2: nums)
        {
            n2 = product / n2;
        }
        
        return nums;
    }
};