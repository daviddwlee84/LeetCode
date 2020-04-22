from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Brute Force

        Time Complexity: O(n^3)
        Space Complexity: O(n)
        """
        count = 0
        # Considering every possible subarray O(n^2)
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):

                # Calculate sum O(n)
                if sum(nums[start:end]) == k:
                    count += 1

        return count
