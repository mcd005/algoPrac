'''
https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

Greedy algorithm. For each iteration we are only checking if the current segement is overlapping with the adjacent segment. 
The closest we get to seeing if the local optimum choice is the same as the global optimum choice is when we check the lenghts of the segments
i.e. if segment 1 doesn't extend as far left as segment 2 then we assume it is less likely to overlap with subsequent segments

Time complexity         O(n)
Space complexity        O(n)  
'''


#Helper function
def isOverlapping(I, J, a, b):
    if (a[J] <= b[I] <= b[J]) or (a[J] <= a[I] <= b[J]): #i.e. if segment i starts or ends within seg j
        return True
    else:
        return False

def solution(A, B):
    N = len(A)
    
    #Edge case check
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    #Starting from the back of the arrays because the segments are sorted by their ends
    #Iterate backwards through the arrays  
    stack = [N - 1]
    for i in range(N - 2, -1, -1):
        if not isOverlapping(i, stack[-1], A, B):
            stack.append(i)
        else:
            #proceed with whichever segement has the rightmost left end
            if A[stack[-1]] < A[i]:
                stack.pop(-1)
                stack.append(i)
            
    return len(stack)