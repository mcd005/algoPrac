/*
https://leetcode.com/problems/defanging-an-ip-address/

Very basic string manipulation

Time complexity 	O(n)
Space compexity 	O(1)
*/

#include <algorithm>
#include <string>


class Solution {
public:
    string defangIPaddr(string address) {
        string output = "";
        for (char c: address){
            if (c == '.'){
                output += "[.]";
            }
            else{
                output += c;
            }
        }
        return output;
    }
};

/*

//Alternate solution, but appears to be slower than above

#include <algorithm>
#include <string>


class Solution {
public:
    string defangIPaddr(string address) {
        return regex_replace(address, regex("[.]"), "[.]");
    }
};
*/