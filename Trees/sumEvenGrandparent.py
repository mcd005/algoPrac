'''
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Version 2
Do a level order traversal bu instead the q contains sublists of (current node val, parent node val, grandparent node val)
Then when each node in the q is encountered you can check the value of its grandparent

This solutions is quicker than v1 and appears not to require too much more memory

Time complexity        O(n)
Space complexity       O(n)     
'''

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = [[root, 0, 0]]
        sum = 0
        while (q):
            #print([[item[0].val, item[1], item[2]] for item in q])
            current = q.pop(0)
            node = current[0]
            parent = current[1]
            if node.left:
                q.append([node.left, node.val, parent])
            if node.right:
                q.append([node.right, node.val, parent])
            if (current[2]%2 == 0) and (current[2] > 0):
                sum += node.val
        return sum


'''
Version 1
Do a level order traversal
When you encounter a node with an even value iterate of the children of it's children, summing their values
This solution is pretty slow however because you will visit many nodes twice
'''

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = []
        sum = 0
        q.append(root)
        while (q):
            current = q.pop(0)
            if (current.val % 2 == 0):
                for child in [current.left, current.right]:
                    if child:
                        for grandchild in [child.left, child.right]:
                            if grandchild:
                                sum += grandchild.val
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        return sum






