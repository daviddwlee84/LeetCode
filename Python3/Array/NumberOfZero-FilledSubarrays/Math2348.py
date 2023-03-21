from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        continuous_zeros = []
        temp_count = 0
        for num in nums:
            if num == 0:
                temp_count += 1
            else:
                continuous_zeros.append(temp_count)
                temp_count = 0
        continuous_zeros.append(temp_count)

        answer = 0
        for count in continuous_zeros:
            # e.g. 3 zeros => 3 + 2 + 1
            for i in range(count, 0, -1):
                answer += i

        return answer
