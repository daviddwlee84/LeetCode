from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        order = sorted(list(zip(capital, profits)))

        # print(order)

        candidate_projects = []

        i = 0
        while k:
            # Dump possible project into heap
            while i < len(profits) and order[i][0] <= w:
                # Push prices
                # (negative for max heap)
                heapq.heappush(candidate_projects, -order[i][1])
                i += 1

            # print(candidate_projects, w, k)

            if not candidate_projects:
                # Can't find project anymore
                break

            w -= heapq.heappop(candidate_projects)
            k -= 1

        return w
