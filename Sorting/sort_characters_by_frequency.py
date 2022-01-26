# Version 2 - Like version 1 but regenerate the string
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        desc = sorted(counts, key=lambda c: counts[c], reverse=True)
        return "".join(c * counts[c] for c in desc)
        


# Version 1 - Hash and then sort string
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join(sorted(s, key=lambda char: (counter[char], char), reverse=True))

'''
Create a coutner of each element
Call sort on the string and use the entry from the counter as the key
Time complexity         O(n + nlogn)
Space                   O(1)            for a constant size alphabet

### Key Lessons ###
sorted() returns a list
Better to build a string then sort one
'''