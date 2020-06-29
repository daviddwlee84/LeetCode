from itertools import product


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        https://leetcode.com/problems/unique-paths/discuss/711190/Python-2-solutions%3A-dp-and-oneliner-math-explained
        https://leetcode.com/problems/unique-paths/discuss/711209/Summary-of-4-different-solutions-w-Recursion-Tree
        """

        dp = [[1] * n for _ in range(m)]

        for i, j in product(range(1, m), range(1, n)):
            # product: cartesian product, equivalent to a nested for-loop
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

# Runtime: 28 ms, faster than 81.01% of Python3 online submissions for Unique Paths.
# Memory Usage: 14 MB, less than 25.51% of Python3 online submissions for Unique Paths.
