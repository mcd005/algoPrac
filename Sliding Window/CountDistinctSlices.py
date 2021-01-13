'''
Problem description: https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/

Caterpillar/sliding window method

Have the forward pointer advance until the end of the array or until a non-distinct integer has been encountered.

The number of distinct slices between the front and the back pointer is actually (x/2)*(x + 1) 
where x is the number of elements between the two pointers. 

Because this is the same as the sum as the first x natural numbers what we instead do is count the number of elements between the two pointers, advance the back pointer and repeat until the two pointers are at the same index

From here the forward pointer continues to progress again.

Time complexity     O(n)    At every step we only move the front or the back of the caterpillar and never more than n
Space complexity    O(m)    The pointers and count of disitnct are const no matter the size of the input. However the array used to track which ints are present in a slice scales with M.
'''

def solution(M, A):
    N = len(A)
    front, back = 0,0
    present = [0] * (M + 1) #To mark which integers are present in the slice
    distinct = 0 #The count of distinct slices
    
    for back in range(N):
        while (front < N) and (present[A[front]] != 1):
            present[A[front]] = 1
            front += 1
        distinct += front - back #Still may be an issue of double counting
        present[A[back]] = 0
        
    return min(distinct, 1000000000)