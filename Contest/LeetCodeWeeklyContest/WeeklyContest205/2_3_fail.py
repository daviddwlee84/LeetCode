from itertools import combinations


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        for num in nums1:
            square_num = num ** 2
            for num_j, num_k in combinations(nums2, 2):
                if square_num == num_j * num_k:
                    answer += 1

        for num in nums2:
            square_num = num ** 2
            for num_j, num_k in combinations(nums1, 2):
                if square_num == num_j * num_k:
                    answer += 1

        return answer

# TLE
