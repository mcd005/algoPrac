# Version 1 - DFS but using a set to track visited
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        numProvinces = 0

        def dfs(row):
            visited.add(row)
            for col in range(n):
                if isConnected[row][col] == 1 and col not in visited:  
                    dfs(col)
            return
        
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                numProvinces += 1
                dfs(i)
                
        return numProvinces 

# Version 2 - Union find (quite slow in ms)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]
        
        n = len(isConnected)
        roots = list(range(n))
        numProvinces = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    root1, root2 = find(i), find(j)
                    if root1 != root2:
                        roots[root1] = root2 #Union
                        numProvinces -= 1
        
        return numProvinces

#Version 3 - fastest union find I could see on LC submission
class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        n = len(A)
        size = n
        root = list(range(n))
        
        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]
        
        def union(a, b):
            nonlocal size
            x, y = find(a), find(b)
            if x == y:
                return
            size -= 1
            root[x] = y
        
        for i in range(n):
            for j in range(i):
                if A[i][j]:
                    union(i, j)
        return size