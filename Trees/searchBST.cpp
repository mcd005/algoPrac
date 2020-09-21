/*
https://leetcode.com/problems/search-in-a-binary-search-tree

Because the tree is a BST we can direct our search. We only traverse the left or right branches of a the current node based on it's value compared to the target
Traversal is done recursively

Time complexity		O(n)	average search takes logn but if it is a degenerate linked list then will have to traverse all the nodes
Space complexity	O(n)	same as above with recursive functions on the call stack
*/

class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root){
            if (root->val == val){
                return root;
            }
            else if (root->val > val){
                return searchBST(root->left, val);
            }
            else if (root->val < val){
                return searchBST(root->right, val);
            }
        }
        return NULL;
    }
};