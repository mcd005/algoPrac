# https://leetcode.com/problems/knight-dialer/
# Version 1 - Recursive with memoisation
# See .cpp solution for the ideal solution 
# Time complexity      O(n)
# Space complexity     O(n)
class Solution:
    def knightDialer(self, n: int) -> int:
        self.valid_coords = {
            (0, 3), (1, 3), (2, 3),
            (0, 2), (1, 2), (2, 2),
            (0, 1), (1, 1), (2, 1),
                    (1, 0)
        }
        #  memo[i][y][x] which gives number of distinct numbers from coord (x,y) with i hops left
        self.memo = [[[-1 for x in range(3)] for y in range(4)] for i in range(n)]

        num_numbers = 0
        for coord in self.valid_coords:
            num_numbers += self.jump_from(coord, n - 1)

        return num_numbers % (10**9 + 7)

    def jump_from(self, coord, jumps_left):
        x, y = coord
        if self.memo[jumps_left][y][x] == -1:
            if not jumps_left:
                self.memo[jumps_left][y][x] = 1
            else:
                num_numbers = 0
                new_coords = [(x + 1, y + 2), (x + 2, y + 1),
                              (x + 2, y - 1), (x + 1, y - 2),
                              (x - 1, y - 2), (x - 2, y - 1),
                              (x - 2, y + 1), (x - 1, y + 2)]
                for new_coord in new_coords:
                    if new_coord in self.valid_coords:
                        num_numbers += self.jump_from(new_coord, jumps_left - 1)
                self.memo[jumps_left][y][x] = num_numbers

        return self.memo[jumps_left][y][x]

# Version 2 - Tabular DP (but gets TLE)
class Solution:
    def knightDialer(self, n: int) -> int:
        self.memo = {x: {y: 1 for y in range(4)} for x in range(3)}
        del self.memo[0][0]
        del self.memo[2][0]

        for jumps in range(1, n):
            temp = {x: {y: 0 for y in range(4)} for x in range(3)}
            del temp[0][0]
            del temp[2][0]
            for x in range(3):
                for y in range(4):
                    if x in temp and y in temp[x]:
                        new_coords = [(x + 1, y + 2), (x + 2, y + 1),
                                    (x + 2, y - 1), (x + 1, y - 2),
                                    (x - 1, y - 2), (x - 2, y - 1),
                                    (x - 2, y + 1), (x - 1, y + 2)]
                        for new_x, new_y in new_coords:
                            temp[x][y] += self.memo.get(new_x, {}).get(new_y, 0)
            self.memo = temp

        return sum(self.memo[x][y] for x in self.memo for y in self.memo[x]) % (10**9 + 7)

# Version 3 - Recursion with cache. Also each number can only legally go to a list of other numbers
from functools import cache
moves = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        6: [1, 7, 0],
        7: [2,6],
        8: [1,3],
        9: [2,4],
        0: [4,6],
    }

class Solution:
    
    @staticmethod
    @cache
    def dp(loc, n):
        if n == 1:
            return 1 
        else:
            total = 0
            for next_loc in moves[loc]:
                total += Solution.dp(next_loc, n-1)
            return total
        
    def knightDialer(self, n: int) -> int:   
    
        if n == 1:
            return 10
        return sum(Solution.dp(start, n) for start in moves) % 1000000007

### Key Lessons and Understandings ###
# Think of base case first in recursion. Make sure there is no overlap in responsibility between base case and recursive case
# Consider how much recomputation your recursion will do. Might be worth doing memoisation straight away
# Consider how you can reduce the decisions the code has to make
