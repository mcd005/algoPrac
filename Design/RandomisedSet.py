# https://leetcode.com/problems/insert-delete-getrandom-o1
# Version 2 - Use a map that points to the indices of an array
# Time complexity           O(1)
# Space complexity          O(n)
from random import random
class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.arr = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = self.n
        self.arr.append(val)
        self.n += 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # We swap the item at the back of the array with the item to be removed
        # This allows us to pop off the back of the array in O(1)
        i = self.map[val]
        self.map[self.arr[-1]] = i
        self.map.pop(val)
        self.arr[i] = self.arr[-1]
        self.arr.pop()
        self.n -= 1

        return True

    def getRandom(self) -> int:
        return self.arr[int(random() * self.n)]

# Version 1 - Binary tree
# We will store our numbers in a kind of trie, where each word is the 32-bit binary representation of the given numbers
# The trie will have a height of 32 throughout, one for each bit of the numbers given 
# And a final bit, the sign bit, where 0 shall be positive and 1 shall be negative. Won't be quite twos compelment though
# Each node will have a "zero" or one child (or both)
# And will have a count of how many leaves it has attached to either child, so the future rolls to get random numbers can be weighted accordingly
# To insert, we just traverse the tree and lay down new nodes as necessary
# To remove, we first check if the given number is present, and if it is we traverse to that leaf updating the counts accordingly
#     We also want to delete the branch that originates from the closest divergence to the leaf
#     We know what that divergence is after we have traversed to the leaf. We delete that branch recursively
# To getRandom, we just pick branches using a weighted coin toss, summing bits as we go
# This solution is quite slow and large though

# Time complexity       O(1)
# Space complexity      O(n)
# Where n is the number of insert calls
import random
class Node:
    def __init__(self, zero=None, one=None, num_left=0, num_right=0) -> None:
        self.zero = zero
        self.one = one
        self.num_left = num_left
        self.num_right = num_right

class RandomizedSet:

    def __init__(self):
        self.root = Node()
        self._set = set()

    def insert(self, val: int) -> bool:
        was_present = val in self._set
        self._set.add(val)

        sign = 1 if val >= 0 else -1
        val = abs(val)
        node = self.root
        for i in range(32):
            if (i <= 30 and val % 2 == 0) or (i == 31 and sign == 1):
                node.num_left += 1
                if not node.zero:
                    node.zero = Node()
                node = node.zero
            else:
                node.num_right += 1
                if not node.one:
                    node.one = Node()
                node = node.one
            val >>= 1
        return not was_present

    def remove(self, val: int) -> bool:
        was_present = val in self._set

        if was_present:
            self._set.remove(val)
            sign = 1 if val >= 0 else -1
            val = abs(val)
            node = self.root
            closest_divergence = (node, val % 2)
            for i in range(32):
                if node.zero and node.one:
                    closest_divergence = (node, val % 2)
                if (i <= 30 and val % 2 == 0) or (i == 31 and sign == 1):
                    node.num_left -= 1
                    node = node.zero
                else:
                    node.num_right -= 1
                    node = node.one
                val >>= 1
            fork_node, direction = closest_divergence

            if direction == 0:
                self.delete_branch(fork_node.zero)
                fork_node.zero = None
            else:
                self.delete_branch(fork_node.one)
                fork_node.one = None

            return True

        return False
        
    def delete_branch(self, node):
        if node:
            self.delete_branch(node.zero)
            self.delete_branch(node.one)
            node.zero, node.one = None, None
            del node

    def getRandom(self) -> int:
        node = self.root
        val, bit_val = 0, 1
        for i in range(32):
            bit = self.weighted_coin_toss(node.num_left, node.num_right)
            node = node.zero if not bit else node.one
            if i < 31:
                val += bit_val * bit
                bit_val <<= 1
            else:
                val *= (bit * -2) + 1
        return val
    
    def weighted_coin_toss(self, num_left, num_right):
        return 0 if random.random() < (num_left / (num_left + num_right)) else 1

### Tree Notes ####
# Probably better instead to store in a binary tree rather than hex
# There may be a way to do with variable levels but I that will require extra logic to decide 
#       e.g If we encounter bit sequences that are prefixes to other numbers
#           How do we decide if we want to stop or continue?

#### Draft Ideas #### 
# Have a map for the insert and remove
# And the values of the map need to point to a data structure that you can:
#       index randomly
#       insert into and remove from in constant time
# We can index an array randomly but removal takes O(n)

# Cyclic Linked list
# Map with {number: pointer to list node}
# Insert
#   Insert the number in the list wherever the pointer is 
#   Thing is you have to advance the pointer in linear time
# Remove
#   Look in map for pointer
#   Call remove on pointer. Call remove on map
# Get random
#   Increment the pointer a random number of times
#   Return that value

# What about a graph
# What if we used some kind of array of hex
# Or could use a tree

##### Key Understandings and Lessons #####
# You need to keep solving the subproblems presented until you absolutely hit a wall
# e.g. Q:Need O(1) lookup? A:Use a map
#      Q:But I can't index a map randomly! A:Point to an array
#      Q:But I can't do O(1) insertion/removal! A:You can at the back of the array
#      So find a way to move to and from the back etc
# Use examples rather than trying to reason out the algo
# Don't just use heuristics for your maths, sit down and check your assumptions are valid
# Was more useful to store info in bits rather than a list for sign. Try and come up with solutions that are general
# If you give [] as default argument in Python, it's the same across all intances
# Can't just delete in python, need to sever the connection to that node with "None"
# K constant ops is still O(1)