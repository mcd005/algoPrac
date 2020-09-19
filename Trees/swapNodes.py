# https://www.hackerrank.com/challenges/swap-nodes-algo/
#
# We need to:
# Convert the 2D array into a tree
# Then for as many times as there are queries
#     Level order traverse the tree keeping track of depth
#     Swap at the appropriate levels
# After all the swaps have been carried out, do an inOrder traversal and append the result to the output
# Return the output
#
# Time complexity         O(tn^2)     assuming worst case of having to swap all the nodes
# Space complexity        O(tn)       we have to save all the nodes for each query
#
# Do I want to convert to a tree first?
#   I considered leaving the input in 2D array form
#   But then it seemed to me that swapping would become really time intensive (insertion is O(n) in an array)
#   And also would require some awkward mathematics
# So I decided that yes it would be better to convert the 2D array to a tree
#   Would take O(n)
#   But swapping would just be a constant time operation, changing pointers
#
# Also had to increase recursion depth to account for tall trees
#   A workaround could have declaring a stack in the program itself that would serve as the function call stack
#   Rather than having the recursive function calls on the stack of the virtual machine, we could just put the
#   Requisite parameters onto the stack in out program. That way the stack can be arbitrarily large

import sys

sys.setrecursionlimit(1500)

# Below lines are to read in input from .txt
tc = open("SwapNodes_TestCase10.txt", 'r')

n = int(tc.readline())
indexes = []
for i in range(n):
    indexes.append([int(num) for num in tc.readline().rstrip().rsplit()])

t = int(tc.readline())
queries = []
for i in range(t):
    queries.append(int(tc.readline().rstrip()))


class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def convertToTree(idxs):
    root = TreeNode(1)
    q = [root]

    for i in range(len(idxs)):
        cur = q.pop(0)
        for j in range(2):
            if (idxs[i][j] != -1):
                newChild = TreeNode(idxs[i][j])
                q.append(newChild)
                if j:
                    cur.right = newChild
                else:
                    cur.left = newChild

    return root

def inOrder(root):
    if root:
        left_list = inOrder(root.left)
        right_list = inOrder(root.right)
        return left_list + [root.val] + right_list
    else:
        return []

def swap(treeNode):
    if treeNode:
        treeNode.left, treeNode.right = treeNode.right, treeNode.left



def swapNodes(indexes, queries):
    output = []

    root = convertToTree(indexes)

    for query in queries:
        q = [root]
        level = 1
        while q:
            if level % query == 0:
                for node in q:
                    swap(node)
            q = [child for node in q for child in (node.left, node.right) if child]
            level += 1
        output.append(inOrder(root))

    return output

#Driver code
print(swapNodes(indexes,queries))