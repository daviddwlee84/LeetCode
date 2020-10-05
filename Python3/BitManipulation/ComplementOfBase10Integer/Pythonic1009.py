class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # int(str, 2) => convert to base 10 from base 2
        # Use bin to get binary digits; Use XOR to reverse digit
        return int(''.join([str((int(c) ^ 1)) for c in bin(N)[2::]]), 2)

# Runtime: 32 ms, faster than 49.35% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 14 MB, less than 15.35% of Python3 online submissions for Complement of Base 10 Integer.
