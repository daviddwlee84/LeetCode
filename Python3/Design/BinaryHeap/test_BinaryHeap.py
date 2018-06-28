import pytest
from BinaryHeap import BinaryHeap, IllegalStateException

def test_MinHeap():
    """
        10
       /  \
      15  20
     /  \
    17  25
    """
    emptyMinHeap = BinaryHeap()
    with pytest.raises(IllegalStateException) as e_info:
        emptyMinHeap.peek()
    assert str(e_info.value) == 'The size of the heap is zero.'

    minHeap1 = BinaryHeap([10, 15, 20, 17, 25])
    assert minHeap1.poll() == 10
    assert minHeap1.peek() == 15
    minHeap1.add(3)
    assert minHeap1.peek() == 3

def test_MaxHeap():
    """
        25
       /  \
      15  20
     /  \
    13  14
    """
    emptyMinHeap = BinaryHeap(minHeapMode=False)
    with pytest.raises(IllegalStateException) as e_info:
        emptyMinHeap.peek()
    assert str(e_info.value) == 'The size of the heap is zero.'

    minHeap1 = BinaryHeap([25, 15, 20, 13, 14], minHeapMode=False)
    assert minHeap1.poll() == 25
    assert minHeap1.peek() == 20
    minHeap1.add(22)
    assert minHeap1.peek() == 22