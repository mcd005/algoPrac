# https://leetcode.com/problems/non-decreasing-array
# Version 4 - Prefentially modify nums[i - 1] if we have and invalid pair. This is the textbook one imho
# Time complexity           O(n)
# Space complexity          O(1)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if modified:
                    return False
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                modified = 1
                
        return True

# Version 3 - From LC. Rectify both and compare against sorted array
# Time complexity           O(n + nlogn)
# Space complexity          O(n)
class Solution(object):
    def checkPossibility(self, nums):
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
            
# Version 2 - Check if you've modified or the current triple would take require 2 modifications
# Time complexity           O(n)
# Space complexity          O(1)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if err or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                err = 1
        return True

# Version 1 - Check all triples
# Time complexity           O(n)
# Space complexity          O(1)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True

        self.nums = nums
        self.idx_modified = -1
        for i in range(1, n - 1):
            left, mid, right = i - 1, i, i + 1
            if self.nums[left] <= self.nums[mid] and self.nums[right] < self.nums[mid]:
                if self.nums[right] < self.nums[left]:
                    if not self.is_valid_to_modify(right):
                        return False
                    self.nums[right] = self.nums[mid]
                    self.idx_modified = right
                elif not self.is_valid_to_modify(mid):
                    return False
                self.nums[mid] = self.nums[left]
                self.idx_modified = mid
            elif self.nums[left] > self.nums[mid]:
                if self.nums[right] < self.nums[mid]:
                    return False
                elif not self.is_valid_to_modify(left):
                    return False
                self.nums[left] = self.nums[mid]
                self.idx_modified = left
                    
        return True

    def is_valid_to_modify(self, idx_to_modify):
        return self.idx_modified == -1 or self.idx_modified == idx_to_modify

'''
Take care not to forget that non-decreasing means all elements can be equal

Is there anything wrong with iterating through and counting the number of idxs where this value is not true
And then at then end returning false if that value is greater than 1?
    Yes if we have an array that looks like [1, 2, 3, 4, 1, 1, 1, 1]
    The count of num_decreasing will only be one
    So what if we rectify the first 1 and make it a 4?

If we greedily rectify the first decreasing element will that cause us problems?
    Yes for [4, 2, 3] we would change it to [4, 4, 3] and return False when it should be True
    Maybe we need to change the order we check. Instead of each element looking ahead, each neighnour looks behind
        That wouldn't solve things though
    Maybe if index is zero then we change current element [4, 2, 3] goes to [2, 2, 3]
        Then only on subsequent to would we want to modify leading element not preceding

Above does not work for [-1,4,2,3]
    We shouldn't just be considering the two points. Instead we should be considering at least three
    What are the configurations, either the leading, middle or end values are illegal
    
### Key lessons ###
Sometimes you can just enumerate all the logical outcomes
Try and leverage the properties of the sorted array
'''
