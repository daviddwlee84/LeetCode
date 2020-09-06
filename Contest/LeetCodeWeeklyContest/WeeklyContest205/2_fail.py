from itertools import combinations


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        squares_num1 = set(num**2 for num in nums1)
        squares_num2 = set(num**2 for num in nums2)

        answer = 0

        for num_j, num_k in combinations(nums1, 2):
            if num_j * num_k in squares_num2:
                answer += 1

        for num_j, num_k in combinations(nums2, 2):
            if num_j * num_k in squares_num1:
                answer += 1

        return answer
