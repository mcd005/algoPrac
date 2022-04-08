class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i] :
                stack.pop()
            if stack:
                max_area = max(max_area, heights[stack[-1]] * (i + 1 - stack[-1]))
                if heights[stack[-1]] == heights[i]:
                    continue
            else:
                max_area = max(max_area, heights[i])
            if heights[i] > 0:
                stack.append(i)
        while stack:
            top = stack.pop()
            max_area = max(max_area, heights[top] * (n + 1 - top))
        return max_area

'''
[2,1,5,6,2,3]

s = [1,4]
max_area = 10


Brute force
For each index start a sliding window
The largest rectangle in the window is the min val in the window times by width of window

Would probably be better to think about it in the other direction
i.e move our window backwards from current index

Starting from index 0 we ask, what is the min among the heights behind me
If the min is current index then just go wide as possible


What if we did a sliding window where back sets the value of min
We move front forward whilst it's greater than or equal to min
If we hit a new min we start the window from there

For any non-zero height, we will always be able to do better than a min of 1
It's not like having lots of 1s 

Is this like kadanes? 
Where if the value of an height by itself is better than the preceding interval, we switch?
'''
