class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

# Runtime: 32 ms, faster than 79.57% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Sqrt(x).
