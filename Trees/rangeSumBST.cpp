/*
https://leetcode.com/problems/range-sum-of-bst/

Since the tree is a BST we can direct which way we need to traverse to find values between L and R

Time complexity		O(log n)
Space complexity	O(log n)
*/

class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(root){
            int sum = 0;
            if(root->val >= L && root->val <= R){
                sum += root->val;
            }
            if(root->val <= R){
                sum += rangeSumBST(root->right, L, R);
            }
            if(root->val >= L){
                sum += rangeSumBST(root->left, L, R);
            }
            return sum;
        }   
        else {
            return 0;
        }
    }
};

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */