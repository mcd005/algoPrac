# Problem description: https://leetcode.com/problems/invert-binary-tree/

# Version 1 - Level order traversal of the tree
# If a node has children then flip them using the helper function

# Time complexity     O(n)    where n is the number of nodes in the tree
# Space complexity    O(n)    since nodes have to be stored in a queue

# Version 2 - recursive solution
# Time Complexity     O(n)
# Space Complexity    O(n)   
# if the tree is a degenerate linked list there will be n calls until base case 
# (this is a high upper bound though because max memory allocated is for deepest level in tree)

# Version 2
def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

# Version 1
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def flip(node):
            temp = node.right
            node.right = node.left
            node.left = temp
        
        q = [root]
        while q:
            cur = q.pop(0)
            if cur.left or cur.right:
                flip(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
        return root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



            

