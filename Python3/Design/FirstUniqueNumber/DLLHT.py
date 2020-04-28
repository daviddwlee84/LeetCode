from typing import List
from llist import dllist

# since leetcode doesn't support llist, so haven't test yet


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.unique_num_list = dllist()
        self.hash_table = {}
        for num in nums:
            if num not in self.hash_table:
                list_node = self.unique_num_list.append(num)
                self.hash_table[num] = list_node
            else:
                if num in self.unique_num_list:
                    self.unique_num_list.remove(self.hash_table[num])
                # might left some deleted node in hash table
                # but won't affect the correctness
                # since we only need it to check whether a number appeared

    def showFirstUnique(self) -> int:
        if self.unique_num_list:
            return self.unique_num_list[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.hash_table:
            if value in self.unique_num_list:
                self.unique_num_list.remove(self.hash_table[value])
        else:
            list_node = self.unique_num_list.append(value)
            self.hash_table[value] = list_node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
