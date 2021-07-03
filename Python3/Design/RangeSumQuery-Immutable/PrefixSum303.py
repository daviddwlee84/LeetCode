from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Runtime: 72 ms, faster than 93.07% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.8 MB, less than 45.85% of Python3 online submissions for Range Sum Query - Immutable.
