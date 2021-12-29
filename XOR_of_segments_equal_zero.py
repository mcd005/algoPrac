# Version 3 - Currently not working DP like my C++ 
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # totals[i] is the number of occurences of an index with i % k = 0
        totals = [0] * k 
        # counter[i][j] is the ocurrences of j and at index i % k 
        counter = [[0] * 1024] * k
        # nums_present_at_index[i] is the set of numbers that occur at index i % k
        nums_present_at_index = {idx: set() for idx in range(k)}

        for i in range(n):
            index = i % k
            totals[index] += 1
            counter[index][nums[i]] += 1
            nums_present_at_index[index].add(nums[i])

        dp = [[n + 1] * 1024] * k
        dp[0][0] = 0 
        current_best = 0
        for i in range(k):
            best_for_i = n + 1
            for j in range(1024):
                if i == 0:
                    dp[i][j] = totals[i] - counter[i][j]
                    # i.e. we assume we replace all the elements the greedy way for i == 0
                else:
                    for other_num in nums_present_at_index[i]:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j ^ other_num] + totals[i] - counter[i][other_num])
                    dp[i][j] = min(dp[i][j], current_best + totals[i])
                best_for_i = min(best_for_i, dp[i][j])
            current_best = best_for_i

        return dp[k - 1][0]

# Make a counter for each index
# Make a counter that is the total of each index
# We also create a dict of sets that tells us the num at each position
# We iteratre over nums to populate these

# Then make a DP that has k rows each of 1024 cols
# dp[i][j] is the gives the number of changes needed for the xor from 0 to i to equal j
# We populate it by iterating over each number an 

# Version 2 - DP where I did the
from collections import deque
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        xored_except_self = self.xor_except_self(nums[:k])
        change_counts = [int(nums[i] != xored_except_self[i]) for i in range(k)]
        # previous_segment_combos[i] = [queue containing previous segment, ]
        previous_segment_combos = [[deque(), 0] for i in range(k)]

        for i in range(k):
            for j in range(1, k):
                num = nums[j] if i != j else xored_except_self[j]
                previous_segment_combos[i][0].append(num)
                previous_segment_combos[i][1] ^= num

        for num in nums[k:]:
            for i in range(k):
                # When we include num in the segment does it make the XOR equal to zero?
                number_required_for_zero = previous_segment_combos[i][1]
                if num != number_required_for_zero:
                    change_counts[i] += 1
                previous_segment_combos[i][0].append(number_required_for_zero)
                previous_segment_combos[i][1] ^= number_required_for_zero 
                dequeued = previous_segment_combos[i][0].popleft()
                previous_segment_combos[i][1] ^= dequeued
            print(previous_segment_combos)

        return min(change_counts)

    def xor_except_self(self, segment):
        k = len(segment)
        values_needed = [0] * k
        left, right = 0, 0
        for l in range(k):
            values_needed[l] = left
            left ^= segment[l]
        for r in range(k - 1, -1, -1):
            values_needed[r] ^= right
            right ^= segment[r]

        return values_needed

# Base case: 1 2 4 1
# 7 2 4 1
# 1 4 4 1
# 1 2 2 1
# 1 2 4 7

# What is the problem we are trying to solve?
#   Min number elements to change in entire array
# What is the subproblem we are trying to solve?
#   Min number to change in each segment
# What is the base case?
#   Min number to change in the first segment only
# Base case is how many do you change if there is only the first segment?
# First case is how many do you change if there are the first and second element?
# How about you change the first segment in the k ways it can be changed
# First segment [3, 4, 5] 
# [1, 4, 5] = 1 change
# [3, 6, 5] = 1 change
# [3, 4, 7] = 1 change
# Then you look at the next element: 2 
# [4, 5, 2] would need to make 1 change + number of changes from prev = 1 + 1 = 2
# [6, 5, 2] would need to make 1 change + number of changes from prev = 1 + 1 = 2
# [4, 7, 2] would need to make 1 change + number of changes from prev = 1 + 1 = 2
# Then you look at the next element: 1
# [5, 1, 1] would need to make 1 change + number of changes from prev = 1 + 2 = 3
# [5, 3, 1] would need to make 1 change + number of changes from prev = 1 + 2 = 3
# [7, 3, 1] would need to make 1 change + number of changes from prev = 1 + 2 = 3
# Then you look at the next element 7
# [1, 4, 7] would need to make 1 change + prev = 1 + 3 = 4
# [3, 6, 7] would need to make 1 change + prev = 4
# [3, 4, 7] no change + prev = 3
# Then look at next element 3
# [4, 5, 3]
# [6, 5, 3]
# 

# dp will look like [num_changes, xor_of_segment, number_to_be_dequeued]
# We have dp that contains the all of the single element mutations of the previous segment, and
# how many changes were required in all the preceding segments for that one to be legal
# Do we need to do a zero change case?


# Version 1 - Use a dict of counters to try and decide how to make all segments look like an "ideal" segement
from collections import defaultdict

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        leader_counter = {i: defaultdict(lambda: 0) for i in range(k)} # Looks like {index: {number: count of that number at all index + nk}}
        ideal_segment = []

        n = len(nums)
        for i in range(k):
            leader, max_for_idx = -1, 0
            for j in range(i, n, k):
                leader_counter[i][nums[j]] += 1
                leader_counter[i][-1] += 1
                if leader_counter[i][nums[j]] > max_for_idx:
                    max_for_idx = leader_counter[i][nums[j]]
                    leader = nums[j]
            ideal_segment.append(leader)

        values_needed = self.xor_except_self(ideal_segment)

        num_changes, max_savings = 0, -2001
        for idx, leader in enumerate(ideal_segment):
            changes_to_get_leader = leader_counter[idx][-1] - leader_counter[idx][leader]
            changes_to_get_needed = leader_counter[idx][-1] - leader_counter[idx][values_needed[idx]]
            saving = changes_to_get_leader - changes_to_get_needed
            max_savings = max(max_savings, saving)
            num_changes += changes_to_get_leader

        print(leader_counter)
        print(ideal_segment)
        print(values_needed)
        return num_changes - max_savings

    def xor_except_self(self, segment):
        # ideal_segment = [14, 27, 32]
        # values_needed = [59, 46, 21]
        # left = [0, 14, 21, 59]
        # right = [53, 59, 32, 0]
        # values_needed[i] = left[i] ^ right[i + 1]

        k = len(segment)
        values_needed = [0] * k
        left, right = 0, 0
        for l in range(k):
            values_needed[l] = left
            left ^= segment[l]
        for r in range(k - 1, -1, -1):
            values_needed[r] ^= right
            right ^= segment[r]

        return values_needed
        
# The hint notes that we need nums[i] to be equal to nums[i + k]
# This makes intuitive sense because then any given segment will have the same k ints
# If we take the segment nums[0:k] and move it along one to nums[1:k + 1], we have 
# lost nums[0] from the segment and gained nums[k]. Thus for the segment to remain zero nums[0] must equal nums[k]

# We need to make every segment identical

# Find out the leading number for each index of a certain multiple
# {
#  0: {3: 2, 2: 1},
#  1: {4: 2, 1: 1},
#  2: {7: 2, 5: 1}
# }

# We walk through and ask, how much would it cost to change to ideal_segment
# We also ask how much would it cost to change to the value_needed
# We assume we change to ideal segment
# At the end when we find 

# Currently my algo says: "If you're ideal segment is 14 and 27, then you'll need to change one of those for 21 for the XOR to equal zero"
# When in reality we would just need to change 27 to be 14

# What we need to do is create an array that is XOR_of_all_elements_except_self
# That will tell us what we need to replace our self to for the segment to equal zero
# We could then walk through that array and pick the index multiple for which the most value_needed were present already
# I'm still missing something though
# Maybe this is where I need to work out what the cost saving is
# For each element work out: how much to change to leader, and how much to change to value needed
# Then pick the index for which I get the greatest saving
# Is there another value we could be changing to to make a saving on changes
# No we must make every segment look the same and the cheapest way to do that is the way I'm doing it
# If that is the cheapest way then 
# One problem with the ideal segment is that if all ints occur once for a given index of a certain multiple
# Then we would end up just picking the first int encountered
# When actually we could just pick something that would be the value_needed
# e.g. for this example [26,19,19,28,13,14,6,25,28,19,0,15,25,11] 
# our ideal segment is [26, 19, 19]
# but could instead be [19, 0, 19]
# and we'd make a 1 change saving


# [23,27,14,0,14,3,7,10,14,23,5,5]
# {0: {23: 1, -1: 6, 14: 3, 7: 1, 5: 1}), 1: {27: 1, -1: 6, 0: 1, 3: 1, 10: 1, 23: 1, 5: 1})}
# ideal_segment = [14, 27]
# xor_except_self = [27, 14]
# costs = [(3, 6), (5, 6)] so we go [14, 14]
# which is 3 + 6 

# [26,19,19,28,13,14,6,25,28,19,0,15,25,11]
# 3

# {0: {26: 1, -1: 5, 28: 1, 6: 1, 19: 1, 25: 1, 0: 0}), 
#  1: {19: 1, -1: 5, 13: 1, 25: 1, 0: 1, 11: 1, 9: 0}), 
#  2: {19: 1, -1: 4, 14: 1, 28: 1, 15: 1, 9: 0})}
# [26, 19, 19]
# [0, 9, 9]
# 26: to leader 4, to needed 5, saving -1
# 19: to leader 4, to needed 5, saving -1
# 19: to leader 3, to needed 4, saving -1


# Brute force
# XOR all k elements in a segment
# This will leave us with the bits that we have to change
# We can either plus or minus them but only where there is not already a 1 present
# But then we need to look at the entire array and decide which combination results in the fewest changes
# We could do this greedily but one problem is that we can add extra bits but that may mean having to recompute for the other segments
# Think we need 3D dp for that dp[i][j][k]

# Taking example 2
# 3 ^ 4 ^ 5 = 011 ^ 100 ^ 101 = 010
# We need +-010 
# 4 ^ 5 ^ 2 = 100 ^ 101 ^ 010 = 011
# We need an extra 010 and 001

# Taking example 3
# 1 ^ 2 ^ 4 = 001 ^ 010 ^ 100 = 111

##### Key Understandings and Lessons #####
# Spot that nums[i] == nums[i + k]
# Found the greedy algo where you try to aim for a segment that requires least changes from 
# an "average" segment, which is determined through counters
# Identified the "tie-breaker" problem with the greedy algo but didn't even consider doing a DP to solve
# Then attempted a DP that maybe had a hint of wokring but didn't make it general enough

# Need sleep otherwise won't spot stupid assumptions made about algo
# Write down though process because you can't visualise all of that at once
# [] * 3 = [] but [""] * 3 = ["", "", ""]
# But be careful [[deque(), 0]] * 3 creates only 1 deque
