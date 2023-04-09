from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        WA

        [4,0,2,1,2,5,5,3]
        3
        Expected: 1
        """
        nums.sort()
        diff1 = [0] * (len(nums) // 2)
        diff2 = [0] * (len(nums) // 2)
        for i in range(0, len(nums), 2):
            diff1[i // 2] = nums[i + 1] - nums[i]
            if i + 2 < len(nums):
                diff2[i // 2] = nums[i + 2] - nums[i + 1]
        # print(nums, diff1, diff2)

        return min(sum(diff1[:p]), sum(diff2[:p]))
