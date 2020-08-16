from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        """
        next n =
          1. n - 1
          2. n / 2   if n % 2 == 0
          3. n / 3   if n % 3 == 0

        Consider if we want to make 2. move, then there is the case:

        n is even => directly do n/2
        n is odd  => do n - 1 first then n / 2

        Similar case when we want to make 3. move

        n is a multiple of three => directly do n / 3
        n is not a multiple of three => do n - 1 twice then n / 3
        """

        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return n

            return min(
                # (this is actually not needed, because the others are obviously better)
                # n,  # Don't make either 2. or 3. move
                dp(n // 2) + 1 + n % 2,  # make 2. move first
                dp(n // 3) + 1 + n % 3,  # make 3. move first
            )

        return dp(n)

# because the Constraints is 2*10^9, so any kind like BFS will not hold.


class Solution:
    memo = {}  # THIS CAN REUSE MEMO THROUGH THE TESTCASES!!!

    def minDays(self, n: int) -> int:
        """
        Equivalent with using lru_cache
        """

        def dp(n):
            if n not in Solution.memo:
                if n <= 1:
                    ans = n
                else:
                    ans = min(
                        dp(n // 2) + 1 + n % 2,  # make 2. move first
                        dp(n // 3) + 1 + n % 3,  # make 3. move first
                    )
                Solution.memo[n] = ans

            return Solution.memo[n]

        return dp(n)
