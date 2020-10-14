from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C%2B%2B-(16ms)-Python-BFS-Solutions-with-Explanations
        """

        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

# Runtime: 112 ms, faster than 34.65% of Python3 online submissions for Jump Game II.
# Memory Usage: 16 MB, less than 7.43% of Python3 online submissions for Jump Game II.
