class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start, self.dest = startValue, destValue
        return self.dfs(root, "")

    def dfs(self, node, steps):
        if node:
            if node.val == self.start:
                return "U" * len(steps)
            if node.val == self.dest:
                return steps
            left_sub = self.dfs(node.left, steps + "L")
            right_sub = self.dfs(node.right, steps + "R")
