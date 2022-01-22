# htps://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Version 1 - DFS
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.col_map = defaultdict(lambda: [])
        self.min_col, self.max_col = 0, 0
        self.traverse(root, 0, 0)
        output = []
        for col in range(self.min_col, self.max_col + 1):
            if col in self.col_map:
                # Put vals from lower rows first
                # If rows are the same, maintain order they were added in (left to right)
                self.col_map[col].sort(key=lambda x: (x[0]))
                col_list = []
                for _, val in self.col_map[col]:
                    col_list.append(val)
                output.append(col_list)

        return output

    def traverse(self, node, row, col):
        if node:
            self.col_map[col].append((row, node.val))
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            self.traverse(node.left, row + 1, col - 1)
            self.traverse(node.right, row + 1, col + 1)

#### Key Lessons ####
# Good spot on sorting only using first value in tuple