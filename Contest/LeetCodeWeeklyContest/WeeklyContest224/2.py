from typing import List
from itertools import combinations
from collections import Counter
from math import comb


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        # 2 3 4 6 8 12
        # 4*6 = 2*12
        # 4*6 = 8*3
        # 3 (4)
        #
        products = Counter(a*b for a, b in combinations(nums, 2))
        same_product = 0
        for product, count in products.items():
            if count > 1:
                # https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
                same_product += comb(count, 2) * 8

        return same_product
