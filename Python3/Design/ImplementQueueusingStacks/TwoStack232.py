class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.auxiliary = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.data) == 0:
            # If queue is empty then the front will be the new input element
            self.front = x

        while len(self.data) != 0:
            # Pop out every element in data and store it in auxiliary
            self.auxiliary.append(self.data.pop())
        self.auxiliary.append(x) # Add new element to the top of auxilary

        while len(self.auxiliary) != 0:
            # Push all elements back to data
            self.data.append(self.auxiliary.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        rtn = self.data.pop() # The top element in data is the front element of queue
        if len(self.data) != 0:
            # Set front as the last element
            self.front = self.data[len(self.data)-1]
        
        return rtn

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.data):
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()