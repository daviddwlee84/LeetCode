from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort(nums, 0, len(nums)-1)
        return nums[-k]

    def quicksort(self, nums: List[int], start: int, end: int):
        if start < end:
            split = self._partition(nums, start, end)
            # quick sort left part
            self.quicksort(nums, start, split-1)
            # quick sort right part
            self.quicksort(nums, split+1, end)

    def _partition(self, nums: List[int], start: int, end: int):
        pivot = nums[end]  # use last element as pivot
        i = start - 1 # index of smaller element
        for j in range(start, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1
