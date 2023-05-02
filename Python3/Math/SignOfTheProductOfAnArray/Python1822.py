from typing import List
from functools import reduce
from operator import mul


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x: int) -> int:
            if x == 0:
                return 0
            elif x > 0:
                return 1
            else:
                return -1

        # Somewhat equivalent
        # (this can avoid overflow issue in C/C++)
        # return reduce(mul, map(signFunc, nums))

        return signFunc(reduce(mul, nums))
