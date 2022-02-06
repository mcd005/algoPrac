class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # We build our 2D prefix sum
        pre = [[0 for j in range(n)] for i in range(m)]
        pre[0][0] = matrix[0][0]
        for i in range(1, m):
            pre[i][0] = pre[i - 1][0] + matrix[i][0]
        for j in range(1, n):
            pre[0][j] = pre[0][j - 1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                pre[i][j] = matrix[i][j] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]

        num_submatrices = 0
        for i in range(m):
            for j in range(n):
                for k in range(i, m):
                    for l in range(j, n):
                        if pre[k][l] \
                           - (i > 0)*(pre[i - 1][l]) \
                           - (j > 0)*(pre[k][j - 1]) \
                           + (i > 0 and j > 0)*(pre[i - 1][j - 1]) \
                               == target:
                               num_submatrices += 1

        return num_submatrices
'''
m x n is m rows and n columns

Brute force would involve looking at all possible submatrices and seeing what they sum to and then checking 
if that sum equals target

If we take each square as the top left corner of a submatrix, then the submatrices it accounts for are
1x1, 1x2 ... 1xn
2x1  2x2 ... 
3x1
mx1           mxn
That is mxn possible for each mn cells

How do we reuse compuation? 
Or how do we query a submatrix in O(1)?
    Top right corner is here, bottom right is here. What is the sum?
    We can build a 2D prefix sum
Ok that allows us to query any given submatrix in constant time but we still have many submatrices
How do we check them efficiently?
    At the moment my plan is to iterate over every cell and treat it as the top left as described above, whereby I enumerate
    all of it's possible sumatrices
    If the cells only held positive values you could quite easily shrink or grow you query area as necessary
    What rationale do we use with sliding window and the two corners of the submatrix?
    Is there a Kadanes like approach to this?
How do we adapt the rationale from the 1D version of the problem?
    For each number in our prefix sum we asked
        Is the sum of the subarray that starts at zero and ends at i equal to k? If it is incremnet count
        Is there a previous subarray that summed to num - k? If there is that means the subarray fror there to here == k
    So for each number in our 2D prefix sum we need to ask
        Are their submatrices that lie within our current submatrix that we can subtract to make k
            Important differences though
                You can't just have one hash map that contains the submatrix sums for the all the possible submatrices
                contained within out current submatrix
                    The coords are important. The reduced submatrix must have 4 sides
                    We can only iterate along the current row and column of the current large submatrix in question
        I can currently only think of an O(n^2) to answer this question. For each column we iterate over all the rows
        and see what results
            Maybe I think of it the wrong way by tying to check for all three?


Algo 
    We build a 2D prefix sum
    Then we iterate over the 2D prefix sum
    If a cell equal target we know we can increment count
    Then we want to ask
        If we trim of some columns to the left of our matrix can we get k?
            We can answer this in O(1) because we have kept a map of the results in the row so far
        If we trim of of the rows in the top region of our submatrix can we get k?
            Like wise we can also answer this in O(1)
        If we trim a combo of a rows and cols?
            How would we have gained that info previously?
            What we need is some kind of map that says: 
                If you've trimmed to this column, these are the number of rows that give you a total of k

1 -1
-1 1

1 0
0 0

When we get to 5, we are looking for num - k i.e. previous submatrices that sum to 5

dp[i][j][k] gives the list of the sum of all matrices whose bottom right corner is at i j
Is it true that k must be less than or equal to 2?
No it's not true. You can have a 1xj or 

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
'''