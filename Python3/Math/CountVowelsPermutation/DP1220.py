class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        j (a, e, i, o, u)
        0 a -> e
        1 e -> a, i
        2 i -> a, e, o, u
        3 o -> i, u
        4 u -> a
        """
        MOD = 10 ** 9 + 7
        dp = [[1, 1, 1, 1, 1]] + [[0] * 5 for _ in range(n - 1)]

        for i in range(1, n):

            # a
            dp[i][0] += dp[i - 1][1]  # e
            dp[i][0] += dp[i - 1][2]  # i
            dp[i][0] += dp[i - 1][4]  # u

            # e
            dp[i][1] += dp[i - 1][0]  # a
            dp[i][1] += dp[i - 1][2]  # i

            # i
            dp[i][2] += dp[i - 1][1]  # e
            dp[i][2] += dp[i - 1][3]  # o

            # o
            dp[i][3] += dp[i - 1][2]  # i

            # u
            dp[i][4] += dp[i - 1][2]  # i
            dp[i][4] += dp[i - 1][3]  # o

            for j in range(5):
                dp[i][j] %= MOD

        return sum(dp[n - 1]) % MOD


# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         a = e = i = o = u = 1
#         mod = 10 ** 9 + 7
#         for _ in range(1, n):
#             # https://docs.python.org/3/reference/expressions.html#evaluation-order
#             a, e, i, o, u = (e + u + i) % mod, (a + i) % mod, (e + o) % mod, i, (o + i) % mod
#         return sum([a, e, i, o, u]) % mod
