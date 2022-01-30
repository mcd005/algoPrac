class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pass


'''
0 0 1 1
0 1 2 3
0 1 1 1

  0 0 0
  0 1 0
  1 2 1
  1 3 1

From each point we want to know:
    what is the sum of the sub-row that ends here?
    what is the sum of the sub-col that ends here?
    what is the row of the sub-rectangle that ends here?

If we go in the other direction we can cover all our bases right?


At each i j we have the following submatrices whose bottom left corners are at i and j:  
1x1, 1x2, ... 1xj
2x1, 
From each point you can have up to ixj submatrices

Brute force would involve looking at all possible submatrices and seeing what they sum to and then checking 
if that sum equals target
You would do all the 1x1 submatrcies first
Then all the 1x2 submatrics
Then all the 2x2 submatrices
And so on until you did the single ixj submatrix

dp[i][j][k] gives the list of the sum of all matrices whose bottom right corner is at i j
Is it true that k must be less than or equal to 2?
No it's not true. You can have a 1xj or 
'''