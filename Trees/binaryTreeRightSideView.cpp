class Solution {
public:
    void bfs( TreeNode* r, int h, vector<int>& data){
        if(r == NULL){
            return;
        }
        if(r->left == NULL && r->right == NULL){
            data[h] = r->val;
            return;
        }
        data[h] = r->val;
        bfs( r->left,h+1, data);
        bfs(r->right,h+1, data);
    }
    
    vector<int> rightSideView(TreeNode* root) {
        if(root == NULL){
            return {};
        }
        vector<int> data(100,-101);
        bfs(root,0,data);
        while(data[data.size()-1] == -101){
            data.pop_back();
        }
        return data;
    }
};