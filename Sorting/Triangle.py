'''
Problem description: https://app.codility.com/programmers/lessons/6-sorting/triangle/

Pre-sort the array
Iterate through it the array checking these equalities

A[i] + A[i+1] > A[i+2]
A[i+1] + A[i+2] > A[i]
A[i+2] + A[i] > A[i+1]

If all three are met return 1
If the whole arrray has been iterated through and no triplets match this condition return 0

Time complexity 	O(NlogN) 	(i.e. time complexity of sort() which I believe is quicksort)
Space compexlity 	O(1)		(i.e. space complexity of sort() which I believe is in place)

For C++ solution care must be taken with integer overflow, based on the possible input values specified by the question
'''

def solution(A):
    if (len(A) < 3):
        return 0
    A.sort()
    for i in range(len(A) - 2):
        if (A[i] + A[i+1] > A[i+2]) and (A[i+1] + A[i+2] > A[i]) and (A[i+2] + A[i] > A[i+1]):
            return 1
    return 0