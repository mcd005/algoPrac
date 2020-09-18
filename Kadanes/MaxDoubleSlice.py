'''
A double slice is basically all the numbers from X+1 to Z-1, excluding Y
The smallest value X can take is 0 and the largest value Z can take is N - 1
So maybe run Kadanes on range(1,N - 1) and exclude the smallest value, which would be the element at index Y

We need to keep track of what the min is in the slice that is the max sum slice?
At present we are returning the min value of the last slice
If we never encounter a new slice then the minInSlice is the globalMin?

When will the answer not be just the max slice?
    When an element in the max slice is negative
    Then it can be inclduded to increase the sum of the max slice


Is a possible stragegy to find the biggest slice and the exclude its smallest element?
    What if the smallest element is at the start of the subarray?
        Then it would be invalid to exlcude?
        Same at the end of the subarray
    Also a problem is the start, then end and the middle could be the reason why it is the biggest subarray
    
Could maybe find the indicies of the biggest slice, then iterate through those from start + 1 to end-1 and exclude smallest in that range?

When iterating we have to stop short of N by two elements. Z must be less than N by at least 1 and the double slice must exclude Z

[0, 10, -5, -2, 0]

Maybe check if we are above a certain number of iterations before keeping track of mins


[-8, 10, 20, -5, -7, -4]
Got 20 expected 30

[6, 1, 5, 6, 4, 2, 9, 4]
got 27 expected 26
'''

def solution(A):
    N = len(A)
    if N == 3:
        return 0
    
    localMax = A[1]
    globalMax = A[1]
    currMin = A[1]
    minInSlice = 0
    
    for i in range(2,N - 1):
        if localMax + A[i] < A[i]:
            currMin = A[i]
        else:
            currMin = min(currMin, A[i])
            
        localMax = max(localMax + A[i], A[i])
        prevGlobal = globalMax
        globalMax = max(globalMax, localMax)
        
        if prevGlobal != globalMax: #i.e. if a new max sum has been found
            minInSlice = currMin
    
    if minInSlice < 0:
        return globalMax - minInSlice
    else:
        return globalMax