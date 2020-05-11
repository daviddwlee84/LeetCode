from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.data = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        """ Binary Insert
        https://www.geeksforgeeks.org/binary-insertion-sort/
        https://nachtimwald.com/2018/01/18/binary-search-and-insert/
        """

        start = 0
        end = len(self.data) - 1

        while start <= end:
            mid = (start + end) // 2

            if self.data[mid] < val:
                start = mid + 1
            elif self.data[mid] > val:
                end = mid - 1
            else:
                start = mid
                break

        self.data.insert(start, val)

        return self.data[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Runtime: 164 ms, faster than 31.25% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.1 MB, less than 8.70% of Python3 online submissions for Kth Largest Element in a Stream.
