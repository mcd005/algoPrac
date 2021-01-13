/*
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

~~~Version 1~~~
Search helper function returns a vector which is the path from either a target node to the root
We generate these paths for both p and q and then compare vectors to see where the paths diverge
The node where they diverge is the LCA

The problem is the solution is slow (in ms) and memory intensive

Time complexity     O(n) 
Space complexity    O(n)


~~~Version 2~~~
A recursive function below which basically says:
    If this node has one of the targets (p or q) on its left branch
    and the other target on it's right
    then this node is the LCA

    Alternatively if this node has, say, p on one of its branches 
    but q is not on the other branch, 
    then p must be the LCA of both.

Time complexity         O(n)
Space complexity        O(n) 
in the worst case (degnerate linked list) but O(log n) on average 
since we only have recursive functions for one half of the tree on the callstack 
*/


//Version 2
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == q || root == p || !root) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        if (!left && !right) return nullptr;
        if (left && right) return root;
        return !left ? right : left;

    }
};

//Version 1
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> pPath = search(root, p);
        vector<TreeNode*> qPath = search(root, q);
	
        int i = pPath.size() - 1, j = qPath.size() - 1;
        
        while (i > 0 && j > 0){
            if (pPath[i] == qPath[j]){
                i--;
                j--;
            }
            else{
                return pPath[i + 1];
            }  
        }
        if (pPath[i] != qPath[j]){
            return pPath[i + 1];
        }
        else{
            return pPath[i];
        }
    }
    
    vector<TreeNode*> search(TreeNode* node, TreeNode* target){
        if (node){
            if (node != target){
                vector<TreeNode*> left = search(node->left, target);
                if (!left.empty()){
                    left.push_back(node);
                    return left;
                }
                vector<TreeNode*> right = search(node->right, target);
                if (!right.empty()){
                    right.push_back(node);
                    return right;
                }     
            }
            else{
                vector<TreeNode*> found{node};
                return found;
            }
        }
        return {};
    }
};




