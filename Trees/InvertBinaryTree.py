# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Problem description: https://leetcode.com/problems/invert-binary-tree/

Level order traversal of the tree
If a node has children then flip them using the helper function

Time complexity     O(n)    where n is the number of nodes in the tree
Space complexity    O(n)    since nodes have to be stored in a queue
                            (this is a high upper bound though because max memory allocated is for deepest level in tree)
'''
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
        
'''
Recursive solution
I didn't implement this because I got stuck on thinking "what is an elegant way for this function to ask if a node has children but also recursively reverse them"
The trick here is that you just ask if a node exist, and then by the time child is the node in question you are effectively asking if the child exists

This solution is faster than mine (96.7% vs 85.6%) but apparently takes more memory (maybe because of the increasing number of function calls on the stack)

def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
            
Time Complexity     O(n)
Space Complexity    O(n)    if the tree is a degenerate linked list there will be n calls until base case
'''