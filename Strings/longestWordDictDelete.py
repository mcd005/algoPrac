# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting

# Version 1 - fastest .py I could find on LC
# Time complexity       O(nm)
# Space complexity      O(m)
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = ""
        for w in d:
            diff = len(w) - len(result)
            # i.e. if current word is not longer than our current
            # candidate for the result, then current word can't possibly
            # be our end result
            if diff >= 0: 
                # If it's at least the same lenght though and lexicographically smaller
                # give it a go
                if diff > 0 or w < result:
                    try:
                        pos = -1
                        # Here we check if all the chars in word
                        # are present in s
                        # we skip to next word if index() can't find a char
                        # i.e. raises a value error
                        for c in w:
                            pos = s.index(c, pos + 1)
                        result = w
                    except ValueError:
                        pass
                    
        return result