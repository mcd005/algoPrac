'''
Problem Description: https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

A profit is only possible in a subarray that starts in with a local minimum  \_/
The magnitude of the profit is given by difference between the value of the local minimum and maximum in that subarray

We start by assuming that the first point is a local minimum
We then iterate though the array
If the encountered element is bigger then we have a new max in the subarray
    We calculate the profit and if it is bigger than the max profit seen so far it is stored
If the encountered element is smaller then we have a new local minimum and thus are examining a new subarray
    Previous local maxima are forgotten because of the chronolgical contraints placed by the question (i.e. indexs represent days where 0 is a day before 1)

Time complexity     O(n)
Space complexity    O(1)
'''

def solution(A):
    N = len(A)
    if (N == 0):
        return 0

    peak = A[0]
    trough = A[0]
    diff = 0

    for i in range(1,N):
        if A[i] > peak:
            peak = A[i]
            diff = max(diff, peak - trough)
        elif A[i] < trough:
            trough = A[i]
            peak = trough

    return diff