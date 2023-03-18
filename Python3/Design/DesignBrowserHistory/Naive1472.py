class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.max_future = 0

    def visit(self, url: str) -> None:
        # print('visited', url, self.history)
        self.curr += 1
        if len(self.history) > self.curr:
            self.history[self.curr] = url
            self.max_future = self.curr
        else:
            self.max_future = len(self.history)
            self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        # print('back to', self.history[self.curr], self.history)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.max_future)
        # print('forward to', self.history[self.curr], self.history)
        return self.history[self.curr]

# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
