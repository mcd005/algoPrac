/*
https://leetcode.com/problems/reverse-words-in-a-string-iii/

When you encounter a space reverse all the chars between it and the previous space (i.e prevSpace idx + 1)
Make sure to account for the edge case when for loop reaches end of string

Time complexity 	O(n)
Space complexity 	O(1)
*/

class Solution {
public:
    string reverseWords(string s) {
        // int n = s.size();
        // if (n == 0) return s;
        
        int prevSpace = 0;
        
        for (int i = 0; i < s.size(); i++){
            if (isspace(s[i])){
                reverse(s.begin() + prevSpace, s.begin() + i);
                prevSpace =  i + 1;
            }    
        }
        reverse(s.begin() + prevSpace, s.end());
        
        return s;
    }
};