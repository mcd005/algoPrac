# https://leetcode.com/problems/gas-station/
# Time complexity       O(n)
# Space complexity      O(1)
# Version 2 - If sum of all the net costs is greater than zero there must be a solution
# If our tank runs out (i.e. goes negative) at a station we know that we can't start at any station before it
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, tank, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start

# Version 1 - Two pointer
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_costs = [g - c for g, c in zip(gas, cost)]
        n = len(gas)
        trip_cost = 0
        end = 0
        for start in range(n):
            if net_costs[start] >= 0:
                if end < start:
                    end = start
                    trip_cost = 0
                while end < n * 2 and end - start < n and trip_cost + net_costs[end % n] >= 0:
                    trip_cost += net_costs[end % n]
                    end += 1
                if end - start == n:
                    return start
            trip_cost -= net_costs[start]
        return -1

'''
Brute force
We start from station 0 and try to make it all the way around
If we reach a point where we do not have enough gas to travel to the next station we start again from station 1
And so on until we find a valid station or exhaust them all
Time complexity     O(n^2)

Is there any computation we can reuse?
    Yes let's do two pointers
    With two pointers we will cover every possible start location
    And it's ok if we're not covering every start location end location pair
    Because if a pair i, j is invalid, then we don't really care about checking i, j - 1

Algo
We have two pointers start and end, both initialised to zero
We initialise tank to zero
We compute net gas for trip by doing current_net 
We compute gas for a given 


### Key Lessons ###
Run through the brute force to get an idea of wasted work and better abstractions
    Penny dropped when I realised you needed a starting fuel that was equal to sum of the net costs from that point on
Rather than thinking about a specific solution that could work get an idea of the heart of the problem
'''