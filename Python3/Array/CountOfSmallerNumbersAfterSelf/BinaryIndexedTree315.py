from typing import List
import heapq


class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def __lowbit(self, index: int):
        """
        To get the "lowest" bit with 1 (and also the following 0)
        index is a positive number
        `-index` is equivalent to `(~index + 1)`
        """
        return index & (-index)

    def update(self, index: int, delta: int):
        """
        Update a single node: plus `delta` for the position of `index`
        """
        while index <= self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index: int):
        """
        Search within an interval: how many number less equal than `index`
        Query is about the "prefix sum"
        """
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Edge cases
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        # Remove duplicate items
        unique_items = list(set(nums))
        heapq.heapify(unique_items)

        fenwick_tree = FenwickTree(len(unique_items))

        rank_map = {}
        rank = 1
        while unique_items:
            num = heapq.heappop(unique_items)
            rank_map[num] = rank
            rank += 1

        # Fill the answer from the back
        res = [None for _ in range(size)]
        for index in range(size - 1, -1, -1):
            # 1、Search for the order
            rank = rank_map[nums[index]]
            # 2、Update the rank in the tree
            fenwick_tree.update(rank, 1)
            # 3、How many items less equal than "current rank - 1"
            res[index] = fenwick_tree.query(rank - 1)
        return res

# Runtime: 3568 ms, faster than 44.37% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 35 MB, less than 53.72% of Python3 online submissions for Count of Smaller Numbers After Self.
