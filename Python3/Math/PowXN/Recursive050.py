class Solution:
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
            x = 1/x
            n = -n

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

# Runtime: 32 ms, faster than 60.99% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.9 MB, less than 34.36% of Python3 online submissions for Pow(x, n).
