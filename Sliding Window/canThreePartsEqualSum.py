# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum
#
# ~~~Version 1~~~
# Sliding window technique
# In this case the sliding window represents the middle of the three slices (back and front elements included)
# Move the front of the window forward until the righthand slice is half the sum of the left and middle slices
#     (i.e. the right hand slice is a candidate for one of the three equal slices)
# Then move the back of the window forward, either until the right, middle and left slices are equal
# Or until the back and forward pointers meet before the forward pointer has reached the penultimate element
#
# Time Complexity     O(n)    at most both back and front move through the array once
# Space complexity    O(1)
#
# ~~~Version 2~~~
# Connecting the dots math-wise
#     If the sum of the whole array is not divisible by 3 then then there is not valid set of slices
#     If the whole array has a sum of S then average sum of each of the slices must be S/3
# So iterate through the array and if the current slice has a sum of S/3, count it as a valid slice
# If by the end of the array you have 3 (or more in the case where a the whole array sums to zero) valid slices
# then the array can be split into 3 equal parts
#
# Time Complexity     O(n)   
# Space complexity    O(1)

# Version 1
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        
        front = 1
        left, mid = A[0], A[front]
        right = sum(A) - mid - left
        
        for back in range(1, n - 1):
            while (front < n - 2) and ((left + mid != 2*right) or (back == front and left != mid)):
                front += 1
                mid += A[front]
                right -= A[front]
            if (left == mid == right):
                return True
            left += A[back] 
            mid -= A[back]
            
        return False
        
# Version 2
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        total = sum(A)

        if total % 3 != 0:
            return False

        avSum, sliceSum, numWithAv = total / 3, 0, 0

        for num in A:
            sliceSum += num
            if sliceSum == avSum:
                numWithAv += 1
                sliceSum = 0

        return numWithAv >= 3