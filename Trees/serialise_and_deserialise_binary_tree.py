# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Version 1 - Level Order
# Time complexity       O(n)
# Space complexity      O(n)
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        last_non_null = 0
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur:
                output.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
                last_non_null = len(output) - 1
            else:
                output.append("null")
            
        return " ".join(output[:last_non_null + 1])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split()
        root = self.init_node_with_string(vals[0])
        if root:
            node = root
            isLeftChild = True
            n = len(vals)
            q = deque()
            for i in range(1, n):
                child = self.init_node_with_string(vals[i])
                if child:
                    if isLeftChild:
                        node.left = child
                        q.append(node.left)
                    else:
                        node.right = child
                        q.append(node.right)
                if not isLeftChild and q:
                    node = q.popleft()
                isLeftChild = not isLeftChild
        return root

    def init_node_with_string(self, val):
        if val == "null":
            return None
        return TreeNode(int(val))

# Version 2 - Preorder
# Time complexity       O(n)
# Space complexity      O(n)
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.output = []
        self.preorder(root) 
        return ",".join(self.output)

    def preorder(self, node):
        if node:
            self.output.append(str(node.val))
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            self.output.append("#")
        # 1,2,null,null,3,4,null,null,5,null,null

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if self.i >= len(vals):
                return None
            val = vals[self.i]
            self.i += 1
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
