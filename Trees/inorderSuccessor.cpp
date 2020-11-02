/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

/*
If the node has a right child, then traverse the left branch of the descendants of that child until you reach a leaf. That leaf is the IOS.
If the node has no right branch and but has an ancestor that is bigger then it, that ancestor is the IOS.
If the node has no right branch and all the ancestor including the root are is smaller then there is no IOS.

N.B. you could do this without checking the values of the nodes by using pointers only
Rather than asking "Is the parent bigger than the current node?" 
you'd ask "Is the pointer to the left child of the parent equal to the pointer to the current node?"

Time complexity		O(n)	Average case logn. 
				You either have to find the deepest leaf, 
				or go from the deepest leaf to the root.
Space complexity 	O(1)
*/

class Solution {
public:
    Node* inorderSuccessor(Node* node) {
        if (node->right){
            node = node->right;
            while (node->left){
                node = node->left;
            }
            return node;
        }
        else{
            while (node->parent){
                if (node->parent->val > node->val){ //could also have: if (node->parent->left == node). See N.B.
                    return node->parent;
                }
                else{
                    node = node->parent;
                }
            }
            return NULL; //i.e. we have reached the root and not found a node greater than our starting one
        }
    }
};





