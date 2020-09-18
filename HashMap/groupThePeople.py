'''
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
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
        return result