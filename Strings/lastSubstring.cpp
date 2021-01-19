// https://leetcode.com/problems/last-substring-in-lexicographical-order/

//Version 2
// For shorthand "max substring" is last substring in lexicographical order, and "bigger" means further on in the lexicographical order
// "first" is the pointer to the index that is the start of our current max substring
// "second" is the pointer to a index that is the start of a potentially bigger substring. let's call this the candidate
// most of the time we can immediately eliminate the candidate; it will typically start with a smaller letter than "first"
// and so we keep on incrementing the pointer for second, looking for a new candidate

// However sometimes we encounter a char or sequence of chars that are equal to the ones that starts our max substring
// in this case, using "offset" to point to the correpsonding positions in both sequences, 
// we compare them until they are no longer equal and have diverged
// in this case either:

    // 1) the divergence was caused because a char in the candidate is bigger.
    // This means that we have found a new max substring and can update our pointer to first. 
    // (If first + offset exceeds second we can actually set our new first to 1 greater than this value;
    // we've already checked the elements after second, no need to check them again)

    // 2) at the divergence, a char in the orignal max substring is bigger. 
    // Our original substring is still the max
    // Set our second pointer to 1 index past the divergence so we aren't rechecking the same elements

// Alternatively we've reached the end of the string. In this case the candidate can't be bigger
// It's entirety is merely a susbtring of our max susbtring. By definition is lexicographically "smaller"
class Solution {
public:
    string lastSubstring(string s) {
        int first = 0, second = 1, offset = 0;
        int n = s.size();
        while (second + offset < n) {
            if (s[first + offset] == s[second + offset]) offset++;
            else if (s[first + offset] < s[second + offset]) {
                first = max(first + offset + 1, second);
                second = first + 1;
                offset = 0;
            } 
            else {
                second += offset + 1;
                offset = 0;
            }
        }
        return s.substr(first);
    }
};

// Version 1 - currently not working
// times out for large repeated chars e.g. aaaaaaaaaaaaaa...
// Need a way of jumping forward i because it is currently O(n^2)
class Solution {
public:
    string lastSubstring(string s) {
        int n = s.size();
        
        int maxIdx = 0;
        for (int i = 1; i < n; ++i){
            if (s[i] > s[maxIdx]){
                maxIdx = i;
            }
            else if (s[i] == s[maxIdx]){
                int j = 1; //This is our offset
                while (s[maxIdx + j] == s[i + j] && i + j < n) ++j;
                if (s[maxIdx + j] < s[i + j]) maxIdx = i;
                //Can we skip forward our i here?
            }
        }
        return s.substr(maxIdx);
    }
};

