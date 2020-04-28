from typing import List
from collections import deque, defaultdict


class FirstUnique:
    """ https://www.youtube.com/watch?v=_y0FiPJXgZk """

    def __init__(self, nums: List[int]):
        self.occur = defaultdict(int)
        self.queue = deque()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and self.occur[self.queue[0]] >= 2:
            self.queue.popleft()

        if not self.queue:
            return -1

        return self.queue[0]

    def add(self, value: int) -> None:
        self.occur[value] += 1
        self.queue.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
