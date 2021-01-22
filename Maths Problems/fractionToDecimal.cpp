// # https://leetcode.com/problems/fraction-to-recurring-decimal/

// Version 1 - long division simulated
// When we've see the same remainder for the second time, we have a repeating sequence
// + lots of additional logic to handle the various edge cases
// Time complexity          O(period of repeating segment)      there is some theory of modulo maths that can work this out I think
// Space complexity         O(period of repeating segment)
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";

        string output = "";
        // Two minuses make a plus so we XOR
        if (numerator < 0 ^ denominator < 0) output += "-";
        
        //Long to avoid int overflow when 10x the remainder
        long n = labs(numerator), d = labs(denominator);
        output += to_string(n / d);
        
        n %= d;
        //I.e. if numerator / denominator gives an integer result
        if (n == 0) return output;
        
        output += ".";
        int i = output.size();
        unordered_map<long, int> seenNumerators;
        // Here we are keeping track of where in the post decimal sequence the repetend begins
        seenNumerators.insert({n, i});
        while (n > 0 ){
            
            long multiplier = 10;
            output += to_string(n * multiplier / d);
            
            int nextNumerator = n * multiplier % d;
            
            // When the nextNumerator (i.e. the remainder) has been seen before
            // we have a repeating sequence
            // use seenNumerators to check where the sequence started 
            // and bracket it per the instructions
            if (seenNumerators.find(nextNumerator) != seenNumerators.end()){
                output.insert(seenNumerators[nextNumerator], "(");
                output += ")";
                break;
            }
            
            seenNumerators.insert({n, i});
            ++i;
            n = nextNumerator;
        }
        return output;
    }
};