# https://leetcode.com/problems/word-search
# Version 1 - Classic DFS
# Time Complexity       O(n)
# Space Complexity      O(n)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, i, j, word_idx):
        if word_idx == len(self.word):
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.word[word_idx] != self.board[i][j]:
            return False
        tmp = self.board[i][j]
        self.board[i][j] = "#"
        found = self.dfs(i + 1, j, word_idx + 1) or self.dfs(i - 1, j, word_idx + 1) \
        or self.dfs(i, j + 1, word_idx + 1) or self.dfs(i, j - 1, word_idx + 1)
        self.board[i][j] = tmp
        return found