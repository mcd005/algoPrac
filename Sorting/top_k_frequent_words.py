# https://leetcode.com/problems/top-k-frequent-words/
# Version 1 - Fully sort and take first k 
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = list(Counter(words).items()) # Looks like [(word: count of word), (other_word, count of other word)]
        word_count.sort(key=lambda x: (-x[1], x[0])) 
        print(word_count)
        return [word_count[i][0] for i in range(k)]

# Version 2 - K sized heap, currently not working
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = [(count, word[::-1]) for word, count in Counter(words).items()]
        word_heap = word_count[:k]
        heapq.heapify(word_heap)

        m = len(word_count)
        for i in range(k + 1, m):
            heapq.heappushpop(word_heap, word_count[i])

        word_heap.sort(reversed=True)
        return [word[::-1] for _, word in word_heap]

# Version 3 - Partial sort, currently not working
from collections import Counter
from random import randint
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        self.word_counter = [(count, word) for word, count in Counter(words).items()]
        self.m = len(self.word_counter)
        self.partial_sort(0, self.m - 1, k)
        return [self.word_counter[i][1] for i in range(0, k)]

    def partial_sort(self, i, j, k):
        if i < j:
            pivot_idx = randint(i, j)
            pivot_idx = self.partition(i, j, pivot_idx)
            self.partial_sort(i, pivot_idx - 1, k)
            if pivot_idx < k - 1:
                self.partial_sort(pivot_idx + 1, j, k)

    def partition(self, i, j, pivot_idx):
        pivot = self.word_counter[pivot_idx]
        start, end = i, j
        self.word_counter[pivot_idx], self.word_counter[start] = self.word_counter[start], self.word_counter[pivot_idx]
        i += 1
        while i < j:
            while i < end and self.is_left_of_pivot(self.word_counter[i], pivot):
                i += 1
            while j > start and not self.is_left_of_pivot(self.word_counter[j], pivot):
                j -= 1
            if i < j:
                self.word_counter[i], self.word_counter[j] = self.word_counter[j], self.word_counter[i]
        self.word_counter[start], self.word_counter[j] = self.word_counter[j], self.word_counter[start]
        return j

    def is_left_of_pivot(self, word_count, pivot):
        return word_count[0] > pivot[0] or (word_count[0] == pivot[0] and word_count[1] < pivot[1])


# Construct a counter in O(n) and then we either

# Sort it fully in nlogn
# Take the first k
# Time complexity           O(2n + nlogn + k)
# Space complexity          O(n)

# Heapify our counter and then pop k times
# Time complexity           O(n + n + klogn)
# Space complexity          O(n)

# Create a min heap of size k
# Iterate over our counter and add each element to the heap
# Remove the smallest element that rises to the top of the heap
# Time complexity           O(n + nlogk + klogk)
# Space complexity          O(n)

# Or in place partial sort in in O(nlogk)
#    To implement partial sort I think you pivot srot but only recur on the top half of the array
# Time complexity           O(n + nlogk + k)
# Space complexity          O(1)

### Key Lessons ###
# Don't bite off more than you can chew. Implement the basic stuff first, then move onto more advanced
# If the problem suits C++ do it there
# Moving pivot to the end means you don't have to write logic for comparing against self
# You can call nsmallest on something that's not a heap