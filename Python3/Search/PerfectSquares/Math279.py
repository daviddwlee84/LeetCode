class Solution:
    def numSquares(self, n: int) -> int:
        """
        https://leetcode.com/problems/perfect-squares/discuss/707526/Python-Fastest-O(sqrt(n))-solution-with-math-explanied.
        https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem

        https://leetcode.com/problems/perfect-squares/discuss/707517/Python-no-DP-O(N)
        """
        if int(n ** 0.5) ** 2 == n:
            return 1

        for j in range(int(n ** 0.5) + 1):
            if int((n - j ** 2) ** 0.5) ** 2 == n - j ** 2:
                return 2

        while n % 4 == 0:
            n >>= 2

        if n % 8 == 7:
            return 4

        return 3

# Runtime: 40 ms, faster than 97.47% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14 MB, less than 55.91% of Python3 online submissions for Perfect Squares.
