# https://leetcode.com/problems/subarray-sum-equals-k/
# Version 1 - Like a prefix sum version of two sum
# Time complexity       O(n)
# Space complexity      O(1)
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]

        num_equal_k = 0
        sum_counter = defaultdict(lambda: 0)
        for num in pre:
            if num == k:
                num_equal_k += 1
            num_equal_k += sum_counter.get(num - k, 0)
            sum_counter[num] += 1

        return num_equal_k

'''
Brute force
Iterate over each element
And check all the subarrays that start at that element
Gives an O(n^2) runtime
How do we query all the subarrays that start at a given element in O(1)
How can a prefix sum help?
    Each element in a prefix sum tells you the sum of all the elements from the start to the current point
    If the current point is equal to k then we know we can increment a count
    Otherwise we need to look for an element further on in the array that is equal to num - k
    Rather than iterating ahead and searching for it we say 
        "hey look we saw num. If you num - k in future we have another valid subarray?"

We want to able to ask: How many subarrays from a given element sum to target?
And we want to get the answer to that in O(1)

What if we start from i = n - 1 and ask that question?
Because there is only 1 subarry that starts at i that gives us 1 O(1) answer
And then we also know the value of that subarray sum
Then we move back to i = n - 2
And the answer to the above question is 
[1, 2, 3] k = 3
i = n - 1
    1 of 1 subarrys sum to k
    values of subarrays = 3
    3: 1
i = n - 2
    How many subarrays of value 1 are in i = n - 1s subarrays
        0
    5: 1
    2: 1
i = n - 3
    How many subarrays of value 2 are in i = n - 2's subarrays
        1
    5: 1 
    3: 1

#### Key lessons ###
    Try and flip the question you are asking on it's head
        Rather than saying: 
            "How do we query all the subarrays that start at a given element in O(1)?"
            instead ask
            "How do we query all the subarrays that end at a given element in O(1)?"
        It's important to ask the questions for both directions
        Seeing as we iterated from the start of the array, we only been able to gain the information to answer one of those questions
        Also inveitably the answer to "How to answer a query in O(1)?" is look in a data structure where we stored the results of prior queries
        Which will then lead you to ask, what is the best way to phrase our query so the result will be useful for future queries
    Explicitly spell out the properties of the data structures you are working with
        It was only by grokking that num in prefix sum is from the start that we got to a solution
'''
