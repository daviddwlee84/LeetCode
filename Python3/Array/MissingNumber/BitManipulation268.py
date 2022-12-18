from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bit = 2 ** (len(nums) + 1) - 1
        for num in nums:
            bit ^= 1 << num

        ans = 0
        while bit != 1:
            ans += 1
            bit >>= 1

        return ans
