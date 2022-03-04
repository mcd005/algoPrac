# https://leetcode.com/problems/longest-common-prefix/
# Version 2 - Use the lexicographical ordering
# The prefix is most likely to diverge earliest between the two elements that are 
# lexicographically the furthest apart
# So we determine what they are and then compare them character by character until the corresponding characters differ
# Time complexity       O(nl + l) where n is the len of strs, l is the average length of a str 
# Time complexity       O(1) where n is the len of strs and m is the longest str
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # s_min will be the lowest in lexicographical order and s_max will be the greatest
        s_min, s_max = strs[0], strs[0]
        for str in strs:
            if str < s_min:
                s_min = str
            elif str > s_max:
                s_max = str
        for i, char in enumerate(s_min):
            if char != s_max[i]:
                return s_min[:i]
        return s_min

# Version 1 - Trie
# Time complexity       O(nl) where n is the len of strs, l is the average length of a str
# Time complexity       O(m) where m is the len of strs and m is the longest str
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = {}
        for word in strs:
            node = root
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['#'] = '#'

        output = []
        child, node = None, root
        while child != '#' and len(node) == 1:
            child, node = list(node.items())[0]
            if child != '#':
                output.append(child)

        return "".join(output)

'''
Build a trie
Set a pointer to the root of the trie. This is current node
While the node has one child, add the letter that child denotes to our result
Return constructed prefix at the end
'''
