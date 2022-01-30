# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 0 3 12 11 16 14 5
        #     w
        #     r
        n = self.get_linked_list_len(l1) # 4
        m = self.get_linked_list_len(l2) # 3

        if n > m:
            dummy = ListNode(val=0, next=l1)
            long_ptr = self.advance_ptr_x_times(l1, n - m)
            short_ptr = l2
        else:
            dummy = ListNode(val=0, next=l2)
            long_ptr = self.advance_ptr_x_times(l2, m - n)
            short_ptr = l1

        while long_ptr and short_ptr:
            long_ptr.val += short_ptr.val
            long_ptr, short_ptr = long_ptr.next, short_ptr.next

        write_ptr = read_ptr = dummy
        while write_ptr:
            if write_ptr == read_ptr:
                write_ptr.val %= 10
            if read_ptr and ((read_ptr == write_ptr) or read_ptr.val == 9):
                read_ptr = read_ptr.next
            elif write_ptr != read_ptr:
                if read_ptr and read_ptr.val > 9:
                    write_ptr.val = (write_ptr.val + 1) % 10
                write_ptr = write_ptr.next

        if dummy.val == 0:
            output = dummy.next
            dummy.next = None
            del dummy
            return output
        return dummy


    def get_linked_list_len(self, node):
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def advance_ptr_x_times(self, ptr, x):
        while ptr and x:
            x -= 1
            ptr = ptr.next
        return ptr


'''
Most straightfoward solution would be to reverse both lists then add them as you would on paper (starting from LSD)
O(n) time and space if recursive reversal. O(1) space if iterative reversal

We could put both nodes in stacks and then pop off the stack and add and carry as we go
O(n) time and space

Are there O(1) space solutions that doesn't involve reversing?
    Count the lenghts of both lists
    If one of the lists is shorter, advance the pointer on the longer list so it's in line with the shorter on 
    What to do if you have carries?
        Keep an array to mark where the carries are applied?
            Well then solution becomes O(n) space
        Mark the val in way to indicate carries
        How do we retrieve that info and apply it to upstream digits with O(1) space?
        When we do a CLA we can mark which digits propagate or generate carries
            Will propagate if 9 or more
                Can a carry ever be 2?
                    No max a single digit can be is 9
                    So max two can be is 18
                    So only 1 will ever carry
            Will generate if 10 or more
        Then at the end we can inspect all the the bits and propagate carries as necesarry
        We can do this with two pointers

Algo
    Count the lenghts of both lists
    If one of the lists is shorter, advance the pointer on the longer list so it's in line with the shorter on 
    We also we to prepend a dummy head to the longer list so that we have somewhere to put carries if they propagate that far
    Add the values from the shorter list to corresponding nodes on the longer list
    This will tell us which nodes will generate and which will propagate
    Then we iterate through the list again using two pointers
        Slow will be a write head
        Fast will be a read head
        Fast will iterate through any nodes that propagate
        Then write to moves to meet it, incrementing each and taking their mod 10 if the digit at the end of the run generates

Need to try with a zero given for one of the inputs

### Key Lessons ###
Explicity write down space and time complexities so you can better compare algos
Good job using the mem given to you to keep it O(1)
Good job boiling down the logic for propagating and generating carries
'''