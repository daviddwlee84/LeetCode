class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        https://leetcode.com/problems/arranging-coins/solution/

        Solve equation:

        k(k+1) <= 2N

        k = sqrt(2N + 1/4) - 1/2
        """
        return int((2 * n + 0.25) ** 0.5 - 0.5)

# Runtime: 32 ms, faster than 86.95% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.6 MB, less than 96.67% of Python3 online submissions for Arranging Coins.
