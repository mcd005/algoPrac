'''
FROM PRAMP:

Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3
'''

# Version 2 - Iterative
def root(x, n):
    if x == 0:
        return 0
    lower = 0
    upper = max(1, x)
    while upper - lower > 0.001:
        midpoint = (upper + lower) / 2.0
        if lower**n < x <= midpoint**n:
            upper = midpoint
        else:
            lower = midpoint

    return lower

# Version 1 - Recursive
def root(x, n):
  return recursive(0, max(1, x), x, n)
  
def recursive(lower, upper, x, n):
  if upper - lower <= 0.001:
    return lower
  midpoint = (upper + lower) / 2.0
  if lower**n < x <= midpoint**n:
    return recursive(lower, midpoint, x, n)
  return recursive(midpoint, upper, x, n)

### Key ideas and lessons ###
# Especially in interview settings need to question that each line serves it's purpose
#  e.g. need to do upper + lower; need to do less than or equal to
# Be clear in explaining your process
# py2 != py3