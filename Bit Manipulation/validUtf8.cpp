// https://leetcode.com/problems/utf-8-validation/

// Version 1 - Use bitmasking to get the relevant MSBs
// checking the bytes comply with the rules as given
// by using two pointers.
// Also take care to account for the order in which you check MSBs
// Time complexiy       O(n)
// Space complexity     O(1) 
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int n = data.size();
        
        // Need a min of one byte for valid char
        if (n == 0) return false; 
        
        // Slow will check the header/leading byte, fast will check the continuation bytes
        int slow = 0, fast = 0;
        while (slow < n){
            // Bit mask the 5 MSBs to see how many continuation bytes to expect
            int msbs = data[slow] & 0b11111000;
            
            // 0b10000000 is only legal for a continuation byte, not a header
            // Equally can't have more than 3 continuation bytes, 
            // given constraint that char is max 4 bytes
            if ((msbs & 0b11000000) == 0b10000000 || msbs > 0b11110000) return false;
            
            int contBytes = 0;
            // >= accounts for trailing 1s that haven't been masked e.g. 11001
            // this is why we check contBytes in descending order
            if (msbs == 0b11110000) contBytes = 3;
            else if (msbs >= 0b11100000) contBytes = 2;
            else if (msbs >= 0b11000000) contBytes = 1;
            while (fast < slow + contBytes){
                ++fast;
                // Verify that there are as many continuation bytes as claimed
                // If we reach the end of the array and still haven't seen all the continuation bytes
                // we know we have invalid char
                if (fast >= n || (data[fast] & 0b11000000) != 0b10000000) return false;
            }
            // Once we've checked all the continuation bytes move to the next header and repeat
            ++fast;
            slow = fast;
        }
        
        // If we reach the end of the array then all chars must be valid utf
        return true;
    }
};

// Version 2 - Adapted from the top speed solution on LC
// Checks the MSBs by bit shifting rather than bitmasking
// Time complexiy       O(n)
// Space complexity     O(1) 
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        for(int i = 0; i < data.size(); ++i)
        {
            int number = data[i];
            int ones = 0;
            int shift = 7;
            while (shift >= 0)
            {
                // Starting from MSB count the number of 1s until you reach a 0
                if (number & (1 << shift))
                    ++ones;
                else
                    break;
                --shift;
            }
            if (shift < 0) return false; // byte was all 1s
            if (ones == 0) continue; // i.e. a valid one byte char
            if (ones == 1) return false;
            if (ones > 4) return false; 
            --ones;
            int j = i + 1;
            while(j < data.size() && ones)
            {
                int followed = data[j++];
                // Checking that byte is 0b10xxxxxx
                if (!(followed & (1 << 7)) || followed & (1 << 6)) return false;
                --ones;
            }
            if(j == data.size() && ones) return false;
            i = j - 1;
        }
        return true;
    }
};

// Version 3 - An adapted version for situations
// where the input array is a string not a vector
#include<bitset>
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        string newInput = "";
        for (auto d: data){
            string nextByte = bitset<8>(d & 0b11111111).to_string();
            //cout << nextByte << endl;
            newInput += nextByte;
        }
        
        return helper(newInput);
    }
    
    bool helper(string word){
        int n = word.size();
        if (n == 0 || n % 8 != 0) return false;

        int bytePtr = 0, bytePtrFast = 0;
        while (bytePtr < n)
        {
            int bitPtr = 0;
            while (word[bytePtr + bitPtr] == '1' && bitPtr < 5) ++bitPtr;
            if (bitPtr == 1 || bitPtr == 5) return false;
            int continuationBytesExpected = bitPtr - 1;

            while (bytePtrFast < bytePtr + continuationBytesExpected * 8)
            {
                bytePtrFast += 8;
                if (bytePtrFast >= n || 
                    word[bytePtrFast] != '1' || 
                    word[bytePtrFast + 1] != '0') return false;
            }
            bytePtrFast += 8;
            bytePtr = bytePtrFast;
        }
        return true;
    }
};