class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        reach_one = False
        while n:
            if n & 1:
                if not reach_one:
                    reach_one = True
                else:
                    return False
            n = n >> 1

        # 0 case, so don't direct return True
        return reach_one

# Runtime: 40 ms, faster than 15.33% of Python3 online submissions for Power of Two.
# Memory Usage: 13.7 MB, less than 77.41% of Python3 online submissions for Power of Two.
