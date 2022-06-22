from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(start: int, end: int):
            pivot = nums[start]
            i, j = start, end

            # print(pivot, nums[start:end + 1], nums)
            while i < j:
                # skip all >= case and find first < case from back
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                # print('from back to front:',
                #       nums[i], nums[j], nums[start:end + 1])
                # skip all <= case and find first > case from front
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
                # print('from front to back:',
                #       nums[i], nums[j], nums[start:end + 1])

                # keep the same process until i & j intersect

            nums[i] = pivot

            # found the kth item, no need to "sort"
            if i == len(nums) - k:
                return nums[i]
            # the ending index is more than k (i.e. k is in the first half part)
            elif i > len(nums) - k:
                return quick_select(start, i - 1)
            # i.e. k is in the second half part
            else:
                return quick_select(i + 1, end)

        return quick_select(0, len(nums) - 1)


# Runtime: 1152 ms, faster than 13.59% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 19.7 MB, less than 8.61% of Python3 online submissions for Kth Largest Element in an Array.
