# https://leetcode.com/problems/copy-list-with-random-pointer/
# Version 2 -  Construct a list that looks like node1 --> copy_of_node1 --> node2 --> copy_of_node2 etc
# Populate random pointers on 2nd run
# Disentangle on third run
# Time complexity       O(3n)
# Time complexity       O(1)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        w_ptr = head
        while w_ptr:
            w_ptr.next = Node(x=w_ptr.val, next=w_ptr.next)
            w_ptr = w_ptr.next.next
        r_ptr = head
        while r_ptr:
            r_ptr.next.random = r_ptr.random.next if r_ptr.random else None
            r_ptr = r_ptr.next.next
        new_ptr = new_head = head.next
        old_ptr = head
        while old_ptr:
            old_ptr.next = old_ptr.next.next
            new_ptr.next = new_ptr.next.next if new_ptr.next else None
            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        return new_head

# Version 1 - Position of old nodes in a map, with new nodes in a list
# Time complexity       O(2n)
# Time complexity       O(2n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        og_node = head
        new_node = new_head = Node(x=og_node.val, random=og_node.random) 
        idx = 0
        old_positions = {}
        old_positions[og_node] = idx
        new_nodes = [new_node]
        while og_node.next:
            og_nxt = og_node.next
            idx += 1
            old_positions[og_nxt] = idx
            new_node.next = Node(x=og_nxt.val, random=og_nxt.random)
            new_nodes.append(new_node.next)
            new_node = new_node.next
            og_node = og_nxt
        ptr = new_head
        while ptr:
            if ptr.random:
                ptr.random = new_nodes[old_positions[ptr.random]]
            ptr = ptr.next
        return new_head

'''
We iterate through the og list
For each node we create a copy with the same val
We also copy next at the same time
We connect them
For our new nodes random pointer, we set it to the same as the old nodes random pointer (i.e it will still be pointing to a node in the old list) 
At the same time we have a dict for the old list that looks like { old_node_ptr: idx }
As we construct nodes in the new list we append them to a vector
We then iterate through the new list again and use the map and vector to swap the old_ptr to new ptr
'''


"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
