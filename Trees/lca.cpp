/*
https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/

If we know both nodes are present in the tree then we just need to return the node that represents the divergence in the binary search of the two values
Or if node we have arrived at has the value of one of the targets than that node must be the LCA

Time complexity 	O(n) 	average is logn but big-Oh is is worst case and for degnerate linked list
Space complexity	O(n)

N.B. if we don't know both nodes are in the tree we can use a helper function that will check if they are present first
*/

Node *lca(Node *root, int v1,int v2) {
    if (root){
        if (v1 > root->data && v2 > root->data){
            return lca(root->right, v1, v2);
        }
        else if (v1 < root->data && v2 < root->data){
            return lca(root->left, v1, v2);
        }
        else{
            return root;
        }
    }
    return NULL;
}