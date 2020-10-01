from collections import deque


class RecentCounter:
    """
    https://leetcode.com/problems/number-of-recent-calls/discuss/189239/JavaPython-3-Five-solutions%3A-TreeMap-TreeSet-ArrayList-Queue-Circular-List.
    https://leetcode.com/problems/number-of-recent-calls/solution/ => Iteration over Sliding Window
    """

    def __init__(self):
        # This queue only maintain item that is in range
        self.queue = deque()

    def ping(self, t: int) -> int:
        # step 1). append the current call
        self.queue.append(t)
        # step 2). invalidate the outdated pings
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Runtime: 316 ms, faster than 54.99% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 18.8 MB, less than 12.64% of Python3 online submissions for Number of Recent Calls.
