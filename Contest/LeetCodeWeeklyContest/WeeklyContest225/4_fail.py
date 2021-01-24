class Solution:
    def minimumBoxes(self, n: int) -> int:
        total = 0
        floor = 0
        i = 1
        while total < n:
            floor += i
            total += floor
            i += 1

        return floor

# WA
# 15
# 9
# count too much
