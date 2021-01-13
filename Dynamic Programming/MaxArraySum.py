'''
Problem description: https://www.hackerrank.com/challenges/max-array-sum/

Brute force would require a large number of combinations, which suggest dynamic programming solution

As we iterate through the input array, the question we are asking is:
    "What is the maximum value of this element + all the elements before it that it can be legally added to?"
However knowing the answer to this question requires asking the same question of the elements before it

So we use a bottom up, tabluarisation approach. We declare an array dp to store solutions to subproblems
dp[0] and dp[1] are the base cases because the answer to the above quesiton for these are trivial:

dp[0] - There are no elements before it so it maximum value is the value of dp[0]
dp[1] - Only dp[0] is the element before dp[1] and these can't be legally added together. so dp[1] = max(dp[0],dp[1])

From here we iterate through both the input array and the dp array and ask which of these is biggest:
	The element itself
	The dp element before it
	Or the dp before that (which is the sum of all the legal elements before that)
	Or the element itself + the dp before element before the dp element before it (i.e. 2 indices back)

When we have iterated through the entire array the last value of dp will be the answer

Time complexity         O(n)
Space complexity        O(n)    This could be done more space efficiently, using constant space. We only need to remember dp[i - 1] and dp[i - 2].
'''

# #Used to read large test cases from files
# test_input = open("MaxArraySum_TestCases_2.txt", "r")
# inputSize = int(test_input.readline())
# inputArrayStr = test_input.readline().split()
# inputArray = [int(numeric_string) for numeric_string in inputArrayStr]
# test_input.close()

def maxSubsetSum(arr, n):
    dp = [0] * n
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(arr[i], dp[i - 1], dp[i - 2], dp[i - 2] + arr[i])

    return dp[n - 1]

print(maxSubsetSum(inputArray, inputSize))