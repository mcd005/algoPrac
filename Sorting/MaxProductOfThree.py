'''
Problem Description: https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

Sort the array
If any of the integers are positive:
    Greatest triplet product is either the two values closest and the most positive
    Or the three most positive
Else
    The greatest triplet product is the three least negative integers

Time complexity     O(NlogN)    i.e. the time complexity of sort which I believe is a Quicksort implementation in Python
Space complexity    O(1)        I believe sort() is in place
'''

def solution(A):
    A.sort()
    if A[-1] < 0:
        return A[-3] * A[-2] * A[-1]
    else:
        return max( (A[0] * A[1]) , (A[-3] * A[-2]) ) * A[-1]