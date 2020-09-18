'''
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

The naive solution would be to check all possible subarrays and see which has the max sum. The problems is this solution has an O(n^2) runtime
Instead we implement Kadanes algorithm

Time complexity     O(n)
Space complexity    O(1)
'''

def solution(A):
    currentMax = A[0]
    globalMax = A[0]
    
    
    for i in range(1,len(A)):
       currentMax = max(currentMax + A[i], A[i])
       globalMax = max(currentMax, globalMax)
       '''
       If current subarray + A[i] is smaller than just A[i], then the current subarray could NEVER be the max subarray because it's neighbour, A[i], is already bigger just by itself
       Indeed if the current subarray started at index 2 for example, then we'd know that it would be impossible ANY subarray starting at index 2 to be the max subarray
       This is why Kandanes algorithm is faster. We don't need to check the rest of the (n - i + 1) possible subarrays for each ith element
       We instead assume that the max subarray starts at A[i] and check if this assumption holds each iteration
       It may not, in which case the max subarray starts at A[i + ...] and so on until we have iterated through the whole array
       '''
       
    return globalMax