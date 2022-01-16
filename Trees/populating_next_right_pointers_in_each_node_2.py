# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
# Version 2.5 - Iterative BFS, turning the next level into a linked list which will be our q (one while loop)
# Time complexity           O(n)
# Space complexity          O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        dummy = tail = Node(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                node = dummy.next
                dummy.next = None
                tail = dummy = Node(0)

        return root

# Version 2 - Iterative BFS, turning the next level into a linked list which will be our q
# Time complexity           O(n)
# Space complexity          O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            dummy = tail = Node(0) # We create the dummy head for the linked list that will join all the children
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                node = node.next
            node = dummy.next
            dummy.next = None

        return root

# Version 1.5 - Iterative BFS (more concise)
# Time complexity           O(n)
# Space complexity          O(n)
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

# Version 1 - Iterative BFS
# BFS but enque nodes on the write first
# When we vist that node, save it's ptr so we can point the next node in the level at it
# Time complexity           O(n)
# Space complexity          O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur_level = [root]
        while cur_level:
            next_right = None
            next_level = []
            for node in cur_level:
                node.next = next_right
                for child in [node.right, node.left]:
                    if child:
                        next_level.append(child)
                next_right = node
            cur_level = next_level

        return root

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## Key Lessons ##
# Don't attempt recursive BFS it's infeasible
# And it's way too tough to get state from a differnt recursive call without O(n) memory
# So with the above in mind you have to use the memory given you already if you want O(1)