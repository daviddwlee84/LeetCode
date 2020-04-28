from typing import List
from collections import Counter  # double linked list


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.count = Counter(nums)

    def showFirstUnique(self) -> int:
        for item in self.data:
            if self.count[item] == 1:
                return item
        return -1

    def add(self, value: int) -> None:
        self.data.append(value)
        self.count[value] += 1


# TLE


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
