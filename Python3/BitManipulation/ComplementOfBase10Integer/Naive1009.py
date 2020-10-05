class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        i = 0
        temp = num
        while temp > 0:
            temp //= 2
            i += 1

        # Get the minimum power of 2 that is larger than num
        # The complement is the same as the remainder
        return (2 ** i - 1) % num

# Runtime: 28 ms, faster than 69.43% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Complement of Base 10 Integer.
