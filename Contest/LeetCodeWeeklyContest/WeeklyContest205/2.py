from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        counter2 = defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                mul = nums2[i] * nums2[j]
                counter2[mul] += 1
        for num in nums1:
            square = num ** 2
            if square in counter2:
                ans += counter2[square]

        counter1 = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                mul = nums1[i] * nums1[j]
                counter1[mul] += 1
        for num in nums2:
            square = num ** 2
            if square in counter1:
                ans += counter1[square]

        return ans
