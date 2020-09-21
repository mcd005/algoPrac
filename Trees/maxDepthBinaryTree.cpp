/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

First solution is recursive and is kind of like asking: "How deep is the left branch? Is that deeper than the right branch?"
This continues until a base case of a null node

Time complexity 	O(n)  	have to traverse all the nodes
Space complexity	O(n)	in the worse case (degenerated linked list) there will be n recursive function calls on the stack

Second is iterative. Level order traversal, keeping track of the levels by saving the size of the queue holding the nodes at each level

Time complexity 	O(n)
Space complexity	O(n)
*/

#include <bits/stdc++.h>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root){
            return max(1 + maxDepth(root->left), 1 + maxDepth(root->right));
        }
        return 0;
    }
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        
        std::queue<TreeNode*> q;
        q.push(root);
        int lvl = 0;
        
        while (!q.empty()){
            int n = q.size();
            while (n--){
                TreeNode* cur = q.front();
                q.pop();
                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }
            lvl++;
        }
        
        return lvl;
    }
};