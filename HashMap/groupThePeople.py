'''
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

We first construct a dict whose keys are the distinct group sizes 
and whose vals are list of indices of people who belong a in group of that size
Then we break those lists of indices up into smaller list of a size equal to their key

Time complexity         O(n)
Space complexity        O(n)
'''

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        result = []
        for i in range(len(groupSizes)):
            if groupSizes[i] in dict:
                dict[groupSizes[i]].append(i)
            else:
                dict[groupSizes[i]] = [i]
                
        for k,v in dict.items():
            for j in range(0,len(v),k):
                result.append(v[j:(j+k)])
                # Before we have {3 : [0, 2, 5, 7, 12, 13]} 
                # We break this into two group of size 3: [0, 2, 5], [7, 12, 13]
                # And we store them both in the result
        return result