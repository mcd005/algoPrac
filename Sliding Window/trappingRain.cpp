/* 
The amount of rain trapped above each index is equal to:
    min(max height of a peak to left of index, max height of a peak to right of index) - height at index
We could use a brute force approach to find each of these variables: 
    for every index we send a pointer out to the left looking for height of max peak to the left
    and vice versa for right

This would take O(n^2) time complexity though. We want to do it in O(n) and in one pass

So take a shorcut
Rather asking question "What is the max height of a peak to right of this index?"
We instead ask "Is there a peak to the right of this index that's at least as big as our current leftMax?"
If the answer is "Yes", then we actually don't care if there is a rightMax that is bigger than that
So long as it's at least as big as our current leftMax we can guarantee that there is a region where some water can be tapped

We use two pointers 
one starting from the left and and one starting from the right
both travelling inward
to keep track of leftMax and rightMax respectively

And as long as the max value a pointer has seen is less than the max value of it's opposite
then that pointer can proceed inwards

Time complexity         O(n)
Space complexity        O(1)
 */

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        
        if (n < 3) return 0;
        

        int left(0), right(n - 1), leftMax(0), rightMax(0), res(0);
        
        while (left < right){
            leftMax = max(leftMax, height[left]);
            rightMax = max(rightMax, height[right]);
            if (leftMax <= rightMax){
                res += leftMax - height[left];
                ++left;
            }
            else{
                res += rightMax - height[right];
                --right;
            }
        }
        
        return res;
    }
};