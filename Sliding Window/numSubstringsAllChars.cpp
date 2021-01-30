// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

// Version 1 - Sliding window
// Time complexity          O(n)
// Space complexity         O(1)
class Solution {
public:
    int numberOfSubstrings(string s) {
        int result = 0;
        
        // Tracks the counts of each of a,b and c in the current substring
        int abcCount[3] = {0, 0, 0};
        
        int n = s.size();
        int front = 0;
        for (int back = 0; back < n - 2; ++back){
            // Move the front of the window forward until a, b and c are present in the substring
            while ( (front < n) && (abcCount[0] == 0 || abcCount[1] == 0 || abcCount[2] == 0) ){
                ++abcCount[s[front] - 97];
                ++front;
            }
            // Either all of abc are present in the substring, in which case all substrings
            // in the set s[back:front], s[back:front + 1], s[back:front + 2] ... s[back:n]
            // are valid and are counted toward the result
            if (abcCount[0] > 0 && abcCount[1] > 0 && abcCount[2] > 0){
                result += n - (front - 1);
            }
            // Or abc are not present and front has reached the end of the string
            // there are no more valid strings that can be found by moving back along
            // i.e. narrowing the window is not doing anything to find more chars 
            else break;
            // Decerement the chars that are now no longer in the narrowed window
            --abcCount[s[back] - 97];
        }
        return result;
    }
};

// Version 2 - Same as V1 but allows for more letters other than abc
class Solution {
public:
    int numberOfSubstrings(string s) {
        int result = 0;

        int abcCount[3] = {0, 0, 0};
        
        int n = s.size();
        int front = 0;
        for (int back = 0; back < n - 2; ++back){
            while ( (front < n) && (abcCount[0] == 0 || abcCount[1] == 0 || abcCount[2] == 0) ){
                int frontLetterIdx = s[front] - 97;
                if (frontLetterIdx < 3) ++abcCount[frontLetterIdx];
                ++front;
            }
            if (abcCount[0] > 0 && abcCount[1] > 0 && abcCount[2] > 0){
                result += n - (front - 1);
            }
            else break;
            int backLetterIdx = s[back] - 97;
            if (backLetterIdx < 3) --abcCount[backLetterIdx];
        }
        return result;
    }
};

// Version 3 - sliding window but track indices not counts
// Fastest submission I could find on LC for reference
class Solution {
public:
    int numberOfSubstrings(string s) {
        int aIndex = -1, bIndex = -1, cIndex = -1;
        int i, j;
        int ans = 0;
        for(i = 0; i < s.length(); ++i){
            if (s[i]=='a') aIndex = i;
            else if (s[i]=='b') bIndex = i;
            else if (s[i]=='c') cIndex = i;
            if(aIndex != -1 && bIndex != -1 && cIndex != -1){
                ans += 1;
                j = min(aIndex, bIndex);
                j = min(j , cIndex);
                ans += j;
            }
        }
        return ans;
    }
};