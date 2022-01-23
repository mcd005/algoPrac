# Version 1 - Recursive DFS 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -2**31 - 1, 2**31)

    def dfs(self, node, floor, ceil):
        if node:
            if node.val <= floor or node.val >= ceil:
                return False
            return self.dfs(node.left, floor, min(node.val, ceil)) and self.dfs(node.right, max(node.val, floor),  ceil)
        return True