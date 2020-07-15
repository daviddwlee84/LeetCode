class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        bit = 32
        while bit:
            reverse <<= 1
            reverse |= n & 1
            n >>= 1
            bit -= 1
        return reverse
