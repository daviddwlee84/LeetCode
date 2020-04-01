from typing import List
import heapq


class Solution:
    """ greedy with priority queue """

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        priorityQueue = []
        result = 0
        speedSum = 0
        # sorted so it will start from the highest efficiency
        # for the same efficiency, it will be sorted from the highest speed
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            # each time push speed into priority queue
            heapq.heappush(priorityQueue, s)
            speedSum += s

            if len(priorityQueue) > k:
                # if items is more than the limit, remove the one with the lowest speed
                speedSum -= heapq.heappop(priorityQueue)

            result = max(result, speedSum * e)

        # if use 1e9 with int() it just won't work in the very large case
        return result % (10**9 + 7)

# Runtime: 424 ms, faster than 77.49% of Python3 online submissions for Maximum Performance of a Team.
# Memory Usage: 28.6 MB, less than 100.00% of Python3 online submissions for Maximum Performance of a Team.


if __name__ == "__main__":
    print(Solution().maxPerformance(
        6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2), 60)
    print(Solution().maxPerformance(
        3, [2, 8, 2], [2, 7, 1], 2), 56)
    print(Solution().maxPerformance(
        3, [2, 8, 1], [2, 7, 2], 2), 56)
