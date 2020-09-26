/*
https://leetcode.com/problems/insert-into-a-binary-search-tree/
 
Using the rules of a BST, traverse the tree
Once you are directed to an null node you know you have found the right spot, so insert the given node as a leaf

Time complexity     O(n)    average case O(logn)

Space complexity for recursive    O(n)    average case O(logn)
Space complexity for iterative    O(1)
*/

//Version 1 Recursive
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (root) {
            if (val > root->val) {
                if (root->right) {
                    insertIntoBST(root->right, val);
                }
                else {
                    root->right = new TreeNode(val);
                }
            }
            else {
                if (root->left) {
                    insertIntoBST(root->left, val);
                }
                else {
                    root->left = new TreeNode(val);
                }
            }
        }
        else {
            root = new TreeNode(val);
        }
        return root;
    }
};

//Version 2 Iterative
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            root = new TreeNode(val);
            return root;
        }
        TreeNode* cur = root;
        while (cur) {
            if (val > cur->val) {
                if (cur->right) {
                    cur = cur->right;
                }
                else {
                    cur->right = new TreeNode(val);
                    break;
                }
            }
            else {
                if (cur->left) {
                    cur = cur->left;
                }
                else {
                    cur->left = new TreeNode(val);
                    break;
                }
            }
        }
        return root;
    }
};

//Version 3 Iterative pointers to pointers. This is not mine but thought it was interesting to include
TreeNode* insertIntoBST(TreeNode* root, int val)
{
    TreeNode** cur = &root;
    while (*cur)
        cur = (val > (*cur)->val) ? &(*cur)->right : &(*cur)->left;
    *cur = new TreeNode(val);
    return root;
}