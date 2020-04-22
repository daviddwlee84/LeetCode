from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Directly find the sum on the go while considering different end points

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                if s == k:
                    count += 1

        return count
