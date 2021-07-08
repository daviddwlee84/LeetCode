from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Hint: Use dynamic programming. dp[i][j] will be the answer for inputs A[:i], B[:j].
        """

        # +1 to deal with the edge = 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        # Find the max value in this memory
        return max(max(row) for row in dp)

# Runtime: 3048 ms, faster than 77.87% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.4 MB, less than 59.38% of Python3 online submissions for Maximum Length of Repeated Subarray.
