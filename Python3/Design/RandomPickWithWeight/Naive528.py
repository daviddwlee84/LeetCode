import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.cumulative = [0]
        for val in w:
            self.cumulative.append(self.cumulative[-1] + val)

    def pickIndex(self) -> int:
        val = random.randint(0, self.total-1)

        # TLE
        # for i in range(len(self.cumulative)-1):
        #     if self.cumulative[i] <= val < self.cumulative[i+1]:
        #         return i

        left, right = 0, len(self.cumulative)-1
        while left < right:
            mid = left + (right - left) // 2
            if self.cumulative[mid] <= val < self.cumulative[mid + 1]:
                return mid
            elif self.cumulative[mid] < val:
                left = mid + 1
            else:
                right = mid

        # return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
# [[[1, 3]], [], [], [], [], []]

def test(init_w: List[int], times: int):
    print(init_w, times)
    obj = Solution(init_w)
    print(obj.cumulative)
    for _ in range(times):
        print(obj.pickIndex())


if __name__ == "__main__":
    test([1], 1)
    test([1, 3], 5)
    test([3, 14, 1, 7], 10000)
