from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Subtract the cumulative sum corresponding to the two indices to obtain the sum directly

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        count = 0
        cumulative_sum = [0]
        for i in range(len(nums)):
            cumulative_sum.append(cumulative_sum[-1] + nums[i])

        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if cumulative_sum[end] - cumulative_sum[start] == k:
                    count += 1

        return count
