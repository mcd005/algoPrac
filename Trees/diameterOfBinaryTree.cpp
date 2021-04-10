// https://leetcode.com/problems/diameter-of-binary-tree/
// For each node we ask, how deep are your deepest left and deepest right leaves
// If the sum of of those values is a path greater than the longest seen so far store it
// Time complexity      O(n)
// Space complexity     O(n) worst O(h = logn) average 
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int longestPathNotThroughRoot = 0;
        return max(getDeepest(root->left, longestPathNotThroughRoot) + getDeepest(root->right, longestPathNotThroughRoot),
                   longestPathNotThroughRoot);
    }

    int getDeepest(TreeNode* root, int &lpntr)
    {
        if (root)
        {
            int leftDepth = getDeepest(root->left, lpntr);
            int rightDepth = getDeepest(root->right, lpntr);
            lpntr = max(leftDepth + rightDepth, lpntr);
            return 1 + max(leftDepth, rightDepth);
        }
        return 0;
    }
};
