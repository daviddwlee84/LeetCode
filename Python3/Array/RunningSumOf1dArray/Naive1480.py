from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0]
        for num in nums:
            running_sum.append(running_sum[-1] + num)

        return running_sum[1:]
