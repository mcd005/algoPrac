class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass

'''
True brute force
    Enumerate all the possible substrings
    If there is a total count of k among the non-dominant characters then that substring is valid, save it's length
    Compare it's length to the other valid substrings


Sliding window
    We have a value called dominant count
    This gives the count of the most common element in a substring
    We widen out window until it's size is equal to dominant count + k
    We narrow the widnow
        AS we narrow we check if elements we are leaving behind are the dominant ones
    We move the front of the window forward each element counted we increment in out counter
    If that number exceeds current dominant count it's the new dominant count
    We also have a total count for the chars in the window, but this can just be given by the size of the window
    If the size of the window is equal to dominant count + k, we have a valid window, save it's length
    
0123456
AABABBA
  b
    f

move forward forward while f < n and (f - b) + 1 <= leader_count + k
    increment forward
    increment count of whatver forward moved to
    check if that count makes a new leader
move back forward otherwise
    check what character we're leaving behind
    decrement it's count in the dict
    if that count was the leader, decrement the leader

counters = { A:1, B: 2}
leader = A
leader_count = 1
max = 1

Iterate through the sting and look at all the sequences

We need to find a substring were there is one dominant char and only k other non-dominant

We could do it greedily

2A 1B 1A 2B 1A
'''