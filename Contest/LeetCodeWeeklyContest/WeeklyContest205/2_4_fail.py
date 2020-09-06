from itertools import combinations
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        comb = Counter(combinations(nums2, 2))
        for num in nums1:
            square_num = num ** 2
            for (num_j, num_k), cnt in comb.items():
                if square_num == num_j * num_k:
                    answer += cnt

        comb = Counter(combinations(nums1, 2))
        for num in nums2:
            square_num = num ** 2
            for (num_j, num_k), cnt in comb.items():
                if square_num == num_j * num_k:
                    answer += cnt

        return answer

# TLE
