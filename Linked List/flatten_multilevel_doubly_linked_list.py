# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
# Version 1 - Keep a stack detached lists (i.e cur.next when we encounter a child)
# and attach them onto the tail of the child level
# Time complexity       O(n)
# Space complexity      O(n)
# for n nodes
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        detached_lists = []
        while node:
            if node.child:
                if node.next:
                    detached_lists.append(node.next)
                node.next, node.child.prev, node.child = node.child, node, None
            if not node.next:
                if detached_lists:
                    after = detached_lists.pop()
                    node.next = after
                    after.prev = node
                else:
                    break
            node = node.next
        
        return head

# Version 2 - From LC. Recursively flatten, passing head and tail from each level
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
                
        def recurse(head):
            prev, cur = None, head
            while cur:
                if cur.child:
                    next = cur.next
                    child_head, child_tail = recurse(cur.child)
                    cur.next, child_head.prev, child_tail.next = child_head, cur, next
                    if next:
                        next.prev = child_tail
                    cur.child = None
                    prev, cur = child_tail, next
                else:
                    prev, cur = cur, cur.next
            
            return head, prev
            
        headPtr, tailPtr = recurse(head)
        return headPtr

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""