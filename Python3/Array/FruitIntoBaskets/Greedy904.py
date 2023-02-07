from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Keep the window size MAX (this is a little bit trick)

        https://leetcode.com/problems/fruit-into-baskets/solutions/170740/java-c-python-sliding-window-for-k-elements/
        https://leetcode.com/problems/fruit-into-baskets/solutions/2960000/fruit-into-baskets/
        """
        basket = defaultdict(int)
        oldest_fruit = 0
        for fruit in fruits:
            basket[fruit] += 1
            
            # Whenever the basket contains more than 1 fruit, it will try to
            if len(basket) > 2:
                basket[fruits[oldest_fruit]] -= 1
                
                # Keep remove until the the oldest fruit has been removed
                if basket[fruits[oldest_fruit]] == 0:
                    basket.pop(fruits[oldest_fruit])

                # Shrink the window size
                oldest_fruit += 1

        return len(fruits) - oldest_fruit

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         basket = defaultdict(int)
#         max_sum = 0
#         for fruit in fruits:
#             if len(basket) < 2:
#                 basket[fruit] += 1
#             else:
#                 if fruit in basket:
#                     basket[fruit] += 1
#                 else:
#                     for f in basket.keys():
#                         if f != last_fruit:
#                             another_fruit = f
#                     basket.pop(another_fruit)
#                     basket[fruit] += 1
#
#             max_sum = max(max_sum, sum(basket.values()))
#             last_fruit = fruit
#
#         return max_sum

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         basket = defaultdict(int)
#         last_fruit = None
#         last_fruit_continue_count = 0
#         temp_basket = defaultdict(int)
#         max_sum = 0
#         for fruit in fruits:
#             if len(basket) < 2:
#                 basket[fruit] += 1
#                 temp_basket[fruit] += 1
#             else:
#                 if fruit in basket:
#                     basket[fruit] += 1
#                     temp_basket[fruit] += 1
#                 else:
#                     for f in basket.keys():
#                         basket[f] -= temp_basket[f]
#                     temp_basket.clear()
#                     basket[last_fruit] += last_fruit_continue_count
#
#                     for f in basket.keys():
#                         if f != last_fruit:
#                             another_fruit = f
#                     basket.pop(another_fruit)
#
#                     basket[fruit] += 1
#
#             max_sum = max(max_sum, sum(basket.values()))
#             if fruit == last_fruit:
#                 last_fruit_continue_count += 1
#             else:
#                 last_fruit_continue_count = 0
#             last_fruit = fruit
#
#         return max_sum
