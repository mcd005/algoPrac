/*
https://leetcode.com/problems/robot-bounded-in-circle/

The robot is bounded in a circle if and only if, after the first cycle of instructions:
    the direction it is facing is not north
    or
    it's ended at it's starting postion (0, 0)

To handle direction I assigned N = 0, E = 1, S = 2, W = 3
In version 1, I used a helper function to handle cases of negative direction (i.e. if the robot had to turn left when it was pointing north)
In version 2, I used smarter modulo maths to deal with this (a left turn is equal to three right turns)
A version 3 could be quicker still by avoiding branching with if statements and would look something like:
    x += d[i][0]; y += d[i][1];
Where d[][] = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};

Time complexity:    O(n)
Space complexity:   O(1)

An alternative approach could have been to use a cyclical doubly linked list to handle directions: 
    NESW for each node val, R turn would mean traverse to next node, L turn to previous
*/

// Version 2
class Solution {
public:
    bool isRobotBounded(string instructions) {
        int direction = 0; 
        int x = 0;
        int y = 0;
        
        int n = instructions.size();
        for (int i = 0; i < n; ++i){
            char instruction = instructions[i];
            
            if (instruction == 'G'){
                if (direction == 0) y++;
                else if (direction == 1) x++;
                else if (direction == 2) y--;
                else x--;
            }
            else if (instruction == 'R'){
                direction = (direction + 1) % 4;
            }
            else{
                direction =  (direction + 3) % 4;
            }
        }
        
        return ( direction != 0 || (x == 0 && y == 0) ) ? true : false;
    }
};

// Version 1
class Solution {
public:
    bool isRobotBounded(string instructions) {
        int direction = 0; //N = 0, E = 1, S = 2, W = 3 and again N = 0 etc with the use of a helper function
        int x = 0;
        int y = 0;
        
        int n = instructions.size();
        for (int i = 0; i < n; ++i){
            char instruction = instructions[i];
            
            if (instruction == 'G'){
                if (direction == 0) y++;
                else if (direction == 1) x++;
                else if (direction == 2) y--;
                else x--;
            }
            else if (instruction == 'R'){
                direction++;
            }
            else{
                direction--;
            }
            direction = trueDirection(direction);
        }
        
        return ( direction != 0 || (x == 0 && y == 0) ) ? true : false;
    }
    
    int trueDirection(int rawDirection){
        if (rawDirection < 0){
            return 4 - abs(rawDirection % 4);
        }
        return rawDirection % 4;
    }
};