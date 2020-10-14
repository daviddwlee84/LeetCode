from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Jump when we have to jump, and jump to the furthest position.
        https://leetcode.com/problems/jump-game-ii/discuss/541548/DP-and-Greedy
        """
        if len(nums) < 2:
            return 0

        to_jump = 0
        num_jumps = 0

        max_reach = [0] * len(nums)

        for i, num in enumerate(nums):
            # Assuming we can jump to nums[i], we can reach up to max_reach[i]
            max_reach[i] = max(max_reach[i - 1], num + i)

        # Jump when we have to and count the jumps
        for i in range(len(nums)):
            if i == to_jump:
                num_jumps += 1
                if max_reach[i] >= len(nums) - 1:
                    break
                to_jump = max_reach[i]

        return num_jumps

# Runtime: 100 ms, faster than 58.02% of Python3 online submissions for Jump Game II.
# Memory Usage: 16.2 MB, less than 7.43% of Python3 online submissions for Jump Game II.
