from typing import List
from collections import defaultdict
import math


class Solution:
    def waysToBuildRooms(self, arr: List[int]) -> int:
        """
        https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1299540/Python-clean-DFS-solution-with-explanation
        """
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for cur, pre in enumerate(arr):
            graph[pre].append(cur)

        def dfs(cur: int):
            """
            The number of ways to build rooms if we start at node cur
            return How many combination/possibility,  How may on the right branch
            """
            if not graph[cur]:
                return 1, 1
            ans, left = 1, 0
            for nxt in graph[cur]:
                tmp, right = dfs(nxt)
                ans = (ans * tmp * math.comb(left + right, right)) % MOD
                left += right
            return ans, left + 1

        return dfs(0)[0]

# Runtime: 4224 ms, faster than 25.00% of Python3 online submissions for Count Ways to Build Rooms in an Ant Colony.
# Memory Usage: 173.7 MB, less than 25.00% of Python3 online submissions for Count Ways to Build Rooms in an Ant Colony.
