from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        result = 40**2 + 1
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        q = deque([(0, 0, k, 0)]) # queue of tuples that look like (i, j, dynamite, steps)
        while q:
            i, j, dynamite, steps = q.popleft()
            if i == self.m - 1 and j == self.n - 1:
                result = min(result, steps)
                return result
            if self.is_visitable(i + 1, j):
                q.append( (i + 1, j, dynamite - self.grid[i + 1][j], steps + 1) )
            if self.is_visitable(i, j + 1):
                q.append( (i, j + 1, dynamite - self.grid[i][j + 1], steps + 1) )
        return result if result != 40**2 + 1 else -1

    def is_visitable(self, i, j):
        return (0 <= i < self.m) and (0 <= j < self.n)

# q = (1, 0, 0, 1)  (0, 1, 0, 1)


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        search = self.dfs(0, 0, k)
        return search if search <= 40**2 else -1

    def is_visitable(self, i, j):
        return (0 <= i < self.m) and (0 <= j < self.n) and self.grid[i][j] != -1

    def dfs(self, i, j, dynamite):
        if i == self.m - 1 and j == self.n - 1:
            return 0
        if self.grid[i][j] == 1:
            if dynamite == 0:
                return 40**2 + 1
            dynamite -= 1
        temp, self.grid[i][j] = self.grid[i][j], -1
        cur_min = 40**2 + 1
        for n_i, n_j in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            if self.is_visitable(n_i, n_j):
                cur_min = min(cur_min, self.dfs(n_i, n_j, dynamite))
        self.grid[i][j] = temp
        return 1 + cur_min


'''
Basically like unique paths except we can remove k obstacles
For each cell we need to check if the cell above required fewer steps o
We could just do a DFS
We pass the the DFS call the number of obstacles that can skill be removed
And pass to each dfs call 

Enqueue first tile
While there are elements in q, enqueue their unvisited neighbours
If the neighbours are blocked, spend dynamite to go there
If you have no dynamite then you can't enqueue neighbours that are blocked

And we should priority queue tiles where we didn't have to spend dynamite
'''