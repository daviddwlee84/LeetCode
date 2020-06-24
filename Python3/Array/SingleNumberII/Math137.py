from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/single-number-ii/discuss/700780/Python-Easy-to-understand-(beats-99.85-)-simple-maths
        """
        return (3*sum(set(nums))-sum(nums))//2
