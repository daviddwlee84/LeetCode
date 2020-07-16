class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation

        Note that
        if n & 1 was same as: if n % 2
        n >> 1 was same as : n //= 2
        """
        ans = 1
        absN = abs(n)
        while absN > 0:
            if absN & 1:
                ans *= x
            absN >>= 1
            x *= x

        if n < 0:
            ans = 1 / ans

        return ans
