#include <math.h>
class Solution
{
public:
    int countGoodNumbers(long long n)
    {
        long long MOD = pow(10, 9) + 7;
        long long ans = 1;
        ans *= (long long)pow(5, n - n / 2) % MOD;
        ans %= MOD;
        ans *= (long long)pow(4, n / 2) % MOD;
        ans %= MOD;
        return ans;
    };
};

// WA
// 50
