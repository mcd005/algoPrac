class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass

    def dfs(self, ):
        pass

'''
[0]
[1]
[2, 4]
We look at 2 and enqueue 1, 3, and 4
[4, 1, 3, 4]
We are looking at 4
Then we enqueue 1, 2 and 3
[1, 3, 4, 2, 1, 2]
We look at 1
We've been here before
We came here from 2
We've taken a total of 3 hops from 0
We took 1 hop to get here before
How about you can backtrack but only if you've come back with a new element
[3, 4, 2, 1, 2, 0, 2, 4]


[0]
[(1, 0), (2, 0), (3, 0)]
[(2, 0), (3, 0), (1, 01)]
[(3, 0), (1, 01), (1, 02)]
[(1, 01), (1, 02), (1, 03)]


How do we deal with cycles whilst still allowing backtracking
If we reach a node with only one edge we must backtrack,
unless we decide we want to have started from there instead
How do you work out when you can make a saving on hops?

Brute force
Enumerate all possible paths from a single source node to a single destination node
Then stitch them together in the order which requires the least hops

Start from each node
Calculate cost to get to each of the other nodes depth first style

You start at a node and you ask:
If I were to DFS my neighbours, how many nodes would I encounter?
If that number is less than n, you know you are going to have to double back from that branch

How would we go about DFS?
Call DFS on each of the neighbours
Pass a number that gives number of hops taken
After DFSing that branch if we haven't seen all the nodes then we know we either have to turn around
Or decide that we should have started on that branch

How would we go about BFS
How do we avoid problems with cycles?
We want to mark some nodes as visited
But for some graphs we are going to have to revisit some nodes that we have already visited

We ask: What is the quickest way to 4 from any given node?
It must be by one of 4s neighbours. 
So we look at 4's neigbours and ask what's the quickest way to each of you?
It must be by one of their neighbours, (except 4)

Do we want to do some kind of DP
dp[i][j] gives us the shortest path that connects node i to j

What is the min cost to visit i starting from j?
  0 1 2 3 4
----------- 
0|0 1 - - -  
1|1 0 1 - 1
2|- 1 0 1 1
3|- - 1 0 -
4|- 1 1 - 0

We ask: what is the cost to get to 4 having vistited all other nodes
The answer to that is 1 + the min cost to get to 4s neighbours

What is the min cost to visit all nodes?
The answer to that is the min cost required to vist all of the nodes but i=4, + the cost to visit i=4
What is the min cost to vist all the nodes but i=4?
The min cost to visit all nodes but i=3 and 4 + the cost to visit 3
What is the min cost to visit all nodes but i=2
The min cost to visit all nodes but i=2 + the cost to visit 2
What is the min cost to visit all nodes but i=1
The min cost to visit all nodes but i=1 + the cost to visit 1
...
What is the min cost to visit all nodes but i=1 
wh

Shortest path visiting all nodes
1 + shortest path visiting all nodes but n from n's neighbour
1 + shortest path vistiing all nodes but n, n's neighbour f

We start by limiting all nodes to just node 0
Then we say all nodes is nodes 0 and 1
'''

