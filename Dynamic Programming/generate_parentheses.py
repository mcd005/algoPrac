# https://leetcode.com/problems/generate-parentheses/
# Version 1 - Recursive with memoisation
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.memo = {}
        self.memo[1] = ["()"]
        return self.generate(n)

    def generate(self, n):
        if n not in self.memo:
            new_combos = set()
            for combo in self.generate(n - 1):
                new_combos.add('(' + combo + ')')
            for i in range(1, n):
                for lhs in self.generate(i):
                    for rhs in self.generate(n - i):
                        new_combos.add(lhs + rhs)
            self.memo[n] = list(new_combos)
        return self.memo[n]

# Version 2 - Tabular DP. Logic is similar to recursive but more concise
class Solution:
    def generateParenthesis(self, n):
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

'''
We generate recursively
The base case is n == 1 where we just have an open and close brace otherwise for n > 1
We have an arrangement that looks like '(' + generate(n - 1) + ')'
Then the rest are generate(i) + generatate(n - i)
'''