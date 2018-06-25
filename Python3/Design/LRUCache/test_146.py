from NaiveLRU146 import LRUCache as Naive
from OrderedDict146 import LRUCache as OrderedDict

def test_Naive():
    cache = Naive(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1         # returns 1
    cache.put(3, 3)                  # evicts key 2
    assert cache.get(2) == -1        # returns -1 (not found)
    cache.put(4, 4)                  # evicts key 1
    assert cache.get(1) == -1        # returns -1 (not found)
    assert cache.get(3) == 3         # returns 3
    assert cache.get(4) == 4         # returns 4

    cache = Naive(2)
    cache.put(2, 1)
    cache.put(2, 2)                  # update key 2
    assert cache.get(2) == 2         # returns 1
    cache.put(1, 1)                  
    cache.put(4, 1)                  # evicts key 2
    assert cache.get(2) == -1        # returns -1 (not found)

def test_OrderedDict():
    cache = OrderedDict(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1         # returns 1
    cache.put(3, 3)                  # evicts key 2
    assert cache.get(2) == -1        # returns -1 (not found)
    cache.put(4, 4)                  # evicts key 1
    assert cache.get(1) == -1        # returns -1 (not found)
    assert cache.get(3) == 3         # returns 3
    assert cache.get(4) == 4         # returns 4

    cache = OrderedDict(2)
    cache.put(2, 1)
    cache.put(2, 2)                  # update key 2
    assert cache.get(2) == 2         # returns 1
    cache.put(1, 1)                  
    cache.put(4, 1)                  # evicts key 2
    assert cache.get(2) == -1        # returns -1 (not found)
 