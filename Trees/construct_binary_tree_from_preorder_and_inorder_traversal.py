# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Version 1 - Use preorder to find the roots of each subtree in inorder
# Time complexity       O(n)
# Space complexity      O(n + h)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.positions = {val: idx for idx, val in enumerate(inorder)}
        self.root_ptr = 0
        self.preorder = preorder
        return self.subtree(0, len(inorder))

    def subtree(self, left, right):
        if left == right:
            return None
        root_val = self.preorder[self.root_ptr]
        node = TreeNode(root_val)
        mid = self.positions[root_val]
        self.root_ptr += 1
        node.left = self.subtree(left, mid)
        node.right = self.subtree(mid + 1, right)
        return node

'''
We have to use the two arrays to triangulate
Inorder is structured such that the root of the tree sits in the "middle" of the arr
    Then it's left child sits in the "middle" of the left subarry
    Right child sits in the "middle" of the right subarray
And so on recursively
    [9, 3, 15, 20, 7]
        r
     r          r
            r      r

With preorder the root of tree is the very first element

### Key lesson ###
Build what is intuitive to you! Do not try and cram some other existing solution into this one
''' 
