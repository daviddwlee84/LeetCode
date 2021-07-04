#include <math.h>
class Solution
{
public:
    int countGoodNumbers(long long n)
    {
        long long MOD = pow(10, 9) + 7;
        long long ans = 1;
        for (long long i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                ans *= 5;
            }
            else
            {
                ans *= 4;
            }
            ans %= MOD;
        }

        return ans;
    }
};

// TLE
// 806166225460393
