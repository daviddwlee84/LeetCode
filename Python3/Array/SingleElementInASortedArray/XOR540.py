from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        bitmap = 0
        for num in nums:
            bitmap ^= num

        return bitmap
