'''
Porblem Description: https://app.codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/

The question we are trying to answer with the algorithm is:
    What is the maximal overall score that can be achieved?
    
For the game to finish, the pebble has to land on the N-1 square. So the sub-problem/sub-question is:
    What is the maximal score among the squares that are a dice roll away from N - 1? (i.e the 6 preceding squares)
    If we have this score, then the maximal overall score = A[N - 1] + maximal score in 6 preceding squares

However the maximal score in the 6 preceding squares is based on the maximal score in the 6 squares preceding each of those squares. And so on.

So we use a bottom up approach. The smallest sub-problem is "What is the maximal score of the first square?" which is simply the value of the first square.
From there we can ask "What is the maximum score amongst the previous (up to 6) squares?" and there is no need to solve any sub-problems. Just check the vlau

Time complexity         O(n)    

Usually a nested loop would indictate O(n^2) but since j only iterates a max of 6 times this can be treated as a constant time operation

Space complexity        O(1)
'''

def solution(A):
    N = len(A)
    
    for i in range(1, N):
        maxInPrev6  = A[i - 1]
        for j in range(i - 1 , i - 7, -1):
            if j < 0:
                break
            else:
                maxInPrev6  = max(maxInPrev6, A[j])
        A[i] += maxInPrev6
    
    return A[N - 1]