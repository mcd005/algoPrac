'''
https://leetcode.com/problems/jewels-and-stones

Classic HashMap Problem

Time complexity     O(n)    where n is the length of string S
Space complexity    O(m)    where m is the length of string J
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        count = 0
        for stone in S:
            if stone in J:
                count +=1
        return count