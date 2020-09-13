from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        previous = None  # None: init; 1: positive; -1: negative
        length = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > 0:
                if previous == -1 or previous is None:
                    length += 1
                previous = 1
            elif diff < 0:
                if previous == 1 or previous is None:
                    length += 1
                previous = -1

        return length

# Runtime: 32 ms, faster than 82.09% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 13.9 MB, less than 52.46% of Python3 online submissions for Wiggle Subsequence.
