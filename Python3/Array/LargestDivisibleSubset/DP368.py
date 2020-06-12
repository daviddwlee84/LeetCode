from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/largest-divisible-subset/discuss/684738/Python-Short-DP-with-O(n2)-explained-(update)
        """
        if not nums:
            return []

        nums.sort()

        # initialize dp matrix
        sol = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                # because we have sorted the nums, we can just calculate in Si % Sj direction
                # and we only need to calculate if it has the potential to getting longer (otherwise we might miss override)
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]

        return max(sol, key=len)

# Runtime: 432 ms, faster than 68.49% of Python3 online submissions for Largest Divisible Subset.
# Memory Usage: 13.9 MB, less than 67.71% of Python3 online submissions for Largest Divisible Subset.
