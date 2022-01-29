# Version 2 - Python BFS
class Solution(object):
    def calcEquation(self, equations, values, queries):

        graph = {}
        
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            q = collections.deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]

# Version 3 - Code golf BFS from LC
# We essentially mark all the paths to and from nodes then do a BFS to find the
def calcEquation(self, equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]


# Version 1 - Union find
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.roots = {}  # looks like {variable: [cost to get to root,  root]}
        for eq, val in zip(equations, values):
            nume, denom = eq
            if nume not in self.roots or nume == self.roots[nume][1]:
                cost_d, root_d = self.find(denom)
                self.roots[nume] = [cost_d * val, root_d]
            else:
                self.reverse(denom)
                cost_n, root_n = self.find(nume)
                self.roots[denom] = [cost_n / val, root_n]
        
        results = []
        for qn, qd in queries:
            if qn not in self.roots or qd not in self.roots:
                results.append(-1.0)
                continue
            cost_qn, root_qn = self.find(qn) 
            cost_qd, root_qd = self.find(qd) 
            if root_qn != root_qd:
                results.append(-1.0)
            else:
                results.append(cost_qn / cost_qd)
        
        return results
                
    def find(self, node):
        if node not in self.roots:
            self.roots[node] = [1, node]
        cost_to_root, root = self.roots[node]
        if node != root:
            roots_cost, roots_root = self.find(root)
            self.roots[node] = [cost_to_root * roots_cost, roots_root]
        return self.roots[node]

    def reverse(self, node):
        if node not in self.roots:
            self.roots[node] = [1, node]
        cost_to_root, root = self.roots[node]
        if node != root:
            self.reverse(root)
            self.roots[root] = [1 / cost_to_root, node]

'''
Union find
We want to express each equation in terms of one variable

Algo
    We iterate through each set of eqs an union find the two
        To do union find we have an array or dict that looks like {var: root of that var} 
        Initally all vars are their own root
            Typically we know beforehand all the possible nodes,
            but with this question we will just have to initialise them as we go along (I think?)
        We call finding by asking:
            Who is your root?
                If it's not yourself then find it's root
            Set the value of your root to your ancestor who is it's own root
            As we traverse to that ancestor though, we need to incorporate the value from values by multiplying
    Then we iterate through queries and all we need to do run find on both:
        This should return how much it costs to get to the root
        And what their root is
    If they don't share a common root then we return -1

We need to be carfeul with zero
    What happens if there are mutliple definitions of zero?
    Is it possible for a denom in a query to equal zero?
        Zero not allowed, so we don't need an answer to these
Variable bc is not the product of b and c is it?
    No each string is a distinct variable
Are there other possiblities of circular definitions?
    We build our graph in the order it's given to us
Can we expect "a"/"a"?
    Yes and it's accounted for
How do we deal with sticking two networks together?
    For given nume-denom
    We will either be connecting
        1) root-root
        2) root-child
        3) child-root
        4) child-child
    For 1 we can just do as normal and set the new root to be the overall root
    For 2 it's the same, because that child will eventually point to the root
    For 3 I think we will have to reverse the directions of the nodes in the denom
    For 4 likewise will have to reverse the chain of one of the children

### Key lessons ###
Do a bit more ideation
    If you can do union find then maybe you can do a bidirectional graph implementation
Don't rely on a wing and a prayer
    You can reduce all the possible examples down into a few key ones
    using some simple rules (e.g. their are only child nodes and parent nodes)
    How do we deal with sticking two graphs together?
    "Our current algo causes connections to be severed. How do we deal with that?"
Use examples, do not try and picture it all, especially for recursion   
If it's making you're life difficult to have edges going only one way then have bidirectional edges
Approach to recursion
    First line written should be the desired effect for most cases
    Then consider the base case
    Then order the function so that things happen at the right time
'''