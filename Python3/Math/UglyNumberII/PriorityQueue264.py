import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        last_num = None
        count = 0
        while count < n:
            num = heapq.heappop(heap)
            if num == last_num:
                # prevent from duplicate like 2 * 3 vs. 3 * 2
                continue

            heapq.heappush(heap, num * 2)
            heapq.heappush(heap, num * 3)
            heapq.heappush(heap, num * 5)

            last_num = num
            count += 1

        return num

# Runtime: 440 ms, faster than 20.52% of Python3 online submissions for Ugly Number II.
# Memory Usage: 14 MB, less than 35.63% of Python3 online submissions for Ugly Number II.
