class Solution:
    def mySqrt(self, x: int) -> int:
        """ recursive """
        return self.recursiveFind(x, 0, x)

    def recursiveFind(self, x: int, left: int, right: int):
        if left == right:
            if left * left == x:
                return left
            else:
                return left - 1

        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            return self.recursiveFind(x, mid + 1, right)
        else:
            return self.recursiveFind(x, left, mid)

# Runtime: 36 ms, faster than 59.57% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Sqrt(x).
