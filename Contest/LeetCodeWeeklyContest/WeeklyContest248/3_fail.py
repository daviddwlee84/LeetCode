class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        even = 0, 2, 4, 6, 8
        prime = 2, 3, 5, 7
        """
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(n):
            if i % 2 == 0:
                ans *= 5
            else:
                ans *= 4
            ans %= MOD
        return ans

# TLE
# 806166225460393
