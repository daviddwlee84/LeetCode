from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        shift = 0
        while True:
            if start + shift < len(nums) and nums[start + shift] == target:
                return shift
            elif start - shift >= 0 and nums[start - shift] == target:
                return shift
            shift += 1
