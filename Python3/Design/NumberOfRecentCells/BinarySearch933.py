import bisect


class RecentCounter:
    """
    https://leetcode.com/problems/number-of-recent-calls/discuss/189239/JavaPython-3-Five-solutions%3A-TreeMap-TreeSet-ArrayList-Queue-Circular-List.
    """

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return len(self.requests) - bisect.bisect_left(self.requests, t - 3000)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Runtime: 316 ms, faster than 54.99% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 19.2 MB, less than 5.10% of Python3 online submissions for Number of Recent Calls.
