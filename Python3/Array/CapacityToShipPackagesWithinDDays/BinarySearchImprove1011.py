from typing import List
import math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid_capacity(capacity: int) -> bool:
            days_used = 1
            day_capacity_left = capacity
            for weight in weights:
                if weight > capacity:
                    return False
                if weight > day_capacity_left:
                    # Reset
                    if days_used == days:
                        return False
                    days_used += 1
                    day_capacity_left = capacity

                day_capacity_left -= weight

            return True

        left = max(weights)
        # This might be the key of getting faster
        right = math.ceil(len(weights) / days) * left

        while left < right:
            mid = left + (right - left) // 2
            if not is_valid_capacity(mid):
                left = mid + 1
            else:
                right = mid

        return left
