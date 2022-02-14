# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Time complexity       O(n)
# Space complexity      O(n)
# Average space complexity is the height of the tree, which is logarithmic, but in worst case (i.e. linked list) it's linear
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.output = []
        self.dfs(root)
        return self.output

    def dfs(self, node):
        if node:
            distance_to_leaf = max(self.dfs(node.left), self.dfs(node.right))
            if distance_to_leaf + 1 > len(self.output):
                self.output.append([])
            self.output[distance_to_leaf].append(node.val)
            return distance_to_leaf + 1
        return 0

'''
Brute force
    Traverse
    When you hit a leaf, append it to the list
    Then mark at as visited using a -101
    Repeat the process again
    Do so until there are no nodes left
    Pretty bad becuase it takes O(n^2)

Every node will be a leaf eventually, we just want to know how to group it
It will be grouped according to how many descendants it has 
If a node has zero descendants then it will be in the zeroth list
If a node has two descendants then it will be in the first in the list

Rather than working out the log maths required to insert at the right index is there an easy way to do things?
Yes we don't need to count number of descendants but rather distance from a leaf
The nodes with no children are leaves thus are at a distance of zero from the leaf and are inserted at index zero
The parents of those nodes are at a distance of one from a leaf thus are inserted at index 1
If that index doesn't exist then we can we just append to the list?
    Yes we will always append deepest nodes first

### Key Lessons ###
Write your workings down here
Think about how you can quantify observations. Attach a numerical rule to them
'''