# https://leetcode.com/problems/word-break-ii

# Version 2 - DP with memoisation
# If we know how many valid sentences are in any given substring
# then we know all the valid sentences for the whole string
# But we save time by only slicing into substrings that will at least have a whole word
# And memoising the result for future queries, a benefit we don't get for V1
# Time complexity               O(mn^2) 
# Space complexity              O(n^2)
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

    
# Version 1 - Recursive
# Time complexity           O(n^2)
# Space complexity          O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.root = {}
        for word in wordDict:
            node = self.root
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['#'] = True

        self.s = s
        self.n = len(s)
        self.output = []
        self.check_suffix(0, [])

        return self.output

    def check_suffix(self, index, sentence):
        if index >= self.n:
            self.output.append("".join(sentence))
            return

        ptr = self.root
        cur_word = ""
        for i in range(index, self.n + 1):
            if '#' in ptr:
                self.check_suffix( i, sentence + ([" ", cur_word] if sentence else [cur_word]) )
            if i < self.n and self.s[i] in ptr:
                cur_word += self.s[i]
                ptr = ptr[self.s[i]]
            else:
                break

# Version 3 - Iterative with stacks. Not yet working
# TODO get working by fixing index control flow problem right 
# In the recursive is the way we are handling sentences correct?
# We skip an index when we encounter and EOW
#   What if we decrement in the EOW case
# And we're going to get stuck in an infite loop because we are going to keep checking if 
# t is an end of word marker
# It's possible we run into the same issues with the other base case
# Can we refactor to have logic for base cases in same place
# Maybe take inspo from the V1 cpp and don't use a trie
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = {}
        for word in wordDict:
            node = root
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['#'] = True

        i, n = 0, len(s)
        ptr = root
        stack, sentence, output = [], [], []
        cur_word = ""
        base_case = False
        while i < n:
            if '#' in ptr:
                stack.append((ptr, i))
                if sentence:
                    sentence.append(" ")
                sentence.append(cur_word)
                ptr = root
                if i == n - 1:
                    output.append("".join(sentence))
                    base_case = True
            elif s[i] in ptr:
                cur_word += s[i]
                ptr = ptr[s[i]]
            elif s[i] not in ptr:
                base_case = True
            if base_case:
                if not stack:
                    break
                ptr, i = stack.pop()
                cur_word = sentence.pop()
                sentence = sentence[:-1]
                base_case = False
            i += 1

        return output

# The entire word including spaces must form a sentence
# You can break up s however you like, so long as each remaining word is in word dict

# We construct a trie
# We start with a pointer to the root of the trie
# We iterate over the characters in s
# If the current node marks the end of the word, we put it and the relevant index in the stack
#   we would then recursively begin this process again
# If char is a child of the current node, we advance the pointer to that child
# If char is not in the children of s, we know there are no valid sentences in that suffix
#   we pop the call off the top of the stack and proceed with that
# If the recursive call we have made is to an index that beyond the length of the array, we have hit base case
#   we can append all the words in the stack to the output

# We need to be able to do DP
# When you find a word that ends at index i, you need to be able to ask:
#   How many valid sentences lie between i and n - 1?
#   How many complete words lie between two ranges
# Surely that's quite hard to answer though?
#   There could be only one space inserted in that range
#   Or 2
#   Or n - 1 - i

# Insert all possible combinations of spaces and check if we have formed words
# Would be very intensive. The kind of thing we could make quicker with DP though
# How can computation be reusued there?

# Could you solve by saying you only have one space but you can use for any substring?

# c, a, t, s, a, n, d, d, o, g
# 'ca', 'at', 'ts' 'sa' 'an' 'nd' 'dd' 'do' 'og'
# 'cat' 'ats' 'tsa' 'san' 'and' 'ndd' 'ddo' 'dog'
# 'cats' 'atsa' 'tsan' 'sand' 'andd' 'nddo' 'ddog' 'dog'z
# "c, atsanddog", "ca, tsanddog", "cat, sanddog", "cats, anddog"

### Key lessons and understandings ###
# If char is not in the children of the current node of trie, the we know there are no valid sentences in that suffix
# If you're doing it recursive, write a recursive function first, then think about converting to iterative
# Every idea you have on less than 7.5 hrs sleep is basically worthless