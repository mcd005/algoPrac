# https://leetcode.com/problems/linked-list-cycle/
# Version 1 - Slow and fast pointer
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while slow and fast:
            fast = fast.next
            if fast:
                if fast == slow:
                    return True
                fast = fast.next
            slow = slow.next
        return False

# Version 2 - Use exception handling
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
'''
Can either store all the addresses of the nodes in a set
If we encounter an address that's already in the set we must have a cycle

Or we can use two pointers, one fast and slow
If there is a cylce the fast pointer will "lap" the slow one

Can be more concise if you check for next.next
'''