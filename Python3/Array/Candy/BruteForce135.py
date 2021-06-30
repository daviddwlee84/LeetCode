from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        TLE: https://leetcode.com/submissions/detail/514303860/testcase/
        """
        candies = [1] * len(ratings)
        has_changed = True
        while has_changed:
            has_changed = False
            for i in range(len(ratings)):
                if i != len(ratings) - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    has_changed = True

                if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    has_changed = True

        return sum(candies)
