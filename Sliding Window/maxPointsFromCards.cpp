// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
// Time complexity      O(k) average O(n) worst case
// Space complexity     O(1)
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        if (n == k) return accumulate(cardPoints.begin(), cardPoints.end(), 0);
       
        // Take the sum of the first K elements as prefix 
        int prefix = 0;
        for (int i = 0; i < k; ++i)
        {
            prefix += cardPoints[i];
        }

        int suffix = 0;
        int result = prefix;

        // Sliding winding
        // For each iteration we close the window at the front of card points
        // And open it at the back
        // In doing do we get all k combinations
        int i = k - 1, j = n - 1;
        while (i > -1)
        {
            prefix -= cardPoints[i];
            suffix += cardPoints[j];
            result = max(result, prefix + suffix);
            --i;
            --j;
        }
        
        return result;
    }
};