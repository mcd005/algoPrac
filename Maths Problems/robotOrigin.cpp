// https://leetcode.com/problems/robot-return-to-origin/
// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (auto mv: moves){
            if (mv == 'U') ++y;
            else if (mv == 'D') --y;
            else if (mv == 'L') --x;
            else ++x;
        }
        return x == 0 && y == 0;
    }
};