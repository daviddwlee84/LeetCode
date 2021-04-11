class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.elements = []

    def addElement(self, num: int) -> None:
        self.elements.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.elements) < self.m:
            return -1

        container = self.elements[-self.m:]
        container.sort()
        to_calc = container[self.k:-self.k]
        # return round(sum(to_calc) / len(to_calc))
        return sum(to_calc) // len(to_calc)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

# WA (solved, not round(), is int())
# ["MKAverage","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage"]
# [[6,1],[3],[1],[12],[5],[3],[4],[]]
# expect: [null,null,null,null,null,null,null,3]
