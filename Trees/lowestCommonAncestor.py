# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Iterative solution (see lowestCommonAncestor.cpp for recursive)

# Do a level order traversal of all the nodes and remember each nodes parent using a dict

# Create an empty set that will hold all of p's ancestors

# Using the dict, check who is p's parent and add this to p's list of ancestors
#     Set p's parent equal to current node
#     Check who the current node's parent is
#     And so on all the way up to the root
# You now have all of p's ancestors
    
# Now starting with q
#     If q's parent is in the list of p's ancestors, you have by definition found the LCA
#     Otherwise set p's parent to the current node
#     And check if the current nodes parent is in p's list of ancestors
# If none of q's ancestors are in p's list of ancestors then q must be the LCA

# Time complexity     O(n) for BFS
# Space complexity    O(n) if not degenerated linked list O(log n) on average

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qu = [root]
        parent = {root : None}
        while p not in parent or q not in parent:
            node = qu.pop(0)
            if node.left:
                qu.append(node.left)
                parent[node.left] = node
            if node.right:
                qu.append(node.right)
                parent[node.right] = node
                
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
            
        while q not in ancestors:
            q = parent[q]
            
        return q