from typing import List
from itertools import combinations
import numpy as np


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """ brute force """
        max_dot_product = float('-inf')
        for k in range(1, min(len(nums1), len(nums2)) + 1):
            for subnums1 in combinations(nums1, k):
                for subnums2 in combinations(nums2, k):
                    max_dot_product = max(max_dot_product, np.dot(
                        np.array(subnums1), np.array(subnums2)))

        return max_dot_product

# TLE
