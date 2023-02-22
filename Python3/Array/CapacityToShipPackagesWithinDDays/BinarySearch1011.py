from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        
        while start < end:
            mid = start + (end - start) // 2
            # print(start, mid, end, self.test_valid(weights, days, mid))
            if self.test_valid(weights, days, mid):
                end = mid
            else:
                start = mid + 1
        
        return start
        
    @staticmethod
    def test_valid(weights: List[int], days: int, capacity: int) -> bool:
        temp = 0
        # debug = [[]]
        for weight in weights:
            # print(weight, debug, days, temp, capacity)
            if days < 0:
                return False
            if temp + weight <= capacity:
                temp += weight
                # debug[-1].append(weight)
            else:
                # debug.append([weight])
                temp = weight
                days -= 1
        return days > 0
