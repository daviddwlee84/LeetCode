from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        This is a "literally" solution, and will TLE

        Time Complexity: O(n^2)
        """

        max_sum = 0

        for i in range(len(fruits)):

            basket = defaultdict(int)

            for fruit in fruits[i:]:
                if len(basket) < 2:
                    basket[fruit] += 1
                elif len(basket) == 2 and fruit in basket:
                    basket[fruit] += 1
                else:
                    # TODO: Do something here to improve
                    break

            max_sum = max(max_sum, sum(basket.values()))

        return max_sum
