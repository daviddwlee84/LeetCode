from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        """
        https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/solutions/3360907/image-explanation-dp-prefix-sum-c-java-python/
        """
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        # 2D prefix sum
        # Apple that exist in the rest part of the pizza
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                prefix_sum[r][c] = prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - \
                    prefix_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k: int, r: int, c: int) -> int:
            # No Apple left
            if prefix_sum[r][c] == 0:
                return 0
            # No need to cut => current piece
            if k == 0:
                return 1

            ans = 0
            # Try cut horizontal
            for nr in range(r + 1, m):
                # Try each cut that at least contain an Apple
                if prefix_sum[r][c] - prefix_sum[nr][c] > 0:
                    ans = (ans + dp(k - 1, nr, c)) % MOD
            # Try cut vertical
            for nc in range(c + 1, n):
                # Try each cut that at least contain an Apple
                if prefix_sum[r][c] - prefix_sum[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD

            return ans

        return dp(K - 1, 0, 0)
