from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]
        for num in nums[:-1]:
            left_sum.append(left_sum[-1] + num)
        for num in nums[len(nums) - 1:0:-1]:
            right_sum.append(right_sum[-1] + num)

        return [abs(r - l) for r, l in zip(reversed(right_sum), left_sum)]
