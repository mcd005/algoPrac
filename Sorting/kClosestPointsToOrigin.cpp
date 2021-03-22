// https://leetcode.com/problems/k-closest-points-to-origin/

// Version 1 - 
// One pass to work out distances, appending them to points in input array
// Partial sort
// One pass to construct result vector
// Time complexity      O(n + n + klogk + k)
// Space complexity     O(n)
class Solution {
private:
    int distanceSquared(vector<int> coord)
    {
        return pow(coord[0], 2) + pow(coord[1], 2);
    }
    
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        vector<vector<int>> distMap;
        int n = points.size();
        for (int i = 0; i < n; ++i)
        {
            distMap.push_back({distanceSquared(points[i]), i});
        }
        
        std::partial_sort(distMap.begin(), 
                          distMap.begin() + k,
                          distMap.end(),
                          [](vector<int> &a, vector<int> &b)
                          {
                              return a[0] < b[0];
                          });
        
        
        vector<vector<int>> result;
        
        for (int i = 0; i < k; ++i)
        {
            result.push_back(points[distMap[i][1]]);
        }
        
        return result;                
    }
};

// Version 2 - A more sophisticated partial sort
// Time complexity    O(nlogk) worst case but O(n) average (depends on implementation of nth_element)
// Space complexity     O(n)
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K)
    {
        auto cmp = [](const auto & a, const auto & b) {
            return ((a[0] * a[0]) + (a[1] * a[1])) < ((b[1] * b[1]) + (b[0] * b[0]));
        };
        
        // Tnth_element changes the array such that. Lets call points.begin() + k, kth
        //      The element pointed at by kth is changed to whatever element would occur in that position if [first, last) 
        //      were sorted by the distances calculated by cmp
        //      All of the elements before this new kth element have distances less than or equal to the elements after the new kth element.
        nth_element(
            points.begin(),
            points.begin() + K,
            points.end(),
            cmp);

        return vector<vector<int>>(points.begin(), points.begin() + K);
    }
};