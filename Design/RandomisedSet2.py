# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Version 1 - Dict for O(1) retrieval, list of random indexing
# Time complexity       O(1)
# Space complexity      O(n)
from random import randint
from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.q_stack = []
        self.idx_map = defaultdict(lambda: set())

    def insert(self, val: int) -> bool:
        is_present = len(self.idx_map.get(val, [])) > 0
        self.q_stack.append(val)
        self.idx_map[val].add(len(self.q_stack) - 1)
        return not is_present

    def remove(self, val: int) -> bool:
        is_present = len(self.idx_map.get(val, [])) > 0
        if is_present:
            idx_of_val = self.idx_map[val].pop()
            idx_of_back = len(self.q_stack) - 1
            val_at_back = self.q_stack[idx_of_back]
            # could have logic here to only swap if we are only removing val at back
            self.q_stack[idx_of_val], self.q_stack[idx_of_back] = self.q_stack[idx_of_back], self.q_stack[idx_of_val]
            self.q_stack.pop()
            self.idx_map[val_at_back].add(idx_of_val)
            self.idx_map[val_at_back].remove(idx_of_back)
        return is_present
        
    def getRandom(self) -> int:
        return self.q_stack[randint(0, len(self.q_stack) - 1)]

'''
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom", "remove", "remove"]
[[], [1], [1], [2], [], [1], [], [1], [2]]
[null, true, false, 1, true, true, 2, false, true]

q_stack = [2]
idx_of val = 1
idx_back = 1

idx_map = {1: {}, 2: {0}}


We have a quasi-stack list to hold each val
We have a dict that looks like { val: set(idxs of array where that val is)}

When we insert
    we first check if that val is already present
    We push to the list
    And we mark it the set at val

When we remove
    Look at the set at val and pop one of those idxs
    We look at the val at the back of the list (let's call this old_back)
    We swap the positions of val and old_back
    We update the set at old back to reflect it's no longer at the back of the list
    We pop val off the back of the list

get random
    return the value at a random idx in the list
'''