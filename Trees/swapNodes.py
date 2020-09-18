'''
https://www.hackerrank.com/challenges/swap-nodes-algo/

We need to:
Convert the 2D array into a tree
Then for as many times as there are queries
    Level order traverse the tree keeping track of depth
    Swap at the appropriate levels
    After each swap carry out an inOrder traversal and append the result to the output
Return the output

Do I want to convert to a tree first?
Technically you could leave it as a 2D array
But then wouldn't a swap me a really time intensive operation
Rather than just changing a pointer you'd have to insert entire slices into arrays
'''

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
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

def swapNodes(indexes, queries):
    root = convertToTree(indexes)

    for query in queries:
        q = [(root, 1)]
        
        while q:
            cur 
            q = [child for node in q for child in (node.left, node.right)]
            #There is probably a pretty pythonic way of saying:
            #   If this level is one of that needs to be swap, iterate through all the nodes swapping their children