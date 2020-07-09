from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/3sum/discuss/725581/Python-2-Pointers-O(n2)-solution-explained
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            begin, end = i + 1, n - 1
            while begin < end:
                if nums[begin] + nums[end] < target:
                    begin += 1
                elif nums[begin] + nums[end] > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[begin], nums[end]))
                    # keep searching the same target
                    begin += 1
                    end -= 1

        return set(result)

# Runtime: 1208 ms, faster than 41.54% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than 29.24% of Python3 online submissions for 3Sum.
