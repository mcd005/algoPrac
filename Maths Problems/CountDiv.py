
#Problem Description: See the cpp solution
#Naive solution would be to iterate between A and B and take the mod of each value to work out if it is divisible by K. This would take O(N) time.

#An attempt to at an O(1) solution would be (B-A)/K, however this value will have a discrepancy if the start point A is not divisible by K.

#The size of the discrepancy is (A % K)//K and can thus be corrected for

#Time Complexity    O(1)
#Space Complexity   O(1)

def solution(A, B, K):
    if A % K == 0:
        return (B - A)//K + 1
    else:
        return ((B - A) + (A % K))//K
        
#NB: Aside from realising immediately this had a mathematical solution, this took a small amount of trial and error
