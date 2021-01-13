/*
https://www.hackerrank.com/challenges/swap-nodes-algo/

We need to:
Convert the 2D array into a tree
Then for as many times as there are queries
    Level order traverse the tree keeping track of depth
    Swap at the appropriate levels
    After each swap carry out an inOrder traversal and append the result to the output
Return the output

Do I want to convert to a tree first?
Technically you could leave it as a 2D array
But then wouldn't a swap me a really time intensive operation
Rather than just changing a pointer you'd have to insert entire slices into arrays

*/
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

TreeNode* convertToTree(vector<vector<int>> idxs) {
    TreeNode* root = new TreeNode(1);

    queue<TreeNode*> q;
    q.push(root);

    for (int i = 0; i < idxs.size(); i++) {
        TreeNode* cur = q.front();
        for (int j = 0; j < 2; j++) {
            if (idxs[i][j] != -1) {
                TreeNode* newChild = nullptr;
                newChild = new TreeNode(idxs[i][j]);
                q.push(newChild);
                j ? cur->right = newChild : cur->left = newChild;
            }
        }
    }
    return root;
}

void inOrder(TreeNode* root, vector<int> nodes) {
    if (root) {
        inOrder(root->left, nodes);
        cout << root->val << endl;
        nodes.push_back(root->val);
        inOrder(root->right, nodes);
    }
    return;
}

vector<vector<int>> swapNodes(vector<vector<int>> indexes, vector<int> queries) {
    vector<vector<int>> output;

    TreeNode* tree = convertToTree(indexes);

    return { {} };
}