from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        self.solution = set()

        for i, num_to_fix in enumerate(nums):
            target = 0 - num_to_fix
            self.twoSum(nums, target, i)

        return list(map(list, self.solution))

    def twoSum(self, nums: List[int], target: int, skip_index: int):
        """ two pointer """
        for i in range(len(nums)):
            if i == skip_index:
                continue
            for j in range(i + 1, len(nums)):
                if j == skip_index:
                    continue

                if nums[i] + nums[j] == target:
                    self.solution.add(
                        tuple(sorted([nums[i], nums[j], nums[skip_index]])))

# TLE
