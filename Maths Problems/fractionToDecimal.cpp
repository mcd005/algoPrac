// Not yet complete
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator % denominator == 0) return to_string(numerator / denominator);

        string result = "0.";
        
        while (numerator > 0){
            cout << numerator << " ";
            result += to_string(numerator * 10 / denominator);
            numerator = numerator * 10 % denominator;
            cout << numerator << endl;
        }
        return result;
    }
};

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator % denominator == 0) return to_string(numerator / denominator);
        
        numerator = (long long) numerator;
        denominator = (long long) denominator;
        
        string temp = "";
        
        while (numerator > 0){
            int digitsToAdd = 0;
            while (numerator * 10 < denominator){
                denominator *= 10;
                ++digitsToAdd;
            }
            cout << 400 % 333 << endl;
            numerator = 0;
        }
        
        
        // temp += to_string(numerator / denominator)
        // numerator / denominator
        return "0."; //+ temp;
    }
};

//Int overflow