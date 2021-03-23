# https://leetcode.com/problems/verifying-an-alien-dictionary
# Version 1
# Map for encoding and check each string with neighbour char-wise
# Time complexity       O(k + n * m) for n strings of average length m
# Space complexity      O(k) for an alphabet of length k, arguably constant
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        encoding = {char : val for val, char in enumerate(order)}
        prev = words[0]
        n = len(words)
        for i in range(1, n):
            cur = words[i]
            prevSize, curSize = len(prev), len(cur)
            j = 0
            while (j < prevSize and j < curSize):
                if encoding[cur[j]] > encoding[prev[j]]:
                    break
                elif encoding[cur[j]] == encoding[prev[j]]:
                    j += 1
                else:
                    return False
            if j == curSize and curSize < prevSize:
                return False
            prev = cur
        return True


# TODO try a solution that does encoding along these lines
# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         encoding = {char : val for val, char in enumerate(order)} #Flip this later
#         prev = encode(words[0], -1, encoding)
#         n = len(words)
#         for i in range(1, n):
#             cur = encode(words[i], prev, encoding)
#             if cur < prev:
#                 return False
#             prev = cur
#         return True
    
# def encode(cur, prev, encoding):
#         result = 0
#         radix = len(encoding)
#         m = len(cur)
#         for i in range(m - 1, -1, -1):
#             result = encoding[cur[i]] + result / radix
#         return  result