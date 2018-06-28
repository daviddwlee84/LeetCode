class IllegalStateException(Exception):
    def __init__(self, expression):
        self.expression = expression

class BinaryHeap:
    def __init__(self, initialHeap = [], minHeapMode = True):
        self.__size = len(initialHeap)
        self.__items = initialHeap
        self.__minHeapMode = minHeapMode # Default is min heap
    
    def __repr__(self):
        return ("Min" if self.__minHeapMode else "Max") + " Heap with size: " + str(self.__size) + " and data: " + str(self.__items)

    def __getLeftChildIndex(self, parentIndex):
        return 2*parentIndex + 1
    def __getRightChildIndex(self, parentIndex):
        return 2*parentIndex + 2
    def __getParentIndex(self, childIndex):
        return (childIndex-1) // 2

    def __hasLeftChild(self, index):
        return self.__getLeftChildIndex(index) < self.__size
    def __hasRightChild(self, index):
        return self.__getRightChildIndex(index) < self.__size
    def __hasParent(self, index):
        return self.__getParentIndex(index) >= 0

    def __leftChild(self, index):
        return self.__items[self.__getLeftChildIndex(index)]
    def __rightChild(self, index):
        return self.__items[self.__getRightChildIndex(index)]
    def __parent(self, index):
        return self.__items[self.__getParentIndex(index)]

    def __swap(self, indexOne, indexTwo):
        self.__items[indexOne], self.__items[indexTwo] = self.__items[indexTwo], self.__items[indexOne] 
    
    ##### Main Public Methods

    # Return max/min
    def peek(self):
        if self.__size == 0:
            raise IllegalStateException('The size of the heap is zero.')
        return self.__items[0]
        
    # Pop max/min
    def poll(self):
        if self.__size == 0:
            raise IllegalStateException('The size of the heap is zero.')

        item = self.__items[0] # The max/min element
        self.__items[0] = self.__items[self.__size - 1] # Move the last element to the root
        del self.__items[self.__size - 1]
        self.__size -= 1
        self.__heapifyDown() # Rearrange the heap from the last node
        return item

    # Add new element
    def add(self, item):
        self.__items.append(item)
        self.__size += 1
        self.__heapifyUp() # Rearrange the heap from the root

    # Helper function for add()
    def __heapifyUp(self):
        index = self.__size - 1 # Start from the last element
        if self.__minHeapMode:
            # Do while 1. There is parent 2. The parent is bigger than the item
            while self.__hasParent(index) and self.__parent(index) > self.__items[index]:
                self.__swap(self.__getParentIndex(index), index) # Swap parent with current index
                index = self.__getParentIndex(index) # Go to parent index
        else:
            while self.__hasParent(index) and self.__parent(index) < self.__items[index]:
                self.__swap(self.__getParentIndex(index), index)
                index = self.__getParentIndex(index)
        
    # Helper function for poll()
    def __heapifyDown(self):
        index = 0 # Start from the root
        if self.__minHeapMode:
            while self.__hasLeftChild(index): # If there is no left child, it won't have a right child
                smallerChildIndex = self.__getLeftChildIndex(index) # First give the smaller child as left child
                if self.__hasRightChild(index) and self.__rightChild(index) < self.__leftChild(index):
                    # If there is right child and right chile is smaller than left child, then the smaller child is right child
                    smallerChildIndex = self.__getRightChildIndex(index)

                if self.__items[index] < self.__items[smallerChildIndex]: # Reach the right order
                    break
                else:
                    self.__swap(index, smallerChildIndex)
                
                index = smallerChildIndex
        else:
            while self.__hasLeftChild(index):
                biggerChildIndex = self.__getLeftChildIndex(index)
                if self.__hasRightChild(index) and self.__rightChild(index) > self.__leftChild(index):
                    biggerChildIndex = self.__getRightChildIndex(index)
                if self.__items[index] > self.__items[biggerChildIndex]:
                    break
                else:
                    self.__swap(index, biggerChildIndex)
                index = biggerChildIndex
