class RecentCounter:

    def __init__(self):
        self.count = 0
        self.requests = []

    def ping(self, t: int) -> int:
        """
        It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
        """
        in_range_count = 0
        self.requests.append(t)
        i = 0
        for req in reversed(self.requests):
            if t - 3000 <= req <= t:
                in_range_count += 1
            elif req > t:
                break
            i += 1
        return in_range_count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# TLE
# https://leetcode.com/submissions/detail/403358531/testcase/
