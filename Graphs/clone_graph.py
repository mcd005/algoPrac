# https://leetcode.com/problems/clone-graph/discuss/42313/C%2B%2B-BFSDFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Version 1 - Recursive DFS
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            visited = [None] * 101
            return self.dfs(node, visited)
        return None

    def dfs(self, node, visited):
        if not visited[node.val]: 
            visited[node.val] = Node(node.val)
            visited[node.val].neighbors = [self.dfs(nei, visited) for nei in node.neighbors]
        return visited[node.val]


'''
We are given node 1 and we want to return node 1
We use the given constructor to create the new node
We iterate over the originals neighbours and also create them, doing so recursively
If a node has already been created, we do not DFS there
And when we are intiailiasing the list of neighbours,
We've run into a problem because visited is not populated until all the neighbours have been traversed
Maybe we should instead pass the parent pointer
    But then if you had a cycle you still wouldn't recognise your grandparent
So we should mark a node as visited first

We could definetly save space by using all the memory given with the original graph
But that's not really copying because we muck up the original graph


### Key Lessons ###
Sometimes you don't want to do it all on one line
'''
