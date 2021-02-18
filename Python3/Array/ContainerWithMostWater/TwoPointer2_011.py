from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
        https://leetcode.com/problems/container-with-most-water/discuss/1069570/Python-2-Pointers-solution-explained
        https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms
        """
        start, end = 0, len(height) - 1
        ans = 0
        while start < end:
            ans = max(ans, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return ans

# Runtime: 156 ms, faster than 95.65% of Python3 online submissions for Container With Most Water.
# Memory Usage: 16.4 MB, less than 90.84% of Python3 online submissions for Container With Most Water.
