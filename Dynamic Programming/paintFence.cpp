/*
https://leetcode.com/problems/paint-fence/

Large number of combinations suggest DP approach
Here is what building up from the base case looks like:
    1 post can be done k ways
    2 posts can be done k^2 ways
    3 post could be done k^3 ways but in the cases where post 1 and 2 are the same colour, k of those k^3 ways are illegal
        Think of this removing the combinations
        c1 c1 c1
        c2 c2 c2
        c3 c3 c3
    so
    3 posts can be done k^3 - k ways
    4 post could be done k * (k^3 - k) ways but 

Base case is the first two posts. They can each be one of k colours
However once we get to the third post we assume that the first two posts are the same colour.
Without the "three adjacent post cannot be same colour" restriction, the numbers of ways of painting the fence would be k^3
Because of this restriction k of those combinations are illegal so we have k^3 - k



Time complexity		O(n)
Space complexity 	O(1)

1 post can be done k ways
2 posts can 

*/

class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0 || k == 0) return 0;
        
        int odds = 0;
        int evens = 0;
        int pre = k;
        int cur = pre;
        
        for (int i = 2; i < n + 1; i++){
            if (i % 2 == 0){
                cur = pre * k - evens + odds;
                odds += pre;
            }
            else{
                cur = pre * k - odds + evens;
                evens += pre;
            }
            pre = cur;
        }
        
        return pre;
    }
}; 

