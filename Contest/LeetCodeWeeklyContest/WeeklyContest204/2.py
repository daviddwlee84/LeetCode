from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zero_idx = [i for i, num in enumerate(nums) if num == 0]
        max_len = 0
        if zero_idx:
            prev_idx = 0
            for idx in zero_idx:
                subarr = nums[prev_idx:idx]
                max_len = max(max_len, self.getMaxLenWithoutZero(subarr))
                prev_idx = idx + 1
            subarr = nums[prev_idx:]
            max_len = max(max_len, self.getMaxLenWithoutZero(subarr))

        else:
            max_len = self.getMaxLenWithoutZero(nums)

        return max_len

    def getMaxLenWithoutZero(self, nums: List[int]):
        # print(nums)
        if not nums:
            return 0

        neg_idx = [i for i, num in enumerate(nums) if num < 0]
        if len(neg_idx) % 2 == 0:
            return len(nums)

        # print(neg_idx)

        if len(neg_idx) == 1:
            # print(nums[neg_idx[0]], neg_idx[0], len(nums) - neg_idx[0] - 1)
            return max(neg_idx[0], len(nums) - neg_idx[0] - 1)

        # 0 1 2  3 4 5 6  7 8 9 10 11
        # 1 1 1 -1 1 1 1 -1 1 1 -1  1

        # print(nums[neg_idx[-2]], neg_idx[-2] + 1)
        # print(nums[neg_idx[1]], neg_idx[1], len(nums) - neg_idx[1])
        return max((neg_idx[-1] - 1) + 1, len(nums) - (neg_idx[0] + 1))


if __name__ == "__main__":
    print(Solution().getMaxLen([0, 1, -2, -3, -4]))
    print(Solution().getMaxLen([5, -20, -20, -39, -5, 0, 0, 0,
                                36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]))
    print(Solution().getMaxLen(
        [-16, 0, -14, 4, -13, -17, -19, -17, -21, -11, 12]))

# [5, -20, -20, -39, -5, 0, 0, 0, 36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]
# 8

# [-16, 0, -14, 4, -13, -17, -19, -17, -21, -11, 12]
# 8
