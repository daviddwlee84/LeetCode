class Solution:
    def minOperations(self, n: int) -> int:
        """
        Alex Wice's Solution

        [1 3 5]
         2   4
         3   3

        [1 3 5 7]
         2 4 4 6
         3     5
         4     4
        """
        ans = 0

        for x in range(1, 2 * n, 2):
            ans += abs(x - n)

        return ans >> 1
