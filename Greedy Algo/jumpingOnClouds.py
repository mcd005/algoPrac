# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

# Time complexity       O(n)
# Space complexity      O(1)

# Version 1 - Greedy array slicing
def jumpingOnClouds(c):
    jumps = 0
    while len(c) > 1:
        if len(c) == 2: # If the end is in range jump for it
            jumps += 1
            break
        else:
            if c[2] == 0: # Otherwise try to jump as far as you can
                c = c[2:]
            elif c[1] == 0: # Or jump 1 otherwise
                c = c[1:]
            jumps += 1
    return jumps

# In order to avoid computational and memory overhead
# would likely be better not to slice arrays
