from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/minimize-deviation-in-array/solutions/3223541/day-55-priority-queue-easiest-beginner-friendly-sol/
        """
        max_heap = []
        # min_value = min(num if num % 2 == 0 else num * 2 for num in nums)
        min_value = float('inf')
        min_deviation = float('inf')

        # Greedily convert all number into their maximum form
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(max_heap, -num)
                min_value = min(min_value, num)
            else:
                heapq.heappush(max_heap, -num * 2)
                min_value = min(min_value, num * 2)

        # print(max_heap, min_value)

        while True:
            # Try every potential
            max_value = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_value - min_value)

            # print(max_value, min_deviation)

            if max_value % 2 == 1:
                # Can't reduce max value anymore
                break
            max_value //= 2

            # Update minimum value and add back to max heap
            min_value = min(min_value, max_value)
            heapq.heappush(max_heap, -max_value)
            # print(max_value, min_value)
        
        return min_deviation
