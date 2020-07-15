class Solution:
    def reverseBits(self, n: int) -> int:
        reverseStr = bin(n)[2:][::-1]
        reverseStr = '0b' + reverseStr + '0' * (32 - len(reverseStr))
        return int(reverseStr, 2)
