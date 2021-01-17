# We intitialise a dictionary, whose values will be lists that are priority queues 
# Then we iterate through items and push student scores to these list
# heapq makes it so that the heap invariant is satisfied: the first item in the list will be the smallest
# If the list exceed 5 elements, remove the smallest
# As such we will always have the top 5 scores
# 
# Once the dictionary has been constructed, use list comprehension to average the scores and build the ouptut
#
# Time complexity       O(n logn) for n insertions into a heap
# Space complexity      O(n)

# Version 1 - as explained above
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict = collections.defaultdict(list)
        
        for ID, score in items:
            heapq.heappush(dict[ID], score)
        
            if len(dict[ID]) > 5:
                heapq.heappop(dict[ID])
                
        output = [[student, sum(scores) // 5] for student, scores in sorted(dict.items())]
        
        return output

# Version 2 - only grab the 5 biggest scores at the end using heapq.nlargest()
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict = collections.defaultdict(lambda:[])
        
        for ID, score in items:
            heapq.heappush(dict[ID], score)
            
        output = []
        for student, scores in dict.items():
            output.append([student, sum(heapq.nlargest(5, scores)) // 5])
        
        return sorted(output, key = lambda x : x[0])

# Version 3 - the rationale is similar to a heapq: 
# bisect.insort maintains a list in a sorted order
# under the hood this works much like a binary search algorithm 
# so finding the insertion points takes O(logn)
# however because it it's maintaining a sorted list insertion is O(n). So overall:
#
# Time complexity         O(n^2)
# Space complexity        O(n)
#
# Interestingly however, this algorithm is the fastest of the three in ms 
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict = collections.defaultdict(lambda:[])
        
        for ID, score in items:
	        bisect.insort(dict[ID], score)
        
        return [[student, sum(dict[student][-5:]) // 5] for student in sorted(dict)]