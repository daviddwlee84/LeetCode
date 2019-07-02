from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        startIdx = 0
        endIdx = len(nums)

        while endIdx > startIdx:
            if nums[startIdx] == val:
                nums[startIdx] = nums[endIdx - 1]
                endIdx -= 1  # reduce array size by one
            else:
                startIdx += 1

        return endIdx
