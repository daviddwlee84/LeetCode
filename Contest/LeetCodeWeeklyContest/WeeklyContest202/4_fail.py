from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        elif n % 6 == 0:
            return min(self.minDays(n - 2 * (n // 3)), self.minDays(n - n // 2), self.minDays(n - 1)) + 1
        elif n % 3 == 0:
            return min(self.minDays(n - 2 * (n // 3)), self.minDays(n - 1)) + 1
        elif n % 2 == 0:
            return min(self.minDays(n - n // 2), self.minDays(n - 1)) + 1
        else:
            return self.minDays(n - 1) + 1

# RecursionError: maximum recursion depth exceeded in comparison
# 820592
