from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        nums = [1] * len(target)
        return self.backtracking(nums, target)

    def backtracking(self, temp: List[int], target: List[int]) -> bool:
        if temp == target:
            return True

        for tmp, tar in zip(temp, target):
            if tmp > tar:
                return False

        result = set()
        for i in range(len(temp)):
            s = sum(temp)
            newTemp = temp.copy()
            newTemp[i] = s
            result.add(self.backtracking(newTemp, target))

        return True if True in result else False

# TLE
