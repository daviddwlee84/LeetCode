from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = Queue()
        self.temp = Queue()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.top_element = x
        self.data.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.data.qsize() > 1:
            # get each element and push it to the temp queue until left only one element
            self.top_element = self.data.get()
            self.temp.put(self.top_element)
        
        rtn = self.data.get() # pop the last element as an answer
        self.data, self.temp = self.temp, self.data # swap temp queue to data queue
        return rtn


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.data.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()