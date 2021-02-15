# // https://leetcode.com/problems/minimum-time-difference/
# See .cpp for explanation
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        for i in range(n):
            timePoints[i] = (int(timePoints[i][0:2]), int(timePoints[i][3:5]))
            
        timePoints.sort(key = lambda tp : (tp[0], tp[1]))
        
        minDiff = 24 * 60
        for i in range(n):
            if (i < n - 1):
                curDiff = (timePoints[i + 1][0] - timePoints[i][0]) * 60 + timePoints[i + 1][1] - timePoints[i][1]
            else:
                curDiff = (timePoints[0][0] + 24 - timePoints[i][0]) * 60 + timePoints[0][1] - timePoints[i][1]
            minDiff = min(curDiff, minDiff)
            
        return minDiff