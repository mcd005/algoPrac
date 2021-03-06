# https://leetcode.com/problems/word-search-ii

# Each solution uses a either recursive DFS or iterative BFS
# and some form a Trie (implemented literally or using just a hashmap)

# Time complexity      O(wk + (nm)^2)
# Space complexity     O(wk + nm)

# for adding w words of length k to a trie
# and iterating through an n*m board
# where the recursive function calls could be made on all nm elements before a base case is reached (in worst case).
# The max size of the callstack will be nm

# Version 1 - Recursive DFS solution with Trie class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isComplete = False

def addToTrie(word, node):
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.isComplete = True

def dfs(board, node, i, j, path, otpt):
    if node.isComplete:
        otpt.append(path)
        node.isComplete = False
    if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
        return
    temp = board[i][j]
    node = node.children.get(temp)
    if not node:
        return
    # Don't need to use extra memory to record visited coords
    # instead mark visited with a #
    board[i][j] = "#"
    dfs(board, node, i + 1, j, path + temp, otpt)
    dfs(board, node, i, j + 1, path + temp, otpt)
    dfs(board, node, i - 1, j, path + temp, otpt)
    dfs(board, node, i, j - 1, path + temp, otpt)
    board[i][j] = temp

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            addToTrie(word, root)

        output = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(board, root, row, col, "", output)

        return output



# Version 2 - DFS with hashmap for trie
def findWords(self, board, words):
    trie = {}
    for w in words:
        t = trie
        for c in w:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#' # terminating char
    self.res = set()
    self.used = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            self.find(board, i, j, trie, '')
    return list(self.res)


def find(self, board, i, j, trie, pre):
    if '#' in trie:
        self.res.add(pre)
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    if not self.used[i][j] and board[i][j] in trie:
        self.used[i][j] = True
        self.find(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
        self.find(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
        self.find(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
        self.find(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
        self.used[i][j] = False



# Version 3 - Recursive DFS, a hashmap for a trie and backtracking
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_key = '$' 
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_key] = word

        # starting from each cell
        rows, cols = len(board), len(board[0])
        matchWords = []

        def backtrack(r, c, parent):
            letter = board[r][c]
            currNode = parent[letter]

            word_match = currNode.pop(word_key, False)
            if word_match: matchWords.append(word_match)
            board[r][c] = '#'
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r1, c1 = r + x, c + y
                if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols: continue
                if not board[r1][c1] in currNode:
                    continue
                backtrack(r1, c1, currNode)
            board[r][c] = letter

            if not currNode:
                parent.pop(letter)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    backtrack(r, c, trie)
        return matchWords

# Version 1 - Iterative BFS Solution
# Unfortunately this function is quite memory intensive because:
#   It stores a set of all the preceding letters for each of the letters in the queue
#   so worst case space complexity of O(n^2)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = None

def addToTrie(word, node, num):
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.val = num

# Helper function to return tuples which are the coords of the neighbours of a letter
def neighbours(r, c, maxR, maxC):
    return [tup for tup in [(r, c + 1), (r - 1, c), (r, c - 1), (r + 1, c)] if (0 <= tup[0] < maxR) and (0 <= tup[1] < maxC)]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        if not board or not words:
            return output
        
        # Create a Trie and add all the words to it
        root = TrieNode()
        for wordNum, word in enumerate(words):
            addToTrie(word, root, wordNum)
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                letter = board[row][col]
                if letter in root.children:
                    #For each letter we need three queues:
                    #One for nodes in which the letter could be a child
                    nodeQ = [root.children[letter]] 
                    # One for coordinates of the letter
                    coordQ = [(row, col)]
                    # One for sets of coordinates of the letters before it that are considered part of the word (initially an empty)
                    usedQ = [{(row, col)}]
                    while nodeQ:
                        curNode = nodeQ.pop(0)
                        curCoord = coordQ.pop(0)
                        curUsed = usedQ.pop(0)
                        for nb in neighbours(curCoord[0],curCoord[1], rows, cols):
                            if (nb[0], nb[1]) not in curUsed and board[nb[0]][nb[1]] in curNode.children:
                                    nodeQ.append(curNode.children[board[nb[0]][nb[1]]]) # The node in which the neighbouring letter could be a child
                                    coordQ.append((nb[0], nb[1])) # The coordinates of the neighbouring letter
                                    nextUsed = curUsed | {(nb[0], nb[1])} # The set of coordinates of letters that could precede the neighbouring letter in the word
                                    usedQ.append(nextUsed)
                        # If the current letters node.val exists.
                        if curNode.val != None: 
                            # If it does then add to the output the word in "words" at index = node.val
                            # Set node.val to None so that the word won't be added again if it is found again
                            output.append(words[curNode.val])
                            curNode.val = None
                            
        return output


# Helper functions for debugging

# def findInTrie(word, node):
#     for char in word:
#         if char not in node.children:
#             return None
#         node = node.children[char]
#     return node.val

# def printTrieWord(word, node):
#     for char in word:
#         print(node.children, node.val)
#         node = node.children[char]