# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = self.get_linked_list_len(l1)
        m = self.get_linked_list_len(l2)

        ptr1 =


    def get_linked_list_len(self, node):
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def advance_ptr_x_times(self, x):
        pass


'''
Most straightfoward solution would be to reverse both lists then add them as you would on paper (starting from LSD)
O(n) time and space if recursive reversal. O(1) space if iterative reversal

We could put both nodes in stacks and then pop off the stack and add and carry as we go
O(n) time and space

Is there are O(1) space solution that doesn't involve reversing?
    Count the lenghts of both lists
    If one of the lists is shorter, advance the pointer on the longer list so it's in line with the shorter on 
    What to do if you have carries?
        Keep an array to mark where the carries are applied?
            Well then solution becomes O(n) space
        Mark the val in way to indicate carries
        How do we retrieve that info and apply it to upstream digits with O(1) space
        When we do a CLA we can mark which digits propagate or generate carries
        Then at the end we can inspect all the the bits and propagate carries as necesarry
        We can do this with two pointers


7 7 10 7

How about you assume the lists are the same lenght then add them digit wise
When you get to the end of one list
'''