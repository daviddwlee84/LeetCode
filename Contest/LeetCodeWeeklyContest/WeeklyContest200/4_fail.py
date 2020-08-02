from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_index_dict = defaultdict(list)
        self.nums2_index_dict = defaultdict(list)
        for i, num in enumerate(nums1):
            self.nums1_index_dict[num].append(i)

        for i, num in enumerate(nums2):
            self.nums2_index_dict[num].append(i)

        self.answer = 0
        self.dfs(0, -1, True, set())
        self.dfs(-1, 0, False, set())
        return self.answer

    def dfs(self, pointer_1: int, pointer_2: int, at_num1: bool, nums_set: set):
        if at_num1:
            nums_set.add(self.nums1[pointer_1])
            if pointer_1 == len(self.nums1) - 1:
                if self.nums1[pointer_1] not in self.nums2_index_dict or self.nums2_index_dict[pointer_1][-1] <= pointer_2:
                    self.answer = max(self.answer, len(nums_set))
                    return
            else:
                self.dfs(pointer_1 + 1, pointer_2, True, nums_set)

            for next_pointer_2 in self.nums2_index_dict[pointer_1]:
                if next_pointer_2 > pointer_2:
                    self.dfs(pointer_1, next_pointer_2, False, nums_set)

            nums_set.remove(self.nums1[pointer_1])

        else:
            nums_set.add(self.nums2[pointer_2])

            if pointer_2 == len(self.nums2) - 1:
                if self.nums2[pointer_2] not in self.nums1_index_dict or self.nums1_index_dict[pointer_2][-1] <= pointer_1:
                    answer = max(answer, len(nums_set))
                    return
            else:
                self.dfs(pointer_2 + 1, pointer_1, True, nums_set)

            for next_pointer_1 in self.nums1_index_dict[pointer_2]:
                if next_pointer_1 > pointer_1:
                    self.dfs(pointer_1, next_pointer_1, False, nums_set)

            nums_set.remove(self.nums2[pointer_2])
