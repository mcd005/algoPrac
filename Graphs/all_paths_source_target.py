# https://leetcode.com/problems/all-paths-from-source-to-target/
# Version 2 - Recursive
# Time complexity       O(n)
# Space complexity       O(longest path) -> O(n) in the worst case
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.target = len(graph) - 1
        return self.dfs(0, [])
        
    def dfs(self, node, path):
        path.append(node)
        if node == self.target:
            return [path]
        return [child_path for child in self.graph[node] for child_path in self.dfs(child, path.copy()) if child_path]

# Version 1 - Iterative BFS
# Time complexity       O(n)
# Space Complexity      O(n)
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        output = []
        q = deque([ [0] ])
        while q:
            path = q.popleft()
            if path[-1] == n - 1:
                output.append(path)
                continue
            for next_node in graph[path[-1]]:
                q.append(path + [next_node])

        return output

#### Key understandings ####
# When to add to a path is an important decision
# node.empty() doesn't necessarily mean that you've reached the end
# Once you have a working solution think of ones that require less copying