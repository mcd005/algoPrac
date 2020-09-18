/*
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Not sure why I converted to binary in my Python soltion, you can already carry out binary ops on base 10 int
*/

class Solution {
public:
    int numberOfSteps (int num) {
        if (num == 1 || num == 0){
            return 0;
        }
        else {
            int steps = 0;
            int count = -1;
            while (num > 0){
                //cout << num << " " << num % 2 << endl;
                steps += (num % 2);
                num /= 2;
                count++;
            }
            return count + steps;
        }
        
    }
};