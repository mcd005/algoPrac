# Version 2 - Kahns algorithm
# Time complexity       O(n + e) 
# Space complexity       O(n + e)
# where n is nodes and e is edges
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        num_deps = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            num_deps[course] += 1
        q = deque(idx for idx, num in enumerate(num_deps) if num == 0)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for child in graph[node]:
                num_deps[child] -= 1
                if num_deps[child] == 0:
                    q.append(child)
        return order if len(order) == numCourses else []

# Version 3 - Cleaner DFS. From LC. Our graph parents not children
# Time complexity       O(n + e) 
# Space complexity       O(n + e)
# where n is nodes and e is edges
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.graph = defaultdict(list)
        self.res = []
        for course, prereq in prerequisites:
            self.graph[course].append(prereq) 
        self.visited = [0 for _ in range(numCourses)]
        for course in range(numCourses):
            if not self.DFS(course):
                return []
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1:
            return False
        if self.visited[node] == 1:
            return True
        self.visited[node] = -1
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1
        self.res.append(node)
        return True

# Version 1 - Topological sort using DFS with an inelegant way of checking for cycles
# Time complexity       O(n + e) 
# Space complexity       O(n + e)
# where n is nodes and e is edges
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for c in range(numCourses)] 
        for course, prereq in prerequisites:
            self.graph[prereq].append(course)
        self.visited = [False] * numCourses
        self.ordering = [None] * numCourses
        self.order_ptr = numCourses - 1
        for node_idx in range(numCourses):
            if not self.visited[node_idx]:
                current_run = set()
                isCycle = self.dfs(node_idx, current_run)
                if isCycle:
                    return []
        return self.ordering

    def dfs(self, node_idx, current_run):
        current_run.add(node_idx)
        self.visited[node_idx] = True
        for child in self.graph[node_idx]:
            if child in current_run:
                return True
            if not self.visited[child]:
                isCylce = self.dfs(child, current_run)
                if isCylce:
                    return True
        current_run.remove(node_idx)
        self.ordering[self.order_ptr] = node_idx
        self.order_ptr -= 1
        return False


'''
### Version 1 ###
Build an adjacency list that is a list of python lists
    We'll call it graph
    If graph[0] looks like [1, 2, 3] then courses 1, 2 and 3 depend on course 0
Then we'll run a topological sort
    We'll have an array to mark which nodes have been visited and an array for the output
    We pick an unvisited node
    We DFS
        The base case is when we hit a node that hsa no unvisited children
        At that point we add it to the ordering

What if there are isolated nodes/networks
    I think that is fine so long as there is one course without prerequisites and no cycles
How do we deal with cycles?

### Version 2 ###
Build an adacency list that has all the children for a given node
With a seperate structure keep a count of how many dependencies (parents) each node has
Go through this seperate strucutre and enqueue all the nodes with no dependencies
While this q has items,m dequeue them and for each
    Append them to the order to be output
    Visit their children, and decrement their count of dependecies, to denote that their parent (i.e) the current node, has been removed
    If we decrement their count of deps to zero, then enqueue them
At the end, if our order contains less than the total number of nodes, we encountered a cycle
Otherwise return the order

Khans works because we can't start with or enqueue any node in a cycle; by definition they have deps
'''