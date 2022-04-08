class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


'''
Naive
    Iterate over each of the two lists, merging them
    When there are (m + n) / 2 elements left return the element we are on
    However this would take linear time

We don't need to take linear time to find the insertion point in each list though
Because the lists are sorted we can bisect

We can iterate over the elements of the shorter list and ask where in the longer list they would be inserted
    Lets say the size of the longer list is n and the shorter is m
We don't actually need to insert the elements from the shorter list though we can just pretend we have
If we pretend to insert an element to the left of index n / 2 then the midpoint is shifted to the left in the longer array
If we pretend to insert the element to the right of n / 2 then the midpoint is shifted to the right in the longer array
Either way after we've pretended to insert all of the shorter lists elements, we have a new midpoint, which we return
However this gives us a time complexity of O(mlogn)

So how do we compress the number of pretend insertions we need to make?
Again rather than iterating lineraly over the shorter list we could ask:
    How many of these points are we inserting before the midpoint?
    That requires a binary search we we just look for where the current long list midpoint would sit in the shorter list

But as we insert elements the midpoint changes
    For each element inserted, the midpoint moves by half an index
So I suppose we need to ask two questions:
    If we tried to insert k elements before the midpoint
    would the shift in midpoint mean it was inappropirate to move insert all k?
            It's appropriate to continue with the insertion if the biggest of the k elements to be inserted is less
            than the value at nums1[old_midpoint - k / 2]
            We would need to decrement k by one until there was no overlap
    Is the insertion point of the k elements to be inserted within  k / 2 of the midpoint?

1, 2, 6, 8, 10, 13 -> Median = 7
1, 2, 6, 8, 10, 13, 14 -> Median = 8
0, 1, 2, 6, 8, 10, 13, 14 -> Median = 6


Take the longer array
Look at it's median
Binary search in the shorter array for where that median would sit
Divide the shorter array into two parts, left and right about the index at which the median from longer would sit
Now we are going to pretend to insert the two parts into the longer array


Look at the median of the first array and the median of the second
This will tell us where we need to insert 
'''