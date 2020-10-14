from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Define state(i) as the minimum jumps to reach i
        state(i) = min(1 + state(j)) for each j that can jump to i.
        The goal state is state(nums.length - 1).
        https://leetcode.com/problems/jump-game-ii/discuss/541548/DP-and-Greedy
        """
        state = [float('inf')] * len(nums)
        state[0] = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] + j >= i:
                    state[i] = min(state[i], state[j] + 1)

        return state[-1]

# TLE: [1, 1, 1, ...]
# https://leetcode.com/submissions/detail/410040887/testcase/
