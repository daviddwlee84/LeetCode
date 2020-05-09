class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            if i * i > num:
                return False
            elif i * i == num:
                return True

# Runtime: 32 ms, faster than 46.70% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 14 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.
