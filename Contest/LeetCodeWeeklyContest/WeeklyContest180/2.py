class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)

    def pop(self) -> int:
        if self.data:
            return self.data.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.data))):
            self.data[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
