# Create an array dp so we can remember how much candy we have given to each student
# We iterate forward through the students
# making sure if a student sat behind the current one has a rating greater than the current student
# he gets 1 candy more than the current student

# However this will mean that some students with a medium rating sat behing a student with a high rating
# will only get 1 candy (e.g. ... 8 9 2 1 -> ... 3 4 1 1)

# So we iterate backwartd through the students
# and make sure every student who is sat in front of the current student
# and has a rating greater than the current student
# gets 1 more candy than the current student

# Time complexity     O(n)
# Space complexity    O(n)

# Unfortunately this solution is not ideal.
# Although it runs in linear time we have to iterate through arr twice
# And also we have to allocate a linear amount of memory
#
# There is a way this can be done with one pass, using constant memory
# It requires treating slices of the student ratings as sequences of ascending or descending sequences
# And the total candy given in that sequence is equal to the sum of the arithmetic progression for the sequence
# However I had trouble implementing this based on intersecting ascending and descending sequences
# e.g. with the algorith below 1 6 10 8 7 3 2 -> 1 2 3 4 3 2 1
#                             when it should be  1 2 5 4 3 2 1

def candies(n, arr):
    if n == 0:
        return 1

    dp = [1 for x in range(n)]

    for i in range(n - 1):
        if (arr[i + 1] > arr[i]):
            dp[i + 1] = dp[i] + 1

    for i in range(n - 1, 0, -1):
        if (arr[i - 1] > arr[i]) and (dp[i - 1] <= dp[i]):
            dp[i - 1] = dp[i] + 1

    return sum(dp)

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         if n == 1:
#             return 1
#
#         # Helper function to identify if a sequence is ascendeing, descending or equal
#         def whichType(idx, arr):
#             if arr[idx] > arr[idx - 1]:
#                 return 1  # ascending
#             elif arr[idx] < arr[idx - 1]:
#                 return 2  # descending
#             else:
#                 return 3  # equal
#
#         def bank(typ, rn):
#             if typ == 3:
#                 return run
#             else:
#                 return int((run * (run + 1)) / 2)
#
#         candies = 0
#         preType = 0  # New (i.e. the start of ratings or when candies have just been banked)
#         run = 1
#
#         for i in range(1, n):
#             runType = whichType(i, ratings)
#
#             if (preType == 0) or (preType == runType):
#                 run += 1
#                 preType = runType
#             else:
#                 candies += bank(preType, run)
#
#                 if ((runType == 1) or (preType == 3 and runType == 2)):
#                     candies -= 1
#                     run = 2
#                 else:
#                     run = 1
#
#                 preType = 0
#
#         candies += bank(preType, run)
#
#         return candies