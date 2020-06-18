from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        https://leetcode.com/problems/h-index/discuss/693375/Short-C%2B%2B-Solution
        """
        if not citations:
            return 0
        N = len(citations)
        left, right = 0, N
        while left < right:
            mid = left + (right - left) // 2
            if citations[mid] < N - mid:
                left = mid + 1
            else:
                right = mid

        return N - left
