from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Alex Wice's Solution
        """

        graph = defaultdict(list)

        # Same number can be treated as the same node in the graph
        for i in range(len(nums1) - 1):
            graph[nums1[i]].append(nums1[i+1])
        for i in range(len(nums2) - 1):
            graph[nums2[i]].append(nums2[i+1])

        graph[nums1[-1]]  # point to null
        graph[nums2[-1]]

        dp = defaultdict(int)
        # sorted, so we will get the largest key (same as graph.keys())
        for node in sorted(graph, reverse=True):
            dp[node] = node  # include its value
            # if a node has neighbor
            if graph[node]:
                # we only consider the max (because we can only build one path?!)
                dp[node] += max(dp[neighbor] for neighbor in graph[node])

        return max(dp.values()) % (10 ** 9 + 7)

# Runtime: 1276 ms, faster than 42.86% of Python3 online submissions for Get the Maximum Score.
# Memory Usage: 57.8 MB, less than 100.00% of Python3 online submissions for Get the Maximum Score.
