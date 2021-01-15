# https://leetcode.com/problems/trapping-rain-water/

# Time complexity         O(n)
# Space complexity        O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # Smallest region where rain can be trapped is 101
        if n < 3:
            return 0
        
        # Rain can only be trapped between two consecutive local maxmima
        # where the the height of one is equal to or greater than the height of the other

        # With the sliding window approach we use below
        # unless every other local maxima is the same height as the global maximum
        # then by defintion all other local maxima will not be equal to or greater height 

        # To resolve this, we split the input array in half at the global maximum
        # Sweep left to right in the left half
        # And right to left in the right half
        maxPeak = max(height)
        idxOfMax = height.index(maxPeak)
        
        l2r = 0
        front = 0
        lowerEdge = 0
        for back in range(idxOfMax + 1):
            # Front pointer advances looking for a peak
            while front < idxOfMax and (height[front] < height[back] or front == back):
                front += 1
                # When it finds one, it stores the height of the rear of the two consecutive peaks in lowerEdge
                lowerEdge = height[back]
            if height[back] < lowerEdge:
                # As the back pointer advances, it tallies the depth of rain trapped between the two regions
                l2r += lowerEdge - height[back]
                   
        r2l = 0
        back = n - 1
        for front in range(n - 1, idxOfMax - 1,  - 1):
            while back > idxOfMax and (height[front] > height[back] or front == back):
                back -= 1
                lowerEdge = height[front]
            if height[front] < lowerEdge:
                r2l += lowerEdge - height[front]
                
        return l2r + r2l