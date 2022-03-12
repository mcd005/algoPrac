# https://leetcode.com/problems/alien-dictionary/
# Version 2 - Compare string with neighbour to build graph. Topsort graph with Kahns
# Time complexity       O(m + k)
# Space complexity      O(min(k^2, n) + k)
# Where m is the total length of all the words and k is the size of alphabet and n is the number of words
# An adjacency list requires O(V + E) space. Each letter could connect to k - 1 other letters (i.e to give k^2),
# but only as long as there are more words than that, to allow for those possible combinations
from collections import OrderedDict, defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {} # looks like {letter: {child_letter1, child_letter2}}
        in_degree = defaultdict(int) # looks like {node: count of deps}
        n = len(words)
        for i in range(n):
            has_diverged = False
            first = len(words[i])
            second = len(words[i + 1]) if i < n - 1 else 0
            for j in range(first):
                if words[i][j] not in graph:
                    graph[words[i][j]] = set()
                if j < second and not has_diverged and words[i][j] != words[i + 1][j]:
                    if words[i + 1][j] not in graph[words[i][j]]:
                        graph[words[i][j]].add(words[i + 1][j])
                        in_degree[words[i + 1][j]] += 1
                    has_diverged = True
            if i < n - 1 and not has_diverged and first > second:
                return ""
        order = []
        q = deque(char for char in graph if in_degree[char] == 0)
        while q:
            char_node = q.popleft()
            order.append(char_node)
            for child in graph[char_node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
        return "".join(order) if len(order) == len(graph) else ""

# Version 1 - Attempted to use a trie with it's children ordered to determine precedence. Probably not possible as some info about ordering is lost
from collections import OrderedDict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.graph = {} # looks like {letter: {child_letter1, child_letter2}}
        self.in_degree = {} # looks like {node: count of deps}
        trie_root = OrderedDict()
        for word in words:
            node = trie_root
            for letter in word:
                if letter not in self.graph:
                    self.graph[letter] = set()
                    self.in_degree[letter] = 0
                if letter not in node:
                    node[letter] = OrderedDict()
                node = node[letter]
            node['#'] = '#'
        self.construct_graph(trie_root)
        print(self.in_degree)
        order = []
        q = deque(char for char, num_in_degree in self.in_degree.items() if num_in_degree == 0)
        while q:
            char_node = q.popleft()
            order.append(char_node)
            for child in self.graph[char_node]:
                self.in_degree[child] -= 1
                if self.in_degree[child] == 0:
                    q.append(child)
        return "".join(order) if len(order) == len(self.graph) else ""
        
    def construct_graph(self, trie_node):
        children = list(trie_node.items())
        m = len(children)
        for i in range(m):
            letter, child_node = children[i]
            if letter != '#':
                if i < m - 1:
                    next_letter, _ = children[i + 1]
                    self.graph[letter].add(next_letter)
                    self.in_degree[next_letter] += 1
                self.construct_graph(child_node)

'''
We have some hidden mapping that says w -> 0, t -> 1 etc
If we wanted to sort a list strings using the dictionary we would do something roughly like words.sort(key=lambda x: idx of char in dict)

Algo
We build a trie, using nested ordered dictionaries
Now we are going to build a regular dict that looks like {char: prev char in alien dict}
    We shall call this alien_dict
    This is essentially an abstraction of the linked list that, when stitched together, give us the hidden alien dcit we are after
We do this by starting at the root and doing the following:
    For each child of our current node we populate our alien_dict so it looks like {child: next child in ordered dict}
    We recursively call the populate function of each of those children, so it will do the same process with it's children
Then, we convert our alien_dict into a string by traversing the linked list it represents

We have a few problems though:
    What do we do for undefined relationships/disjointed list nodes?
        e.g. if words is ["ab", "de"]
        I guess we can return b or e in any order
    What is a efficient way of checking the order does not give an invalid dict?
        If a char already has a prev then we are creating an invalid dict?
            Not sure this is always true though
            Especially because as we get into the leaves of the trie we begin to fill gaps in the dictionary
        I guess as we are building the final string, if we see a char pop up again we know we have an invalid dict
    What if we have the ends of words that are not leaves?
        This is fine, just means the location of that char is not strictly defined and can be placed with some flexibility
    Do we need to build a trie?
        Only common prefixes allow us to confirm the ordering of letters
        I can't think of way of doing this without lots of recursion which will also be O(n) and more complicated
        There are probably other methods but this one is clearest to me at the moment
    What are the ways the this gap filling could go wrong?
        Because we are only allowing a 1-1 parent to child relationship, we lose some information when we break a parent child
        connection
        Instead what we should do is have each parent hold multiple children
    
So rather than listifying our trie children, we should connect them in a graph and do Kahns algo to topsort
We need to keep a track somewhere of how many nodes there are
    Is this just the len of our graph?
        No because only nodes with children are added and some nodes don't have children
        Same with indegree
        We need to initialise both when we build the trie
        The len of that gives us what we need

A trie is not a appropriate data structure here
    Does not account for redefined relationships/cycles e.g. [z, x, z]
So instead I think what we want to do is walk through each pair of strings, i and i + 1
    When they diverge gives us ordering 
'''
