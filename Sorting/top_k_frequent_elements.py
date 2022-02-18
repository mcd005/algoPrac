# Version 1 - Counter most_common (which creates a heap)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [k for k, v in counts.most_common(k)]

# Version 2 - Bucket sort (concise)
# The most frequent element can only come up at most n times
class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()
        for num, freq in Count: bucket[freq].append(num)
        flat_list = list(chain(*bucket)) # We turn the list of iterables into one continuous iterable
        return flat_list[::-1][:k]