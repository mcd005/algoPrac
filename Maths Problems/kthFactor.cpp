class Solution
{
public:
    int kthFactor(int n, int k)
    {
        int counter = 0;
        for (int x = 1; x <= n; ++x)
        {
            if (n % x == 0)
            {
                ++counter;
                if (counter == k) return x; 
            }
        }
        return -1;
    }
};