class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prods = [1] # Track the products from past to current number
        self.zeros = [0] # Track the number of zeros to current position

    def add(self, num: int) -> None:
        self.nums.append(num)
        if self.prods[-1] == 0:
            self.prods.append(num)
            self.zeros.append(self.zeros[-1] + 1)
        else:
            self.prods.append(self.prods[-1] * num)
            self.zeros.append(self.zeros[-1])

    def getProduct(self, k: int) -> int:
        if self.zeros[-1] - self.zeros[-k] > 0:
            return 0
        if self.prods[-k-1] == 0:
            prod = 1
        else:
            prod = self.prods[-k-1]
        return self.prods[-1] // prod


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
