// https://leetcode.com/problems/max-value-of-equation/
// Version 2 - Priority Queue
// Since i < j we can write yi + yj + |xi - xj| ---> yi - xi + yj + xj
// As we iterate through each point j we just need to find the maximum value of yi - xi 
// that also satisfies the constraint |xi - xj| <= k
// we can do this with a priority queue, with the top of the queue being the point with said max value
// Time complexity      O(n^2 + logn)
// Space complexity     O(n)
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        int currentMax = -200000001;
        
        priority_queue<pair<int, int>> q;

        int n = points.size();
        for (int j = 0; j < n; ++j)
        {
            while (!q.empty() && q.top().second < points[j][0] - k)
            {
                q.pop();
            }
            if (!q.empty()) currentMax = max(currentMax, points[j][0] + points[j][1] + q.top().first);
            q.push({points[j][1] - points[j][0], points[j][0]});
        }
        
        return currentMax;
    }
};

// Version 1 - Attempt a sliding window. Not suitable for this problem
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        int currentMax = -200000001;
        int n = points.size();
        int j = 1;
        for (int i = 0; i < n - 1; ++i)
        {
            if (i == j) ++j;
            while (j < n && abs(points[i][0] - points[j][0]) <= k) 
            {
                currentMax = max(currentMax, points[i][1] + points[j][1] + abs(points[i][0] - points[j][0]));
                ++j; 
            }
        }
        return currentMax;
    }
};