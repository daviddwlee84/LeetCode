from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        # Both skip the last one (right most or left most num)
        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])
        for i in reversed(range(1, len(nums))):
            right.append(right[-1] * nums[i])

        answer = []
        for i in range(len(nums)):
            answer.append(left[i] * right[-i-1])

        return answer

# Runtime: 128 ms, faster than 51.90% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.7 MB, less than 36.00% of Python3 online submissions for Product of Array Except Self.
