from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_count = 0
        one_count = 0
        counts = [(0, 0)]
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1

            counts.append((zero_count, one_count))

        max_length = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                diff = self.tupleMinus(counts[j], counts[i])
                if diff[0] == diff[1]:
                    max_length = max(max_length, j - i)

        return max_length

    @staticmethod
    def tupleMinus(a, b):
        return tuple(x - y for x, y in zip(a, b))

# Time Limit Exceeded
