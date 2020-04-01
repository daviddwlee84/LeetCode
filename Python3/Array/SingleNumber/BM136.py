from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            # xor
            # the bit of the number itself will be reversed when xor
            a ^= num
        return a
