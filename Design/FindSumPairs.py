from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_dict = Counter(nums1)
        self.nums2_arr = nums2
        self.nums2_dict = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_dict[self.nums2_arr[index]] -= 1
        self.nums2_arr[index] += val
        self.nums2_dict[self.nums2_arr[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1_dict:
            count += self.nums2_dict[tot - num] * self.nums1_dict[num]
        return count

# nums1_dict = {1: 2, 2: 3, 3: 1}  
# nums2_dict = {1: 1, 4: 4, 5: 2, 2: 0}
#          0  1  2  3  4  5
# nums2 = [1, 4, 5, 4, 5, 4]

# count(7) = 0 + (3 * 2) + (1 * 2) = 8
# add(3, 2)
# count(8) = 0 + 0 + 2 = 2

# Most naive way
# When count is called you iterate over nums1 and for each you i you iterate over nums2 looking 
# for to see if nums1[i] + nums2[j] == tot
# This would take O(n * m) for n and m being the lengths of nums1 and nums2 respectively
# If you had a dict to represent the nums in nums2 then you could solve in O(n), since
# you could iterate over nums1 and look to see the count of tot - nums1[i] in that dict
# Is there a way to compute count in O(1)?
# count(int tot) can only be made a few ways (can be made tot ways be to exact)
# What count is really returning is 
#  num(tot - 1, 1) + num(tot - 2, 2) + ... num(1, tot - 1num of )
#  We can get each num(x, y) in constant time but is there any way we can query all the possible combos
# in less than O(tot) time?