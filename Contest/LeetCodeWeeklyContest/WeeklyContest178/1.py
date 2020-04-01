from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    answer[i] += 1

        return answer
