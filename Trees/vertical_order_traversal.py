# Version 1 - Keep info for each node in dict that looks like {col : [(row, value)]}
# Sort the list at each node, first by row, then by value
# Time complexity       O(n + c(rlogr + r)) However the sum of all len(col_map[col]) = n, so entire alogrithm is linear
# Space complexity      O(n)
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.col_map = defaultdict(lambda: [])
        self.min_col, self.max_col = 0, 0
        self.traverse(root, 0, 0)
        output = []
        for col in range(self.min_col, self.max_col + 1):
            if col in self.col_map:
                # Put vals from lower rows first. If rows are the same, order by val
                self.col_map[col].sort(key=lambda x: (x[0], x[1]))
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

# We traverse the tree keeping track of the positions given by col and row
# We put these in a dict that looks like {col : [(row, value)]}
# As we go we keep track of the min and max cols
# When we've traversed the tree we iterate from min_col to max_col inclusive, stopping on iterations where the col number is in the dict
# We sort the list held at this key 

#### Key Lessons ####
# Good spot on defaultdict functionality
# Good job adding broad enough test cases