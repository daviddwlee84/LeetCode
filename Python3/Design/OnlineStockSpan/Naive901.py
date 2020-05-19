class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        less_equal_than = 1
        for p in reversed(self.data):
            if p <= price:
                less_equal_than += 1
            else:
                break
        self.data.append(price)
        return less_equal_than


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# TLE
