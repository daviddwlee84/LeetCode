from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            mid = start + (end - start) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours > H:
                start = mid + 1
            else:
                end = mid

        return start

# Runtime: 456 ms, faster than 86.68% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15 MB, less than 60.11% of Python3 online submissions for Koko Eating Bananas.
