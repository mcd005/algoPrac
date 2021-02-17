// https://leetcode.com/problems/flood-fill
// Version 1 - Classic grid DFS
// Time complexity      O(n*m)
// Space complexity     O(n*m)
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int n = image.size(), m = image[0].size();
        helper(image, sr, sc, n, m, newColor);
        return image;
    }
    
    void helper(vector<vector<int>>& image, int sr, int sc, int maxR, int maxC, int newColor){
        int startColor = image[sr][sc];
        if (newColor == startColor) return; //We'd be DFSing forever in cases where newColour == startColour
        image[sr][sc] = newColor;
        if (sr - 1 >= 0 && image[sr - 1][sc] == startColor)
            helper(image, sr - 1, sc, maxR, maxC, newColor);
        if (sc + 1 < maxC && image[sr][sc + 1] == startColor)
            helper(image, sr, sc + 1, maxR, maxC, newColor);
        if (sr + 1 < maxR && image[sr + 1][sc] == startColor)
            helper(image, sr + 1, sc, maxR, maxC, newColor);
        if (sc - 1 >= 0 && image[sr][sc - 1] == startColor)
            helper(image, sr, sc - 1, maxR, maxC, newColor);
    }
};
