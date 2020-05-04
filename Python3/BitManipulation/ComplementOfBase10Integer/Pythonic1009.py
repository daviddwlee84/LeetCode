class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # int(str, 2) => convert to base 10 from base 2
        return int(''.join([str((int(c) ^ 1)) for c in bin(N)[2::]]), 2)
