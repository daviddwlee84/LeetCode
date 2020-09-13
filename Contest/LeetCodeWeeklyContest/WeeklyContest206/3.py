from typing import List
from itertools import combinations
from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [(i, *point) for i, point in enumerate(points)]

        edges = defaultdict(list)
        heap = []
        for (i, xi, yi), (j, xj, yj) in combinations(points, 2):
            dest = abs(xi - xj) + abs(yi - yj)
            # print(i, j, dest)
            edges[i].append((j, dest))
            edges[j].append((i, dest))
            heapq.heappush(heap, (dest, i, j))

        # print(heap)

        selected = set()
        answer = 0
        pending = []
        while heap:
            dest, i, j = heapq.heappop(heap)
            # print(i, j, dest)
            if not selected or ((i in selected) ^ (j in selected)):
                # print(selected)
                selected.add(i)
                selected.add(j)
                answer += dest
                while pending:
                    heapq.heappush(heap, pending.pop())
            elif (i not in selected) and (j not in selected):
                pending.append((dest, i, j))

        return answer


if __name__ == "__main__":
    print(Solution().minCostConnectPoints(
        [[2, -3], [-17, -8], [13, 8], [-17, -15]]), 53)
