/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
An emulation of the list comprehension methodn used in my python solution

Starting with the a queue that just has the root in it
Use n to keep track of all the nodes at that level
Iterate through all the nodes at their level, adding their children to the next q
If the node doesn't have children you know it's a leaf, so you add its value to sum
You only return this value of sum, however, when you none of the leaves at a level have children
	(i.e. they are the deepest leaves)
Hence the deepest leaves sum is returned

Time complexity 	O(n)
Space complexity	O(log n)
*/

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        queue <TreeNode*> q;
        q.push(root);
        int sum = 0;
        while (!q.empty()){
            int n = q.size();
            sum = 0;
            while (n--){
                cout << sum << endl;
                TreeNode* node = q.front(); q.pop();
                if (node->left){
                    q.push(node->left);
                }
                if (node->right){
                    q.push(node->right);
                }
                if(!node->left && !node->left){
                    sum += node->val;
                }
            }
        }
        return sum;
    }
};

/*
//This a tidier version of my logic

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        int res = 0, i;
        queue<TreeNode*> q;
        q.push(root);
        while (q.size()) {
            for (i = q.size() - 1, res = 0; i >= 0; --i) { //Reinitialise res to 0
                TreeNode* node = q.front(); q.pop();
                res += node->val;
                if (node->right) q.push(node->right);
                if (node->left)  q.push(node->left);
            }
        }
        return res;
    }
};
*/