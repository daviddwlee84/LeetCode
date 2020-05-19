class StockSpanner:

    def __init__(self):
        self.data = []
        self.previous_days = []

    def next(self, price: int) -> int:
        less_equal_than = 1
        prev_position = 1
        while prev_position <= len(self.data):
            if self.data[-prev_position] <= price:
                less_equal_than += self.previous_days[-prev_position]
                prev_position += self.previous_days[-prev_position]
            else:
                # back track the value until found anything bigger
                break
        self.data.append(price)
        self.previous_days.append(less_equal_than)

        return less_equal_than

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Runtime: 912 ms, faster than 5.39% of Python3 online submissions for Online Stock Span.
# Memory Usage: 19.1 MB, less than 100.00% of Python3 online submissions for Online Stock Span.
