from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Dynamic Window Size

        Sliding Window II
        https://leetcode.com/problems/fruit-into-baskets/solutions/2960000/fruit-into-baskets/
        """
        basket = defaultdict(int)
        max_picked = 0
        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            # If the current window has more than 2 types of fruit,
            # we remove fruit from the left index (left) of the window,
            # until the window has only 2 types of fruit.
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                
                # Keep remove until the the oldest fruit has been removed
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])

                left += 1
            
            max_picked = max(max_picked, right - left + 1)

        return max_picked
