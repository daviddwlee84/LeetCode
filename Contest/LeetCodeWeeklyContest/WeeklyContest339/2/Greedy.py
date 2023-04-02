from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)

        answer = []
        while True:
            temp = []
            all_zero = True
            for num in counter:
                if counter[num] == 0:
                    continue

                counter[num] -= 1
                temp.append(num)
                all_zero = False

            if temp:
                answer.append(temp)

            if all_zero:
                break

        return answer
