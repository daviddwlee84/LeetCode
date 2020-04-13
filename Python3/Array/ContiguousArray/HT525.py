from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_count = 0
        one_count = 0

        # current count for each number
        counts = [(0, 0)]
        # difference of one_count - zero_count
        diff_count_map = {0: 0}
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1

            counts.append((zero_count, one_count))
            if one_count - zero_count not in diff_count_map:
                diff_count_map[one_count - zero_count] = i + 1

        # for all count, find a complementary one, and update the max length
        max_length = 0
        for j, cnt in enumerate(counts):
            if cnt[1] - cnt[0] in diff_count_map:
                max_length = max(
                    max_length, j - diff_count_map[cnt[1] - cnt[0]])

        return max_length
