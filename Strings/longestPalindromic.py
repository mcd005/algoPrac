# https://leetcode.com/problems/longest-palindromic-substring/
# Version 1
# Iterate through the string
# Check if a char is either
#       The same as its neighbour aa
#       The same as its neighbours neighbour aba
# If it is begin expanding out until the letters are not the same
# Each time check if the length of the palindrome is greater than max
# Time complexity       O(n^2)
# Space complexiy       O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 1
        n = len(s)
        for i in range(n):
            j, k = 1, 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                j += 1
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            if (2 * j - 2) > (end - start):
                start, end = i - j + 2, i + j
            elif (2 * k + 1 - 2) > (end - start):
                start, end = i - k + 1, i + k
        return s[start:end]
        
# Version 2 - a slighlty more Pythonic way of expressing 
# the same logic as in V1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s

        last_successful_length = 1
        last_successful_start = 0

        for right in range(1, len(s)):
            odd_start = right - last_successful_length - 1
            even_start = right - last_successful_length

            odd = s[odd_start:right + 1]
            even = s[even_start:right + 1]

            if odd_start >= 0 and odd == odd[::-1]:
                last_successful_start = odd_start
                last_successful_length += 2
            elif even == even[::-1]:
                last_successful_start = even_start
                last_successful_length += 1

        return s[last_successful_start: last_successful_start + last_successful_length]