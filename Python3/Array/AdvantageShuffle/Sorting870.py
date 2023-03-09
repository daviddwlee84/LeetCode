from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/advantage-shuffle/solutions/1125119/python-greedy-solution-two-pointers-explained/
        """
        # 2, 7, 11, 15
        # 1, 4, 10, 11

        # 8, 12, 24, 32 (x)
        # 11, 13, 25, 32
        # 12, 24, 32, 8 (o)

        sorted_num1 = sorted(nums1, reverse=True)
        sorted_num2 = sorted(
            enumerate(nums2), key=lambda x: x[1], reverse=True)
        answer = [0] * len(nums1)

        start = 0  # largest candidate
        end = len(nums1) - 1  # smallest candidate

        # Start from the largest one
        for ori_idx, num in sorted_num2:
            if sorted_num1[start] > num:
                answer[ori_idx] = sorted_num1[start]
                start += 1
            else:
                # If not applicable, use the smallest one
                answer[ori_idx] = sorted_num1[end]
                end -= 1
        return answer
