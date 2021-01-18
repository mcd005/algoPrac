// Version 3 - like Version 1 but only uses constant space
// Instead of appending to the end of the orignal array we overwrite the start
// This form of the algorithm (single pointer with overwrites) 
// yields the fastest code in ms, in both cpp and py
// Time complexity       O(n)
// Space complexity      O(n) 
class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 1) return 1;
        
        char prevChar = chars[0];
        int seqLength = 1;
        int writeHead = 0;
        
        for (int i = 1; i < n; ++i){
            if (chars[i] == prevChar) ++seqLength;
            else{
                chars[writeHead++] = prevChar;
                if (seqLength > 1){
                    string seqLengthString = to_string(seqLength);
                    for (auto c: seqLengthString) {
                        chars[writeHead++] = c;
                    }
                }
                seqLength = 1;
            }
            prevChar = chars[i];
        }
        
        chars[writeHead++] = prevChar;
                if (seqLength > 1){
                    string seqLengthString = to_string(seqLength);
                    for (auto c: seqLengthString) {
                        chars[writeHead++] = c;
                    }
                }
        
        return writeHead;
    }
};

// Version 2 - a tidied version of V1
// We have an extra iteration in th loop so that the code that
// Time complexity       O(n)
// Space complexity      O(n) 
class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 1) return 1;
        
        char prevChar = chars[0];
        int seqLength = 1;
        
        for (int i = 1; i < n + 1; ++i){
            if (i < n && chars[i] == prevChar) ++seqLength;
            else {
                chars.push_back(prevChar);
                if (seqLength > 1){
                    string seqLengthString = to_string(seqLength);
                    for (auto c: seqLengthString) {
                        chars.push_back(c);
                    }
                }
            seqLength = 1;
            }
            prevChar = chars[i];
        }
        
        chars.erase(chars.begin(), chars.begin() + n);
        
        return chars.size();
    }
};

// Version 1 - one pointer
// Time complexity       O(n)
// Space complexity      O(n) 
class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 1) return 1;
        
        char prevChar = chars[0];
        int seqLength = 1;
        
        for (int i = 1; i < n; ++i){
            // Keep track of how long a sequence goes on for
            if (chars[i] == prevChar) ++seqLength;
            // If it's interrupted, add the char of the interrupeted sequence to the end of the vector
            else{
                chars.push_back(prevChar);
                // As per the stipulations
                // if the sequence is longer than a single character
                // add it's comma separated digits
                if (seqLength > 1){
                    string seqLengthString = to_string(seqLength);
                    for (auto c: seqLengthString) {
                        chars.push_back(c);
                    }
                }
                seqLength = 1;
            }
            prevChar = chars[i];
        }
    
        // This is tidied in V2
        // Kept here because this allows V1 to run faster
        chars.push_back(prevChar);
        if (seqLength > 1){
            string seqLengthString = to_string(seqLength);
            for (auto c: seqLengthString) {
                chars.push_back(c);
            }
        }
        
        // Thought we had to tidy up original array
        // See comment at the bottom of Version 1 in compressString.py
        chars.erase(chars.begin(), chars.begin() + n);
        
        return chars.size();
    }
};