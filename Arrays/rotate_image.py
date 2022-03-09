# https://leetcode.com/problems/rotate-image/
# Version 1 - Use idx maths
# Space Complexity      O(n^2)
# Space Complexity      O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n - 1 - i):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

# Version 2 - Reverse the rows, unpack them and them zip them together as columns
# Space Complexity      O(n^2)
# Space Complexity      O(n^2)
class Solution:
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])

# Version 3 - A functional "proper" version of 2 (which actually is a list of tuples)
# Space Complexity      O(n^2)
# Space Complexity      O(n^2)
class Solution:
    def rotate(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))

# Version 4 - The same as 4 but with list comprehension
# Space Complexity      O(n^2)
# Space Complexity      O(n)
class Solution:
    def rotate(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]

# Version 5 - What NOT to do. Probably shouldn't use a generator on an underlying structure that is changing
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        rotated = (element for old_col in zip(*matrix) for element in reversed(old_col))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = next(rotated)
'''
Can do this recursively where were move top left quadrant to top right, move top right to bottom right, bottom right etc
Base case is the a square with 4 cells where we just swap each of the cells
Two problems though
    Not an easy way to do it with an odd number for n
    Would have to do stacks of matrix slicing to define a square

So realistically should do it with idx maths
Iterate as we usually would
    Would need to make sure we step inward once each time though
And perform a 4 way swap operation
    e.g. matrix[0][1] -> matrix[1][3] -> matrix[3][2] -> matrix[2][0]
    e.g. matrix[1][1] -> matrix[1][2] -> matrix[2][2] -> matrix[2][1]
    e.g. matrix[i][j] -> matrix[j][n - 1 - i] -> matrix[n - 1 - i][n - 1 - j] -> matrix[n - 1 - j][i]
'''