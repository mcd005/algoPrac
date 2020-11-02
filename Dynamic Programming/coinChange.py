def coinChange(coins, amount):
    n = len(coins)

    dp = [0] + [10**4 + 1] * amount

    for i in range(n + 1):
        for j in range(coins[i - 1], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)

    return dp

print(coinChange([1,2,5], 11))