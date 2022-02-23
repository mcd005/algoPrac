# https://leetcode.com/problems/set-matrix-zeroes/
# Version 1 - Mark rows and cols for zeroing, being careful not to lose important info
# Time complexity       O(mn)
# Space complexity      O(1)
# See cpp for even more concise
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        is_first_row_zero = False
        is_first_col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0 or j == 0:
                        if i == 0:
                            is_first_row_zero = True
                        if j == 0:
                            is_first_col_zero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        if is_first_row_zero:
            matrix[0] = [0] * n
        if is_first_col_zero:
            for i in range(m):
                matrix[i][0] = 0 

'''
The naive O(1) approach would be to determine if a zero was in a row and then set that row to zero
However that would mean when we came to look at columns we would not be sure if it started as a zero or was set to a zero

So we need to make one pass to mark all the elements that should be set to zero and then another to actually set them
Usually this is done by negating a value however here each value is a signed int
We could replace them with a signed long in python but that wouldn't work in other languages

We only need to mark the rows and columns that need to change
So we should just mark the starts of the rows and columns to be zeroed

### Key Lessons ###
Retaining information depends on:
    Order information is stored: if you're not revisiting a cell it won't be overwritten
    Space given: a flag can only store two states but the number of differnet states for the first row col was 4
        Need to keep the info elsewhere
    When you do "value = evaluate boolean" value can flip if evaluation is done multiple times
'''