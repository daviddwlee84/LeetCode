class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        https://leetcode.com/problems/patching-array/discuss/78492/C%2B%2B-8ms-greedy-solution-with-explanation
        https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation
        """
        answer = 0

        i = 0  # index of nums
        max_num = 0  # the maximum range that we can reach currently

        while max_num < n:
            if i < len(nums) and nums[i] <= max_num + 1:
                # the current maximum range already contain the current num
                # we can just use it without any cost and expand the maximum range
                max_num += nums[i]
                i += 1
            else:
                # we have to expand the range
                max_num += max_num + 1
                answer += 1

        return answer

# Runtime: 64 ms, faster than 76.32% of Python3 online submissions for Patching Array.
# Memory Usage: 14 MB, less than 37.50% of Python3 online submissions for Patching Array.
