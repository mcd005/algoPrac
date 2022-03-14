# https://leetcode.com/problems/minimum-window-substring/
# Version 1 - Sliding window
# Time complexity       O(n + m)
# Space complexity       O(m)
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        begin, end = 0, 0
        targets = Counter(t)
        window_count = {char: 0 for char in targets}
        num_absent = len(window_count)
        n = len(s)
        front = 0
        for back in range(n):
            while front < n and num_absent > 0:
                if s[front] in window_count:
                    window_count[s[front]] += 1
                    if window_count[s[front]] == targets[s[front]]:
                        num_absent -= 1
                front += 1
            if num_absent > 0:
                return s[begin:end]
            if s[back] in window_count:
                if window_count[s[back]] == targets[s[back]]:
                    num_absent += 1
                    if begin == end or end - begin > front - back:
                        begin, end = back, front
                window_count[s[back]] -= 1
        return s[begin:end]

'''
Create a counter that will be used to keep track of the occurences of each char in t that is in our window
Also initalise a variable num_absent that is equal to the length of our counter
While this varaible is not zero we widen our window
When a char is introduced to the window and it's in our counter, we increment the count
Only when that count hits the target count we decrement num_absent
When num_abset is zero we narrow the window
For each window narrowing we save the substring contanined in the prev window
When narrowing causes one of the cahnge in counts to deviate in target, and num absent to go non zero
    we save prev string as the min so far
'''
