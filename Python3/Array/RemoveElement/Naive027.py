from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        startIdx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[startIdx] = nums[i]
                startIdx += 1
        return startIdx
