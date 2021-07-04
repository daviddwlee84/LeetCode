from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans
