import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        2147483648 is 2^31
        https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/593317/Simple-3-line-Java-solution-faster-than-100
        """
        while n > m:
            n &= n - 1
        
        return m & n
