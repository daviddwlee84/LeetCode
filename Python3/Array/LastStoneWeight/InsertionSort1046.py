from typing import List
from bisect import insort


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def helper(sorted_stones: List[int]) -> int:

            if not sorted_stones:
                return 0

            if len(sorted_stones) == 1:
                return sorted_stones[0]

            first = sorted_stones.pop()
            second = sorted_stones.pop()

            if first > second:
                insort(sorted_stones, first - second)

            # print(sorted_stones)

            return helper(sorted_stones)

        return helper(sorted(stones))
