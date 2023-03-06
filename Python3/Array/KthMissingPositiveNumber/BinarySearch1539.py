from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/kth-missing-positive-number/solutions/3262334/day-65-binary-seach-o-logn-time-o-1-space-easiest-beginner-friendly-sol/?orderBy=hot
        """
        left = 0
        right = len(arr)
        # print([num - (i + 1) for i, num in enumerate(arr)])

        while left < right:
            mid = left + (right - left) // 2

            # Number of missing number
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid

        return left + k
