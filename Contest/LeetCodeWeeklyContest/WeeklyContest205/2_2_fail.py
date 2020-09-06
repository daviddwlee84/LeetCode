from collections import Counter
import math


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def combinations(n: int, k: int):
            return math.factorial(n) / math.factorial(n - k) / math.factorial(k)

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        answer = 0
        for num1 in counter1:
            for num2 in counter2:
                if num1 == num2:
                    if counter2[num2] >= 2:
                        answer += combinations(counter2[num2], 2) * 2

                elif num1 ** 2 % num2 in counter2:
                    answer += 1

        for num2 in counter2:
            for num1 in counter1:
                if num1 == num2:
                    if counter1[num1] >= 2:
                        answer += combinations(counter1[num1], 2) * 2

                elif num2 ** 2 % num1 in counter1:
                    answer += 1

        return int(answer / 2)
