class StockSpanner:
    """ https://leetcode.com/problems/online-stock-span/solution/ """

    def __init__(self):
        # a weighted stack of decreasing elements
        # the size of the weight will be the total number of elements skipped
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            # we don't need to store everything, we can just store each peak value
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Runtime: 556 ms, faster than 15.57 % of Python3 online submissions for Online Stock Span.
# fastest solution is the same = = (416 ms)
# Memory Usage: 18.5 MB, less than 100.00 % of Python3 online submissions for Online Stock Span.
