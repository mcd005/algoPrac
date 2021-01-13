/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

Version 1 - iterative
Level order traversal, 
Keeping track of the levels by saving the size of the queue holding the nodes at each level

Time complexity 	O(n)
Space complexity	O(n)

Version 2 - Recursive
This is kind of like asking: "How deep is the left branch? Is that deeper than the right branch?"
This continues until a base case of a null node

Time complexity 	O(n)  	have to traverse all the nodes
Space complexity	O(n)	in the worse case (degenerated linked list) there will be n recursive function calls on the stack
*/

#include <bits/stdc++.h>

// Version 2
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root){
            return max(1 + maxDepth(root->left), 1 + maxDepth(root->right));
        }
        return 0;
    }
};

// Version 1
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