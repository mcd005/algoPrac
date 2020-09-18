'''
Sort from largest to smallest radius
Walk through and for each check its radius plus minus its index
Then from that point walk trhough and check all subsquent points that match
Would probably be O(N^2) though 
    O(N) for each 
    
Sort
Then for each circle we can say it at least contains any circle with an origin within the radius
And then some circles whose origins are outside but there index +- radius = index +- radius



Walk through and mark a boundaries as incoming and outgoing
Starting with the lefmost incoming boundary walk along the line and when you encounter an incoming boundary, begin counting subsqeuent incomign boundaries

Try a multiplier as well?
Could do a recursive algo when you encounter a new boundary as it to start counting?
Maybe have a helper function called within bounds that?



Iterate through the A and determine the position of the lefmost left boundary and the rightmost right boundary (e.g. -4 and 8 in the example)
Iterate through A again and mark the positions of all the

Use these values to create an array that marks the positions of all the left boundaries
Convert this array to prefix sum array                                                     
Using the prefix sum array you can determine how many lef bondaries (and hence how many discs) lie between two intervals 

Possible to have the postiion map just keep in mind index 0 is equal to leftmost
And will have to make that conversion every time function is called

TO DO: explain the shifting
'''

def solution(A):
    N = len(A)
    leftmost = 0 - A[0]
    rightmost = 0 + A[0]
    for i in range(1, N):
        if A[i]:
            leftmost = min(i - A[i], leftmost)
            rightmost = max (i + A[i], rightmost)
        
    POLB = [0]*(1 + rightmost - leftmost)
    for i in range(N):
        if A[i]:
            POLB[(i - A[i]) - leftmost] += 1
    print(POLB)
    
    M = len(POLB)
    prefPOLB = [0] * (M + 1)
    for i in range(1,M + 1):
        prefPOLB[i] = prefPOLB[i - 1] + POLB[i - 1]
    print(prefPOLB)
    
    count = 0 
    for i in range(N):
        curCount = prefPOLB[i + A[i] - leftmost + 1]  - prefPOLB[i - A[i] - leftmost] - 1
        print(curCount)
    