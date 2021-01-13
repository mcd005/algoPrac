# https://leetcode.com/problems/coin-change/

# Version 1 - Tabularisation approach
# 
# Time complexity       O(n * m)
# Space complexity      O(n)   
# 
# where n is "amount" divided by the smallest denomination 
# and m is the number of denominations
# Rather than build the entire table, which is typical of the tabularisation approach 
# and requires O(n * m) space
# you can build one row and modify it in place
def coinChange(coins, amount):
    n = len(coins)

    dp = [0] + [10**4 + 1] * amount

    for i in range(1, n + 1):
        for j in range(coins[i - 1], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)

    return dp

# Version 2 - Returns which denominations are needed
def coinChange2(coins, amount):
    numDenoms = len(coins)

    numNeeded = [0] + [10**4 + 1] * amount
    firstCoin = [0] * (amount + 1)

    for i in range(1, numDenoms + 1):
        for j in range(coins[i - 1], amount + 1):
            numNeeded[j] = min(numNeeded[j], numNeeded[j - coins[i - 1]] + 1)
            firstCoin[j] = coins[i - 1]

    coinsUsed = []
    changeLeft = amount
    while changeLeft > 0:
        coinsUsed.append(firstCoin[changeLeft])
        changeLeft -= firstCoin[changeLeft]

    return coinsUsed

# Driver code
print(coinChange2([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000], 1125))

# min(dp[j], dp[j - coins[i - 1]] + 1)
# In plain English this could be:
# What is smaller?
# the number of coins used to meet this value without the denomination that was just added
# OR
# The number of coins used to meet an amount equal to the current amount minus the denomination just added plus 1
