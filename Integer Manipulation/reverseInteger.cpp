/*
https://leetcode.com/problems/reverse-integer/

Save the sign of the input int
Convert input to absolute value
Convert int to string
Check if the int will produce a legal output (i.e. will not cause integer overflow if reversed)
Reverse the string
Convert it back to an int
Apply correct sign and return

Time complexity			O(n) 	for an n digit number
Space compexity			O(n) 	
*/

#include <string>
#include <algorithm>

class Solution {
public:
    int reverse(int x) {
        bool negative = (x < 0)? true: false;
        x = abs(x);
        std::string num = std::to_string(x);
        if (illegalInput(num, negative)) return 0;
        std::reverse(num.begin(), num.end());
        int rvsd = std::stoi(num);
        return negative? rvsd * -1 : rvsd;
    }
    
    bool illegalInput(string input, bool neg){
        int n = input.size();
        std::string legal = neg ? "2147483647":"2147483648";
        
        if (n > 10){
            return true;
        }
        else if (n == 10){
            for (int i = 0; i < n; i++){
                if (input[n - 1 - i] < legal[i]){
                    return false;
                }
                else if (input[n - 1 - i] > legal[i]){
                    return true;
                }
            }
            return false;
        }
        else{
            return false;
        }
    }
    
};
