from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        total_candies = 0
        for i in range(len(ratings)):
            total_candies += max(left2right[i], right2left[i])

        return total_candies

# Runtime: 168 ms, faster than 51.33% of Python3 online submissions for Candy.
# Memory Usage: 16.6 MB, less than 78.06% of Python3 online submissions for Candy.
