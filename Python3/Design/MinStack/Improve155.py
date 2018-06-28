import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.data.append(self.min) # Store last min
            self.min = x # Update new min
        self.data.append(x) # Push new value

    def pop(self):
        """
        :rtype: void
        """
        if self.data.pop() == self.min: # If pop the min
            self.min = self.data.pop() # Pop another value (That's last min)

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()