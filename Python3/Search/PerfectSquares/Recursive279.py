from functools import lru_cache


class Solution:
    def numSquares(self, n: int) -> int:
        self.total = float('inf')
        self.find_minimum(n, 0)
        return self.total

    @lru_cache(None)
    def find_minimum(self, n: int, count: int):
        if n == 0:
            self.total = min(self.total, count)
            return

        if count > self.total:
            return

        for i in range(1, n + 1):
            if i <= n ** 0.5:
                self.find_minimum(n - i**2, count + 1)
            else:
                break

# TLE
# 221
# 224
# 123
