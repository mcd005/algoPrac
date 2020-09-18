'''
Not yet solved
'''

def isTriangular(arr, P, Q, R):
    if (arr[P] + arr[Q] > arr[R]) and (arr[Q] + arr[R] > arr[P]) and (arr[R] + arr[P] > arr[Q]):
        return True
    else:
        return False
    
def solution(A):
    N = len(A)
    if N < 3:
        return 0
        
    num_triangular = 0
    j,k = 1,2 #i is the back, j is the middle and k is the front of the caterpillar
    
    for i in range(N - 2):
        while (isTriangular(A, i, j, k) == False) and (k < N):
            k += 1
            while (j < k - 1) and (isTriangular(A, i, j + 1, k) == True):
                j += 1
                num_triangular += 1

        num_triangular += 1