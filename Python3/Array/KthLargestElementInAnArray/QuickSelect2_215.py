from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums, 0, len(nums) - 1)
        # i.e. the kth smallest item is at the right part
        if k > pos + 1:
            # kind of update the target value k to k-pos-1
            return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
        # i.e. the kth smallest item is at the left part
        elif k < pos + 1:
            return self.findKthSmallest(nums[:pos], k)
        # found the target
        else:
            return nums[pos]

    def partition(self, nums: List[int], start: int, end: int) -> int:
        # nums[end] (right-most element) is pivot

        # low is the next element to be replaced
        low = start
        while start < end:
            if nums[start] < nums[end]:
                nums[start], nums[low] = nums[low], nums[start]
                low += 1
            start += 1

        # put pivot to the "pos"
        nums[end], nums[low] = nums[low], nums[end]

        return low

# Runtime: 2269 ms, faster than 8.22% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 117.2 MB, less than 5.51% of Python3 online submissions for Kth Largest Element in an Array.
