from typing import List
# this is python 3.8 feature...
# https://docs.python.org/3/library/math.html#math.comb
# from math import comb

import operator as op
from functools import reduce


def comb(n: int, r: int) -> int:
    """
    https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
    """
    if n < r:  # this is necessary
        return 0

    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        k -= 1
        v, h = destination

        answer = []

        while h or v:
            ways = comb(h - 1 + v, v)
            if k < ways:
                answer.append('H')
                h -= 1
            else:
                answer.append('V')
                v -= 1
                k -= ways

        return ''.join(answer)

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Kth Smallest Instructions.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Kth Smallest Instructions.
