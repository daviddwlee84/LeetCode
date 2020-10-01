class RecentCounter:
    """
    https://leetcode.com/problems/number-of-recent-calls/discuss/189239/JavaPython-3-Five-solutions%3A-TreeMap-TreeSet-ArrayList-Queue-Circular-List.
    """

    def __init__(self):
        self.time = [0] * 3001

    def ping(self, t: int) -> int:
        self.time[t % 3001] = t
        return sum([self.time[i] and self.time[i] >= t - 3000 for i in range(3001)])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# TLE
# https://leetcode.com/submissions/detail/403364226/testcase/
