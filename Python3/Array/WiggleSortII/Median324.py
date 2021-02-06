from typing import List
import random


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        https://leetcode.com/problems/wiggle-sort-ii/discuss/333079/Python-deterministic-O(n)-time-%2B-O(1)-memory-quick-select-%2B-%22median-of-medians%22
        https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
        """
        def nsmallest(nums: List[int], n: int) -> int:
            """
            Quick Select; Used to find median
            return index
            """
            start, end = 0, len(nums) - 1
            while True:
                pivot = nums[random.randint(start, end)]
                i, j, k = start, end, start
                while k <= j:
                    if nums[k] < pivot:
                        nums[i], nums[k] = nums[k], nums[i]
                        i += 1
                        k += 1
                    elif nums[k] > pivot:
                        nums[j], nums[k] = nums[k], nums[j]
                        j -= 1
                    else:
                        k += 1
                if i <= n - 1 <= j:
                    return pivot
                elif n - 1 < i:
                    end = i - 1
                else:
                    start = i + 1

        n = len(nums)

        # Find a median
        mid = nsmallest(nums, (n + 1) // 2)

        def mapIdx(i):
            """
            Index-rewiring
            """
            return (1 + 2 * i) % (n | 1)

        # 3-way-partition-to-wiggly in O(n) time with O(1) space
        i, j, k = 0, n - 1, 0
        while k <= j:
            if nums[mapIdx(k)] > mid:
                nums[mapIdx(k)], nums[mapIdx(
                    i)] = nums[mapIdx(i)], nums[mapIdx(k)]
                i += 1
                k += 1
            elif nums[mapIdx(k)] < mid:
                nums[mapIdx(k)], nums[mapIdx(
                    j)] = nums[mapIdx(j)], nums[mapIdx(k)]
                j -= 1
            else:
                k += 1

# Runtime: 276 ms, faster than 18.51% of Python3 online submissions for Wiggle Sort II.
# Memory Usage: 16.9 MB, less than 98.51% of Python3 online submissions for Wiggle Sort II.
