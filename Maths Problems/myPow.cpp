// https://leetcode.com/problems/powx-n/
// Version 1 - Iterative
// Time complexity       O(logn)
// Space complexity      O(1)
double myPow(double x, int n)
{
    if (n == 0) return 1;
    if (n < 0)
    {
        n = -n;
        x = 1 / x;
    }
    double ans = 1;
    while (n > 0)
    {
        // Every time we encounter a 1 in the binary representation of n we want to mutliplt ans with 
        if (n & 1) ans *= x;
        x *= x;
        n >>= 1;
    }
    return ans;
}

// Version 2 - Recursive
// Time complexity       O(logn)
// Space complexity      O(logn)
double myPow(double x, int n)
{
    if (n == 0) return 1;
    if (n < 0)
    {
        n = -n;
        x = 1 / x;
    }
    return n % 2 == 0 ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
}

/*
Naive: If we want to get x^n and we can't use built in pow() then we could do x * x * x .... n times
But we want to reduced the number of times thats required
So we can do x^n = x^a * x^b * x^c
Where a, b and c sum to n
Easiest to do this with binary because we know how combinations of powers of two can sum to n
e.g. 9 = 2^3 + 2^0 = 1001
So if we we go back to the example x^9 = x^(2^3) * x(2^0)
So what we need to do is just times have some value ans = 1
And then times ans by x^(2^i), for the ith bit of n that is equal to 1
Then we add some extra logic to deal with negative powers of n
*/