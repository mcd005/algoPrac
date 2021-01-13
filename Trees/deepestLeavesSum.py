
'''
https://leetcode.com/problems/deepest-leaves-sum

This algorithm is basically a level order traversal
but we have saved in memory both the current and previous levels

Add root to queue
While there are nodes in the queue
   Using list comprehension set the previous level to the current nodes in the queue
   At the same time set the queue equal to the children of the current nodes in the queue (provided they exist)
Once the queue is empty, your at the last level. Sum all the node values

Time complexity     O(n)
Space complexity    O(n)
'''

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            pre, queue = queue , [child for node in queue for child in [node.left, node.right] if child]
        return sum(leaf.val for leaf in pre)


#Depth first search
#Keep track of depth
#If depth less than max, no need to add to sum
#If depth equal max depth add to sum
#If depth greater than max set sum to that value
#Return sum

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = sum = maxDepth = 0
        return traverse(root, depth, sum, maxDepth)

def traverse(Node, depth, sum, maxDepth):
    if (Node):
        print(Node.val, depth, maxDepth)
        depth += 1
        traverse(Node.left, depth, sum, maxDepth)
        traverse(Node.right, depth, sum, maxDepth)
        if (depth == maxDepth):
            sum += Node.val
        elif (depth > maxDepth):
            sum = Node.val
            maxDepth = depth
        #print(Node.val, depth)
        depth -= 1
    return sum
