# https://leetcode.com/problems/contains-duplicate/
# Version 1 - Set
# Time complexity       O(n)
# Space complexity      O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

'''
Basic solution would be to keep track of seen numbers in a set
So as we iterate through we just ask if that number is already in the set
O(n) time and space

Is there a constant space solution? Other than naive O(n^2) search
Possibly with bitwise ops
Was going to suggest XOR but you can only check that at then end and if there is an odd 
number of elements looks the same as if there is a single element

Could sort and then check if any element was the same as it's neighbour
O(nlogn) time but O(1) space
'''
