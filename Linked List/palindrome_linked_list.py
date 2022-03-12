# https://leetcode.com/problems/palindrome-linked-list/
# Version 1 - Slow and fast pointer
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        midpoint = slow
        tail = self.reverse(midpoint, midpoint.next, None)
        is_palindrome = True
        front, back = head, tail
        while back is not midpoint:
            if front.val != back.val:
                is_palindrome = False
            front = front.next
            back = back.next
        self.reverse(None, tail, midpoint)
        return is_palindrome

    def reverse(self, prev, node, terminating):
        while node is not terminating:
            node.next, node, prev = prev, node.next, node
        return prev

'''
We use a slow and fast pointer to find the midpoint of the list
    We need to be careful about whether the list is even or odd
We save the ptr of the midpoint
We reverse the list from that point, making sure to save the old tail
We then iterate inwards from head and tail to determine if the list is palindromic
Once we've reached the halfway point we can stop searching
We unreverse the list using the old tail
'''