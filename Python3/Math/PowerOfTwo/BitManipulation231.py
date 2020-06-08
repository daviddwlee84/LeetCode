class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n - 1)))

# Runtime: 32 ms, faster than 60.00% of Python3 online submissions for Power of Two.
# Memory Usage: 13.6 MB, less than 95.45% of Python3 online submissions for Power of Two.
