class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            # corner case
            return 1

        ans = 0
        digit = 0
        while N:
            temp = 0
            if N & 1 == 0:
                # if we need an "1"
                temp = 1

            N >>= 1
            # put the "1" to the right position
            ans += temp << digit
            digit += 1

        return ans

# Runtime: 24 ms, faster than 92.83% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 14.2 MB, less than 5.45% of Python3 online submissions for Complement of Base 10 Integer.
