from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pos_diff = [max(heights[i + 1] - heights[i], 0)
                    for i in range(len(heights) - 1)]

        diff_sum = 0
        diff_taken = []

        for i, diff in enumerate(pos_diff):
            if diff == 0:
                continue

            if diff_sum + diff <= bricks:
                diff_sum += diff
                heapq.heappush(diff_taken, -diff)
            else:
                if diff != 0 and ladders:
                    diff_sum += diff
                    heapq.heappush(diff_taken, -diff)
                    diff_sum += heapq.heappop(diff_taken)
                    ladders -= 1
                else:
                    return i

        return i + 1
