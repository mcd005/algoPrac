'''
Problem description: https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/

We can use less than N blocks if there are intervals bounded by two numbers of the same value, where all numbers in between are greater than or equal to the bounds
e.g. 7 9 8 7
Rather than having 4 distinct blocks we can have a block of height 2 and a block of height 1 both sitting on a block of height 7

Every one of these intervals results in allows the total number of blocks to be one fewer than N

Time complexity     O(n)
Space complexity    O(n)
'''

def solution(H):
    N = len(H)
    if N == 1:
        return 1
    
    #Store the heights of the current group of blocks in a stack
    stack = [H[0]]
    blocksSaved = 0
    
    for i in range(1, N):
        #With this loop we're basically looking through the stack until we find a specified height that is greater than or equal to H[i]
        while stack and H[i] < stack[-1]:
            stack.pop()
        if stack and H[i] == stack[-1]:
            #If we find a height that is equal to we have one of the aforementioned intervals
            blocksSaved += 1
        stack.append(H[i])
        #If we find a height that is greater, it could be a value that lies within one of the intervals so we add it to the stack and move on to H[i + 1]
        #If neither has been found, the stack has been exhausted and is now empty
        #We start a new one with H[i] forming the foundation of the next group of blocks in which an interval could lie
    return N - blocksSaved
