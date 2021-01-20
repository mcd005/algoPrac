
// alpha is used to keep track of the lowest index each letter occurs
// If the same letter is encountered twice mark it's lowest index as 
// one that is beyond the array (i.e. can't possible be the minIndex)

// Iterate through alpha, comparing the indices of all the unique chars
// and return the minimum

// Time complexity      O(n)
// Space complexity     O(1)
class Solution {
public:
    int firstUniqChar(string s) {
        int n = s.size();
        
        int alpha[26] = {[0 ... 25] = n};
    
        
        for (int i = 0; i < n; ++i){
            int index = s[i] - 97;
            if (alpha[index] == n){
                alpha[index] = i;
            }
            else if (alpha[index] < n){
                alpha[index] = n + 1;
            }
        }
        
        int minIndex = n;
        
        for (int i = 0; i < 26; ++i){
            minIndex = min(alpha[i], minIndex);
        }
        
        return minIndex != n ? minIndex : -1;
    }
};

//Version 2
// repeat the above but rather than iterating through s once and alpha once
// iterate through s twice, on the second run checking for the first char whose count is 1
