'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Seperate these and consider time diffs
'''

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        '''number = ''
        while head:
            number += str(head.val)
            head = head.next
        return(int(number,2))'''
        
        bitPos = []
        currentPos = 0
        while head:
            if head.val == 1:
                bitPos.append(currentPos)
            currentPos += 1
            head = head.next
        MSB = currentPos
        
        result = 0
        for pos in bitPos:
            result += 2**(MSB - 1 - pos)
        return result

'''
Walk through keeping note of postion of 1s
Walk through array of positions, adding relevent power of 2
28 64 44 ave 45ms runtime

Or create a string of the number and convert using some kind of built in Python function
40 36 36 