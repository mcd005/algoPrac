# https://leetcode.com/problems/spiral-matrix/submissions/ 
# Time complexity       O(n*m)
# Space complexity      O(n*m) (constant if you don't include output)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        i, j = 0, 0
        min_i, min_j = 0, 0
        max_i, max_j = len(matrix), len(matrix[0])
        direction = "right"
        while min_i != max_i and min_j != max_j:
            if direction == "right":
                if j < max_j - 1:
                    output.append(matrix[i][j])
                    j += 1
                else:
                    direction = "down"
                    min_i += 1
            elif direction == "down":
                if i < max_i - 1:
                    output.append(matrix[i][j])
                    i += 1
                else:
                    direction = "left"
                    max_j -= 1
            elif direction == "left":
                if j > min_j:
                    output.append(matrix[i][j])
                    j -= 1
                else:
                    direction = "up"
                    max_i -= 1
            elif direction == "up":
                if i > min_i:
                    output.append(matrix[i][j])
                    i -= 1
                else:
                    direction = "right"
                    min_j += 1
        output.append(matrix[i][j])
        return output

# Version 2 - Code golf from LC
# Upack the first row then repack as a list
# Then unpack the subsquent rows and zip them so the coulmns are now in a list not the rows
# Reverse them so the last column is now the first entry in the list
# Recur
# Time complexity       O(n*m)
# Space complexity       O(nm) (O(min(m, n)) calls on the stack)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
'''
Maybe we just want a state machine setting direction and then a while loop incrementing based on direction
We just need to adjust bounds as we go

min_i, min_j = 0
max_i, max_j = len(matrix), len(matrix)
'''