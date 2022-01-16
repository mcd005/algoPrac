# Version 2 - Recursive (doesn't work)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.recursive(root, None)
        return root

    def recursive(self, node, next_right):
        if node:
            node.next = next_right
            if next_right:
                right_child_next_right = next_right.left if next_right.left else next_right.right
            else:
                right_child_next_right = None
            self.recursive(node.right, right_child_next_right)
            self.recursive(node.left, node.right)

# Version 1.5 - Iterative BFS (more concise)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur_level = [root]
        while cur_level:
            next_right = None
            next_level = []
            for node in cur_level:
                if node:
                    node.next = next_right
                    next_level.append(node.right)
                    next_level.append(node.left)
                    next_right = node
            cur_level = next_level

        return root