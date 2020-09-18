'''
Problem Description: https://app.codility.com/programmers/lessons/6-sorting/distinct/

A lazy Python way of doing this would be with collections.Counter() 
https://docs.python.org/2/library/collections.html#collections.Counter

    from collections import Counter
    
    def solution(A):
        values = Counter(A)
        return(len(values))

An implementation of this without collections would be:

Iterate through A 
    If the intger at A[i] has not been encountered before add it to the set "seen"
    If it has been encountered pass
Return the length of the set

Time complexity is O(N)
Space complexity is O(N)

Alternatively Method:
Could presort the array and then check pairs to see if they match, incrementing a count each time they don't
This would take O(nlogn) so would be slower but would be O(1) space complexity, so the tradeoff can be considered
'''

def solution(A):
    seen = {}
    for i in range(len(A)):
        if A[i] not in seen:
            seen[A[i]] = 1
    return(len(seen))
