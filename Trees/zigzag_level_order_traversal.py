# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Version 1 - Iterative BFS
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = [root] if root else []
        l_to_r = True
        while q:
            m = len(q)
            cur_level = [101] * m 
            next_level = []
            for idx, node in enumerate(q):
                cur_level[idx + (not l_to_r)*(m - 1 - idx * 2)] = node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            output.append(cur_level)    
            q = next_level
            l_to_r = not l_to_r

        return output

'''
### Key Lessons ###
Don't get complacent. ACtually think about what the algo needs to do
    You are still traversing in the correct order just reporting values in reverse order
'''