'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

~~~Version 1~~~
Walk the linked list keeping note of postion of 1s
Walk through array of positions, adding relevent power of 2

Time complexity         O(n)
Space complexity        O(n)

~~~Version 2~~~
Walk the linked list
Cosntructing the binary number as a string as you go
Then convert number to base 10 using Python built-in

Time complexity         O(n)
Space complexity        O(n)
'''

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
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

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = ''
        while head:
            number += str(head.val)
            head = head.next
        return(int(number,2))