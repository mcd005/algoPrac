'''
Problem Description: https://app.codility.com/programmers/lessons/8-leader/dominator/

We use a verison of the algorithm suggested in 8.3 of this: https://codility.com/media/train/6-Leader.pdf

Basically the algorithm involves iterating though A, pushing each element on top of a stack
If the stack has a size of at least 2
    We check the top two elements of the stack every iteration
    If they are different from each other then they are both are popped off
In all other instances (stack empty, top of stack them same) we just continue pushing elements on top of the stack

Given these rules, all the values below the top of the stack will actually be equal
So rather than storing an entire stack in memory we can just store this value and the size of the stack as variables

Having iterated through all of A, this stored value will be the candidate for leader
We just need to iterate through A again and count it's occurrances  
If there are greater than N/2 occurrences it is indeed the leader
We return the index of an element whose value is the leader

Time complexity     O(n)
Space complexity    O(1)
'''

def solution(A):
    N = len(A)
    
    #Edge case to account for empty input
    if N == 0:
        return -1
    
    candidate = A[0]
    size = 1
    for i in range(1, N):
        if size == 0:
            candidate = A[i]
            size += 1
        else:
            if candidate != A[i]:
                size -= 1
            else:
                size += 1
    
    count = 0
    for i in range(N):
        if A[i] == candidate:
            count += 1
            index = i
    if count > (N // 2):
        return index
    else:
        return -1