from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [self.isArithmetic(sorted(nums[left:right + 1]))for left, right in zip(l, r)]

    def isArithmetic(self, array: List[int]) -> bool:
        seq_diff = None
        for i in range(len(array) - 1):
            diff = array[i + 1] - array[i]
            if seq_diff is None:
                seq_diff = diff
            else:
                if seq_diff != diff:
                    return False
        return True

        # or we can do
        #
        # return all(
        #     array[i + 1] - array[i] == array[1] - array[0]
        #     for i in range(len(array) - 1)
        # )
