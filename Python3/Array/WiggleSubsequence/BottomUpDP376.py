from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev_up = 1
        prev_down = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff > 0:  # ascending
                prev_up = prev_down + 1
            elif diff < 0:  # descending
                prev_down = prev_up + 1

        return max(prev_up, prev_down)

# Runtime: 24 ms, faster than 99.16% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 13.8 MB, less than 72.46% of Python3 online submissions for Wiggle Subsequence.
