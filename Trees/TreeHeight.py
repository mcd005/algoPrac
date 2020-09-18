'''
Problem Description:https://app.codility.com/programmers/lessons/99-future_training/tree_height/

This is basically a level order traversal
However list comprehension is used so that each layer can be distinguished
Each layer represents an increase in the height by one
Continue until you reach an empty layer, and thus the bottom of the tree

Time complexity         O(n)
Space complexity        O(n)
'''

from extratypes import Tree  # library with types used in the task

def solution(T):
    height = -1
    
    #To handle an input of None
    if not T:
        return height
        
    q = [T]
    while q:
        height += 1
        cur = [child for node in q for child in (node.l, node.r) if child]
        q = cur
        
    return height