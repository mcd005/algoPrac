# https://leetcode.com/problems/search-suggestions-system/
# Version 2 - Found on LC
# We sort the products so the lexographically minimum one is at the start
# We iterate through the prefixes of the search word
# We use bisect to see at what index that prefix would be if it were inserted into that list whilst still maintaining order
# Provided they contain the prefix take the words at the next three indices
# Time complexity       O(nlogn + qlogn + k)
# Time complexity       O(qmk)
# Where n is the number of products, m is the average number of letters in a product,
# k is the number of suggestions that should be returned (here 3) and q is the number of letters in the searchWord
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix, i = '', 0
        res = []
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res

# Version 1 - Trie
# We construct a trie made up of the words in products
# Each node of the trie has a list called "leaves" which holds the three lexicograhically min products at the leaves on it's branch
# Time complexity       O(nmk + q)
# Space complexity      O(nmk + q)
# Where n is the number of products, m is the average number of letters in a product,
# k is the number of suggestions that should be returned (here 3) and q is the number of letters in the searchWord
import bisect

class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaves = []

    def add_leaf(self, word):
        bisect.insort(self.leaves, word)
        if len(self.leaves) > 3:
            self.leaves.pop()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_to_trie(self, word):
        node = self.root
        for letter in word:
           if letter not in node.children: 
               node.children[letter] = TrieNode()
           node = node.children[letter]
           node.add_leaf(word)

    def print_trie(self):
        self.print_node(self.root) 
    
    def print_node(self, node):
        for letter, child in node.children.items():
            print(letter)
            self.print_node(child)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.add_to_trie(product)

        output = []
        node = trie.root
        for letter in searchWord:
            if node and letter in node.children:
                node = node.children[letter]
                output.append(node.leaves)
            else:
                node = None
                output.append([])

        return output