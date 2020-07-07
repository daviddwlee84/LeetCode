class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while num % factor == 0:
                num //= factor

        return num == 1

# Runtime: 40 ms, faster than 20.55% of Python3 online submissions for Ugly Number.
# Memory Usage: 14 MB, less than 11.24% of Python3 online submissions for Ugly Number.
