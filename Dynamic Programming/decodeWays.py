'''
https://leetcode.com/problems/decode-ways/

Combinatorial explosion indicates use of dynamic programming solution

We start by asking: "What is the number of ways a message of length 1 can be decoded?"
The answer is obviously only one
Then we ask: "What is the number of ways a a message of length 2 can be decoded?


Improved from second attempt solution by:
Making it constant space. Before we had an array of size n + 1
However we only need to remember the i - 1 and i - 2 values in the array
So instead we just made those into variables
    prePre = dp[i - 2]
    pre = dp[i - 1]
    cur = dp[i]
Then each iteration we shift each variable as if its gone back by 1

Time complexity		O(n)
Space complexity	O(1)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        cur = 0
        
        prePre = 1
        if s[0] == '0':
            return 0
        else:
            pre = 1
            
        for i in range(2, n + 1):
            if int(s[i-1:i]) != 0:
                cur += pre
            if 10 <= int(s[i-2:i]) <= 26:
                cur += prePre
            # print(prePre, pre, cur)
            prePre, pre, cur = pre, cur, 0
        
        return pre


'''
##First attempt##

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        
        if n == 1:
            return 1
        
        def validPair(st, i):
            if (int(st[i - 1]) > 2 or st[i - 1] == '0') and st[i] == '0':
                return False
            else:
                return True
        
        if not validPair(s, 1):
            return 0
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = dp[0] if s[1] == '0' or (int(s[0])*10 + int(s[1]) > 26) else dp[0] + 1
        
        for i in range(2,n):
            if not validPair(s, i):
                return 0
            elif (s[i - 1] == '0') or (int(s[i - 1])*10 + int(s[i]) > 26):
                dp[i] = dp[i - 1]
            elif s[i] == '0':
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]



##Second attempt: DP with tabularisation##

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0 for x in range(n + 1)]
        
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
            
        for i in range(2, n + 1):
            if int(s[i-1:i]) != 0:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        print(dp)
        
        return dp[n]
    

#Improved from first attemp solution by:
#Making DP size n + 1 using list comprehension, extra dp is used to account for edge cases
#Have one if statement to check the single digit not equal to zero in which case dp[i] += dp[i - 1]
#Have another if statement to check if the double digit is valid in which case dp[i] += dp[i - 2]
#Return the last value of dp
'''