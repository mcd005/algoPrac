'''
https://leetcode.com/problems/binary-tree-postorder-traversal/

Classic recursive postOrder traversal

Time complexity		O(n)		number of recursive calls until base
Space complexity	O(log n)	height of the tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        leaves = []
        
        def traverse(Node):
            if (Node):
                traverse(Node.left)
                traverse(Node.right)
                leaves.append(Node.val)
            
        traverse(root)
        return leaves
        