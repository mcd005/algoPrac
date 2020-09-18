'''
Is it correct to say that the the leader in each subarray divided by the equileader is equal to the leader for the whole array?
    Yes
    
If there are no leaders in the array can there be an equileader?
    No
    
So the solution is to first establish the candidate for leader
Then to count to verify if it is leader
If it isn't then there are zero equileaders
If it is then we iterate through the array again and keep track of the occurrences of leader in the left and right hand sides of the array (i.e. left and right of the index for the current iteration). We can do this in constant time because we already have the count of the leader
Each time leftCount > leftSize/2 and rightcount> rightSize/2 we have an equileader; the equileader count is incremented

Time complexity     O(n)
Space complexity    O(1)
'''
def solution(A):
    N = len(A)
    if N == 1:
        return  0
        
    size = 0
    for i in range(N):
        if size == 0:
            candidate = A[i]
            size += 1
        else:
            if A[i] != candidate:
                size -= 1
            else:
                size += 1
    
    count = 0
    for i in range(N):
        if A[i] == candidate:
            count += 1
            
    if count < N // 2:
        return 0
    else:
        equis = 0
        leftCount = 0
        rightCount = count
        for i in range(N):
            if A[i] == candidate:
                leftCount += 1
                rightCount -= 1
            if (leftCount > (i + 1) // 2) and (rightCount > (N - i - 1) // 2):
                equis += 1
    
    return equis