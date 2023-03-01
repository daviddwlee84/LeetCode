from typing import List
import bisect


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        answer = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = nums[i] + nums[j]

                # find the leftest edge of target
                left = bisect.bisect_left(nums, target, j + 1, len(nums))
                length = left - j - 1

                answer += length

        return answer
