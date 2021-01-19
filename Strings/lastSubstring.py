# https://leetcode.com/problems/last-substring-in-lexicographical-order/
# See .cpp for more explanations and more efficient solutions

# Version 1 - brute force
# This was simply to aid my understanding of the problem
# Not acceptable because of poor time and space complexity
#
# Time complexity       O(n^2 + nlogn)
# Space complexity      O(n)
class Solution:
    def lastSubstring(self, s: str) -> str:
        substrings = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substrings.add(s[i:j + 1])

        return (sorted(substrings)[-1])

# Version 2 - Imagine that each suffix is a base 26 number 
# Converting from this number to decimal would go something like:
# (first char in suffix ASCII value * base**n-1) + (second char in suffix ASCII value * base**n-2) + ... and so on 
# Now instead imagine the base is equal to the number of unique chars in the string
# If we start from end of the string and iterate left
# we can convert each suffix into a decimal value in constant time
# and then compare it to subsequent suffixes in constant time
class Solution:
    def lastSubstring(self, s: str) -> str:
        index = {c: i for i, c in enumerate(sorted(set(s)))}
        base, maxVal, curVal, maxIdx = len(index), 0, 0, 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            curVal = index[s[i]] + curVal / base
            if curVal >= maxVal:
                maxVal = curVal
                maxIdx = i


# Version 3 - do somehthing like this: https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation
# Find the indices for all candidate suffixes
# increment each index and compare each of the candidates subsequent letters, eliminating smaller ones accordingly
# do this until only one candidate remains. This is our answer

#TODO understand this
class Solution:
    def lastSubstring(self, s: str) -> str:
    
        max_c = max(s)
        last_max_c = None
        parts = []
        
        for i, c in enumerate(s):
            if c == max_c:
                if i> 0 and s[i - 1] == max_c:
                    continue
                                    
                if last_max_c is not None:
                    parts.append(s[last_max_c:i])
                    
                last_max_c = i
                
        parts.append(s[last_max_c:])
        # print(parts)
        
        max_p, max_p_i = parts[0], 0
        for i, p in enumerate(parts):
            if p > max_p:
                max_p = p
                max_p_i = i
        
        return ''.join(parts[max_p_i:])
