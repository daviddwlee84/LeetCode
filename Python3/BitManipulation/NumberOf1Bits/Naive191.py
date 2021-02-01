class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n:
            s += n & 1
            n >>= 1
        return s
