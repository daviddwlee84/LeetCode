from functools import lru_cache


class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        """
        https://leetcode.com/problems/powx-n/discuss/19546/Short-and-easy-to-understand-solution
        https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        https://leetcode.com/problems/powx-n/discuss/182026/Python-or-Recursion-tm
        https://leetcode.com/problems/powx-n/discuss/19544/5-different-choices-when-talk-with-interviewers
        """
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 1:
            return x

        # Note: this style doesn't reduce the complexity
        # There are duplicate calculation, and thus we will need memory(cache) to deal with this
        return self.myPow(x, n // 2) * self.myPow(x, n - n // 2)

# Runtime: 32 ms, faster than 60.99% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.9 MB, less than 28.51% of Python3 online submissions for Pow(x, n).
