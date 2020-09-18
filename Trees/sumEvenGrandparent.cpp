/*
Version 1

Essentially an adaptation of my fastest Python solution (see performance analysis there)
*/

class Solution {
public:
    int sumEvenGrandparent(TreeNode* root) {
        
        int result = 0;
        queue<TreeNode *> q;
        queue<int> p; //Q for parents
        queue<int> gp; //Q for grandparents
        
        q.push(root);
        p.push(NULL);
        gp.push(NULL);
            
        while (!q.empty()){
            TreeNode *node = q.front();
            int parent = p.front();
            
            cout << node->val << parent << gp.front() << endl;
            
            if (node->left != NULL){
                q.push(node->left);
                p.push(node->val);
                gp.push(parent);
            }
            if (node->right != NULL){
                q.push(node->right); 
                p.push(node->val);
                gp.push(parent);
            }
            if ((gp.front()%2 == 0) && (gp.front() > 0)){
                result += node->val;
            }
            
            q.pop();
            p.pop();
            gp.pop();
        }
        return result;
    }
};

/*
Alternate solution

Recursive way of passing the granparent, parent information to children. 
Won't lie, I found this in the Leetcode discussion for the question but it is pretty nutty
*/

class Solution {
public:
    int sumEvenGrandparent(TreeNode* root, int p = 1, int gp = 1) {
        return root ? sumEvenGrandparent(root->left, root->val, p) + sumEvenGrandparent(root->right, root->val, p) + (gp % 2 ? 0 : root->val)  : 0;
    }
};