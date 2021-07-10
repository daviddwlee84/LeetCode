from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        The array `d` is to store the LIS. The d[i] is the minimum value of the last element.
        The length of `d` is the LIS length itself.
        https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
        """
        d = []
        for num in nums:
            if not d or num > d[-1]:
                # Greedily pick any possible number to get longer increasing subsequence
                d.append(num)
            else:
                # Binary Search in the array `d` to find a replacement
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= num:
                        # The best replacement is the value "just larger than or equal to the number"
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = num

        return len(d)

# Runtime: 80 ms, faster than 86.72% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.6 MB, less than 75.22% of Python3 online submissions for Longest Increasing Subsequence.
