# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.next_temp = iterator.next() if iterator.hasNext() else None
        self.iterator = iterator
        self.reach_end = self.next_temp is None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_temp

    def next(self):
        """
        :rtype: int
        """
        to_return = self.next_temp
        self.next_temp = self.iterator.next() if self.iterator.hasNext() else None
        self.reach_end = self.next_temp is None
        return to_return

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.reach_end


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
