
# Version 1 - Sort based on max delta costB - costA
# Send all in first half of the array (i.e. bigger delta) to A, and all in second half to B
# In a naive implementation we would greedily ask: which person is cheapest to send to city A?
# And then we would send that person, and then send the second cheapest person and so on
# What we need to do instead is consider it a trade-off
# If we have a pair that is (10, 100) then we make a 90 unit saving by sending that person to A
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(reverse=True, key=lambda cost: cost[1] - cost[0])

        min_cost = 0
        two_n = len(costs)
        for i in range(two_n):
            if i < (two_n / 2):
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]
        
        return min_cost

    
# Version 2 - Code golf of V1
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[1] - cost[0])
        n = len(costs) / 2
        return sum( (cost[idx < n] for idx, cost in enumerate(costs)) )