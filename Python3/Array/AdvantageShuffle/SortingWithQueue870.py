from collections import deque
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/advantage-shuffle/solutions/1125119/python-greedy-solution-two-pointers-explained/
        https://leetcode.com/problems/advantage-shuffle/solutions/149842/python-greedy-solution-using-sort/
        """
        sorted_nums1 = deque(sorted(nums1, reverse=True))
        sorted_nums2 = sorted(
            enumerate(nums2), key=lambda x: x[1], reverse=True)
        for i, num2 in sorted_nums2:
            # Override nums2 since it's unused
            nums2[i] = sorted_nums1.popleft(
            ) if sorted_nums1[0] > num2 else sorted_nums1.pop()
        return nums2
