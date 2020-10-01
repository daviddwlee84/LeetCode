class RecentCounter:

    def __init__(self):
        self.count = 0
        self.requests = []

    def ping(self, t: int) -> int:
        in_range_count = 1
        i = 0
        for req in self.requests:
            if t - 3000 <= req <= t:
                in_range_count += 1
            elif req > t:
                break
            i += 1
        self.requests.insert(i, t)
        return in_range_count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# TLE
# https://leetcode.com/submissions/detail/403134818/testcase/
