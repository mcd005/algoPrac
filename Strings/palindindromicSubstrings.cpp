// https://leetcode.com/problems/palindromic-substrings/

// Time complexity       O(n^2)
// Space complexity      O(1)
class Solution {
public:
    int countSubstrings(string s) {
        int result = 0;
        
        int n = s.size();
        for (int i = 0; i < n; i++){
            // Each char is itself a palindrome so count it
            ++result;
            
            int j = 1, k = 1; 
            // This while loop allows us to count palindromes whose length are an even number of chars
            // e.g. would kick in for the "nn" in "hannah"
            while (i + 1 - j >= 0 && i + j < n && s[i + 1 - j] == s[i + j]){
                ++j;
                ++result;
            }
            // This while loop allows us to count palindromes whose length are an odd number of chars
            // e.g. would kick in for the "cec" in "racecar"
            while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]){
                ++k;
                ++result;
            }
            // N.B if we wanted to be more memory efficient
            // we could reuse j for both loops if we reassign it to 1 after the first
            // However it's faster in ms using 3 pointers 
            // (beats 100% on Leetcode with 3 ptrs vs 90% with two)
        }
        return result;
    }
};