# Version 1 - Recursive DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            output.append(root.val)
            right_view = self.rightSideView(root.right)
            left_view = self.rightSideView(root.left)
            r, l = len(right_view), len(left_view)
            longer_branch = max(r, l)
            for i in range(longer_branch):
                if i < r:
                    output.append(right_view[i])
                else:
                    output.append(left_view[i])
        return output

# The rookie error here would be to only try to traverse right nodes
# However there will be left nodes that are visible from the right

# For each node we are going to want to traverse it's right children and recursively look for the linked list at the leading edge
# However in cases where the left branch is longer than the right branch, some of the nodes near the leaf will be visible
# Once we have both lists, we'll splice them, taking the right hand nodes preferentially

# We'll think later about how to make it less expensive in terms of list copying

# You could also do this with a BFS approach, wher you only save the last node in every level

## Key Lessons ##
# If you get a question like this in an interview, you won't have the benefit of seeing % passed. Never assume as easy as it looks
# The best memory saving technique is to write to memory that is outside the recusrive call scope
# Here we do that by keeping track of which level we are at