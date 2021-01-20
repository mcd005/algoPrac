# Version 1 - standard hashmap
# Time complexity       O(n)
# Space complexity      O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.defaultdict(lambda:[])
        
        n = len(s)
        for i in range(n):
            cnt[s[i]].append(i)
        
        minIndex = n
        for idxList in cnt.values():
            if len(idxList) == 1:
                minIndex = min(idxList[0], minIndex)
        
        if minIndex < n:
            return minIndex
        else:
            return -1