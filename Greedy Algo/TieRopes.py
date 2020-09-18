'''
Problem Description: https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

Iterate through and keep typing ropes together until you exceed K
Once this occurs, stop tying and move on to the next section of rope, starting a new chain of tied ropes

Time Complexity     O(n)
Space complexity    O(1)
'''

def solution(K, A):
    total_prev_lengths = 0
    numGtrK = 0 
    
    for i in range(len(A)):
        total_prev_lengths += A[i]
        if (total_prev_lengths >= K):
            numGtrK += 1
            total_prev_lengths = 0
    
    return numGtrK