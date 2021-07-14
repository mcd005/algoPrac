# https://leetcode.com/problems/number-of-ships-in-a-rectangle/

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

# Version 1 - Recursive quaternary search
# Time complexity       O(10log(nm))
# Space complexity       O(log(nm))
# where n and m are the side lengths of our original area
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        num_ships = 0
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1
            x_median = (bottomLeft.x + topRight.x) // 2
            y_median = (bottomLeft.y + topRight.y) // 2
            num_ships += self.countShips(sea, Point(x_median, topRight.y), Point(bottomLeft.x, y_median + 1))
            num_ships += self.countShips(sea, topRight, Point(x_median + 1, y_median + 1))
            num_ships += self.countShips(sea, Point(x_median, y_median), bottomLeft)
            num_ships += self.countShips(sea, Point(topRight.x, y_median), Point(x_median + 1, bottomLeft.y))
        return num_ships
    
##### Key Understandings #####
# You need to do a quaternary search
# topRight and bottomLeft can be the same point
#       Otherwise there would be no way to determine how many corners of a cell had a ship
# You need to be careful how you set your slice up the current area
#       If you do this incorrectly you could have overlap
#       This means the size of your search scope is not always shrinking and you could have an infinite loop
# You don't need store the coords in a data strucutre, just count occurences
# The starting case is a recursive case like any other. If you treat it differently it will cause problems