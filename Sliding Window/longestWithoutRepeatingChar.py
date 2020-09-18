'''
Problem description: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

Sliding window approach

Keeping track of the chars in the substring using a set (because of the lookup in constant time)
Advance the front pointer until a duplicate is encountered or until the end of the string
If either occurs, check if the length of the substring is greater than the length of the longest valid substring seen so far
Advance the backward pointer until the first instance of the duplicate is no longer in the substring (i.e the left end of the window has passed it)
Repeat until both pointers are at the end of the string

Time complexity         O(n)    At every step we only move the front or the back of the caterpillar and never more than n
Space complexity        O(n)    in the worst case scenario all chars in the string may be distinct
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
    
        seen = set()
        maxLength = 1 
        
        front = 0
        for back in range(n):
            while (front < n) and (s[front] not in seen):
                seen.add(s[front])
                front += 1
            maxLength = max(maxLength, front - back)
            seen.remove(s[back])
        
        return maxLength