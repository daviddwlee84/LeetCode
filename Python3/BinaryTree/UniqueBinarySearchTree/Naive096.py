from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        total = 0
        # take turn to be the root
        for i in range(0, n):
            left_left = i - 0
            right_left = n - i - 1

            # left_count = self.numTrees(left_left)
            # right_count = self.numTrees(right_left)
            # if not left_count:
            #     total += right_count
            # elif not right_count:
            #     total += left_count
            # else:
            #     total += left_count * right_count

            total += max(1, self.numTrees(left_left)) * \
                max(1, self.numTrees(right_left))

        return total

# Runtime: 32 ms, faster than 47.87% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14 MB, less than 5.17% of Python3 online submissions for Unique Binary Search Trees.
