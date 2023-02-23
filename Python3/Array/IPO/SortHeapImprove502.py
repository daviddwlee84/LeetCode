from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # In this case, we don't need to consider capital
        if w >= max(capital):
            return w+sum(heapq.nlargest(k, profits))

        # We only need to sort by capital since we will add all the same capital profit in the heap anyway
        order = sorted(list(zip(capital, profits)), key=lambda x: x[0])

        candidate_projects = []

        i = 0
        while k:
            # Dump possible project into heap
            while i < len(profits) and order[i][0] <= w:
                # Push prices
                # (negative for max heap)
                heapq.heappush(candidate_projects, -order[i][1])
                i += 1

            if not candidate_projects:
                # Can't find project anymore
                break

            w -= heapq.heappop(candidate_projects)
            k -= 1

        return w
