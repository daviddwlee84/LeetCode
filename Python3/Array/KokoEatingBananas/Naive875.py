from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        Brute Force
        """
        for speed in range(1, max(piles) + 1):
            hours_taken = 0
            for pile in piles:
                while pile > 0 and hours_taken <= H:
                    pile -= speed
                    hours_taken += 1

                if hours_taken > H:
                    break

            if hours_taken == H:
                return speed
