#Naive would be to try all possible subarrays, however time complexity would be O(N^2)
#Could try Kadanes

#Starting with slice 01
#Work out it's value
#Then ask if the neighbouring slice is

#Does minimal mean th value closest to zero? Because Python min is value closest to negative inf

import random

def generatePrefSum(array):
    N = len(array)
    prefSum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefSum[i] = prefSum[i - 1] + array[i - 1]
    return prefSum
    
def sliceAv(arr, P, Q):
    return abs( (arr[Q + 1] - arr[P])/(Q - P + 1) )

def solution(A):
    if len(A) == 2:
        return 0
    ps = generatePrefSum(A)
    currentMin =  globalMin = sliceAv(ps, 0, 1)
    startPos = 0
    for i in range(1, len(A) - 1):
        currentMin = min( sliceAv(ps, i, i+1) , sliceAv(ps, startPos, i+1))
        if currentMin < globalMin:
            globalMin = currentMin
            startPos = i
    return startPos