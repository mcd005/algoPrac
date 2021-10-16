// Version 2 - Sort arr first, then count
// Time complexity      O(nlogn + n + mlogm + m)
// Space complexity      O(n + m)
class Solution
{
public:
    int findLeastNumOfUniqueInts(vector<int> &arr, int k)
    {
        sort(arr.begin(), arr.end());

        vector<int> counts;
        int n = arr.size(), currentNum = -1, currentCount = 0;
        for (int i = 0; i < n; ++i)
        {
            if (arr[i] != currentNum)
            {
                if (currentCount > 0) counts.push_back(currentCount);
                currentNum = arr[i];
                currentCount = 1;
            }
            else
            {
                ++currentCount;
            }
        }
        counts.push_back(currentCount);

        sort(counts.begin(), counts.end());
        int i = 0, m = counts.size();
        while (i < m)
        {
            k -= counts[i];
            if (k < 0) break;
            ++i;
        }
        return m - i;
    }
};

// Version 1 - Use a map as a counter
// Time complexity      O(n + n + mlog(min(m,k)) + m)
// Space complexity      O(n + m)
class Solution
{
public:
    int findLeastNumOfUniqueInts(vector<int> &arr, int k)
    {
        std::unordered_map<int, int> counts;
        for (auto &el : arr)
        {
            ++counts[el];
        }

        std::vector<int> count_vals;
        for (auto &kvp : counts)
        {
            count_vals.push_back(kvp.second);
        }
        int m = count_vals.size();
        std::partial_sort(count_vals.begin(), count_vals.begin() + min(k, m), count_vals.end());

        int i = 0;
        while (i < m)
        {
            k -= count_vals[i];
            if (k < 0) break;
            ++i;
        }
        return m - i;
    }
};

// [4,3,1,1,3,3,2], k = 3
// {4 : 1, 3: 3, 1: 2, 2: 1}
// [1 1 2 3]
//  |           k = 2
//    |         k = 1
//      |       k = -1
// Need to make a map of count
// Then sort on the values so the fewest occurring numbers are at the start of the map
// Then iterating from the start of the map you decrement k by the count of the current element
// When k hits zero you have no more elements to remove and that's how many uniques you have left