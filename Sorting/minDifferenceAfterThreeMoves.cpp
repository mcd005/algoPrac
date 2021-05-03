// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
// Version 2 - Partial sort. See V1 for explanation.
// Time complexity      O(nlog(4))  -->  O(n)
// Space complexity     O(4)        -->  O(1)
// In general for m moves the time complexity   is O(nlog(m + 1))
class Solution
{
public:
    int minDifference(vector<int> &nums)
    {
        int n = nums.size();
        if (n <= 4) return 0;

        partial_sort(nums.begin(), nums.begin() + 4, nums.end());
        vector<int> k_smallest(nums.begin(), nums.begin() + 4);
        partial_sort(nums.begin(), nums.begin() + 4, nums.end(), greater<int>());

        int result = nums[0] - k_smallest[0];
        for (int i = 3; i >= 0; --i)
        {
            result = min(result, nums[3 - i] - k_smallest[i]);
        }
        return result;
    }
};

// Version 1 - Full sort the array
// You can either change the smallest three so they match the biggest
// Or change the biggest three so they match the smallest
// Or any combination in between (4 combos total)
// If you were manually changing the first three
//     the smallest element in the new array would be element at index 3
//     and the biggest would still be the one at index n-1
// So if you start at index 3 and n-1 and iterate backward 4 times
// Comparing the difference between the values at those two indices
// It's the same as changing the values per all the combinations
// Time complexity      O(nlogn)
// Space complexity     O(1)
class Solution
{
public:
    int minDifference(vector<int> &nums)
    {
        int n = nums.size();
        if (n <= 4) return 0;

        sort(nums.begin(), nums.end());
        int result = nums[n - 1] - nums[0];
        for (int i = 3; i >= 0; --i)
        {
            result = min(result, nums[n - 4 + i] - nums[i]);
        }
        return result;
    }
};