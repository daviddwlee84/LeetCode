class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = left + (right - left) // 2
            square_mid = mid * mid

            if square_mid == num:
                return True
            elif square_mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 13.7 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.
