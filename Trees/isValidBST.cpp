// Version 3 - Apply the rules of a BST recursively
// Time complexity       O(n)    
// Space complexity      O(h = logn)
// for n nodes
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        
        return  isValidBST(root->left) && 
                isValidBST(root->right) &&
                larger_than(root, root->left) && 
                smaller_than(root, root->right);
    }
    
    bool larger_than(TreeNode* root, TreeNode* left) {
        if (!root || !left) return true;
        return (root->val > left->val) && 
                larger_than(root, left->left) && 
                larger_than(root, left->right);
    }
    
    bool smaller_than(TreeNode* root, TreeNode* right) {
        if (!root || !right) return true;
        
        return (root->val < right->val) && 
                smaller_than(root, right->left) && 
                smaller_than(root, right->right);
    }
};

// Version 2 - Iterative inOrder traversal
// Time complexity       O(n)    
// Space complexity      O(h) average O(n) if degenerate LL
class Solution {
public:
    bool isValidBST(TreeNode* root) {
       stack<TreeNode*> s;
       TreeNode* pre = nullptr;
       while (root != NULL || !s.empty()) {
          while (root != NULL) {
             s.push(root);
             root = root->left;
          }
          root = s.top();
          s.pop();
          if(pre != NULL && root->val <= pre->val) return false;
          pre = root;
          root = root->right;
       }
       return true;
    } 
};

//Version 1 - inOrder traversal storing each node val in an array.
// Then checking the array is in the correct order
// Time complexity       O(n)    
// Space complexity      O(n)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        vector<int> vals;
        inOrder(root, vals);
        
        int n = vals.size();
        if (n == 1) return true;
        
        for (int i = 0; i < n - 1; ++i){
            if (vals[i] >= vals[i + 1]){
                return false;
            }
        }
        
        return true;
    }
    
    void inOrder(TreeNode* root, vector<int> &vals){
        if (root){
            inOrder(root->left, vals);
            vals.push_back(root->val);
            inOrder(root->right, vals);
        }
    }
};

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */