from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=os4B7MlHAbs

        Question in 2 cases

        1. [xxx [Max Subarray in Middle] xxx]
        2. [[Max ...] Min sum subarray [... Subarray]]

        We can prove that the middle part in the second case must be the "min sum" subarray

        Answer in 3 cases

        1. max_sum_subarray
        2. total_sum - min_sum_subarray
        3. largest element
        """

        total_sum = 0
        max_ending_at = 0
        min_ending_at = 0

        max_sum = float('-inf')
        min_sum = float('inf')

        for x in A:
            total_sum += x
            max_ending_at = max(max_ending_at + x, x)
            max_sum = max(max_ending_at, max_sum)

            min_ending_at = min(min_ending_at + x, x)
            min_sum = min(min_ending_at, min_sum)

        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum

# Runtime: 592 ms, faster than 58.28% of Python3 online submissions for Maximum Sum Circular Subarray.
# Memory Usage: 18.1 MB, less than 100.00% of Python3 online submissions for Maximum Sum Circular Subarray.
