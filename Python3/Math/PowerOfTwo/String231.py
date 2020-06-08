class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Bit Count
        """
        if n < 0:
            return False

        one_count = sum(char == '1' for char in bin(n)[2:])
        return one_count == 1

# Runtime: 32 ms, faster than 60.00% of Python3 online submissions for Power of Two.
# Memory Usage: 13.8 MB, less than 59.26% of Python3 online submissions for Power of Two.
