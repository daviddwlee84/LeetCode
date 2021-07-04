class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        even = 0, 2, 4, 6, 8
        prime = 2, 3, 5, 7
        """
        MOD = 10 ** 9 + 7
        ans = 1
        ans *= 5 ** (n - n // 2)
        ans *= 4 ** (n // 2)
        ans %= MOD
        return ans

# TLE
# 806166225460393
