class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left + 2 <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] > arr[mid]:
                right = mid
            elif arr[mid] < arr[mid + 1]:
                left = mid

'''
[0,1,5,7,3]
     l m r
'''