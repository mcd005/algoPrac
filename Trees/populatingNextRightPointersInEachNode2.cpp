// Version 1 - Recursive
class Solution {
public:
    Node* connect(Node* root) {
        if(!root) return NULL;
        Node* n = root->next;
        while(n)
        {
            if(n->left)
            {
                n = n->left;
                break;
            }
            if(n->right)
            {
                n = n->right;
                break;
            }
            n = n->next;
        }
        if(root->right) root->right->next = n;
        if(root->left) root->left->next = root->right ? root->right : n;  
        connect(root->right);
        connect(root->left);
        return root;
    }
};