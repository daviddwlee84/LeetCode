class Solution:

    dp = [0]  # dp[i]: least number of square numbers that sum to i

    def numSquares(self, n: int) -> int:
        while len(self.dp) <= n:
            length = len(self.dp)
            minimum = float('inf')
            for j in range(1, n + 1):
                if j ** 2 > length:
                    break

                minimum = min(minimum, self.dp[length - j ** 2] + 1)

            self.dp.append(minimum)

        return self.dp[n]
