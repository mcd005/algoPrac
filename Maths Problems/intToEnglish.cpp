// https://leetcode.com/problems/integer-to-english-words/

// Version 1
// Time complexity      O(n) for an n digit number
// Space complexity     O(n)
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        
        string ones[10] = {"",
                           "One", 
                           "Two",
                           "Three",
                           "Four",
                           "Five",
                           "Six",
                           "Seven",
                           "Eight",
                           "Nine"};
        
        string tens[10] = {"",
                           "", 
                           "Twenty",
                           "Thirty",
                           "Forty",
                           "Fifty",
                           "Sixty",
                           "Seventy",
                           "Eighty",
                           "Ninety"};
        
        string teens[10] = {"Ten",
                            "Eleven", 
                            "Twelve",
                            "Thirteen",
                            "Fourteen",
                            "Fifteen",
                            "Sixteen",
                            "Seventeen",
                            "Eighteen",
                            "Nineteen"};
        
        string output = "";
         // This is so we don't add a space before the leading word
         // but do for subsequent words
        string padding = "";
        
        vector<int> digits = digitise(num);
        int i = digits.size() - 1;
        
        // This flag will allow us to ignore 3 consecutive zeros
        bool seenNonZero = false;
        while (i > -1) {
            int curDigit = digits[i];
            if (curDigit != 0){
                seenNonZero = true;
                if ((i - 2) % 3 == 0){
                output += padding + ones[curDigit] + " Hundred";
                }
                else if ((i - 1) % 3 == 0){
                    if (curDigit != 1) output += padding + tens[curDigit];
                    else {
                        int nextDigit = digits[i - 1];
                        output += padding + teens[nextDigit];
                        --i;
                    }
                }
                else output += padding + ones[curDigit];
            }
            
            // You only want to mention a jump in 3 orders of magnitude when there are
            // non-zero digits within those 3 orders of magitude
            if (seenNonZero) {
                if (i == 3) output += " Thousand";
                else if (i == 6) output += " Million";
                else if (i == 9) output += " Billion";
            }
            if (i % 3 == 0) seenNonZero = false;

            --i;
            padding = " ";
        }
        
        return output;
    }
    
    // Helper function to break a number into its digits
    vector<int> digitise(int num){
        vector<int> out;
        
        while (num > 0){
            out.push_back(num % 10);
            num /= 10;
        }
        
        return out;
    } 
};