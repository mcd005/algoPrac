/*
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Because the tree is a BST you can do an in order traversal, starting from the rightmost node
And you can just accumulate the values of the nodes as you go along

Time complexity     O(n)
Space complexity    O(n)    if BST is unbalanced (basically the height of the tree)
*/

class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        int sum = 0;
        inOrder(root, sum);
        return root;
    }
    
    int inOrder(TreeNode* node, int sum){
        if (node){
            sum = inOrder(node->right, sum);
            sum += node->val;
            node->val = sum;
            sum = inOrder(node->left, sum);
        }
        return sum;
    }
};

/*

//Alternate solution

class Solution {
public:
    int pre = 0;
    TreeNode* bstToGst(TreeNode* root) {
        if (root->right) bstToGst(root->right);
        pre = root->val = pre + root->val;
        if (root->left) bstToGst(root->left);
        return root;
    }
};



