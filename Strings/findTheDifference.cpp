/* 
https://leetcode.com/problems/find-the-difference/

XOR all the the chars together and the difference will come out in the wash

Time complexity         O(n)
Space complexity        O(1)
 */
class Solution {
public:
    char findTheDifference(string s, string t) {
        char result = t[0];
        
        for (int i = 1; i < t.size(); i++){
            result ^= t[i];
        }
        
	    //Actually only need to loop one time (see below)
        for (int i = 0; i < s.size(); i++){
            result ^= s[i];
        }
        
        return result;
    }
};

/* Looping 1 time
for (int i = 0; i < s.size(); i++){
            result ^= t[i] ^ s[i];
}
        
return result ^ t.back();
*/
