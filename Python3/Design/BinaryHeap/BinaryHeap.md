# Binary Heap (Min/Max Heap)

## Methods

### Public Methods

* peek() - O(1)
* poll() - O(logn) because of heapifyDown()
* add(x) - O(logn) because of heapifyUp()

### Important Private Methods

* heapifyUp() - O(logn)
* heapifyDown() - O(logn)

## Key

* Binary heap is uaually visualized as an complete binary tree.
* Complete binary tree usually represent as an array
    * A node with index i (index of the array start from 0)
        * left child index: i*2+1
        * right child index: i*2+2
        * parent index: (i+1)//2
* Difference between min and max heap is only when comparing numbers of parent and child

## Notes

* [Pytest Exception](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)
* [Pyton - User-defined Exception](https://docs.python.org/3.6/tutorial/errors.html#user-defined-exceptions)

## Resources

[HackerRank's Data Structures: Heaps](https://youtu.be/t0Cq6tVNRBA)