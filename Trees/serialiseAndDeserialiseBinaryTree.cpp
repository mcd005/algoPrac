class Codec {
public:
    void serial(TreeNode* root, string &s) {
        if (root==nullptr) return;
        s.append(to_string(root->val));
        s.append("(");
        serial(root->left, s);
        s.append(")(");
        serial(root->right, s);
        s.append(")");
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s;
        serial(root, s);
        return s;
    }

    TreeNode* des(string &s, int &i, int n) {
        int val = 0;
        bool neg = false;
        while (isdigit(s[i]) || s[i]=='-') {
            if (s[i]=='-') neg = true;
            else val = val*10+(s[i]-'0');
            i++;
        }
        if (neg) val = -val;
        TreeNode* root = new TreeNode(val);
        i++;
        if (isdigit(s[i]) || s[i]=='-') root->left = des(s, i, n);
        i++;
        i++;
        if (isdigit(s[i]) || s[i]=='-') root->right = des(s, i, n);
        i++;
        return root;
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int n = data.size();
        if (n==0) return nullptr;
        int i = 0;
        return des(data, i, n);
    }
};