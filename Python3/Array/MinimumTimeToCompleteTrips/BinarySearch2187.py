from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def able_to_complete(time: List[int], totalTrips: int, givenTime: int):
            return sum(givenTime // t for t in time) >= totalTrips

        left = 1
        right = max(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            if able_to_complete(time, totalTrips, mid):
                right = mid
            else:
                left = mid + 1

        return left
