class Solution {
public:
    int balancedStringSplit(string s) {
        int result = 0, R = 0, L = 0;
        if (s.size() == 1){
            return 0;
        }
        for (char& c : s){
            if (c == 'R'){
                R++;
            }
            else{
                L++;
            }
            if (R == L){
                result++;
            }
        }
        return result;
    }
};