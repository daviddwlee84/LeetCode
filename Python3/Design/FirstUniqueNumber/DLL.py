from typing import List
from collections import deque


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.unique_num_list = deque()
        self.exist_at_least_one_set = set()
        for num in nums:
            if num not in self.exist_at_least_one_set:
                self.exist_at_least_one_set.add(num)
                self.unique_num_list.append(num)
            else:
                try:
                    self.unique_num_list.remove(num)
                except:
                    pass

    def showFirstUnique(self) -> int:
        if self.unique_num_list:
            return self.unique_num_list[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.exist_at_least_one_set:
            try:
                self.unique_num_list.remove(value)
            except:
                pass
        else:
            self.exist_at_least_one_set.add(value)
            self.unique_num_list.append(value)

# TLE


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
