
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        max_dot_product = float('-inf')
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                dp[i + 1][j + 1] = max(dp[i][j] + nums1[i]
                                       * nums2[j], dp[i+1][j+1])
                max_dot_product = max(max_dot_product, nums1[i] * nums2[j])

        if max_dot_product >= 0:
            max_dot_product = max(
                max_dot_product, dp[len(nums1)][len(nums2)])

        return max_dot_product
