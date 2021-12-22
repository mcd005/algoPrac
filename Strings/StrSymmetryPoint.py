'''
https://app.codility.com/programmers/lessons/99-future_training/str_symmetry_point/

Initial check to see if the length of the string can allow for a valid reflection point
    i.e. can't have a reflection for an empty string or a string of even length

Then just iterate through the string with two pointers, one moving from 0 to N and the other from N - 1 to 0
Return the index at which they converge

Time complexity         O(n)
Space complexity        O(1)

An alternative approach would be the initial checks as above
Then reverse the string and compare it to the orginal
If they are the same return the midpoint

This solution however requires linar memory and would involve iterating through n elements twice
'''


def solution(S):
    N = len(S)
    
    if (N == 0) or (N % 2 == 0):
        return -1
    
    for i in range(N):
        if S[i] != S[N - 1 - i]:
            return -1
        elif (i == N - 1 - i):
            return i