class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
            if n % 4 != 0:
                break
            n /= 4
        return False
